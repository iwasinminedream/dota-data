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
const dotaExe = path.join(dotaBinDir, 'dota2.exe');
const args = [
  '-novid',
  '-tools',
  '-addon',
  ADDON_NAME,
  `+dota_launch_custom_game ${ADDON_NAME} dota`,
];

const steamInfPath = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
const steamInfContent = fs.readFileSync(steamInfPath);

// --- Tunables -------------------------------------------------------------
const CONNECT_PORT = 29000;
const STARTUP_DELAY_MS = 5000; // give Dota a moment before connecting to vConsole
const DUMP_TIMEOUT_MS = 4 * 60 * 1000; // hard cap from connect to ===ENDOFDUMP
const INACTIVITY_TIMEOUT_MS = 120 * 1000; // no console output this long => Dota frozen
// (must exceed the gap between connecting and the match reaching GAME_IN_PROGRESS,
// when the dump fires — otherwise a slow load looks like a freeze)
const MODIFIER_GRACE_MS = 45 * 1000; // after the dump, wait this long for the modifier test
// (the modifier test is currently disabled in addon_game_mode.lua, so this is
// just the upper bound the dumper waits before finishing on the dump alone)
const HEARTBEAT_MS = 10 * 1000;
const MAX_ATTEMPTS = 3;

let succeeded = false;
for (let attempt = 1; attempt <= MAX_ATTEMPTS && !succeeded; attempt++) {
  console.log(`\n=== Dump attempt ${attempt}/${MAX_ATTEMPTS} ===`);
  succeeded = await runAttempt();
  if (!succeeded && attempt < MAX_ATTEMPTS) {
    console.warn('Attempt did not produce a complete dump — retrying with a fresh Dota launch...');
    await delay(3000);
  }
}

if (!succeeded) {
  console.error(`Failed to capture a complete dump after ${MAX_ATTEMPTS} attempts.`);
  process.exit(1);
}

console.log('\nSaved dump + modifier test — dumper finished successfully.');
process.exit(0);

// --------------------------------------------------------------------------

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function streamEnd(stream: fs.WriteStream): Promise<void> {
  return new Promise((resolve) => stream.end(() => resolve()));
}

async function runAttempt(): Promise<boolean> {
  const dumpWriteStream = fs.createWriteStream('dumper/dump');
  dumpWriteStream.write(steamInfContent);
  const modifierWriteStream = fs.createWriteStream('dumper/modifier_test_output.txt');

  console.log('Spawning Dota:', dotaExe, args.join(' '));
  const p1 = spawn(dotaExe, args, { cwd: dotaBinDir });

  let dotaExited = false;
  p1.on('error', (err) => console.error('Failed to spawn dota2.exe:', err));
  p1.on('exit', (code, signal) => {
    dotaExited = true;
    console.log(`dota2.exe exited with code=${code} signal=${signal}`);
  });

  const killDota = () => {
    if (dotaExited) return;
    // In -tools mode Dota spawns child processes; kill the whole tree so a
    // frozen instance can't linger and hold the vConsole port for the retry.
    try {
      if (p1.pid) spawn('taskkill', ['/F', '/T', '/PID', String(p1.pid)]);
    } catch {}
    try {
      p1.kill();
    } catch {}
  };

  try {
    await delay(STARTUP_DELAY_MS);

    let dotaConsole: Socket;
    try {
      dotaConsole = await vConsole.connect(CONNECT_PORT);
    } catch (err) {
      console.error('Could not connect to vConsole after launching Dota:', err);
      return false;
    }

    console.log('Connected! Waiting for dump...');

    let ok = false;
    try {
      ok = await readDump(dotaConsole, dumpWriteStream, modifierWriteStream, () => dotaExited);
    } catch (err) {
      console.error('Error while reading dump:', err);
      ok = false;
    }

    try {
      await vConsole.disconnect(dotaConsole);
    } catch {}

    return ok;
  } finally {
    await streamEnd(dumpWriteStream);
    await streamEnd(modifierWriteStream);
    killDota();
  }
}

async function readDump(
  dota: Socket,
  dumpStream: fs.WriteStream,
  modifierStream: fs.WriteStream,
  isDotaExited: () => boolean,
): Promise<boolean> {
  return new Promise((resolve) => {
    let dumpReading = false;
    let dumpDone = false;
    let modifierReading = false;
    let modifierDone = false;
    let settled = false;
    let sawAnyMessage = false;
    let messageCount = 0;
    let lastActivity = Date.now();
    let modifierGraceTimer: ReturnType<typeof setTimeout> | null = null;

    // Optional raw capture of every console message (set DUMP_DEBUG=1) for
    // diagnosing what Dota actually prints and in what order.
    const rawStream = process.env.DUMP_DEBUG ? fs.createWriteStream('dumper/console-raw.log') : null;

    const overall = setTimeout(() => {
      console.warn('Timed out waiting for ===ENDOFDUMP.');
      settle(dumpDone);
    }, DUMP_TIMEOUT_MS);

    const watchdog = setInterval(() => {
      if (isDotaExited() && !dumpDone) {
        console.warn('Dota exited before the dump completed.');
        settle(false);
        return;
      }

      const idleFor = Date.now() - lastActivity;
      if (idleFor > INACTIVITY_TIMEOUT_MS) {
        if (dumpDone) {
          console.warn('No further output after the dump — continuing without the modifier test.');
          settle(true);
        } else if (!sawAnyMessage) {
          console.warn('No console output at all — Dota appears frozen during load.');
          settle(false);
        } else {
          console.warn('Console output stalled before the dump completed — Dota appears frozen.');
          settle(false);
        }
      }
    }, 5000);

    const heartbeat = setInterval(() => {
      const stage = dumpDone ? 'waiting for modifier test' : 'capturing dump';
      console.log(
        `  …${stage}: ${messageCount} msgs, dump ${(dumpStream.bytesWritten / 1024).toFixed(0)} KB`,
      );
    }, HEARTBEAT_MS);

    function settle(ok: boolean) {
      if (settled) return;
      settled = true;
      clearTimeout(overall);
      clearInterval(watchdog);
      clearInterval(heartbeat);
      if (modifierGraceTimer) clearTimeout(modifierGraceTimer);
      if (rawStream) rawStream.end();
      resolve(ok);
    }

    function checkDone() {
      if (dumpDone && modifierDone) {
        console.log('Dump + modifier test complete.');
        settle(true);
      }
    }

    vConsole.onMessage(dota, (type, _channel, message) => {
      if (type !== 'PRNT') return;
      sawAnyMessage = true;
      messageCount++;
      lastActivity = Date.now();
      if (rawStream) rawStream.write(message);

      // Dump capture
      if (!dumpDone) {
        if (message.startsWith('$>')) {
          dumpReading = true;
        }
        if (message.startsWith('===ENDOFDUMP')) {
          dumpReading = false;
          dumpDone = true;
          console.log('Dump completed. Waiting for modifier test...');
          // The modifier test only runs once the game reaches GAME_IN_PROGRESS,
          // which can fail independently of the dump. Don't let it block forever:
          // proceed with the (essential) dump after a grace period.
          modifierGraceTimer = setTimeout(() => {
            if (!modifierDone) {
              console.warn('Modifier test did not finish in time — continuing without it.');
              modifierDone = true;
              settle(true);
            }
          }, MODIFIER_GRACE_MS);
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
    });
  });
}
