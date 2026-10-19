/*
 * Finds the "is the application in tools mode?" checks in libvscript.so that guard the FDesc /
 * CDesc / EDesc documentation tables (see dumper_hook.c). Pattern based, so it survives updates:
 *
 *   1. The engine interface table pairs the name "VApplication001" with the global slot that holds
 *      the IApplication pointer (two R_X86_64_RELATIVE relocations next to each other).
 *   2. Every RIP-relative lea/mov of that slot followed shortly by `call [rax+0xd0]` is a check.
 *
 * Returns the virtual addresses of the `call` instructions.
 */
import * as fs from 'fs';

const R_X86_64_RELATIVE = 8;
const SHT_RELA = 4;
const PT_LOAD = 1;
const PF_X = 1;
const CALL_VFUNC_D0 = Buffer.from([0xff, 0x90, 0xd0, 0x00, 0x00, 0x00]);
const SEARCH_WINDOW = 48;

interface Segment {
  offset: number;
  vaddr: number;
  filesz: number;
  flags: number;
}

export function findVScriptPatchSites(libPath: string): number[] {
  const elf = fs.readFileSync(libPath);
  if (elf.readUInt32BE(0) !== 0x7f454c46 || elf[4] !== 2) {
    throw new Error(`${libPath} is not a 64-bit ELF file`);
  }

  const phoff = Number(elf.readBigUInt64LE(0x20));
  const shoff = Number(elf.readBigUInt64LE(0x28));
  const phentsize = elf.readUInt16LE(0x36);
  const phnum = elf.readUInt16LE(0x38);
  const shentsize = elf.readUInt16LE(0x3a);
  const shnum = elf.readUInt16LE(0x3c);

  const segments: Segment[] = [];
  for (let i = 0; i < phnum; i++) {
    const p = phoff + i * phentsize;
    if (elf.readUInt32LE(p) !== PT_LOAD) continue;
    segments.push({
      flags: elf.readUInt32LE(p + 4),
      offset: Number(elf.readBigUInt64LE(p + 8)),
      vaddr: Number(elf.readBigUInt64LE(p + 16)),
      filesz: Number(elf.readBigUInt64LE(p + 32)),
    });
  }
  const offsetToVaddr = (offset: number) => {
    const s = segments.find((x) => offset >= x.offset && offset < x.offset + x.filesz);
    return s ? offset - s.offset + s.vaddr : undefined;
  };

  // R_X86_64_RELATIVE relocations: slot address -> value written there at load time.
  const relative = new Map<number, number>();
  for (let i = 0; i < shnum; i++) {
    const s = shoff + i * shentsize;
    if (elf.readUInt32LE(s + 4) !== SHT_RELA) continue;
    const offset = Number(elf.readBigUInt64LE(s + 0x18));
    const size = Number(elf.readBigUInt64LE(s + 0x20));
    for (let r = offset; r + 24 <= offset + size; r += 24) {
      if (Number(elf.readBigUInt64LE(r + 8) & 0xffffffffn) !== R_X86_64_RELATIVE) continue;
      relative.set(Number(elf.readBigUInt64LE(r)), Number(elf.readBigInt64LE(r + 16)));
    }
  }

  const name = Buffer.from('\0VApplication001\0', 'latin1');
  let applicationSlot: number | undefined;
  for (let at = elf.indexOf(name); at !== -1; at = elf.indexOf(name, at + 1)) {
    const nameVaddr = offsetToVaddr(at + 1);
    if (nameVaddr === undefined) continue;
    for (const [where, value] of relative) {
      if (value === nameVaddr && relative.has(where + 8)) {
        applicationSlot = relative.get(where + 8);
        break;
      }
    }
    if (applicationSlot !== undefined) break;
  }
  if (applicationSlot === undefined) {
    throw new Error(`VApplication001 interface slot not found in ${libPath}`);
  }

  const sites: number[] = [];
  for (const segment of segments.filter((x) => x.flags & PF_X)) {
    const end = segment.offset + segment.filesz;
    for (let i = segment.offset; i + 7 <= end; i++) {
      // REX.W (+R) lea/mov reg, [rip+rel32]
      if ((elf[i] !== 0x48 && elf[i] !== 0x4c) || (elf[i + 1] !== 0x8d && elf[i + 1] !== 0x8b)) {
        continue;
      }
      if ((elf[i + 2] & 0xc7) !== 0x05) continue;
      const insnVaddr = i - segment.offset + segment.vaddr;
      if (insnVaddr + 7 + elf.readInt32LE(i + 3) !== applicationSlot) continue;

      const window = elf.subarray(i + 7, Math.min(i + 7 + SEARCH_WINDOW, end));
      const call = window.indexOf(CALL_VFUNC_D0);
      if (call !== -1) sites.push(insnVaddr + 7 + call);
    }
  }

  return [...new Set(sites)].sort((a, b) => a - b);
}

if (process.argv[1] && import.meta.url.endsWith(process.argv[1].replace(/\\/g, '/'))) {
  const sites = findVScriptPatchSites(process.argv[2]);
  console.log(sites.map((x) => `0x${x.toString(16)}`).join(','));
}
