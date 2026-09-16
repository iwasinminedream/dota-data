import * as s from '../../src/schema-builder';
import { deserialize, isDuplicateKeyArray, isKvObject, KVObject } from 'valve-kv';
import got from 'got';

export interface CreateIntegrationTestOptions {
  name: string;
  schema: s.RootSchema;
  url: string;
  ignore?: string[];
}

export function createIntegrationTest({
  name,
  url,
  schema,
  ignore = [],
}: CreateIntegrationTestOptions) {
  test(
    name,
    async () => {
      const content = await fetchRoot(url);
      delete content.Version;
      parseNumbersRecursive(content);
      const duplicates = ignoreDuplicates(content);

      // eslint-disable-next-line no-void
      void duplicates;
      // Uncomment to print out duplicate keys:
      // if (duplicates.length > 0) {
      //   const filteredDuplicates = duplicates.filter(
      //     (d) => !d.includes('.Bot.Loadout.') && !d.includes('.AbilityPreview.'),
      //   );

      //   const filePath = url.split('pak01_dir/')[1] ?? url.split('master')[1];
      //   console.log(`Found duplicate keys in: ${filePath}\n\n${filteredDuplicates.join('\n')}`);
      // }

      const validationResult = schema.validateRoot(content);
      expect(validationResult).toEqual(
        [...ignore].sort((a, b) => validationResult.indexOf(a) - validationResult.indexOf(b)),
      );
      // npc_heroes.txt pulls in one file per hero, so this downloads well over a hundred of them.
    },
    60_000,
  );
}

const getFirstRoot = (object: KVObject): KVObject =>
  (object[Object.keys(object)[0]] as KVObject) ?? {};

const baseIncludeRegex = /^[^\S\n]*#base[^\S\n]*"([^"]*)"[^\S\n]*$/gm;

// Since 6933 npc_heroes.txt holds nothing but `#base` includes, one per hero file.
// valve-kv only resolves those in deserializeFile, so follow them over http instead
// and merge every included root into the one of the file that pulled it in.
async function fetchRoot(url: string): Promise<KVObject> {
  const { body } = await got(url);
  const root = getFirstRoot(deserialize(body.replace(baseIncludeRegex, '')));

  // Fetched in parallel, merged in include order so later files keep overriding earlier ones.
  const includes = [...body.matchAll(baseIncludeRegex)].map(([, include]) =>
    fetchRoot(new URL(include.replace(/\\/g, '/'), url).href),
  );
  for (const included of await Promise.all(includes)) Object.assign(root, included);

  return root;
}

function parseNumbersRecursive(object: KVObject) {
  for (const [key, value] of Object.entries(object)) {
    if (typeof value === 'string' && value.length > 0) {
      const numberValue = Number(value);
      if (!Number.isNaN(numberValue)) {
        object[key] = numberValue;
      }
    } else if (isKvObject(value)) {
      parseNumbersRecursive(value);
    }
  }
}

function ignoreDuplicates(object: KVObject, path?: string): string[] {
  const duplicates = [];
  for (const [key, value] of Object.entries(object)) {
    const keyPath = path ? `${path}.${key}` : key;
    if (Array.isArray(value) && isDuplicateKeyArray(value)) {
      duplicates.push(keyPath);
      const newValue = value[value.length - 1];
      object[key] = newValue;
      if (isKvObject(newValue)) {
        ignoreDuplicates(newValue, keyPath);
      }
    } else if (isKvObject(value)) {
      duplicates.push(...ignoreDuplicates(value, keyPath));
    }
  }

  return duplicates;
}
