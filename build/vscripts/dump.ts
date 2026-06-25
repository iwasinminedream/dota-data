import { execSync } from 'child_process';
import { readFileSync } from 'fs';
import { join } from 'path';
import { readDump } from '../util';
import { unknownTypeFixes } from './unknown-type-fixes';

const reloadMessage = 'Initializing script VM...\n...done';
const repoRoot = join(__dirname, '../..');

// ---------------------------------------------------------------------------
// Carry-forward of known types over <unknown>.
//
// The engine intermittently reports <unknown> for native argument/return types
// (Vector, QAngle, string, …). When a previous published version had a real type
// there, reuse it instead of letting the type degrade to <unknown>. This keeps
// the API stable and stops the changelog from showing phantom "Vector -> unknown"
// changes — without needing a manual entry per occurrence.
// ---------------------------------------------------------------------------
function coreType(types: unknown): string | null {
  if (!Array.isArray(types)) return null;
  const real = types.find((t) => typeof t === 'string' && t !== 'nil' && t !== 'unknown');
  return typeof real === 'string' ? real : null;
}

function gitShow(ref: string, file: string): string {
  return execSync(`git show ${ref}:${file}`, {
    cwd: repoRoot,
    maxBuffer: 512 * 1024 * 1024,
    stdio: ['pipe', 'pipe', 'ignore'],
  }).toString('utf8');
}

interface PrevMethodTypes {
  args: (string | null)[];
  returns: string | null;
}

// Map of `${className}.${method}` (or `_G.${func}`) → previous-version types.
function loadPreviousApiTypes(): Map<string, PrevMethodTypes> {
  const map = new Map<string, PrevMethodTypes>();
  try {
    const currentVersion = readFileSync(join(repoRoot, 'dumper', 'dump'), 'utf8').match(
      /ClientVersion=(\d+)/,
    )?.[1];
    const shas = execSync('git rev-list --max-count=60 HEAD', {
      cwd: repoRoot,
      stdio: ['pipe', 'pipe', 'ignore'],
    })
      .toString()
      .trim()
      .split('\n')
      .filter(Boolean);

    // Find the most recent commit whose dump is a DIFFERENT version — that is the
    // previous published version whose types we want to carry forward.
    let apiJson: unknown = null;
    for (const sha of shas) {
      try {
        const ver = gitShow(sha, 'dumper/dump').match(/ClientVersion=(\d+)/)?.[1];
        if (ver && ver !== currentVersion) {
          apiJson = JSON.parse(gitShow(sha, 'files/vscripts/api.json'));
          break;
        }
      } catch {
        // dump/api.json missing in this commit — keep walking back.
      }
    }
    if (!Array.isArray(apiJson)) return map;

    const add = (key: string, member: { args?: { types?: unknown }[]; returns?: unknown }) => {
      map.set(key, {
        args: (member.args ?? []).map((a) => coreType(a.types)),
        returns: coreType(member.returns),
      });
    };
    for (const item of apiJson as any[]) {
      if (item.kind === 'class' && Array.isArray(item.members)) {
        for (const m of item.members) if (m.kind === 'function') add(`${item.name}.${m.name}`, m);
      } else if (item.kind === 'function') {
        add(`_G.${item.name}`, item);
      }
    }
  } catch {
    // No git history / first build — nothing to carry forward.
  }
  return map;
}

const previousApiTypes = loadPreviousApiTypes();

// Only native C++ types that the engine genuinely fails to resolve (reporting
// <unknown>) are safe to carry forward into the RAW dump. Carrying forward a
// processed type (e.g. an enum like DOTATeam_t that an extension override added)
// would inject a value that isn't a valid dump source type and break type
// validation.
const CARRY_FORWARD_TYPES = new Set(['Vector', 'QAngle', 'Vector2D', 'Quaternion', 'string']);

// Fill any remaining <unknown> args/returns of a dump method from the previous
// version's types (matched by name and positional arg index).
function carryForwardUnknowns(key: string, member: DumpMethod): void {
  const prev = previousApiTypes.get(key);
  if (!prev) return;
  member.args.forEach((arg, i) => {
    const t = prev.args[i];
    if (arg.type === '<unknown>' && t && CARRY_FORWARD_TYPES.has(t)) arg.type = t;
  });
  if (member.returns === '<unknown>' && prev.returns && CARRY_FORWARD_TYPES.has(prev.returns)) {
    member.returns = prev.returns;
  }
}

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
function applyManualArgFix(member: DumpMethod, fix: { returns?: string; args?: Record<number, string> }) {
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

function applyUnknownTypeFixes(dump: Dump): Dump {
  for (const item of dump) {
    if (item.kind === 'class') {
      // Normalize C_ prefix for client-side classes (e.g. C_BaseEntity → CBaseEntity)
      const normalizedName = item.name.replace(/^C_/, 'C');
      const classFixes = unknownTypeFixes[normalizedName];

      for (const member of item.members) {
        const fix = classFixes?.[member.name];
        if (fix) applyManualArgFix(member, fix);
        // Fill any <unknown> still left over from the previous version's types.
        carryForwardUnknowns(`${normalizedName}.${member.name}`, member);
      }
    } else if (item.kind === 'function') {
      const fix = unknownTypeFixes._G?.[item.name];
      if (fix) applyManualArgFix(item, fix);
      carryForwardUnknowns(`_G.${item.name}`, item);
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
