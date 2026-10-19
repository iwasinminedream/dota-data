/*
 * Things a Linux dump cannot see, taken over from the previous dump (normally a Windows -tools
 * one) so the generated files do not lose them:
 *
 * - cvarlist: a retail client only registers part of the convars; the ~2600 development ones are
 *   compiled in but only appear with -tools, which does not exist on Linux. Entries missing from
 *   the new list are copied from the previous dump. They can only be refreshed by a Windows dump.
 * - TypeScript declarations: the Linux client prints 64-bit integer arguments (e.g.
 *   SetDialogVariableTime's time) without a type. When the previous dump has the same interface
 *   member with the same arguments plus the missing types, its line is used.
 */

interface Section {
  name: string;
  body: string;
}

interface SplitDump {
  head: string;
  sections: Section[];
}

export interface CarryForwardReport {
  convars: number;
  typedMembers: number;
}

const DECLARATION_SECTIONS = [
  'cl_panorama_typescript_declarations',
  'panel_typescript_declarations',
];

export function splitDump(text: string): SplitDump {
  const parts = text.split(/^\$> (.+)\n/m);
  const sections: Section[] = [];
  for (let i = 1; i < parts.length; i += 2) sections.push({ name: parts[i], body: parts[i + 1] });
  return { head: parts[0], sections };
}

export function joinDump({ head, sections }: SplitDump): string {
  return head + sections.map((s) => `$> ${s.name}\n${s.body}`).join('');
}

const cvarName = (line: string) => line.split(' : ')[0].trim();
const cvarSortKey = (name: string) => name.replace(/^[+-]/, '').toLowerCase();

export function compareCvarNames(a: string, b: string): number {
  const ka = cvarSortKey(a);
  const kb = cvarSortKey(b);
  if (ka !== kb) return ka < kb ? -1 : 1;
  return a < b ? -1 : a > b ? 1 : 0;
}

/** Adds previous cvarlist entries the new list lacks; returns the new body and how many. */
export function mergeCvarlist(body: string, previousBody: string): { body: string; added: number } {
  const isEntry = (line: string) => line.includes(' : ') && !line.startsWith('cvar list');
  const lines = body.split('\n');
  const first = lines.findIndex(isEntry);
  if (first === -1) return { body, added: 0 };
  let last = first;
  while (last + 1 < lines.length && isEntry(lines[last + 1])) last++;

  const entries = lines.slice(first, last + 1);
  const known = new Set(entries.map(cvarName));
  const carried = previousBody
    .split('\n')
    .filter((line) => isEntry(line) && !known.has(cvarName(line)));
  if (carried.length === 0) return { body, added: 0 };

  const merged = [...entries, ...carried].sort((a, b) =>
    compareCvarNames(cvarName(a), cvarName(b)),
  );
  const tail = lines
    .slice(last + 1)
    .map((line) => line.replace(/^(\s*)\d+( total convars\/concommands)/, `$1${merged.length}$2`));
  return { body: [...lines.slice(0, first), ...merged, ...tail].join('\n'), added: carried.length };
}

const MEMBER = /^(\s*)([\w$.]+)\((.*)\)(.*);\s*$/;

function memberArgs(line: string): string[] | null {
  const match = MEMBER.exec(line);
  if (!match) return null;
  return match[3].trim() === '' ? [] : match[3].split(',').map((x) => x.trim());
}

function declarationIndex(body: string): Map<string, string> {
  const index = new Map<string, string>();
  let iface = '';
  for (const line of body.split('\n')) {
    const header = /^interface ([\w$]+)/.exec(line);
    if (header) {
      iface = header[1];
      continue;
    }
    const match = MEMBER.exec(line);
    if (match) index.set(`${iface}.${match[2]}`, line);
  }
  return index;
}

/** Restores argument types the Linux client printed without; returns the new body and count. */
export function restoreArgumentTypes(
  body: string,
  previous: Map<string, string>,
): { body: string; restored: number } {
  let iface = '';
  let restored = 0;
  const lines = body.split('\n').map((line) => {
    const header = /^interface ([\w$]+)/.exec(line);
    if (header) {
      iface = header[1];
      return line;
    }
    const match = MEMBER.exec(line);
    if (!match) return line;
    const args = memberArgs(line)!;
    if (!args.some((arg) => !arg.includes(':'))) return line;

    const old = previous.get(`${iface}.${match[2]}`);
    const oldArgs = old && memberArgs(old);
    if (!old || !oldArgs || oldArgs.length !== args.length) return line;
    const compatible = args.every(
      (arg, i) => arg === oldArgs[i] || (!arg.includes(':') && oldArgs[i].startsWith(`${arg}:`)),
    );
    if (!compatible || old.trim() === line.trim() || MEMBER.exec(old)![4] !== match[4]) return line;
    restored++;
    return match[1] + old.trimStart();
  });
  return { body: lines.join('\n'), restored };
}

export function carryForward(
  dump: string,
  previousDump: string,
): { dump: string; report: CarryForwardReport } {
  const current = splitDump(dump);
  const previous = splitDump(previousDump);
  const previousBody = (name: string) => previous.sections.find((s) => s.name === name)?.body;
  const report: CarryForwardReport = { convars: 0, typedMembers: 0 };

  const oldDeclarations = new Map<string, string>();
  for (const name of DECLARATION_SECTIONS) {
    const body = previousBody(name);
    if (body) for (const [key, line] of declarationIndex(body)) oldDeclarations.set(key, line);
  }

  for (const section of current.sections) {
    if (section.name === 'cvarlist') {
      const old = previousBody('cvarlist');
      if (old) {
        const { body, added } = mergeCvarlist(section.body, old);
        section.body = body;
        report.convars += added;
      }
    } else if (DECLARATION_SECTIONS.includes(section.name)) {
      const { body, restored } = restoreArgumentTypes(section.body, oldDeclarations);
      section.body = body;
      report.typedMembers += restored;
    }
  }

  return { dump: joinDump(current), report };
}
