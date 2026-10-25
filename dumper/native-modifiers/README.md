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

## How it works

Everything is found in the binary itself, nothing is hard-coded per build (offsets included: the handler table
from the Lua modifier's declare loop, its size from `MODIFIER_FUNCTION_LAST`, the fields after it):

| What | How |
|---|---|
| modifier classes | MSVC RTTI: every class derived from `CDOTA_Buff`; the name is what `GetName` (vtable slot 9) returns |
| declared functions | `DeclareFunctions` (the slot `CDOTA_Modifier_Lua` overrides with its declare loop) stores `{handler, this adjustment}` at `this + 0xE0 + 16 * P`; it is executed and the table read back |
| function names | `modifierfunction` / `modifierstate` name tables of the engine (`{name, value}` every 0x20 bytes); Lua handler names from `CDOTA_Modifier_Lua`'s switch from P to the Lua callback |
| handler results | the engine calls `handler(this, &result, &params)`; result: `+0` kind (1 number, 2 string), `+4` float, `+8` string |
| fields | every virtual function the class overrides (OnCreated, OnRefresh, OnIntervalThink, ...) and every handler is executed; its stores to the modifier's own fields are recorded |
| names of calls | the Lua bindings of server.dll (`script_api.py`, emulating the registration code): each method's native code is executed and what it returns becomes a template (`bit(ld(obj + 0xd18), 1)` is `obj:IsRangedAttacker()`, `ld(obj + 0x84)` on a modifier is `GetStackCount()`); virtual slots of abilities and modifiers are named after the Lua callbacks `CDOTA_Ability_Lua` / `CDOTA_Item_Lua` / `CDOTA_Modifier_Lua` forward them to |
| special values | the getters (float / int / bool) all start with the same level + lookup calls as the one `GetSpecialValueFor` uses |
| params | the function that converts the params struct to the Lua table (`report_max`, `original_damage`, ...): offset -> key |
| creation parameters | KeyValues imports (`FindKey`, `GetFloat`, ...) on the table passed to OnCreated / OnRefresh |
| modifier lookups | calls on an NPC's modifier manager (its offset from `FindModifierByName`) with a `modifier_*` string |
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
          "kv": []                         // creation parameters it reads
        }
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
`when: "?"` marks paths the analysis could not follow). `event` functions (`MODIFIER_EVENT_*`) are listed without a formula. `unresolved` has a `reason` (the
executor's: a loop, too many paths). When several abilities define all the special values (shared
values like `bonus_damage`), files/ has `abilities` instead of `ability`.

## Working on it

`python extract.py --dll <server.dll> --out <file>` runs everything (about two minutes). The modules can
be used one by one; `Renderer.unknown` / `Renderer.examples` count and show what made formulas partial,
which is the list to work from when a patch changes the code patterns.
