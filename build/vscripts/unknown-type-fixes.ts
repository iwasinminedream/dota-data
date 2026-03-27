/**
 * Known type corrections for `<unknown>` types in the Dota 2 dump.
 *
 * The engine's Lua binding reflection system returns `<unknown>` for certain
 * native C++ types (mostly Vector, QAngle, and occasionally string) that it
 * can't resolve at runtime. This map provides the correct types for all known
 * occurrences, keyed by class name (or '_G' for globals) → method name.
 *
 * These corrections are applied automatically after parsing the dump JSON,
 * so future dumps will produce correct types without manual intervention.
 */

interface TypeFix {
  returns?: string;
  args?: Record<number, string>;
}

export const unknownTypeFixes: Record<string, Record<string, TypeFix>> = {
  _G: {
    CreateDamageInfo: { args: { 3: 'Vector' } },
    CreateTrigger: { args: { 0: 'Vector' } },
    CreateTriggerRadiusApproximate: { args: { 0: 'Vector' } },
    DebugDrawBox: { args: { 0: 'Vector' } },
    DebugDrawBoxDirection: { args: { 0: 'Vector' } },
    DebugDrawCircle: { args: { 0: 'Vector' } },
    DebugDrawLine: { args: { 0: 'Vector', 1: 'Vector' } },
    DebugDrawLine_vCol: { args: { 0: 'Vector', 1: 'Vector' } },
    DebugDrawSphere: { args: { 0: 'Vector' } },
    DebugDrawText: { args: { 0: 'Vector' } },
    EmitSoundOnLocationForAllies: { args: { 0: 'Vector' } },
    EmitSoundOnLocationWithCaster: { args: { 0: 'Vector' } },
    RotatePosition: { returns: 'Vector', args: { 0: 'Vector', 2: 'Vector' } },
    ScreenShake: { args: { 0: 'Vector' } },
    StartSoundEventFromPosition: { args: { 1: 'Vector' } },
    StartSoundEventFromPositionReliable: { args: { 1: 'Vector' } },
    StartSoundEventFromPositionUnreliable: { args: { 1: 'Vector' } },
  },
  CBaseEntity: {
    EyePosition: { returns: 'Vector' },
    GetAbsOrigin: { returns: 'Vector' },
    GetCenter: { returns: 'Vector' },
    GetOrigin: { returns: 'Vector' },
    SetAbsOrigin: { args: { 0: 'Vector' } },
    TransformPointEntityToWorld: { returns: 'Vector' },
    TransformPointWorldToEntity: { args: { 0: 'Vector' } },
  },
  CBaseModelEntity: {
    GetAttachmentOrigin: { returns: 'Vector' },
  },
  CBodyComponent: {
    AddImpulseAtPosition: { args: { 1: 'Vector' } },
  },
  CDOTABaseAbility: {
    GetCursorPosition: { returns: 'Vector' },
  },
  CDOTA_BaseNPC: {
    GetCursorPosition: { returns: 'Vector' },
    MoveToPositionAggressive: { args: { 0: 'Vector' } },
  },
  CDebugOverlayScriptHelper: {
    Axis: { args: { 1: 'QAngle' } },
    BoxAngles: { args: { 3: 'QAngle' } },
    Capsule: { args: { 1: 'QAngle' } },
    Circle: { args: { 1: 'QAngle' } },
    Cross3DOriented: { args: { 1: 'QAngle' } },
    SweptBox: { args: { 4: 'QAngle' } },
    VectorText3D: { args: { 1: 'QAngle' } },
  },
  CEntities: {
    FindAllByClassnameWithin: { args: { 1: 'Vector' } },
    FindAllByNameWithin: { args: { 1: 'Vector' } },
    FindAllInSphere: { args: { 0: 'Vector' } },
    FindByClassnameNearest: { args: { 1: 'Vector' } },
    FindByClassnameWithin: { args: { 2: 'Vector' } },
    FindByModelWithin: { args: { 2: 'Vector' } },
    FindByNameNearest: { args: { 1: 'Vector' } },
    FindByNameWithin: { args: { 2: 'Vector' } },
    FindInSphere: { args: { 1: 'Vector' } },
  },
  CEnvEntityMaker: {
    SpawnEntityAtLocation: { args: { 0: 'Vector' } },
  },
  CMarkupVolumeTagged: {
    HasTag: { args: { 0: 'string' } },
  },
  CTakeDamageInfo: {
    GetDamagePosition: { returns: 'Vector' },
    GetReportedPosition: { returns: 'Vector' },
    SetDamagePosition: { args: { 0: 'Vector' } },
    SetReportedPosition: { args: { 0: 'Vector' } },
  },
};
