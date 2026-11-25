import fs from 'fs-extra';
import path from 'path';

export * from './export-types';
export * from './normalization';

// Lines the engine prints on its own while the dumper is writing a section. They are not part of
// any section and can land in the middle of one: 6980 and 6985 had "LUA Memory usage warning: …"
// inside the script_reload JSON, which then failed to parse; 6996 had Steam's networking warning
// (two lines) there.
const CONSOLE_NOISE = [
  /^LUA Memory usage warning: .*$/,
  /^Stall detected\.$/,
  /^SteamNetworkingSockets lock held for .*$/,
  /^This is usually a symptom of a general performance problem such as thread starvation\.$/,
];
const isConsoleNoise = (line: string) =>
  CONSOLE_NOISE.some((re) => re.test(line.replace(/\r$/, '')));

const dump = fs
  .readFileSync(path.join(__dirname, '../../dumper/dump'), 'utf8')
  .split('\n')
  .filter((line) => !isConsoleNoise(line))
  .join('\n');
const [, ...dumpGroups] = dump.split(/\$> (.+)/g);

export function tryReadDump(name: string): string | undefined {
  const index = dumpGroups.indexOf(name);
  if (index === -1) return undefined;
  let value = dumpGroups[index + 1];
  // eslint-disable-next-line @typescript-eslint/no-unnecessary-condition
  if (value == null) return undefined;
  if (value.trim().startsWith('Initializing')) {
    // Cut off initializing scripting VM line
    value = value.slice(value.indexOf('['));
  }

  return value.trim();
}

/**
 * A JSON section of the dump. The dumper writes it pretty-printed: every line of it is indented or
 * starts with a bracket, a brace or a quote. When it does not parse, lines that start with a letter
 * in the first column (console output of the engine that is not in CONSOLE_NOISE yet) are dropped
 * and it is parsed again, with a warning naming them; if it still does not parse, the error stands.
 */
export function parseDumpJson<T = any>(text: string, section: string): T {
  try {
    return JSON.parse(text);
  } catch (error) {
    const dropped: string[] = [];
    const kept = text
      .split('\n')
      .filter((line) => (/^[A-Za-z]/.test(line) ? (dropped.push(line.trim()), false) : true))
      .join('\n');
    if (dropped.length === 0) throw error;
    let value: T;
    try {
      value = JSON.parse(kept);
    } catch {
      throw error;
    }
    console.warn(
      `Dump section "${section}": dropped ${dropped.length} console line(s) inside its JSON ` +
        `(add them to CONSOLE_NOISE in build/util):\n  ${dropped
          .map((l) => l.slice(0, 160))
          .join('\n  ')}`,
    );
    return value;
  }
}

export function readDump(name: string) {
  const value = tryReadDump(name);
  if (value === undefined) throw new Error(`Couldn't find dump "${name}"`);
  return value;
}

const FILES = path.join(__dirname, '../../files');
export const outputFile = (name: string, data: string) =>
  fs.outputFileSync(path.join(FILES, name), `${data.trimEnd()}\n`);
export const outputJson = (name: string, data: any) =>
  fs.outputJsonSync(path.join(FILES, `${name}.json`), data, { spaces: 2 });
