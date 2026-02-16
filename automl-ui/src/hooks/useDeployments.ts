import { useState, useCallback } from 'react'
import api from '../api'
import { useAsyncOperation } from './useAsyncOperation'
import type {
  Deployment,
  DeploymentResponse,
  DeploymentStatusResponse,
  DeploymentLogs,
  QuickDeployRequest,
  DeployFromJobRequest,
  ModelApi,
} from '../types/deployment'

interface UseDeploymentsResult {
  deployments: Deployment[]
  modelApis: ModelApi[]
  loading: boolean
  error: string | null
  fetchDeployments: () => Promise<Deployment[]>
  fetchModelApis: () => Promise<ModelApi[]>
  getDeployment: (deploymentId: string) => Promise<Deployment | null>
  getDeploymentStatus: (deploymentId: string) => Promise<DeploymentStatusResponse | null>
  startDeployment: (deploymentId: string) => Promise<DeploymentResponse | null>
  stopDeployment: (deploymentId: string) => Promise<DeploymentResponse | null>
  deleteDeployment: (deploymentId: string) => Promise<boolean>
  getDeploymentLogs: (deploymentId: string, logType?: string) => Promise<string | null>
  quickDeploy: (request: QuickDeployRequest) => Promise<DeploymentResponse | null>
  deployFromJob: (request: DeployFromJobRequest) => Promise<DeploymentResponse | null>
}

export function useDeployments(): UseDeploymentsResult {
  const [deployments, setDeployments] = useState<Deployment[]>([])
  const [modelApis, setModelApis] = useState<ModelApi[]>([])

  const fetchDeploymentsOp = useAsyncOperation(
    async () => {
      const { data } = await api.get<{ success: boolean; data: Deployment[]; error?: string; warning?: string }>('deployments')
      if (!data.success) {
        throw new Error(data.error || data.warning || 'Failed to fetch deployments')
      }
      const deploymentList = data.data || []
      setDeployments(deploymentList)
      return deploymentList
    },
    { errorMessage: 'Failed to fetch deployments' }
  )

  const fetchModelApisOp = useAsyncOperation(
    async () => {
      const { data } = await api.get<{ success: boolean; data: ModelApi[]; error?: string; warning?: string }>('modelapis')
      if (!data.success) {
        throw new Error(data.error || data.warning || 'Failed to fetch model APIs')
      }
      const apiList = data.data || []
      setModelApis(apiList)
      return apiList
    },
    { errorMessage: 'Failed to fetch model APIs' }
  )

  const getDeploymentOp = useAsyncOperation(
    async (deploymentId: string) => {
      const { data } = await api.post<{ success: boolean; data: Deployment }>('deploymentget', {
        deployment_id: deploymentId
      })
      return data.data || null
    },
    { errorMessage: 'Failed to get deployment' }
  )

  const getDeploymentStatusOp = useAsyncOperation(
    async (deploymentId: string) => {
      const { data } = await api.post<DeploymentStatusResponse>('deploymentstatus', {
        deployment_id: deploymentId
      })
      return data
    },
    { errorMessage: 'Failed to get deployment status' }
  )

  const startDeploymentOp = useAsyncOperation(
    async (deploymentId: string, refreshFn: () => Promise<Deployment[]>) => {
      const { data } = await api.post<DeploymentResponse>('deploymentstart', {
        deployment_id: deploymentId
      })
      // Refresh deployments list
      await refreshFn()
      return data
    },
    { errorMessage: 'Failed to start deployment' }
  )

  const stopDeploymentOp = useAsyncOperation(
    async (deploymentId: string, refreshFn: () => Promise<Deployment[]>) => {
      const { data } = await api.post<DeploymentResponse>('deploymentstop', {
        deployment_id: deploymentId
      })
      // Refresh deployments list
      await refreshFn()
      return data
    },
    { errorMessage: 'Failed to stop deployment' }
  )

  const deleteDeploymentOp = useAsyncOperation(
    async (deploymentId: string, refreshFn: () => Promise<Deployment[]>) => {
      await api.post('deploymentdelete', { deployment_id: deploymentId })
      // Refresh deployments list
      await refreshFn()
      return true as const
    },
    { errorMessage: 'Failed to delete deployment' }
  )

  const getDeploymentLogsOp = useAsyncOperation(
    async (deploymentId: string, logType = 'stdout') => {
      const { data } = await api.post<DeploymentLogs>('deploymentlogs', {
        deployment_id: deploymentId,
        log_type: logType
      })
      return data.logs || null
    },
    { errorMessage: 'Failed to get deployment logs' }
  )

  const quickDeployOp = useAsyncOperation(
    async (request: QuickDeployRequest, refreshFn: () => Promise<Deployment[]>) => {
      const { data } = await api.post<DeploymentResponse>('quickdeploy', request)
      // Refresh deployments list
      await refreshFn()
      return data
    },
    { errorMessage: 'Failed to deploy model' }
  )

  const deployFromJobOp = useAsyncOperation(
    async (request: DeployFromJobRequest, refreshFn: () => Promise<Deployment[]>) => {
      const { data } = await api.post<DeploymentResponse>('deployfromjob', request)
      // Refresh deployments list
      await refreshFn()
      return data
    },
    { errorMessage: 'Failed to deploy from job' }
  )

  // Derive combined loading/error from all operations
  const loading = fetchDeploymentsOp.loading || fetchModelApisOp.loading ||
    getDeploymentOp.loading || getDeploymentStatusOp.loading || startDeploymentOp.loading ||
    stopDeploymentOp.loading || deleteDeploymentOp.loading || getDeploymentLogsOp.loading ||
    quickDeployOp.loading || deployFromJobOp.loading
  const error = fetchDeploymentsOp.error ?? fetchModelApisOp.error ??
    getDeploymentOp.error ?? getDeploymentStatusOp.error ?? startDeploymentOp.error ??
    stopDeploymentOp.error ?? deleteDeploymentOp.error ?? getDeploymentLogsOp.error ??
    quickDeployOp.error ?? deployFromJobOp.error ?? null

  // Wrap execute calls to preserve the original return-type contracts
  const fetchDeployments = useCallback(async () => {
    const result = await fetchDeploymentsOp.execute()
    return result ?? []
  }, [fetchDeploymentsOp.execute])

  const fetchModelApis = useCallback(async () => {
    const result = await fetchModelApisOp.execute()
    return result ?? []
  }, [fetchModelApisOp.execute])

  const getDeployment = useCallback(async (deploymentId: string) => {
    const result = await getDeploymentOp.execute(deploymentId)
    return result ?? null
  }, [getDeploymentOp.execute])

  const getDeploymentStatus = useCallback(async (deploymentId: string) => {
    const result = await getDeploymentStatusOp.execute(deploymentId)
    return result ?? null
  }, [getDeploymentStatusOp.execute])

  const startDeployment = useCallback(async (deploymentId: string) => {
    const result = await startDeploymentOp.execute(deploymentId, fetchDeployments)
    return result ?? null
  }, [startDeploymentOp.execute, fetchDeployments])

  const stopDeployment = useCallback(async (deploymentId: string) => {
    const result = await stopDeploymentOp.execute(deploymentId, fetchDeployments)
    return result ?? null
  }, [stopDeploymentOp.execute, fetchDeployments])

  const deleteDeployment = useCallback(async (deploymentId: string) => {
    const result = await deleteDeploymentOp.execute(deploymentId, fetchDeployments)
    return result ?? false
  }, [deleteDeploymentOp.execute, fetchDeployments])

  const getDeploymentLogs = useCallback(async (deploymentId: string, logType?: string) => {
    const result = await getDeploymentLogsOp.execute(deploymentId, logType ?? 'stdout')
    return result ?? null
  }, [getDeploymentLogsOp.execute])

  const quickDeploy = useCallback(async (request: QuickDeployRequest) => {
    const result = await quickDeployOp.execute(request, fetchDeployments)
    return result ?? null
  }, [quickDeployOp.execute, fetchDeployments])

  const deployFromJob = useCallback(async (request: DeployFromJobRequest) => {
    const result = await deployFromJobOp.execute(request, fetchDeployments)
    return result ?? null
  }, [deployFromJobOp.execute, fetchDeployments])

  return {
    deployments,
    modelApis,
    loading,
    error,
    fetchDeployments,
    fetchModelApis,
    getDeployment,
    getDeploymentStatus,
    startDeployment,
    stopDeployment,
    deleteDeployment,
    getDeploymentLogs,
    quickDeploy,
    deployFromJob,
  }
}
