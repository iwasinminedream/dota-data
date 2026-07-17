import { outputFile, outputJson } from '../util';
import { apiTypes, generatePanoramaApi } from './api';
import { cssTypes, generateCss } from './css';
import { enums, enumsTypes } from './enums';
import { generatePanoramaEvents, panoramaEventsTypes } from './events';
import { generatePanoramaPanels, panelsTypes } from './panels';

export function generatePanorama() {
  outputJson('panorama/api', generatePanoramaApi());
  outputFile('panorama/api.d.ts', apiTypes);
  outputJson('panorama/css', generateCss());
  outputFile('panorama/css.d.ts', cssTypes);
  outputJson('panorama/enums', enums);
  outputFile('panorama/enums.d.ts', enumsTypes);
  outputJson('panorama/events', generatePanoramaEvents());
  outputFile('panorama/events.d.ts', panoramaEventsTypes);

  const panels = generatePanoramaPanels();
  if (panels !== undefined) {
    outputJson('panorama/panels', panels);
    outputFile('panorama/panels.d.ts', panelsTypes);
  }
}
