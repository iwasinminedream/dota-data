"""Native modifiers of Dota 2 and the modifier functions they implement, read offline from server.dll.

    python extract.py [--dll server.dll] [--out modifiers.json]

For every native modifier (a class derived from CDOTA_Buff with a name): the modifier functions its
DeclareFunctions registers (properties and events), and for every property the value its handler returns,
as a formula over the ability's special values, the modifier's creation parameters, the stack count and
calls on the caster / parent / ability. See README.md next to this file.
"""
import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from expr import C, TRUE, base_off, lnot, walk  # noqa: E402
from knowledge import Knowledge  # noqa: E402
from modifiers import OUT, PARAMS, THIS, Modifiers, decision, lua_callback_names, read_enum  # noqa: E402
from pe import Image  # noqa: E402
from render import Renderer  # noqa: E402
from script_api import script_classes  # noqa: E402

DEFAULT_DLL = os.path.join(r"C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta", "game", "dota", "bin",
                           "win64", "server.dll")
WRITER_SLOTS = {"OnCreated", "OnRefresh", "OnIntervalThink", "OnStackCountChanged", "OnRemoved", "OnDestroy"}


def analyse(path, enums_path=None, log=print):
    t0 = time.time()
    im = Image(path)
    functions = read_enum(im, "MODIFIER_PROPERTY_PREATTACK_BONUS_DAMAGE", "MODIFIER_")
    states = read_enum(im, "MODIFIER_STATE_ROOTED", "MODIFIER_STATE_")
    lua_names = lua_callback_names(im)
    classes = script_classes(im, path)
    vts = im.vtables()
    by_name = {}
    for vt, (n, col) in vts.items():
        by_name.setdefault(n, vt)
    kb = Knowledge(im, classes, lambda cpp: by_name.get(".?AV%s@@" % cpp))
    log("bindings: %d classes, %d templates, %d special-value getters (%.0f s)" % (
        len(classes), sum(len(v) for v in kb.templates.values()), len(kb.special_getters), time.time() - t0))
    last = next((v for v, n in functions.items() if n == "MODIFIER_FUNCTION_LAST"), None)
    if last is None:
        raise RuntimeError("MODIFIER_FUNCTION_LAST not found in the modifierfunction table")
    mods = Modifiers(im, kb.named, last)
    mods.ex.type_byte = kb.type_byte
    enums = None
    if enums_path and os.path.exists(enums_path):
        with open(enums_path, encoding="utf-8") as f:
            enums = json.load(f)
    renderer = Renderer(kb, functions, states, mods.fields_from, enums)

    result = {}
    stats = {"modifiers": 0, "functions": 0}
    for vt, cname in sorted(mods.classes.items(), key=lambda x: x[1]):
        name = mods.name_of(vt)
        if not name:
            continue
        declared = mods.declared(vt)
        # fields: every store an overridden virtual function or a handler makes to the modifier's fields
        writers = []
        for slot, f in mods.overridden(vt):
            label = mods.slot_names.get(slot, "vfunc_%d" % slot)
            done, _ = mods.run(f, vt, rdx=('sym', 'kv') if label == "OnCreated" or label == "OnRefresh"
                               else ('sym', 'arg1'))
            writers.append((label, mods.writes(done, mods.fields_from)))
        handlers = {}
        for P, (h, adj) in sorted(declared.items()):
            rcx = THIS if not adj else ('op', 'add', THIS, C(adj))
            done, aborted = mods.run(h, vt, rcx=rcx, rdx=OUT, r8=PARAMS)
            handlers[P] = (h, done, aborted)
            fname = functions.get(P, "")
            writers.append((lua_names.get(P) or fname, mods.writes(done, mods.fields_from)))
        entry = renderer.modifier(name, cname, mods.bases[vt], declared, handlers, writers, lua_names)
        checked = mods.check_state(vt)
        if checked is not None:
            states = renderer.check_states(checked[0]) if checked[0] else None
            if states:
                entry["states"] = states
                stats["states"] = stats.get("states", 0) + 1
            elif states is None:
                entry["states_unresolved"] = True     # it sets states, but from data the analysis cannot read
        result[name] = entry
        stats["modifiers"] += 1
        stats["functions"] += len(declared)
    log("modifiers: %d, declared functions: %d, with states: %d (%.0f s)" % (
        stats["modifiers"], stats["functions"], stats.get("states", 0), time.time() - t0))
    return result, renderer.summary()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dll", default=os.environ.get("DOTA_SERVER_BINARY") or DEFAULT_DLL)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "native_modifiers.json"))
    ap.add_argument("--version", default=None, help="game version the DLL belongs to (ClientVersion)")
    ap.add_argument("--enums", default=os.path.join(HERE, "..", "..", "files", "vscripts", "enums.json"),
                    help="enums.json of dota-data: names for flags in the formulas")
    args = ap.parse_args()
    data, summary = analyse(args.dll, args.enums)
    out = {"version": args.version, "modifiers": dict(sorted(data.items()))}
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("functions: " + summary)


if __name__ == "__main__":
    main()
