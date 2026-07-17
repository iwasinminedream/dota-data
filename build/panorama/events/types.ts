import { exportNamespacedRoot } from '../../util';

// EXPORT START
export interface PanoramaEvent {
  description: string;
  panelEvent: boolean;
  args: PanoramaEventArgument[];
  /** Real usage of this event quoted from Valve's UI code. */
  example?: string;
  /** Path of the Valve layout/script file the example is quoted from. */
  exampleSource?: string;
}

export interface PanoramaEventArgument {
  name?: string;
  type: string;
}
// EXPORT END

export const types = exportNamespacedRoot(
  __filename,
  'events',
  'Record<string, events.PanoramaEvent>',
);
