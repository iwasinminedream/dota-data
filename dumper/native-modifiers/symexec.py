"""A small symbolic executor for the MSVC x86-64 code of server.dll.

Registers and memory hold expressions (expr.py). Every path through a function is followed (conditional
jumps fork), calls into small functions of the image are inlined, calls the caller named are replaced by
symbolic results, everything else becomes an opaque ('call', 'sub_<rva>', args). When an inlined call
cannot be followed (a loop, an unsupported instruction, too many paths), the path restarts from the call
with the call made opaque. A path ends at the return of the entry function; its State keeps the stores,
the return value and the path condition.

Assumptions that keep the number of paths down (formulas describe the normal case):
  * entity handles read from memory are valid (not -1 / -2) and resolve to their entity;
  * pointers loaded from memory are not null (results of named or opaque calls may be: those checks stay).
"""
from capstone import CS_ARCH_X86, CS_MODE_64, Cs
from capstone.x86 import X86_OP_IMM, X86_OP_MEM, X86_OP_REG

from expr import C, F, FALSE, ONE, TRUE, ZERO, MASK, addr, base_off, cmp, ite, iop, lnot, op, signed, un

GPR64 = ["rax", "rcx", "rdx", "rbx", "rsp", "rbp", "rsi", "rdi"] + ["r%d" % i for i in range(8, 16)]
M64_NEG1 = (1 << 64) - 1
M64_NEG2 = (1 << 64) - 2


def _regmap():
    m = {}
    for r in GPR64:
        m[r] = (r, 8)
    for x in "abcd":
        m["e%sx" % x] = ("r%sx" % x, 4)
        m["%sx" % x] = ("r%sx" % x, 2)
        m["%sl" % x] = ("r%sx" % x, 1)
        m["%sh" % x] = ("r%sx" % x, -1)      # high byte
    for x in ("si", "di", "bp", "sp"):
        m["e" + x] = ("r" + x, 4)
        m[x] = ("r" + x, 2)
        m[x + "l"] = ("r" + x, 1)
    for i in range(8, 16):
        m["r%dd" % i] = ("r%d" % i, 4)
        m["r%dw" % i] = ("r%d" % i, 2)
        m["r%db" % i] = ("r%d" % i, 1)
    return m


REG = _regmap()
VOLATILE = ["rax", "rcx", "rdx", "r8", "r9", "r10", "r11"]
ARGS = ["rcx", "rdx", "r8", "r9"]
LOSIZE = {1: 'lo8', 2: 'lo16', 4: 'lo32'}
SXSIZE = {1: 'sx8', 2: 'sx16', 4: 'sx32'}
CC = {
    "o": None, "no": None,
    "b": "ult", "c": "ult", "nae": "ult", "ae": "uge", "nb": "uge", "nc": "uge",
    "e": "eq", "z": "eq", "ne": "ne", "nz": "ne",
    "be": "ule", "na": "ule", "a": "ugt", "nbe": "ugt",
    "s": "s", "ns": "ns", "p": "p", "pe": "p", "np": "np", "po": "np",
    "l": "slt", "nge": "slt", "ge": "sge", "nl": "sge", "le": "sle", "ng": "sle", "g": "sgt", "nle": "sgt",
}
FLOAT_CC = {"ult": "flt", "uge": "fge", "ule": "fle", "ugt": "fgt", "eq": "feq", "ne": "fne"}
FOPS = {"add": "fadd", "sub": "fsub", "mul": "fmul", "div": "fdiv", "min": "fmin", "max": "fmax"}
# instructions whose result the formulas never need: the destination becomes opaque
OPAQUE = {"sbb", "adc", "rol", "ror", "rcl", "rcr", "xadd", "cmpxchg", "popcnt", "lzcnt",
          "tzcnt", "bsf", "bsr", "bswap", "shld", "shrd", "andn", "bextr", "blsr", "blsi", "shlx", "shrx", "sarx",
          "pand", "pandn", "por", "orps", "orpd", "andnps", "andnpd", "shufps", "shufpd", "unpcklps", "unpckhps",
          "unpcklpd", "unpckhpd", "movlhps", "movhlps", "punpckldq", "punpcklqdq", "punpckhdq", "pshufd",
          "pshuflw", "pshufhw", "insertps", "movsldup", "movshdup", "blendps", "blendvps", "pinsrd", "pinsrq",
          "pextrd", "pextrq", "movhps", "movlps", "cmpps", "cmpss", "cmpeqps", "cmpltps", "cmpleps", "cmpneqps",
          "cmpnltps", "cmpnleps", "cmpeqss", "cmpltss", "cmpless", "cmpneqss", "cmpnltss", "cmpnless",
          "pcmpeqd", "pcmpeqb", "pcmpgtd", "paddd", "psubd", "pmulld", "psrld", "pslld", "psrad", "psrldq",
          "pslldq", "packssdw", "movmskps", "pmovmskb", "roundss", "roundps", "rcpss", "rsqrtss", "rcpps",
          "rsqrtps", "sqrtps", "dpps", "haddps", "cvtps2pd", "cvtpd2ps", "movntps", "xchg8", "rdtsc", "cpuid",
          "stmxcsr", "ldmxcsr", "crc32", "movbe", "cmpxchg16b", "setz"}


class Abort(Exception):
    pass


class Insn:
    __slots__ = ("addr", "size", "mn", "ops", "next")

    def __init__(self, addr_, size, mn, ops):
        self.addr, self.size, self.mn, self.ops = addr_, size, mn, ops
        self.next = addr_ + size


class State:
    __slots__ = ("regs", "xmm", "mem", "flags", "conds", "pc", "pc_next", "depth", "visits", "steps", "calls",
                 "frames", "fid")

    def copy(self):
        s = State()
        s.regs = dict(self.regs)
        s.xmm = dict(self.xmm)
        s.mem = dict(self.mem)
        s.flags = self.flags
        s.conds = self.conds
        s.pc = self.pc
        s.pc_next = self.pc_next
        s.depth = self.depth
        s.visits = dict(self.visits)
        s.steps = self.steps
        s.calls = self.calls
        s.frames = self.frames
        s.fid = self.fid
        return s


def pointer_like(e):
    """Expressions that are addresses of objects (null checks on them are assumed to pass)."""
    t = e[0]
    if t in ('ent', 'slot', 'g'):
        return True
    if t == 'sym':
        return e[1] in ('this', 'out', 'params', 'rsp0', 'kv', 'states')
    if t == 'ld':
        return e[2] == 8
    if t == 'op' and e[1] == 'add':
        return pointer_like(e[2]) or pointer_like(e[3])
    return False


def opsize(o):
    return o[2] if o[0] in ("r", "i") else o[5]


def strip_ext(x):
    while x[0] == 'un' and x[1] in ('lo32', 'sx32', 'zx32'):
        x = x[2]
    return x


class Executor:
    def __init__(self, image, named=None, max_paths=96, max_steps=6000, max_depth=4, inline_limit=0x600,
                 loop_limit=3):
        self.im = image
        self.base = image.base
        self.md = Cs(CS_ARCH_X86, CS_MODE_64)
        self.md.detail = True
        self.cache = {}
        # rva -> f(executor, state) -> (rax expr, xmm0 expr) | None: calls replaced by a symbolic result
        self.named = named or {}
        self.no_inline = set()
        self.fallbacks = {}
        self.fid_counter = 0
        self.type_byte = None        # offset of the entity class byte (see Knowledge.find_type_byte)
        self.on_opaque = None        # f(executor, state, name, args) before an opaque call
        self.max_paths, self.max_steps, self.max_depth = max_paths, max_steps, max_depth
        self.inline_limit, self.loop_limit = inline_limit, loop_limit

    # --- decoding
    def insn(self, rva):
        i = self.cache.get(rva)
        if i is not None:
            return i
        if not self.im.is_code(rva):
            raise Abort("pc outside code %x" % rva)
        raw = self.im.mem[rva:rva + 16]
        for ins in self.md.disasm(raw, rva, 1):
            ops = []
            for o in ins.operands:
                if o.type == X86_OP_REG:
                    ops.append(("r", ins.reg_name(o.reg), o.size))
                elif o.type == X86_OP_IMM:
                    ops.append(("i", o.imm, o.size))
                elif o.type == X86_OP_MEM:
                    m = o.mem
                    ops.append(("m", ins.reg_name(m.base) if m.base else None,
                                ins.reg_name(m.index) if m.index else None, m.scale, m.disp, o.size,
                                ins.reg_name(m.segment) if m.segment else None))
            mn = ins.mnemonic
            if mn.startswith("lock "):
                mn = mn[5:]
            i = Insn(rva, ins.size, mn, ops)
            break
        else:
            raise Abort("undecodable %x" % rva)
        self.cache[rva] = i
        return i

    # --- registers
    def rget(self, st, name):
        if name.startswith("xmm") or name.startswith("ymm"):
            return st.xmm.get("xmm" + name[3:], ZERO)
        full, size = REG[name]
        v = st.regs.get(full)
        if v is None:
            v = ('sym', 'reg_' + full)
        if size == 8:
            return v
        if size == -1:
            return un('lo8', iop('shr', v, C(8)))
        return un(LOSIZE[size], v)

    def rset(self, st, name, v):
        if name.startswith("xmm") or name.startswith("ymm"):
            st.xmm["xmm" + name[3:]] = v
            return
        full, size = REG[name]
        if size == 8:
            st.regs[full] = v
        elif size == 4:
            st.regs[full] = v if v[0] != 'c' else C(v[1] & 0xFFFFFFFF)
        else:
            # partial write: keep the rest only when everything is constant
            old = st.regs.get(full)
            m = MASK[abs(size)]
            if v[0] == 'c' and old is not None and old[0] == 'c':
                if size == -1:
                    st.regs[full] = C((old[1] & ~0xFF00) | ((v[1] & 0xFF) << 8))
                else:
                    st.regs[full] = C((old[1] & ~m) | (v[1] & m))
            else:
                st.regs[full] = v if size != -1 else ('sym', 'partial')

    # --- memory
    def ea(self, st, o):
        _, b, i, scale, disp, _, seg = o
        if b == "rip":
            return C(self.base + disp + st.pc_next)
        e = C(disp)
        if seg:
            e = iop('add', ('sym', 'tls_' + seg), e)
        if b:
            e = iop('add', self.rget(st, b), e)
        if i:
            e = iop('add', e, iop('mul', self.rget(st, i), C(scale)) if scale != 1 else self.rget(st, i))
        return self.fix_addr(e)

    def fix_addr(self, e):
        """Recognise the entity-list lookup: chunk[(h & 0x7fff) >> 9] + (h & 0x1ff) * 0x70 -> slot(h)."""
        if e[0] == 'op' and e[1] == 'add':
            for x, y in ((e[2], e[3]), (e[3], e[2])):
                if x[0] == 'op' and x[1] == 'mul' and x[3] == C(0x70):
                    a = strip_ext(x[2])
                    if a[0] == 'op' and a[1] == 'and' and a[3] == C(0x1FF):
                        h = a[2]
                        while True:
                            if h[0] == 'un' and h[1] in ('lo32', 'zx32', 'sx32'):
                                h = h[2]
                            elif h[0] == 'op' and h[1] == 'and' and h[3] == C(0x7FFF):
                                h = h[2]
                            else:
                                break
                        if y[0] == 'ld':
                            return ('slot', h)
        return e

    def load(self, st, a, size):
        base, off = base_off(a)
        if base is None:
            rva = off - self.base
            if 0 <= rva < self.im.size:
                if self.im.is_readonly(rva) or self.im.is_code(rva):
                    if size == 16:
                        return ('cat', ((0, 8, C(self.im.q(rva))), (8, 8, C(self.im.q(rva + 8)))))
                    return C(int.from_bytes(self.im.mem[rva:rva + size], "little"))
                base, off = ('g', rva), 0
            else:
                base, off = ('abs', off), 0
        if base[0] == 'slot':
            if off == 0 and size == 8:
                return ('ent', base[1])
            if off == 0x10 and size == 4:
                return ('serial', base[1])
        pieces = st.mem.get(base, ())
        hit = [p for p in pieces if p[0] < off + size and off < p[0] + p[1]]
        if not hit:
            if base == ('sym', 'rsp0') and off < 0:
                return ('sym', 'undef')
            return ('ld', addr(base, off), size)
        if size == 16:
            parts = []
            for p in sorted(hit):
                if p[0] >= off and p[0] + p[1] <= off + 16:
                    parts.append((p[0] - off, p[1], p[2]))
            return ('cat', tuple(parts))
        for po, ps, pv in hit:
            if po == off and ps == size:
                return pv
            if po <= off and off + size <= po + ps:
                if pv[0] == 'c':
                    return C((pv[1] >> (8 * (off - po))) & MASK[size])
                if pv[0] == 'cat':
                    for (co, cs, cv) in pv[1]:
                        if co == off - po and cs == size:
                            return cv
                        if co <= off - po and off - po + size <= co + cs and cv[0] == 'c':
                            return C((cv[1] >> (8 * (off - po - co))) & MASK[size])
                    return ('ld', addr(base, off), size)
                if off == po:
                    return un(LOSIZE.get(size, 'lo32'), pv) if size < ps else pv
                return un(LOSIZE.get(size, 'lo32'), iop('shr', pv, C(8 * (off - po))))
        return ('ld', addr(base, off), size)

    def store(self, st, a, size, v):
        base, off = base_off(a)
        if base is None:
            rva = off - self.base
            base, off = (('g', rva), 0) if 0 <= rva < self.im.size else (('abs', off), 0)
        if v[0] == 'cat':
            for (co, cs, cv) in v[1]:
                self.store(st, addr(base, off + co), cs, cv)
            return
        pieces = st.mem.get(base, ())
        keep = tuple(p for p in pieces if not (p[0] < off + size and off < p[0] + p[1]))
        st.mem[base] = keep + ((off, size, v),)

    # --- operands
    def get(self, st, o):
        t = o[0]
        if t == "r":
            return self.rget(st, o[1])
        if t == "i":
            return C(o[1])
        return self.load(st, self.ea(st, o), o[5])

    def put(self, st, o, v):
        if o[0] == "r":
            self.rset(st, o[1], v)
        elif o[0] == "m":
            self.store(st, self.ea(st, o), o[5], v)
        else:
            raise Abort("write to immediate")

    def xget(self, st, o, size):
        """A scalar from an xmm register, a general register or memory."""
        if o[0] == "r":
            if o[1].startswith("xmm") or o[1].startswith("ymm"):
                v = st.xmm.get("xmm" + o[1][3:], ZERO)
            else:
                v = self.rget(st, o[1])
            if v[0] == 'cat':
                v = next((cv for (co, cs, cv) in v[1] if co == 0), ZERO)
            return v
        if o[0] == "i":
            return C(o[1])
        return self.load(st, self.ea(st, o), size)

    # --- conditions
    def condition(self, st, cc):
        name = CC.get(cc)
        f = st.flags
        if name is None or f is None:
            raise Abort("flags %s" % cc)
        kind = f[0]
        if kind == 'cmp':
            _, a, b, size = f
            if name in ('s', 'ns'):
                r = cmp('slt', iop('sub', a, b), ZERO, size)
                return r if name == 's' else lnot(r)
            if name in ('p', 'np'):
                raise Abort("parity after cmp")
            return cmp(name, a, b, size)
        if kind in ('test', 'res'):
            if kind == 'test':
                _, a, b, size = f
                r = a if a == b else iop('and', a, b)
            else:
                _, r, size = f
            if name in ('eq', 'ne'):
                return cmp(name, r, ZERO, size)
            if name in ('s', 'slt'):
                return cmp('slt', r, ZERO, size)
            if name in ('ns', 'sge'):
                return cmp('sge', r, ZERO, size)
            if name == 'sle':
                return cmp('sle', r, ZERO, size)
            if name == 'sgt':
                return cmp('sgt', r, ZERO, size)
            if name == 'ult':
                return FALSE
            if name == 'uge':
                return TRUE
            if name == 'ule':
                return cmp('eq', r, ZERO, size)
            if name == 'ugt':
                return cmp('ne', r, ZERO, size)
            raise Abort("flags %s after test" % cc)
        if kind == 'fcmp':
            _, a, b = f
            if name == 'p':
                return FALSE
            if name == 'np':
                return TRUE
            fn = FLOAT_CC.get(name)
            if fn is None:
                raise Abort("float flags %s" % cc)
            return cmp(fn, a, b)
        if kind == 'bt':
            _, a, k = f
            bit = ('bit', a, k)
            if name == 'ult':
                return bit
            if name == 'uge':
                return lnot(bit)
            raise Abort("flags %s after bt" % cc)
        raise Abort("flags kind %s" % kind)

    def assume(self, st, c):
        """TRUE / FALSE when the path condition or an assumption decides c, else None."""
        if c in (TRUE, FALSE):
            return c
        if c in st.conds:
            return TRUE
        if lnot(c) in st.conds:
            return FALSE
        if c[0] == 'cmp' and c[1] in ('eq', 'ne'):
            a, b = c[2], c[3]
            if b[0] == 'c' and a[0] != 'c':
                k = b[1]
                if k == 0 and pointer_like(a):
                    return FALSE if c[1] == 'eq' else TRUE
                x = strip_ext(a)
                if k in (0xFFFFFFFF, 0xFFFFFFFE, M64_NEG1, M64_NEG2) and x[0] == 'ld' and x[2] == 4:
                    return FALSE if c[1] == 'eq' else TRUE
            for x in (a, b):
                if x[0] == 'serial':
                    return TRUE if c[1] == 'eq' else FALSE
            # the entity class byte checked against a constant: an inlined cast, assumed to succeed
            if self.type_byte is not None and a[0] == 'ld' and a[2] == 1 and b[0] == 'c':
                eb, eo = base_off(a[1])
                if eo == self.type_byte and eb is not None and pointer_like(eb):
                    return TRUE if c[1] == 'eq' else FALSE
        if c[0] == 'lnot':
            r = self.assume(st, c[1])
            if r is not None:
                return lnot(r)
        return None

    # --- calls
    def call_args(self, st):
        return tuple(self.rget(st, r) for r in ARGS)

    def set_result(self, st, rax, x0, name):
        for r in VOLATILE:
            st.regs[r] = ('sym', 'clobber')
        st.regs["rax"] = rax
        for i in range(6):
            st.xmm["xmm%d" % i] = ('sym', 'clobber')
        st.xmm["xmm0"] = x0
        st.flags = None
        st.calls = st.calls + (name,)

    def opaque(self, st, name, args):
        res = ('call', name, args)
        if self.on_opaque is not None:
            self.on_opaque(self, st, name, args)
        self.set_result(st, res, res, name)

    def do_call(self, st, target, ret_to, tail_ret=None):
        """Call a function of the image; returns True when the call was inlined (pc moved into it)."""
        h = self.named.get(target)
        if h is not None:
            r = h(self, st)
            if r is not None:
                self.set_result(st, r[0], r[1], target)
                return False
        fo = self.im.func_of(target)
        size = (fo[1] - fo[0]) if fo else 0x40
        if st.depth < self.max_depth and size <= self.inline_limit and target not in self.no_inline:
            snap = st.copy()
            rsp = iop('add', self.rget(st, "rsp"), C(-8))
            self.store(st, rsp, 8, ('ret', ret_to) if tail_ret is None else tail_ret)
            st.regs["rsp"] = rsp
            # loops are counted per call: a frame id for the visits of this call
            caller_fid = st.fid if tail_ret is None else (st.frames[-1][4] if st.frames else 0)
            frame = (snap, target, ret_to, tail_ret, caller_fid)
            self.fid_counter += 1
            st.fid = self.fid_counter
            if tail_ret is None:
                st.depth += 1
                st.frames = st.frames + (frame,)
            else:
                st.frames = (st.frames[:-1] if st.frames else ()) + (frame,)
            st.pc = target
            return True
        self.opaque(st, "sub_%x" % target, self.call_args(st))
        return False

    def resolve_target(self, st, o):
        """Target of a call/jmp operand: rva, ('import', name), ('vcall', obj, slot), ('icall', expr)."""
        if o[0] == "i":
            return o[1]
        if o[0] == "m":
            a = self.ea(st, o)
            base, off = base_off(a)
            if base is None and (off - self.base) in self.im.imports:
                return ("import", self.im.imports[off - self.base])
            v = self.load(st, a, 8)
        else:
            v = self.rget(st, o[1])
            if v[0] == 'ld':
                a = v[1]
                base, off = base_off(a)
            else:
                base, off = None, 0
        if v[0] == 'c':
            rva = v[1] - self.base
            if 0 <= rva < self.im.size and self.im.is_code(rva):
                return rva
        if base is not None and base[0] == 'ld' and base[2] == 8 and off % 8 == 0:
            return ("vcall", base[1], off // 8)
        return ("icall", v)

    # --- main loop
    def run(self, entry, regs=None, mem=None, xmm=None):
        """Follow every path from entry; returns (finished states, abort reasons)."""
        st = State()
        st.regs = {"rsp": ('sym', 'rsp0')}
        st.regs.update(regs or {})
        st.xmm = dict(xmm or {})
        st.mem = {}
        st.pc_next = entry
        for (a, size, v) in (mem or []):
            self.store(st, a, size, v)
        self.store(st, ('sym', 'rsp0'), 8, ('sym', 'retaddr'))
        st.flags = None
        st.conds = ()
        st.pc = entry
        st.depth = 0
        st.visits = {}
        st.steps = 0
        st.calls = ()
        st.frames = ()
        st.fid = 0
        work = [st]
        done, aborted = [], []
        forks = 0
        used_fallbacks = set()
        while work:
            s = work.pop()
            try:
                r = self.step_until_fork(s)
                if r is not None:
                    forks += 1
                    if forks > self.max_paths:
                        raise Abort("too many paths")
            except Abort as ex:
                if s.frames:
                    t = self.fallback(s, used_fallbacks)
                    if t is not None:
                        (done if t.pc is None else work).append(t)
                    continue
                aborted.append(str(ex))
                continue
            if r is None:
                done.append(s)
                continue
            cond, taken_pc, fall_pc = r
            t = s.copy()
            t.conds = s.conds + (cond,)
            t.pc = taken_pc
            s.conds = s.conds + (lnot(cond),)
            s.pc = fall_pc
            work.append(s)
            work.append(t)
        return done, aborted

    def fallback(self, s, used):
        """Restart a path from its innermost inlined call, with that call made opaque.

        Returns the restarted state (pc None when that already completes the path) or None when another
        path already restarted from the same call."""
        snap, target, ret_to, tail_ret, _ = s.frames[-1]
        key = id(snap)
        if key in used:
            return None
        used.add(key)
        self.fallbacks[target] = self.fallbacks.get(target, 0) + 1
        if self.fallbacks[target] >= 8:
            self.no_inline.add(target)
        t = snap.copy()
        t.steps = s.steps
        self.opaque(t, "sub_%x" % target, self.call_args(t))
        if tail_ret is None:
            t.pc = ret_to
        elif self.do_ret(t, tail_ret) == "ret":
            t.pc = None
        return t

    def step_until_fork(self, st):
        """Execute until the entry function returns (None) or a branch needs a fork ((cond, taken, fall))."""
        if st.pc is None:
            return None
        while True:
            st.steps += 1
            if st.steps > self.max_steps:
                raise Abort("step limit")
            key = (st.fid, st.pc)
            n = st.visits.get(key, 0) + 1
            if n > self.loop_limit:
                raise Abort("loop at %x" % st.pc)
            st.visits[key] = n
            ins = self.insn(st.pc)
            st.pc_next = ins.next
            r = self.exec(st, ins)
            if r is None:
                st.pc = ins.next
                continue
            if r == "ret":
                st.pc = None
                return None
            if r == "jump":
                continue
            return r

    def exec(self, st, ins):
        mn, ops = ins.mn, ins.ops
        g = self.get

        if mn in ("nop", "lfence", "mfence", "sfence", "pause", "endbr64") or mn.startswith("prefetch"):
            return None
        if mn == "int3" or mn == "ud2" or mn == "hlt":
            raise Abort(mn)
        if mn in ("mov", "movabs"):
            v = g(st, ops[1])
            if ops[1][0] == "i":
                v = C(v[1] & MASK[opsize(ops[0])])
            self.put(st, ops[0], v)
            return None
        if mn == "movzx":
            v = g(st, ops[1])
            self.put(st, ops[0], un(LOSIZE[opsize(ops[1])], v) if ops[1][0] == "r" else v)
            return None
        if mn in ("movsx", "movsxd"):
            self.put(st, ops[0], un(SXSIZE[opsize(ops[1])], g(st, ops[1])))
            return None
        if mn == "lea":
            self.put(st, ops[0], self.ea(st, ops[1]))
            return None
        if mn == "push":
            v = g(st, ops[0])
            rsp = iop('add', self.rget(st, "rsp"), C(-8))
            st.regs["rsp"] = rsp
            self.store(st, rsp, 8, v)
            return None
        if mn == "pop":
            rsp = self.rget(st, "rsp")
            v = self.load(st, rsp, 8)
            st.regs["rsp"] = iop('add', rsp, C(8))
            self.put(st, ops[0], v)
            return None
        if mn in ("imul", "mul") and len(ops) == 1:
            size = opsize(ops[0])
            src = g(st, ops[0])
            a = self.rget(st, {4: "eax", 8: "rax"}.get(size, "eax"))
            if size not in (4, 8):
                raise Abort("mul size")
            self.rset(st, {4: "eax", 8: "rax"}[size], iop('mul', a, src))
            self.rset(st, {4: "edx", 8: "rdx"}[size], ('op', 'mulhi%d' % (8 * size), a, src))
            st.flags = None
            return None
        if mn in ("add", "sub", "and", "or", "xor", "imul", "shl", "shr", "sar", "sal"):
            if mn == "imul" and len(ops) == 3:
                size = opsize(ops[0])
                v = iop('mul', g(st, ops[1]), g(st, ops[2]))
                self.put(st, ops[0], v if size == 8 else un(LOSIZE[size], v))
                st.flags = None
                return None
            size = opsize(ops[0])
            a = g(st, ops[0])
            b = g(st, ops[1])
            if ops[1][0] == "i":
                b = C(b[1] & MASK[size])
            name = {"imul": "mul", "sal": "shl"}.get(mn, mn)
            if mn == "xor" and ops[0] == ops[1]:
                v = ZERO
            elif name in ("shl", "shr", "sar"):
                v = self.shift(name, a, b, size)
            else:
                v = iop(name, a, b)
                if name == 'add':
                    v = self.fix_addr(v)
                    v = self.div_fixup(v)
            if size < 8 and v[0] == 'c':
                v = C(v[1] & MASK[size])
            elif size < 8 and name in ('add', 'sub', 'mul', 'shl', 'xor', 'or') and v[0] != 'c':
                v = un(LOSIZE[size], v)
            self.put(st, ops[0], v)
            st.flags = ('cmp', a, b, size) if mn == "sub" else ('res', v, size)
            return None
        if mn in ("inc", "dec"):
            size = opsize(ops[0])
            v = iop('add', g(st, ops[0]), C(1 if mn == "inc" else -1))
            if size < 8 and v[0] == 'c':
                v = C(v[1] & MASK[size])
            self.put(st, ops[0], v)
            st.flags = ('res', v, size)
            return None
        if mn in ("neg", "not"):
            size = opsize(ops[0])
            v = un(mn, g(st, ops[0]))
            if size < 8 and v[0] == 'c':
                v = C(v[1] & MASK[size])
            self.put(st, ops[0], v)
            if mn == "neg":
                st.flags = ('res', v, size)
            return None
        if mn == "cmp":
            size = opsize(ops[0])
            a, b = g(st, ops[0]), g(st, ops[1])
            if ops[1][0] == "i":
                b = C(b[1] & MASK[size])
            st.flags = ('cmp', a, b, size)
            return None
        if mn == "test":
            size = opsize(ops[0])
            a, b = g(st, ops[0]), g(st, ops[1])
            if ops[1][0] == "i":
                b = C(b[1] & MASK[size])
            st.flags = ('test', a, b, size)
            return None
        if mn in ("bts", "btr", "btc"):
            size = opsize(ops[0])
            a, b = g(st, ops[0]), g(st, ops[1])
            if b[0] != 'c':
                self.put(st, ops[0], ('sym', 'opaque'))
                st.flags = None
                return None
            k = b[1] & (8 * size - 1)
            st.flags = ('bt', a, k)
            m = 1 << k
            v = {"bts": iop('or', a, C(m)), "btr": iop('and', a, C(~m & MASK[size])),
                 "btc": iop('xor', a, C(m))}[mn]
            self.put(st, ops[0], v)
            return None
        if mn == "bt":
            a, b = g(st, ops[0]), g(st, ops[1])
            if b[0] != 'c':
                raise Abort("bt with register index")
            st.flags = ('bt', a, b[1] & 63)
            return None
        if mn in ("cdqe", "cwde", "cbw"):
            src = {"cdqe": ("eax", 'sx32', "rax"), "cwde": ("ax", 'sx16', "eax"), "cbw": ("al", 'sx8', "ax")}[mn]
            self.rset(st, src[2], un(src[1], self.rget(st, src[0])))
            return None
        if mn in ("cdq", "cqo"):
            size = 4 if mn == "cdq" else 8
            v = self.rget(st, "eax" if size == 4 else "rax")
            self.rset(st, "edx" if size == 4 else "rdx",
                      C(0 if signed(v[1], size) >= 0 else -1) if v[0] == 'c' else ('sym', 'signext'))
            return None
        if mn in ("idiv", "div"):
            size = opsize(ops[0])
            if size not in (4, 8):
                raise Abort("div size")
            d = g(st, ops[0])
            n = self.rget(st, {4: "eax", 8: "rax"}[size])
            self.rset(st, {4: "eax", 8: "rax"}[size], op('sdiv' if mn == "idiv" else 'udiv', n, d))
            self.rset(st, {4: "edx", 8: "rdx"}[size], op('srem' if mn == "idiv" else 'urem', n, d))
            st.flags = None
            return None
        if mn == "xchg":
            a, b = g(st, ops[0]), g(st, ops[1])
            self.put(st, ops[0], b)
            self.put(st, ops[1], a)
            return None
        if mn.startswith("set"):
            c = self.condition(st, mn[3:])
            r = self.assume(st, c)
            c = r if r is not None else c
            self.put(st, ops[0], ONE if c == TRUE else ZERO if c == FALSE else ('un', 'b2i', c))
            return None
        if mn.startswith("cmov"):
            c = self.condition(st, mn[4:])
            r = self.assume(st, c)
            c = r if r is not None else c
            a, b = g(st, ops[0]), g(st, ops[1])
            self.put(st, ops[0], ite(c, b, a))
            return None

        # --- control flow
        if mn == "jmp":
            t = self.resolve_target(st, ops[0])
            if isinstance(t, int) and self.is_local_jump(st.pc, t):
                st.pc = t
                return "jump"
            # tail call: the callee returns straight to our return address
            rsp = self.rget(st, "rsp")
            ret_val = self.load(st, rsp, 8)
            st.regs["rsp"] = iop('add', rsp, C(8))
            if isinstance(t, int):
                if self.do_call(st, t, None, tail_ret=ret_val):
                    return "jump"
            else:
                self.call_symbolic(st, t)
            return self.do_ret(st, ret_val)
        if mn.startswith("j"):
            c = self.condition(st, mn[1:])
            r = self.assume(st, c)
            t = ops[0][1]
            if r == TRUE:
                st.pc = t
                return "jump"
            if r == FALSE:
                return None
            return (c, t, ins.next)
        if mn == "call":
            t = self.resolve_target(st, ops[0])
            if isinstance(t, int):
                if self.do_call(st, t, ins.next):
                    return "jump"
                return None
            self.call_symbolic(st, t)
            return None
        if mn == "ret":
            rsp = self.rget(st, "rsp")
            v = self.load(st, rsp, 8)
            st.regs["rsp"] = iop('add', rsp, C(8 + (ops[0][1] if ops else 0)))
            return self.do_ret(st, v)

        # --- SSE scalar
        if mn in ("movss", "movd", "movq", "movsd"):
            size = 4 if mn in ("movss", "movd") else 8
            dst = ops[0]
            if dst[0] == "r" and (dst[1].startswith("xmm") or dst[1].startswith("ymm")):
                v = self.xget(st, ops[1], size)
                if ops[1][0] == "r" and not ops[1][1].startswith("xmm") and size == 4:
                    v = un('lo32', v)
                self.rset(st, dst[1], v)
            elif dst[0] == "r":
                self.rset(st, dst[1], self.xget(st, ops[1], size))
            else:
                self.store(st, self.ea(st, dst), size, self.xget(st, ops[1], size))
            return None
        if mn in ("movaps", "movups", "movdqa", "movdqu", "movapd", "movupd", "lddqu"):
            if ops[0][0] == "r":
                if ops[1][0] == "r":
                    self.rset(st, ops[0][1], self.rget(st, ops[1][1]))
                else:
                    self.rset(st, ops[0][1], self.load(st, self.ea(st, ops[1]), 16))
            else:
                v = self.rget(st, ops[1][1])
                if v[0] != 'cat':
                    v = ('cat', ((0, 4, v),)) if v != ZERO else ('cat', ((0, 8, ZERO), (8, 8, ZERO)))
                self.store(st, self.ea(st, ops[0]), 16, v)
            return None
        if mn in ("xorps", "xorpd", "pxor"):
            if ops[0] == ops[1]:
                self.rset(st, ops[0][1], F(0.0))
                return None
            b = self.xget(st, ops[1], 4)
            a = self.xget(st, ops[0], 4)
            if b[0] == 'c' and b[1] & 0xFFFFFFFF == 0x80000000:
                self.rset(st, ops[0][1], un('fneg', a))
                return None
            if b[0] == 'c' and b[1] == 0x8000000000000000:
                self.rset(st, ops[0][1], un('fneg', a))
                return None
            self.rset(st, ops[0][1], ('sym', 'opaque'))
            return None
        if mn in ("andps", "andpd"):
            b = self.xget(st, ops[1], 4)
            if b[0] == 'c' and b[1] & 0xFFFFFFFF == 0x7FFFFFFF:
                self.rset(st, ops[0][1], un('fabs', self.xget(st, ops[0], 4)))
                return None
            self.rset(st, ops[0][1], ('sym', 'opaque'))
            return None
        if mn[:3] in FOPS and mn[3:] in ("ss", "sd", "ps", "pd"):
            a = self.xget(st, ops[0], 4)
            b = self.xget(st, ops[1], 4)
            self.rset(st, ops[0][1], op(FOPS[mn[:3]], a, b))
            return None
        if mn in ("sqrtss", "sqrtsd"):
            self.rset(st, ops[0][1], un('fsqrt', self.xget(st, ops[1], 4)))
            return None
        if mn in ("cvtsi2ss", "cvtsi2sd"):
            v = self.get(st, ops[1])
            self.rset(st, ops[0][1], un('i2f' if opsize(ops[1]) == 4 else 'i2f64', v))
            return None
        if mn in ("cvtdq2ps", "cvtdq2pd"):
            self.rset(st, ops[0][1], un('i2f', self.xget(st, ops[1], 4)))
            return None
        if mn in ("cvttss2si", "cvtss2si", "cvttsd2si", "cvtsd2si", "cvttps2dq", "cvtps2dq"):
            self.rset(st, ops[0][1], un('f2i', self.xget(st, ops[1], 4)))
            return None
        if mn in ("cvtss2sd", "cvtsd2ss"):
            self.rset(st, ops[0][1], self.xget(st, ops[1], 4))
            return None
        if mn in ("comiss", "ucomiss", "comisd", "ucomisd"):
            st.flags = ('fcmp', self.xget(st, ops[0], 4), self.xget(st, ops[1], 4))
            return None
        if mn.startswith("rep ") or mn.startswith("stos") or mn.startswith("movs") and mn[4:] in ("b", "w", "d", "q"):
            return None
        if mn in OPAQUE or mn.startswith("v"):
            if ops and ops[0][0] in ("r", "m"):
                if mn in ("cmpxchg", "xadd") and len(ops) > 1:
                    pass
                self.put(st, ops[0], ('sym', 'opaque'))
            st.flags = None
            return None
        raise Abort("insn %s" % mn)

    def shift(self, name, a, b, size):
        """Shifts; a right shift of the high half of a multiplication by a magic constant is a division."""
        if b[0] == 'c':
            x = a
            while x[0] == 'un' and x[1] in ('lo32', 'sx32'):
                x = x[2]
            if x[0] == 'op' and x[1].startswith('mulhi') and name in ('sar', 'shr'):
                bits = int(x[1][5:])
                q = self.magic_div(x[2], x[3], bits, b[1])
                if q is not None:
                    return q
            if x[0] == 'op' and x[1] == 'add' and name in ('sar', 'shr'):
                # signed magic with the high bit set: mulhi(n, M) + n
                for m, n in ((x[2], x[3]), (x[3], x[2])):
                    m = strip_ext(m)
                    if m[0] == 'op' and m[1].startswith('mulhi') and strip_ext(m[2]) == strip_ext(n):
                        bits = int(m[1][5:])
                        q = self.magic_div(m[2], m[3], bits, b[1], extra=1 << bits)
                        if q is not None:
                            return q
        if name == 'sar' and size < 8:
            a = un(SXSIZE[size], a)
        return iop(name, a, b)

    @staticmethod
    def magic_div(n, magic, bits, k, extra=0):
        if magic[0] != 'c':
            n, magic = magic, n
        if magic[0] != 'c':
            return None
        m = magic[1] & ((1 << bits) - 1)
        m += extra
        if not m:
            return None
        d = (1 << (bits + k)) / m
        r = round(d)
        if r >= 2 and abs(d - r) < 0.01:
            return ('op', 'sdiv', strip_ext(n), C(r))
        return None

    def div_fixup(self, v):
        """q + (q >> 31): the rounding fix-up of a signed division by a constant -> q (also when the
        division needs no shift: q = mulhi(n, magic))."""
        if v[0] == 'op' and v[1] == 'add':
            for x, y in ((v[2], v[3]), (v[3], v[2])):
                y0 = strip_ext(y)
                if y0[0] == 'op' and y0[1] in ('shr', 'sar') and y0[3] in (C(31), C(63)) and \
                        strip_ext(y0[2]) == strip_ext(x):
                    q = strip_ext(x)
                    if q[0] == 'op' and q[1] == 'sdiv':
                        return x
                    if q[0] == 'op' and q[1].startswith('mulhi'):
                        d = self.magic_div(q[2], q[3], int(q[1][5:]), 0)
                        if d is not None:
                            return d
        return v

    def is_local_jump(self, pc, t):
        if t in self.named:
            return False
        cur = self.im.primary_function(pc)
        dst = self.im.primary_function(t)
        if cur is not None:
            return dst == cur
        # leaf function (no unwind data): short jumps stay inside
        return dst is None and abs(t - pc) < 0x100

    def call_symbolic(self, st, t):
        if t[0] == "import":
            self.opaque(st, "import:" + t[1], self.call_args(st))
        elif t[0] == "vcall":
            self.opaque(st, ('vcall', t[1], t[2]), self.call_args(st))
        else:
            self.opaque(st, ('icall', t[1]), self.call_args(st))

    def do_ret(self, st, v):
        if v[0] == 'ret':
            st.depth -= 1
            st.fid = st.frames[-1][4] if st.frames else 0
            st.frames = st.frames[:-1]
            st.pc = v[1]
            return "jump"
        if v == ('sym', 'retaddr'):
            return "ret"
        raise Abort("return to %s" % (v[0],))
