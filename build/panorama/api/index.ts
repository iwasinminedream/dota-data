import { readDump } from '../../util';
import { PanoramaApiFunction, PanoramaApiFunctionArg, PanoramaApiInterface } from './types';

export { types as apiTypes } from './types';

function parseFunction(line: string): PanoramaApiFunction | null {
  // Match function definitions like:
  // Subscribe( pEventName: string, funcVal ): number;
  // GetAbsOrigin( nEntityIndex: number );
  // Time(): number;
  const funcMatch = line.match(/^\s*(\w+)\s*\(\s*(.*?)\s*\)(?:\s*:\s*(.+?))?;?$/);
  
  if (!funcMatch) return null;
  
  const [, name, argsStr, returns] = funcMatch;
  
  const args: PanoramaApiFunctionArg[] = [];
  if (argsStr.trim()) {
    // Split by comma but handle generic types like "args"
    const argParts = argsStr.split(/,\s*/);
    for (const argPart of argParts) {
      const argMatch = argPart.match(/(\w+)(?:\s*:\s*(.+))?/);
      if (argMatch) {
        args.push({
          name: argMatch[1],
          type: argMatch[2]?.trim(),
        });
      }
    }
  }
  
  return {
    name,
    args,
    returns: returns?.trim(),
  };
}

export function generatePanoramaApi(): PanoramaApiInterface[] {
  const dump = readDump('cl_panorama_typescript_declarations');
  
  const interfaces: PanoramaApiInterface[] = [];
  
  // Split by interface declarations
  const interfaceBlocks = dump.split(/(?=^interface\s+)/m);
  
  for (const block of interfaceBlocks) {
    if (!block.trim().startsWith('interface')) continue;
    
    // Extract interface name
    const nameMatch = block.match(/^interface\s+(\w+)/);
    if (!nameMatch) continue;
    
    const interfaceName = nameMatch[1];
    const members: PanoramaApiFunction[] = [];
    
    // Parse lines within the interface
    const lines = block.split('\n');
    let currentComment: string | undefined;
    
    for (const line of lines) {
      // Check for JSDoc comment
      const commentMatch = line.match(/\/\*\*\s*(.+?)\s*\*\//);
      if (commentMatch) {
        currentComment = commentMatch[1];
        continue;
      }
      
      // Parse function
      const func = parseFunction(line);
      if (func) {
        if (currentComment) {
          func.description = currentComment;
          currentComment = undefined;
        }
        members.push(func);
      }
    }
    
    if (members.length > 0) {
      interfaces.push({
        name: interfaceName,
        members,
      });
    }
  }
  
  return interfaces;
}
