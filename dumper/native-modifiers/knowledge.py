"""Names for what the executor sees, taken from the Lua bindings of server.dll.

Every script method's native implementation is executed symbolically with `obj` as its object. When the
result is a plain function of the object (a field, a bit of a field, the entity behind a handle field, a
call of an internal function or a virtual function of the object), that expression becomes a template:
the same expression inside a modifier handler is the same method call, e.g.
    bit(ld(obj + 0xd18), 1)          ->  obj:IsRangedAttacker()
    ld(obj + 0x84)  (on a modifier)  ->  self:GetStackCount()
    ent(ld(obj + 0x74)) (modifier)   ->  self:GetParent()
The special-value getters (GetSpecialValueFor and its int/bool siblings, which the game code calls
directly) are recognised by the lookup function they all start with.
"""
import collections
import re

from expr import ZERO, base_off, substitute, walk
from symexec import Executor

WILD = ('sym', 'obj')
ARG_SYMS = {('sym', 'a1'): 0, ('sym', 'a2'): 1, ('sym', 'a3'): 2}
# classes whose methods can name things on an object of a kind
KIND_CLASSES = {
    'modifier': ["CDOTA_Buff"],
    'npc': ["CDOTA_BaseNPC_Hero", "CDOTA_BaseNPC", "CBaseFlex", "CBaseAnimatingActivity", "CBaseModelEntity",
            "CBaseEntity", "CEntityInstance"],
    'ability': ["CDOTA_Item", "CDOTABaseAbility", "CBaseEntity", "CEntityInstance"],
}
KIND_CLASSES['any'] = KIND_CLASSES['npc'] + ["CDOTA_Item", "CDOTABaseAbility", "CDOTA_Buff"]
# singletons whose methods read globals and ignore the object: rendered as Class:Method()
CMP_BYTE_3 = re.compile(rb"\x80[\xb8-\xbf](....)\x03", re.S)   # cmp byte ptr [reg + disp32], 3
GLOBAL_CLASSES = {"CDOTAGameRules": "GameRules", "CDOTA_PlayerResource": "PlayerResource", "_G": None}


def strip_script_handle(e):
    """ld(ld(E + 0x10) + 0x28): an entity's script instance (what a binding returns) -> E."""
    if e[0] == 'ld' and e[2] == 8:
        b, o = base_off(e[1])
        if o == 0x28 and b is not None and b[0] == 'ld' and b[2] == 8:
            b2, o2 = base_off(b[1])
            if o2 == 0x10 and b2 is not None:
                return b2
    return e


def head(e):
    """Index key of an expression: its tag and name plus the first field offset down its left side."""
    t = e[0]
    if t == 'ld':
        b, o = base_off(e[1])
        return ('ld', o, e[2])
    if t == 'bit':
        x = e[1]
        if x[0] == 'ld':
            b, o = base_off(x[1])
            return ('bit', o + e[2] // 8, e[2] % 8)
        return ('bit', None, e[2])
    if t == 'ent':
        return ('ent', head(e[1]))
    if t == 'call':
        n = e[1]
        if isinstance(n, tuple) and n[0] == 'vcall':
            return ('vcall', n[2])
        return ('call', n)
    if t in ('op', 'un', 'cmp'):
        x = e[2]
        while x[0] in ('op', 'un', 'cmp'):
            x = x[2]
        return (t, e[1], head(x) if x[0] in ('ld', 'bit') else x[0])
    return (t,)


def norm_bit(e):
    """bit(ld(base + off, size), k) -> (base, byte offset, bit in byte)."""
    x = e[1]
    if x[0] != 'ld':
        return None
    b, o = base_off(x[1])
    return b, o + e[2] // 8, e[2] % 8


def unify(t, e, env):
    """Match template t against expression e, binding WILD (the object) and the method arguments."""
    if t == WILD:
        if 'obj' in env:
            return env['obj'] == e
        env['obj'] = e
        return True
    if t[0] == 'sym':
        if t in ARG_SYMS:
            k = ARG_SYMS[t]
            if k in env:
                return env[k] == e
            env[k] = e
            return True
        return True             # clobbered / undefined registers match anything
    if t[0] == 'bit' and e[0] == 'bit':
        a, b = norm_bit(t), norm_bit(e)
        if a is None or b is None:
            return False
        return a[1:] == b[1:] and unify(a[0], b[0], env)
    if t[0] != e[0] or len(t) != len(e):
        return False
    if t[0] == 'ld':
        tb, to = base_off(t[1])
        eb, eo = base_off(e[1])
        if to != eo or (tb is None) != (eb is None):
            return False
        return tb is None or unify(tb, eb, env)
    for x, y in zip(t[1:], e[1:]):
        if isinstance(x, tuple) and x and isinstance(x[0], str):
            if not isinstance(y, tuple) or not y or not isinstance(y[0], str) or not unify(x, y, env):
                return False
        elif isinstance(x, tuple):
            if not isinstance(y, tuple) or len(x) != len(y):
                return False
            for xx, yy in zip(x, y):
                if not unify(xx, yy, env):
                    return False
        elif x != y:
            return False
    return True


def size_of(e):
    return sum(1 for _ in walk(e))


class Knowledge:
    def __init__(self, im, classes, vtable_of):
        """classes: script_api.script_classes(); vtable_of(cpp class name) -> vtable rva or None."""
        self.im = im
        self.classes = classes
        self.ex = Executor(im, max_paths=24, max_steps=3000)
        self.templates = collections.defaultdict(list)    # head -> [(size, class, method, template, nargs)]
        self.vslots = {}                                  # (class, slot) -> method
        self.special_getters = set()
        self.find_special_getters()
        self.dynamic_cast = self.find_dynamic_cast()
        self.type_byte = self.find_type_byte()
        self.ex.type_byte = self.type_byte
        self.named = {f: self.special_handler for f in self.special_getters}
        if self.dynamic_cast is not None:
            self.named[self.dynamic_cast] = self.identity     # dynamic_cast: assume it succeeds
        self.ex.named = self.named
        for cname, c in classes.items():
            vt = vtable_of(c["cpp"]) if c.get("cpp") else None
            for m in c["methods"]:
                self.add_method(cname, m, vt)
        self.derive_game_time()
        for k in self.templates:
            self.templates[k].sort(key=lambda x: -x[0])
        # virtual functions the Lua classes forward to Lua callbacks of the same name
        for lua, base in (("CDOTA_Ability_Lua", "CDOTABaseAbility"), ("CDOTA_Item_Lua", "CDOTA_Item"),
                          ("CDOTA_Modifier_Lua", "CDOTA_Buff")):
            lvt, bvt = vtable_of(lua), vtable_of(base)
            if lvt is not None and bvt is not None:
                for slot, name in lua_slot_names(im, lvt, bvt).items():
                    self.vslots.setdefault((base, slot), name)
        self.find_params()
        self.modifier_manager = self.find_modifier_manager()

    def derive_game_time(self):
        """CDOTA_Buff:GetElapsedTime() = current game time - GetCreationTime(): its left side, which reads
        only globals, is GameRules:GetGameTime()."""
        for lst in list(self.templates.values()):
            for size, cname, mname, t, nargs in lst:
                if cname == "CDOTA_Buff" and mname == "GetElapsedTime" and t[0] == 'op' and t[1] == 'fsub':
                    x = t[2]
                    if not any(y == WILD for y in walk(x)) and any(y[0] == 'g' for y in walk(x)):
                        self.templates[head(x)].append((size_of(x), "CDOTAGameRules", "GetGameTime", x, 0))
                        return

    def find_dynamic_cast(self):
        """__RTDynamicCast (statically linked CRT): the function called most often with RTTI type
        descriptors in r8 (source type) and r9 (target type)."""
        im = self.im
        counts = {}
        for a, n in im.code_sections():
            blob = im.mem[a:a + n]
            i = blob.find(b"\x4c\x8d\x0d")              # lea r9, [rip + X]
            while i >= 0:
                p = a + i
                t = p + 7 + im.i32(p + 3)
                if 0 <= t < im.size - 24 and im.mem[t + 16:t + 20] == b".?AV":
                    k = im.mem.find(b"\xe8", p + 7, p + 0x30)
                    if k > 0:
                        target = k + 5 + im.i32(k + 1)
                        counts[target] = counts.get(target, 0) + 1
                i = blob.find(b"\x4c\x8d\x0d", i + 1)
        if not counts:
            return None
        best = max(counts, key=counts.get)
        return best if counts[best] >= 50 else None

    def find_type_byte(self):
        """The entity class byte: `cmp byte ptr [entity + X], 3` (is it an NPC) is by far the most common
        comparison of a byte field with a constant; checks of it are inlined casts."""
        import re
        import struct
        counts = {}
        for a, n in self.im.code_sections():
            for m in re.finditer(CMP_BYTE_3, self.im.mem[a:a + n]):
                d = struct.unpack("<i", m.group(1))[0]
                counts[d] = counts.get(d, 0) + 1
        if not counts:
            return None
        best = max(counts, key=counts.get)
        return best if counts[best] >= 1000 else None

    def find_modifier_manager(self):
        """Offset of the modifier manager in an NPC: FindModifierByName calls the lookup with
        rcx = npc + offset and the name argument."""
        impl = self.method_impl("CDOTA_BaseNPC", "FindModifierByName")
        if impl is None:
            return None
        found = []

        def hook(ex, st, name, args):
            if ('sym', 'a1') in args and args[0][0] == 'op':
                b, o = base_off(args[0])
                if b == WILD:
                    found.append(o)

        ex = Executor(self.im, max_paths=8, max_steps=2000, max_depth=0)
        ex.on_opaque = hook
        ex.run(impl, regs={"rcx": WILD, "rdx": ('sym', 'a1'), "r8": ('sym', 'a2'), "r9": ('sym', 'a3')})
        return found[0] if found else None

    @staticmethod
    def identity(ex, st):
        v = ex.rget(st, "rcx")
        return v, v

    def vslot_name(self, kind, slot):
        """Method name of virtual slot `slot` on an object of a kind (unique among the kind's classes)."""
        names = []
        for cname in KIND_CLASSES.get(kind, KIND_CLASSES['any']):
            n = self.vslots.get((cname, slot))
            if n and n not in names:
                names.append(n)
        if len(names) == 1 or (names and kind != 'any'):
            return names[0]
        return None

    # --- special values
    def method_impl(self, cname, mname):
        c = self.classes.get(cname)
        for m in (c["methods"] if c else []):
            if m["name"] == mname:
                return m["impl"]
        return None

    def find_special_getters(self):
        """GetSpecialValueFor's implementation calls the float getter. Every getter variant (float, int,
        bool) starts the same way: the current level when -1 was passed, then the value lookup by name;
        every function that starts with calls of those two is a special-value getter."""
        impl = self.method_impl("CDOTABaseAbility", "GetSpecialValueFor")
        if impl is None:
            return
        im = self.im
        calls = direct_calls(im, impl, 0x40)
        if not calls:
            return
        getter = calls[0]
        prologue = direct_calls(im, getter, 0x60)[:2]
        if len(prologue) < 2:
            return
        lookup = prologue[-1]
        self.special_getters.add(getter)
        for a, n in im.code_sections():
            blob = im.mem[a:a + n]
            i = blob.find(b"\xe8")
            while i >= 0:
                p = a + i
                if i + 5 <= len(blob) and p + 5 + im.i32(p + 1) == lookup:
                    f = im.primary_function(p)
                    if f is not None and p - f < 0x60 and direct_calls(im, f, 0x60)[:2] == prologue:
                        self.special_getters.add(f)
                i = blob.find(b"\xe8", i + 1)

    def find_params(self):
        """{(offset, size): key} of the params struct of modifier functions: the function that converts it
        to the Lua table reads every field and sets it under its key (IScriptVM SetValue, a virtual call
        with the key string in r8 and the value as a script variant {value, +8 type} in r9)."""
        im = self.im
        refs = []
        for s in im.strings("original_damage"):
            refs += im.code_refs(s)
        conv = None
        for r in refs:
            f = im.primary_function(r)
            if f is not None and any(im.code_refs(x) and im.primary_function(im.code_refs(x)[0]) == f
                                     for x in im.strings("report_max")):
                conv = f
                break
        self.params = {}
        self.param_kinds = {}
        if conv is None:
            return
        ex = Executor(im, max_paths=400, max_steps=20000)
        found = []

        def hook(ex, st, name, args):
            if isinstance(name, tuple) and name[0] == 'vcall' and args[2][0] == 'c':
                key = im.text(args[2][1] - im.base, 80)
                if key:
                    typ = ex.load(st, ('op', 'add', args[3], ('c', 8)), 1)
                    t = typ[1] if typ[0] == 'c' else None
                    val = ex.load(st, args[3], {1: 4, 5: 4, 6: 1}.get(t, 8))
                    found.append((key, t, strip_script_handle(val)))

        ex.on_opaque = hook
        ex.run(conv, regs={"rcx": ('sym', 'p'), "rdx": ('sym', 'a1'), "r8": ('sym', 'a2'), "r9": ('sym', 'a3')})
        for key, t, val in found:
            ent = val[0] == 'ent'
            x = val[1] if ent else val
            if x[0] != 'ld':
                continue
            b, o = base_off(x[1])
            if b != ('sym', 'p'):
                continue
            if ent:
                self.params.setdefault(('ent', o), key)
                self.param_kinds[key] = 'ability' if key in ('ability', 'inflictor') else 'npc'
            else:
                self.params.setdefault((o, x[2]), key)

    @staticmethod
    def special_handler(ex, st):
        """A special-value getter call: (ability, name, level = -1 for the current level, ...)."""
        name = ex.rget(st, "rdx")
        s = ex.im.text(name[1] - ex.im.base, 200) if name[0] == 'c' else None
        level = ex.rget(st, "r8d")
        e = ('call', 'special', (ex.rget(st, "rcx"), ('s', s) if s is not None else name, level))
        return e, e

    # --- templates
    def add_method(self, cname, m, vt):
        impl = m.get("impl")
        if impl is None:
            return
        slot = m.get("slot")
        targets = []
        if slot is not None:
            self.vslots[(cname, slot)] = m["name"]
            if vt is not None:
                f = self.im.va(self.im.q(vt + 8 * slot))
                if f is not None:
                    targets.append(f)
        else:
            targets.append(impl)
        for f in targets:
            try:
                if cname == "_G":       # a global function: no object, the arguments start in rcx
                    regs = {"rcx": ('sym', 'a1'), "rdx": ('sym', 'a2'), "r8": ('sym', 'a3'), "r9": ('sym', 'a4')}
                    xmm = {"xmm0": ('sym', 'a1'), "xmm1": ('sym', 'a2'), "xmm2": ('sym', 'a3')}
                else:
                    regs = {"rcx": WILD, "rdx": ('sym', 'a1'), "r8": ('sym', 'a2'), "r9": ('sym', 'a3')}
                    xmm = {"xmm1": ('sym', 'a1'), "xmm2": ('sym', 'a2')}
                done, ab = self.ex.run(f, regs=regs, xmm=xmm)
            except Exception:
                continue
            if len(done) != 1 or ab:
                continue
            s = done[0]
            # the binding's return type: 1 (float) and 2 (double) come back in xmm0
            results = (s.xmm.get("xmm0"),) if m.get("ret") in (1, 2) else (s.regs.get("rax"), s.xmm.get("xmm0"))
            for v in results:
                if v is None:
                    continue
                v = strip_script_handle(v)
                if v[0] == 'un' and v[1] in ('b2i', 'lo8', 'lo32', 'zx8'):
                    v = v[2]
                if not self.useful(v, cname in GLOBAL_CLASSES):
                    continue
                if not m.get("params"):
                    # registers a method without parameters reads are not arguments: match anything
                    v = substitute(v, lambda x: ('sym', 'clobber') if x in ARG_SYMS else None)
                nargs = sum(1 for x in walk(v) if x in ARG_SYMS)
                self.templates[head(v)].append((size_of(v), cname, m["name"], v, nargs))
                break

    @staticmethod
    def useful(v, global_class=False):
        """A template must be a function of the object (or, for a singleton, of globals only)."""
        if v[0] in ('c', 'f', 'sym', 's'):
            return False
        has_obj = any(x == WILD for x in walk(v))
        has_global = any(x[0] == 'g' for x in walk(v))
        for x in walk(v):
            if x[0] == 'sym' and x[1] in ('undef', 'opaque', 'partial', 'signext'):
                return False
        if has_obj:
            return True
        return global_class and has_global and v[0] in ('ld', 'op', 'un', 'cmp', 'bit')

    def match(self, e, kind):
        """(class, method, object, args) of the best template matching e, or None."""
        cands = self.templates.get(head(e))
        if not cands:
            return None
        allowed = KIND_CLASSES.get(kind, KIND_CLASSES['any']) + list(GLOBAL_CLASSES)
        best = None
        for size, cname, mname, t, nargs in cands:
            if cname not in allowed:
                continue
            env = {}
            if unify(t, e, env) and ('obj' in env or cname in GLOBAL_CLASSES):
                rank = (size, -allowed.index(cname))
                if best is None or rank > best[0]:
                    best = (rank, cname, mname, env)
        if best is None:
            return None
        _, cname, mname, env = best
        args = [env[k] for k in sorted(k for k in env if k != 'obj')]
        return cname, mname, env.get('obj'), args


def lua_slot_names(im, lua_vt, base_vt):
    """{slot: Lua callback name} of the virtual functions a Lua class overrides to call Lua by name
    (the first identifier-like string the override references)."""
    out = {}
    base = im.vfuncs(base_vt)
    for i, f in enumerate(im.vfuncs(lua_vt)):
        if i >= len(base) or f == base[i]:
            continue
        end = (im.func_of(f) or (f, f + 0x200))[1]
        for k in range(f, min(end, f + 0x400)):
            if im.mem[k] in (0x48, 0x4c) and im.mem[k + 1] == 0x8d and im.mem[k + 2] & 0xC7 == 0x05:
                s = im.text(k + 7 + im.i32(k + 3), 80)
                if s and re.fullmatch(r"(Get|Is|On|Has|Can|Should|Allow|Spell|Cast|Requires|Process)[A-Za-z]+", s):
                    out[i] = s
                    break
    return out


def direct_calls(im, f, limit):
    """Targets of the direct calls in the first `limit` bytes of a function, in order."""
    from capstone import CS_ARCH_X86, CS_MODE_64, Cs
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    out = []
    for ins in md.disasm_lite(im.mem[f:f + limit], f):
        if ins[2] == "call" and ins[3].startswith("0x"):
            out.append(int(ins[3], 16))
        if ins[2] in ("ret", "int3"):
            break
    return out
