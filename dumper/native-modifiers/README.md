# Native modifiers

`extract.py` reads server.dll (the Windows server module; no game launch) and writes, for every native
(C++) modifier, the modifier functions it implements and, for every property, the value its handler
returns as a formula:

```
modifier_item_phase_boots_active
  MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE  (GetModifierMoveSpeedBonus_Percentage)
    state(parent, MODIFIER_STATE_ATTACKS_ARE_MELEE) ? %phase_movement_speed%
      : parent:IsRangedAttacker() ? %phase_movement_speed_range% : %phase_movement_speed%
modifier_lina_fiery_soul
  MODIFIER_PROPERTY_ATTACKSPEED_BONUS_CONSTANT  self:GetStackCount() * %fiery_soul_attack_speed_bonus%
```

It runs at the end of every successful `npm run auto-dump` (`dumper/native-modifiers.mts`) and alone as
`npm run dump:native-modifiers`; the result is `dumper/native_modifiers.json`, which
`npm run build:native-modifiers` (part of `npm run build`) checks against the dump, links to abilities and
copies to `files/vscripts/native_modifiers.json`. Requirements: Python 3 and capstone 5
(`pip install capstone`), nothing else. On Linux the Windows server.dll comes from `DOTA_SERVER_BINARY`
(the Wine depot); with only libserver.so the previous file is kept.

The same analysis runs on client.dll (`--dll client.dll`, next to server.dll or `DOTA_CLIENT_BINARY`) into
`dumper/native_modifiers_client.json`. The client has its own compiled copy of every modifier: the values
it predicts and shows in tooltips, without the creation parameters (`kv` exists only on the server) and
sometimes with logic the server does not need (or the other way round). `build:native-modifiers` merges it
in, see "Output". The client's CheckState is not used: states are the server's (networked); the client's
copy only predicts them.

## How it works

Everything is found in the binary itself, nothing is hard-coded per build (offsets included: the handler table
from the Lua modifier's declare loop, its size from `MODIFIER_FUNCTION_LAST`, the fields after it):

| What | How |
|---|---|
| modifier classes | MSVC RTTI: every class derived from `CDOTA_Buff`; the name is what `GetName` returns (the vtable slot whose overrides return a `modifier_*` constant: 9 in server.dll, 3 in client.dll) |
| declared functions | `DeclareFunctions` (the slot `CDOTA_Modifier_Lua` overrides with its declare loop) stores `{handler, this adjustment}` at `this + 0xE0 + 16 * P`; it is executed and the table read back |
| function names | `modifierfunction` / `modifierstate` name tables of the engine (`{name, value}` every 0x20 bytes); Lua handler names from `CDOTA_Modifier_Lua`'s switch from P to the Lua callback |
| handler results | the engine calls `handler(this, &result, &params)`; result: `+0` kind (1 number, 2 string), `+4` float, `+8` string |
| fields | every virtual function the class overrides (OnCreated, OnRefresh, OnIntervalThink, ...) and every handler is executed; its stores to the modifier's own fields are recorded |
| names of calls | the Lua bindings of the DLL (`script_api.py`, emulating the registration code; client.dll's `C_X` classes are matched as server.dll's `CX`): each method's native code is executed and what it returns becomes a template (`bit(ld(obj + 0xd18), 1)` is `obj:IsRangedAttacker()`, `ld(obj + 0x84)` on a modifier is `GetStackCount()`); virtual slots of abilities and modifiers are named after the Lua callbacks `CDOTA_Ability_Lua` / `CDOTA_Item_Lua` / `CDOTA_Modifier_Lua` forward them to |
| special values | the getters (float / int / bool) all start with the same level + lookup calls as the one `GetSpecialValueFor` uses |
| params | the function that converts the params struct to the Lua table (`report_max`, `original_damage`, ...): offset -> key |
| creation parameters | KeyValues imports (`FindKey`, `GetFloat`, ...) on the table passed to OnCreated / OnRefresh |
| modifier lookups | calls on an NPC's modifier manager (its offset from `FindModifierByName`) with a `modifier_*` string; in client.dll, calls of `C_DOTA_BaseNPC::FindModifierByName` (the function `HasModifier` calls) |
| client states | client.dll tests a state in the union of two masks (the server's and the predicted one): `(ld(npc + A) \| ld(npc + B))` bit k is read as state k (A, B from `IsRooted`) |
| states | `CheckState` (the slot `CDOTA_Modifier_Lua` forwards to `CheckState`) fills two 64-bit masks: `+0` the states it sets true, `+8` those it sets false (the Lua modifier turns `{[state] = true}` into `bts [+0]`, `btr [+8]`); every path is executed and each `MODIFIER_STATE_*` bit read back |

The executor (`symexec.py`) is symbolic: registers and memory hold expressions (`expr.py`), conditional
jumps fork the path, small functions are inlined (a call that cannot be followed is made opaque and the
path restarts from it), `__RTDynamicCast` is the identity. `render.py` joins the paths into one expression
(conditions that split them become `?:`), replaces fields by the values OnCreated / OnRefresh store,
names everything it can and prints it.

Assumptions (the formulas describe the normal case): entity handles are valid, pointers loaded from
memory are not null, casts succeed (`dynamic_cast` and the inlined "is it an NPC" class-byte checks),
a field that is zero in one place and set to one value elsewhere has that value.

## Formula syntax

| Text | Meaning |
|---|---|
| `%name%` | special value `name` of the modifier's ability (`GetSpecialValueFor`, current level) |
| `kv.name`, `kv.name or 5` | creation parameter `name` (the table of `AddNewModifier`), with the default used when it is missing |
| `self`, `caster`, `parent`, `ability` | the modifier, `GetCaster()`, `GetParent()`, `GetAbility()` |
| `obj:Method(args)` | a script method (`Time()` and other global functions without an object) |
| `state(obj, MODIFIER_STATE_X)` | obj currently has the modifier state |
| `params.name` | the params table of the modifier function (`params[0x14]`: a field Lua does not get) |
| `self.field_XXXX` | a field of the modifier the game changes over time; its writers are under `fields` |
| `?` | a part that could not be followed (status `partial`) |

Operators are Lua's (`~=`, `not`, `and`, `math.min`) plus `cond ? a : b`.

## Output

```jsonc
{
  "version": "6967",                       // ClientVersion of the game the DLL belongs to
  "modifiers": {
    "modifier_item_phase_boots_active": {
      "class": "CDOTA_Modifier_Item_PhaseBoots_Active",
      "bases": [],                         // C++ base classes between it and CDOTA_Buff
      "ability": "item_phase_boots",       // files/ only: the ability defining all its special values
      "functions": [
        {
          "function": "MODIFIER_PROPERTY_MOVESPEED_BONUS_PERCENTAGE",
          "handler": "GetModifierMoveSpeedBonus_Percentage",   // the Lua callback of that function
          "status": "formula",             // constant | formula | partial | unresolved | event
          "formula": "...",
          "specials": ["phase_movement_speed", "phase_movement_speed_range"],
          "kv": [],                        // creation parameters it reads
          "client": { "status": "formula", "formula": "...", "specials": [] }
                                           // files/ only: client.dll's result where it differs
        },
        { "function": "MODIFIER_EVENT_ON_DEATH", "status": "event", "side": "server" }
                                           // files/ only: declared by one DLL only
      ],
      "fields": { "field_1ab0": [{ "in": "OnIntervalThink", "value": "..." }] },
      "states": [                          // CheckState
        { "state": "MODIFIER_STATE_NO_UNIT_COLLISION", "value": true },
        { "state": "MODIFIER_STATE_DEBUFF_IMMUNE", "value": true, "when": "..." }
      ]
    }
  }
}
```

`states` lists every state the modifier sets: `value` true or false, `when` the condition when it is not
unconditional (a state can appear twice: true under one condition, false under another; `value: null` with
`when: "?"` marks paths the analysis could not follow; `states_unresolved: true` instead of the list when the
masks come from data it cannot read, e.g. the KV table of `modifier_datadriven`). `event` functions (`MODIFIER_EVENT_*`) are listed without a formula. `unresolved` has a `reason` (the
executor's: a loop, too many paths). When several abilities define all the special values (shared
values like `bonus_damage`), files/ has `abilities` instead of `ability`.

In files/ (merged by `build:native-modifiers`): `client` on a function is client.dll's result when its
status or formula differs from server.dll's (fields are compared by order of appearance: their offsets
differ between the DLLs); no `client` means the same result. Many differences are the analysis reaching
further in one DLL than in the other (a `?` on one side), or the same test written differently
(`parent:IsDebuffImmune()` is a virtual call in client.dll, `state(parent, ...)` in server.dll); the
real ones are values the client shows differently (a constant tooltip value, no `kv`). `side: "server"`
/ `"client"` marks a function or a whole modifier only one DLL has (client-only modifiers carry only
their functions). The changelog tracks client results as `modifier_function_client`.

## Working on it

`python extract.py --dll <server.dll | client.dll> --out <file>` runs everything (about two minutes for
server.dll, half a minute for client.dll). The modules can
be used one by one; `Renderer.unknown` / `Renderer.examples` count and show what made formulas partial,
which is the list to work from when a patch changes the code patterns.

# Table keys (`table_keys.py`)

The keys server.dll reads from (and writes to) the Lua tables VScript functions take: CreateIllusions'
`modifierKeys`, the options of `ApplyDamage`, `ExecuteOrderFromTable` and the projectiles, the `Trace*` tables,
the event tables of the `Set*Filter` callbacks, and so on. Static analysis of the Windows server.dll with the same
tooling (`pe.py`, `script_api.py`, `modifiers.py`, `x64emu.py`); about 35 s on 6986.

```
python3 -I dumper/native-modifiers/table_keys.py --dll server.dll [--out dumper/table_keys.json] [--version 6986]
                                                 [--debug]   # roots with RVAs, notes, call chains, untraced
npm run dump:table-keys                                      # the same, as the dumper runs it (dumper/table-keys.mts)
```

`dumper/table-keys.mts` runs it after every dump (`npm run auto-dump`); then `build/vscripts/table-keys.ts`
(part of `generateVScripts`) compares the result with the documented table types:

- `files/vscripts/table_keys.json`: every function with its keys, `access` (`read`: the engine reads it from the
  table; `write`: the engine puts it there, e.g. a filter event field), the engine code that does it (`sources`),
  `documented` against the argument's type, `documentedNotSeen`, and for filters `notReadBack` (documented as
  writable, but the engine does not read it back after the filter, so a change in Lua is ignored);
- `files/vscripts/api-types.json`: a key a type lacks is added to it, `types: ['unknown']` and a description
  saying where it was found, so a key a new build starts reading shows up in the types and in the changelog at
  once. Describe it in `build/vscripts/api-types/index.ts` and the description there takes its place. Not added:
  nested keys, keys of the entity spawn tables (`SpawnEntityFromTable*`, `CreateUnitFromTable`: the whole table
  becomes the entity's keyvalues), keys the engine itself writes into an option table (bookkeeping such as
  `creationtime`), and keys only the generic modifier creation reads (AddNewModifier's own keys);
- the changelog category **Lua Table Keys** (one item per function and key; its read/write is the signature).

## How it works

1. **Roots**: every binding of `script_classes()` with a direct implementation (2287 functions in 91 classes on
   6986), plus extra roots where a table is read outside the binding: `CDOTA_Modifier_Illusion::OnCreated` /
   `OnRefresh` and the C++ AddNewModifier for CreateIllusions (the KeyValues reach the illusion modifier through
   the spawn key `illusionKeyValues`), and for every `Set*Filter` the functions that invoke the filter (they pass
   the field the setter stores the function into to the shared filter runner, which turns the event KeyValues
   into a table, calls Lua and reads the table back).
2. **Data flow** per function (capstone, basic blocks, registers and stack slots): string literals, `g_pScriptVM`
   and its slots, the arguments, `new KeyValues`, call results, the `GetValue` out-variant (nested tables), struct
   fields, HKeySymbols. Callees to depth 3, summarised in terms of their arguments and substituted at each call.
3. **What is recorded**: virtual calls on the script VM with a literal key (`getvalue` / `setvalue`; the slots are
   calibrated from the code: GetValue is the slot whose out-variant is passed to ReleaseValue afterwards), the
   KeyValues imports with a literal key (`kv_get`: `Get*`, `FindKey`, also through cached HKeySymbols; `kv_set`:
   `Set*`, `Add*`, `FindKey(create)`), and keys compared while the table is iterated (`iter_cmp`).
4. **Tracing**: a finding counts only when its object goes back to the Lua table (the argument, a nested table read
   from it, or KeyValues filled from it); everything else is `_untraced` and is written only with `--debug`
   (it depends on inlining and would come and go between builds).
5. **Check**: if the VM slots cannot be calibrated, or keys every working analysis finds are missing (`ANCHORS`:
   ApplyDamage's victim/attacker/damage/damage_type, CreateIllusions' outgoing/incoming_damage and bounty_base,
   the damage filter's `damage`, TraceLine's startpos/endpos), it exits 3 without output and the previous file is
   kept, instead of a changelog that removes every key and adds them back with the next build.

KeyValues compare keys without case (`illusionLabel` = `illusionlabel`). The output has no addresses: the same
analysis of the same DLL gives the same file (checked with different `PYTHONHASHSEED` and environments).

**Known limits.** Keys read through objects the analysis does not model (heap fields, globals, `GetPtr`, virtual
calls it cannot resolve) are missed or untraced: `fullhp` of CreateIllusions is read by the spawn code behind
`illusionKeyValues` and is not seen. Keys built at run time and `GetFirstSubKey` loops are invisible. Engine
→ Lua tables that are not filter events (modifier event parameters, return values) are not covered.

**Found with it on 6986**: `illusion_effectiveness` of CreateIllusions (a float `modifier_illusion` keeps;
default 20), and the filter fields `level` (AbilityTuningValue) and `shop_item_name` (ExecuteOrder), which are not
read back; it also confirms that TraceCollideable reads `min`/`max` and TraceHull does not read `mask`.
