/*
 * dumper/table_keys.json (the keys server.dll reads from / writes to the Lua tables VScript functions take,
 * see dumper/table-keys.mts) against the documented table types:
 *
 *  - files/vscripts/table_keys.json: every function with its keys, how the engine uses each one (read /
 *    write), whether the type of that argument documents it, and the documented keys it was not seen using;
 *  - the api-types declarations with the keys a type lacks added (description "found in server.dll…"),
 *    so a key a new build starts reading shows up in the types (and in the changelog) without waiting
 *    for someone to describe it. A described key in build/vscripts/api-types/index.ts takes its place.
 *
 * Added to a type are only keys the analysis traced to the Lua table itself, and not:
 *  - nested keys (a.b), keys of entity spawn tables (the whole table goes to the entity's keyvalues),
 *  - keys the engine itself writes into the same table (bookkeeping: creationtime, stack_count…),
 *  - keys only the generic modifier creation reads (AddNewModifier's own keys, documented there).
 */
import * as fs from 'fs';
import * as path from 'path';
import * as apiTypes from './api/types';
import * as apiTypesTypes from './api-types/types';

const INPUT = path.join(__dirname, '..', '..', 'dumper', 'table_keys.json');

interface DumpKey {
  access: string[];
  sources: string[];
}
interface Dump {
  version: string | null;
  functions: Record<string, { keys: Record<string, DumpKey> }>;
}

export interface TableKey {
  name: string;
  /** read: the engine reads it from the table; write: the engine puts it into the table */
  access: ('read' | 'write')[];
  /** the engine code that does it (the binding, a modifier callback, a filter invoker…) */
  sources: string[];
  /** documented by the argument's type (absent when the argument has no table type) */
  documented?: boolean;
  /** added to the type by this build step */
  addedToType?: boolean;
}

export interface TableKeysFunction {
  function: string;
  types: string[];
  keys: TableKey[];
  /** documented keys the analysis did not see the engine use */
  documentedNotSeen?: string[];
  /** filter events: documented keys the engine does not read back after the filter (read-only) */
  notReadBack?: string[];
}

export interface TableKeysFile {
  version: string | null;
  functions: TableKeysFunction[];
}

const READ = new Set(['getvalue', 'kv_get', 'iter_cmp']);
const WRITE = new Set(['setvalue', 'kv_set']);
// types without a function argument of their own in api.json (the argument is typed `table`)
const MANUAL: Record<string, string[]> = {
  SpawnEntityFromTableOptions: [
    '_G.SpawnEntityFromTableSynchronous',
    '_G.SpawnEntityFromTableAsynchronous',
  ],
};
// the whole table becomes the spawned entity's keyvalues: what reads them is entity code, not the binding
const PASSTHROUGH = new Set(['SpawnEntityFromTableOptions', 'CreateUnitFromTableOptions']);
const GENERIC_MODIFIER = 'generic modifier creation';

function typeNames(types: unknown, objects: Map<string, apiTypesTypes.Object>): string[] {
  const names = JSON.stringify(types).match(/"([A-Za-z_][A-Za-z0-9_]*)"/g) ?? [];
  return [...new Set(names.map((x) => x.slice(1, -1)).filter((x) => objects.has(x)))];
}

/** type -> functions with an argument of that type; and the types only used for `callback` arguments */
function typeFunctions(api: apiTypes.Declaration[], objects: Map<string, apiTypesTypes.Object>) {
  const functions = new Map<string, Set<string>>();
  const argNames = new Map<string, Set<string>>();
  const add = (type: string, fn: string, arg: string) => {
    if (!functions.has(type)) functions.set(type, new Set());
    functions.get(type)!.add(fn);
    if (!argNames.has(type)) argNames.set(type, new Set());
    argNames.get(type)!.add(arg);
  };
  for (const top of api) {
    if (top.kind === 'class') {
      for (const member of top.members) {
        if (member.kind !== 'function') continue;
        for (const arg of member.args) {
          for (const t of typeNames(arg.types, objects))
            add(t, `${top.name}.${member.name}`, arg.name);
        }
      }
    } else if (top.kind === 'function') {
      for (const arg of top.args) {
        for (const t of typeNames(arg.types, objects)) add(t, `_G.${top.name}`, arg.name);
      }
    }
  }
  for (const [t, fns] of Object.entries(MANUAL)) for (const fn of fns) add(t, fn, 'table');
  const callbackOnly = new Set(
    [...argNames].filter(([, names]) => names.size === 1 && names.has('callback')).map(([t]) => t),
  );
  return { functions, callbackOnly };
}

function fieldsOf(
  objects: Map<string, apiTypesTypes.Object>,
  name: string,
  own = false,
  seen: string[] = [],
): string[] {
  const d = objects.get(name);
  if (!d || seen.includes(name)) return [];
  const out = d.fields.map((f) => f.name);
  if (!own)
    for (const base of d.extend ?? []) out.push(...fieldsOf(objects, base, false, [...seen, name]));
  return out;
}

function accessOf(k: DumpKey): ('read' | 'write')[] {
  const out: ('read' | 'write')[] = [];
  if (k.access.some((x) => READ.has(x))) out.push('read');
  if (k.access.some((x) => WRITE.has(x))) out.push('write');
  return out;
}

function describe(kind: 'options' | 'filter' | 'outputs', key: TableKey): string {
  const where = key.sources.join(', ');
  if (kind === 'filter') {
    const how = key.access.includes('write')
      ? key.access.includes('read')
        ? 'the engine fills it and reads it back after the filter'
        : 'the engine fills it and does not read it back (read-only)'
      : 'the engine reads it after the filter';
    return `Not described yet: found in server.dll by the dumper (${how}; ${where}).`;
  }
  if (kind === 'outputs') {
    return `Not described yet: found in server.dll by the dumper (the engine fills it; ${where}).`;
  }
  return `Not described yet: found in server.dll by the dumper (read by ${where}).`;
}

/**
 * The api-types declarations with the undocumented keys added, and files/vscripts/table_keys.json.
 * Without dumper/table_keys.json the declarations are returned as they are and the file is null.
 */
export function applyTableKeys(
  api: apiTypes.Declaration[],
  declarations: apiTypesTypes.Declaration[],
): { declarations: apiTypesTypes.Declaration[]; file: TableKeysFile | null } {
  if (!fs.existsSync(INPUT)) return { declarations, file: null };
  const dump: Dump = JSON.parse(fs.readFileSync(INPUT, 'utf8'));
  const dumpFile = path.join(path.dirname(INPUT), 'dump');
  const dumpVersion = fs.existsSync(dumpFile)
    ? fs.readFileSync(dumpFile, 'utf8').match(/ClientVersion=(\d+)/)?.[1]
    : undefined;
  if (dump.version && dumpVersion && dump.version !== dumpVersion) {
    // the analysis failed on this build and kept the previous file (see dumper/table-keys.mts)
    console.warn(`dumper/table_keys.json is from ${dump.version}, the dump is ${dumpVersion}.`);
  }

  const result: apiTypesTypes.Declaration[] = declarations.map((d) =>
    d.kind === 'object' ? { ...d, fields: [...d.fields] } : d,
  );
  const objects = new Map(
    result.filter((d): d is apiTypesTypes.Object => d.kind === 'object').map((d) => [d.name, d]),
  );
  const { functions: typeFns, callbackOnly } = typeFunctions(api, objects);

  // function -> its table types (an Outputs type belongs to the functions of its Inputs type)
  const fnTypes = new Map<string, string[]>();
  for (const name of objects.keys()) {
    const source = name.endsWith('Outputs') ? name.replace(/Outputs$/, 'Inputs') : name;
    const fns = [...(typeFns.get(source) ?? [])];
    if (fns.length === 0 || callbackOnly.has(source)) continue;
    if (fns.every((f) => f.startsWith('CDOTA_Modifier_Lua.'))) continue; // modifier callback parameters
    for (const fn of fns) fnTypes.set(fn, [...(fnTypes.get(fn) ?? []), name]);
  }

  const out: TableKeysFunction[] = [];
  for (const fn of Object.keys(dump.functions).sort()) {
    const dumpKeys = dump.functions[fn].keys;
    const types = (fnTypes.get(fn) ?? []).sort();
    const keys: TableKey[] = Object.keys(dumpKeys)
      .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()) || a.localeCompare(b))
      .map((name) => ({
        name,
        access: accessOf(dumpKeys[name]),
        sources: [...dumpKeys[name].sources].sort(),
      }));
    const entry: TableKeysFunction = { function: fn, types, keys };
    const notSeen = new Set<string>();
    const notReadBack = new Set<string>();
    for (const type of types) {
      const kind = type.endsWith('FilterEvent')
        ? 'filter'
        : type.endsWith('Outputs')
        ? 'outputs'
        : 'options';
      const documented = fieldsOf(objects, type, kind === 'outputs');
      // KeyValues compare keys without case; filter events go through KeyValues too
      const viaKv =
        kind === 'filter' ||
        Object.values(dumpKeys).some((k) =>
          k.access.some((x) => x.startsWith('kv_') || x === 'iter_cmp'),
        );
      const norm = (k: string) => (viaKv ? k.toLowerCase() : k);
      const docSet = new Set(documented.map(norm));
      const relevant = (k: TableKey) =>
        kind === 'outputs'
          ? k.access.includes('write')
          : kind === 'filter'
          ? k.access.length > 0
          : k.access.includes('read');
      for (const key of keys) {
        if (!relevant(key) || key.name.includes('.')) continue;
        if (docSet.has(norm(key.name))) {
          key.documented = true;
          continue;
        }
        key.documented ??= false;
        if (PASSTHROUGH.has(type)) continue;
        if (kind === 'options' && key.access.includes('write')) continue; // engine bookkeeping
        if (key.sources.length > 0 && key.sources.every((s) => s === GENERIC_MODIFIER)) continue;
        const object = objects.get(type)!;
        if (object.fields.some((f) => norm(f.name) === norm(key.name))) continue;
        object.fields.push({
          name: key.name,
          types: ['unknown'],
          description: describe(kind, key),
        });
        key.addedToType = true;
      }
      const seen = new Set(keys.filter(relevant).map((k) => norm(k.name)));
      for (const d of documented) if (!seen.has(norm(d))) notSeen.add(d);
      if (kind === 'filter') {
        const readBack = new Set(
          keys.filter((k) => k.access.includes('read')).map((k) => norm(k.name)),
        );
        for (const d of documented) {
          if (!d.endsWith('_const') && seen.has(norm(d)) && !readBack.has(norm(d)))
            notReadBack.add(d);
        }
      }
    }
    if (notSeen.size > 0 && !types.some((t) => PASSTHROUGH.has(t)))
      entry.documentedNotSeen = [...notSeen].sort();
    if (notReadBack.size > 0) entry.notReadBack = [...notReadBack].sort();
    out.push(entry);
  }
  return { declarations: result, file: { version: dump.version, functions: out } };
}
