/*
 * Utility script that automatically starts dota with the dumper addon.
 * npm run start:dumper
 */
import { spawn } from 'child_process';
import * as fs from 'fs';
import { Socket } from 'net';
import * as path from 'path';

import { findSteamAppById } from '@moddota/find-steam-app';
import * as vConsole from './vconsole.mts';

const ADDON_NAME = 'dumper';

const dota2Dir = await findSteamAppById(570);

if (!dota2Dir) {
  throw 'Could not locate a dota 2 installation';
} else {
  console.log(`Found DotA 2 installation: ${dota2Dir}`);
}

console.log('Copying dumper addon...');

const addonPath = path.join(dota2Dir, 'game', 'dota_addons', ADDON_NAME);
if (!fs.existsSync(addonPath)) {
  fs.mkdirSync(addonPath);
}

const vscriptsPath = path.join(addonPath, 'scripts', 'vscripts');
if (!fs.existsSync(vscriptsPath)) {
  fs.mkdirSync(vscriptsPath, { recursive: true });
}
fs.copyFileSync(
  path.join('dumper', 'addon_game_mode.lua'),
  path.join(vscriptsPath, 'addon_game_mode.lua'),
);
fs.copyFileSync(path.join('dumper', 'addon_init.lua'), path.join(vscriptsPath, 'addon_init.lua'));

const modifiersPath = path.join(vscriptsPath, 'modifiers');
if (!fs.existsSync(modifiersPath)) {
  fs.mkdirSync(modifiersPath, { recursive: true });
}
fs.copyFileSync(
  path.join('dumper', 'modifier_test_properties.lua'),
  path.join(vscriptsPath, 'modifier_test_properties.lua'),
);

console.log('Starting dumper...');

const dotaBinDir = path.join(dota2Dir, 'game', 'bin', 'win64');
const args = [
  '-novid',
  '-tools',
  '-addon',
  ADDON_NAME,
  `+dota_launch_custom_game ${ADDON_NAME} dota`,
];

const steamInfPath = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
const steamInfContent = fs.readFileSync(steamInfPath);

const dumpWriteStream = fs.createWriteStream('dumper/dump', {});
dumpWriteStream.write(steamInfContent);

let dumpCompleted = false;

//const p2 = spawn(path.join(dotaBinDir, "vconsole2.exe"), { detached: true });
console.log('Spawning Dota:', path.join(dotaBinDir, 'dota2.exe'), args.join(' '));
const p1 = spawn(path.join(dotaBinDir, 'dota2.exe'), args, { cwd: dotaBinDir });

p1.on('error', (err) => {
  console.error('Failed to spawn dota2.exe:', err);
  process.exit(1);
});
p1.on('exit', (code, signal) => {
  console.log(`dota2.exe exited with code=${code} signal=${signal}`);

  try { dumpWriteStream && dumpWriteStream.close(); } catch (e) {}

  if (!dumpCompleted) {
    console.error('dota2.exe exited before the dump was completed.');
    const exitCode = typeof code === 'number' && code !== 0 ? code : 1;
    process.exit(exitCode);
  }
});

await new Promise((r) => setTimeout(r, 5000));

let dotaConsole;
try {
  dotaConsole = await vConsole.connect(29000);
} catch (err) {
  console.error('Не удалось подключиться к vConsole после запуска Dota:', err);
  try { p1.kill(); } catch (e) {}
  process.exit(1);
}

console.log('Connected! Waiting for dump...');

const modifierWriteStream = fs.createWriteStream('dumper/modifier_test_output.txt', {});
let modifierTestCompleted = false;

try {
  await readDump(dotaConsole, dumpWriteStream, modifierWriteStream);
} catch (err) {
  console.error('Failed while reading dump:', err);
  try { p1.kill(); } catch (e) {}
  process.exit(1);
}

await new Promise<void>((resolve) => dumpWriteStream.end(resolve));
await new Promise<void>((resolve) => modifierWriteStream.end(resolve));

dumpCompleted = true;
modifierTestCompleted = true;
console.log('Saved dump + modifier test — exiting dumper.');

try {
  await vConsole.disconnect(dotaConsole);
} catch (e) {

}

try { p1.kill(); } catch (e) {}

process.exit(0);


async function readDump(dota: Socket, dumpStream: fs.WriteStream, modifierStream: fs.WriteStream): Promise<void> {
  return new Promise((resolve) => {
    let dumpReading = false;
    let dumpDone = false;
    let modifierReading = false;
    let modifierDone = false;

    function checkDone() {
      if (dumpDone && modifierDone) {
        resolve();
      }
    }

    vConsole.onMessage(dota, (type, channel, message) => {
      if (type === 'PRNT') {
        // Dump capture
        if (!dumpDone) {
          if (message.startsWith('$>')) {
            dumpReading = true;
          }
          if (message.startsWith('===ENDOFDUMP')) {
            dumpReading = false;
            dumpDone = true;
            console.log('Dump completed. Waiting for modifier test...');
            checkDone();
          } else if (dumpReading) {
            dumpStream.write(message);
          }
        }

        // Modifier test capture
        if (message.startsWith('local previous_state')) {
          modifierReading = true;
        }
        if (message.startsWith('===ENDOFMODIFIERTEST')) {
          modifierReading = false;
          modifierDone = true;
          console.log('Modifier test completed.');
          checkDone();
        } else if (modifierReading) {
          modifierStream.write(message);
        }
      }
    });
  });
}
