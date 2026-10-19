#!/usr/bin/env python3
"""
Function-level comparison of two builds of a stripped x86-64 .so (Dota's Linux libraries): which
functions changed, appeared or disappeared, what each one is and what changed in its code.

    funcdiff.py OLD.so NEW.so [--out FILE]

Functions: a linear sweep of .text (capstone) cut at the int3 padding between functions and at
known entry points (.eh_frame FDEs, function pointers in data). Each instruction is normalised so
that a function compiles to the same text in both builds unless its code changed: a reference to a
string becomes the string, a value loaded from read-only data becomes the value (float constants of
game logic: a changed number is a changed function), other code/data addresses become T/D,
branches inside the function L, calls and jumps out of it F.

Names come from RTTI: a function that is slot N of the vtable of class C is "C::vfunc#N"; when the
slot is one a Lua class (CDOTA_Ability_Lua, CDOTA_Item_Lua, CDOTA_Modifier_Lua) forwards to a Lua
callback of the same name (it references the string "OnSpellStart"...), every class deriving from
the Lua class's base gets that name: "CDOTA_Ability_Tinker_Rearm::OnSpellStart". The callback names
are read from the dump (files/vscripts/api.json).

Pairing: identical code that is unique in both builds anchors the order; in the gaps between
anchors functions pair by identical code, then by order, strings, names and size; leftovers pair
across the whole library by names and strings. A pair of identical code whose called functions are
not each other's pairs is a change too ("calls a different function").

The function table of a library is cached in <snapshot>/funcs/<lib>.json.gz next to the snapshot.
"""
import argparse
import bisect
import collections
import difflib
import gzip
import hashlib
import json
import os
import re
import struct
import subprocess
import sys

import capstone

HERE = os.path.dirname(os.path.abspath(__file__))
API_JSON = os.path.join(os.path.dirname(HERE), 'files', 'vscripts', 'api.json')
CACHE_VERSION = 9
RIP = re.compile(r'(?:(byte|word|dword|qword|xmmword) ptr )?\[rip ([+-]) (0x[0-9a-f]+|\d+)\]')
BRANCH = re.compile(r'^(?:(?:bnd|notrack) )?(call|jmp|j[a-z]+|loop[a-z]*)$')
TYPEINFO_NAME = re.compile(r'^(?:N(?:K|V)*)?\d+[A-Za-z_]\w*$')
SIZES = {'byte': 1, 'word': 2, 'dword': 4, 'qword': 8, 'xmmword': 16}
MAX_REFS = 400


class Image:
    """An ELF64 shared object: sections, PT_LOAD mapping, RELATIVE relocations."""

    def __init__(self, path):
        self.path = path
        self.data = data = open(path, 'rb').read()
        shoff, = struct.unpack_from('<Q', data, 0x28)
        shentsize, shnum, shstrndx = struct.unpack_from('<HHH', data, 0x3a)
        heads = [struct.unpack_from('<IIQQQQ', data, shoff + i * shentsize) for i in range(shnum)]
        names = heads[shstrndx]
        strtab = data[names[4]:names[4] + names[5]]
        self.sections = {}
        for name, typ, _flags, addr, off, size in heads:
            self.sections[strtab[name:strtab.index(b'\0', name)].decode()] = (typ, addr, off, size)
        phoff, = struct.unpack_from('<Q', data, 0x20)
        phentsize, phnum = struct.unpack_from('<HH', data, 0x36)
        self.loads = []
        for i in range(phnum):
            typ, flags, off, vaddr, _paddr, filesz = struct.unpack_from('<IIQQQQ', data, phoff + i * phentsize)
            if typ == 1:
                self.loads.append((vaddr, off, filesz, flags))
        _t, self.text_addr, self.text_off, self.text_size = self.sections['.text']
        self._relocs = None
        self.symbolic = set()  # slots with a symbol relocation (e.g. __cxa_pure_virtual in a vtable)

    def segment(self, va):
        for vaddr, off, size, flags in self.loads:
            if vaddr <= va < vaddr + size:
                return va - vaddr + off, flags
        return None, 0

    def offset(self, va):
        return self.segment(va)[0]

    def in_text(self, va):
        return self.text_addr <= va < self.text_addr + self.text_size

    def cstring(self, va):
        """The C string starting at va (printable, 3+ characters, in read-only data), else None:
        bytes in writable data that look like text are pointers or variables, not strings."""
        off, flags = self.segment(va)
        if off is None or flags & 3 or (off and self.data[off - 1] != 0):
            return None
        end = self.data.find(b'\0', off, off + 400)
        chunk = self.data[off:end] if end > off else b''
        if len(chunk) >= 3 and all(32 <= c < 127 or c == 9 for c in chunk):
            return chunk.decode()
        return None

    def constant(self, va, size, mnemonic):
        """The value at va when it lies in read-only data (not code, not writable), else None."""
        off, flags = self.segment(va)
        if off is None or flags & 3 or off + size > len(self.data):
            return None
        raw = self.data[off:off + size]
        if mnemonic.endswith(('ss', 'ps')) and size in (4, 16):
            return ','.join(format(v, '.7g') for v in struct.unpack(f'<{size // 4}f', raw))
        if mnemonic.endswith(('sd', 'pd')) and size in (8, 16):
            return ','.join(format(v, '.10g') for v in struct.unpack(f'<{size // 8}d', raw))
        return '0x' + raw[::-1].hex()

    def relocs(self):
        """R_X86_64_RELATIVE: slot address -> target."""
        if self._relocs is None:
            self._relocs = {}
            for typ, _addr, off, size in self.sections.values():
                if typ != 4:  # SHT_RELA
                    continue
                for r in range(off, off + size - 23, 24):
                    slot, info, addend = struct.unpack_from('<QQq', self.data, r)
                    if info & 0xffffffff == 8:
                        self._relocs[slot] = addend
                    elif info & 0xffffffff in (1, 6):  # R_X86_64_64, GLOB_DAT
                        self.symbolic.add(slot)
        return self._relocs

    def fde_starts(self):
        hdr = self.sections.get('.eh_frame_hdr')
        if not hdr:
            return set()
        _t, addr, off, _size = hdr
        version, _ptr_enc, count_enc, table_enc = self.data[off:off + 4]
        if (version, count_enc, table_enc) != (1, 0x03, 0x3b):
            return set()
        count, = struct.unpack_from('<I', self.data, off + 8)
        starts = set()
        for i in range(count):
            initial, _fde = struct.unpack_from('<ii', self.data, off + 12 + 8 * i)
            starts.add(addr + initial)
        return starts


def demangle_types(names):
    if not names:
        return {}
    out = subprocess.run(['c++filt'], input='\n'.join('_ZTS' + n for n in names),
                         capture_output=True, text=True).stdout.splitlines()
    return {n: (o[len('typeinfo name for '):] if o.startswith('typeinfo name for ') else n)
            for n, o in zip(names, out)}


def classes(img):
    """RTTI: {class: {'vtable': [function addresses of the primary vtable], 'base': class or None}}."""
    rel = img.relocs()
    typeinfo = {}  # typeinfo object address -> mangled name
    for slot, target in rel.items():
        name = img.cstring(target)
        if name and TYPEINFO_NAME.match(name):
            typeinfo[slot - 8] = name
    pretty = demangle_types(sorted(set(typeinfo.values())))
    out = {}
    for ti, mangled in typeinfo.items():
        base = rel.get(ti + 16)
        if base is None:  # __vmi_class_type_info: flags, base count, then the bases
            base = rel.get(ti + 24)
        out[pretty.get(mangled, mangled)] = {'vtable': [], 'base': typeinfo.get(base), 'ti': ti}
    for name in out:
        b = out[name]['base']
        out[name]['base'] = pretty.get(b, b) if b else None
    by_ti = {v['ti']: k for k, v in out.items()}
    for slot, target in rel.items():
        cls = by_ti.get(target)
        if cls is None or slot - 8 in rel:
            continue
        off = img.offset(slot - 8)
        if off is None or struct.unpack_from('<q', img.data, off)[0] != 0:
            continue  # only primary vtables: offset-to-top 0
        funcs, at = [], slot + 8
        while (at in rel and img.in_text(rel[at])) or at in img.symbolic:
            funcs.append(rel.get(at, 0))  # 0: an imported function (pure virtual)
            at += 8
        while funcs and not funcs[-1]:
            funcs.pop()
        if len(funcs) > len(out[cls]['vtable']):
            out[cls]['vtable'] = funcs
    return out


def lua_callbacks():
    """{Lua class: its callback names} from the dump: the server's CDOTA_*_Lua classes and the
    client's C_DOTA_*_Lua ones (same callbacks)."""
    try:
        with open(API_JSON) as f:
            api = json.load(f)
    except (OSError, ValueError):
        return {}
    out = {}
    for c in api:
        if c.get('name', '').endswith('_Lua'):
            names = {m['name'] for m in c.get('members', [])}
            out[c['name']] = names
            out['C_' + c['name'][1:]] = names
    return out


def ancestors(cls, table):
    seen = []
    while cls and cls in table and cls not in seen:
        seen.append(cls)
        cls = table[cls]['base']
    return seen


def slot_names(table, strings_of):
    """{class: {slot: name}} from the Lua classes: a slot whose Lua-class implementation references
    exactly one of the class's callback names is that callback. The name belongs to the root-most
    ancestor that has the slot (Spawn, Precache: every entity; OnSpellStart: every ability)."""
    out = collections.defaultdict(dict)
    for lua, callbacks in lua_callbacks().items():
        info = table.get(lua)
        if not info or not info['base'] or not callbacks:
            continue
        # the slots the base defines: the usual vtable length of its subclasses (the Lua class may
        # add its own after them)
        sizes = collections.Counter(len(v['vtable']) for v in table.values() if v['base'] == info['base'])
        base_len = min(sizes.most_common(1)[0][0], len(info['vtable']))
        chain = ancestors(info['base'], table)
        for n, fn in enumerate(info['vtable'][:base_len]):
            hits = {s for s in strings_of.get(fn, ()) if s in callbacks}
            if len(hits) != 1:
                continue
            owner = info['base']
            for anc in chain:
                if len(table[anc]['vtable']) > n:
                    owner = anc
            out[owner].setdefault(n, hits.pop())
    return out


def function_names(table, strings_of):
    """Function address -> up to 4 names 'Class::Name' / 'Class::vfunc#N'. Base classes go first,
    so a function many classes share is named after the class that defines it."""
    slots = slot_names(table, strings_of)
    names, more = collections.defaultdict(list), collections.Counter()
    for cls in sorted(table, key=lambda c: len(ancestors(c, table))):
        known = {}
        for anc in ancestors(cls, table):
            for n, name in slots.get(anc, {}).items():
                known.setdefault(n, name)
        for n, fn in enumerate(table[cls]['vtable']):
            if not fn:
                continue
            if len(names[fn]) >= 4:
                more[fn] += 1
                continue
            label = f'{cls}::{known[n]}' if n in known else f'{cls}::vfunc#{n}'
            if label not in names[fn]:
                names[fn].append(label)
    return {fn: labels + ([f'(и ещё {more[fn]} классов)'] if more[fn] else []) for fn, labels in names.items()}


def normalise(img, addr, size, mnemonic, op, start, end, strings, refs):
    def rip(match):
        disp = int(match.group(3), 0)
        target = addr + size + (disp if match.group(2) == '+' else -disp)
        width = match.group(1)
        if width:  # a memory operand: the value, when it is a constant
            value = img.constant(target, SIZES[width], mnemonic)
            if value is not None:
                return f'{width} ptr [K:{value}]'
            return f'{width} ptr [{"T" if img.in_text(target) else "D"}]'
        text = img.cstring(target)
        if text is not None:
            strings.append(text)
            return '[S:' + json.dumps(text[:120]) + ']'
        if img.in_text(target):
            refs.append(target)
            return '[T]'
        return '[D]'

    op = RIP.sub(rip, op)
    if BRANCH.match(mnemonic) and re.fullmatch(r'0x[0-9a-f]+', op):
        target = int(op, 16)
        if start <= target < end:
            op = 'L'
        else:
            op = 'F'
            refs.append(target)
    return f'{mnemonic} {op}'.rstrip()


def tokens(img, insns, start, end):
    strings, refs = [], []
    toks = [normalise(img, a, s, m, o, start, end, strings, refs) for a, s, m, o in insns]
    # trailing nop padding before the next function is not part of the code
    while toks and toks[-1].startswith('nop'):
        toks.pop()
    return toks, strings, refs


def sweep(img, entries):
    """Yields (start, end, [(addr, size, mnemonic, op)]) for every function of .text."""
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    md.skipdata = True
    code = img.data[img.text_off:img.text_off + img.text_size]
    current = []
    for insn in md.disasm_lite(code, img.text_addr):
        addr, _size, mnemonic, _op = insn
        if mnemonic == 'int3':
            if current:
                yield current[0][0], addr, current
                current = []
            continue
        if current and addr in entries:
            yield current[0][0], addr, current
            current = []
        current.append(insn)
    if current:
        yield current[0][0], current[-1][0] + current[-1][1], current


def build_table(path):
    img = Image(path)
    entries = img.fde_starts() | {t for t in img.relocs().values() if img.in_text(t)}
    funcs = []
    for start, end, insns in sweep(img, entries):
        toks, strings, refs = tokens(img, insns, start, end)
        if not toks:
            continue
        h = hashlib.blake2b('\n'.join(toks).encode(), digest_size=8).hexdigest()
        funcs.append([start, end, len(toks), h, list(dict.fromkeys(strings))[:20], [], refs[:MAX_REFS]])
    table = classes(img)
    names = function_names(table, {f[0]: f[4] for f in funcs})
    for f in funcs:
        f[5] = names.get(f[0], [])
    return {'version': CACHE_VERSION, 'lib': os.path.basename(path), 'funcs': funcs}


def cache_path(path):
    return os.path.join(os.path.dirname(os.path.dirname(path)), 'funcs', os.path.basename(path) + '.json.gz')


def load_table(path, build=True):
    """The function table of a library: from the cache, else built (and cached when possible)."""
    cache = cache_path(path)
    try:
        with gzip.open(cache, 'rt') as f:
            table = json.load(f)
        if table.get('version') == CACHE_VERSION and os.path.getmtime(cache) >= os.path.getmtime(path):
            return table
    except (OSError, ValueError):
        pass
    if not build:
        return None
    table = build_table(path)
    try:
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        with gzip.open(cache + '.tmp', 'wt', compresslevel=4) as f:
            json.dump(table, f)
        os.replace(cache + '.tmp', cache)
    except OSError:
        pass
    return table


def function_tokens(path, start, end, img=None):
    img = img or Image(path)
    md = capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_64)
    md.skipdata = True
    off = img.offset(start)
    insns = [i for i in md.disasm_lite(img.data[off:off + (end - start)], start) if i[2] != 'int3']
    return tokens(img, insns, start, end)[0]


def _lis(pairs):
    """Longest chain of pairs increasing in both indexes (pairs sorted by the first)."""
    tails, links, idx = [], [None] * len(pairs), []
    for k, (_i, j) in enumerate(pairs):
        pos = bisect.bisect_left(tails, j)
        if pos == len(tails):
            tails.append(j)
            idx.append(k)
        else:
            tails[pos] = j
            idx[pos] = k
        links[k] = idx[pos - 1] if pos else None
    out, k = [], idx[-1] if idx else None
    while k is not None:
        out.append(pairs[k])
        k = links[k]
    return out[::-1]


def similarity(a, b):
    sa, sb = set(a[4]), set(b[4])
    strings = len(sa & sb) / len(sa | sb) if sa | sb else 0.5
    size = min(a[2], b[2]) / max(a[2], b[2])
    names = 1.0 if a[5] and set(a[5]) & set(b[5]) else 0.0
    return strings + size + names


def _greedy(cands, used_i, used_j, threshold):
    picked = []
    for score, i, j in sorted(cands, reverse=True):
        if score < threshold or i in used_i or j in used_j:
            continue
        used_i.add(i)
        used_j.add(j)
        picked.append((i, j))
    return picked


def match(old, new):
    """Pairs old/new functions: (same, changed, removed, added) as index pairs / lists."""
    oc = collections.Counter(f[3] for f in old)
    nc = collections.Counter(f[3] for f in new)
    where_new = {f[3]: j for j, f in enumerate(new) if nc[f[3]] == 1}
    anchors = _lis(sorted((i, where_new[f[3]]) for i, f in enumerate(old) if oc[f[3]] == 1 and nc[f[3]] == 1))
    same, changed, removed, added = list(anchors), [], [], []
    prev = (-1, -1)
    for ai, aj in anchors + [(len(old), len(new))]:
        os_, ns = list(range(prev[0] + 1, ai)), list(range(prev[1] + 1, aj))
        prev = (ai, aj)
        if not os_ and not ns:
            continue
        # identical code inside the gap, in order
        rest_new, left_old = list(ns), []
        for i in os_:
            k = next((k for k, j in enumerate(rest_new) if new[j][3] == old[i][3]), None)
            if k is None:
                left_old.append(i)
            else:
                same.append((i, rest_new.pop(k)))
        os_, ns = left_old, rest_new
        if len(os_) == len(ns):
            for i, j in zip(os_, ns):
                if similarity(old[i], new[j]) >= 0.6:
                    changed.append((i, j))
                else:
                    removed.append(i)
                    added.append(j)
            continue
        if len(os_) * len(ns) > 250000:
            removed += os_
            added += ns
            continue
        used_i, used_j = set(), set()
        changed += _greedy([(similarity(old[i], new[j]), i, j) for i in os_ for j in ns], used_i, used_j, 1.2)
        removed += [i for i in os_ if i not in used_i]
        added += [j for j in ns if j not in used_j]
    # leftovers across the whole library: same names or shared strings
    buckets = collections.defaultdict(list)
    for j in added:
        for key in new[j][5] + new[j][4]:
            buckets[key].append(j)
    cands = set()
    for i in removed:
        for key in old[i][5] + old[i][4]:
            if len(buckets.get(key, ())) <= 50:
                cands.update((i, j) for j in buckets.get(key, ()))
    used_i, used_j = set(), set()
    changed += _greedy([(similarity(old[i], new[j]), i, j) for i, j in cands], used_i, used_j, 1.5)
    removed = [i for i in removed if i not in used_i]
    added = [j for j in added if j not in used_j]
    return same, sorted(changed), removed, added


def callee_changes(old, new, same):
    """Pairs of identical code whose called/referenced functions are not each other's pairs."""
    o_index = {f[0]: i for i, f in enumerate(old)}
    n_start = [f[0] for f in new]
    pair = dict(same)
    out = []
    for i, j in same:
        for x, y in zip(old[i][6], new[j][6]):
            oi = o_index.get(x)
            if oi is not None and oi in pair and n_start[pair[oi]] != y:
                out.append((i, j, x, y))
                break
    return out


FIELD = re.compile(r'\[(?!rsp|rbp|rip)([re]?[a-z0-9]+) \+ (0x[0-9a-f]+)\]')
VCALL = re.compile(r'^(?:call|jmp) qword ptr \[(?!rsp|rbp|rip)[a-z0-9]+ \+ (0x[0-9a-f]+)\]$')
IMM = re.compile(r'^-?(0x[0-9a-f]+|\d+)$')


def features(toks):
    f = {'strings': collections.Counter(), 'consts': collections.Counter(), 'imms': collections.Counter(),
         'vcalls': collections.Counter(), 'fields': collections.Counter(), 'calls': 0}
    for t in toks:
        mnemonic, _, ops = t.partition(' ')
        f['strings'].update(re.findall(r'\[S:("(?:[^"\\]|\\.)*")\]', ops))
        f['consts'].update(re.findall(r'\[K:([^\]]+)\]', ops))
        m = VCALL.match(t)
        if m:
            f['vcalls'][m.group(1)] += 1
        elif mnemonic != 'lea':
            f['fields'].update(o for _r, o in FIELD.findall(ops))
        if mnemonic == 'call':
            f['calls'] += 1
        parts = [p.strip() for p in ops.split(',')]
        if len(parts) > 1 and parts[0] not in ('rsp', 'rbp', 'esp') and not mnemonic.startswith('nop'):
            f['imms'].update(p for p in parts[1:] if IMM.match(p))
    return f


def summary(old_toks, new_toks):
    a, b = features(old_toks), features(new_toks)
    out = []

    def diff(key, label, fmt=str, cap=12):
        plus = list((b[key] - a[key]).elements())
        minus = list((a[key] - b[key]).elements())
        if plus or minus:
            items = [f'+{fmt(x)}' for x in plus[:cap]] + [f'−{fmt(x)}' for x in minus[:cap]]
            more = max(len(plus) - cap, 0) + max(len(minus) - cap, 0)
            out.append(f'{label}: ' + ' '.join(items) + (f' (и ещё {more})' if more else ''))

    diff('strings', 'строки', cap=20)
    diff('consts', 'константы из данных (числа логики)')
    diff('imms', 'числа в инструкциях', cap=8)
    diff('vcalls', 'виртуальные вызовы', lambda o: f'{o} (слот {int(o, 16) // 8})')
    diff('fields', 'поля объектов')
    if a['calls'] != b['calls']:
        out.append(f"прямых вызовов: {a['calls']} → {b['calls']}")
    out.append(f'инструкций: {len(old_toks)} → {len(new_toks)}')
    return out


def describe(f, callers=None):
    head = f"{f[0]:#x} ({f[1] - f[0]} байт)"
    if f[5]:
        head += ' ' + ', '.join(f[5][:3])
    elif callers:
        head += ' вызывается из: ' + ', '.join(callers[:3])
    if f[4]:
        head += ' | строки: ' + '; '.join(json.dumps(s[:80], ensure_ascii=False) for s in f[4][:8])
    return head


def caller_names(funcs):
    """Function index -> names of the named functions that call / reference it (first 3)."""
    index_of_start = {f[0]: i for i, f in enumerate(funcs)}
    out = collections.defaultdict(list)
    for f in funcs:
        if not f[5]:
            continue
        for t in set(f[6]):
            k = index_of_start.get(t)
            if k is not None and len(out[k]) < 3 and f[5][0] not in out[k]:
                out[k].append(f[5][0])
    return out


def compare(old_path, new_path, diff_budget=250000):
    """Function-level comparison: {'lib', 'counts', 'entries'} for people and models."""
    old = load_table(old_path)['funcs']
    new = load_table(new_path)['funcs']
    same, changed, removed, added = match(old, new)
    swapped = callee_changes(old, new, same)
    changed = [(i, j) for i, j in changed if old[i][3] != new[j][3]]
    # an "added" function whose exact code the old build already has (or a "removed" one the new
    # build still has) is one more / one less copy of a template or folded function, not new code
    o_hashes, n_hashes = {f[3] for f in old}, {f[3] for f in new}
    copies_added = [j for j in added if new[j][3] in o_hashes]
    copies_removed = [i for i in removed if old[i][3] in n_hashes]
    added = [j for j in added if new[j][3] not in o_hashes]
    removed = [i for i in removed if old[i][3] not in n_hashes]
    o_callers, n_callers = caller_names(old), caller_names(new)
    o_img, n_img = Image(old_path), Image(new_path)
    lib = os.path.basename(new_path)
    # code diffs: about diff_budget characters per library in all (50 per line), at least 10 lines
    # a function while the budget lasts; the rest only through so-query fdiff
    per_function = max(10, min(120, diff_budget // max(len(changed), 1) // 50))
    lines_left = diff_budget // 50 * 3 // 2
    entries = []
    for i, j in changed:
        o, n = old[i], new[j]
        ot, nt = function_tokens(old_path, o[0], o[1], o_img), function_tokens(new_path, n[0], n[1], n_img)
        diff = [d[:200] for d in difflib.unified_diff(ot, nt, lineterm='', n=2) if not d.startswith(('---', '+++'))]
        entries.append({'kind': 'changed', 'old': o[0], 'new': n[0], 'names': n[5] or o[5],
                        'title': describe(n, n_callers.get(j)), 'was': f'{o[0]:#x} ({o[1] - o[0]} байт)',
                        'summary': summary(ot, nt), 'diff': diff[:min(per_function, max(lines_left, 0))],
                        'diff_total': len(diff)})
        lines_left -= per_function
    for i, j, x, y in swapped:
        entries.append({'kind': 'callee', 'old': old[i][0], 'new': new[j][0], 'names': new[j][5],
                        'title': describe(new[j], n_callers.get(j)), 'was': f'{old[i][0]:#x}',
                        'summary': [f'код тот же, но вызывает другую функцию: было {x:#x}, стало {y:#x}'],
                        'diff': [], 'diff_total': 0})
    for j in added:
        entries.append({'kind': 'added', 'new': new[j][0], 'names': new[j][5],
                        'title': describe(new[j], n_callers.get(j)), 'summary': [], 'diff': [], 'diff_total': 0})
    for i in removed:
        entries.append({'kind': 'removed', 'old': old[i][0], 'names': old[i][5],
                        'title': describe(old[i], o_callers.get(i)), 'summary': [], 'diff': [], 'diff_total': 0})
    for j in copies_added:
        entries.append({'kind': 'copy_added', 'new': new[j][0], 'names': new[j][5],
                        'title': describe(new[j], n_callers.get(j)), 'summary': [], 'diff': [], 'diff_total': 0})
    for i in copies_removed:
        entries.append({'kind': 'copy_removed', 'old': old[i][0], 'names': old[i][5],
                        'title': describe(old[i], o_callers.get(i)), 'summary': [], 'diff': [], 'diff_total': 0})
    counts = {'functions_old': len(old), 'functions_new': len(new), 'same': len(same) - len(swapped),
              'changed': len(changed) + len(swapped), 'added': len(added), 'removed': len(removed),
              'copies': len(copies_added) + len(copies_removed)}
    return {'lib': lib, 'counts': counts, 'entries': entries}


KIND = {'changed': 'изменена', 'callee': 'изменена', 'added': 'добавлена', 'removed': 'удалена',
        'copy_added': 'ещё одна копия существующего кода', 'copy_removed': 'одной копией существующего кода меньше'}


def render(result, diffs=True):
    c = result['counts']
    lib = result['lib']
    lines = [f"## {lib}: функций {c['functions_old']} → {c['functions_new']}; без изменений {c['same']}, "
             f"изменено {c['changed']}, добавлено {c['added']}, удалено {c['removed']}", '']
    copies = [e for e in result['entries'] if e['kind'].startswith('copy_')]
    for e in result['entries']:
        if e['kind'].startswith('copy_'):
            continue
        lines.append(f"### {KIND[e['kind']]}: {e['title']}")
        if e['kind'] == 'changed':
            lines.append(f"было: {e['was']}")
        lines += [f'- {s}' for s in e['summary']]
        if diffs and e['diff']:
            lines.append('```diff')
            lines += e['diff']
            lines.append('```')
            if e['diff_total'] > len(e['diff']):
                lines.append(f"(ещё {e['diff_total'] - len(e['diff'])} строк диффа: "
                             f"so-query.py fdiff {lib} {e['new']:#x})")
        lines.append('')
    if copies:
        lines.append(f'### копии существующего кода ({len(copies)}): шаблонные / склеенные компоновщиком функции, '
                     'такой же код есть и в другой сборке — не новый код')
        lines += [f"- {KIND[e['kind']]}: {e['title']}" for e in copies[:200]]
        if len(copies) > 200:
            lines.append(f'- … ещё {len(copies) - 200}')
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('old')
    p.add_argument('new')
    p.add_argument('--out')
    p.add_argument('--json', help='also write the comparison as JSON here')
    args = p.parse_args()
    result = compare(args.old, args.new)
    if args.json:
        with open(args.json, 'w') as f:
            json.dump(result, f, ensure_ascii=False)
    text = render(result)
    if args.out:
        with open(args.out, 'w') as f:
            f.write(text)
    else:
        sys.stdout.write(text)


if __name__ == '__main__':
    main()
