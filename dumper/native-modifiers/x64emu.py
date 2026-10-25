"""A minimal x86-64 emulator (the MSVC code of Dota's DLLs) on top of capstone, for offline reading of registration code.

Not a real CPU: it executes the subset of instructions initialisation code needs (mov/lea/
arithmetic/jumps/calls/SSE moves/rep stos/movs). Sparse memory: the DLL image (a writable copy),
everything else is 4 KB pages that appear on first access (read as zeros). Nothing fails:
an unknown address reads zeros, an unknown call is a stub returning a "fake object" (whose virtual table
records every call). Imports of the DLL are replaced with stubs by name.

    emu = Emu(path)                       # the image at its ImageBase
    obj = emu.fake_object("VM")           # an object whose virtual calls are recorded in emu.vcalls
    emu.call(va, rcx=obj, budget=2_000_000)

Ported from dota-metamod/tools/x64emu.py; used by script_api.py.
"""
import struct

from pe import Image
from capstone import CS_ARCH_X86, CS_MODE_64, CS_OP_IMM, CS_OP_MEM, CS_OP_REG, Cs

MASK = {1: 0xFF, 2: 0xFFFF, 4: 0xFFFFFFFF, 8: 0xFFFFFFFFFFFFFFFF, 16: (1 << 128) - 1}
SIGN = {1: 0x80, 2: 0x8000, 4: 0x80000000, 8: 0x8000000000000000}

HEAP_BASE = 0x0000_1000_0000_0000
STACK_TOP = 0x0000_7FF0_0000_0000
IMPORT_BASE = 0x0000_6000_0000_0000   # import cells: IMPORT_BASE + i*0x100 (as code: stub i, as data: an object)
FAKE_VT = 0x0000_6100_0000_0000       # tables of fake objects: FAKE_VT + id*0x1000
FAKE_FN = 0x0000_6200_0000_0000       # "functions" of fake objects: FAKE_FN + id*0x1000 + slot*8
SENTINEL = 0x0000_6FFF_FFFF_0000      # return address of the emulation

GPR = ["rax", "rcx", "rdx", "rbx", "rsp", "rbp", "rsi", "rdi"] + ["r%d" % i for i in range(8, 16)]


def _regmap():
    m = {}
    for r in GPR:
        m[r] = (r, 8, 0)
    legacy = {"rax": "a", "rbx": "b", "rcx": "c", "rdx": "d"}
    for r, l in legacy.items():
        m["e%sx" % l] = (r, 4, 0)
        m["%sx" % l] = (r, 2, 0)
        m["%sl" % l] = (r, 1, 0)
        m["%sh" % l] = (r, 1, 8)
    for r, n in (("rsi", "si"), ("rdi", "di"), ("rbp", "bp"), ("rsp", "sp")):
        m["e" + n] = (r, 4, 0)
        m[n] = (r, 2, 0)
        m[n + "l"] = (r, 1, 0)
    for i in range(8, 16):
        r = "r%d" % i
        m[r + "d"] = (r, 4, 0)
        m[r + "w"] = (r, 2, 0)
        m[r + "b"] = (r, 1, 0)
    return m


REGMAP = _regmap()

CC = {
    "o": lambda f: f["of"], "no": lambda f: not f["of"],
    "b": lambda f: f["cf"], "c": lambda f: f["cf"], "nae": lambda f: f["cf"],
    "ae": lambda f: not f["cf"], "nb": lambda f: not f["cf"], "nc": lambda f: not f["cf"],
    "e": lambda f: f["zf"], "z": lambda f: f["zf"], "ne": lambda f: not f["zf"], "nz": lambda f: not f["zf"],
    "be": lambda f: f["cf"] or f["zf"], "na": lambda f: f["cf"] or f["zf"],
    "a": lambda f: not (f["cf"] or f["zf"]), "nbe": lambda f: not (f["cf"] or f["zf"]),
    "s": lambda f: f["sf"], "ns": lambda f: not f["sf"],
    "p": lambda f: f["pf"], "pe": lambda f: f["pf"], "np": lambda f: not f["pf"], "po": lambda f: not f["pf"],
    "l": lambda f: f["sf"] != f["of"], "nge": lambda f: f["sf"] != f["of"],
    "ge": lambda f: f["sf"] == f["of"], "nl": lambda f: f["sf"] == f["of"],
    "le": lambda f: f["zf"] or f["sf"] != f["of"], "ng": lambda f: f["zf"] or f["sf"] != f["of"],
    "g": lambda f: not f["zf"] and f["sf"] == f["of"], "nle": lambda f: not f["zf"] and f["sf"] == f["of"],
}

SSE_MOV16 = {"movaps", "movups", "movdqa", "movdqu", "movapd", "movupd", "lddqu", "vmovups", "vmovaps",
             "vmovdqu", "vmovdqa"}
SSE_XOR = {"xorps", "xorpd", "pxor"}


class Stop(Exception):
    pass


class Emu:
    def __init__(self, path, import_handlers=None, image=None):
        im = image or Image(path)
        self.path = path
        self.base = im.base
        self.img = bytearray(im.mem)
        self.end = self.base + len(self.img)
        self.code = [(self.base + a, self.base + a + n) for a, n in im.code_sections()]
        self.funcs = list(im.funcs)
        self.pages = {}
        self.dirty = set()           # pages of the image that were written
        self.heap = HEAP_BASE
        self.blocks = []             # (address, size) of allocated memory
        self.alloc_site = {}         # block address -> call chain at the allocation
        self.imports = {}            # index -> name
        self.import_index = {}       # name -> index
        for idx, (cell, name) in enumerate(sorted(im.imports.items())):
            self.imports[idx] = name
            self.import_index[name] = idx
            struct.pack_into("<Q", self.img, cell, IMPORT_BASE + idx * 0x100)
        self.fakes = []              # id -> name of the fake object
        self.fake_ptr = []           # id -> address of the object
        self.vcalls = []             # (object name, slot, registers, rsp)
        self.import_handlers = import_handlers or {}
        self.vcall_handlers = {}     # object name -> f(emu, slot) -> rax value or None
        self.profile = None          # collections.Counter(): instructions executed per function
        self.on_external = None      # f(emu, target) -> rax value or None; sees every external call
        self.call_hooks = {}         # VA of an image function -> f(emu) -> rax: f runs instead of the call
        # an object behind every import cell, for imported data (g_pMemAlloc and the like)
        for i, name in self.imports.items():
            obj = self.fake_object("imp:" + name)
            self.w(IMPORT_BASE + i * 0x100, 8, obj)
        self.md = Cs(CS_ARCH_X86, CS_MODE_64)
        self.md.detail = True
        self.cache = {}
        self.unknown = {}            # mnemonics the emulator does not know -> count
        self.log = []
        self.reset_cpu()

    # ------------------------------------------------------------------ memory
    def _page(self, a):
        p = self.pages.get(a >> 12)
        if p is None:
            p = self.pages[a >> 12] = bytearray(0x1000)
        return p

    def rb(self, a, n):
        if self.base <= a and a + n <= self.end:
            return bytes(self.img[a - self.base:a - self.base + n])
        if FAKE_VT <= a < FAKE_FN:
            out = bytearray()
            for k in range(a & ~7, a + n + 7 & ~7, 8):
                oid, slot = (k - FAKE_VT) >> 12, (k & 0xFFF) >> 3
                out += struct.pack("<Q", FAKE_FN + (oid << 12) + slot * 8)
            off = a & 7
            return bytes(out[off:off + n])
        out = bytearray()
        while n > 0:
            o = a & 0xFFF
            k = min(n, 0x1000 - o)
            out += self._page(a)[o:o + k]
            a += k
            n -= k
        return bytes(out)

    def wb(self, a, data):
        n = len(data)
        if self.base <= a and a + n <= self.end:
            o = a - self.base
            self.img[o:o + n] = data
            for p in range(o >> 12, (o + n - 1 >> 12) + 1):
                self.dirty.add(p)
            return
        i = 0
        while i < n:
            o = a & 0xFFF
            k = min(n - i, 0x1000 - o)
            self._page(a)[o:o + k] = data[i:i + k]
            a += k
            i += k

    def r(self, a, n):
        return int.from_bytes(self.rb(a, n), "little")

    def w(self, a, n, v):
        self.wb(a, (v & MASK[n]).to_bytes(n, "little"))

    def q(self, a):
        return self.r(a, 8)

    def cstr(self, a, limit=512):
        if not a:
            return None
        out = bytearray()
        while len(out) < limit:
            c = self.rb(a + len(out), 1)[0]
            if c == 0:
                break
            out.append(c)
        return out.decode("utf-8", "replace")

    def alloc(self, size, tag=None):
        size = max(16, (size + 15) & ~15)
        a = self.heap
        self.heap += size + 0x10
        self.blocks.append((a, size, tag))
        # who allocated: the chain of functions (VA) at the time of the allocation, the last 4
        self.alloc_site[a] = [f[0] for f in getattr(self, "stack", [])[-4:]]
        return a

    def fake_object(self, name):
        oid = len(self.fakes)
        a = self.alloc(0x400, "fake:" + name)
        self.w(a, 8, FAKE_VT + (oid << 12))
        self.fakes.append(name)
        self.fake_ptr.append(a)
        return a

    def in_image(self, a):
        return self.base <= a < self.end

    def is_code(self, a):
        return any(s <= a < e for s, e in self.code)

    # ------------------------------------------------------------------ cpu
    def reset_cpu(self):
        self.regs = {r: 0 for r in GPR}
        self.xmm = [0] * 16
        self.f = {"zf": False, "sf": False, "cf": False, "of": False, "pf": False}

    def get(self, name):
        full, size, shift = REGMAP[name]
        return (self.regs[full] >> shift) & MASK[size]

    def set(self, name, v):
        full, size, shift = REGMAP[name]
        v &= MASK[size]
        if size == 8:
            self.regs[full] = v
        elif size == 4:
            self.regs[full] = v          # a write to a 32-bit register clears the upper half
        else:
            m = MASK[size] << shift
            self.regs[full] = (self.regs[full] & ~m) | (v << shift)

    def decode(self, a):
        ins = self.cache.get(a)
        if ins is None:
            code = self.rb(a, 16)
            got = next(self.md.disasm(code, a, 1), None)
            if got is None:
                raise Stop("undecodable %x" % (a - self.base))
            ins = self.cache[a] = got
        return ins

    def ea(self, ins, op):
        m = op.mem
        a = m.disp
        if m.base:
            bn = ins.reg_name(m.base)
            a += ins.address + ins.size if bn == "rip" else self.get(bn)
        if m.index:
            a += self.get(ins.reg_name(m.index)) * m.scale
        if m.segment and ins.reg_name(m.segment) == "gs":
            a += 0x0000_5000_0000_0000   # TEB: zeros (stack limit 0, empty TLS)
        return a & MASK[8]

    def rd(self, ins, op, size=None):
        size = size or op.size
        if op.type == CS_OP_REG:
            name = ins.reg_name(op.reg)
            if name.startswith("xmm") or name.startswith("ymm"):
                return self.xmm[int(name[3:])] & MASK[min(size, 16)]
            return self.get(name)
        if op.type == CS_OP_IMM:
            return op.imm & MASK[size]
        return self.r(self.ea(ins, op), size)

    def wr(self, ins, op, v, size=None):
        size = size or op.size
        if op.type == CS_OP_REG:
            name = ins.reg_name(op.reg)
            if name.startswith("xmm") or name.startswith("ymm"):
                i = int(name[3:])
                if size >= 16:
                    self.xmm[i] = v & MASK[16]
                else:
                    self.xmm[i] = (self.xmm[i] & ~MASK[size]) | (v & MASK[size])
                return
            self.set(name, v)
        else:
            self.w(self.ea(ins, op), size, v)

    def flags_logic(self, v, size):
        v &= MASK[size]
        self.f.update(zf=v == 0, sf=bool(v & SIGN[size]), cf=False, of=False, pf=bin(v & 0xFF).count("1") % 2 == 0)

    def flags_add(self, a, b, size, carry=0):
        r = a + b + carry
        m = MASK[size]
        res = r & m
        self.f.update(zf=res == 0, sf=bool(res & SIGN[size]), cf=r > m,
                      of=bool(~(a ^ b) & (a ^ res) & SIGN[size]), pf=bin(res & 0xFF).count("1") % 2 == 0)
        return res

    def flags_sub(self, a, b, size, borrow=0):
        m = MASK[size]
        res = (a - b - borrow) & m
        self.f.update(zf=res == 0, sf=bool(res & SIGN[size]), cf=a < b + borrow,
                      of=bool((a ^ b) & (a ^ res) & SIGN[size]), pf=bin(res & 0xFF).count("1") % 2 == 0)
        return res

    def push(self, v):
        self.regs["rsp"] -= 8
        self.w(self.regs["rsp"], 8, v)

    def pop(self):
        v = self.q(self.regs["rsp"])
        self.regs["rsp"] += 8
        return v

    @staticmethod
    def sx(v, size):
        return v - (1 << (8 * size)) if v & SIGN[size] else v

    # ------------------------------------------------------------------ calls
    def external(self, target):
        """A call outside the image's code. Returns the value of rax."""
        if self.on_external:
            v = self.on_external(self, target)
            if v is not None:
                return v
        if IMPORT_BASE <= target < IMPORT_BASE + 0x100 * (len(self.imports) + 1):
            idx = (target - IMPORT_BASE) // 0x100
            name = self.imports.get(idx, "?")
            h = self.import_handlers.get(name)
            if h:
                v = h(self)
                return 0 if v is None else v
            return 0
        if FAKE_FN <= target < SENTINEL:
            oid, slot = (target - FAKE_FN) >> 12, ((target - FAKE_FN) & 0xFFF) >> 3
            name = self.fakes[oid] if oid < len(self.fakes) else "?"
            regs = dict(self.regs)
            self.vcalls.append((name, slot, regs, [self.q(self.regs["rsp"] + 8 * k) for k in range(5, 12)]))
            h = self.vcall_handlers.get(name) or self.vcall_handlers.get("*")
            if h:
                v = h(self, name, slot)
                if v is not None:
                    return v
            return self.fake_object("ret:%s.%d" % (name, slot))
        return self.fake_object("ret:%x" % target)

    def call(self, target, budget=3_000_000, frame_budget=200_000, maxdepth=40, skip=None, **regs):
        """Run function target (VA) until it returns. Argument registers are keyword arguments.

        A nested call that failed (int3/ud2/int 0x29) or ran more than frame_budget instructions with its
        callees is "thrown": it returns to its caller with rax = 0 (like an exception), and the function is
        remembered in self.skip and not executed again (the call becomes a stub). This way registration code
        gets past CRT/std/protobuf initialisers that need real data."""
        if skip is not None:
            self.skip = set(skip)
        elif not hasattr(self, "skip"):
            self.skip = set()
        self.reset_cpu()
        self.regs["rsp"] = STACK_TOP - 0x10000
        for k, v in regs.items():
            self.set(k, v)
        self.push(SENTINEL)
        rip = target
        steps = 0
        self.unwound = []
        nonvol = ("rbx", "rbp", "rsi", "rdi", "r12", "r13", "r14", "r15")
        # function, rsp after the return address, step it started at, saved registers (as unwinding restores them)
        frames = [[target, self.regs["rsp"], 0, None]]
        self.stack = frames

        def unwind(why, level=None):
            level = len(frames) - 1 if level is None else level
            fr = frames[level]
            del frames[level:]
            self.unwound.append((fr[0] - self.base, why))
            self.skip.add(fr[0])
            if why == "budget":
                for other in frames:
                    other[2] = steps
            self.regs["rsp"] = fr[1]
            self.regs["rax"] = 0
            self.regs.update(fr[3])
            return self.pop()

        while True:
            if rip == SENTINEL:
                self.steps = steps
                return self.regs["rax"]
            if not self.in_image(rip) or not self.is_code(rip):
                # a jump (jmp / tail call) into external code: like a call + ret
                self.regs["rax"] = self.external(rip)
                rip = self.pop()
                if len(frames) > 1:
                    frames.pop()
                continue
            steps += 1
            if self.profile is not None:
                self.profile[frames[-1][0] - self.base] += 1
                if len(frames) == 1: self.profile[("ip", rip - self.base)] += 1
            if steps > budget:
                raise Stop("budget of %d instructions used up at %x (calls: %s)" % (
                    budget, rip - self.base, " > ".join("%x" % (f[0] - self.base) for f in frames)))
            if (steps & 0x3FF) == 0 and len(frames) > 1:
                over = [i for i in range(1, len(frames)) if steps - frames[i][2] > frame_budget]
                if over:
                    rip = unwind("budget", over[-1])
                    continue
            ins = self.decode(rip)
            nxt = rip + ins.size
            mn = ins.mnemonic
            if mn.startswith("lock "):
                mn = mn[5:]
            ops = ins.operands
            if mn.startswith("rep ") or mn.startswith("repe ") or mn.startswith("repne "):
                self.rep(ins)
                rip = nxt
                continue
            if mn == "call" or mn == "jmp":
                t = self.rd(ins, ops[0], 8)
                if mn == "call":
                    if t in self.call_hooks:
                        v = self.call_hooks[t](self)
                        self.regs["rax"] = 0 if v is None else v
                        rip = nxt
                        continue
                    if t in self.skip or len(frames) > maxdepth or not self.in_image(t) or not self.is_code(t):
                        self.regs["rax"] = self.external(t) if not (self.in_image(t) and self.is_code(t)) else 0
                        rip = nxt
                        continue
                    self.push(nxt)
                    frames.append([t, self.regs["rsp"], steps, {r: self.regs[r] for r in nonvol}])
                    rip = t
                    continue
                rip = t
                continue
            if mn == "ret":
                rip = self.pop()
                if ops:
                    self.regs["rsp"] += ops[0].imm
                if len(frames) > 1:
                    frames.pop()
                continue
            if mn[0] == "j":
                if mn == "jrcxz" or mn == "jecxz":
                    take = self.get("rcx" if mn == "jrcxz" else "ecx") == 0
                else:
                    take = CC[mn[1:]](self.f)
                rip = self.rd(ins, ops[0], 8) if take else nxt
                continue
            if mn in ("int3", "ud2", "hlt", "int"):
                if len(frames) > 1:
                    rip = unwind(mn)
                    continue
                raise Stop("%s at %x" % (mn, rip - self.base))
            self.exec(ins, mn, ops)
            rip = nxt

    def rep(self, ins):
        mn = ins.mnemonic.split()[1]
        unit = {"b": 1, "w": 2, "d": 4, "q": 8}[mn[-1]]
        cnt = self.regs["rcx"]
        if cnt > 0x1000000:
            cnt = 0x1000000
        if mn.startswith("stos"):
            val = self.regs["rax"] & MASK[unit]
            self.wb(self.regs["rdi"], val.to_bytes(unit, "little") * cnt)
            self.regs["rdi"] += unit * cnt
        elif mn.startswith("movs"):
            data = self.rb(self.regs["rsi"], unit * cnt)
            self.wb(self.regs["rdi"], data)
            self.regs["rdi"] += unit * cnt
            self.regs["rsi"] += unit * cnt
        else:
            self.unknown[ins.mnemonic] = self.unknown.get(ins.mnemonic, 0) + 1
            return
        self.regs["rcx"] = 0

    def exec(self, ins, mn, ops):
        f = self.f
        if mn in ("mov", "movabs"):
            self.wr(ins, ops[0], self.rd(ins, ops[1], ops[0].size))
        elif mn == "lea":
            self.wr(ins, ops[0], self.ea(ins, ops[1]))
        elif mn == "movzx":
            self.wr(ins, ops[0], self.rd(ins, ops[1]))
        elif mn in ("movsx", "movsxd"):
            self.wr(ins, ops[0], self.sx(self.rd(ins, ops[1]), ops[1].size))
        elif mn in ("add", "adc", "sub", "sbb", "cmp"):
            s = ops[0].size
            a = self.rd(ins, ops[0])
            b = ops[1].imm & MASK[s] if ops[1].type == CS_OP_IMM else self.rd(ins, ops[1])
            if mn in ("add", "adc"):
                res = self.flags_add(a, b, s, int(f["cf"]) if mn == "adc" else 0)
            else:
                res = self.flags_sub(a, b, s, int(f["cf"]) if mn == "sbb" else 0)
            if mn != "cmp":
                self.wr(ins, ops[0], res)
        elif mn in ("and", "or", "xor", "test"):
            s = ops[0].size
            a = self.rd(ins, ops[0])
            b = ops[1].imm & MASK[s] if ops[1].type == CS_OP_IMM else self.rd(ins, ops[1])
            res = a & b if mn in ("and", "test") else a | b if mn == "or" else a ^ b
            self.flags_logic(res, s)
            if mn != "test":
                self.wr(ins, ops[0], res)
        elif mn in ("inc", "dec"):
            s = ops[0].size
            cf = f["cf"]
            a = self.rd(ins, ops[0])
            res = self.flags_add(a, 1, s) if mn == "inc" else self.flags_sub(a, 1, s)
            f["cf"] = cf
            self.wr(ins, ops[0], res)
        elif mn == "neg":
            s = ops[0].size
            self.wr(ins, ops[0], self.flags_sub(0, self.rd(ins, ops[0]), s))
        elif mn == "not":
            self.wr(ins, ops[0], ~self.rd(ins, ops[0]))
        elif mn in ("shl", "sal", "shr", "sar", "rol", "ror"):
            s = ops[0].size
            a = self.rd(ins, ops[0])
            c = (self.rd(ins, ops[1], 1) if len(ops) > 1 else 1) & (0x3F if s == 8 else 0x1F)
            if c:
                if mn in ("shl", "sal"):
                    res = (a << c) & MASK[s]
                    f["cf"] = bool((a >> (8 * s - c)) & 1)
                elif mn == "shr":
                    res = a >> c
                    f["cf"] = bool((a >> (c - 1)) & 1)
                elif mn == "sar":
                    res = (self.sx(a, s) >> c) & MASK[s]
                    f["cf"] = bool((a >> (c - 1)) & 1)
                elif mn == "rol":
                    c %= 8 * s
                    res = ((a << c) | (a >> (8 * s - c))) & MASK[s]
                else:
                    c %= 8 * s
                    res = ((a >> c) | (a << (8 * s - c))) & MASK[s]
                if mn not in ("rol", "ror"):
                    f.update(zf=res == 0, sf=bool(res & SIGN[s]), pf=bin(res & 0xFF).count("1") % 2 == 0)
                self.wr(ins, ops[0], res)
        elif mn == "imul":
            if len(ops) == 1:
                s = ops[0].size
                v = self.sx(self.get({1: "al", 2: "ax", 4: "eax", 8: "rax"}[s]), s) * self.sx(self.rd(ins, ops[0]), s)
                self.set({1: "ax", 2: "ax", 4: "eax", 8: "rax"}[s], v)
                if s > 1:
                    self.set({2: "dx", 4: "edx", 8: "rdx"}[s], v >> (8 * s))
            else:
                s = ops[0].size
                a = self.sx(self.rd(ins, ops[1 if len(ops) == 3 else 0]), s)
                b = self.sx(self.rd(ins, ops[-1], ops[-1].size), ops[-1].size)
                self.wr(ins, ops[0], a * b)
        elif mn == "mul":
            s = ops[0].size
            v = self.get({1: "al", 2: "ax", 4: "eax", 8: "rax"}[s]) * self.rd(ins, ops[0])
            self.set({1: "ax", 2: "ax", 4: "eax", 8: "rax"}[s], v)
            if s > 1:
                self.set({2: "dx", 4: "edx", 8: "rdx"}[s], v >> (8 * s))
        elif mn in ("div", "idiv"):
            s = ops[0].size
            d = self.rd(ins, ops[0])
            if s == 1:
                n = self.get("ax")
            else:
                lo, hi = {2: ("ax", "dx"), 4: ("eax", "edx"), 8: ("rax", "rdx")}[s]
                n = (self.get(hi) << (8 * s)) | self.get(lo)
            if mn == "idiv":
                d = self.sx(d, s)
                n = n - (1 << (16 * s)) if n >> (16 * s - 1) else n
            if d == 0:
                raise Stop("division by 0 at %x" % (ins.address - self.base))
            qv = int(n / d)
            rv = n - qv * d
            if s == 1:
                self.set("al", qv)
                self.set("ah", rv)
            else:
                lo, hi = {2: ("ax", "dx"), 4: ("eax", "edx"), 8: ("rax", "rdx")}[s]
                self.set(lo, qv)
                self.set(hi, rv)
        elif mn == "cdq":
            self.set("edx", 0xFFFFFFFF if self.get("eax") & SIGN[4] else 0)
        elif mn == "cqo":
            self.set("rdx", MASK[8] if self.regs["rax"] & SIGN[8] else 0)
        elif mn == "cdqe":
            self.set("rax", self.sx(self.get("eax"), 4))
        elif mn == "cwde":
            self.set("eax", self.sx(self.get("ax"), 2))
        elif mn == "push":
            self.push(self.rd(ins, ops[0], 8) if ops[0].type != CS_OP_IMM else self.sx(ops[0].imm & MASK[4], 4))
        elif mn == "pop":
            self.wr(ins, ops[0], self.pop())
        elif mn.startswith("set"):
            self.wr(ins, ops[0], 1 if CC[mn[3:]](f) else 0)
        elif mn.startswith("cmov"):
            if CC[mn[4:]](f):
                self.wr(ins, ops[0], self.rd(ins, ops[1]))
            elif ops[0].size == 4:
                self.wr(ins, ops[0], self.rd(ins, ops[0]))
        elif mn == "xchg":
            a, b = self.rd(ins, ops[0]), self.rd(ins, ops[1])
            self.wr(ins, ops[0], b)
            self.wr(ins, ops[1], a)
        elif mn in ("xadd",):
            a, b = self.rd(ins, ops[0]), self.rd(ins, ops[1])
            self.wr(ins, ops[1], a)
            self.wr(ins, ops[0], self.flags_add(a, b, ops[0].size))
        elif mn == "cmpxchg":
            s = ops[0].size
            acc = {1: "al", 2: "ax", 4: "eax", 8: "rax"}[s]
            cur = self.rd(ins, ops[0])
            self.flags_sub(self.get(acc), cur, s)
            if f["zf"]:
                self.wr(ins, ops[0], self.rd(ins, ops[1]))
            else:
                self.set(acc, cur)
        elif mn in ("bt", "bts", "btr"):
            s = ops[0].size
            bit = self.rd(ins, ops[1]) % (8 * s)
            v = self.rd(ins, ops[0])
            f["cf"] = bool((v >> bit) & 1)
            if mn == "bts":
                self.wr(ins, ops[0], v | (1 << bit))
            elif mn == "btr":
                self.wr(ins, ops[0], v & ~(1 << bit))
        elif mn in ("bsf", "tzcnt", "bsr", "lzcnt"):
            s = ops[0].size
            v = self.rd(ins, ops[1])
            if mn in ("bsf", "tzcnt"):
                res = (v & -v).bit_length() - 1 if v else (8 * s if mn == "tzcnt" else 0)
            elif mn == "bsr":
                res = v.bit_length() - 1 if v else 0
            else:
                res = 8 * s - v.bit_length()
            f["zf"] = v == 0
            self.wr(ins, ops[0], res)
        elif mn in SSE_MOV16:
            self.wr(ins, ops[0], self.rd(ins, ops[1], 16), 16)
        elif mn in ("movq", "vmovq"):
            v = self.rd(ins, ops[1], 8)
            if ops[0].type == CS_OP_REG and ins.reg_name(ops[0].reg).startswith("xmm"):
                self.wr(ins, ops[0], v, 16)
            else:
                self.wr(ins, ops[0], v, 8)
        elif mn in ("movd", "vmovd"):
            v = self.rd(ins, ops[1], 4)
            if ops[0].type == CS_OP_REG and ins.reg_name(ops[0].reg).startswith("xmm"):
                self.wr(ins, ops[0], v, 16)
            else:
                self.wr(ins, ops[0], v, 4)
        elif mn in ("movss", "movsd") and any(o.type == CS_OP_REG and ins.reg_name(o.reg).startswith("xmm") for o in ops):
            n = 4 if mn == "movss" else 8
            v = self.rd(ins, ops[1], n)
            if ops[0].type == CS_OP_REG and ops[1].type == CS_OP_MEM:
                self.wr(ins, ops[0], v, 16)
            else:
                self.wr(ins, ops[0], v, n)
        elif mn in SSE_XOR:
            self.wr(ins, ops[0], self.rd(ins, ops[0], 16) ^ self.rd(ins, ops[1], 16), 16)
        elif mn in ("pand", "andps", "andpd"):
            self.wr(ins, ops[0], self.rd(ins, ops[0], 16) & self.rd(ins, ops[1], 16), 16)
        elif mn in ("por", "orps", "orpd"):
            self.wr(ins, ops[0], self.rd(ins, ops[0], 16) | self.rd(ins, ops[1], 16), 16)
        elif mn in ("punpcklqdq", "unpcklpd", "movlhps"):
            a = self.rd(ins, ops[0], 16) & MASK[8]
            b = self.rd(ins, ops[1], 16 if ops[1].type == CS_OP_REG else 8) & MASK[8]
            self.wr(ins, ops[0], a | (b << 64), 16)
        elif mn in ("movhps", "movhpd"):
            if ops[0].type == CS_OP_REG:
                a = self.rd(ins, ops[0], 16) & MASK[8]
                self.wr(ins, ops[0], a | (self.rd(ins, ops[1], 8) << 64), 16)
            else:
                self.wr(ins, ops[0], self.rd(ins, ops[1], 16) >> 64, 8)
        elif mn in ("movlps", "movlpd"):
            if ops[0].type == CS_OP_REG:
                a = self.rd(ins, ops[0], 16) & ~MASK[8]
                self.wr(ins, ops[0], a | self.rd(ins, ops[1], 8), 16)
            else:
                self.wr(ins, ops[0], self.rd(ins, ops[1], 16) & MASK[8], 8)
        elif mn in ("pcmpeqb", "pcmpeqw", "pcmpeqd", "pcmpeqq"):
            lane = {"b": 1, "w": 2, "d": 4, "q": 8}[mn[-1]]
            a = self.rd(ins, ops[0], 16).to_bytes(16, "little")
            b = self.rd(ins, ops[1], 16).to_bytes(16, "little")
            out = b"".join((b"\xff" * lane) if a[i:i + lane] == b[i:i + lane] else (b"\0" * lane)
                           for i in range(0, 16, lane))
            self.wr(ins, ops[0], int.from_bytes(out, "little"), 16)
        elif mn == "pmovmskb":
            v = self.rd(ins, ops[1], 16).to_bytes(16, "little")
            self.wr(ins, ops[0], sum(1 << i for i in range(16) if v[i] & 0x80), 4)
        elif mn in ("movmskps", "movmskpd"):
            lane = 4 if mn == "movmskps" else 8
            v = self.rd(ins, ops[1], 16)
            self.wr(ins, ops[0], sum(1 << k for k in range(16 // lane) if (v >> (8 * lane * (k + 1) - 1)) & 1), 4)
        elif mn in ("psrldq", "pslldq"):
            c = min(ops[1].imm, 16) * 8
            v = self.rd(ins, ops[0], 16)
            self.wr(ins, ops[0], (v >> c) if mn == "psrldq" else (v << c), 16)
        elif mn == "pshufd":
            v = self.rd(ins, ops[1], 16)
            imm = ops[2].imm
            d = [(v >> (32 * ((imm >> (2 * k)) & 3))) & MASK[4] for k in range(4)]
            self.wr(ins, ops[0], d[0] | d[1] << 32 | d[2] << 64 | d[3] << 96, 16)
        elif mn in ("punpcklbw", "punpcklwd", "punpckldq"):
            lane = {"bw": 1, "wd": 2, "dq": 4}[mn[-2:]]
            a = self.rd(ins, ops[0], 16).to_bytes(16, "little")
            b = self.rd(ins, ops[1], 16).to_bytes(16, "little")
            out = b"".join(a[i:i + lane] + b[i:i + lane] for i in range(0, 8, lane))
            self.wr(ins, ops[0], int.from_bytes(out, "little"), 16)
        elif mn in ("pminub", "pmaxub"):
            a = self.rd(ins, ops[0], 16).to_bytes(16, "little")
            b = self.rd(ins, ops[1], 16).to_bytes(16, "little")
            fn = min if mn == "pminub" else max
            self.wr(ins, ops[0], int.from_bytes(bytes(fn(x, y) for x, y in zip(a, b)), "little"), 16)
        elif mn == "ptest":
            a, b = self.rd(ins, ops[0], 16), self.rd(ins, ops[1], 16)
            f.update(zf=(a & b) == 0, cf=(~a & b & MASK[16]) == 0, sf=False, of=False)
        elif mn in ("nop", "endbr64", "pause", "lfence", "mfence", "sfence", "prefetcht0", "prefetchw", "cld",
                    "int1", "fnop", "lock", "clflush"):
            pass
        elif mn in ("stosb", "stosw", "stosd", "stosq", "movsb", "movsw", "movsd", "movsq"):
            unit = {"b": 1, "w": 2, "d": 4, "q": 8}[mn[-1]]
            if mn.startswith("stos"):
                self.w(self.regs["rdi"], unit, self.regs["rax"])
            else:
                self.wb(self.regs["rdi"], self.rb(self.regs["rsi"], unit))
                self.regs["rsi"] += unit
            self.regs["rdi"] += unit
        else:
            # unknown (usually floating point): the result is zero rather than garbage
            self.unknown[mn] = self.unknown.get(mn, 0) + 1
            if ops and ops[0].type == CS_OP_REG and ops[0].access & 2:
                name = ins.reg_name(ops[0].reg)
                if name.startswith("xmm") or name.startswith("ymm"):
                    self.xmm[int(name[3:])] = 0
                elif name in REGMAP:
                    self.set(name, 0)

    # ------------------------------------------------------------------ .pdata
    def primary_function(self, rva):
        """Start of a function (RVA) by .pdata, following chained tails (UNW_FLAG_CHAININFO)."""
        import bisect
        i = bisect.bisect_right(self.funcs, (rva, 1 << 62, 0)) - 1
        if i < 0 or not (self.funcs[i][0] <= rva < self.funcs[i][1]):
            return None
        begin, _, unwind = self.funcs[i]
        for _ in range(64):
            flags = self.img[unwind] >> 3
            if not flags & 4:
                return begin
            count = self.img[unwind + 2]
            off = unwind + 4 + 2 * ((count + 1) & ~1)
            begin, _, unwind = struct.unpack_from("<III", self.img, off)
        return begin
