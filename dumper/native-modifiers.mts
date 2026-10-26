/*
 * Native modifiers: the modifier functions every native (C++) modifier implements and the formulas of
 * its properties, read offline from server.dll by dumper/native-modifiers/extract.py (Python 3 +
 * capstone, see dumper/native-modifiers/README.md) into dumper/native_modifiers.json, and the same from
 * client.dll (the client's own code of the same modifiers: what it predicts and shows in tooltips) into
 * dumper/native_modifiers_client.json.
 *
 * Runs at the end of every successful `npm run auto-dump`, or alone: `npm run dump:native-modifiers`.
 * Needs the Windows DLLs (`DOTA_SERVER_BINARY` points at server.dll on Linux, as for build/engine-enums;
 * client.dll is taken from the same directory, or from `DOTA_CLIENT_BINARY`); with only libserver.so,
 * or without Python / capstone, the previous files are kept and a warning printed.
 */
import { spawnSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

// CommonJS module (build/ is not ESM): named imports are not visible from .mts.
import dotaDir from '../build/util/dota-dir';

const OUTPUT = path.join('dumper', 'native_modifiers.json');
const CLIENT_OUTPUT = path.join('dumper', 'native_modifiers_client.json');
const SCRIPT = path.join('dumper', 'native-modifiers', 'extract.py');

function pythonCommands(): string[][] {
  if (process.env.DUMPER_PYTHON) return [[process.env.DUMPER_PYTHON]];
  return process.platform === 'win32'
    ? [['python'], ['py', '-3'], ['python3']]
    : [['python3'], ['python']];
}

/** Runs extract.py on one DLL; returns true when `output` was rewritten. */
function extract(binary: string, output: string, version?: string): boolean {
  const partial = `${output}.partial`;
  const args = [SCRIPT, '--dll', binary, '--out', partial];
  if (version) args.push('--version', version);
  for (const [command, ...prefix] of pythonCommands()) {
    console.log(`Native modifiers: ${command} ${[...prefix, ...args].join(' ')}`);
    const result = spawnSync(command, [...prefix, ...args], { stdio: 'inherit' });
    if (result.error && (result.error as NodeJS.ErrnoException).code === 'ENOENT') continue;
    if (result.status === 0 && fs.existsSync(partial)) {
      fs.renameSync(partial, output);
      console.log(`Saved ${output}`);
      return true;
    }
    fs.rmSync(partial, { force: true });
    console.warn(
      `Native modifiers failed (exit ${result.status}); ${output} was kept. ` +
        'The analysis needs Python 3 with capstone 5 (pip install capstone).',
    );
    return false;
  }
  console.warn(
    `Native modifiers skipped: no Python 3 found (set DUMPER_PYTHON). ${output} was kept.`,
  );
  return false;
}

/** Returns true when dumper/native_modifiers.json (server.dll) was rewritten. */
export function extractNativeModifiers(dota2Dir: string, version?: string): boolean {
  let binary: string;
  try {
    binary = dotaDir.findServerBinary(dota2Dir);
  } catch (error) {
    console.warn(`Native modifiers skipped: ${(error as Error).message}`);
    return false;
  }
  if (!binary.toLowerCase().endsWith('.dll')) {
    console.warn(
      `Native modifiers skipped: the analysis reads the Windows server.dll, found ${binary} ` +
        `(set DOTA_SERVER_BINARY). ${OUTPUT} and ${CLIENT_OUTPUT} were kept.`,
    );
    return false;
  }
  if (!extract(binary, OUTPUT, version)) return false;

  const client = process.env.DOTA_CLIENT_BINARY ?? path.join(path.dirname(binary), 'client.dll');
  if (fs.existsSync(client)) extract(client, CLIENT_OUTPUT, version);
  else console.warn(`Native modifiers: no ${client} (set DOTA_CLIENT_BINARY); ${CLIENT_OUTPUT} was kept.`);
  return true;
}

/** ClientVersion of the installed game (the build its server.dll belongs to). */
export function installedVersion(dota2Dir: string): string | undefined {
  const inf = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
  if (!fs.existsSync(inf)) return undefined;
  return fs.readFileSync(inf, 'utf8').match(/ClientVersion=(\d+)/)?.[1];
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const dota2Dir = await dotaDir.findDota2Dir();
  process.exit(extractNativeModifiers(dota2Dir, installedVersion(dota2Dir)) ? 0 : 1);
}
