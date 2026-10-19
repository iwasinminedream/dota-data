/*
 * Panel declarations phase helpers: the layout XSD digest and the per-type interface capture.
 */

// The panel declarations phase is driven from here (not from the addon SCRIPT)
// because the list of panel types is only known after the dump has produced the
// layout XSD — we parse it, then ask Dota for per-type TypeScript declarations.
export interface PanelAttribute {
  name: string;
  description?: string;
}

export interface PanelInfo {
  name: string;
  base?: string;
  attributes: PanelAttribute[];
}

function decodeXmlEntities(text: string): string {
  return text
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&amp;/g, '&');
}

// The XSD lists every panel type as a complexType with all attributes flattened
// down the inheritance chain; each attribute's documentation records the class
// that declared it ("(from X)") and the type header records the parent
// ("derived from X"). Keeping only the attributes declared by the type itself
// loses nothing — the full set is rebuilt by walking `base`.
export function parseLayoutXsd(xsd: string): PanelInfo[] {
  const panels: PanelInfo[] = [];
  const blocks = xsd.split(/(?=<xs:complexType name=")/).slice(1);
  for (const block of blocks) {
    const typeMatch = block.match(/^<xs:complexType name="([\w.-]+)Type"/);
    if (!typeMatch) continue;
    const header = block.match(/&lt;b&gt;([\w.-]+)&lt;\/b&gt;(?: \(derived from ([\w.-]+)\))?/);
    const name = header?.[1] ?? typeMatch[1];
    if (name.startsWith('Internal_')) continue;

    const attributes: PanelAttribute[] = [];
    const seen = new Set<string>();
    for (const attr of block.matchAll(
      /<xs:attribute name="([\w.-]+)"[^>]*>\s*<xs:annotation><xs:documentation[^>]*>&lt;b&gt;[\w.-]+&lt;\/b&gt; \(from ([\w.-]+)\)&lt;br \/&gt;&lt;br \/&gt;([^<]*)</g,
    )) {
      const [, attrName, from, rawDescription] = attr;
      if (from !== name || seen.has(attrName)) continue;
      seen.add(attrName);
      const description = decodeXmlEntities(rawDescription.trim());
      attributes.push(description ? { name: attrName, description } : { name: attrName });
    }
    attributes.sort((a, b) => (a.name < b.name ? -1 : 1));

    const base = header?.[2];
    panels.push(base ? { name, base, attributes } : { name, attributes });
  }
  panels.sort((a, b) => (a.name < b.name ? -1 : 1));
  return panels;
}

// Split captured `cl_panorama_typescript_declarations <type>` output into
// interface blocks. Tolerates unrelated console lines between blocks.
export function extractInterfaces(text: string): Map<string, string[]> {
  const result = new Map<string, string[]>();
  const lines = text.split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const match = lines[i].match(/^interface ([\w$]+)$/);
    if (!match || lines[i + 1]?.trim() !== '{') continue;
    const body: string[] = [];
    let j = i + 2;
    while (j < lines.length && lines[j].trim() !== '}') {
      body.push(lines[j].trim());
      j++;
    }
    result.set(match[1], body);
    i = j;
  }
  return result;
}
