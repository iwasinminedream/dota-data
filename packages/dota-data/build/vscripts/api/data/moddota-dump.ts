import { array, ExtensionFunction, func } from './utils';

export const moddotaDump: Record<string, ExtensionFunction> = {
  'CBaseEntity.FirstMoveChild': { returns: 'CBaseEntity' },
  'CBaseEntity.FollowEntity': { args: { '0': [null, 'CBaseEntity'] } },
  'CBaseEntity.GetMoveParent': { returns: 'CBaseEntity' },
  'CBaseEntity.GetOwner': { returns: 'CBaseEntity' },
  'CBaseEntity.GetOwnerEntity': { returns: 'CBaseEntity' },
  'CBaseEntity.GetRootMoveParent': { returns: 'CBaseEntity' },
  'CBaseEntity.GetTeam': { returns: 'DotaTeam' },
  'CBaseEntity.GetTeamNumber': { returns: 'DotaTeam' },
  'CBaseEntity.NextMovePeer': { returns: 'CBaseEntity' },
  'CBaseEntity.SetOwner': { args: { '0': [null, 'CBaseEntity'] } },
  'CBaseEntity.SetTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CBaseTrigger.IsTouching': { args: { '0': [null, 'CBaseEntity'] } },
  'CCustomGameEventManager.RegisterListener': {
    returns: 'CustomGameEventListenerID',
    args: { '1': ['listener', func([['userId', 'number'], ['event', 'table']], 'nil')] },
  },
  'CCustomGameEventManager.Send_ServerToAllClients': { args: { '1': [null, 'table'] } },
  'CCustomGameEventManager.Send_ServerToPlayer': {
    args: { '0': [null, 'CDOTAPlayer'], '2': [null, 'table'] },
  },
  'CCustomGameEventManager.Send_ServerToTeam': {
    args: { '0': ['team', 'DotaTeam'], '2': [null, 'table'] },
  },
  'CCustomGameEventManager.UnregisterListener': {
    args: { '0': ['listener', 'CustomGameEventListenerID'] },
  },
  'CDOTABaseAbility.CanAbilityBeUpgraded': { returns: 'bool' },
  'CDOTABaseAbility.GetAbilityDamageType': { returns: 'DamageTypes' },
  'CDOTABaseAbility.GetAbilityKeyValues': {},
  'CDOTABaseAbility.GetAbilityTargetFlags': { returns: 'UnitTargetFlags' },
  'CDOTABaseAbility.GetAbilityTargetTeam': { returns: 'UnitTargetTeam' },
  'CDOTABaseAbility.GetAbilityTargetType': { returns: 'UnitTargetType' },
  'CDOTABaseAbility.GetCastRange': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTABaseAbility.GetCaster': { returns: 'CDOTA_BaseNPC' },
  'CDOTABaseAbility.GetCloneSource': { returns: 'CDOTA_BaseNPC' },
  'CDOTABaseAbility.GetCursorTarget': { returns: 'CDOTA_BaseNPC' },
  'CDOTABaseAbility.IsCosmetic': { args: { '0': [null, 'CBaseEntity'] } },
  'CDOTABaseGameMode.GetCustomAttributeDerivedStatValue': {
    args: { '0': [null, 'AttributeDerivedStat'] },
  },
  'CDOTABaseGameMode.SetCustomAttributeDerivedStatValue': {
    args: { '0': [null, 'AttributeDerivedStat'] },
  },
  'CDOTABaseGameMode.SetCustomHeroMaxLevel': { args: { '0': ['maxLevel'] } },
  'CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel': { args: { '0': [null, 'table'] } },
  'CDOTABaseGameMode.SetHUDVisible': { args: { '0': [null, 'HudVisibility'] } },
  'CDOTABaseGameMode.SetOverrideSelectionEntity': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTABaseGameMode.SetRuneEnabled': { args: { '0': [null, 'RuneType'] } },
  'CDOTABaseGameMode.SetTopBarTeamValue': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTAGamerules.BeginNightstalkerNight': { args: { '0': ['duration'] } },
  'CDOTAGamerules.BeginTemporaryNight': { args: { '0': ['duration'] } },
  'CDOTAGamerules.EnableCustomGameSetupAutoLaunch': { args: { '0': ['enabled'] } },
  'CDOTAGamerules.GetCustomGameTeamMaxPlayers': { args: { '0': ['team', 'DotaTeam'] } },
  'CDOTAGamerules.GetDOTATime': { args: { '0': ['includePreGame'], '1': ['includeNegativeTime'] } },
  'CDOTAGamerules.GetDroppedItem': { returns: 'CDOTA_Item', args: { '0': ['index'] } },
  'CDOTAGamerules.GetGameModeEntity': { returns: 'CDOTABaseGameMode' },
  'CDOTAGamerules.LockCustomGameSetupTeamAssignment': { args: { '0': ['locked'] } },
  'CDOTAGamerules.MakeTeamLose': { args: { '0': ['team', 'DotaTeam'] } },
  'CDOTAGamerules.PlayerHasCustomGameHostPrivileges': { args: { '0': ['player', 'CDOTAPlayer'] } },
  'CDOTAGamerules.SetCreepMinimapIconScale': { args: { '0': ['scale'] } },
  'CDOTAGamerules.SetCustomGameAllowBattleMusic': { args: { '0': ['allow'] } },
  'CDOTAGamerules.SetCustomGameAllowHeroPickMusic': { args: { '0': ['allow'] } },
  'CDOTAGamerules.SetCustomGameAllowMusicAtGameStart': { args: { '0': ['allow'] } },
  'CDOTAGamerules.SetCustomGameDifficulty': { args: { '0': ['difficulty'] } },
  'CDOTAGamerules.SetCustomGameEndDelay': { args: { '0': ['delay'] } },
  'CDOTAGamerules.SetCustomGameSetupAutoLaunchDelay': { args: { '0': ['delay'] } },
  'CDOTAGamerules.SetCustomGameSetupRemainingTime': { args: { '0': ['remainingTime'] } },
  'CDOTAGamerules.SetCustomGameSetupTimeout': { args: { '0': ['timeout'] } },
  'CDOTAGamerules.SetCustomGameTeamMaxPlayers': {
    args: { '0': ['team', 'DotaTeam'], '1': ['maxPlayers'] },
  },
  'CDOTAGamerules.SetCustomVictoryMessage': { args: { '0': ['message'] } },
  'CDOTAGamerules.SetCustomVictoryMessageDuration': { args: { '0': ['duration'] } },
  'CDOTAGamerules.SetFirstBloodActive': { args: { '0': ['active'] } },
  'CDOTAGamerules.SetGameWinner': { args: { '0': ['team', 'DotaTeam'] } },
  'CDOTAGamerules.SetGoldPerTick': { args: { '0': ['amount'] } },
  'CDOTAGamerules.SetGoldTickTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetHeroMinimapIconScale': { args: { '0': ['scale'] } },
  'CDOTAGamerules.SetHeroRespawnEnabled': { args: { '0': ['enabled'] } },
  'CDOTAGamerules.SetHeroSelectionTime': { args: { '0': ['selectionTime'] } },
  'CDOTAGamerules.SetHideKillMessageHeaders': { args: { '0': ['hideHeaders'] } },
  'CDOTAGamerules.SetOverlayHealthBarUnit': {
    args: { '0': ['unit', 'CDOTA_BaseNPC'], '1': ['style'] },
  },
  'CDOTAGamerules.SetPostGameTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetPreGameTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetRuneSpawnTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetSameHeroSelectionEnabled': { args: { '0': ['enabled'] } },
  'CDOTAGamerules.SetShowcaseTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetStartingGold': { args: { '0': ['amount'] } },
  'CDOTAGamerules.SetStrategyTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetTimeOfDay': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetTreeRegrowTime': { args: { '0': ['time'] } },
  'CDOTAGamerules.SetUseBaseGoldBountyOnHeroes': { args: { '0': ['useBaseGoldBounties'] } },
  'CDOTAGamerules.SetUseCustomHeroXPValues': { args: { '0': ['useCustomXPValues'] } },
  'CDOTAGamerules.SetUseUniversalShopMode': { args: { '0': ['useUniversalShopMode'] } },
  'CDOTAGamerules.State_Get': { returns: 'GameState' },
  'CDOTAPlayer.GetAssignedHero': { returns: 'CDOTA_BaseNPC_Hero' },
  'CDOTAPlayer.SetKillCamUnit': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTATutorial.AddBot': { args: { '0': ['heroName'] } },
  'CDOTATutorial.AddShopWhitelistItem': { args: { '0': ['itemName'] } },
  'CDOTATutorial.IsItemInWhiteList': { args: { '0': ['itemName'] } },
  'CDOTATutorial.RemoveShopWhitelistItem': { args: { '0': ['itemName'] } },
  'CDOTATutorial.SelectHero': { args: { '0': ['heroName'] } },
  'CDOTATutorial.SetOrModifyPlayerGold': { args: { '0': ['goldAmount'], '1': ['setNotModify'] } },
  'CDOTATutorial.SetQuickBuy': { args: { '0': ['itemName'] } },
  'CDOTATutorial.SetShopOpen': { args: { '0': ['open'] } },
  'CDOTATutorial.SetTimeFrozen': { args: { '0': ['timeFrozen'] } },
  'CDOTATutorial.SetWhiteListEnabled': { args: { '0': ['whitelistEnabled'] } },
  'CDOTATutorial.UpgradePlayerAbility': { args: { '0': ['abilityName'] } },
  'CDOTA_Ability_Lua.CastFilterResult': { returns: 'UnitFilterResult' },
  'CDOTA_Ability_Lua.CastFilterResultLocation': { returns: 'UnitFilterResult' },
  'CDOTA_Ability_Lua.CastFilterResultTarget': {
    returns: 'UnitFilterResult',
    args: { '0': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_Ability_Lua.GetBehavior': { returns: 'AbilityBehavior' },
  'CDOTA_Ability_Lua.GetCastAnimation': { returns: 'GameActivity' },
  'CDOTA_Ability_Lua.GetCastRange': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Ability_Lua.GetChannelAnimation': { returns: 'GameActivity' },
  'CDOTA_Ability_Lua.GetCustomCastErrorTarget': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Ability_Lua.OnHeroDiedNearby': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '1': [null, 'CDOTA_BaseNPC'], '2': ['event', 'table'] },
  },
  'CDOTA_Ability_Lua.OnItemEquipped': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_Ability_Lua.OnProjectileHit': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Ability_Lua.OnProjectileHitHandle': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '2': [null, 'ProjectileID'] },
  },
  'CDOTA_Ability_Lua.OnProjectileHit_ExtraData': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '2': ['data', 'table'] },
  },
  'CDOTA_Ability_Lua.OnProjectileThinkHandle': { args: { '0': [null, 'ProjectileID'] } },
  'CDOTA_Ability_Lua.OnProjectileThink_ExtraData': { args: { '1': ['data', 'table'] } },
  'CDOTA_Ability_Lua.OnStolen': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.AddAbility': { returns: 'CDOTABaseAbility' },
  'CDOTA_BaseNPC.AddItem': { returns: 'CDOTA_Item', args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.AddItemByName': { returns: 'CDOTA_Item' },
  'CDOTA_BaseNPC.AddNewModifier': {
    returns: 'CDOTA_Buff',
    args: {
      '0': [null, ['CDOTA_BaseNPC', 'nil']],
      '1': [null, ['CDOTABaseAbility', 'nil']],
      '2': ['modifierName'],
      '3': [null, ['table', 'nil']],
    },
  },
  'CDOTA_BaseNPC.AlertNearbyUnits': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '1': [null, 'CDOTABaseAbility'] },
  },
  'CDOTA_BaseNPC.CanEntityBeSeenByMyTeam': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.CastAbilityImmediately': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.CastAbilityNoTarget': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.CastAbilityOnPosition': { args: { '1': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.CastAbilityOnTarget': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '1': [null, 'CDOTABaseAbility'] },
  },
  'CDOTA_BaseNPC.CastAbilityToggle': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.DisassembleItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.DropItemAtPosition': { args: { '1': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.DropItemAtPositionImmediate': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.EjectItemFromStash': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.FadeGesture': { args: { '0': [null, 'GameActivity'] } },
  'CDOTA_BaseNPC.FindAbilityByName': { returns: 'CDOTABaseAbility' },
  'CDOTA_BaseNPC.FindAllModifiers': { returns: array('CDOTA_Buff') },
  'CDOTA_BaseNPC.FindAllModifiersByName': {
    returns: array('CDOTA_Buff'),
    args: { '0': ['modifierName'] },
  },
  'CDOTA_BaseNPC.FindItemInInventory': { returns: 'CDOTA_Item' },
  'CDOTA_BaseNPC.FindModifierByName': { returns: 'CDOTA_Buff', args: { '0': ['modifierName'] } },
  'CDOTA_BaseNPC.FindModifierByNameAndCaster': {
    returns: 'CDOTA_Buff',
    args: { '0': ['modifierName'], '1': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_BaseNPC.ForcePlayActivityOnce': { args: { '0': [null, 'GameActivity'] } },
  'CDOTA_BaseNPC.GetAbilityByIndex': { returns: 'CDOTABaseAbility' },
  'CDOTA_BaseNPC.GetAggroTarget': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_BaseNPC.GetAttackCapability': { returns: 'UnitAttackCapability' },
  'CDOTA_BaseNPC.GetAttackTarget': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_BaseNPC.GetAverageTrueAttackDamage': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.GetCloneSource': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_BaseNPC.GetCurrentActiveAbility': { returns: 'CDOTABaseAbility' },
  'CDOTA_BaseNPC.GetCursorCastTarget': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_BaseNPC.GetForceAttackTarget': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_BaseNPC.GetInitialGoalEntity': { returns: 'CBaseEntity' },
  'CDOTA_BaseNPC.GetItemInSlot': { returns: 'CDOTA_Item', args: { '0': ['slot'] } },
  'CDOTA_BaseNPC.GetModifierStackCount': {
    args: { '0': ['modifierName'], '1': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_BaseNPC.GetOpposingTeamNumber': { returns: 'DotaTeam' },
  'CDOTA_BaseNPC.GetPlayerOwner': { returns: 'CDOTAPlayer' },
  'CDOTA_BaseNPC.GetPlayerOwnerID': { returns: 'PlayerID' },
  'CDOTA_BaseNPC.GetRangeToUnit': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.Heal': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.IsAttackingEntity': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.IsOpposingTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_BaseNPC.Kill': { args: { '0': [null, 'CDOTABaseAbility'], '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.MakeVisibleDueToAttack': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_BaseNPC.MakeVisibleToTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_BaseNPC.ModifyHealth': { args: { '1': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.MoveToNPC': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.MoveToNPCToGiveItem': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '1': [null, 'CDOTA_Item'] },
  },
  'CDOTA_BaseNPC.MoveToTargetToAttack': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.PerformAttack': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.PickupDroppedItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.PickupRune': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.RemoveGesture': { args: { '0': [null, 'GameActivity'] } },
  'CDOTA_BaseNPC.RemoveHorizontalMotionController': { args: { '0': [null, 'CDOTA_Buff'] } },
  'CDOTA_BaseNPC.RemoveItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.RemoveModifierByNameAndCaster': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.RemoveVerticalMotionController': { args: { '0': [null, 'CDOTA_Buff'] } },
  'CDOTA_BaseNPC.SellItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.SetAbilityByIndex': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.SetAggroTarget': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.SetAttackCapability': { args: { '0': [null, 'UnitAttackCapability'] } },
  'CDOTA_BaseNPC.SetAttacking': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.SetCursorCastTarget': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.SetForceAttackTarget': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.SetInitialGoalEntity': { args: { '0': [null, 'CBaseEntity'] } },
  'CDOTA_BaseNPC.SetModifierStackCount': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_BaseNPC.SetMoveCapability': { args: { '0': [null, 'UnitMoveCapability'] } },
  'CDOTA_BaseNPC.SpendMana': { args: { '1': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.StartGesture': { args: { '0': [null, 'GameActivity'] } },
  'CDOTA_BaseNPC.StartGestureWithPlaybackRate': { args: { '0': [null, 'GameActivity'] } },
  'CDOTA_BaseNPC.TakeItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_BaseNPC.TriggerSpellAbsorb': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC.TriggerSpellReflect': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_BaseNPC_Creature.AddItemDrop': { args: { '0': [null, 'table'] } },
  'CDOTA_BaseNPC_Hero.GetAdditionalOwnedUnits': { returns: array('CDOTA_BaseNPC') },
  'CDOTA_BaseNPC_Hero.GetPlayerID': { returns: 'PlayerID' },
  'CDOTA_BaseNPC_Hero.GetPrimaryAttribute': { returns: 'Attribute', description: '' },
  'CDOTA_BaseNPC_Hero.GetTogglableWearable': { returns: 'CBaseEntity' },
  'CDOTA_BaseNPC_Hero.SetPrimaryAttribute': { args: { '0': [null, 'Attribute'] } },
  'CDOTA_BaseNPC_Hero.UpgradeAbility': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_Buff.GetAbility': { returns: 'CDOTABaseAbility' },
  'CDOTA_Buff.GetCaster': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_Buff.GetParent': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_Item.GetContainer': { returns: 'CDOTA_Item_Physical' },
  'CDOTA_Item.GetPurchaser': { returns: 'CDOTA_BaseNPC' },
  'CDOTA_Item.GetShareability': { returns: 'ItemShareability' },
  'CDOTA_Item.SetPurchaser': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Item.SetShareability': { args: { '0': [null, 'ItemShareability'] } },
  'CDOTA_Item_Lua.CastFilterResult': { returns: 'UnitFilterResult' },
  'CDOTA_Item_Lua.CastFilterResultLocation': { returns: 'UnitFilterResult' },
  'CDOTA_Item_Lua.CastFilterResultTarget': {
    returns: 'UnitFilterResult',
    args: { '0': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_Item_Lua.GetBehavior': { returns: 'AbilityBehavior' },
  'CDOTA_Item_Lua.GetCastRange': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Item_Lua.GetCustomCastErrorTarget': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Item_Lua.OnHeroDiedNearby': {
    args: { '0': [null, 'CDOTA_BaseNPC'], '1': [null, 'CDOTA_BaseNPC'], '2': ['event', 'table'] },
  },
  'CDOTA_Item_Lua.OnItemEquipped': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_Item_Lua.OnProjectileHit': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Item_Lua.OnStolen': { args: { '0': [null, 'CDOTABaseAbility'] } },
  'CDOTA_Item_Physical.GetContainedItem': { returns: 'CDOTA_Item' },
  'CDOTA_Item_Physical.SetContainedItem': { args: { '0': [null, 'CDOTA_Item'] } },
  'CDOTA_MapTree.CutDown': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_MapTree.CutDownRegrowAfter': { args: { '1': [null, 'DotaTeam'] } },
  'CDOTA_Modifier_Lua.GetAttributes': { returns: 'ModifierAttribute' },
  'CDOTA_Modifier_Lua.GetAuraEntityReject': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Modifier_Lua.GetAuraSearchFlags': { returns: 'UnitTargetFlags' },
  'CDOTA_Modifier_Lua.GetAuraSearchTeam': { returns: 'UnitTargetTeam' },
  'CDOTA_Modifier_Lua.GetAuraSearchType': { returns: 'UnitTargetType' },
  'CDOTA_Modifier_Lua.GetEffectAttachType': { returns: 'ParticleAttachment' },
  'CDOTA_Modifier_Lua.GetPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua.HeroEffectPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua.OnCreated': { args: { '0': ['params', 'table'] } },
  'CDOTA_Modifier_Lua.OnRefresh': { args: { '0': ['params', 'table'] } },
  'CDOTA_Modifier_Lua.StatusEffectPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua_Horizontal_Motion.GetPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua_Horizontal_Motion.SetPriority': { args: { '0': [null, 'ModifierPriority'] } },
  'CDOTA_Modifier_Lua_Horizontal_Motion.UpdateHorizontalMotion': {
    args: { '0': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_Modifier_Lua_Motion_Both.GetPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua_Motion_Both.SetPriority': { args: { '0': [null, 'ModifierPriority'] } },
  'CDOTA_Modifier_Lua_Motion_Both.UpdateHorizontalMotion': {
    args: { '0': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_Modifier_Lua_Motion_Both.UpdateVerticalMotion': { args: { '0': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_Modifier_Lua_Vertical_Motion.GetMotionPriority': { returns: 'ModifierPriority' },
  'CDOTA_Modifier_Lua_Vertical_Motion.SetMotionPriority': {
    args: { '0': [null, 'ModifierPriority'] },
  },
  'CDOTA_Modifier_Lua_Vertical_Motion.UpdateVerticalMotion': {
    args: { '0': [null, 'CDOTA_BaseNPC'] },
  },
  'CDOTA_PlayerResource.GetConnectionState': { returns: 'ConnectionState' },
  'CDOTA_PlayerResource.GetNthCourierForTeam': {
    returns: 'CDOTA_Unit_Courier',
    args: { '1': [null, 'DotaTeam'] },
  },
  'CDOTA_PlayerResource.GetNthPlayerIDOnTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_PlayerResource.GetNumCouriersForTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_PlayerResource.GetPlayerCountForTeam': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_PlayerResource.GetKillsDoneToHero': { args: { '1': [null, 'PlayerID'] } },
  'CDOTA_PlayerResource.GetSelectedHeroEntity': { returns: 'CDOTA_BaseNPC_Hero' },
  'CDOTA_PlayerResource.GetTeam': { returns: 'DotaTeam' },
  'CDOTA_PlayerResource.GetTeamKills': { args: { '0': [null, 'DotaTeam'] } },
  'CDOTA_PlayerResource.IncrementAssists': { args: { '1': [null, 'PlayerID'] } },
  'CDOTA_PlayerResource.IncrementDeaths': { args: { '1': [null, 'PlayerID'] } },
  'CDOTA_PlayerResource.IncrementKills': { args: { '1': [null, 'PlayerID'] } },
  'CDOTA_PlayerResource.IncrementTotalEarnedXP': { args: { '2': [null, 'ModifyXpReason'] } },
  'CDOTA_PlayerResource.ModifyGold': { args: { '3': [null, 'ModifyGoldReason'] } },
  'CDOTA_PlayerResource.SetCameraTarget': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_PlayerResource.SetCustomTeamAssignment': { args: { '1': [null, 'DotaTeam'] } },
  'CDOTA_PlayerResource.SetOverrideSelectionEntity': { args: { '1': [null, 'CDOTA_BaseNPC'] } },
  'CDOTA_PlayerResource.SpendGold': { args: { '2': [null, 'ModifyGoldReason'] } },
  'CDOTA_PlayerResource.UpdateTeamSlot': { args: { '1': [null, 'DotaTeam'] } },
  'CEntities.CreateByClassname': { returns: 'CBaseEntity', args: { '0': ['className'] } },
  'CEntities.FindAllByClassname': { returns: array('CBaseEntity'), args: { '0': ['className'] } },
  'CEntities.FindAllByClassnameWithin': {
    returns: array('CBaseEntity'),
    args: { '0': ['className'], '1': ['location'], '2': ['radius'] },
  },
  'CEntities.FindAllByModel': { returns: array('CBaseEntity'), args: { '0': ['modelName'] } },
  'CEntities.FindAllByName': { returns: array('CBaseEntity'), args: { '0': ['name'] } },
  'CEntities.FindAllByNameWithin': {
    returns: array('CBaseEntity'),
    args: { '0': ['name'], '1': ['location'], '2': ['radius'] },
  },
  'CEntities.FindAllByTarget': { returns: array('CBaseEntity'), args: { '0': ['target'] } },
  'CEntities.FindAllInSphere': {
    returns: array('CBaseEntity'),
    args: { '0': ['location'], '1': ['radius'] },
  },
  'CEntities.FindByClassname': {
    returns: 'CBaseEntity',
    args: { '0': ['previous', ['CBaseEntity', 'nil']], '1': ['className'] },
  },
  'CEntities.FindByClassnameNearest': {
    returns: 'CBaseEntity',
    args: { '0': ['className'], '1': ['location'], '2': ['radius'] },
  },
  'CEntities.FindByClassnameWithin': {
    returns: 'CBaseEntity',
    args: {
      '0': ['previous', ['CBaseEntity', 'nil']],
      '1': ['className'],
      '2': ['location'],
      '3': ['radius'],
    },
  },
  'CEntities.FindByModel': {
    returns: 'CBaseEntity',
    args: { '0': ['previous', ['CBaseEntity', 'nil']], '1': ['modelName'] },
  },
  'CEntities.FindByModelWithin': {
    returns: 'CBaseEntity',
    args: {
      '0': ['previous', ['CBaseEntity', 'nil']],
      '1': ['modelName'],
      '2': ['location'],
      '3': ['radius'],
    },
  },
  'CEntities.FindByName': {
    returns: 'CBaseEntity',
    args: { '0': ['previous', ['CBaseEntity', 'nil']], '1': ['name'] },
  },
  'CEntities.FindByNameNearest': {
    returns: 'CBaseEntity',
    args: { '0': ['name'], '1': ['location'], '2': ['radius'] },
  },
  'CEntities.FindByNameWithin': {
    returns: 'CBaseEntity',
    args: {
      '0': ['previous', ['CBaseEntity', 'nil']],
      '1': ['name'],
      '2': ['location'],
      '3': ['radius'],
    },
  },
  'CEntities.FindByTarget': {
    returns: 'CBaseEntity',
    args: { '0': ['previous', ['CBaseEntity', 'nil']], '1': ['target'] },
  },
  'CEntities.FindInSphere': {
    returns: 'CBaseEntity',
    args: { '0': ['previous', ['CBaseEntity', 'nil']], '1': ['location'], '2': ['radius'] },
  },
  'CEntities.First': { returns: 'CBaseEntity' },
  'CEntities.GetLocalPlayer': { returns: 'CDOTAPlayer' },
  'CEntities.Next': { returns: 'CBaseEntity', args: { '0': ['previous', 'CBaseEntity'] } },
  'CScriptHeroList.GetAllHeroes': { returns: array('CDOTA_BaseNPC_Hero') },
  'CScriptHeroList.GetHero': { returns: ['CDOTA_BaseNPC_Hero', 'nil'], args: { '0': ['nth'] } },
  'CScriptParticleManager.CreateParticle': {
    returns: 'ParticleID',
    args: {
      '0': ['particleName'],
      '1': ['particleAttach', 'ParticleAttachment'],
      '2': ['owner', ['CDOTA_BaseNPC', 'nil']],
    },
  },
  'CScriptParticleManager.CreateParticleForPlayer': {
    returns: 'ParticleID',
    args: {
      '0': ['particleName'],
      '1': ['particleAttach', 'ParticleAttachment'],
      '2': ['owner', ['CDOTA_BaseNPC', 'nil']],
      '3': ['player', 'CDOTAPlayer'],
    },
  },
  'CScriptParticleManager.CreateParticleForTeam': {
    returns: 'ParticleID',
    args: {
      '0': ['particleName'],
      '1': ['particleAttach', 'ParticleAttachment'],
      '2': ['owner', ['CDOTA_BaseNPC', 'nil']],
      '3': ['team', 'DotaTeam'],
    },
  },
  'CScriptParticleManager.DestroyParticle': {
    args: { '0': ['particle', 'ParticleID'], '1': ['immediate'] },
  },
  'CScriptParticleManager.ReleaseParticleIndex': { args: { '0': ['particle', 'ParticleID'] } },
  'CScriptParticleManager.SetParticleAlwaysSimulate': { args: { '0': ['particle', 'ParticleID'] } },
  'CScriptParticleManager.SetParticleControl': {
    args: { '0': ['particle', 'ParticleID'], '1': ['controlPoint'], '2': ['value'] },
  },
  'CScriptParticleManager.SetParticleControlEnt': {
    args: {
      '0': ['particle', 'ParticleID'],
      '1': ['controlPoint'],
      '2': ['unit', 'CDOTA_BaseNPC'],
      '3': ['particleAttach', 'ParticleAttachment'],
      '4': ['attachment'],
      '5': ['offset'],
      '6': ['lockOrientation'],
    },
  },
  'CScriptParticleManager.SetParticleControlForward': {
    args: { '0': ['particle', 'ParticleID'], '1': ['controlPoint'] },
  },
  'CScriptParticleManager.SetParticleControlOrientation': {
    args: { '0': ['particle', 'ParticleID'], '1': ['controlPoint'] },
  },
  'Convars.GetBool': { returns: 'bool' },
  'Convars.GetCommandClient': { returns: 'CDOTAPlayer' },
  'Convars.GetDOTACommandClient': { returns: 'CDOTAPlayer' },
  'Convars.GetFloat': { returns: 'number' },
  'Convars.GetInt': { returns: 'number' },
  'Convars.GetStr': { returns: 'string' },
  'Convars.RegisterCommand': { args: { '1': ['callback', 'function'], '2': ['description'] } },
  'Convars.RegisterConvar': { args: { '2': ['description'] } },
  'Convars.SetBool': { args: { '1': ['value'] } },
  'Convars.SetFloat': { args: { '1': ['value'] } },
  'Convars.SetInt': { args: { '1': ['value'] } },
  'Convars.SetStr': { args: { '1': ['value'] } },
  '_G.AddFOWViewer': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.ClearTeamCustomHealthbarColor': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.CreateHTTPRequest': { returns: 'CScriptHTTPRequest' },
  '_G.CreateHTTPRequestScriptVM': { returns: 'CScriptHTTPRequest' },
  '_G.CreateHeroForPlayer': {
    returns: 'CDOTA_BaseNPC_Hero',
    args: { '0': ['heroName'], '1': ['player', 'CDOTAPlayer'] },
  },
  '_G.CreateItem': {
    returns: 'CDOTA_Item',
    args: { '0': ['itemName'], '1': ['owner', 'CDOTAPlayer'], '2': ['purchaser', 'CDOTAPlayer'] },
  },
  '_G.CreateItemOnPositionForLaunch': { args: { '0': ['location'], '1': ['item', 'CDOTA_Item'] } },
  '_G.CreateItemOnPositionSync': { args: { '0': ['location'], '1': ['item', 'CDOTA_Item'] } },
  '_G.CreateUnitByName': {
    returns: 'CDOTA_BaseNPC',
    args: {
      '0': ['unitName'],
      '1': ['location'],
      '2': ['findClearSpace'],
      '3': ['npcOwner', ['CBaseEntity', 'nil']],
      '4': ['unitOwner', ['CDOTAPlayer', 'nil']],
      '5': ['teamNumber', 'DotaTeam'],
    },
  },
  '_G.CreateUnitByNameAsync': {
    args: {
      '0': ['unitName'],
      '1': ['location'],
      '2': ['findClearSpace'],
      '3': ['npcOwner', ['CDOTA_BaseNPC', 'nil']],
      '4': ['playerOwner', ['CDOTAPlayer', 'nil']],
      '5': ['team', 'DotaTeam'],
      '6': ['callback', func([['unit', 'CDOTA_BaseNPC']], 'nil')],
    },
  },
  '_G.DoCleaveAttack': {
    args: {
      0: ['attacker', 'CDOTA_BaseNPC'],
      1: ['target', 'CDOTA_BaseNPC'],
      2: ['ability', 'CDOTABaseAbility'],
      3: ['damage'],
      4: ['startRadius'],
      5: ['endRadius'],
      6: ['distance'],
      7: ['effectName'],
    },
  },
  '_G.DoUniqueString': { args: { '0': ['seed'] } },
  '_G.EntIndexToHScript': { returns: 'CBaseEntity', args: { '0': ['entIndex'] } },
  '_G.ExecuteOrderFromTable': { args: { '0': ['order', 'table'] } },
  '_G.FindClearSpaceForUnit': { args: { '0': ['unit', 'CDOTA_BaseNPC'], '1': ['location'] } },
  '_G.FindUnitsInLine': {
    returns: array('CDOTA_BaseNPC'),
    args: {
      '0': ['team', 'DotaTeam'],
      '1': ['startPos'],
      '2': ['endPos'],
      '3': ['cacheUnit', 'CBaseEntity'],
      '4': ['width'],
      '5': ['teamFilter', 'UnitTargetTeam'],
      '6': ['typeFilter', 'UnitTargetType'],
      '7': ['flagFilter', 'UnitTargetFlags'],
    },
  },
  '_G.FindUnitsInRadius': {
    returns: array('CDOTA_BaseNPC'),
    args: {
      '0': ['team', 'DotaTeam'],
      '1': ['location'],
      '2': ['cacheUnit', 'CBaseEntity'],
      '3': ['radius'],
      '4': ['teamFilter', 'UnitTargetTeam'],
      '5': ['typeFilter', 'UnitTargetType'],
      '6': ['flagFilter', 'UnitTargetFlags'],
      '7': ['order'],
      '8': ['canGrowCache'],
    },
  },
  '_G.FireGameEvent': { args: { '0': ['eventName'], '1': ['eventData', 'table'] } },
  '_G.FireGameEventLocal': { args: { '0': ['eventName'], '1': ['eventData', 'table'] } },
  '_G.GetEntityIndexForTreeId': { returns: 'number' },
  '_G.GetGroundHeight': { args: { 0: ['location'], 1: ['unitHull', ['CDOTA_BaseNPC', 'nil']] } },
  '_G.GetGroundPosition': { args: { 0: ['location'], 1: ['unitHull', ['CDOTA_BaseNPC', 'nil']] } },
  '_G.GetTeamHeroKills': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.GetTeamName': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.IsLocationVisible': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.IsValidEntity': { args: { '0': ['entity', 'table'] } },
  '_G.LinkLuaModifier': { args: { '1': ['filePath'], '2': [null, 'LuaModifierMotionType'] } },
  '_G.LoadKeyValues': { args: { '0': ['filePath'] } },
  '_G.LoadKeyValuesFromString': { args: { '0': ['kvString'] } },
  '_G.MinimapEvent': {
    args: {
      '0': ['team', 'DotaTeam'],
      '1': [null, 'CBaseEntity'],
      '4': [null, 'MinimapEventType'],
      '5': ['duration', 'float'],
    },
  },
  '_G.PauseGame': { args: { '0': ['paused'] } },
  '_G.PrecacheItemByNameAsync': { args: { '0': ['itemName'], '1': ['callback', 'function'] } },
  '_G.PrecacheUnitByNameAsync': {
    args: { '0': ['unitName'], '1': ['callback', 'function'], '2': ['playerId'] },
  },
  '_G.RandomFloat': { args: { '0': ['min'], '1': ['max'] } },
  '_G.RandomInt': { args: { '0': ['min'], '1': ['max'] } },
  '_G.RandomVector': { args: { '0': ['length'] } },
  '_G.RollPercentage': {
    description:
      'Rolls a number from 1 to 100 and returns true if the roll is less than or equal to the number specified.',
    args: { '0': ['successPercentage'] },
  },
  '_G.Say': { args: { '0': ['entity', 'CBaseEntity'], '1': ['message'], '2': ['teamOnly'] } },
  '_G.SendOverheadEventMessage': {
    args: { '0': [null, 'CDOTAPlayer'], '2': [null, 'CDOTA_BaseNPC'], '4': [null, 'CDOTAPlayer'] },
  },
  '_G.SetTeamCustomHealthbarColor': { args: { '0': ['team', 'DotaTeam'] } },
  '_G.SpawnEntityFromTableSynchronous': {
    returns: 'CBaseEntity',
    args: { '0': ['baseclass'], '1': ['data', 'table'] },
  },
  '_G.UTIL_Remove': { args: { '0': ['entity', 'CBaseEntity'] } },
  '_G.UTIL_RemoveImmediate': { args: { '0': ['entity', 'CBaseEntity'] } },
  'ProjectileManager.CreateLinearProjectile': {
    returns: 'ProjectileID',
    args: { '0': ['projectileData', 'table'] },
  },
  'ProjectileManager.CreateTrackingProjectile': {
    returns: 'ProjectileID',
    args: { '0': ['projectileData', 'table'] },
  },
  'ProjectileManager.DestroyLinearProjectile': { args: { '0': ['projectile', 'ProjectileID'] } },
  'ProjectileManager.GetLinearProjectileLocation': {
    args: { '0': ['projectile', 'ProjectileID'] },
  },
  'ProjectileManager.GetLinearProjectileRadius': { args: { '0': ['projectile', 'ProjectileID'] } },
  'ProjectileManager.GetLinearProjectileVelocity': {
    args: { '0': ['projectile', 'ProjectileID'] },
  },
  'ProjectileManager.ProjectileDodge': { args: { '0': ['unit', 'CDOTA_BaseNPC'] } },
  'ProjectileManager.UpdateLinearProjectileDirection': {
    args: { '0': ['projectile', 'ProjectileID'], '1': ['direction'], '2': ['speed'] },
  },
};
