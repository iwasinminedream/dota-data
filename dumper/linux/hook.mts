/*
 * Builds dumper_hook.so (see dumper_hook.c) and computes the environment the Linux client needs.
 */
import { execFileSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

import { findVScriptPatchSites } from './vscript-patch.mts';

const here = path.dirname(fileURLToPath(import.meta.url));

export function buildHook(): string {
  const source = path.join(here, 'dumper_hook.c');
  const output = path.join(here, '.build', 'dumper_hook.so');
  if (fs.existsSync(output) && fs.statSync(output).mtimeMs >= fs.statSync(source).mtimeMs) {
    return output;
  }

  fs.mkdirSync(path.dirname(output), { recursive: true });
  try {
    execFileSync(
      'gcc',
      [
        '-shared',
        '-fPIC',
        '-O2',
        '-Wall',
        '-o',
        output,
        source,
        '-Wl,--no-as-needed',
        '-l:libdl.so.2',
      ],
      { stdio: 'inherit' },
    );
  } catch (err) {
    throw new Error(`Building ${source} failed (is gcc installed?): ${err}`);
  }
  return output;
}

export function hookEnvironment(dota2Dir: string, clipboardFile: string): Record<string, string> {
  const libvscript = path.join(dota2Dir, 'game', 'bin', 'linuxsteamrt64', 'libvscript.so');
  const sites = findVScriptPatchSites(libvscript);
  if (sites.length === 0) {
    throw new Error(
      `No tools-mode checks found in ${libvscript}: the Lua API dump would be empty. ` +
        'dumper/linux/vscript-patch.mts needs updating for this Dota build.',
    );
  }
  console.log(`libvscript.so: enabling script documentation at ${sites.length} sites`);

  return {
    LD_PRELOAD: [buildHook(), process.env.LD_PRELOAD].filter(Boolean).join(':'),
    DUMPER_VSCRIPT_PATCH: sites.map((x) => `0x${x.toString(16)}`).join(','),
    DUMPER_CLIPBOARD_FILE: clipboardFile,
  };
}
