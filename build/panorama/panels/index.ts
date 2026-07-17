import { tryReadDump } from '../../util';
import { PanoramaPanel } from './types';

export { types as panelsTypes } from './types';

// The `panorama_panels` section is a digest produced by the dumper from the
// output of `panorama_generate_layout_xsd`: every panel type usable in layout
// XML, its parent type, and the XML attributes the type itself declares
// (inherited attributes are found by walking `base`).
export function generatePanoramaPanels(): PanoramaPanel[] | undefined {
  const dump = tryReadDump('panorama_panels');
  if (dump === undefined) {
    console.warn('Dump has no "panorama_panels" section — skipping files/panorama/panels');
    return undefined;
  }

  return JSON.parse(dump);
}
