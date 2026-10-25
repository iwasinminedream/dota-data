"""The VScript (Lua) classes of server.dll with the native implementation of every method, read offline.

Every script function is a ScriptFunctionBinding_t (0x50 bytes) that registration code fills in place: the
word 0xff1d at +0x18 (return type "unknown", optional-argument count -1) marks where a description is
created. The functions around such places (by .pdata, following chained tails) are the registration roots;
roots that turn out to be shared helpers (AddToTail of the description vector) are replaced by their call
sites. Every root runs in the x86-64 emulator (x64emu.py): image memory, allocations through g_pMemAlloc /
UtlVectorMemory_* are real (inside the emulator), g_pScriptVM is a fake object whose virtual calls are
recorded. The class descriptions (ScriptClassDesc_t) then sit in the emulator heap:
    +0 Lua name, +8 C++ name, +0x10 description, +0x18 base class, +0x20 function count, +0x28 functions
A function description: +0 Lua name, +8 C++ name, +0x10 description, +0x18 return type, +0x1a parameter
count, +0x1b parameter types, +0x28 parameter names, +0x30 class, +0x38 binding stub, +0x40 implementation,
+0x48 flags (1 = method).

Ported from dota-metamod/tools/dump_script_api.py (server.dll part only).
"""
import collections
import re
import struct

from x64emu import Emu, Stop

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def setup(emu):
    def calc(e):
        return (e.regs["r8"] & 0xFFFFFFFF) + 32

    def vec_alloc(e):
        new, old, p = e.regs["r8"], e.regs["r9"], e.regs["rcx"]
        a = e.alloc(new or 16, "utlvec")
        if p and old:
            e.wb(a, e.rb(p, min(old, new)))
        return a

    def init_once(e):
        if e.regs["r8"]:
            e.w(e.regs["r8"], 4, 1)
        return 1

    def malloc(e):
        return e.alloc(e.regs["rcx"] or 16, "malloc")

    def realloc_(e):
        a = e.alloc(e.regs["rdx"] or 16, "realloc")
        if e.regs["rcx"]:
            e.wb(a, e.rb(e.regs["rcx"], e.regs["rdx"]))
        return a

    emu.import_handlers.update({
        "UtlVectorMemory_CalcNewAllocationCount": calc,
        "UtlVectorMemory_Alloc": vec_alloc,
        "InitOnceBeginInitialize": init_once,
        "InitOnceComplete": lambda e: 1,
        "MemAlloc_AllocFunc": malloc,
        "MemAlloc_ReallocFunc": realloc_,
    })

    def mem_alloc(e, name, slot):
        if slot == 1:
            return e.alloc(e.regs["rdx"] or 16, "alloc")
        if slot == 2:
            a = e.alloc(e.regs["r8"] or 16, "realloc")
            if e.regs["rdx"]:
                e.wb(a, e.rb(e.regs["rdx"], e.regs["r8"]))
            return a
        return 0

    emu.vcall_handlers["imp:g_pMemAlloc"] = mem_alloc


def code_blobs(emu):
    for sa, se in emu.code:
        yield sa, bytes(emu.img[sa - emu.base:se - emu.base])


def find_vm_global(emu):
    """g_pScriptVM: the global loaded into rcx next to the "Started VScript virtual machine" message."""
    pos = emu.img.find(b"VSCRIPT: Started VScript virtual machine")
    if pos < 0:
        return None
    target = emu.base + pos
    for sa, blob in code_blobs(emu):
        for m in re.finditer(rb"[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]", blob):
            p = sa + m.start()
            if p + 7 + struct.unpack_from("<i", blob, m.start() + 3)[0] != target:
                continue
            window = blob[m.start() - 0x30:m.start()]
            found = None
            for k in range(len(window) - 7):
                if window[k:k + 3] == b"\x48\x8b\x0d":      # mov rcx, [rip+G]
                    at = p - 0x30 + k
                    found = at + 7 + struct.unpack_from("<i", window, k + 3)[0]
            if found:
                return found
    return None


def binding_sites(emu):
    """Addresses (VA) of `mov word ptr [...], 0xff1d` instructions."""
    out = []
    for sa, blob in code_blobs(emu):
        for m in re.finditer(rb"\x66[\x40-\x4f]?\xc7", blob):
            p = sa + m.start()
            try:
                ins = emu.decode(p)
            except Stop:
                continue
            if ins.mnemonic == "mov" and ins.op_str.endswith(", 0xff1d") and ins.operands[0].size == 2:
                out.append(p)
    return out


def function_start(emu, va):
    rva = va - emu.base
    f = emu.primary_function(rva)
    if f is not None:
        return emu.base + f
    p = rva     # leaf function without .pdata: back to the int3 padding
    while p > 0 and not (emu.img[p - 1] == 0xCC and emu.img[p - 2] == 0xCC):
        p -= 1
    return emu.base + p


def callers(emu, target):
    out = []
    for sa, blob in code_blobs(emu):
        i = blob.find(b"\xe8")
        while i >= 0:
            if i + 5 <= len(blob) and sa + i + 5 + struct.unpack_from("<i", blob, i + 1)[0] == target:
                out.append(sa + i)
            i = blob.find(b"\xe8", i + 1)
    return out


def find_roots(emu):
    sites = binding_sites(emu)
    roots = collections.Counter(function_start(emu, s) for s in sites)
    final = collections.Counter()
    ends = {b: e for b, e, u in emu.funcs}
    for r, n in roots.items():
        end = ends.get(r - emu.base)
        size = (end - (r - emu.base)) if end else 0
        body = bytes(emu.img[r - emu.base:r - emu.base + size])
        # helper of the description vector (AddToTail): small, element size 0x50 (mov r9d, 0x50), many callers
        if 0 < size < 0x400 and bytes.fromhex("41b950000000") in body:
            cs = callers(emu, r)
            if len(cs) >= 8:
                for c in cs:
                    final[function_start(emu, c)] += 1
                continue
        final[r] += n
    return final


def register_call_sites(emu, vm_global):
    """`mov rcx, [rip+g_pScriptVM]` ... `call [rax+0xc0]` (RegisterFunction) of static descriptions."""
    out = []
    if not vm_global:
        return out
    pat = re.compile(rb"\x48\x8b\x0d(....)", re.S)
    reg = re.compile(rb"(\xff\x90|[\x48\x4c]\x8b[\x80\x88\x90\x98\xa0\xa8\xb0\xb8])\xc0\x00\x00\x00")
    for sa, blob in code_blobs(emu):
        for m in pat.finditer(blob):
            p = sa + m.start()
            if p + 7 + struct.unpack("<i", m.group(1))[0] != vm_global:
                continue
            if reg.search(blob[m.end():m.end() + 0x18]):
                out.append(p)
    return out


def read_binding(emu, p):
    b = emu.rb(p, 0x50)
    q = lambda o: struct.unpack_from("<Q", b, o)[0]
    impl = q(0x40)
    return {
        "name": emu.cstr(q(0), 128),
        "cpp": emu.cstr(q(8), 256),
        "params": max(0, struct.unpack_from("<b", b, 0x1a)[0]),
        "ret": b[0x18],
        "impl": (impl - emu.base) if emu.in_image(impl) else None,
    }


def desc_at(emu, d):
    try:
        name = emu.cstr(emu.q(d), 128)
    except Exception:
        return None
    if not name or not IDENT.match(name):
        return None
    cnt = emu.r(d + 0x20, 4)
    arr = emu.q(d + 0x28)
    if not (0 < cnt < 10000) or not arr or arr & 7:
        return None
    if emu.q(arr + 0x30) != d:
        return None
    return cnt


def scan_descs(emu):
    found = {}
    for a, size, tag in emu.blocks:
        if size >= 0x50 and desc_at(emu, a):
            found[a] = tag
    for page in sorted(emu.dirty):
        base = emu.base + (page << 12)
        for off in range(0, 0x1000, 8):
            d = base + off
            if emu.img[d - emu.base + 0x20:d - emu.base + 0x24] == b"\0\0\0\0":
                continue
            if desc_at(emu, d):
                found[d] = "static"
    queue = list(found)
    while queue:       # base classes without functions of their own
        d = queue.pop()
        b = emu.q(d + 0x18)
        if b and b not in found:
            nm = emu.cstr(emu.q(b), 128)
            if nm and IDENT.match(nm):
                found[b] = "base"
                queue.append(b)
    return found


def vcall_slot(img, rva):
    """MSVC vcall thunk `mov rax,[rcx]; jmp [rax+N]` -> N/8 (the slot), else None."""
    code = bytes(img[rva:rva + 12])
    if code[:3] == b"\x48\x8b\x01":
        if code[3:5] == b"\xff\x60":
            return code[5] // 8
        if code[3:5] == b"\xff\xa0":
            return struct.unpack_from("<i", code, 5)[0] // 8
    if code[:2] == b"\xff\x21":        # jmp [rcx]
        return 0
    return None


def looks_binding(emu, p):
    if not p or p & 7:
        return False
    try:
        name = emu.cstr(emu.q(p), 128)
    except Exception:
        return False
    if not name or not IDENT.match(name):
        return False
    stub = emu.q(p + 0x38)
    return emu.in_image(stub) and emu.is_code(stub)


def script_classes(image, path):
    """{Lua class name: {"cpp", "base", "methods": [{"name", "cpp", "params", "impl", "slot"}]}}; the global
    functions registered on the game's VM are the methods of the pseudo-class "_G"."""
    from x64emu import FAKE_FN, SENTINEL
    emu = Emu(path, image=image)
    setup(emu)
    vm_global = find_vm_global(emu)
    vm = emu.fake_object("g_pScriptVM")
    if vm_global:
        emu.w(vm_global, 8, vm)
    globals_ = []

    def on_external(e, target):
        # IScriptVM::RegisterFunction(ScriptFunctionBinding_t *) is slot 24 of the VM
        if FAKE_FN <= target < SENTINEL:
            oid, slot = (target - FAKE_FN) >> 12, ((target - FAKE_FN) & 0xFFF) >> 3
            if oid < len(e.fakes) and e.fakes[oid] == "g_pScriptVM" and slot == 24 and looks_binding(e, e.regs["rdx"]):
                globals_.append(read_binding(e, e.regs["rdx"]))
        return None

    emu.on_external = on_external
    roots = find_roots(emu)
    for s in register_call_sites(emu, vm_global):
        roots[function_start(emu, s)] += 1
    for r in sorted(roots):
        try:
            emu.call(r, rcx=emu.fake_object("arg0"), rdx=emu.fake_object("arg1"),
                     r8=emu.fake_object("arg2"), r9=emu.fake_object("arg3"), budget=5_000_000)
        except Stop:
            pass
    classes = {}
    for d, tag in scan_descs(emu).items():
        name = emu.cstr(emu.q(d), 128)
        base = emu.q(d + 0x18)
        cnt = emu.r(d + 0x20, 4) if tag != "base" else 0
        arr = emu.q(d + 0x28)
        methods = []
        for i in range(cnt):
            m = read_binding(emu, arr + i * 0x50)
            if m["impl"] is not None:
                m["slot"] = vcall_slot(emu.img, m["impl"])
            methods.append(m)
        entry = {"cpp": emu.cstr(emu.q(d + 8), 256), "base": emu.cstr(emu.q(base), 128) if base else None,
                 "methods": methods}
        if name in classes and len(classes[name]["methods"]) >= len(methods):
            continue
        classes[name] = entry
    seen = set()
    gl = []
    for m in globals_:
        if m["name"] not in seen and m["impl"] is not None:
            seen.add(m["name"])
            m["slot"] = None
            gl.append(m)
    classes["_G"] = {"cpp": None, "base": None, "methods": sorted(gl, key=lambda m: m["name"])}
    return classes
