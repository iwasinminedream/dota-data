#!/usr/bin/env python3
"""
Read-only questions about the .so snapshots of an update, for the model writing the update report
(the only shell command it may run). Works on the snapshots named in ./so-query.json of the
analysis workspace and nothing else ("new" = the installed build; "old" = the build before, when
there is a snapshot of it); every answer is capped.

    so-query.py libs                              libraries of the snapshot(s), changed ones marked
    so-query.py strings old|new LIB REGEX         read-only-data strings matching REGEX
    so-query.py symbols old|new LIB REGEX         exported symbols (demangled) matching REGEX
    so-query.py xref old|new LIB STRING           code that references the exact string STRING,
                                                  with the instructions around each place
    so-query.py context old|new LIB STRING        the other strings the code around each reference
                                                  to STRING uses (what that code is about)
    so-query.py disasm old|new LIB ADDRESS [N]    N bytes (default 160, max 600) of code at ADDRESS

  functions (function-level comparison of the two builds, see funcdiff.py):
    so-query.py funcs LIB [REGEX]                 changed / added / removed functions of LIB with
                                                  their names, strings and what changed (REGEX
                                                  filters by name/strings/summary)
    so-query.py fdiff LIB ADDRESS [SKIP]          the whole diff of a changed function (its new or
                                                  old address), from line SKIP
    so-query.py func old|new LIB ADDRESS [SKIP]   the function containing ADDRESS: names, strings,
                                                  callers, callees and its code with strings and
                                                  constants resolved, from instruction SKIP
    so-query.py callers old|new LIB ADDRESS       functions that call / reference that function
    so-query.py vtable old|new LIB CLASS          the class's base classes and the vtable slots it
                                                  overrides (Lua callback names where known)

LIB is a file name such as libserver.so (game server; libclient.so: client and UI; libengine2.so:
engine). Addresses are virtual addresses (hex). Function names: "Class::OnSpellStart" is the
class's override of a Lua-visible callback, "Class::vfunc#N" an unnamed vtable slot N.
"""
import bisect
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('so_report', os.path.join(HERE, 'so-report.py'))
so_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(so_report)

spec = importlib.util.spec_from_file_location('funcdiff', os.path.join(HERE, 'funcdiff.py'))
funcdiff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(funcdiff)

MAX_LINES = 200


def fail(message):
    print(message)
    sys.exit(1)


def snapshots():
    try:
        with open('so-query.json') as f:
            return json.load(f)
    except OSError:
        fail('no so-query.json here: run from the analysis workspace')


def library(which, name):
    snaps = snapshots()
    if which not in ('old', 'new'):
        fail('first argument: old or new')
    if not snaps.get(which):
        fail(f'there is no {which} snapshot for this report')
    if not re.fullmatch(r'[\w.+-]+\.so[\w.]*', name):
        fail('LIB must be a file name like libserver.so')
    for sub in ('bin', 'dota-bin'):
        path = os.path.join(snaps[which], sub, name)
        if os.path.isfile(path):
            return path
    fail(f'{name} is not in the {which} snapshot')


def capped(lines):
    lines = list(lines)
    for line in lines[:MAX_LINES]:
        print(line)
    if len(lines) > MAX_LINES:
        print(f'... {len(lines) - MAX_LINES} more (narrow the pattern)')


def segments(data):
    phoff = int.from_bytes(data[0x20:0x28], 'little')
    phentsize = int.from_bytes(data[0x36:0x38], 'little')
    phnum = int.from_bytes(data[0x38:0x3a], 'little')
    out = []
    for i in range(phnum):
        p = phoff + i * phentsize
        if int.from_bytes(data[p:p + 4], 'little') != 1:  # PT_LOAD
            continue
        flags = int.from_bytes(data[p + 4:p + 8], 'little')
        off = int.from_bytes(data[p + 8:p + 16], 'little')
        vaddr = int.from_bytes(data[p + 16:p + 24], 'little')
        size = int.from_bytes(data[p + 32:p + 40], 'little')
        out.append((off, vaddr, size, flags))
    return out


def disasm(path, start, length):
    result = subprocess.run(['objdump', '-d', '--no-show-raw-insn', '-M', 'intel', '-C',
                             f'--start-address={start:#x}', f'--stop-address={start + length:#x}', path],
                            capture_output=True, text=True)
    # The nearest exported symbol objdump names (`<...@@Base+0x2ba888>`) is meaningless in a
    # stripped library: keep the bare addresses.
    return [re.sub(r' <.*@@Base\+0x[0-9a-f]+>$', '', l) for l in result.stdout.splitlines()
            if re.match(r'^\s+[0-9a-f]+:', l)]


def cmd_libs(_args):
    snaps = snapshots()

    def sums(path):
        with open(os.path.join(path, 'SHA256SUMS')) as f:
            return dict(reversed(line.split()) for line in f if line.strip())

    new = sums(snaps['new'])
    if not snaps.get('old'):
        print('only the new snapshot (no snapshot of the build before):')
        for rel in sorted(new):
            print(f'         {rel}')
        return
    old = sums(snaps['old'])
    for rel in sorted(set(old) | set(new)):
        state = 'added' if rel not in old else 'removed' if rel not in new else \
            'same' if old[rel] == new[rel] else 'changed'
        if state != 'same':
            print(f'{state:8} {rel}')


def cmd_strings(args):
    which, name, pattern = args
    rx = re.compile(pattern)
    capped(sorted(s for s in so_report.rodata_strings(library(which, name)) if rx.search(s)))


def cmd_symbols(args):
    which, name, pattern = args
    names = sorted(so_report.exports(library(which, name)))
    dem = so_report.demangle(names)
    rx = re.compile(pattern)
    capped(sorted(dem.get(n, n) for n in names if rx.search(dem.get(n, n)) or rx.search(n)))


def rip_leas(data, segs, start=None, end=None):
    """(instruction vaddr, target vaddr) of every `lea reg, [rip+rel32]` in code (or in [start, end))."""
    for s_off, vaddr, size, flags in segs:
        if not flags & 1:
            continue
        lo, hi = s_off, s_off + size - 7
        if start is not None:
            lo, hi = max(lo, start - vaddr + s_off), min(hi, end - vaddr + s_off)
        for i in range(lo, hi):
            if data[i] in (0x48, 0x4c) and data[i + 1] == 0x8d and data[i + 2] & 0xc7 == 0x05:
                insn = i - s_off + vaddr
                yield insn, insn + 7 + int.from_bytes(data[i + 3:i + 7], 'little', signed=True)


def string_at(data, segs, target):
    for s_off, vaddr, size, flags in segs:
        if flags & 1 or not vaddr <= target < vaddr + size:
            continue
        off = target - vaddr + s_off
        if off and data[off - 1] != 0:
            return None  # not the start of a string
        end = data.find(b'\0', off, off + 300)
        chunk = data[off:end] if end > off else b''
        if len(chunk) >= 3 and all(32 <= c < 127 for c in chunk):
            return chunk.decode()
    return None


def find_sites(which, name, text):
    path = library(which, name)
    data = open(path, 'rb').read()
    segs = segments(data)
    needle = b'\0' + text.encode() + b'\0'
    targets = set()
    for at in re.finditer(re.escape(needle), data):
        off = at.start() + 1
        for s_off, vaddr, size, _flags in segs:
            if s_off <= off < s_off + size:
                targets.add(off - s_off + vaddr)
    if not targets:
        fail(f'"{text}" is not a string in {name} ({which})')
    sites = [insn for insn, target in rip_leas(data, segs) if target in targets]
    return path, data, segs, targets, sites


def cmd_context(args):
    which, name, text = args
    _path, data, segs, targets, sites = find_sites(which, name, text)
    print(f'"{text}": referenced from {len(sites)} place(s); strings used by the code around each '
          '(±0x500 bytes, may reach into neighbouring functions):')
    for site in sites[:8]:
        seen = []
        for insn, target in rip_leas(data, segs, site - 0x500, site + 0x500):
            s = string_at(data, segs, target)
            if s and s != text and s not in seen:
                seen.append(s)
        print(f'--- {site:#x}')
        capped(f'  {s[:160]}' for s in seen[:60])
    if len(sites) > 8:
        print(f'... {len(sites) - 8} more places')


def cmd_xref(args):
    which, name, text = args
    path, _data, _segs, targets, sites = find_sites(which, name, text)
    print(f'string at {", ".join(hex(t) for t in sorted(targets))}; referenced from {len(sites)} place(s)')
    for site in sites[:8]:
        print(f'--- {site:#x}')
        capped(disasm(path, max(site - 40, 0), 100))
    if len(sites) > 8:
        print(f'... {len(sites) - 8} more places')


def cmd_disasm(args):
    which, name, address = args[:3]
    length = min(int(args[3]), 600) if len(args) > 3 else 160
    capped(disasm(library(which, name), int(address, 16), length))


def comparison(name):
    """The function-level comparison of LIB: precomputed by the report (func-diff/LIB.json)."""
    path = os.path.join('func-diff', f'{name}.json')
    if os.path.isfile(path):
        with open(path) as f:
            return json.load(f)
    old, new = library('old', name), library('new', name)
    if open(old, 'rb').read() == open(new, 'rb').read():
        fail(f'{name} is the same file in both builds: no function changed')
    fail(f'no function-level comparison of {name} (a third-party library): use strings/xref/disasm')


def table(which, name):
    t = funcdiff.load_table(library(which, name), build=False)
    if t is None:
        fail(f'no function table for {name} ({which}) yet')
    return t['funcs']


def containing(funcs, address):
    starts = [f[0] for f in funcs]
    k = bisect.bisect_right(starts, address) - 1
    if k < 0 or not funcs[k][0] <= address < funcs[k][1]:
        fail(f'{address:#x} is not inside a known function')
    return k


def label(f):
    return f"{f[0]:#x}" + (f" {f[5][0]}" if f[5] else '') + \
        (f" | {'; '.join(json.dumps(s[:60]) for s in f[4][:4])}" if f[4] else '')


def cmd_funcs(args):
    result = comparison(args[0])
    rx = re.compile(args[1]) if len(args) > 1 else None
    c = result['counts']
    print(f"{result['lib']}: functions {c['functions_old']} -> {c['functions_new']}; changed {c['changed']}, "
          f"added {c['added']}, removed {c['removed']}; copies of existing code (not listed without "
          f"REGEX) {c.get('copies', 0)}")
    lines = []
    for e in result['entries']:
        if e['kind'].startswith('copy_') and not rx:
            continue
        text = f"{funcdiff.KIND[e['kind']]}: {e['title']}"
        if e['kind'] == 'changed':
            text += f" (было {e['was']})"
        body = [text] + [f'    {s}' for s in e['summary']]
        if rx and not any(rx.search(b) for b in body):
            continue
        lines += body
    capped(lines)


def cmd_fdiff(args):
    name, address = args[0], int(args[1], 16)
    skip = int(args[2]) if len(args) > 2 else 0
    for e in comparison(name)['entries']:
        if e['kind'] in ('changed', 'callee') and address in (e.get('new'), e.get('old')):
            break
    else:
        fail(f'{address:#x} is not a changed function of {name} (see: so-query.py funcs {name})')
    old_path, new_path = library('old', name), library('new', name)
    old, new = table('old', name), table('new', name)
    o, n = old[containing(old, e['old'])], new[containing(new, e['new'])]
    a = funcdiff.function_tokens(old_path, o[0], o[1])
    b = funcdiff.function_tokens(new_path, n[0], n[1])
    diff = [d[:220] for d in funcdiff.difflib.unified_diff(a, b, lineterm='', n=3)
            if not d.startswith(('---', '+++'))]
    print(f"{e['title']}\nбыло {o[0]:#x}, стало {n[0]:#x}; " + '; '.join(e['summary']))
    print(f'diff lines {skip}..{min(skip + 400, len(diff))} of {len(diff)}')
    for line in diff[skip:skip + 400]:
        print(line)


def cmd_func(args):
    which, name, address = args[:3]
    skip = int(args[3]) if len(args) > 3 else 0
    path = library(which, name)
    funcs = table(which, name)
    k = containing(funcs, int(address, 16))
    f = funcs[k]
    print(f'function {f[0]:#x}..{f[1]:#x} ({f[1] - f[0]} bytes, {f[2]} instructions)')
    print('names: ' + (', '.join(f[5]) if f[5] else '-'))
    print('strings: ' + ('; '.join(json.dumps(s) for s in f[4]) if f[4] else '-'))
    by_start = {g[0]: g for g in funcs}
    callers = [g for g in funcs if f[0] in g[6]]
    print(f'callers ({len(callers)}): ' + ('; '.join(label(g) for g in callers[:6]) or '-'))
    callees = [by_start[t] for t in dict.fromkeys(f[6]) if t in by_start]
    print(f'callees ({len(callees)}): ' + ('; '.join(label(g) for g in callees[:10]) or '-'))
    img = funcdiff.Image(path)
    md = funcdiff.capstone.Cs(funcdiff.capstone.CS_ARCH_X86, funcdiff.capstone.CS_MODE_64)
    md.skipdata = True
    off = img.offset(f[0])
    insns = [i for i in md.disasm_lite(img.data[off:off + f[1] - f[0]], f[0]) if i[2] != 'int3']
    lines = []
    for a, size, mnemonic, op in insns[skip:skip + 300]:
        refs = []
        text = funcdiff.normalise(img, a, size, mnemonic, op, f[0], f[1], [], refs)
        if text.endswith((' F', ' L')) or refs:
            target = refs[-1] if refs else int(op, 16)
            text = text[:-1] + f'{target:#x}' if text.endswith((' F', ' L')) else text
            if target in by_start and by_start[target][5]:
                text += f'  ; {by_start[target][5][0]}'
        lines.append(f'  {a:x}: {text}')
    print(f'code, instructions {skip}..{skip + len(lines)} of {len(insns)}:')
    for line in lines:
        print(line)


def cmd_callers(args):
    which, name, address = args
    funcs = table(which, name)
    f = funcs[containing(funcs, int(address, 16))]
    callers = [g for g in funcs if f[0] in g[6]]
    print(f'{label(f)}: {len(callers)} caller(s)')
    capped(label(g) for g in callers)


def cmd_vtable(args):
    which, name, cls = args
    path = library(which, name)
    funcs = table(which, name)
    classes = funcdiff.classes(funcdiff.Image(path))
    if cls not in classes:
        fail(f'no class {cls} with RTTI in {name}')
    chain = funcdiff.ancestors(cls, classes)
    print('class chain: ' + ' -> '.join(chain))
    slots = funcdiff.slot_names(classes, {g[0]: g[4] for g in funcs})
    known = {}
    for anc in chain:
        for n, nm in slots.get(anc, {}).items():
            known.setdefault(n, nm)
    # the inherited function of a slot: the base's, or the most common one among the base's subclasses
    base = chain[1] if len(chain) > 1 else None
    siblings = [v['vtable'] for v in classes.values() if base and v['base'] == base]
    usual = {}
    for n in range(len(classes[cls]['vtable'])):
        votes = funcdiff.collections.Counter(v[n] for v in siblings if len(v) > n)
        usual[n] = votes.most_common(1)[0][0] if votes else None
    if base and classes[base]['vtable']:
        usual.update({n: fn for n, fn in enumerate(classes[base]['vtable']) if fn})
    by_start = {g[0]: g for g in funcs}
    lines = []
    for n, fn in enumerate(classes[cls]['vtable']):
        if usual.get(n) == fn:
            continue
        g = by_start.get(fn)
        strings = '; '.join(json.dumps(s[:60]) for s in g[4][:4]) if g and g[4] else ''
        lines.append(f"  #{n:<4} {known.get(n, ''):32} {fn:#x} {(g[1] - g[0]) if g else '?'} bytes  {strings}")
    print(f"{len(classes[cls]['vtable'])} slots; overridden here (not the inherited function): {len(lines)}")
    capped(lines)


COMMANDS = {'libs': (cmd_libs, 0), 'strings': (cmd_strings, 3), 'symbols': (cmd_symbols, 3),
            'xref': (cmd_xref, 3), 'context': (cmd_context, 3), 'disasm': (cmd_disasm, 3),
            'funcs': (cmd_funcs, 1), 'fdiff': (cmd_fdiff, 2), 'func': (cmd_func, 3),
            'callers': (cmd_callers, 3), 'vtable': (cmd_vtable, 3)}
OPTIONAL = {'disasm', 'funcs', 'fdiff', 'func'}  # one more optional argument


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        return 1
    fn, nargs = COMMANDS[sys.argv[1]]
    args = sys.argv[2:]
    if len(args) < nargs or (sys.argv[1] not in OPTIONAL and len(args) > nargs) or len(args) > nargs + 1:
        print(__doc__)
        return 1
    try:
        fn(args)
    except re.error as e:
        fail(f'bad regex: {e}')
    except ValueError as e:
        fail(f'bad number: {e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
