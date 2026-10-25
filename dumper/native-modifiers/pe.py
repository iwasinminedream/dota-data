"""A Windows x64 PE image (server.dll) laid out as in memory: addresses are RVAs, the image base is 0.

No dependency besides the standard library: sections, imports (IAT cells), .pdata function ranges,
MSVC RTTI (complete object locators, class hierarchy) and a few search helpers.
"""
import bisect
import re
import struct

# lea r64, [rip + disp32]
LEA_RIP = re.compile(rb"[\x48\x4c]\x8d[\x05\x0d\x15\x1d\x25\x2d\x35\x3d]")
# complete object locator of a primary vtable: signature 1, offset 0
COL_HEAD = re.compile(rb"\x01\x00\x00\x00\x00\x00\x00\x00")


class Image:
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as f:
            raw = f.read()
        if raw[:2] != b"MZ":
            raise ValueError("%s is not a PE file" % path)
        pe = struct.unpack_from("<I", raw, 0x3C)[0]
        if raw[pe:pe + 4] != b"PE\0\0":
            raise ValueError("%s: no PE header" % path)
        machine, nsec = struct.unpack_from("<HH", raw, pe + 4)
        if machine != 0x8664:
            raise ValueError("%s is not an x64 image" % path)
        opt_size = struct.unpack_from("<H", raw, pe + 20)[0]
        opt = pe + 24
        if struct.unpack_from("<H", raw, opt)[0] != 0x20B:
            raise ValueError("%s: not PE32+" % path)
        self.base = struct.unpack_from("<Q", raw, opt + 24)[0]
        size_of_image = struct.unpack_from("<I", raw, opt + 56)[0]
        size_of_headers = struct.unpack_from("<I", raw, opt + 60)[0]
        ndirs = struct.unpack_from("<I", raw, opt + 108)[0]
        dirs = [struct.unpack_from("<II", raw, opt + 112 + 8 * i) for i in range(ndirs)]

        img = bytearray(size_of_image)
        img[:size_of_headers] = raw[:size_of_headers]
        self.sections = []   # (rva, size, name, executable)
        sec = opt + opt_size
        for i in range(nsec):
            s = sec + 40 * i
            name = raw[s:s + 8].rstrip(b"\0").decode(errors="replace")
            vsize, va, rsize, rptr = struct.unpack_from("<IIII", raw, s + 8)
            chars = struct.unpack_from("<I", raw, s + 36)[0]
            n = min(rsize, vsize) if vsize else rsize
            img[va:va + n] = raw[rptr:rptr + n]
            self.sections.append((va, vsize or rsize, name, bool(chars & 0x20000000)))
        self.mem = bytes(img)
        self.size = size_of_image

        # imports: RVA of every IAT cell -> imported name
        self.imports = {}
        if len(dirs) > 1 and dirs[1][0]:
            d = dirs[1][0]
            while True:
                ilt, _, _, name_rva, iat = struct.unpack_from("<IIIII", self.mem, d)
                if not name_rva:
                    break
                dll = (self.cstr(name_rva) or "?").lower()
                lookup = ilt or iat
                k = 0
                while True:
                    e = struct.unpack_from("<Q", self.mem, lookup + 8 * k)[0]
                    if not e:
                        break
                    if e >> 63:
                        nm = "%s#%d" % (dll, e & 0xFFFF)
                    else:
                        nm = self.cstr((e & 0x7FFFFFFF) + 2) or "?"
                    self.imports[iat + 8 * k] = nm
                    k += 1
                d += 20

        # .pdata: (begin, end, unwind info) of every function with unwind data
        self.funcs = []
        if len(dirs) > 3 and dirs[3][0]:
            a, n = dirs[3]
            for off in range(a, a + n - 11, 12):
                b, e, u = struct.unpack_from("<III", self.mem, off)
                if b:
                    self.funcs.append((b, e, u))
            self.funcs.sort()
        self._fstarts = [f[0] for f in self.funcs]

    # --- reading
    def q(self, rva):
        return struct.unpack_from("<Q", self.mem, rva)[0]

    def d(self, rva):
        return struct.unpack_from("<I", self.mem, rva)[0]

    def i32(self, rva):
        return struct.unpack_from("<i", self.mem, rva)[0]

    def f32(self, rva):
        return struct.unpack_from("<f", self.mem, rva)[0]

    def cstr(self, rva, limit=512):
        if not 0 <= rva < len(self.mem):
            return None
        end = self.mem.find(b"\0", rva, rva + limit)
        if end < 0:
            return None
        try:
            return self.mem[rva:end].decode("utf-8")
        except UnicodeDecodeError:
            return None

    def text(self, rva, limit=256):
        """A printable ASCII string at rva (identifiers, paths, sound names), else None."""
        s = self.cstr(rva, limit)
        if s is None or not all(32 <= ord(c) < 127 for c in s):
            return None
        return s

    def va(self, ptr):
        """RVA of an absolute pointer into the image, else None."""
        r = ptr - self.base
        return r if 0 <= r < self.size else None

    # --- layout
    def section_of(self, rva):
        for a, n, name, ex in self.sections:
            if a <= rva < a + n:
                return name, ex
        return None, False

    def is_code(self, rva):
        return self.section_of(rva)[1]

    def is_readonly(self, rva):
        return self.section_of(rva)[0] == ".rdata"

    def code_sections(self):
        return [(a, n) for a, n, name, ex in self.sections if ex]

    def data_sections(self):
        return [(a, n) for a, n, name, ex in self.sections if not ex]

    def func_of(self, rva):
        """(begin, end) of the .pdata function containing rva, else None."""
        i = bisect.bisect_right(self._fstarts, rva) - 1
        if i >= 0 and self.funcs[i][0] <= rva < self.funcs[i][1]:
            return self.funcs[i][0], self.funcs[i][1]
        return None

    def primary_function(self, rva):
        """Start of the function owning rva, following chained unwind info of split-off tails."""
        i = bisect.bisect_right(self._fstarts, rva) - 1
        if i < 0 or not (self.funcs[i][0] <= rva < self.funcs[i][1]):
            return None
        begin, _, unwind = self.funcs[i]
        for _ in range(64):
            if not (self.mem[unwind] >> 3) & 4:
                return begin
            count = self.mem[unwind + 2]
            off = unwind + 4 + 2 * ((count + 1) & ~1)
            begin, _, unwind = struct.unpack_from("<III", self.mem, off)
        return begin

    def strings(self, text):
        """RVAs of NUL-terminated occurrences of text."""
        needle = b"\0" + text.encode() + b"\0"
        out = []
        i = self.mem.find(needle)
        while i >= 0:
            out.append(i + 1)
            i = self.mem.find(needle, i + 1)
        return out

    def code_refs(self, target):
        """Addresses of lea r64, [rip+disp32] instructions pointing at target."""
        out = []
        for a, n in self.code_sections():
            blob = self.mem[a:a + n]
            for m in LEA_RIP.finditer(blob):
                p = a + m.start()
                if p + 7 + struct.unpack_from("<i", self.mem, p + 3)[0] == target:
                    out.append(p)
        return out

    # --- MSVC RTTI (x64: 32-bit RVAs inside the locator and the hierarchy)
    def complete_object_locators(self):
        """RVAs of the complete object locators of primary vtables (pSelf = own RVA)."""
        out = []
        for a, n in self.data_sections():
            blob = self.mem[a:a + n]
            for m in COL_HEAD.finditer(blob):
                c = a + m.start()
                if c % 4 == 0 and c + 24 <= len(self.mem) and self.d(c + 20) == c:
                    out.append(c)
        return out

    def vtables(self):
        """{vtable RVA: (decorated class name, locator)} for every primary vtable in the image."""
        cols = {c + self.base for c in self.complete_object_locators()}
        out = {}
        for a, n in self.data_sections():
            start = (a + 7) & ~7
            count = (a + n - start) // 8
            cells = memoryview(self.mem)[start:start + 8 * count].cast("Q")
            for i, v in enumerate(cells):
                if v in cols:
                    col = v - self.base
                    out[start + 8 * i + 8] = (self.cstr(self.d(col + 12) + 16), col)
        return out

    def bases(self, col):
        """Decorated names of the class and all of its bases, from the class hierarchy descriptor."""
        chd = self.d(col + 16)
        count, arr = self.d(chd + 8), self.d(chd + 12)
        return [self.cstr(self.d(self.d(arr + 4 * i)) + 16) for i in range(count)]

    def vfuncs(self, vt, limit=4096):
        """Functions of a vtable, while the pointers lead into code."""
        out = []
        for i in range(limit):
            r = self.va(self.q(vt + 8 * i))
            if r is None or not self.is_code(r):
                break
            out.append(r)
        return out
