# Automatic dumps on a Linux server

Everything here runs on the Linux server that hosts the Dota 2 dedicated servers (a steamcmd install,
no GPU, no Steam client). When the installed Dota build changes it:

1. snapshots the build's `.so` files (`so-report.py snapshot`, store: `/var/lib/dota-data/so/<ClientVersion>-<SourceRevision>/`, last 3 kept);
2. runs `npm run auto-dump` (once more when the dumper reports that the modifier function list
   changed): with the Windows client and Workshop Tools under Wine after refreshing its depots with
   steamcmd — only when Steam's public build is the installed one — and with the Linux client if
   that is not possible or fails (see "Capturing on Linux" in `CLAUDE.md`). A new build is the
   ClientVersion, or the Steam buildid (`/var/lib/dota-data/dumped-build`) for a rebuild of the same
   version; such a rebuild is committed only if it changes something in `files/`;
3. dumps the same build a second time and compares the raw dumps (`dump-diff.py`): the game did not
   change in between, so any difference is dumper noise. It is written to
   `dump-checks/<version>.md` and noted in the commit message; the first dump is the one committed;
4. `npm run build` and `test/files_match_dump.spec.ts` (the schema tests download fixtures that
   no longer exist upstream and fail regardless);
5. commits `<version>`; the commit body says which client dumped and how the control dump went;
6. writes the update report `reports/<version>.md` (`update-report.py`, commit `report: <version>`)
   and pushes to `origin/master`. The report has a summary (Haiku draft, checked by Opus) of the API changes
   (`files/changelogs/<version>.json`, minus what the control dump marked as noise) and of the
   `.so` changes against the previous snapshot (sizes, code size, exports, strings from the
   read-only data and protobuf descriptors) and function by function (`funcdiff.py`, below), plus
   tables computed without the model. The whole function-level comparison, with the code diff of
   every changed function, goes to `reports/<version>-functions.md`. The report is written in
   Russian; `translate-report.py` (Claude Sonnet 5.5) adds the English `reports/<version>.en.md`
   (commit `report: <version> (English)`), which the site shows when its reader picks English.

## Function-level comparison

`funcdiff.py OLD.so NEW.so` finds what changed in the code of a stripped library even when no
string or export did (a balance change, a new condition): it splits `.text` into functions
(capstone linear sweep, cut at the int3 padding and at the `.eh_frame` / data-pointer entry points),
normalises each one so that recompiling at other addresses changes nothing (a string reference
becomes the string, a value loaded from read-only data becomes the value — the float constants of
game logic —, other addresses become placeholders) and pairs the functions of the two builds
(unique identical code as anchors, then order, strings, names and size). Names come from RTTI:
`Class::vfunc#N` for vtable slot N, and `Class::OnSpellStart` when the slot is one that
`CDOTA_Ability_Lua` / `CDOTA_Item_Lua` / `CDOTA_Modifier_Lua` forward to the Lua callback of that
name (callback names from `files/vscripts/api.json`). For each changed function: strings and
constants added / removed, virtual calls, object fields, call count, and the normalised code diff.
A library's function table is cached in `<snapshot>/funcs/<lib>.json.gz` (about a minute and
4–6 GB of memory per big library to build). Needs `pip install capstone` (5.x).

## The models

Both run through the `claude` CLI with the server's Claude Code subscription login
(`ANTHROPIC_API_KEY` in the env file would make the same CLI use the API instead), without a
spending cap, in `/var/lib/dota-data/analysis/<version>/`:

1. **Claude Haiku 4.5 — the bulk pass.** The whole changelog, the whole `.so` diff and every changed
   function, uncapped, are cut into chunks (by API category / library and string group / function,
   `REPORT_CHUNK_CHARS`, 60k
   characters) and each chunk gets a detailed digest with the exact names (`REPORT_DRAFT_WORKERS`,
   3 in parallel, no tools). `chunks/` and `digests/` stay in the workspace.
2. **Claude Opus 5.5 — the check.** It reads every digest, verifies each claim that goes into the
   report against the raw data, fixes and completes them and writes the report, ending with what it
   corrected in Haiku's draft (`--effort high`). Every new property, event and method is also looked
   up in the game code (the installed build's `libserver.so` / `libclient.so`: where its name is
   used, the strings around, the disassembly) and in localization / KV, and the report explains what
   it does, with the evidence and how sure that is. It is a read-only agent: `--tools "Read Grep Glob
   Bash"`, `--permission-mode dontAsk`, the only allowed shell command `automation/so-query.py`
   (strings, exported symbols, code referencing a string, the strings that code uses, disassembly,
   and per function: the changed list, a whole diff, a function's code with strings and constants
   resolved, its callers and callees, a class's vtable — of the installed build's snapshot and the
   one before only), file access limited to the workspace, this repo and the snapshots. Anything
   else (other commands, files elsewhere, writes) is refused without asking. Each changed function
   gets explained in the report: whose it is, what changed, what that means in the game.

Models and effort: `REPORT_DRAFT_MODEL`, `REPORT_FINAL_MODEL`, `REPORT_FINAL_EFFORT`.

`dota-data-sync.sh --check` dumps the installed build once more and compares it with the committed
dump without committing anything (report in `/var/lib/dota-data/checks/`): a quick way to see how
reliable the dumper is right now. `DOTA_DATA_CONTROL_DUMP=0` turns the control dump off.

## Pieces

| file | what |
| --- | --- |
| `dota-data-sync.sh` | the whole run; idempotent, safe to start any time (`--force` re-dumps, `--check` compares) |
| `dump-diff.py` | section-by-section comparison of two raw dumps |
| `so-report.py` | `snapshot`, `list`, `report OLD NEW` (a .so-only report by hand) |
| `update-report.py` | `VERSION --out reports/VERSION.md`: the update report |
| `translate-report.py` | `reports/VERSION.md`: its English version `reports/VERSION.en.md`, checked against the original |
| `funcdiff.py` | `OLD.so NEW.so`: function-level comparison of two builds of a library |
| `so-query.py` | the read-only queries the model may run on the snapshots |
| `systemd/dota-data-sync.service` | runs `dota-data-sync.sh` (nice, idle IO, CPU 400 %, memory 12 G) |
| `systemd/dota-data-sync.path` | starts it when `game/dota/steam.inf` changes (panel «Обновить доту» or a manual steamcmd) |
| `systemd/dota-data-sync.timer` | hourly fallback: snapshots the installed build, retries a failed push |

On this server Dota updates itself: `/root/dota-custom/dota-auto-update.sh` (`dota-auto-update.timer`,
every 5 minutes) asks Steam anonymously for the public build and runs the panel's `dota-update.sh
update` when it differs (lobbies stopped, steamcmd, Metamod plugin check — its result shows in the
panel, not in these reports — lobbies back up); the new `steam.inf` then starts this sync. If Dota
changes while a sync runs, the run discards what it dumped and starts over for the new build.

`dota-data-sync.sh` waits until the update has settled (no live `/run/dota-update.active` marker, no
`steamcmd` process, `StateFlags 4` in `appmanifest_570.acf`). A version whose dump failed is retried
after 6 hours (`/var/lib/dota-data/failed-<version>`), or at once with `--force`. A dirty worktree or a
branch that diverged from `origin/master` stops it without touching anything.

## Server setup

- `/root/dota-data-runtime/dumper.env` — environment for the dumper and the commit author (`DOTA2_DIR`, `DUMPER_LAUNCH`
  pointing at `dumper/linux/headless-launch.sh`, overlay dir, Xvfb display, Steam Runtime entry point,
  the lavapipe `fakegpu` Vulkan layer in `/root/dota-data-runtime/fakegpu`, `DOTA_DATA_GIT_NAME/EMAIL`,
  and for the Wine mode `DOTA_DATA_STEAM_LOGIN`, `DUMPER_WINE_LAUNCH`, `DUMPER_WINE_GAME_DIR`,
  `DUMPER_WIN_DEPOTS`, `DUMPER_STEAMWORKS`, `DUMPER_WIN_SERVER_DLL`, `WINEPREFIX`, `DUMPER_LANGUAGE`).
  Packages: wine (64-bit), gcc-mingw-w64-x86-64, xvfb, mesa-vulkan-drivers, binutils; Python:
  `pip install capstone`.
- Push: a deploy key with write access, `/root/.ssh/dota-data-deploy`, used by this clone through
  `core.sshCommand`, push URL `git@github.com:iwasinminedream/dota-data.git`.
- Units: `cp automation/systemd/* /etc/systemd/system/ && systemctl daemon-reload &&
  systemctl enable --now dota-data-sync.path dota-data-sync.timer`.

Logs: `journalctl -u dota-data-sync`; the client output of the last dump is `dumper/linux/client.log`
and its console log `/var/lib/dota-data/dumper/upper/dota/console.log`.
