import * as fs from 'fs';

// Read-only parser for Valve VPK v1/v2 directory archives.
// Replaces the `vpk` npm package (which transitively pulled `jbinary` → `request`).
// Format reference: https://developer.valvesoftware.com/wiki/VPK_(file_format)

const SIGNATURE = 0x55aa1234;
const HEADER_1_LENGTH = 12;
const HEADER_2_LENGTH = 28;
const ARCHIVE_INDEX_INLINE = 0x7fff;
const ENTRY_TERMINATOR = 0xffff;

interface VpkEntry {
  crc: number;
  preloadBytes: number;
  archiveIndex: number;
  entryOffset: number;
  entryLength: number;
  preloadOffset: number;
}

let crcTable: Uint32Array | null = null;
function getCrcTable(): Uint32Array {
  if (crcTable) return crcTable;
  const table = new Uint32Array(256);
  for (let i = 0; i < 256; i++) {
    let c = i;
    for (let k = 0; k < 8; k++) {
      c = (c & 1) !== 0 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    }
    table[i] = c;
  }
  crcTable = table;
  return table;
}

function crc32(buf: Buffer): number {
  const table = getCrcTable();
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) {
    c = table[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  }
  return (c ^ 0xffffffff) >>> 0;
}

export default class VPK {
  private buffer!: Buffer;
  private version!: number;
  private treeLength!: number;
  private headerLength!: number;
  private tree!: Map<string, VpkEntry>;

  constructor(private readonly directoryPath: string) {}

  load(): void {
    this.buffer = fs.readFileSync(this.directoryPath);
    let offset = 0;

    const signature = this.buffer.readUInt32LE(offset);
    offset += 4;
    if (signature !== SIGNATURE) {
      throw new Error(`VPK signature is invalid: 0x${signature.toString(16)}`);
    }

    this.version = this.buffer.readUInt32LE(offset);
    offset += 4;
    if (this.version !== 1 && this.version !== 2) {
      throw new Error(`VPK version ${this.version} is not supported`);
    }

    this.treeLength = this.buffer.readUInt32LE(offset);
    offset += 4;

    if (this.version === 2) {
      // Skip 4×uint32: unknown1, footerLength, unknown3, unknown4
      offset += 16;
      this.headerLength = HEADER_2_LENGTH;
    } else {
      this.headerLength = HEADER_1_LENGTH;
    }

    this.tree = new Map();

    // Tree layout: extension → directory → filename → entry, each level
    // null-terminated and ended by an empty string. A single space (' ')
    // is used as a sentinel for "none" (no extension / no directory / blank filename).
    while (true) {
      const ext = this.readCString(offset);
      offset = ext.next;
      if (ext.value === '') break;

      while (true) {
        const dir = this.readCString(offset);
        offset = dir.next;
        if (dir.value === '') break;

        while (true) {
          const fname = this.readCString(offset);
          offset = fname.next;
          if (fname.value === '') break;

          let fullPath = fname.value === ' ' ? '' : fname.value;
          if (ext.value !== ' ') fullPath += '.' + ext.value;
          if (dir.value !== ' ') fullPath = dir.value + '/' + fullPath;

          const entry: VpkEntry = {
            crc: this.buffer.readUInt32LE(offset),
            preloadBytes: this.buffer.readUInt16LE(offset + 4),
            archiveIndex: this.buffer.readUInt16LE(offset + 6),
            entryOffset: this.buffer.readUInt32LE(offset + 8),
            entryLength: this.buffer.readUInt32LE(offset + 12),
            preloadOffset: 0,
          };
          const terminator = this.buffer.readUInt16LE(offset + 16);
          if (terminator !== ENTRY_TERMINATOR) {
            throw new Error(`Directory terminator is invalid for ${fullPath}`);
          }
          offset += 18;

          entry.preloadOffset = offset;
          offset += entry.preloadBytes;

          this.tree.set(fullPath, entry);
        }
      }
    }
  }

  get files(): string[] {
    return [...this.tree.keys()];
  }

  getFile(internalPath: string): Buffer {
    const entry = this.tree.get(internalPath);
    if (!entry) {
      throw new Error(`File not found in VPK: ${internalPath}`);
    }

    const out = Buffer.alloc(entry.preloadBytes + entry.entryLength);

    if (entry.preloadBytes > 0) {
      this.buffer.copy(
        out,
        0,
        entry.preloadOffset,
        entry.preloadOffset + entry.preloadBytes,
      );
    }

    if (entry.entryLength > 0) {
      if (entry.archiveIndex === ARCHIVE_INDEX_INLINE) {
        // File data is appended to the _dir.vpk after the tree
        const dataStart = this.headerLength + this.treeLength + entry.entryOffset;
        this.buffer.copy(out, entry.preloadBytes, dataStart, dataStart + entry.entryLength);
      } else {
        // File data is in a numbered archive: pak01_NNN.vpk
        const fileIndex = String(entry.archiveIndex).padStart(3, '0');
        const archivePath = this.directoryPath.replace(/_dir\.vpk$/, `_${fileIndex}.vpk`);
        const fd = fs.openSync(archivePath, 'r');
        try {
          fs.readSync(fd, out, entry.preloadBytes, entry.entryLength, entry.entryOffset);
        } finally {
          fs.closeSync(fd);
        }
      }
    }

    if (crc32(out) !== entry.crc) {
      throw new Error(`CRC does not match for ${internalPath}`);
    }

    return out;
  }

  private readCString(start: number): { value: string; next: number } {
    let end = start;
    while (end < this.buffer.length && this.buffer[end] !== 0) end++;
    const value = this.buffer.toString('utf8', start, end);
    return { value, next: end + 1 };
  }
}
