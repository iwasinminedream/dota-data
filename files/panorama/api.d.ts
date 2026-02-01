declare namespace panoramaApi {
  export interface PanoramaApiFunction {
    name: string;
    description?: string;
    args: PanoramaApiFunctionArg[];
    returns?: string;
  }
  
  export interface PanoramaApiFunctionArg {
    name: string;
    type?: string;
  }
  
  export interface PanoramaApiInterface {
    name: string;
    description?: string;
    members: PanoramaApiFunction[];
  }
}

declare const panoramaApi: panoramaApi.PanoramaApiInterface[];
export = panoramaApi;
