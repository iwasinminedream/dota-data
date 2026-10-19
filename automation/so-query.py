#!/usr/bin/env python3
"""
Read-only questions about the two .so snapshots of an update, for the model writing the update
report (the only shell command it may run). Works on the snapshots named in ./so-query.json of
the analysis workspace and nothing else; every answer is capped.

    so-query.py libs                              changed libraries
    so-query.py strings old|new LIB REGEX         read-only-data strings matching REGEX
    so-query.py symbols old|new LIB REGEX         exported symbols (demangled) matching REGEX
    so-query.py xref old|new LIB STRING           code that references the exact string STRING,
                                                  with the instructions around each place
    so-query.py disasm old|new LIB ADDRESS [N]    N bytes (default 160, max 600) of code at ADDRESS

LIB is a file name such as libserver.so. Addresses are virtual addresses (hex).
"""
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

    old, new = sums(snaps['old']), sums(snaps['new'])
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


def cmd_xref(args):
    which, name, text = args
    path = library(which, name)
    data = open(path, 'rb').read()
    segs = segments(data)
    needle = b'\0' + text.encode() + b'\0'
    targets = []
    for at in re.finditer(re.escape(needle), data):
        off = at.start() + 1
        for s_off, vaddr, size, _flags in segs:
            if s_off <= off < s_off + size:
                targets.append(off - s_off + vaddr)
    if not targets:
        fail(f'"{text}" is not a string in {name} ({which})')
    sites = []
    for s_off, vaddr, size, flags in segs:
        if not flags & 1:
            continue
        for i in range(s_off, s_off + size - 7):
            if data[i] in (0x48, 0x4c) and data[i + 1] == 0x8d and data[i + 2] & 0xc7 == 0x05:
                insn = i - s_off + vaddr
                if insn + 7 + int.from_bytes(data[i + 3:i + 7], 'little', signed=True) in targets:
                    sites.append(insn)
    print(f'string at {", ".join(hex(t) for t in targets)}; referenced from {len(sites)} place(s)')
    for site in sites[:8]:
        print(f'--- {site:#x}')
        capped(disasm(path, max(site - 40, 0), 100))
    if len(sites) > 8:
        print(f'... {len(sites) - 8} more places')


def cmd_disasm(args):
    which, name, address = args[:3]
    length = min(int(args[3]), 600) if len(args) > 3 else 160
    capped(disasm(library(which, name), int(address, 16), length))


COMMANDS = {'libs': (cmd_libs, 0), 'strings': (cmd_strings, 3), 'symbols': (cmd_symbols, 3),
            'xref': (cmd_xref, 3), 'disasm': (cmd_disasm, 3)}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        return 1
    fn, nargs = COMMANDS[sys.argv[1]]
    args = sys.argv[2:]
    if len(args) < nargs or (sys.argv[1] != 'disasm' and len(args) > nargs) or len(args) > nargs + 1:
        print(__doc__)
        return 1
    try:
        fn(args)
    except re.error as e:
        fail(f'bad regex: {e}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
