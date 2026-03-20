import { useQuery } from '@tanstack/react-query'
import api from '../api'

interface BackendCapabilities {
  standalone_mode: boolean
  domino_jobs: boolean
  mlflow_tracking: boolean
  model_registry: boolean
  model_deployment: boolean
  storage_cleanup: boolean
}

export interface Capabilities {
  /** True when Domino features should be shown in the UI. */
  dominoEnabled: boolean
  dominoJobs: boolean
  mlflowTracking: boolean
  modelRegistry: boolean
  modelDeployment: boolean
  storageCleanup: boolean
}

function readEnableDominoParam(): boolean {
  const params = new URLSearchParams(window.location.search)
  return params.get('enableDomino') !== 'false'
}

const STANDALONE: Capabilities = {
  dominoEnabled: false,
  dominoJobs: false,
  mlflowTracking: false,
  modelRegistry: false,
  modelDeployment: false,
  storageCleanup: false,
}

export function useCapabilities(): Capabilities {
  const enableDomino = readEnableDominoParam()

  const { data } = useQuery({
    queryKey: ['capabilities'],
    queryFn: async () => {
      const { data } = await api.get<BackendCapabilities>('capabilities')
      return data
    },
    staleTime: Infinity,
    refetchOnMount: false,
    refetchOnWindowFocus: false,
  })

  // Domino features require BOTH the URL opt-in AND backend availability
  if (!enableDomino || !data || data.standalone_mode) {
    return STANDALONE
  }

  return {
    dominoEnabled: true,
    dominoJobs: data.domino_jobs,
    mlflowTracking: data.mlflow_tracking,
    modelRegistry: data.model_registry,
    modelDeployment: data.model_deployment,
    storageCleanup: Boolean(data.storage_cleanup),
  }
}
