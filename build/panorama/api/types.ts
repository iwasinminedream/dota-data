import { exportNamespacedRoot } from '../../util';

// EXPORT START
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
// EXPORT END

export const types = exportNamespacedRoot(
  __filename,
  'panoramaApi',
  'panoramaApi.PanoramaApiInterface[]',
);
