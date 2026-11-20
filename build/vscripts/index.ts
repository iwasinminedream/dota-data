import { outputFile, outputJson } from '../util';
import { apiDeclarations, apiTypes } from './api';
import { apiTypesDeclarations, apiTypesTypes } from './api-types';
import { generateEnumDeclarations, enumsTypes } from './enums';
import { applyTableKeys } from './table-keys';

export async function generateVScripts() {
  const api = apiDeclarations();
  outputJson('vscripts/api', api);
  outputFile('vscripts/api.d.ts', apiTypes);
  // the table keys server.dll reads (dumper/table_keys.json): undocumented ones join their types
  const tableKeys = applyTableKeys(api, apiTypesDeclarations);
  outputJson('vscripts/api-types', tableKeys.declarations);
  if (tableKeys.file) outputJson('vscripts/table_keys', tableKeys.file);
  outputFile('vscripts/api-types.d.ts', apiTypesTypes);
  const enumDeclarations = generateEnumDeclarations();
  outputJson('vscripts/enums', enumDeclarations.enumDeclarations);
  outputFile('vscripts/enums.d.ts', enumsTypes);

  return {
    enumDeclarations,
  };
}
