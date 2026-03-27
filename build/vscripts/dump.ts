import { readDump } from '../util';
import { unknownTypeFixes } from './unknown-type-fixes';

const reloadMessage = 'Initializing script VM...\n...done';

/**
 * Apply known type corrections for `<unknown>` types in the parsed dump.
 *
 * The engine's Lua binding reflection system returns `<unknown>` for certain
 * native C++ types (Vector, QAngle, string). This function replaces them with
 * the correct types based on a known corrections map.
 *
 * Client-side class names (prefixed with `C_`) are normalized to server-side
 * names (prefixed with `C`) for lookup purposes.
 */
function applyUnknownTypeFixes(dump: Dump): Dump {
  for (const item of dump) {
    if (item.kind === 'class') {
      // Normalize C_ prefix for client-side classes (e.g. C_BaseEntity → CBaseEntity)
      const normalizedName = item.name.replace(/^C_/, 'C');
      const classFixes = unknownTypeFixes[normalizedName];
      if (!classFixes) continue;

      for (const member of item.members) {
        const fix = classFixes[member.name];
        if (!fix) continue;

        if (fix.returns && member.returns === '<unknown>') {
          member.returns = fix.returns;
        }
        if (fix.args) {
          for (const [idx, type] of Object.entries(fix.args)) {
            const argIndex = Number(idx);
            if (member.args[argIndex]?.type === '<unknown>') {
              member.args[argIndex].type = type;
            }
          }
        }
      }
    } else if (item.kind === 'function') {
      const fix = unknownTypeFixes._G?.[item.name];
      if (!fix) continue;

      if (fix.returns && item.returns === '<unknown>') {
        item.returns = fix.returns;
      }
      if (fix.args) {
        for (const [idx, type] of Object.entries(fix.args)) {
          const argIndex = Number(idx);
          if (item.args[argIndex]?.type === '<unknown>') {
            item.args[argIndex].type = type;
          }
        }
      }
    }
  }
  return dump;
}

export const clientDump: Dump = applyUnknownTypeFixes(
  JSON.parse(readDump('cl_script_reload').replace(reloadMessage, '')),
);

let _serverDump: Dump;
try {
  _serverDump = applyUnknownTypeFixes(
    JSON.parse(readDump('script_reload').replace(reloadMessage, '')),
  );
} catch {
  console.warn('Warning: Failed to parse server dump, falling back to client dump');
  _serverDump = clientDump;
}
export const serverDump: Dump = _serverDump;

export type Dump = (DumpConstant | DumpClass | DumpFunction)[];

export interface DumpConstant {
  kind: 'constant';
  name: string;
  value: number;
  enum?: string;
  description?: string;
}

export interface DumpClass {
  kind: 'class';
  name: string;
  members: DumpMethod[];
  extend?: string;
  instance?: string;
}

export interface DumpMethod {
  name: string;
  description?: string;
  args: { name?: string; type: string }[];
  returns: string;
}

export interface DumpFunction extends DumpMethod {
  kind: 'function';
}
