import fs from 'fs-extra';
import path from 'path';

export * from './export-types';
export * from './normalization';

// Lines the engine prints on its own while the dumper is writing a section. They are not part of
// any section and can land in the middle of one: 6980 and 6985 had "LUA Memory usage warning: …"
// inside the script_reload JSON, which then failed to parse.
const CONSOLE_NOISE = [/^LUA Memory usage warning: .*$/, /^Stall detected\.$/];
const isConsoleNoise = (line: string) => CONSOLE_NOISE.some((re) => re.test(line.replace(/\r$/, '')));

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
