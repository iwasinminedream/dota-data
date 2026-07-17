declare namespace events {
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
}

declare const events: Record<string, events.PanoramaEvent>;
export = events;
