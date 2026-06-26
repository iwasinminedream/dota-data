import { PanoramaApiInterface } from './types';

export const override = (interfaces: PanoramaApiInterface[]) => {
  // GameUI.IsKeyDown takes a button code, which the dump only types as `number`.
  const isKeyDown = interfaces
    .find((x) => x.name === 'CDOTA_PanoramaScript_GameUI')
    ?.members.find((x) => x.name === 'IsKeyDown');
  if (isKeyDown?.args[0]) {
    isKeyDown.args[0].type = 'ButtonCode_t';
  }
};
