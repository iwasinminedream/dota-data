declare namespace panoramaPanels {
  export interface PanoramaPanelAttribute {
    name: string;
    description?: string;
  }
  
  export interface PanoramaPanel {
    name: string;
    /**
     * Name of the panel type this type derives from.
     * Attributes of base types also apply to this type.
     */
    base?: string;
    /** XML attributes declared by this panel type itself. */
    attributes: PanoramaPanelAttribute[];
  }
}

declare const panoramaPanels: panoramaPanels.PanoramaPanel[];
export = panoramaPanels;
