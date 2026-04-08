import { useState, useCallback } from 'react'
import api from '../api'
import { useAsyncOperation } from './useAsyncOperation'
import { aggregateAsyncState, orNull } from './asyncHelpers'
import type {
  DeploymentResponse,
  DeployFromJobRequest,
} from '../types/deployment'

interface ModelApiStatus {
  status: string
  isPending: boolean
}

interface UseDeploymentsResult {
  modelApiStatus: ModelApiStatus | null
  loading: boolean
  error: string | null
  fetchModelApiStatus: (modelApiId: string) => Promise<ModelApiStatus | null>
  deployFromJob: (request: DeployFromJobRequest) => Promise<DeploymentResponse | null>
}

export function useDeployments(): UseDeploymentsResult {
  const [modelApiStatus, setModelApiStatus] = useState<ModelApiStatus | null>(null)

  const fetchModelApiStatusOp = useAsyncOperation(
    async (modelApiId: string) => {
      const { data } = await api.get<{ success: boolean; status?: string; isPending?: boolean; error?: string }>(`deployments/model-api/${modelApiId}/status`)
      if (!data.success) {
        throw new Error(data.error || 'Failed to fetch model API status')
      }
      const statusData: ModelApiStatus = {
        status: data.status || 'unknown',
        isPending: data.isPending || false,
      }
      setModelApiStatus(statusData)
      return statusData
    },
    { errorMessage: 'Failed to fetch model API status' }
  )

  const deployFromJobOp = useAsyncOperation(
    async (request: DeployFromJobRequest) => {
      const { data } = await api.post<DeploymentResponse>(`deployments/deploy-from-job/${request.job_id}`, {
        model_name: request.model_name,
        replicas: request.replicas,
      })
      return data
    },
    { errorMessage: 'Failed to deploy from job' }
  )

  const { loading, error } = aggregateAsyncState([
    fetchModelApiStatusOp,
    deployFromJobOp,
  ])

  const fetchModelApiStatus = useCallback(async (modelApiId: string) => {
    return orNull(fetchModelApiStatusOp.execute(modelApiId))
  }, [fetchModelApiStatusOp.execute])

  const deployFromJob = useCallback(async (request: DeployFromJobRequest) => {
    return orNull(deployFromJobOp.execute(request))
  }, [deployFromJobOp.execute])

  return {
    modelApiStatus,
    loading,
    error,
    fetchModelApiStatus,
    deployFromJob,
  }
}
