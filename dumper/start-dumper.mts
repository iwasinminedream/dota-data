/*
 * Utility script that automatically starts dota with the dumper addon.
 * npm run auto-dump
 *
 * Windows: dota2.exe -tools, output read over vConsole (port 29000).
 * Linux: the Linux client (no Workshop Tools there) with dumper/linux/dumper_hook.so preloaded,
 * output read from its -condebug console.log; or, with DUMPER_WINE_LAUNCH, the Windows client and
 * Workshop Tools under Wine, which works like Windows (vConsole). See dumper/linux/ and the Linux
 * section of CLAUDE.md.
 */
import { execSync, spawn, spawnSync, ChildProcess } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

// CommonJS module (build/ is not ESM): named imports are not visible from .mts.
import dotaDir from '../build/util/dota-dir';
import { reportBaselineChange, syncModifierBaseline } from './modifier-baseline.mts';
import { extractNativeModifiers, installedVersion } from './native-modifiers.mts';
import { extractInterfaces, parseLayoutXsd, PanelInfo } from './panels.mts';
import * as vConsole from './vconsole.mts';
import { carryForward } from './linux/carry-forward.mts';
import { followConsoleLog } from './linux/console-log.mts';
import { hookEnvironment } from './linux/hook.mts';
import { killWine, readWineClipboard } from './linux/wine.mts';

const ADDON_NAME = 'dumper';
const IS_LINUX = process.platform === 'linux';
// Windows client with -tools under Wine: Windows behaviour (vConsole, a full -tools dump), started
// and stopped the Linux way.
const IS_WINE = IS_LINUX && !!process.env.DUMPER_WINE_LAUNCH;
// The Linux client: hook, console.log, cfg-driven panel phase, carry-forward.
const LINUX_CLIENT = IS_LINUX && !IS_WINE;

const dota2Dir = await dotaDir.findDota2Dir();
console.log(`Found DotA 2 installation: ${dota2Dir}`);

// Where the client sees its game directory for writing: the install itself, or the upper dir of an
// overlay when a launcher keeps the install untouched (dumper/linux/headless-launch.sh).
const gameDir = process.env.DUMPER_GAME_DIR || path.join(dota2Dir, 'game');

console.log('Copying dumper addon...');

const addonPath = path.join(gameDir, 'dota_addons', ADDON_NAME);
const vscriptsPath = path.join(addonPath, 'scripts', 'vscripts');
fs.mkdirSync(vscriptsPath, { recursive: true });
fs.copyFileSync(
  path.join('dumper', 'addon_game_mode.lua'),
  path.join(vscriptsPath, 'addon_game_mode.lua'),
);
fs.copyFileSync(path.join('dumper', 'addon_init.lua'), path.join(vscriptsPath, 'addon_init.lua'));
fs.copyFileSync(
  path.join('dumper', 'modifier_test_properties.lua'),
  path.join(vscriptsPath, 'modifier_test_properties.lua'),
);

// Custom-game UI that instantiates known panel types, so their JS classes are
// registered by the time the panel declarations phase runs (the engine only
// has cl_panorama_typescript_declarations data for instantiated types).
// dumper/panorama/compiled keeps the resourcecompiler output, refreshed by every Windows run and
// used as-is on Linux, which has no resource compiler.
const COMPILED_UI: [file: string, dir: string][] = [
  ['custom_ui_manifest.vxml_c', path.join('layout', 'custom_game')],
  ['dumper_panels.vxml_c', path.join('layout', 'custom_game')],
  ['dumper_panels.vjs_c', path.join('scripts', 'custom_game')],
];
const compiledUiDir = path.join('dumper', 'panorama', 'compiled');
const addonPanoramaPath = path.join(addonPath, 'panorama');

if (IS_LINUX) {
  for (const [file, dir] of COMPILED_UI) {
    fs.mkdirSync(path.join(addonPanoramaPath, dir), { recursive: true });
    fs.copyFileSync(path.join(compiledUiDir, file), path.join(addonPanoramaPath, dir, file));
  }
  const compiledJs = resourceDataBlock(path.join(compiledUiDir, 'dumper_panels.vjs_c'));
  const sourceJs = fs.readFileSync(path.join('dumper', 'panorama', 'dumper_panels.js'));
  if (!compiledJs || !compiledJs.equals(sourceJs)) {
    console.warn(
      'dumper/panorama/compiled is older than dumper/panorama/dumper_panels.js — run the dumper ' +
        'once on Windows to recompile it. Using the old compiled UI.',
    );
  }
} else {
  const contentPanoramaPath = path.join(dota2Dir, 'content', 'dota_addons', ADDON_NAME, 'panorama');
  const contentLayoutPath = path.join(contentPanoramaPath, 'layout', 'custom_game');
  const contentScriptsPath = path.join(contentPanoramaPath, 'scripts', 'custom_game');
  fs.mkdirSync(contentLayoutPath, { recursive: true });
  fs.mkdirSync(contentScriptsPath, { recursive: true });
  for (const layoutFile of ['custom_ui_manifest.xml', 'dumper_panels.xml']) {
    fs.copyFileSync(
      path.join('dumper', 'panorama', layoutFile),
      path.join(contentLayoutPath, layoutFile),
    );
  }
  fs.copyFileSync(
    path.join('dumper', 'panorama', 'dumper_panels.js'),
    path.join(contentScriptsPath, 'dumper_panels.js'),
  );

  // The -tools launch does not compile the custom UI on its own, so compile it
  // explicitly (compiling the manifest also compiles the layout and script it
  // references). If this fails, the dump still works — the panel phase just
  // captures fewer per-type interfaces.
  try {
    execSync(
      `"${path.join(dota2Dir, 'game', 'bin', 'win64', 'resourcecompiler.exe')}" -i "${path.join(
        contentLayoutPath,
        'custom_ui_manifest.xml',
      )}"`,
      { stdio: 'ignore' },
    );
    console.log('Compiled dumper custom-game UI.');
    for (const [file, dir] of COMPILED_UI) {
      fs.copyFileSync(path.join(addonPanoramaPath, dir, file), path.join(compiledUiDir, file));
    }
  } catch (err) {
    console.warn('Failed to compile the dumper custom-game UI:', err);
  }
}

console.log('Starting dumper...');

const steamInfPath = path.join(dota2Dir, 'game', 'dota', 'steam.inf');
const steamInfContent = fs.readFileSync(steamInfPath);

// --- Tunables -------------------------------------------------------------
// The Linux client renders in software at 1-3 fps: loading takes minutes and
// game time runs ~5x slower than real time, so every wait is longer there.
const CONNECT_PORT = 29000;
const STARTUP_DELAY_MS = 5000; // give Dota a moment before connecting to vConsole
const DUMP_TIMEOUT_MS = (IS_LINUX ? 40 : 8) * 60 * 1000; // hard cap from launch to the end of all phases
const INACTIVITY_TIMEOUT_MS = (IS_LINUX ? 300 : 120) * 1000; // no console output this long => Dota frozen
// (must exceed the gap between connecting and the match reaching GAME_IN_PROGRESS,
// when the dump fires — otherwise a slow load looks like a freeze)
const MODIFIER_GRACE_MS = (IS_LINUX ? 480 : 45) * 1000; // after the dump, wait this long for the modifier test
// (the modifier test runs 25 game seconds into the match; this is the upper
// bound the dumper waits before finishing on the dump alone)
const PANELS_INACTIVITY_MS = (IS_LINUX ? 120 : 60) * 1000; // no output during the panel phase => keep partial capture
const HEARTBEAT_MS = (IS_LINUX ? 30 : 10) * 1000;
const MAX_ATTEMPTS = 3;
const LINUX_PANEL_CHUNK = 100; // commands per cfg file (one exec of all of them overflows the buffer)
const LINUX_PANEL_SLOTS = 64; // chunk cfg files created before launch (see consoleLogSource)

// Linux client files: console log and panel phase cfgs in its game dir, the clipboard text in a
// temp dir the Steam Runtime container shares with the host.
const linuxCfgDir = path.join(gameDir, 'dota', 'cfg');
const linuxConsoleLog = path.join(gameDir, 'dota', 'console.log');
const linuxTmpDir = path.join(process.env.DUMPER_TMP_DIR || '/tmp', `dota-dumper-${process.pid}`);
const linuxClipboardFile = path.join(linuxTmpDir, 'clipboard.xsd');
const LINUX_MARKER = '-dumper_client';

// The panel phase cfgs exist (empty) before the client starts and are only ever rewritten in
// place: with an overlay launcher the client caches "no such file" for a name it looked up, and
// does not see a file replaced by rename, when the upper dir is changed from outside the mount.
const linuxPanelCfgs = [
  'dumper_panels.cfg',
  ...Array.from({ length: LINUX_PANEL_SLOTS }, (_, i) => `dumper_panels_${i}.cfg`),
];

// The script_reload relay disruption can silently drop a whole section from the
// capture (the sacrificial cvarlist usually absorbs it, but not always), so a
// "successful" attempt still has to prove every expected section actually landed.
const DUMP_FILE = 'dumper/dump';
const MODIFIER_FILE = 'dumper/modifier_test_output.txt';
// Attempts write here; the real files are only replaced by a complete dump.
const DUMP_PARTIAL = `${DUMP_FILE}.partial`;
const MODIFIER_PARTIAL = `${MODIFIER_FILE}.partial`;

const REQUIRED_SECTIONS = [
  'script_reload',
  'cl_script_reload',
  'dump_panorama_css_properties',
  'dump_panorama_events',
  'cl_panorama_script_help *',
  'cl_dump_modifier_list',
  'panorama_generate_layout_xsd',
  'cvarlist',
  'cl_panorama_typescript_declarations',
  'panorama_panels',
  // On Windows the panel phase may fail without failing the dump; the unattended Linux run retries.
  ...(IS_LINUX ? ['panel_typescript_declarations'] : []),
];

function findMissingSections(): string[] {
  const content = fs.readFileSync(DUMP_PARTIAL, 'utf8');
  return REQUIRED_SECTIONS.filter((section) => !content.includes(`$> ${section}`));
}

function removePartials() {
  fs.rmSync(DUMP_PARTIAL, { force: true });
  fs.rmSync(MODIFIER_PARTIAL, { force: true });
}

// On Linux the previous dump is the source of what a retail client cannot dump (see
// dumper/linux/carry-forward.mts).
const previousDump = fs.readFileSync(DUMP_FILE, 'utf8');

// Killing the dumper must not leave a headless client running (it holds ~2 cores and several GB).
let runningLinuxClient: ChildProcess | null = null;
for (const signal of ['SIGINT', 'SIGTERM', 'SIGHUP'] as const) {
  process.on(signal, () => {
    if (runningLinuxClient) killLinuxClient(runningLinuxClient);
    if (IS_WINE) killWine();
    if (IS_LINUX) fs.rmSync(linuxTmpDir, { recursive: true, force: true });
    removePartials();
    process.exit(128 + (signal === 'SIGINT' ? 2 : signal === 'SIGTERM' ? 15 : 1));
  });
}

let succeeded = false;
for (let attempt = 1; attempt <= MAX_ATTEMPTS && !succeeded; attempt++) {
  console.log(`\n=== Dump attempt ${attempt}/${MAX_ATTEMPTS} ===`);
  succeeded = await runAttempt();
  if (succeeded) {
    const missing = findMissingSections();
    if (missing.length > 0) {
      console.warn(`Dump is missing sections: ${missing.join(', ')}`);
      succeeded = false;
    }
  }
  if (!succeeded && attempt < MAX_ATTEMPTS) {
    console.warn('Attempt did not produce a complete dump — retrying with a fresh Dota launch...');
    await delay(3000);
  }
}

if (!succeeded) {
  console.error(`Failed to capture a complete dump after ${MAX_ATTEMPTS} attempts.`);
  removePartials();
  process.exit(1);
}

if (LINUX_CLIENT) {
  const { dump, report } = carryForward(fs.readFileSync(DUMP_PARTIAL, 'utf8'), previousDump);
  fs.writeFileSync(DUMP_PARTIAL, dump);
  console.log(
    `Carried over from the previous dump: ${report.convars} tools-only convars, ` +
      `${report.typedMembers} declaration lines with argument types.`,
  );
}
fs.renameSync(DUMP_PARTIAL, DUMP_FILE);
fs.renameSync(MODIFIER_PARTIAL, MODIFIER_FILE);

console.log('\nSaved dump + modifier test — dumper finished successfully.');

// Modifier functions and property formulas of the native modifiers (static analysis of server.dll).
extractNativeModifiers(dota2Dir, installedVersion(dota2Dir));

// Fold this dump's modifier state back into the dumper, and say so at the very end
// if the modifier function list itself changed in this Dota build.
reportBaselineChange(syncModifierBaseline());

process.exit(0);

// --------------------------------------------------------------------------

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function streamEnd(stream: fs.WriteStream): Promise<void> {
  return new Promise((resolve) => stream.end(() => resolve()));
}

/** DATA block of a compiled resource (for .vjs_c it is the JavaScript source). */
function resourceDataBlock(file: string): Buffer | null {
  const data = fs.readFileSync(file);
  const blockOffset = data.readUInt32LE(8);
  const blockCount = data.readUInt32LE(12);
  for (let i = 0, pos = 8 + blockOffset; i < blockCount; i++, pos += 12) {
    if (data.toString('latin1', pos, pos + 4) !== 'DATA') continue;
    const start = pos + 4 + data.readUInt32LE(pos + 4);
    return data.subarray(start, start + data.readUInt32LE(pos + 8));
  }
  return null;
}

/** Where the client's output comes from and how the panel phase commands reach it. */
interface DumpSource {
  onMessage(cb: (message: string) => void): void;
  runPanelCommands(commands: string[]): Promise<void>;
  close(): Promise<void>;
}

function vConsoleSource(socket: import('net').Socket): DumpSource {
  return {
    onMessage(cb) {
      vConsole.onMessage(socket, (type, _channel, message) => {
        if (type === 'PRNT') cb(message);
      });
    },
    async runPanelCommands(commands) {
      for (const [index, command] of commands.entries()) {
        await vConsole.execute(socket, command);
        // Give the console queue room to drain between bursts.
        if (index % 50 === 49) await delay(50);
      }
    },
    async close() {
      await vConsole.disconnect(socket);
    },
  };
}

// --- Linux client -----------------------------------------------------------

function resetLinuxPanelCfgs() {
  fs.mkdirSync(linuxCfgDir, { recursive: true });
  for (const file of linuxPanelCfgs) fs.writeFileSync(path.join(linuxCfgDir, file), '');
}

function consoleLogSource(): DumpSource {
  let follower: ReturnType<typeof followConsoleLog> | null = null;
  return {
    onMessage(cb) {
      follower = followConsoleLog(linuxConsoleLog, 0, (_channel, message) => cb(message));
    },
    // The addon execs cfg/dumper_panels.cfg until it exists, then one chunk per think
    // (addon_game_mode.lua); the last chunk ends with the ===ENDOFPANELS marker.
    async runPanelCommands(commands) {
      const size = Math.max(LINUX_PANEL_CHUNK, Math.ceil(commands.length / LINUX_PANEL_SLOTS));
      const chunks: string[][] = [];
      for (let i = 0; i < commands.length; i += size) chunks.push(commands.slice(i, i + size));
      chunks.forEach((chunk, i) =>
        fs.writeFileSync(path.join(linuxCfgDir, `dumper_panels_${i}.cfg`), `${chunk.join('\n')}\n`),
      );
      fs.writeFileSync(
        path.join(linuxCfgDir, 'dumper_panels.cfg'),
        `dumper_panels_begin ${chunks.length}\n`,
      );
    },
    async close() {
      follower?.stop();
      resetLinuxPanelCfgs();
    },
  };
}

function spawnLinuxClient(): ChildProcess {
  const launcher = process.env.DUMPER_LAUNCH || path.join(dota2Dir, 'game', 'dota.sh');
  const args = [
    LINUX_MARKER,
    '-novid',
    '-nosound',
    '-console',
    '-condebug',
    '-addon',
    ADDON_NAME,
    '+sv_cheats',
    '1',
    '+dota_launch_custom_game',
    ADDON_NAME,
    'dota',
  ];

  // A client orphaned by an earlier killed run would collide with this one.
  spawnSync('pkill', ['-9', '-f', `linuxsteamrt64/dota2 .*${LINUX_MARKER}`]);
  fs.rmSync(linuxTmpDir, { recursive: true, force: true });
  fs.mkdirSync(linuxTmpDir, { recursive: true });
  resetLinuxPanelCfgs();
  fs.mkdirSync(path.dirname(linuxConsoleLog), { recursive: true });
  fs.writeFileSync(linuxConsoleLog, '');

  const clientLog = fs.openSync(path.join('dumper', 'linux', 'client.log'), 'w');
  console.log('Spawning Dota:', launcher, args.join(' '));
  return spawn(launcher, args, {
    cwd: path.dirname(launcher),
    env: { ...process.env, ...hookEnvironment(dota2Dir, linuxClipboardFile) },
    detached: true,
    stdio: ['ignore', clientLog, clientLog],
  });
}

function spawnWineClient(): ChildProcess {
  const launcher = process.env.DUMPER_WINE_LAUNCH!;
  // Same arguments as on Windows; the launcher adds -vulkan.
  const args = [
    LINUX_MARKER,
    '-novid',
    '-tools',
    '-condebug',
    '-console',
    '-addon',
    ADDON_NAME,
    `+dota_launch_custom_game ${ADDON_NAME} dota`,
  ];
  killWine();
  spawnSync('pkill', ['-9', '-f', `dota2\\.exe .*${LINUX_MARKER}`]);
  fs.rmSync(linuxTmpDir, { recursive: true, force: true });
  fs.mkdirSync(linuxTmpDir, { recursive: true });

  const clientLog = fs.openSync(path.join('dumper', 'linux', 'client.log'), 'w');
  console.log('Spawning Dota (Wine):', launcher, args.join(' '));
  return spawn(launcher, args, {
    cwd: path.dirname(launcher),
    env: process.env,
    detached: true,
    stdio: ['ignore', clientLog, clientLog],
  });
}

/** vConsole opens once the Windows client has loaded under Wine, which takes a while. */
async function connectVConsole(deadline: number): Promise<import('net').Socket> {
  for (;;) {
    try {
      return await vConsole.connect(CONNECT_PORT);
    } catch (err) {
      if (Date.now() > deadline) throw err;
    }
  }
}

function killLinuxClient(p: ChildProcess) {
  try {
    if (p.pid) process.kill(-p.pid, 'SIGKILL');
  } catch {}
  // The Steam Runtime container may move the game out of our process group.
  spawnSync('pkill', ['-9', '-f', `linuxsteamrt64/dota2 .*${LINUX_MARKER}`]);
}

// --------------------------------------------------------------------------

async function runAttempt(): Promise<boolean> {
  const attemptStartTime = Date.now();
  const dumpWriteStream = fs.createWriteStream(DUMP_PARTIAL);
  dumpWriteStream.write(steamInfContent);
  const modifierWriteStream = fs.createWriteStream(MODIFIER_PARTIAL);

  let p1: ChildProcess;
  if (LINUX_CLIENT) {
    p1 = spawnLinuxClient();
    runningLinuxClient = p1;
  } else if (IS_WINE) {
    p1 = spawnWineClient();
    runningLinuxClient = p1;
  } else {
    const dotaBinDir = path.join(dota2Dir, 'game', 'bin', 'win64');
    const dotaExe = path.join(dotaBinDir, 'dota2.exe');
    const args = [
      '-novid',
      '-tools',
      '-addon',
      ADDON_NAME,
      `+dota_launch_custom_game ${ADDON_NAME} dota`,
    ];
    console.log('Spawning Dota:', dotaExe, args.join(' '));
    p1 = spawn(dotaExe, args, { cwd: dotaBinDir });
  }

  let dotaExited = false;
  p1.on('error', (err) => console.error('Failed to spawn Dota:', err));
  p1.on('exit', (code, signal) => {
    dotaExited = true;
    console.log(`Dota exited with code=${code} signal=${signal}`);
  });

  const killDota = () => {
    if (IS_LINUX) {
      killLinuxClient(p1);
      if (IS_WINE) killWine();
      return;
    }
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

  let source: DumpSource | null = null;
  try {
    if (LINUX_CLIENT) {
      source = consoleLogSource();
      console.log(`Following ${linuxConsoleLog}...`);
    } else {
      await delay(STARTUP_DELAY_MS);
      try {
        source = vConsoleSource(
          IS_WINE
            ? await connectVConsole(Date.now() + 10 * 60 * 1000)
            : await vConsole.connect(CONNECT_PORT),
        );
      } catch (err) {
        console.error('Could not connect to vConsole after launching Dota:', err);
        return false;
      }
      console.log('Connected! Waiting for dump...');
    }

    let ok = false;
    try {
      ok = await readDump(
        source,
        dumpWriteStream,
        modifierWriteStream,
        () => dotaExited,
        attemptStartTime,
      );
    } catch (err) {
      console.error('Error while reading dump:', err);
      ok = false;
    }
    return ok;
  } finally {
    try {
      await source?.close();
    } catch {}
    await streamEnd(dumpWriteStream);
    await streamEnd(modifierWriteStream);
    killDota();
    if (IS_LINUX) fs.rmSync(linuxTmpDir, { recursive: true, force: true });
  }
}

// panorama_generate_layout_xsd prints "Layout XSD contents copied to clipboard."
// — the schema itself never reaches the console, so read it back via PowerShell
// (on Linux dumper_hook.so writes the clipboard text to a file instead, and under Wine
// dumper/linux/getclip.c reads the Wine clipboard).
function readClipboardXsd(): string | null {
  try {
    const clip = IS_WINE
      ? readWineClipboard(linuxClipboardFile) ?? ''
      : IS_LINUX
      ? fs.readFileSync(linuxClipboardFile, 'utf8')
      : execSync('powershell -NoProfile -Command "Get-Clipboard -Raw"', {
          maxBuffer: 256 * 1024 * 1024,
        }).toString('utf8');
    return clip.includes('<xs:schema') ? clip : null;
  } catch {
    return null;
  }
}

// panorama_generate_layout_xsd may write its result to disk instead of the
// console; pick up any .xsd created after this attempt started.
function findFreshXsdFile(attemptStartTime: number): string | null {
  const found: { file: string; mtime: number }[] = [];
  const walk = (dir: string) => {
    let entries: fs.Dirent[];
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      const entryPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(entryPath);
      } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.xsd')) {
        try {
          const stat = fs.statSync(entryPath);
          if (stat.mtimeMs >= attemptStartTime)
            found.push({ file: entryPath, mtime: stat.mtimeMs });
        } catch {}
      }
    }
  };
  walk(gameDir);
  walk(path.join(dota2Dir, 'content'));
  found.sort((a, b) => b.mtime - a.mtime);
  return found.length > 0 ? found[0].file : null;
}

async function readDump(
  source: DumpSource,
  dumpStream: fs.WriteStream,
  modifierStream: fs.WriteStream,
  isDotaExited: () => boolean,
  attemptStartTime: number,
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
    let currentSection: string | null = null;
    let xsdText = '';
    let panelsStarted = false;
    let panelsCapturing = false;
    let panelsDone = false;
    let panelData: PanelInfo[] = [];
    const panelsBuffer: string[] = [];

    // Optional raw capture of every console message (set DUMP_DEBUG=1) for
    // diagnosing what Dota actually prints and in what order.
    const rawStream = process.env.DUMP_DEBUG
      ? fs.createWriteStream('dumper/console-raw.log')
      : null;

    const overall = setTimeout(() => {
      console.warn('Timed out waiting for the dump to complete.');
      if (dumpDone && panelsStarted && !panelsDone) {
        finishPanels();
      } else {
        settle(dumpDone);
      }
    }, DUMP_TIMEOUT_MS);

    const watchdog = setInterval(() => {
      if (isDotaExited()) {
        if (!dumpDone) {
          console.warn('Dota exited before the dump completed.');
          settle(false);
        } else {
          console.warn('Dota exited before the panel phase completed — keeping what was captured.');
          finishPanels();
          settle(true);
        }
        return;
      }

      const idleFor = Date.now() - lastActivity;
      if (panelsStarted && !panelsDone) {
        if (idleFor > PANELS_INACTIVITY_MS) {
          console.warn('Panel declarations phase stalled — keeping what was captured.');
          finishPanels();
        }
        return;
      }
      if (idleFor > INACTIVITY_TIMEOUT_MS) {
        if (dumpDone) {
          console.warn('No further output after the dump — continuing without the modifier test.');
          void startPanelsPhase();
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
      const stage = panelsStarted
        ? 'capturing panel declarations'
        : dumpDone
        ? 'waiting for modifier test'
        : 'capturing dump';
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
        void startPanelsPhase();
      }
    }

    async function startPanelsPhase() {
      if (panelsStarted || settled) return;
      panelsStarted = true;
      if (modifierGraceTimer) clearTimeout(modifierGraceTimer);

      try {
        let xsd = xsdText.includes('<xs:schema') ? xsdText : null;
        if (!xsd) xsd = readClipboardXsd();
        if (!xsd) {
          const xsdFile = findFreshXsdFile(attemptStartTime);
          if (xsdFile) {
            console.log(`Found generated layout XSD on disk: ${xsdFile}`);
            xsd = fs.readFileSync(xsdFile, 'utf8');
          }
        }

        panelData = xsd ? parseLayoutXsd(xsd) : [];
        if (panelData.length === 0) {
          console.warn('Could not obtain the layout XSD — skipping the panel phase.');
          settle(true);
          return;
        }

        // The raw XSD is ~22 MB of boilerplate (every type repeats all inherited
        // attributes), so the dump stores this compact digest instead.
        dumpStream.write(`\n$> panorama_panels\n${JSON.stringify(panelData, null, 2)}\n`);

        console.log(`Found ${panelData.length} panel types, dumping TypeScript declarations...`);
        panelsCapturing = true;
        lastActivity = Date.now();
        await source.runPanelCommands([
          ...panelData.map((panel) => `cl_panorama_typescript_declarations ${panel.name}`),
          'echoln ===ENDOFPANELS',
        ]);
      } catch (err) {
        console.warn('Panel declarations phase failed:', err);
        settle(dumpDone);
      }
    }

    function finishPanels() {
      if (panelsDone || settled) return;
      panelsDone = true;

      const captured = extractInterfaces(panelsBuffer.join(''));
      const baseOf = new Map(panelData.map((p) => [p.name, p.base]));
      const kept: string[] = [];
      let droppedCount = 0;
      for (const [name, body] of captured) {
        // A type whose flattened JS interface is identical to its nearest captured
        // ancestor's adds nothing — its script API is fully inherited.
        let ancestor = baseOf.get(name);
        while (ancestor && !captured.has(ancestor)) ancestor = baseOf.get(ancestor);
        if (ancestor && captured.get(ancestor)!.join('\n') === body.join('\n')) {
          droppedCount++;
          continue;
        }
        kept.push(`interface ${name}\n{\n${body.map((line) => `    ${line}`).join('\n')}\n}`);
      }

      if (kept.length > 0) {
        dumpStream.write(`\n$> panel_typescript_declarations\n${kept.join('\n')}\n`);
      }
      console.log(
        `Panel declarations captured: ${kept.length} unique interfaces (${droppedCount} fully inherited).`,
      );
      settle(true);
    }

    source.onMessage((message) => {
      // The Linux addon's "exec dumper_panels" polling is not a sign of progress.
      if (message.startsWith("exec: couldn't exec")) return;
      // The tools' stall monitor fires when the main thread is slow (Wine, software rendering) and
      // its message would land in the middle of a section (e.g. inside the script_reload JSON).
      if (message.trim() === 'Stall detected.') return;
      sawAnyMessage = true;
      messageCount++;
      lastActivity = Date.now();
      if (rawStream) rawStream.write(message);

      // Panel declarations capture (phase 2, after dump + modifier test)
      if (panelsCapturing && !panelsDone) {
        if (message.startsWith('===ENDOFPANELS')) {
          finishPanels();
        } else {
          panelsBuffer.push(message);
        }
        return;
      }

      // Dump capture
      if (!dumpDone) {
        if (message.startsWith('$>')) {
          dumpReading = true;
          currentSection = message.slice(2).trim();
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
              void startPanelsPhase();
            }
          }, MODIFIER_GRACE_MS);
          checkDone();
        } else if (dumpReading) {
          dumpStream.write(message);
          if (currentSection === 'panorama_generate_layout_xsd') {
            xsdText += message;
          }
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
