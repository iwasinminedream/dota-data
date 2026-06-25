local panoramaScopes = {
  "GameEvents",
  "CustomNetTables",
  "SteamUGC",
  "SteamFriends",
  "SteamUtils",
  "Buffs",
  "Players",
  "Entities",
  "Abilities",
  "Items",
  "Game",
  "GameUI",
  "Particles",
  "EventData",
  "LocalInventory",
  "$",
  "DOTAHeroModelOverlay",
  "DOTAPlay",
  "Panel",
  "Label",
  "ToggleButton",
  "TabButton",
  "DOTAMapUpdate2023Page",
  "DOTADashboard",
  "PageManager",
  "DOTAHomePage",
  "Movie",
  "DOTAAvatarImage",
  "CustomUIElement",
  "DOTAHudPreGame",
  "SteamUGCQuery",
  "SteamUGCMatchingUGCType",
  "SteamUniverse",
  "DOTA_GameState",
  "DOTA_GC_TEAM",
  "DOTA_GameMode",
  "DOTAConnectionState_t",
  "dotaunitorder_t",
  "DOTA_OVERHEAD_ALERT",
  "DOTA_HeroPickState",
  "DOTATeam_t",
  "DOTA_RUNES",
  "DOTA_UNIT_TARGET_TEAM",
  "DOTA_UNIT_TARGET_TYPE",
  "DOTA_UNIT_TARGET_FLAGS",
  "DOTALimits_t",
  "DOTAInventoryFlags_t",
  "EDOTA_ModifyGold_Reason",
  "DOTAUnitAttackCapability_t",
  "DOTAUnitMoveCapability_t",
  "EShareAbility",
  "DOTAMusicStatus_t",
  "DOTA_ABILITY_BEHAVIOR",
  "DAMAGE_TYPES",
  "ABILITY_TYPES",
  "SPELL_IMMUNITY_TYPES",
  "DOTADamageFlag_t",
  "EDOTA_ModifyXP_Reason",
  "GameActivity_t",
  "DOTAMinimapEvent_t",
  "DOTASlotType_t",
  "modifierfunction",
  "modifierstate",
  "DOTAModifierAttribute_t",
  "Attributes",
  "ParticleAttachment_t",
  "DOTA_MOTION_CONTROLLER_PRIORITY",
  "DOTASpeechType_t",
  "DOTAAbilitySpeakTrigger_t",
  "DotaCustomUIType_t",
  "DotaDefaultUIElement_t",
  "PlayerUltimateStateOrTime_t",
  "PlayerOrderIssuer_t",
  "OrderQueueBehavior_t",
  "CLICK_BEHAVIORS",
  "AbilityLearnResult_t",
  "DOTAKeybindCommand_t",
  "DOTA_SHOP_TYPE",
}

-- NOTE: `script_reload` reinitializes the server script VM and briefly disrupts
-- the vConsole output relay, so whatever is buffered when it fires is dropped.
-- A SECOND script_reload would be captured cleanly but a *warm* reload loses the
-- native argument type metadata (e.g. Vector turns into <unknown>). So we fire a
-- single script_reload and absorb the relay disruption with a verbose sacrificial
-- command before it (`cvarlist`, re-dumped for real later) instead. This keeps
-- the good types from the first/only reload AND captures its full output.
-- The panorama dump commands are listed AFTER the reload so the disruption can't
-- drop them either.
SCRIPT = [[
  clear
  echoln ===SACRIFICE
  cvarlist
  echoln $> script_reload
  script_reload
  echoln $> cl_script_reload
  cl_script_reload
  echoln $> dump_panorama_css_properties
  dump_panorama_css_properties
  echoln $> dump_panorama_events
  dump_panorama_events
  echoln $> cl_panorama_script_help *
  cl_panorama_script_help *
  echoln $> cl_dump_modifier_list
  cl_dump_modifier_list
  echoln $> cvarlist
  cvarlist
  echoln $> cl_panorama_typescript_declarations
]]

for _, scope in pairs(panoramaScopes) do
  SCRIPT = SCRIPT .. "\ncl_panorama_typescript_declarations " .. scope
end

SCRIPT = SCRIPT .. "\necholn ===ENDOFDUMP"

DUMP_TRIGGERED = false

function Activate()
  -- Launch straight into a match with a hero. This keeps the game fully
  -- simulating (entity thinks tick, panorama/game UI is loaded) and skips the
  -- custom-game setup stages. The dump is fired from OnGameRulesStateChange once
  -- the game is in progress — by then the external dumper has long since
  -- connected, so the whole dump (incl. the early panorama sections) is captured
  -- without the connect-vs-dump race. (The old freeze was a vconsole.mts framing
  -- bug, now fixed.)
  GameRules:SetCustomGameSetupAutoLaunchDelay(0)
  GameRules:SetCustomGameSetupTimeout(-1)
  GameRules:SetPreGameTime(6)
  GameRules:SetStrategyTime(0)
  GameRules:SetShowcaseTime(0)
  GameRules:GetGameModeEntity():SetCustomGameForceHero("npc_dota_hero_axe")

  ListenToGameEvent("game_rules_state_change", Dynamic_Wrap(GameMode, "OnGameRulesStateChange"), GameMode)

  Convars:RegisterCommand("dump_vscripts", function()
    if DUMP_TRIGGERED then return end
    DUMP_TRIGGERED = true
    SendToServerConsole(SCRIPT)
  end, "", 0)
end

GameMode = {}

function GameMode:OnGameRulesStateChange()
  if GameRules:State_Get() == DOTA_GAMERULES_STATE_GAME_IN_PROGRESS and not DUMP_TRIGGERED then
    -- Fire the dump first. Its script_reload initializes the console relay that
    -- carries server-side Lua print() to the external dumper — until that has
    -- happened, print() output (e.g. the modifier test) does not reach it.
    GameRules:GetGameModeEntity():SetContextThink("dump_fire", function()
      if DUMP_TRIGGERED then return nil end
      DUMP_TRIGGERED = true
      SendToServerConsole(SCRIPT)
      return nil
    end, 3)

    -- Then run the modifier-properties test, well after the dump has finished so
    -- its output (printed in a burst) lands cleanly after ===ENDOFDUMP and is not
    -- interleaved into the dump itself.
    GameRules:GetGameModeEntity():SetContextThink("modifier_test", function()
      local hHero = PlayerResource:GetSelectedHeroEntity(0)
      if hHero then
        hHero:AddNewModifier(hHero, nil, "modifier_test_properties", {})
      end
      return nil
    end, 25)
  end
end
