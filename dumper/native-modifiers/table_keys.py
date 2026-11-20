#!/usr/bin/env python3
"""Keys Dota 2's server.dll reads from Lua table arguments of VScript functions, read offline (no game).

    python3 -I table_keys.py --dll server.dll [--out dumper/table_keys.json] [--version 6986] [--debug]

Run by dumper/table-keys.mts after every dump (npm run dump:table-keys alone); build/vscripts/table-keys.ts
compares the result with the documented table types (files/vscripts/table_keys.json) and adds the keys they
lack to files/vscripts/api-types.json.

For every VScript method / global function (script_api.script_classes: the native implementation of each
binding) the implementation and its direct callees (to --depth levels) are disassembled with capstone and a
small forward data-flow analysis follows, per register and stack slot: string literals, g_pScriptVM, its
vtable and slot pointers, the incoming arguments, stack addresses, constants and a few call results. What is
collected:

  (a) virtual calls on g_pScriptVM with a string literal as key (r8): IScriptVM::GetValue / SetValue / ...;
      the slots are calibrated from the code itself (GetValue = the slot whose out-variant (r9) is passed to
      another slot, ReleaseValue, afterwards; the table-iteration slot = GetKeyValue; SetValue = the most
      used remaining slot with a literal key and a variant);
  (b) KeyValues imports (tier0.dll) with a string literal as key (rdx): GetInt / GetFloat / FindKey / ...
      (readers) and SetInt / SetString / FindKey(create) / ... (writers).

Every finding carries the object it was made on, traced back through the callees to the root: a VM call is
"traced" when its scope is an argument of the root (the Lua table, or a nested table read from it), a
KeyValues call when its object is a KeyValues filled from the table (a loop over the table with
GetKeyValue that writes non-literal keys into it) or the KeyValues argument of an extra root (OnCreated(kv)).
Untraced findings get the suffix "_untraced". Helper functions that take the key as an argument (wrappers)
are resolved at their call sites (per-function summaries in terms of the arguments). Shared functions
(many callers) and huge functions only contribute findings that depend on their arguments.

Extra roots (EXTRA_ROOTS): functions where the keys of a table are read outside the binding, e.g.
CreateIllusions -> CDOTA_Modifier_Illusion::OnCreated / OnRefresh (vtable by RTTI, slot by the Lua
modifier's callback names); the Set*Filter methods of CDOTABaseGameMode -> the functions that invoke the
filter (they load the field the setter stores the function into, and fill / read back the event table).
"""
import argparse
import bisect
import heapq
import collections
import json
import os
import re
import struct
import sys
import time
import types

HERE = os.path.dirname(os.path.abspath(__file__))   # pe.py, script_api.py, modifiers.py, x64emu.py

# Keys every working analysis finds (function -> keys). Missing ones mean the analysis broke on this build
# (a calibration or pattern that no longer matches): the run fails and the previous file is kept, instead
# of a changelog that removes every key and adds them all back with the next build.
ANCHORS = {
    "_G.ApplyDamage": ("victim", "attacker", "damage", "damage_type"),
    "_G.CreateIllusions": ("outgoing_damage", "incoming_damage", "bounty_base"),
    "CDOTABaseGameMode.SetDamageFilter": ("damage",),
    "_G.TraceLine": ("startpos", "endpos"),
}

# ------------------------------------------------------------------ registers / operands
GPR = ["rax", "rcx", "rdx", "rbx", "rsp", "rbp", "rsi", "rdi"] + ["r%d" % i for i in range(8, 16)]
SUB = {}
for _r in GPR:
    SUB[_r] = (_r, 8)
for _x in "abcd":
    SUB["e%sx" % _x] = ("r%sx" % _x, 4)
    SUB["%sx" % _x] = ("r%sx" % _x, 2)
    SUB["%sl" % _x] = ("r%sx" % _x, 1)
    SUB["%sh" % _x] = ("r%sx" % _x, 1)
for _x in ("si", "di", "bp", "sp"):
    SUB["e" + _x] = ("r" + _x, 4)
    SUB[_x] = ("r" + _x, 2)
    SUB[_x + "l"] = ("r" + _x, 1)
for _i in range(8, 16):
    SUB["r%dd" % _i] = ("r%d" % _i, 4)
    SUB["r%dw" % _i] = ("r%d" % _i, 2)
    SUB["r%db" % _i] = ("r%d" % _i, 1)
ARGREGS = ["rcx", "rdx", "r8", "r9"]
VOLATILE = ("rax", "rcx", "rdx", "r8", "r9", "r10", "r11")
DYN = ("dyn",)    # a key that is not a constant (e.g. from a loop over the table)
NARGS = 8           # arguments recorded at a call: 4 registers + 4 stack slots
MEMRE = re.compile(r"^(?:(\w+) ptr )?(?:\w+:)?\[([^\]]*)\]$")
SIZES = {"byte": 1, "word": 2, "dword": 4, "qword": 8, "xmmword": 16, "ymmword": 32, "tbyte": 10}
NOWRITE = {"cmp", "test", "bt", "ucomiss", "ucomisd", "comiss", "comisd", "nop", "push", "prefetchw",
           "prefetcht0", "prefetcht1", "prefetcht2", "prefetchnta", "ptest", "vptest", "clflush", "lfence",
           "mfence", "sfence", "pause", "int3", "ud2", "vzeroupper", "fnstcw", "fldcw", "stmxcsr", "ldmxcsr"}

# ------------------------------------------------------------------ KeyValues imports
KV_READ = {"GetInt", "GetFloat", "GetUint64", "GetPtr", "GetColor", "GetDataType", "IsEmpty"}
KV_WRITE = {"SetInt", "SetFloat", "SetString", "SetPtr", "SetUint64", "SetColor", "SetBool", "AddInt",
            "AddFloat", "AddPtr", "AddString", "AddKey", "FindAndDeleteSubKey"}
DEMANGLED = re.compile(r"^\?(\w+)@KeyValues@@")


def kv_import(name):
    """(action, method) of a KeyValues import that takes a key in rdx, else None. action: get | set |
    findkey (FindKey(const char*, bool create): get or set by r8) | hfind (FindKey(HKeySymbol): no string) |
    ctor | new | copy (MakeCopy) | merge (MergeFrom: this <- rdx) | copyto (CopySubkeys: rdx <- this)."""
    if name.startswith("??0KeyValues@@QEAA@PEBD"):
        return ("ctor", "KeyValues")
    if name.startswith("??2KeyValues@@"):
        return ("new", "new")
    m = DEMANGLED.match(name)
    if not m:
        return None
    meth = m.group(1)
    if meth == "FindKey":
        if "HKeySymbol" in name:
            return ("hfind", meth)
        return ("findkey", meth) if "_N@Z" in name else ("get", meth)
    if meth in KV_READ:
        return ("get", meth)
    if meth in KV_WRITE:
        return ("set", meth)
    if meth == "MakeCopy":
        return ("copy", meth)
    if meth == "MergeFrom":
        return ("merge", meth)
    if meth == "CopySubkeys":
        return ("copyto", meth)
    return None


# ------------------------------------------------------------------ extra roots
EXTRA_ROOTS = {
    # Script_CreateIllusions copies the table into the KeyValues of "modifier_illusion"; the modifier reads
    # most of the keys in OnCreated(kv) / OnRefresh(kv)
    "_G.CreateIllusions": [
        {"rtti": "CDOTA_Modifier_Illusion", "callback": "OnCreated", "kv_arg": 1},
        {"rtti": "CDOTA_Modifier_Illusion", "callback": "OnRefresh", "kv_arg": 1},
        # the KeyValues reach AddNewModifier("modifier_illusion") through the spawn key "illusionKeyValues"
        # (GetPtr), which the analysis cannot follow: the generic modifier creation reads them too
        {"modifier_core": True},
    ],
}
MODIFIER_ROOT = "CDOTA_BaseNPC.AddNewModifier"
READ_TRACED = ("getvalue", "kv_get", "iter_cmp")


def modifier_core(an, roots):
    """(function, argument index) of the C++ AddNewModifier: the callee of Script_AddNewModifier that gets
    the KeyValues it filled from the table."""
    for r in roots.get(MODIFIER_ROOT, []):
        f = an.analyse(r["start"])
        kvs = {e[1] for e in f.events if e[0] == "kvctor"}
        for t, args, a in f.calls:
            for i, v in enumerate(args):
                if v in kvs:
                    return t, i
    return None, None
FILTER_CLASS = "CDOTABaseGameMode"
FILTER_METHOD = re.compile(r"^Set(\w+)Filter$")
VMREF = re.compile(rb"[\x48\x4c]\x8b[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]")


NONNULL = ("kvnew", "ret", "vmret", "vmval", "kvsub")
SMALL = ("c", "symkey")
CMP_IMPORTS = {"V_stricmp_fast", "_V_strncmp", "_V_strnicmp_fast", "V_stricmp", "V_strcmp", "_stricmp", "strcmp"}       # values that survive 8/16/32-bit registers and stores


def meet(a, b):
    """Values two paths agree on. A pointer the code null-checks (an allocation, a call result) meets the
    null of the failure path as the pointer: the analysis follows the success path."""
    out = {}
    for k, v in a.items():
        w = b.get(k)
        if w == v:
            out[k] = v
        elif w is not None and v is not None:
            if v == ("c", 0) and w[0] in NONNULL:
                out[k] = w
            elif w == ("c", 0) and v[0] in NONNULL:
                out[k] = v
    return out


class Func:
    __slots__ = ("start", "size", "events", "calls", "hfind", "fstores", "error", "rets", "snaps")


class Analyzer:
    def __init__(self, im, log=print):
        from capstone import CS_ARCH_X86, CS_MODE_64, Cs
        self.im = im
        self.log = log
        self.md = Cs(CS_ARCH_X86, CS_MODE_64)
        self.md.detail = False
        self.md.skipdata = False
        # functions: primary start -> [(begin, end)] (chained .pdata chunks of split functions)
        chunks = collections.defaultdict(list)
        for b, e, u in im.funcs:
            p = im.primary_function(b)
            chunks[p if p is not None else b].append((b, e))
        self.chunks = {p: sorted(c) for p, c in chunks.items()}
        self.starts = sorted(self.chunks)
        self.sizes = {p: sum(e - b for b, e in c) for p, c in self.chunks.items()}
        self.imports = im.imports
        self.kvimp = {cell: kv_import(n) for cell, n in im.imports.items() if kv_import(n)}
        self.vm_global = self.find_vm_global()
        self.cache = {}
        self.indeg = None
        self.cmp_cache = {}
        self.emu = None
        self.sym_globals = {}        # global -> key string of the HKeySymbol cached there
        self.field_marks = set()     # field offsets whose loads are marked ('field', off): filter handles

    # --- globals
    def find_vm_global(self):
        """g_pScriptVM: the global loaded into rcx just before the "Started VScript virtual machine" message
        (as script_api.find_vm_global, on RVAs)."""
        im = self.im
        pos = im.mem.find(b"VSCRIPT: Started VScript virtual machine")
        if pos < 0:
            raise RuntimeError("VScript VM message not found")
        lea = re.compile(rb"[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]")
        for a, n in im.code_sections():
            blob = im.mem[a:a + n]
            for m in lea.finditer(blob):
                p = a + m.start()
                if p + 7 + struct.unpack_from("<i", im.mem, p + 3)[0] != pos:
                    continue
                found = None
                for k in range(p - 0x30, p - 7):
                    if im.mem[k:k + 3] == b"\x48\x8b\x0d":
                        found = k + 7 + im.i32(k + 3)
                if found:
                    return found
        raise RuntimeError("g_pScriptVM not found")

    def in_degrees(self):
        """Number of direct call / jmp rel32 sites targeting every function start."""
        if self.indeg is not None:
            return self.indeg
        starts = set(self.starts)
        cnt = collections.Counter()
        mem = self.im.mem
        for a, n in self.im.code_sections():
            end = a + n - 5
            for op in (b"\xe8", b"\xe9"):
                i = mem.find(op, a, end)
                while i >= 0:
                    t = (i + 5 + struct.unpack_from("<i", mem, i + 1)[0]) & 0xFFFFFFFF
                    if t in starts:
                        cnt[t] += 1
                    i = mem.find(op, i + 1, end)
        self.indeg = cnt
        return cnt

    def function_of(self, rva):
        i = bisect.bisect_right(self.starts, rva) - 1
        if i < 0:
            return None
        p = self.starts[i]
        if p == rva:
            return p
        f = self.im.primary_function(rva)
        if f is not None:
            return f
        # a leaf function without unwind data: back to the int3 padding before it
        mem = self.im.mem
        q = rva
        while q > rva - 0x400 and not (mem[q - 1] == 0xCC and mem[q - 2] == 0xCC):
            q -= 1
        return q if q > rva - 0x400 else None

    def is_strcmp(self, t):
        """A string comparison (strcmp / stricmp): a small leaf function that, run in the emulator
        (x64emu.py), returns 0 for equal strings and non-zero for different ones."""
        if t in self.cmp_cache:
            return self.cmp_cache[t]
        res = False
        f = self.analyse(t)
        if not f.calls and not f.events and 0 < self.sizes.get(t, 0) <= 0x400:
            try:
                if self.emu is None:
                    from x64emu import Emu
                    self.emu = Emu(self.im.path, image=self.im)
                e = self.emu

                def s(x):
                    a = e.alloc(len(x) + 1)
                    e.wb(a, x.encode() + b"\0")
                    return a

                def run(x, y):
                    return e.call(e.base + t, rcx=s(x), rdx=s(y), budget=20000) & 0xFFFFFFFF

                res = (run("szItemName", "szItemName") == 0 and run("abc", "abd") != 0 and
                       run("abd", "abc") != 0 and run("abc", "") != 0 and run("", "") == 0)
            except Exception:
                res = False
        self.cmp_cache[t] = res
        return res

    def prescan_symbols(self):
        """Fill sym_globals before the analysis: HKeySymbols of keys are created once (in a static
        initialiser: KeyValuesSystem()->GetSymbolForString("key")) and stored in globals that other
        functions read. Every function calling the KeyValuesSystem import is analysed once."""
        cells = [c for c, n in self.imports.items() if n == "KeyValuesSystem"]
        funcs = set()
        mem = self.im.mem
        for cell in cells:
            for a, n in self.im.code_sections():
                i = mem.find(b"\xff\x15", a, a + n)
                while i >= 0:
                    if i + 6 + struct.unpack_from("<i", mem, i + 2)[0] == cell:
                        p = self.function_of(i)
                        if p is not None:
                            funcs.add(p)
                    i = mem.find(b"\xff\x15", i + 1, a + n)
        for p in sorted(funcs):
            self.analyse(p)
        self.cache.clear()
        return len(funcs)

    # --- decoding
    def decode(self, start):
        """[(addr, size, mnemonic, op_str)] of every chunk of the function (leaf functions without .pdata:
        up to the int3 padding)."""
        ranges = self.chunks.get(start)
        if not ranges:
            end = self.im.mem.find(b"\xcc\xcc", start, start + 0x2000)
            ranges = [(start, end if end > start else start + 0x200)]
        out = []
        for b, e in ranges:
            for ins in self.md.disasm_lite(self.im.mem[b:e], b):
                out.append(ins)
        return out, ranges

    # --- operands
    @staticmethod
    def parse_mem(s):
        m = MEMRE.match(s)
        if not m:
            return None
        size = SIZES.get(m.group(1), 8) if m.group(1) else 8
        base = index = None
        scale = 1
        disp = 0
        expr = m.group(2).replace(" - ", " + -")
        for t in expr.split(" + "):
            t = t.strip()
            if "*" in t:
                r, sc = t.split("*")
                index, scale = r, int(sc, 0)
            elif t.lstrip("-").startswith("0x") or t.lstrip("-").isdigit():
                disp += int(t, 0)
            else:
                base = t
        return size, base, index, scale, disp

    def analyse(self, start):
        """Direct events of one function (memoised)."""
        f = self.cache.get(start)
        if f is not None:
            return f
        f = Func()
        f.start, f.size = start, self.sizes.get(start, 0)
        f.events, f.calls, f.hfind, f.fstores, f.error, f.rets = [], [], 0, [], None, set()
        f.snaps = {}         # call site -> {(argument, offset): value} of structs on our stack passed to it
        self.cache[start] = f
        try:
            self._analyse(f)
        except Exception as ex:      # keep going: one odd function must not stop the run
            f.error = "%s: %s" % (type(ex).__name__, ex)
        return f

    def _analyse(self, f):
        insns, ranges = self.decode(f.start)
        if not insns:
            return
        inside = lambda a: any(b <= a < e for b, e in ranges)
        addrs = [i[0] for i in insns]
        index = {a: k for k, a in enumerate(addrs)}
        # leaders
        leaders = {insns[0][0]}
        for b, e in ranges:
            if b in index:
                leaders.add(b)
        for k, (a, sz, mn, op) in enumerate(insns):
            if mn.startswith("j") or mn in ("ret", "retn", "int3", "ud2"):
                if k + 1 < len(insns):
                    leaders.add(insns[k + 1][0])
                if mn != "jmp" or op.startswith("0x"):
                    if op.startswith("0x"):
                        t = int(op, 16)
                        if t in index:
                            leaders.add(t)
            elif k + 1 < len(insns) and insns[k + 1][0] != a + sz:
                leaders.add(insns[k + 1][0])         # chunk gap
        lead = sorted(leaders)
        blocks = []        # (first index, last index)
        for j, a in enumerate(lead):
            s = index[a]
            e = (index[lead[j + 1]] - 1) if j + 1 < len(lead) else len(insns) - 1
            blocks.append((s, e))
        bstart = {insns[s][0]: bi for bi, (s, e) in enumerate(blocks)}
        succ = [[] for _ in blocks]
        indirect = []
        for bi, (s, e) in enumerate(blocks):
            a, sz, mn, op = insns[e]
            nxt = bi + 1 if bi + 1 < len(blocks) and insns[e][0] + sz == insns[blocks[bi + 1][0]][0] else None
            if mn == "jmp":
                if op.startswith("0x"):
                    t = int(op, 16)
                    if t in bstart:
                        succ[bi].append(bstart[t])
                else:
                    indirect.append(bi)
            elif mn.startswith("j"):
                if op.startswith("0x"):
                    t = int(op, 16)
                    if t in bstart:
                        succ[bi].append(bstart[t])
                if nxt is not None:
                    succ[bi].append(nxt)
            elif mn in ("ret", "retn", "int3", "ud2"):
                pass
            elif nxt is not None:
                succ[bi].append(nxt)
        preds = [0] * len(blocks)
        for bi in range(len(blocks)):
            for t in succ[bi]:
                preds[t] += 1
        entry_state = {"rcx": ("arg", 0), "rdx": ("arg", 1), "r8": ("arg", 2), "r9": ("arg", 3), "_rsp": 0}
        for k in range(4, NARGS):
            entry_state[0x28 + 8 * (k - 4)] = ("arg", k)
        ins_state = [None] * len(blocks)
        ins_state[0] = dict(entry_state)
        out_state = [None] * len(blocks)
        work = [0]
        queued = {0}
        visits = collections.Counter()
        while work:
            bi = heapq.heappop(work)
            queued.discard(bi)
            visits[bi] += 1
            if visits[bi] > 6:
                continue
            st = dict(ins_state[bi])
            s, e = blocks[bi]
            for k in range(s, e + 1):
                self.step(f, st, insns[k], inside, None)
            out_state[bi] = st
            for t in succ[bi]:
                if ins_state[t] is None:
                    ins_state[t] = dict(st)
                    if t not in queued:
                        heapq.heappush(work, t)
                        queued.add(t)
                else:
                    m = meet(ins_state[t], st)
                    if m != ins_state[t]:
                        ins_state[t] = m
                        if t not in queued:
                            heapq.heappush(work, t)
                            queued.add(t)
            if not work:
                # blocks nothing reached (jump-table targets, handlers): the state of the last indirect
                # jump before them, else of the block before them
                for bj in range(len(blocks)):
                    if ins_state[bj] is None:
                        src = None
                        for bk in reversed(indirect):
                            if bk < bj and out_state[bk] is not None:
                                src = out_state[bk]
                                break
                        if src is None and bj > 0 and out_state[bj - 1] is not None:
                            src = out_state[bj - 1]
                        ins_state[bj] = dict(src) if src is not None else {"_rsp": None}
                        heapq.heappush(work, bj)
                        queued.add(bj)
                        break
        # final pass: events from the converged states
        for bi, (s, e) in enumerate(blocks):
            st = dict(ins_state[bi] or {})
            for k in range(s, e + 1):
                self.step(f, st, insns[k], inside, f)

    # --- values
    def rd(self, st, name, size=None):
        full, sz = SUB.get(name, (None, 0))
        if full is None:
            return None
        if full == "rsp":
            r = st.get("_rsp")
            return ("stk", r) if r is not None and sz == 8 else None
        v = st.get(full)
        if sz == 8:
            return v
        if v is not None and v[0] == "c":
            return ("c", v[1] & ((1 << (8 * sz)) - 1))
        if v is not None and v[0] == "symkey":
            return v
        return None

    def wr(self, st, name, v):
        full, sz = SUB.get(name, (None, 0))
        if full is None:
            return
        if full == "rsp":
            st["_rsp"] = v[1] if v is not None and v[0] == "stk" else None
            return
        if sz != 8 and v is not None and v[0] not in SMALL:
            v = None
        if v is None:
            st.pop(full, None)
        else:
            st[full] = v

    def slot_of(self, st, m):
        """Stack slot (offset from the entry rsp) a memory operand names, else None."""
        size, base, index, scale, disp = m
        if index is not None or base is None:
            return None
        if base == "rsp":
            r = st.get("_rsp")
            return None if r is None else r + disp
        bv = st.get(SUB.get(base, (base,))[0])
        if bv is not None and bv[0] == "stk":
            return bv[1] + disp
        return None

    def rip_target(self, ins, m):
        return (ins[0] + ins[1] + m[4]) & 0xFFFFFFFF

    def load(self, st, ins, m):
        size, base, index, scale, disp = m
        if base == "rip":
            t = self.rip_target(ins, m)
            if t == self.vm_global and size == 8:
                return ("vm",)
            if t in self.imports and size == 8:
                return ("imp", t)
            if t in self.sym_globals:
                return ("symkey", self.sym_globals[t])
            return None
        if index is not None or base is None:
            return None
        sl = self.slot_of(st, m)
        if sl is not None:
            v = st.get(sl)
            if v is not None and size != 8 and v[0] not in SMALL:
                return None
            return v
        bv = st.get(SUB.get(base, (base,))[0])
        if bv is not None and bv[0] == "symptr" and disp == 0:
            return ("symkey", bv[1])
        if size == 8 and disp in self.field_marks and (bv is None or bv[0] not in ("vm", "vmvt")):
            return ("field", disp)
        if bv is None or size != 8:
            return None
        if bv == ("vm",) and disp == 0:
            return ("vmvt",)
        if bv == ("vmvt",):
            return ("vmfn", disp)
        if bv[0] == "arg" and disp != 0 and size == 8 and 0 < disp < 0x1000:
            return ("fld", bv[1], disp)        # a field of a struct passed by pointer
        if bv == ("kvsys",) and disp == 0:
            return ("kvsysvt",)
        if bv == ("kvsysvt",):
            return ("ksymfn", disp)
        if bv[0] == "arg" and disp == 0:
            return ("avt", bv[1])          # the vtable of an argument (g_pScriptVM passed to a helper)
        if bv[0] == "avt":
            return ("avfn", bv[1], disp)
        if bv[0] == "a" and bv[1] == self.vm_global and disp == 0:
            return ("vm",)
        return None

    def opval(self, st, ins, s):
        if s in SUB:
            return self.rd(st, s)
        if s[:1].isdigit() or s.startswith("-0x") or s.startswith("-"):
            try:
                return ("c", int(s, 0) & 0xFFFFFFFFFFFFFFFF)
            except ValueError:
                return None
        m = self.parse_mem(s)
        if m is not None:
            return self.load(st, ins, m)
        return None

    def clobber_slots(self, st, ptr, span=0x10):
        """A callee may write through a pointer to our stack: forget the slots it points at (the incoming
        stack arguments, +0x28 and up, only when the pointer is inside them)."""
        if ptr is not None and ptr[0] == "stk":
            o = ptr[1]
            end = o + span if o >= 0x28 else min(o + span, 0x28)
            for k in [k for k in st if isinstance(k, int) and o <= k < end]:
                del st[k]

    def qual(self, f, v):
        """A value as it leaves the function: stack addresses are qualified with the function."""
        if v is None:
            return None
        if v[0] == "stk":
            return ("lstk", f.start, v[1])
        if v[0] == "vmval":
            return ("vmval", v[1], self.qual(f, v[2]), self.qual(f, v[3]), v[4])
        if v[0] == "kvsub":
            return ("kvsub", v[1], self.qual(f, v[2]))
        return v

    def call_args(self, st):
        args = [st.get(r) for r in ARGREGS]
        r = st.get("_rsp")
        for k in range(4, NARGS):
            args.append(st.get(r + 0x20 + 8 * (k - 4)) if r is not None else None)
        return args

    def do_call(self, f, st, ins, target, emit, tail=False):
        """target: ('imp', cell) | ('vmfn', off) | ('direct', rva) | None."""
        a = ins[0]
        args = self.call_args(st)
        ret = None
        if target is not None and target[0] == "imp":
            kv = self.kvimp.get(target[1])
            if self.imports.get(target[1]) == "KeyValuesSystem":
                ret = ("kvsys",)
            if emit and self.imports.get(target[1]) in CMP_IMPORTS:
                for v in args[:2]:
                    if v is not None and v[0] == "a":
                        f.events.append(("cmp", v, a))
            if kv is not None:
                action, meth = kv
                if action == "new":
                    ret = ("kvnew", a)
                elif action == "copy":
                    ret = ("kvnew", a)
                    if emit:
                        f.events.append(("alias", ("kvnew", a), self.qual(f, args[0]), a))
                elif action == "merge":
                    if emit:
                        f.events.append(("alias", self.qual(f, args[0]), self.qual(f, args[1]), a))
                elif action == "copyto":
                    if emit:
                        f.events.append(("alias", self.qual(f, args[1]), self.qual(f, args[0]), a))
                elif action == "hfind":
                    sym = args[1]
                    if sym is not None and sym[0] in ("symkey", "symptr"):
                        ret = ("kvsub", sym[1], args[0])
                        if emit:
                            f.events.append(("kv", "get", "FindKey", ("a", sym[1]), self.qual(f, args[0]), a))
                    elif emit:
                        f.hfind += 1
                elif action == "ctor":
                    ret = args[0]               # a constructor returns this
                    if emit:
                        f.events.append(("kvctor", self.qual(f, args[0]), args[1], a))
                else:
                    if meth == "FindKey" and args[1] is not None and args[1][0] == "a":
                        ret = ("kvsub", args[1][1], args[0])
                if action in ("get", "set", "findkey") and emit:
                    if action == "findkey":
                        fl = args[2]
                        action = "set" if fl is not None and fl[0] == "c" and fl[1] & 0xFF else "get"
                    f.events.append(("kv", action, meth, self.qual(f, args[1]) or DYN, self.qual(f, args[0]), a))
        elif target is not None and target[0] in ("vmfn", "avfn"):
            slot = target[1] if target[0] == "vmfn" else (target[1], target[2])
            ret = ("vmret", slot, a)
            if emit:
                f.events.append(("vm" if target[0] == "vmfn" else "avm", slot, self.qual(f, args[2]) or DYN, self.qual(f, args[1]),
                                 self.qual(f, args[3]), self.qual(f, args[4]), a))
            # the out-variant (r9) of GetValue holds the value afterwards: nested tables can be followed
            r9 = args[3]
            self.clobber_slots(st, r9, 0x10)
            if r9 is not None and r9[0] == "stk":
                st[r9[1]] = ("vmval", slot, args[2], args[1], a)
            self.clobber_slots(st, args[4], 0x10)
        elif target is not None and target[0] == "ksym":
            # IKeyValuesSystem::GetSymbolForString(name, create): the key of a cached HKeySymbol
            if target[1] == 0x18:
                for k in (args[2], args[1]):       # (this, &result, name, create) or (this, name, create)
                    if k is not None and k[0] == "a" and self.key_text(k):
                        ret = ("symptr", k[1])
                        break
        elif target is not None and target[0] == "direct":
            if emit:
                f.calls.append((target[1], tuple(self.qual(f, v) for v in args), a))
                snap = {}
                for i, v in enumerate(args):
                    if v is not None and v[0] == "stk":
                        for d in range(8, 0x48, 8):
                            w = st.get(v[1] + d)
                            if w is not None:
                                snap[(i, d)] = self.qual(f, w)
                if snap:
                    f.snaps[a] = snap
            ret = ("ret", a)
        if tail and emit:
            f.rets.add(ret)
        # the callee may write through pointers to our stack
        for v in args[:4]:
            self.clobber_slots(st, v)
        for r in VOLATILE:
            st.pop(r, None)
        if ret is not None:
            st["rax"] = ret
        if tail:
            st.clear()

    def call_target(self, st, ins, op):
        if op.startswith("0x"):
            t = int(op, 16)
            return ("direct", t) if self.im.is_code(t) else None
        if op in SUB:
            v = self.rd(st, op)
            if v is None:
                return None
            if v[0] in ("vmfn", "avfn"):
                return v
            if v[0] == "ksymfn":
                return ("ksym", v[1])
            if v[0] == "imp":
                return v
            if v[0] == "a" and self.im.is_code(v[1]):
                return ("direct", v[1])
            return None
        m = self.parse_mem(op)
        if m is None:
            return None
        if m[1] == "rip":
            t = self.rip_target(ins, m)
            if t in self.imports:
                return ("imp", t)
            return None
        if m[2] is None and m[1] is not None:
            bv = st.get(SUB.get(m[1], (m[1],))[0])
            if bv == ("vmvt",):
                return ("vmfn", m[4])
            if bv is not None and bv[0] == "avt":
                return ("avfn", bv[1], m[4])
            if bv == ("kvsysvt",):
                return ("ksym", m[4])
        return None

    def step(self, f, st, ins, inside, emit):
        a, sz, mn, op = ins
        ops = op.split(", ") if op else []
        if mn == "call":
            self.do_call(f, st, ins, self.call_target(st, ins, op), emit)
            return
        if mn == "jmp":
            if op.startswith("0x"):
                t = int(op, 16)
                if not inside(t) and self.im.is_code(t):
                    self.do_call(f, st, ins, ("direct", t), emit, tail=True)
                return
            t = self.call_target(st, ins, op)
            if t is not None:
                self.do_call(f, st, ins, t, emit, tail=True)
            return
        if mn in ("ret", "retn") and emit:
            f.rets.add(self.qual(f, st.get("rax")))
        if mn.startswith("j") or mn in ("ret", "retn") or not ops:
            if mn in ("cdq", "cqo", "cdqe", "cwde", "cbw", "cwd"):
                st.pop("rax", None)
                st.pop("rdx", None)
            elif mn in ("leave",):
                v = st.get("rbp")
                st["_rsp"] = v[1] + 8 if v is not None and v[0] == "stk" else None
                st.pop("rbp", None)
            elif mn in ("cpuid", "rdtsc", "rdtscp", "xgetbv"):
                for r in ("rax", "rbx", "rcx", "rdx"):
                    st.pop(r, None)
            elif mn.startswith("rep") or mn.startswith("stos") or mn.startswith("movs") or mn.startswith("scas"):
                for r in ("rcx", "rsi", "rdi"):
                    st.pop(r, None)
            return
        if mn.startswith("rep") or mn.startswith("stos") or mn.startswith("movs") and len(ops) == 0:
            for r in ("rcx", "rsi", "rdi"):
                st.pop(r, None)
            return
        if mn == "push":
            r = st.get("_rsp")
            v = self.opval(st, ins, ops[0])
            if r is not None:
                r -= 8
                st["_rsp"] = r
                if v is None:
                    st.pop(r, None)
                else:
                    st[r] = v
            return
        if mn == "pop":
            r = st.get("_rsp")
            v = st.get(r) if r is not None else None
            self.wr(st, ops[0], v)
            if r is not None and ops[0] != "rsp":
                st["_rsp"] = r + 8
            return
        dst = ops[0]
        if dst in SUB:
            full = SUB[dst][0]
            if full == "rsp":
                if mn in ("sub", "add") and len(ops) == 2:
                    r = st.get("_rsp")
                    try:
                        imm = int(ops[1], 0)
                    except ValueError:
                        st["_rsp"] = None
                        return
                    st["_rsp"] = None if r is None else (r - imm if mn == "sub" else r + imm)
                    return
                if mn == "mov" or mn == "lea":
                    v = self.opval(st, ins, ops[1]) if mn == "mov" else self.lea(st, ins, ops[1])
                    st["_rsp"] = v[1] if v is not None and v[0] == "stk" else None
                    return
                st["_rsp"] = None
                return
            if mn in NOWRITE:
                return
            if mn == "add" and len(ops) == 2 and ops[1].startswith("0x") and int(ops[1], 16) in self.field_marks \
                    and SUB[dst][1] == 8:
                self.wr(st, dst, ("fieldaddr", int(ops[1], 16)))
            elif mn == "mov" or mn == "movabs":
                self.wr(st, dst, self.opval(st, ins, ops[1]))
            elif mn == "lea":
                self.wr(st, dst, self.lea(st, ins, ops[1]))
            elif mn in ("xor", "sub") and len(ops) == 2 and ops[1] == dst:
                self.wr(st, dst, ("c", 0))
            elif mn in ("movzx", "movsx", "movsxd"):
                v = self.opval(st, ins, ops[1])
                self.wr(st, dst, v if v is not None and v[0] == "c" else None)
            elif mn == "xchg" and len(ops) == 2 and ops[1] in SUB:
                v1, v2 = self.rd(st, dst), self.rd(st, ops[1])
                self.wr(st, dst, v2)
                self.wr(st, ops[1], v1)
            elif mn in ("or",) and len(ops) == 2 and ops[1].startswith(("0x", "-")) and int(ops[1], 0) in (-1,):
                self.wr(st, dst, None)
            else:
                self.wr(st, dst, None)
                if mn in ("mul", "div", "idiv") or (mn == "imul" and len(ops) == 1):
                    st.pop("rdx", None)
                    st.pop("rax", None)
            if mn in ("xchg",) and len(ops) == 2 and ops[1] not in SUB:
                pass
            return
        # memory destination
        m = self.parse_mem(dst)
        if m is None:
            return
        if mn in NOWRITE:
            return
        sl = self.slot_of(st, m)
        if mn == "mov" and len(ops) == 2 and m[1] == "rip":
            v = self.opval(st, ins, ops[1])
            if v is not None and v[0] == "symkey":
                self.sym_globals[self.rip_target(ins, m)] = v[1]     # a cached HKeySymbol
            return
        if mn == "mov" and len(ops) == 2:
            v = self.opval(st, ins, ops[1])
            if sl is not None:
                if v is None or (m[0] != 8 and v[0] not in SMALL):
                    st.pop(sl, None)
                else:
                    st[sl] = v
                if m[0] > 8:
                    self.clobber_slots(st, ("stk", sl), m[0])
            elif emit and v is not None and v[0] == "vmret" and m[2] is None and m[1] in SUB:
                bv = st.get(SUB[m[1]][0])
                if bv == ("arg", 0):
                    f.fstores.append((m[4], v[1], a))
            return
        if sl is not None:
            for k in range(sl, sl + max(m[0], 1)):
                st.pop(k, None)
        if mn == "xchg" and len(ops) == 2 and ops[1] in SUB:
            self.wr(st, ops[1], None)

    def lea(self, st, ins, s):
        m = self.parse_mem(s)
        if m is None:
            return None
        size, base, index, scale, disp = m
        if base == "rip":
            return ("a", self.rip_target(ins, m))
        if index is not None or base is None:
            return None
        if base == "rsp":
            r = st.get("_rsp")
            return None if r is None else ("stk", r + disp)
        bv = st.get(SUB.get(base, (base,))[0])
        if bv is not None and bv[0] == "stk":
            return ("stk", bv[1] + disp)
        if disp in self.field_marks:
            return ("fieldaddr", disp)
        return None

    # ------------------------------------------------------------------ resolution through callees
    def key_text(self, v):
        if v is not None and v[0] == "a":
            s = self.im.text(v[1], 200)
            if s and 0 < len(s) <= 128 and not any(c in s for c in "%\n"):
                return s
        return None

    @staticmethod
    def has_arg(v):
        if v is None:
            return False
        if v[0] in ("arg", "fld"):
            return True
        if v[0] == "vmval":
            return Analyzer.has_arg(v[2]) or Analyzer.has_arg(v[3])
        if v[0] == "kvsub":
            return Analyzer.has_arg(v[2])
        return False

    @staticmethod
    def subst(v, args, snap=None):
        """A value of the callee in terms of the caller: its arguments, fields of structs the caller
        built on its stack (snap), nested values."""
        if v is None:
            return None
        if v[0] == "arg":
            return args[v[1]] if v[1] < len(args) else None
        if v[0] == "fld":
            base = args[v[1]] if v[1] < len(args) else None
            if base is None:
                return None
            if base[0] == "arg":
                return ("fld", base[1], v[2])
            if base[0] == "lstk" and snap:
                return snap.get((v[1], v[2]))
            return None
        if v[0] == "vmval":
            return ("vmval", v[1], Analyzer.subst(v[2], args, snap), Analyzer.subst(v[3], args, snap), v[4])
        if v[0] == "kvsub":
            return ("kvsub", v[1], Analyzer.subst(v[2], args, snap))
        return v

    def effects(self, start, depth, shared_limit, huge_limit, memo):
        """Effects of a function and (to depth levels) of its callees, in terms of its own arguments:
        {(kind, x, key-or-dst, scope-or-obj-or-src, r9): call chain} with kind
            vm      (slot, key, scope, out-variant)        a call on g_pScriptVM
            avm     ((arg index, offset), key, scope, r9)   a virtual call on an argument (becomes vm when
                                                            the caller passes g_pScriptVM)
            kv      ("get|set:Method", key, object)         a KeyValues import
            alias   (dst, src)                              MergeFrom / CopySubkeys / MakeCopy
            kvctor  (name, object)                          KeyValues constructor
            return  (value)                                 what the function returns
        A call's result ('ret', site) is replaced by what the callee returns when that is one value."""
        key = (start, depth)
        if key in memo:
            return memo[key]
        memo[key] = {}          # recursion guard
        f = self.analyse(start)
        out = {}
        for e in f.events:
            if e[0] in ("vm", "avm"):
                _, slot, k, scope, r9, s5, a = e
                item = (e[0], slot, k, scope, r9)
            elif e[0] == "kv":
                _, action, meth, k, obj, a = e
                item = ("kv", action + ":" + meth, k, obj, None)
            elif e[0] == "alias":
                item = ("alias", None, e[1], e[2], None)
            elif e[0] == "kvctor":
                item = ("kvctor", None, e[2], e[1], None)
            elif e[0] == "cmp":
                item = ("cmp", None, e[1], None, None)
            else:
                continue
            out.setdefault(item, (start,))
        for target, args, a in f.calls:
            lits = [v for v in args[:2] if v is not None and v[0] == "a" and self.key_text(v)]
            if len(lits) == 1 and self.is_strcmp(target):
                out.setdefault(("cmp", None, lits[0], None, None), (start,))
        retmap = {}
        if depth > 0:
            indeg = self.in_degrees()
            for target, args, a in f.calls:
                if target == start:
                    continue
                restricted = indeg.get(target, 0) > shared_limit or self.sizes.get(target, 0) > huge_limit
                sub = self.effects(target, depth - 1, shared_limit, huge_limit, memo)
                snap = f.snaps.get(a)
                rets = set()
                for item, chain in sub.items():
                    kind, x = item[0], item[1]
                    if kind == "return":
                        rets.add(self.subst(item[2], args, snap))
                        continue
                    if kind == "avm":
                        i, off = x
                        base = args[i] if i < len(args) else None
                        if base == ("vm",):
                            kind, x = "vm", off
                        elif base is not None and base[0] == "arg":
                            x = (base[1], off)
                        else:
                            continue
                    elif restricted and not (self.has_arg(item[2]) or self.has_arg(item[3])):
                        continue
                    it = (kind, x, self.subst(item[2], args, snap), self.subst(item[3], args, snap),
                          self.subst(item[4], args, snap))
                    if it[0] in ("vm", "avm", "kv") and it[2] is None:
                        it = (it[0], it[1], DYN) + it[3:]
                    ch = (start,) + chain
                    if it not in out or len(out[it]) > len(ch):
                        out[it] = ch
                rets = {v for v in rets if v is not None and v[0] != "c"}
                if len(rets) == 1:
                    retmap[("ret", a)] = rets.pop()
        for v in f.rets:
            out.setdefault(("return", None, v, None, None), (start,))
        if retmap:
            def rw(v):
                if v is None:
                    return None
                if v[0] == "ret":
                    return retmap.get(v, v)
                if v[0] == "vmval":
                    return ("vmval", v[1], rw(v[2]), rw(v[3]), v[4])
                if v[0] == "kvsub":
                    return ("kvsub", v[1], rw(v[2]))
                return v
            new = {}
            for it, ch in out.items():
                it = (it[0], it[1], rw(it[2]), rw(it[3]), rw(it[4]))
                if it not in new or len(new[it]) > len(ch):
                    new[it] = ch
            out = new
        memo[key] = out
        return out


# ------------------------------------------------------------------ VM slot calibration
def calibrate(an, funcs):
    """Roles of IScriptVM slots from how the code uses them: get (its out-variant is passed to release
    afterwards), release, iterate (non-literal key position, two out-variants), set (the most used other
    slot with a literal key and a variant)."""
    pairs = collections.Counter()
    lit = collections.Counter()
    five = collections.Counter()
    for s in funcs:
        f = an.analyse(s)
        vms = [e for e in f.events if e[0] == "vm"]
        for i, e in enumerate(vms):
            _, slot, k, scope, r9, s5, a = e
            if an.key_text(k) and r9 is not None and r9[0] == "lstk":
                lit[slot] += 1
                for e2 in vms[i + 1:i + 6]:
                    if e2[3] == r9 and e2[1] != slot:
                        pairs[(slot, e2[1])] += 1
                        break
            elif (k is None or k[0] != "a") and r9 is not None and r9[0] == "lstk" and s5 is not None \
                    and s5[0] == "lstk":
                five[slot] += 1
    roles = {}
    if pairs:
        (g, r), _ = pairs.most_common(1)[0]
        roles[g] = "getvalue"
        roles[r] = "releasevalue"
    for slot, _ in five.most_common():
        if slot not in roles:
            roles[slot] = "iterate"
            break
    for slot, _ in lit.most_common():
        if slot not in roles:
            roles[slot] = "setvalue"
            break
    return roles, {"get_release_pairs": {"0x%x/0x%x" % k: v for k, v in pairs.most_common(5)},
                   "literal_key_slots": {"0x%x" % k: v for k, v in lit.most_common(8)},
                   "iterate_like_slots": {"0x%x" % k: v for k, v in five.most_common(4)}}


# ------------------------------------------------------------------ roots
def modifier_slots(im, vts):
    """{callback name: vtable slot} of CDOTA_Buff from CDOTA_Modifier_Lua's overrides (modifiers.py)."""
    from modifiers import Modifiers
    by_name = {n: vt for vt, (n, col) in vts.items()}
    base_vt = by_name.get(".?AVCDOTA_Buff@@")
    lua_vt = by_name.get(".?AVCDOTA_Modifier_Lua@@")
    if base_vt is None or lua_vt is None:
        return {}
    ns = types.SimpleNamespace(im=im, base_slots=im.vfuncs(base_vt))
    names = Modifiers.lua_slot_names(ns, lua_vt)
    out = {}
    for slot, n in sorted(names.items()):
        out.setdefault(n, slot)
    return out


def filter_fields(an, classes):
    """{Set*Filter method: (setter, field offset)}: the setter stores the copied function handle (the result
    of a VM call) into a field of the game mode (this + offset)."""
    out = {}
    for m in classes.get(FILTER_CLASS, {}).get("methods", []):
        if FILTER_METHOD.match(m["name"]) and m.get("impl") is not None:
            f = an.analyse(m["impl"])
            if f.fstores:
                out[m["name"]] = (m["impl"], f.fstores[0][0])
    return out


def refs_vm(an, p):
    im = an.im
    for b, e in an.chunks.get(p, ()):
        for m in VMREF.finditer(im.mem, b, e):
            if m.start() + 7 + struct.unpack_from("<i", im.mem, m.start() + 3)[0] == an.vm_global:
                return True
    return False


def filter_candidates(an, setter, off):
    """({function: [call targets the field is passed to]} of the functions that read the field the setter
    wrote (mov / lea / add r64 with the offset) and write or read literal keys, the same for the functions
    that pass it on without keys (wrappers, e.g. `add rcx, off; jmp runner`, called through the vtable))."""
    im = an.im
    pat = struct.pack("<i", off)
    found = set()
    for a, n in im.code_sections():
        i = im.mem.find(pat, a, a + n)
        while i >= 0:
            rex, opc, modrm = im.mem[i - 3], im.mem[i - 2], im.mem[i - 1]
            if rex in (0x48, 0x49, 0x4c, 0x4d) and ((opc in (0x8b, 0x8d) and 0x80 <= modrm <= 0xbf) or
                                                    (opc == 0x81 and 0xc0 <= modrm <= 0xc7)) or \
                    (im.mem[i - 2] in (0x48, 0x49) and im.mem[i - 1] == 0x05):
                p = an.function_of(i)
                if p is not None and p != setter:
                    found.add(p)
            i = im.mem.find(pat, i + 1, a + n)
    keyed, plain = {}, {}
    marks = {("field", off), ("fieldaddr", off)}
    for p in sorted(found):
        g = an.analyse(p)
        targets = [t for t, args, _ in g.calls if marks & set(args)]
        if any(e[0] == "vm" and marks & set(e[2:6]) for e in g.events):
            targets.append("vm")         # it calls the VM with the filter itself: a runner of its own
        if not targets:
            continue
        if any((e[0] == "vm" and an.key_text(e[2])) or (e[0] == "kv" and an.key_text(e[3])) for e in g.events):
            keyed[p] = targets
        else:
            plain[p] = targets
    return keyed, plain


def is_keyed(an, p):
    g = an.analyse(p)
    return any((e[0] == "vm" and an.key_text(e[2])) or (e[0] == "kv" and an.key_text(e[3])) for e in g.events)


def round_trip(an, p):
    """The function writes a literal key into KeyValues and reads the same key back (a filter event)."""
    g = an.analyse(p)
    sets = {an.key_text(e[3]) for e in g.events if e[0] == "kv" and e[1] == "set"}
    gets = {an.key_text(e[3]) for e in g.events if e[0] == "kv" and e[1] == "get"}
    for t, args, a in g.calls:            # wrappers of the KeyValues setters (key in rdx)
        if args[1] is not None and args[1][0] == "a":
            sub = an.analyse(t)
            if any(e[0] == "kv" and e[1] == "set" and e[3] == ("arg", 1) for e in sub.events):
                sets.add(an.key_text(args[1]))
    return bool((sets & gets) - {None})


def direct_callers(an, targets):
    """{target: functions with a call rel32 to it} for a few targets (one pass over the code)."""
    im = an.im
    targets = set(targets)
    out = collections.defaultdict(set)
    if not targets:
        return out
    for a, n in im.code_sections():
        i = im.mem.find(b"\xe8", a, a + n - 5)
        while i >= 0:
            t = (i + 5 + struct.unpack_from("<i", im.mem, i + 1)[0]) & 0xFFFFFFFF
            if t in targets:
                p = an.function_of(i)
                if p is not None:
                    out[t].add(p)
            i = im.mem.find(b"\xe8", i + 1, a + n - 5)
    return out


def vcall_sites(an, slot):
    """Functions with a `call qword ptr [r64 + slot*8]` (disp32 form)."""
    im = an.im
    pat = struct.pack("<i", slot * 8)
    out = set()
    for a, n in im.code_sections():
        i = im.mem.find(pat, a, a + n)
        while i >= 0:
            if im.mem[i - 2] == 0xff and 0x90 <= im.mem[i - 1] <= 0x97 and im.mem[i - 1] != 0x94:
                p = an.function_of(i)
                if p is not None:
                    out.add(p)
            i = im.mem.find(pat, i + 1, a + n)
    return out


def filter_invokers(an, ffields, vtables):
    """{Set*Filter: [invokers]}. The event of a filter is built as KeyValues, the runner (one function for
    all filters: it converts the KeyValues to a table, calls the Lua filter and reads the table back) gets
    the address of the filter field. Runners are the call targets that receive the field of at least half
    of the filters; the invokers are the functions that call a runner with the field, or call (through
    the vtable) a wrapper that does."""
    cands = {name: filter_candidates(an, setter, off) for name, (setter, off) in ffields.items()}
    users = collections.defaultdict(set)
    for name, (keyed, plain) in cands.items():
        for c in (keyed, plain):
            for p, targets in c.items():
                for t in targets:
                    users[t].add(name)
    need = max(3, (len(ffields) + 1) // 2)
    runners = {t for t, names in users.items() if len(names) >= need and t != "vm"}
    slots = collections.defaultdict(set)         # function -> vtable slots it is in
    for vt in vtables:
        for i, f in enumerate(an.im.vfuncs(vt)):
            slots[f].add(i)
    own = {p for keyed, plain in cands.values() for p, targets in plain.items()
           if not runners & set(targets) and "vm" in targets and an.sizes.get(p, 0) > 0x80}
    callers = direct_callers(an, own)
    out = {}
    for name, (keyed, plain) in cands.items():
        inv = {p for p, targets in keyed.items() if runners & set(targets)}
        for p, targets in plain.items():
            if runners & set(targets):
                # a wrapper reached through the vtable (e.g. `add rcx, off; jmp runner`)
                for slot in slots.get(p, ()):
                    inv |= {q for q in vcall_sites(an, slot) if round_trip(an, q)}
            elif p in own:
                # a runner of its own: its callers build the event
                inv |= {q for q in callers.get(p, ()) if round_trip(an, q)}
        out[name] = sorted(inv)
    return out, runners


def classify(an, roles, items, table_args, kv_args, local=False, root=None):
    """{key: set(kinds)} and sites of the effects of one root."""
    kvobj = set(kv_args)
    scopes = set(table_args)
    # whole-table copies: a loop over the table (iterate slot on a traced scope) writing non-literal keys
    # whole-table copies: the functions that loop over a traced table (iterate slot); the KeyValues they
    # create (constructor / new) or fill with non-literal keys hold the table
    iterating = set()
    for it, chain in items.items():
        if it[0] == "vm" and roles.get(it[1]) == "iterate":
            s = it[3]
            if s in scopes or (s is not None and s[0] in ("vmret", "vmval")):
                iterating.add(chain[-1])
    copied = bool(iterating)
    notes = []
    for it, chain in items.items():
        for v in (it[2], it[3]):
            if v is not None and v[0] == "kvnew" and an.function_of(v[1]) in iterating:
                kvobj.add(v)
        if it[0] == "kvctor" and chain[-1] in iterating and it[3] is not None:
            kvobj.add(it[3])
        if it[0] == "kv" and it[1].startswith("set:") and an.key_text(it[2]) is None and chain[-1] in iterating \
                and it[3] is not None:
            kvobj.add(it[3])
    for _ in range(3):
        for it in items:
            if it[0] == "alias" and it[3] in kvobj and it[2] is not None:
                kvobj.add(it[2])
    copies = sorted({an.key_text(it[2]) or "?" for it in items if it[0] == "kvctor" and it[3] in kvobj})
    if copied:
        notes.append("the whole table is copied into KeyValues %s (any key is passed through)" %
                     ", ".join('"%s"' % c for c in copies) if copies else
                     "the whole table is iterated (any key is passed through)")
    keys = collections.defaultdict(set)
    sites = collections.defaultdict(set)
    if local:
        # a filter invoker: only the event it builds (KeyValues it creates) and reads back
        for it, chain in items.items():
            for v in (it[2], it[3]):
                if v is not None and v[0] == "kvnew" and an.function_of(v[1]) == root:
                    kvobj.add(v)
            if it[0] == "kvctor" and chain == (root,) and it[3] is not None:
                kvobj.add(it[3])
        # literal keys the invoker passes to helpers (wrappers of the KeyValues getters / setters)
        passed = {v for _, args, _ in an.analyse(root).calls for v in args if v is not None and v[0] == "a"}
    for it, chain in items.items():
        if local and chain != (root,) and not (it[0] == "kv" and len(chain) == 2 and
                                                (it[3] in kvobj or it[2] in passed)):
            continue
        kind = None
        k = an.key_text(it[2])
        if k is None:
            continue
        if it[0] == "vm":
            role = roles.get(it[1])
            if role not in ("getvalue", "setvalue"):
                role = "vm_slot_0x%x" % it[1]
            s = it[3]
            traced = s in scopes or (s is not None and s[0] == "vmval" and (s[3] in scopes or s[3] is not None
                                                                            and s[3][0] == "vmret"))
            traced = traced or (s is not None and s[0] == "vmret")
            kind = role + ("" if traced else "_untraced")
            if s is not None and s[0] == "vmval":
                k = "%s.%s" % (an.key_text(s[2]) or "?", k)
        elif it[0] == "cmp":
            if chain[-1] not in iterating:
                continue
            kind = "iter_cmp"      # a key name compared while looping over the table
        elif it[0] == "kv":
            action = it[1].split(":")[0]
            obj, path = it[3], []
            while obj is not None and obj[0] == "kvsub":
                path.insert(0, an.im.text(obj[1], 200) or "?")
                obj = obj[2]
            if path:
                k = ".".join(path + [k])
            traced = obj in kvobj or (local and (chain == (root,) or it[2] in passed))
            kind = "kv_" + action + ("" if traced else "_untraced")
        else:
            continue
        keys[k].add(kind)
        sites[k].add("->".join("0x%x" % c for c in chain))
    return keys, sites, notes


def root_kind(label):
    """A root's label without its address and slot: 'Script_CreateIllusions', 'CDOTA_Modifier_Illusion::OnCreated',
    'generic modifier creation', 'filter invoker' (stable between builds)."""
    label = re.sub(r"@0x[0-9a-f]+$", "", label)
    return re.sub(r" \(.*\)$", "", label).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dll", default=os.environ.get("DOTA_SERVER_BINARY"), help="server.dll (Windows)")
    ap.add_argument("--lib", default=HERE, help="dumper/native-modifiers (pe.py, script_api.py)")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(HERE), "table_keys.json"))
    ap.add_argument("--version", default=None, help="ClientVersion of the build the DLL belongs to")
    ap.add_argument("--depth", type=int, default=3)
    ap.add_argument("--shared", type=int, default=150, help="callers above which a callee counts as shared")
    ap.add_argument("--huge", type=int, default=0x6000, help="bytes above which a callee counts as huge")
    ap.add_argument("--debug", action="store_true",
                    help="also write roots with addresses, notes, call chains and untraced findings, and "
                         "<out>.meta.json (VM slots, calibration, timing); not for the committed file")
    ap.add_argument("--keep-untraced", action="store_true",
                    help="also keep functions whose reads are all untraced (mostly unit / ability definition reads)")
    ap.add_argument("--classes-cache", default=None, help="pickle of script_classes() (development)")
    args = ap.parse_args()
    if not args.dll:
        ap.error("--dll (or DOTA_SERVER_BINARY) is required")
    sys.path.insert(0, args.lib)
    from pe import Image
    t0 = time.time()
    im = Image(args.dll)
    if args.classes_cache and os.path.exists(args.classes_cache):
        import pickle
        with open(args.classes_cache, "rb") as fh:
            classes = pickle.load(fh)
    else:
        from script_api import script_classes
        classes = script_classes(im, args.dll)
    t_classes = time.time() - t0
    an = Analyzer(im)
    an.in_degrees()
    an.prescan_symbols()
    ffields = filter_fields(an, classes)
    an.cache.clear()                    # analyse again with the filter fields marked
    an.field_marks = {off for _, off in ffields.values()}
    print("script bindings: %d classes, %d functions (%.1f s); g_pScriptVM at 0x%x; %d functions" % (
        len(classes), sum(len(c["methods"]) for c in classes.values()), t_classes, an.vm_global,
        len(an.starts)), file=sys.stderr)

    roots = {}
    for cname, c in classes.items():
        for m in c["methods"]:
            if m.get("impl") is None:
                continue
            impl = m["impl"]
            if m.get("slot") is not None:
                continue            # a vcall thunk: the implementation is virtual
            roots.setdefault("%s.%s" % (cname, m["name"]), []).append(
                {"start": impl, "label": "%s@0x%x" % (m["cpp"] or m["name"], impl), "kv_args": ()})
    roles, calib = calibrate(an, sorted({r[0]["start"] for r in roots.values()}))
    print("VM slots: %s" % ", ".join("0x%x=%s" % (k, v) for k, v in sorted(roles.items())), file=sys.stderr)
    if "getvalue" not in roles.values():
        print("table_keys: IScriptVM::GetValue not found (calibration failed), no output", file=sys.stderr)
        return 3

    vts = im.vtables()
    by_name = {n: vt for vt, (n, col) in vts.items()}
    mslots = modifier_slots(im, vts)
    extra_notes = collections.defaultdict(list)
    core, core_arg = modifier_core(an, roots)
    for fn, specs in EXTRA_ROOTS.items():
        for sp in specs:
            if sp.get("modifier_core"):
                if core is None:
                    extra_notes[fn].append("generic modifier creation not found")
                    continue
                roots.setdefault(fn, []).append({"start": core, "label": "generic modifier creation "
                                                 "(the callee of Script_AddNewModifier, KeyValues = argument %d)@0x%x"
                                                 % (core_arg, core), "kv_args": (("arg", core_arg),)})
                continue
            vt = by_name.get(".?AV%s@@" % sp["rtti"])
            slot = mslots.get(sp["callback"])
            if vt is None or slot is None:
                extra_notes[fn].append("extra root %s::%s not found" % (sp["rtti"], sp["callback"]))
                continue
            f = im.va(im.q(vt + 8 * slot))
            roots.setdefault(fn, []).append({"start": f, "label": "%s::%s (slot %d)@0x%x" % (
                sp["rtti"], sp["callback"], slot, f), "kv_args": (("arg", sp["kv_arg"]),)})
    gm_vts = [vt for vt, (n, col) in vts.items() if ".?AV%s@@" % FILTER_CLASS in (im.bases(col) or ())]
    invokers, runners = filter_invokers(an, ffields, gm_vts)
    for name, (setter, off) in sorted(ffields.items()):
        fn = "%s.%s" % (FILTER_CLASS, name)
        inv = invokers.get(name, [])
        extra_notes[fn].append("filter function stored at +0x%x; invokers (call a filter runner %s with it): %s" % (
            off, "/".join("0x%x" % r for r in sorted(runners)), ", ".join("0x%x" % p for p in inv) or "none found"))
        for p in inv:
            roots.setdefault(fn, []).append({"start": p, "label": "filter invoker@0x%x" % p, "kv_args": (),
                                             "local": True})

    out = {}
    memo = {}
    for fn in sorted(roots):
        allkeys = collections.defaultdict(set)
        allsites = collections.defaultdict(set)
        sources = collections.defaultdict(set)      # key -> root kinds that read / write it (traced)
        notes = list(extra_notes.get(fn, []))
        labels = []
        for r in roots[fn]:
            items = an.effects(r["start"], args.depth, args.shared, args.huge, memo)
            labels.append(r["label"])
            table_args = [("arg", i) for i in range(NARGS)]
            keys, sites, nts = classify(an, roles, items, table_args, r["kv_args"], r.get("local"), r["start"])
            for k, v in keys.items():
                allkeys[k] |= v
                allsites[k] |= sites[k]
                if any(not x.endswith("_untraced") for x in v):
                    sources[k].add(root_kind(r["label"]))
            notes += ["%s: %s" % (r["label"], n) for n in nts]
            f = an.analyse(r["start"])
            if f.hfind:
                notes.append("%s: %d FindKey(HKeySymbol) calls (keys not visible)" % (r["label"], f.hfind))
            if f.error:
                notes.append("%s: analysis error %s" % (r["label"], f.error))
        traced = [k for k, v in allkeys.items() if any(x in READ_TRACED for x in v)]
        untraced = [k for k, v in allkeys.items() if any(x.startswith(("getvalue", "kv_get")) for x in v)]
        if not traced and not (args.keep_untraced and untraced):
            continue
        if args.debug:
            entry = {"keys": {k: sorted(allkeys[k]) for k in sorted(allkeys, key=str.lower)}, "roots": labels,
                     "notes": notes, "sites": {k: sorted(allsites[k]) for k in sorted(allsites, key=str.lower)}}
        else:
            # traced findings only: untraced ones depend on inlining and come and go between builds
            keys = {k: sorted(x for x in v if not x.endswith("_untraced")) for k, v in allkeys.items()}
            keys = {k: v for k, v in keys.items() if v}
            entry = {"keys": {k: {"access": keys[k], "sources": sorted(sources[k])}
                              for k in sorted(keys, key=str.lower)}}
        out[fn] = entry

    missing = []
    for fn, want in ANCHORS.items():
        have = {k.lower() for k in (out.get(fn) or {}).get("keys", {})}
        missing += ["%s.%s" % (fn, k) for k in want if k.lower() not in have]
    if missing:
        print("table_keys: keys every working analysis finds are missing (%s): no output" % ", ".join(missing),
              file=sys.stderr)
        return 3

    result = {"version": args.version, "functions": out}
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, indent=1, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    if args.debug:
        meta = {"dll": args.dll, "vm_global": "0x%x" % an.vm_global,
                "vm_slots": {"0x%x" % k: v for k, v in sorted(roles.items())}, "calibration": calib,
                "depth": args.depth, "shared_callers": args.shared, "huge_bytes": args.huge,
                "functions_analysed": len(an.cache), "seconds": round(time.time() - t0, 1),
                "seconds_script_classes": round(t_classes, 1)}
        with open(os.path.splitext(args.out)[0] + ".meta.json", "w", encoding="utf-8", newline="\n") as fh:
            json.dump(meta, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    print("%d functions with keys, %d functions analysed, %.1f s" % (len(out), len(an.cache), time.time() - t0),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
