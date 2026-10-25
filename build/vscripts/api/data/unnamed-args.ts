import { ExtensionFunction, func } from './utils';

// Names, types and descriptions for arguments that come from the dump without names (`argN`), worked out
// from the engine code: the natives behind the Lua bindings in server.dll / client.dll / vscript.dll
// (build 6966), and checked in game where noted ("Verified in game").
// Merged into `functionExtensions` by `withUnnamedArguments`: an argument field already set there wins.

type Arg = NonNullable<ExtensionFunction['args']>[number];

const rgba = (first: number): Record<number, Arg> => ({
  [first]: ['r', null, 'Red, 0-255.'],
  [first + 1]: ['g', null, 'Green, 0-255.'],
  [first + 2]: ['b', null, 'Blue, 0-255.'],
  [first + 3]: ['a', null, 'Alpha, 0-255.'],
});

const rgb = (first: number): Record<number, Arg> => ({
  [first]: ['r', null, 'Red, 0-255.'],
  [first + 1]: ['g', null, 'Green, 0-255.'],
  [first + 2]: ['b', null, 'Blue, 0-255.'],
});

// CDebugOverlayScriptHelper passes this flag unchanged to the engine's debug overlay, which keeps the shapes
// in two separate lists by it. It is the same flag the older DebugDraw* functions call `ztest`; whether
// `true` enables or disables the depth test was not verified.
const ztest: Arg = [
  'ztest',
  null,
  'Depth test flag, the same as `ztest` of `DebugDrawLine` (which value turns the depth test off was not verified).',
];
const duration: Arg = ['duration', null, 'Seconds.'];

const angularVelocity: Arg = [
  'angularVelocity',
  null,
  'Axis of rotation multiplied by the rotation speed in degrees per second.',
];

const unused = (name = 'unused'): Arg => [name, null, 'Not read by the engine.'];

const soundEntity: Arg = [
  'entity',
  null,
  'Entity the sound is played on. A player controller is replaced with its hero.',
];

const neutralTier: Arg = [
  'tier',
  null,
  "1-based neutral item tier; 0 or less: the item's own tier.",
];

const markAsEarned: Arg = [
  'markAsEarned',
  null,
  "When true, the item is recorded as found by the unit's team (the same record `RecordNeutralItemEarned` makes, without its toast).",
];

const playerEntityIndex: Arg = [
  'playerEntityIndex',
  null,
  'Entity index of the player controller (`CDOTAPlayerController:entindex()`).',
];

const messageContext: Arg = [
  'context',
  'table',
  'Values for the message: `player_id`, `value`, `team_id` (missing keys: -1).',
];

const quaternionNote =
  ' Quaternions cannot be passed to or returned from Lua: `AxisAngleToQuaternion` returns nil there (verified in game).';

export const unnamedArguments: Record<string, ExtensionFunction> = {
  // --- CBodyComponent (physics body of a model entity)
  'CBodyComponent.AddImpulseAtPosition': {
    args: {
      0: ['impulse', null, 'World-space impulse.'],
      1: [
        'position',
        null,
        'World-space point the impulse is applied at; its offset from the center of mass adds angular velocity. Only dynamic bodies are affected.',
      ],
    },
  },
  'CBodyComponent.AddVelocity': { args: { 0: ['linearVelocity'], 1: angularVelocity } },
  'CBodyComponent.SetAngularVelocity': { args: { 0: angularVelocity } },
  'CBodyComponent.SetMaterialGroup': {
    args: { 0: ['materialGroup', null, 'Material group name (hashed into a string token).'] },
  },
  'CBodyComponent.SetVelocity': { args: { 0: ['velocity'] } },

  'CDOTAGameManager.GetHeroLocTokenByID': {
    args: { 0: ['heroId', null, 'Hero ID, 1-255; other values return nil.'] },
  },

  // --- CDOTAGameRules
  'CDOTAGameRules.AddBotPlayerWithEntityScript': {
    args: {
      4: [
        'reuseExistingPlayer',
        null,
        'When true and a player named `playerName` exists, that player gets the hero instead of a new bot being created.',
      ],
    },
  },
  'CDOTAGameRules.AddHeroIDToBlacklist': {
    args: { 0: ['heroId', null, 'Values below 1 are ignored.'] },
  },
  'CDOTAGameRules.AddHeroIDToWhitelist': {
    args: { 0: ['heroId', null, 'Values below 1 are ignored.'] },
  },
  'CDOTAGameRules.AddHeroToBlacklist': {
    args: {
      0: ['heroName', null, 'Both `npc_dota_hero_axe` and `axe` work (verified in game).'],
    },
  },
  'CDOTAGameRules.AddHeroToWhitelist': {
    args: { 0: ['heroName', null, 'Both `npc_dota_hero_axe` and `axe` work.'] },
  },
  'CDOTAGameRules.AddHeroToPlayerAvailability': {
    args: { 0: ['playerId', null, 'Player IDs 64 and above are ignored.'], 1: ['heroId'] },
  },
  'CDOTAGameRules.AddMinimapDebugPoint': {
    args: {
      0: [
        'index',
        null,
        'Identifier sent with the point (`index` of CDOTAUserMsg_MinimapDebugPoint).',
      ],
      1: ['location'],
      ...rgb(2),
      5: ['size'],
      6: duration,
    },
  },
  'CDOTAGameRules.AddMinimapDebugPointForTeam': {
    args: {
      0: [
        'index',
        null,
        'Identifier sent with the point (`index` of CDOTAUserMsg_MinimapDebugPoint).',
      ],
      1: ['location'],
      ...rgb(2),
      5: ['size'],
      6: duration,
      7: ['team', 'DOTATeam_t', 'Team whose players see the point.'],
    },
  },
  'CDOTAGameRules.BeginTemporaryNight': {
    args: {
      1: [
        'source',
        null,
        'Stored as `m_nTemporaryDayNightSource` (what caused the night); the meaning of the values was not established.',
      ],
    },
  },
  'CDOTAGameRules.ClearPlayerHeroAvailability': { args: { 0: ['playerId'] } },
  'CDOTAGameRules.GetGameSessionConfigValue': {
    args: { 0: ['key'], 1: ['defaultValue', null, 'Returned when the key is not set.'] },
  },
  'CDOTAGameRules.GetIetmStockDuration': {
    args: {
      0: [
        'team',
        'DOTATeam_t',
        'Team whose stock is read; a negative value matches no team stock.',
      ],
      1: ['itemName'],
      2: ['playerId', null, 'Player whose own stock is read; -1 matches no player stock.'],
    },
  },
  'CDOTAGameRules.IsHeroEnabledViaLists': { args: { 0: ['heroName'] } },
  'CDOTAGameRules.PrepareSpawners': {
    args: { 0: ['interval', null, 'Seconds between lane creep waves.'] },
  },
  'CDOTAGameRules.RemoveHeroFromBlacklist': { args: { 0: ['heroName'] } },
  'CDOTAGameRules.RemoveHeroFromWhitelist': { args: { 0: ['heroName'] } },
  'CDOTAGameRules.RemoveHeroIDFromBlacklist': { args: { 0: ['heroId'] } },
  'CDOTAGameRules.RemoveHeroIDFromWhitelist': { args: { 0: ['heroId'] } },
  'CDOTAGameRules.ResetPlayer': { args: { 0: ['playerId'] } },
  'CDOTAGameRules.SendCustomMessage': {
    args: {
      0: ['message'],
      1: [
        'playerId',
        null,
        'Player the message is sent on behalf of (`player_id` of CDOTAUserMsg_CustomMsg).',
      ],
      2: ['value', null, 'Integer sent with the message (`value` of CDOTAUserMsg_CustomMsg).'],
    },
  },
  'CDOTAGameRules.SendCustomMessageToTeam': {
    args: {
      0: ['message'],
      1: ['team', 'DOTATeam_t', 'Receiving team; spectators receive the message too.'],
      2: ['playerId', null, 'Player the message is sent on behalf of.'],
      3: ['value', null, 'Integer sent with the message.'],
    },
  },
  'CDOTAGameRules.SetAllowOutpostBonuses': { args: { 0: ['allow'] } },
  'CDOTAGameRules.SetCreepSpawningEnabled': { args: { 0: ['enabled'] } },
  'CDOTAGameRules.SetCustomGameAccountRecordSaveFunction': {
    args: {
      0: [
        'callback',
        null,
        'Function called with a Player ID; nil is rejected with a console message.',
      ],
      1: ['context', null, 'Table the callback is called with; nil is rejected.'],
    },
  },
  'CDOTAGameRules.SetCustomGameAllowSecondaryAbilitiesOnOtherUnits': { args: { 0: ['allow'] } },
  'CDOTAGameRules.SetCustomGameBansPerTeam': { args: { 0: ['bans'] } },
  'CDOTAGameRules.SetEnableAlternateHeroGrids': { args: { 0: ['enabled'] } },
  'CDOTAGameRules.SetFilterMoreGold': { args: { 0: ['filterMoreGold'] } },
  'CDOTAGameRules.SetHeroSelectPenaltyTime': { args: { 0: ['time', null, 'Seconds.'] } },
  'CDOTAGameRules.SetHideBlacklistedHeroes': { args: { 0: ['hide'] } },
  'CDOTAGameRules.SetIgnoreLobbyTeamsInCustomGame': { args: { 0: ['ignore'] } },
  'CDOTAGameRules.SetNeutralInitialSpawnOffset': {
    args: { 0: ['offset', null, 'Seconds added to the delay of the first neutral creep spawn.'] },
  },
  'CDOTAGameRules.SetNextBountyRuneSpawnTime': { args: { 0: ['time'] } },
  'CDOTAGameRules.SetNextRuneSpawnTime': { args: { 0: ['time'] } },
  'CDOTAGameRules.SetPostGameColumns': {
    args: {
      0: [
        'columns',
        'table',
        'Column values 0-9 under keys of at most 2 characters; anything else is rejected with a console message.',
      ],
    },
  },
  'CDOTAGameRules.SetPostGameLayout': {
    args: { 0: ['layout', null, '0 or 1; other values are rejected with a console message.'] },
  },
  'CDOTAGameRules.SetPostGameTeamScores': { args: { 0: ['scores', 'table'] } },
  'CDOTAGameRules.SetRiverPaint': {
    args: {
      0: [
        'riverType',
        null,
        'River style 0-7 (`m_nRiverType`); a river vial sets the position of its item in `river_paint_item_defs`.',
      ],
      1: ['duration', null, 'Seconds.'],
    },
  },
  'CDOTAGameRules.SetSpeechUseSpawnInsteadOfRespawnConcept': { args: { 0: ['useSpawnConcept'] } },
  'CDOTAGameRules.SetSuggestAbilitiesEnabled': { args: { 0: ['enabled'] } },
  'CDOTAGameRules.SetSuggestItemsEnabled': { args: { 0: ['enabled'] } },
  'CDOTAGameRules.SetWeatherWindDirection': { args: { 0: ['direction'] } },

  // --- CDOTATutorial
  'CDOTATutorial.AddBot': {
    args: {
      0: [null, null, '`random` picks a random hero.'],
      1: ['lane', null, "Stored as the bot's `force_lane` setting; nil: not set."],
      2: ['difficulty', null, "Stored as the bot's `difficulty` setting; nil: not set."],
      3: ['goodGuys', null, 'true: the bot joins DOTA_TEAM_GOODGUYS, false: DOTA_TEAM_BADGUYS.'],
    },
  },
  'CDOTATutorial.AddQuest': {
    args: {
      0: ['name', null, 'Quest name, used by `CompleteQuest`.'],
      1: ['type'],
      2: ['title'],
      3: ['text'],
    },
  },
  'CDOTATutorial.CompleteQuest': {
    args: { 0: ['name', null, 'Name the quest was added with.'] },
  },
  'CDOTATutorial.CreateLocationTask': { args: { 0: ['location'] } },
  'CDOTATutorial.EnableCreepAggroViz': { args: { 0: ['enabled'] } },
  'CDOTATutorial.EnablePlayerOffscreenTip': { args: { 0: ['enabled'] } },
  'CDOTATutorial.EnableTowerAggroViz': { args: { 0: ['enabled'] } },
  'CDOTATutorial.MoveCameraToLocation': { args: { 0: ['location'] } },
  'CDOTATutorial.SelectPlayerTeam': {
    args: { 0: ['team', null, '`good` or `bad`; other values are ignored.'] },
  },
  'CDOTATutorial.SetItemGuide': { args: { 0: ['guideName'] } },
  'CDOTATutorial.SetTutorialConvar': { args: { 0: ['convarName'], 1: ['value'] } },
  'CDOTATutorial.SetTutorialUI': { args: { 0: ['mode'] } },

  // --- CEntityInstance (entity I/O)
  'CEntityInstance.ConnectOutput': {
    args: {
      0: ['outputName'],
      1: ['functionName', null, "Function in this entity's script scope."],
    },
  },
  'CEntityInstance.DisconnectOutput': { args: { 0: ['outputName'], 1: ['functionName'] } },
  'CEntityInstance.DisconnectRedirectedOutput': {
    args: { 0: ['outputName'], 1: ['functionName'], 2: ['entity', 'CBaseEntity'] },
  },
  'CEntityInstance.FireOutput': {
    args: {
      0: ['outputName'],
      1: ['activator', ['CBaseEntity', 'nil'], 'nil: this entity.'],
      2: ['caller', ['CBaseEntity', 'nil'], 'nil: this entity.'],
      3: ['value', null, 'Value passed with the output.'],
      4: ['delay', null, 'Seconds.'],
    },
  },
  'CEntityInstance.GetIntAttr': { args: { 0: ['name'] } },
  'CEntityInstance.RedirectOutput': {
    args: {
      0: ['outputName'],
      1: ['functionName'],
      2: ['entity', 'CBaseEntity', 'Entity whose script function is called.'],
    },
  },
  'CEntityInstance.SetIntAttr': { args: { 0: ['name'], 1: ['value'] } },

  'CNativeOutputs.AddOutput': { args: { 0: ['outputName'], 1: unused('description') } },
  'CNativeOutputs.Init': {
    args: { 0: ['count', null, 'Number of outputs to reserve space for.'] },
  },

  // --- CSceneEntity
  'CSceneEntity.AddBroadcastTeamTarget': { args: { 0: ['team', 'DOTATeam_t'] } },
  'CSceneEntity.FindNamedEntity': {
    args: { 0: ['name', null, 'Entity reference such as `!target`, or an entity name.'] },
  },
  'CSceneEntity.RemoveBroadcastTeamTarget': { args: { 0: ['team', 'DOTATeam_t'] } },
  'CSceneEntity.Start': { args: { 0: ['activator', ['CBaseEntity', 'nil']] } },

  'CScriptKeyValues.GetValue': { args: { 0: ['key'] } },

  'CScriptParticleManager.SetParticleControlForward': { args: { 2: ['forward'] } },
  'CScriptParticleManager.SetParticleControlOrientation': {
    args: { 2: ['forward'], 3: ['right'], 4: ['up'] },
  },
  'CScriptParticleManager.SetParticleControlOrientationFLU': {
    args: { 2: ['forward'], 3: ['left'], 4: ['up'] },
  },

  // --- GlobalSys
  'GlobalSys.CommandLineFloat': {
    args: {
      0: ['name', null, 'Parameter name with the leading `-`, e.g. `-port` (verified in game).'],
      1: ['defaultValue', null, 'Returned when the parameter is not on the command line.'],
    },
  },
  'GlobalSys.CommandLineInt': {
    args: {
      0: ['name', null, 'Parameter name with the leading `-`, e.g. `-port` (verified in game).'],
      1: ['defaultValue', null, 'Returned when the parameter is not on the command line.'],
    },
  },
  'GlobalSys.CommandLineStr': {
    args: {
      0: ['name', null, 'Parameter name with the leading `-`, e.g. `-port` (verified in game).'],
      1: ['defaultValue', null, 'Returned when the parameter has no value on the command line.'],
    },
  },

  // --- GridNav
  'GridNav.DestroyTreesAroundPoint': {
    args: { 0: ['position'], 1: ['radius'], 2: ['fullCollision'] },
  },
  'GridNav.GridPosToWorldCenterX': { args: { 0: ['x', null, 'Grid X index.'] } },
  'GridNav.GridPosToWorldCenterY': { args: { 0: ['y', null, 'Grid Y index.'] } },
  'GridNav.IsBlocked': { args: { 0: ['position', null, 'Only x and y are used.'] } },
  'GridNav.IsTraversable': { args: { 0: ['position', null, 'Only x and y are used.'] } },
  'GridNav.WorldToGridPosX': { args: { 0: ['x', null, 'World X coordinate.'] } },
  'GridNav.WorldToGridPosY': { args: { 0: ['y', null, 'World Y coordinate.'] } },

  // --- CDebugOverlayScriptHelper (`debugoverlay`)
  'CDebugOverlayScriptHelper.Axis': {
    args: { 0: ['origin'], 1: ['angles'], 2: ['scale'], 3: ztest, 4: duration },
  },
  'CDebugOverlayScriptHelper.Box': {
    args: { 0: ['mins'], 1: ['maxs'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.BoxAngles': {
    args: {
      0: ['origin'],
      1: ['mins', null, 'Relative to origin.'],
      2: ['maxs', null, 'Relative to origin.'],
      3: ['angles'],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Capsule': {
    args: {
      0: ['origin', null, 'Bottom of the capsule.'],
      1: ['angles'],
      2: ['height', null, 'Distance between the centers of the end spheres.'],
      3: ['radius'],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Circle': {
    args: {
      0: ['center'],
      1: ['angles', null, 'Orientation of the circle plane.'],
      2: ['radius'],
      ...rgba(3),
      7: ztest,
      8: duration,
    },
  },
  'CDebugOverlayScriptHelper.CircleScreenOriented': {
    args: { 0: ['center'], 1: ['radius'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.Cone': {
    args: {
      0: ['apex'],
      1: ['direction'],
      2: ['angle', null, 'Full opening angle in radians.'],
      3: ['length'],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Cross': {
    args: { 0: ['origin'], 1: ['size'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.Cross3D': {
    args: { 0: ['origin'], 1: ['size'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.Cross3DOriented': {
    args: { 0: ['origin'], 1: ['angles'], 2: ['size'], ...rgba(3), 7: ztest, 8: duration },
  },
  'CDebugOverlayScriptHelper.DrawTickMarkedLine': {
    args: {
      0: ['start'],
      1: ['end'],
      2: ['tickDistance', null, 'Distance between ticks (truncated to an integer).'],
      3: [
        'tickTextDistance',
        null,
        'Unverified: in Source, every this many ticks get a distance label.',
      ],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.EntityAttachments': {
    args: {
      0: ['entity'],
      1: ['scale', null, 'Size of the attachment axes; 0 or less picks a default.'],
      2: duration,
    },
  },
  'CDebugOverlayScriptHelper.EntityAxis': {
    args: { 0: ['entity'], 1: ['scale'], 2: ztest, 3: duration },
  },
  'CDebugOverlayScriptHelper.EntityBounds': {
    args: { 0: ['entity'], ...rgba(1), 5: ztest, 6: duration },
  },
  'CDebugOverlayScriptHelper.EntitySkeleton': { args: { 0: ['entity'], 1: duration } },
  'CDebugOverlayScriptHelper.EntityText': {
    args: { 0: ['entity'], 1: ['lineOffset'], 2: ['text'], ...rgba(3), 7: duration },
  },
  'CDebugOverlayScriptHelper.FilledRect2D': {
    args: {
      0: ['mins', null, 'Top-left corner in pixels.'],
      1: ['maxs', null, 'Bottom-right corner in pixels.'],
      ...rgba(2),
      6: duration,
    },
  },
  'CDebugOverlayScriptHelper.HorzArrow': {
    args: { 0: ['start'], 1: ['end'], 2: ['width'], ...rgba(3), 7: ztest, 8: duration },
  },
  'CDebugOverlayScriptHelper.Line': {
    args: { 0: ['start'], 1: ['end'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.Line2D': {
    args: { 0: ['start', null, 'Pixels.'], 1: ['end', null, 'Pixels.'], ...rgba(2), 6: duration },
  },
  'CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope': { args: { 0: ['scopeName'] } },
  'CDebugOverlayScriptHelper.PushDebugOverlayScope': { args: { 0: ['scopeName'] } },
  'CDebugOverlayScriptHelper.RemoveAllInScope': { args: { 0: ['scopeName'] } },
  'CDebugOverlayScriptHelper.SolidCone': {
    args: {
      0: ['apex'],
      1: ['direction'],
      2: ['angle', null, 'Full opening angle in radians.'],
      3: ['length'],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Sphere': {
    args: { 0: ['center'], 1: ['radius'], ...rgba(2), 6: ztest, 7: duration },
  },
  'CDebugOverlayScriptHelper.SweptBox': {
    args: {
      0: ['start'],
      1: ['end'],
      2: ['mins', null, 'Local-space bounds.'],
      3: ['maxs', null, 'Local-space bounds.'],
      4: ['angles'],
      ...rgba(5),
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Text': {
    args: {
      0: ['origin'],
      1: ['lineOffset'],
      2: ['text'],
      3: ['maxDistance', null, 'Hidden farther than this from the camera; 0: always shown.'],
      ...rgba(4),
      8: duration,
    },
  },
  'CDebugOverlayScriptHelper.Texture': {
    args: {
      0: ['textureName'],
      1: ['mins', null, 'Top-left corner in pixels.'],
      2: ['maxs', null, 'Bottom-right corner in pixels.'],
      ...rgba(3),
      7: ['uvMins', null, 'Texture coordinates.'],
      8: ['uvMaxs', null, 'Texture coordinates.'],
      9: duration,
    },
  },
  'CDebugOverlayScriptHelper.Triangle': {
    args: { 0: ['vertex1'], 1: ['vertex2'], 2: ['vertex3'], ...rgba(3), 7: ztest, 8: duration },
  },
  'CDebugOverlayScriptHelper.VectorText3D': {
    args: { 0: ['origin'], 1: ['angles'], 2: ['text'], ...rgba(3), 7: ztest, 8: duration },
  },
  'CDebugOverlayScriptHelper.VertArrow': {
    args: { 0: ['start'], 1: ['end'], 2: ['width'], ...rgba(3), 7: ztest, 8: duration },
  },
  'CDebugOverlayScriptHelper.YawArrow': {
    args: {
      0: ['start'],
      1: ['yaw', null, 'Degrees.'],
      2: ['length'],
      3: ['width'],
      ...rgba(4),
      8: ztest,
      9: duration,
    },
  },

  // --- global functions
  '_G.AngleDiff': {
    args: {
      0: ['destAngle', null, 'Degrees.'],
      1: ['srcAngle', null, 'Degrees. The result is `destAngle - srcAngle` wrapped to -180..180.'],
    },
  },
  '_G.AnglesToVector': { args: { 0: ['angles'] } },
  '_G.AppendToLogFile': { args: { 0: unused('unused1'), 1: unused('unused2') } },
  '_G.AxisAngleToQuaternion': {
    description: (o) => `${o}${quaternionNote}`,
    args: { 0: ['axis'], 1: ['angle', null, 'Degrees.'] },
  },
  '_G.CalcClosestPointOnEntityOBB': { args: { 0: ['entity', 'CBaseEntity'], 1: ['position'] } },
  '_G.CalcDistanceBetweenEntityOBB': {
    args: { 0: ['entity1', 'CBaseEntity'], 1: ['entity2', 'CBaseEntity'] },
  },
  '_G.CalcDistanceToLineSegment2D': {
    description: 'Distance from a point to a line segment, in 2D (z is ignored).',
    args: { 0: ['point'], 1: ['segmentStart'], 2: ['segmentEnd'] },
  },
  '_G.CancelEntityIOEvents': {
    description: 'Cancel all pending I/O events for a particular entity.',
    args: { 0: ['entity'] },
  },
  '_G.CreateDamageInfo': {
    args: {
      0: ['inflictor', ['CBaseEntity', 'nil']],
      1: ['attacker', ['CBaseEntity', 'nil']],
      2: ['force'],
      3: ['position'],
      4: ['damage'],
      5: ['damageType', null, 'Damage type bits of the damage info.'],
    },
  },
  '_G.CreateSceneEntity': {
    args: {
      0: [
        'sceneFile',
        null,
        'Scene file of the `logic_choreographed_scene`; refused once the game is running (only while the map loads).',
      ],
    },
  },
  '_G.CreateTrigger': {
    description: 'Creates and returns an AABB trigger (`trigger_multiple`).',
    args: {
      0: ['origin'],
      1: ['mins', null, 'Relative to origin.'],
      2: ['maxs', null, 'Relative to origin.'],
    },
  },
  '_G.CrossVectors': { args: { 0: ['a'], 1: ['b'] } },
  '_G.cvar_getf': { args: { 0: ['name', null, 'Unknown convars return 0.'] } },
  '_G.cvar_setf': {
    args: {
      0: ['name', null, 'Unknown convars: returns false with a console warning.'],
      1: ['value'],
    },
  },
  '_G.DebugChangeTeam': {
    description: "Moves the hero's player between DOTA_TEAM_GOODGUYS and DOTA_TEAM_BADGUYS.",
    args: { 0: ['hero', 'CDOTA_BaseNPC_Hero'] },
  },
  '_G.DebugCreateHeroWithVariant': {
    args: {
      0: ['playerOwner', 'CDOTAPlayerController'],
      1: ['heroName'],
      2: ['variant', null, 'Hero variant (facet) selected for the player along with the hero.'],
      3: ['team', 'DOTATeam_t'],
      4: unused(),
      5: ['callback', func([['unit', 'CDOTA_BaseNPC']], 'nil')],
    },
  },
  '_G.DebugCreateUnit': { args: { 3: unused() } },
  '_G.DebugDrawBox': {
    description: 'Draw a debug overlay box.',
    args: {
      0: ['origin'],
      1: ['mins', null, 'Relative to origin.'],
      2: ['maxs', null, 'Relative to origin.'],
      ...rgba(3),
      7: duration,
    },
  },
  '_G.DebugDrawLine_vCol': {
    description: 'Draw a debug line using color vec.',
    args: {
      0: ['start'],
      1: ['end'],
      2: ['rgb', null, 'Color, components 0-255.'],
      3: ['ztest', null, 'Same as `ztest` of `DebugDrawLine`.'],
      4: duration,
    },
  },
  '_G.DisconnectClient': {
    args: {
      0: ['playerId'],
      1: [
        'removeBotHeroes',
        null,
        'When true and the player is a fake client (bot), the heroes it owns are removed too. The player is kicked either way.',
      ],
    },
  },
  '_G.DoEntFire': {
    args: {
      0: ['target', null, 'Name of the target entities.'],
      1: ['action', null, 'Input name; empty: `Use`.'],
      2: ['value', null, 'Parameter of the input; empty: none.'],
      3: ['delay', null, 'Seconds; negative values mean 0.'],
      4: ['activator', ['CBaseEntity', 'nil']],
      5: ['caller', ['CBaseEntity', 'nil']],
    },
  },
  '_G.DoEntFireByInstanceHandle': {
    args: {
      0: ['target', 'CBaseEntity'],
      1: ['action', null, 'Input name; empty: `Use`.'],
      2: ['value', null, 'Parameter of the input; empty: none.'],
      3: ['delay', null, 'Seconds; negative values mean 0.'],
      4: ['activator', ['CBaseEntity', 'nil']],
      5: ['caller', ['CBaseEntity', 'nil']],
    },
  },
  '_G.DoIncludeScript': { args: { 0: ['scriptName'], 1: ['scope', ['table', 'nil']] } },
  '_G.DoScriptAssert': {
    args: { 0: ['assertion'], 1: ['message'] },
  },
  '_G.DotProduct': { args: { 0: ['a'], 1: ['b'] } },
  '_G.DropNeutralItemAtPositionForHero': { args: { 3: neutralTier, 4: markAsEarned } },
  '_G.DropNeutralItemAtPositionForHeroWithOffset': {
    returns: 'CDOTA_Item_Physical',
    args: {
      0: ['itemName', null, 'Can be any item name, it does not have to be neutral.'],
      1: ['location'],
      2: ['unit', 'CDOTA_BaseNPC'],
      3: neutralTier,
      4: markAsEarned,
      5: [
        'launchOffset',
        null,
        'Added to the point the item is launched from (the unit position moved up to 100 units toward location).',
      ],
    },
  },
  '_G.EmitSoundOnClient': {
    args: { 1: ['player', null, "Player controller, or the player's hero."] },
  },
  '_G.EmitSoundOnEntityForPlayer': {
    args: { 0: ['soundName'], 1: ['entity', 'CBaseEntity'], 2: ['playerId'] },
  },
  '_G.EmitSoundOnLocationForPlayer': {
    args: { 0: ['soundName'], 1: ['location'], 2: ['playerId'] },
  },
  '_G.ExponentialDecay': {
    description:
      'Smooth curve decreasing slower as it approaches zero: `decayTo ^ (dt / decayTime)`.',
    args: {
      0: ['decayTo', null, 'Value reached after `decayTime`.'],
      1: ['decayTime'],
      2: ['dt'],
    },
  },
  '_G.FindClearRandomPositionAroundUnit': {
    args: {
      0: ['unit', 'CDOTA_BaseNPC', 'Unit that is moved.'],
      1: ['target', 'CDOTA_BaseNPC', 'Unit it is placed around.'],
      2: [
        'extraDistance',
        null,
        "Added to the sum of both units' padded collision radii. The direction steps by 90 degrees on every call.",
      ],
    },
  },
  '_G.FindClearSpaceForUnit': {
    args: {
      2: [
        'interrupt',
        null,
        'When false, a unit whose movement component reports active movement is not moved and false is returned; when true that movement is interrupted and the unit is teleported.',
      ],
    },
  },
  '_G.FireEntityIOInputNameOnly': { args: { 0: ['entity'], 1: ['input'] } },
  '_G.FireEntityIOInputString': { args: { 0: ['entity'], 1: ['input'], 2: ['value'] } },
  '_G.FireEntityIOInputVec': { args: { 0: ['entity'], 1: ['input'], 2: ['value'] } },
  '_G.GetAbilityKeyValuesByName': { args: { 0: ['abilityName'] } },
  '_G.GetClearSpaceForUnit': {
    args: {
      0: ['unit', 'CDOTA_BaseNPC'],
      1: ['location', null, 'Returned unchanged when no clear space is found.'],
    },
  },
  '_G.GetItemCost': { args: { 0: ['itemName', null, 'Unknown items cost 0.'] } },
  '_G.GetItemDefOwnedCount': {
    args: { 0: ['playerId'], 1: ['itemDef', null, 'Econ item definition index.'] },
  },
  '_G.GetItemDefQuantity': {
    args: { 0: ['playerId'], 1: ['itemDef', null, 'Econ item definition index.'] },
  },
  '_G.GetLocalPlayerTeam': {
    args: { 0: ['unused', null, 'Not read: the local player of split-screen slot 0 is used.'] },
  },
  '_G.GetMaxOutputDelay': { args: { 0: ['entity'], 1: ['outputName'] } },
  '_G.GetPhysAngularVelocity': { args: { 0: ['entity', 'CBaseEntity'] } },
  '_G.GetPhysVelocity': { args: { 0: ['entity', 'CBaseEntity'] } },
  '_G.GetTargetAOELocation': {
    description:
      'Center of the best cluster of units for an area effect (the bot helper). Units are searched within `castRange + radius` of origin, invisible ones excluded; returns a vector of FLT_MAX components when fewer than `minTargets` are found.',
    args: {
      0: ['team', 'DOTATeam_t'],
      1: ['typeFilter', 'DOTA_UNIT_TARGET_TYPE'],
      2: ['teamFilter', 'DOTA_UNIT_TARGET_TEAM'],
      3: ['origin'],
      4: ['castRange'],
      5: ['radius'],
      6: ['minTargets'],
    },
  },
  '_G.GetTargetLinearLocation': {
    description:
      'Best point for a line effect (the bot helper). Units are searched within `range + width` of origin, invisible ones excluded; returns a vector of FLT_MAX components when fewer than `minTargets` are found.',
    args: {
      0: ['team', 'DOTATeam_t'],
      1: ['typeFilter', 'DOTA_UNIT_TARGET_TYPE'],
      2: ['teamFilter', 'DOTA_UNIT_TARGET_TEAM'],
      3: ['origin'],
      4: ['range'],
      5: ['width'],
      6: ['minTargets'],
    },
  },
  '_G.GetUnitKeyValuesByName': { args: { 0: ['unitName'] } },
  '_G.HeroMaxLevel': { args: { 0: ['hero', 'CDOTA_BaseNPC_Hero'] } },
  '_G.InitLogFile': { args: { 0: unused('unused1'), 1: unused('unused2') } },
  '_G.LerpVectors': { args: { 0: ['a'], 1: ['b'], 2: ['t', null, 'Not clamped.'] } },
  '_G.LimitPathingSearchDepth': {
    args: { 0: ['limit', null, 'Fraction of the full search space, clamped to 0-1.'] },
  },
  '_G.MakeStringToken': {
    description: 'Returns the string token (hash) of the lowercased string; 0 for an empty string.',
    args: { 0: ['text'] },
  },
  '_G.PrecacheEntityFromTable': { args: { 0: ['className'], 1: ['keyValues', 'table'] } },
  '_G.PrecacheEntityListFromTable': { args: { 0: ['spawnTables', 'table'] } },
  '_G.PrecacheResource': {
    args: {
      0: ['resourceType', null, 'Precache entry key, e.g. `particle`, `soundfile`, `model`.'],
      1: ['resourcePath'],
    },
  },
  '_G.PrecacheUnitFromTableAsync': {
    args: { 0: ['keyValues', 'table', 'The unit is taken from its `MapUnitName` key.'] },
  },
  '_G.PrecacheUnitFromTableSync': {
    args: { 0: ['keyValues', 'table', 'The unit is taken from its `MapUnitName` key.'] },
  },
  '_G.RandomFloatWrapper': { args: { 0: ['min'], 1: ['max'] } },
  '_G.RecordNeutralItemEarned': {
    args: {
      0: ['hero', 'CDOTA_BaseNPC', 'Its team is credited.'],
      1: ['item', 'CDOTA_Item'],
      2: ['tier', null, '1-based neutral item tier.'],
    },
  },
  '_G.RegisterCustomAnimationScriptForModel': {
    args: {
      0: ['modelName', null, 'Only printed: the function is deprecated and does nothing.'],
      1: ['scriptName', null, 'Only printed.'],
    },
  },
  '_G.RegisterSpawnGroupFilterProxy': { args: { 0: ['name'] } },
  '_G.RemoveSpawnGroupFilterProxy': { args: { 0: ['name'] } },
  '_G.RotateOrientation': {
    args: {
      0: ['a'],
      1: ['b', null, 'The result is the rotation of `a` followed by `b` (matrix a * b).'],
    },
  },
  '_G.RotatePosition': {
    args: { 0: ['rotationOrigin'], 1: ['rotationAngle'], 2: ['position'] },
  },
  '_G.RotateQuaternionByAxisAngle': {
    description: (o) => `${o}${quaternionNote}`,
    args: { 0: ['quaternion'], 1: ['axis'], 2: ['angle', null, 'Degrees.'] },
  },
  '_G.RotationDelta': {
    description: 'Find the rotation from one QAngle to another (verified in game).',
    args: { 0: ['src'], 1: ['dest'] },
  },
  '_G.RotationDeltaAsAngularVelocity': {
    description:
      'Rotation from one QAngle to another as an angular velocity: axis multiplied by degrees (verified in game).',
    args: { 0: ['src'], 1: ['dest'] },
  },
  '_G.Script_RandomFloat': { args: { 0: ['min'], 1: ['max'] } },
  '_G.Script_RemapValClamped': {
    args: {
      0: ['value'],
      1: ['inputStart'],
      2: ['inputEnd'],
      3: ['outputStart'],
      4: ['outputEnd'],
    },
  },
  '_G.SendToConsole': { args: { 0: ['command'] } },
  '_G.SendToServerConsole': { args: { 0: ['command'] } },
  '_G.SetOpvarFloatAll': {
    args: { 0: ['stackName'], 1: ['operatorName'], 2: ['opvarName'], 3: ['value'] },
  },
  '_G.SetOpvarFloatPlayer': {
    args: {
      0: ['stackName'],
      1: ['operatorName'],
      2: ['opvarName'],
      3: ['value'],
      4: ['player', 'CDOTAPlayerController'],
    },
  },
  '_G.SetPhysAngularVelocity': { args: { 0: ['entity', 'CBaseEntity'], 1: angularVelocity } },
  '_G.SetQuestName': { args: { 0: ['name'] } },
  '_G.SetQuestPhase': { args: { 0: ['phase'] } },
  '_G.SetRenderingEnabled': { args: { 0: ['entity'], 1: ['enabled'] } },
  '_G.ShowGenericPopup': {
    args: {
      0: ['header'],
      1: ['body'],
      2: ['param1'],
      3: ['param2'],
      4: [
        'flags',
        null,
        '1: tint the screen, 2: show no other dialogs (`tint_screen`, `show_no_other_dialogs` of CDOTAUserMsg_ShowGenericPopup).',
      ],
    },
  },
  '_G.ShowGenericPopupToPlayer': {
    args: {
      0: ['player', 'CDOTAPlayerController'],
      1: ['header'],
      2: ['body'],
      3: ['param1'],
      4: ['param2'],
      5: ['flags', null, '1: tint the screen, 2: show no other dialogs.'],
    },
  },
  '_G.ShowMessage': { args: { 0: ['message'] } },
  '_G.SpawnEffigyOfUnitOrModel': {
    args: {
      0: ['unitOrModel', null, 'Unit name, or a `.vmdl` model path.'],
      1: ['team', 'DOTATeam_t'],
      2: ['origin'],
      3: ['angles', null, 'Pitch, yaw, roll.'],
      4: ['pedestalScale', null, 'Model scale of the pedestal.'],
      5: ['modelScale', null, "Model scale of the statue; negative: the unit's `ModelScale`."],
      6: [
        'effigyType',
        null,
        'Status effect index of the statue material; also selects the pedestal model (with team).',
      ],
    },
  },
  '_G.SpawnEntityFromTableAsynchronous': {
    args: {
      0: ['className'],
      1: ['keyValues', 'table'],
      2: ['callback', null, 'Called when the entity has spawned.'],
      3: ['context'],
    },
  },
  '_G.SpawnEntityGroupFromTable': {
    args: {
      0: ['spawnTables', 'table', 'Entity tables, each with a `classname` key.'],
      1: [
        'async',
        null,
        'true: spawned through the asynchronous queue, the callback runs when it completes; false: spawned right away and the callback runs before the function returns.',
      ],
      2: ['callback'],
    },
  },
  '_G.SpawnEntityListFromTableAsynchronous': {
    args: {
      0: ['spawnTables', 'table', 'Entity tables, each with a `classname` key.'],
      1: ['callback', null, 'Called when spawning is complete.'],
    },
  },
  '_G.SpawnEntityListFromTableSynchronous': {
    args: { 0: ['spawnTables', 'table', 'Entity tables, each with a `classname` key.'] },
  },
  '_G.SplineQuaternions': {
    description: (o) => `${o}${quaternionNote}`,
    args: { 0: ['q0'], 1: ['q1'], 2: ['t', null, 'Clamped to 0-1.'] },
  },
  '_G.SplineVectors': {
    args: { 0: ['v0'], 1: ['v1'], 2: ['t', null, 'Clamped to 0-1; smoothstep curve.'] },
  },
  '_G.StartSoundEvent': { args: { 0: ['soundName'], 1: soundEntity } },
  '_G.StartSoundEventReliable': { args: { 0: ['soundName'], 1: soundEntity } },
  '_G.StartSoundEventUnreliable': { args: { 0: ['soundName'], 1: soundEntity } },
  '_G.StopEffect': { args: { 0: ['entity', ['CBaseEntity', 'nil']], 1: ['effectName'] } },
  '_G.StopGlobalSound': { args: { 0: ['soundName'] } },
  '_G.StopListeningToAllGameEvents': {
    args: { 0: ['context', 'table', 'Context table the listeners were registered with.'] },
  },
  '_G.StopSoundEvent': { args: { 0: ['soundName'], 1: soundEntity } },
  '_G.StopSoundOn': { args: { 0: ['soundName'], 1: soundEntity } },
  '_G.UnloadSpawnGroup': { args: { 0: ['spawnGroupName'] } },
  '_G.UserIDToControllerHScript': {
    args: { 0: ['userId', null, 'The `userid` field of game events.'] },
  },
  '_G.UTIL_MessageText': {
    args: { 0: playerEntityIndex, 1: ['message'], ...rgba(2) },
  },
  '_G.UTIL_MessageText_WithContext': {
    args: { 0: playerEntityIndex, 1: ['message'], ...rgba(2), 6: messageContext },
  },
  '_G.UTIL_MessageTextAll': { args: { 0: ['message'], ...rgba(1) } },
  '_G.UTIL_MessageTextAll_WithContext': {
    args: { 0: ['message'], ...rgba(1), 5: messageContext },
  },
  '_G.UTIL_ResetMessageText': { args: { 0: playerEntityIndex } },
  '_G.VectorAngles': { args: { 0: ['direction'] } },
  '_G.VectorToAngles': { args: { 0: ['direction'] } },

  // --- arguments named after their type
  'CDOTA_Ability_Lua.IsCosmetic': { args: { 0: [null, 'CBaseEntity'] } },
  'CDOTA_Buff.CheckStateToTable': { args: { 0: ['states', 'table'] } },
  'CDOTA_Buff.HasFunction': { args: { 0: ['modifierFunction'] } },
  'CDOTABaseGameMode.ListenForQueryFailed': { args: { 0: ['callback'] } },
  'CDOTABaseGameMode.ListenForQueryProgressChanged': { args: { 0: ['callback'] } },
  'CDOTABaseGameMode.ListenForQuerySucceeded': { args: { 0: ['callback'] } },
  'CDotaQuest.SetTextReplaceString': { args: { 0: ['text'] } },
  'CDotaSubquestBase.SetTextReplaceString': { args: { 0: ['text'] } },
  'CEnvEntityMaker.SpawnEntityAtEntityOrigin': { args: { 0: [null, 'CBaseEntity'] } },
};

/** Adds `unnamedArguments` to function extensions; fields an extension already sets are kept. */
export function withUnnamedArguments(
  extensions: Record<string, ExtensionFunction>,
): Record<string, ExtensionFunction> {
  const result = { ...extensions };
  for (const [name, extra] of Object.entries(unnamedArguments)) {
    const current = result[name] ?? {};
    const args: NonNullable<ExtensionFunction['args']> = { ...extra.args };
    for (const [index, value] of Object.entries(current.args ?? {})) {
      const i = Number(index);
      const added = args[i];
      args[i] = added
        ? [value[0] ?? added[0], value[1] ?? added[1] ?? null, value[2] ?? added[2]]
        : value;
    }
    result[name] = {
      ...extra,
      ...current,
      description: current.description ?? extra.description,
      returns: current.returns ?? extra.returns,
      args,
    };
  }
  return result;
}
