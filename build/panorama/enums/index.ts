import fs from 'fs-extra';
import path from 'path';
import { readDump } from '../../util';
import { getEnumDescription } from '../../vscripts/api/data/modifier-properties';
import { Enum, EnumMember } from './types';

export { types as enumsTypes } from './types';

// ButtonCode_t is not part of the dump but is required by GameUI.IsKeyDown. It is maintained
// alongside this generator as a list of `<value> = "<name>"` lines (one button per line).
function parseButtonCodeEnum(): Enum {
  const dump = fs.readFileSync(path.join(__dirname, 'ButtonCode_t.txt'), 'utf8');
  const members: EnumMember[] = [];

  for (const line of dump.split(/\r?\n/)) {
    const member = line.match(/^\s*(-?\d+)\s*=\s*"(.+)"\s*$/);
    if (member) {
      members.push({ name: member[2], value: Number(member[1]) });
    }
  }

  return { name: 'ButtonCode_t', members };
}

export const enums = (() => {
  const result = readDump('cl_panorama_script_help *')
    .split(/\r?\n\r?\n/)
    .map((group): Enum => {
      const enumName = group.match(/declare enum (.+)([\s{]*)?/)![1];
      const members: EnumMember[] = [];

      let currentComment: string | undefined;

      for (const line of group.slice(group.indexOf('{')).split('\n')) {
        const comment = line.match(/\/\*\* (.+) \*\//);
        if (comment) {
          [, currentComment] = comment;
        }

        const member = line.match(/(\w+) = (-?\d+)/);
        if (member) {
          members.push({
            name: member[1],
            description: currentComment,
            value: Number(member[2]),
          });

          currentComment = undefined;
        }
      }

      return { name: enumName, members };
    });

  for (const member of result.find((x) => x.name === 'modifierfunction')!.members) {
    member.description = getEnumDescription(member.description);
  }

  result.push(parseButtonCodeEnum());

  return result;
})();
