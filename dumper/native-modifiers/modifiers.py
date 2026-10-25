"""Native modifiers of server.dll: their classes, declared modifier functions, fields and handler paths.

A native modifier is a class derived from CDOTA_Buff. Its DeclareFunctions (a virtual function) stores a
handler for every modifier function it implements into the handler table of the object:
    [this + table + 16 * P] = {handler, this adjustment}     (P = modifierfunction value; table = 0xE0
                                                              in 6967, read from the Lua modifier's loop)
The engine calls a property handler as handler(this, &result, &params) and reads the result struct:
    +0 int kind (1 = number, 2 = string), +4 float value, +8 string pointer.
Values a handler returns usually come from fields of the modifier that OnCreated / OnRefresh filled from
the ability's special values, so every overridden virtual function is executed too and its stores to the
fields of the modifier are recorded.
"""
import re
import struct

from expr import C, ZERO, TRUE, lnot
from symexec import Executor

CDOTA_BUFF = ".?AVCDOTA_Buff@@"
CDOTA_MODIFIER_LUA = ".?AVCDOTA_Modifier_Lua@@"
# add r64, imm8 (48 83 /0 ib)
ADD_IMM8 = re.compile(rb"\x48\x83([\xc0-\xc7])(.)", re.S)

THIS = ('sym', 'this')
OUT = ('sym', 'out')
PARAMS = ('sym', 'params')
STATES = ('sym', 'states')
STATES_ON = ('sym', 'states_on')      # the masks before CheckState
STATES_OFF = ('sym', 'states_off')



def read_enum(im, first, prefix):
    """{value: name} of an engine enum from its name table ({const char *name; int value; ...} every 0x20)."""
    def name(e):
        if e < 0 or e + 16 > len(im.mem):
            return None
        r = im.va(im.q(e))
        s = im.cstr(r, 100) if r is not None else None
        return s if s and s.startswith(prefix) else None

    best, start = 0, None
    for s in im.strings(first):
        needle = struct.pack("<Q", im.base + s)
        i = im.mem.find(needle)
        while i >= 0:
            if i % 8 == 0:
                st = i
                while name(st - 0x20):
                    st -= 0x20
                n = 0
                while name(st + 0x20 * n):
                    n += 1
                if n > best:
                    best, start = n, st
            i = im.mem.find(needle, i + 1)
    out = {}
    for k in range(best):
        out[struct.unpack_from("<i", im.mem, start + 0x20 * k + 8)[0]] = name(start + 0x20 * k)
    return out


# CDOTA_Modifier_Lua's switch from a modifierfunction to the Lua callback it calls:
#   cmp r8d, <last>; ja default; movsxd rax, r8d; lea r8, [__ImageBase]; mov edx, [r8+rax*4+table]; add rdx, r8; jmp rdx
# each branch: lea rax, [thunk]; ...; a thunk: ...; lea r8, ["LuaName"]; call helper
LUA_SWITCH = re.compile(rb"\x41\x81\xf8(..)\x00\x00\x0f\x87....\x49\x63\xc0\x4c\x8d\x05....\x41\x8b\x94\x80(....)"
                        rb"\x49\x03\xd0\xff\xe2", re.S)


def lua_callback_names(im):
    """{modifierfunction value: Lua callback name} (only the functions a Lua modifier can implement)."""
    out = {}
    for a, n in im.code_sections():
        for m in LUA_SWITCH.finditer(im.mem[a:a + n]):
            last = struct.unpack("<H", m.group(1))[0]
            table = struct.unpack("<I", m.group(2))[0]
            for i in range(last + 1):
                branch = im.d(table + 4 * i)
                if im.mem[branch:branch + 3] != b"\x48\x8d\x05":
                    continue
                thunk = branch + 7 + im.i32(branch + 3)
                for k in range(thunk, thunk + 0x20):
                    if im.mem[k:k + 3] == b"\x4c\x8d\x05":
                        s = im.text(k + 7 + im.i32(k + 3), 100)
                        if s:
                            out[i] = s
                        break
            return out
    return out


class Modifiers:
    def __init__(self, im, named, function_count):
        """function_count: MODIFIER_FUNCTION_LAST, the number of entries of the handler table."""
        self.im = im
        self.ex = Executor(im, named=named)
        vts = im.vtables()
        self.classes = {}       # vtable -> decorated class name
        self.bases = {}
        for vt, (name, col) in vts.items():
            b = im.bases(col)
            if CDOTA_BUFF in b:
                self.classes[vt] = name
                self.bases[vt] = b
        self.base_vt = next(vt for vt, n in self.classes.items() if n == CDOTA_BUFF)
        self.base_slots = im.vfuncs(self.base_vt)
        lua_vt = next((vt for vt, n in self.classes.items() if n == CDOTA_MODIFIER_LUA), None)
        self.slot_names = self.lua_slot_names(lua_vt) if lua_vt else {}
        self.handler_table = None
        self.declare_slot = self.find_declare_slot(lua_vt)
        # fields of derived classes start after the handler table (one entry per modifier function)
        self.fields_from = self.handler_table + 16 * function_count

    # --- vtable layout from the Lua modifier: the slots it overrides forward to Lua callbacks by name
    def lua_slot_names(self, lua_vt):
        im = self.im
        names = {}
        lua_slots = im.vfuncs(lua_vt)
        for i, f in enumerate(lua_slots):
            if i >= len(self.base_slots) or f == self.base_slots[i]:
                continue
            end = (im.func_of(f) or (f, f + 0x200))[1]
            found = []
            for k in range(f, min(end, f + 0x600)):
                if im.mem[k] in (0x48, 0x4c) and im.mem[k + 1] == 0x8d and im.mem[k + 2] & 0xC7 == 0x05:
                    s = im.text(k + 7 + im.i32(k + 3), 80)
                    if s and re.fullmatch(r"[A-Z][A-Za-z]+", s) and not s.startswith("CDOTA"):
                        found.append(s)
            if found:
                names[i] = found[0]
        return names

    def find_declare_slot(self, lua_vt):
        """The DeclareFunctions slot and the offset of the handler table. The Lua modifier's override loops
        over its declared list and stores each handler at [this + (P + K) * 16]:
            movsxd rcx, [list + i*4]; ...; add rcx, K; ...; add rcx, rcx; movups [this + rcx*8], xmm0
        so the table starts at K * 16."""
        lua_slots = self.im.vfuncs(lua_vt) if lua_vt else []
        for i, f in enumerate(lua_slots):
            if i >= len(self.base_slots) or f == self.base_slots[i]:
                continue
            body = self.im.mem[f:f + 0x100]
            for m in ADD_IMM8.finditer(body):
                reg = m.group(1)[0] & 7
                double = bytes([0x48, 0x03, 0xC0 | (reg << 3) | reg])
                if double in body[m.end():m.end() + 8]:
                    self.handler_table = m.group(2)[0] * 16
                    return i
        raise RuntimeError("DeclareFunctions of CDOTA_Modifier_Lua not found")

    def name_of(self, vt):
        """The modifier name: GetName (slot 9) returns a string constant."""
        f = self.im.va(self.im.q(vt + 9 * 8))
        if f is None:
            return None
        done, _ = self.ex.run(f, regs={"rcx": THIS})
        for s in done:
            v = s.regs.get("rax")
            if v and v[0] == 'c':
                return self.im.text(v[1] - self.im.base, 200)
        return None

    def run(self, f, vt, rcx=THIS, rdx=('sym', 'arg1'), r8=('sym', 'arg2')):
        return self.ex.run(f, regs={"rcx": rcx, "rdx": rdx, "r8": r8, "r9": ('sym', 'arg3')},
                           mem=[(THIS, 8, C(self.im.base + vt))])

    def declared(self, vt):
        """{P: (handler rva, this adjustment)} stored by the DeclareFunctions override (all paths)."""
        f = self.im.va(self.im.q(vt + self.declare_slot * 8))
        if f is None or f == self.base_slots[self.declare_slot]:
            return {}
        done, _ = self.run(f, vt)
        out = {}
        for s in done:
            pieces = {off: v for off, size, v in s.mem.get(THIS, ()) if size == 8}
            table = self.handler_table
            for off, v in pieces.items():
                if table <= off < self.fields_from and (off - table) % 16 == 0 and v[0] == 'c':
                    rva = v[1] - self.im.base
                    if 0 <= rva < self.im.size and self.im.is_code(rva):
                        adj = pieces.get(off + 8, ZERO)
                        out[(off - table) // 16] = (rva, adj[1] if adj[0] == 'c' else 0)
        return out

    def check_state(self, vt):
        """Paths of the CheckState override, or None when the class keeps CDOTA_Buff's. The engine passes
        two 64-bit masks of modifier states: +0 the states the modifier sets true, +8 those it sets false
        (CDOTA_Modifier_Lua turns {[state] = true} into bts [+0] / btr [+8], false the other way round)."""
        slot = next((s for s, n in self.slot_names.items() if n == "CheckState"), None)
        if slot is None:
            return None
        f = self.im.va(self.im.q(vt + slot * 8))
        if f is None or f == self.base_slots[slot]:
            return None
        return self.ex.run(f, regs={"rcx": THIS, "rdx": STATES, "r8": ('sym', 'arg2'), "r9": ('sym', 'arg3')},
                           mem=[(THIS, 8, C(self.im.base + vt)),
                                (STATES, 8, STATES_ON), (('op', 'add', STATES, C(8)), 8, STATES_OFF)])

    def overridden(self, vt):
        """[(slot, function)] of the virtual functions this class (or a base below CDOTA_Buff) overrides."""
        out = []
        for i, f in enumerate(self.im.vfuncs(vt)):
            if i >= len(self.base_slots):
                break
            if f != self.base_slots[i] and i not in (0, 9, self.declare_slot):
                out.append((i, f))
        return out

    def writes(self, done, min_off):
        """[(path condition, {offset: (size, value)})] of the stores a function made to its own fields."""
        out = []
        for s in done:
            fields = {}
            for off, size, v in s.mem.get(THIS, ()):
                if off >= min_off:
                    fields[off] = (size, v)
            out.append((s.conds, fields))
        return out


def decision(paths):
    """Build one expression from [(path condition, value)]: ite over the conditions that split the paths."""
    vals = {v for _, v in paths}
    if len(vals) == 1:
        return next(iter(vals))
    if not paths:
        return None
    for c in paths[0][0]:
        yes = [p for p in paths if c in p[0]]
        no = [p for p in paths if lnot(c) in p[0]]
        if yes and no:
            neither = [p for p in paths if c not in p[0] and lnot(c) not in p[0]]
            a = decision([(tuple(x for x in cs if x != c), v) for cs, v in yes + neither])
            b = decision([(tuple(x for x in cs if x != lnot(c)), v) for cs, v in no + neither])
            from expr import ite
            return ite(c, a, b)
    # the paths differ in a way no recorded condition explains (e.g. one of them was cut short)
    return ('any', tuple(sorted(vals, key=repr)))
