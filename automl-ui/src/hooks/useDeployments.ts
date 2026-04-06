import { useState, useCallback } from 'react'
import api from '../api'
import { useAsyncOperation } from './useAsyncOperation'
import { aggregateAsyncState, orArray, orNull } from './asyncHelpers'
import type {
  Deployment,
  DeploymentResponse,
  DeployFromJobRequest,
} from '../types/deployment'

interface UseDeploymentsResult {
  deployments: Deployment[]
  loading: boolean
  error: string | null
  fetchDeploymentsByModelApi: (modelApiId: string) => Promise<Deployment[]>
  deployFromJob: (request: DeployFromJobRequest) => Promise<DeploymentResponse | null>
}

export function useDeployments(): UseDeploymentsResult {
  const [deployments, setDeployments] = useState<Deployment[]>([])

  const fetchDeploymentsByModelApiOp = useAsyncOperation(
    async (modelApiId: string) => {
      const { data } = await api.get<{ success: boolean; data: Deployment[]; error?: string }>(`deployments/deployments?model_api_id=${modelApiId}`)
      if (!data.success) {
        throw new Error(data.error || 'Failed to fetch deployments')
      }
      const deploymentList = data.data || []
      setDeployments(deploymentList)
      return deploymentList
    },
    { errorMessage: 'Failed to fetch deployments' }
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
    fetchDeploymentsByModelApiOp,
    deployFromJobOp,
  ])

  const fetchDeploymentsByModelApi = useCallback(async (modelApiId: string) => {
    return orArray(fetchDeploymentsByModelApiOp.execute(modelApiId))
  }, [fetchDeploymentsByModelApiOp.execute])

  const deployFromJob = useCallback(async (request: DeployFromJobRequest) => {
    return orNull(deployFromJobOp.execute(request))
  }, [deployFromJobOp.execute])

  return {
    deployments,
    loading,
    error,
    fetchDeploymentsByModelApi,
    deployFromJob,
  }
}
