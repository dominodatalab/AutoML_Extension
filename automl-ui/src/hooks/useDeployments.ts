import { useState, useCallback } from 'react'
import api from '../api'
import { getErrorMessage } from '../utils/errors'
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
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchDeployments = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get<{ success: boolean; data: Deployment[]; error?: string; warning?: string }>('deployments')
      const deploymentList = data.data || []
      setDeployments(deploymentList)
      return deploymentList
    } catch (err) {
      setError(getErrorMessage(err) || 'Failed to fetch deployments')
      return []
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchModelApis = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get<{ success: boolean; data: ModelApi[] }>('modelapis')
      const apiList = data.data || []
      setModelApis(apiList)
      return apiList
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to fetch model APIs'
      setError(message)
      return []
    } finally {
      setLoading(false)
    }
  }, [])

  const getDeployment = useCallback(async (deploymentId: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<{ success: boolean; data: Deployment }>('deploymentget', {
        deployment_id: deploymentId
      })
      return data.data || null
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to get deployment'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getDeploymentStatus = useCallback(async (deploymentId: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentStatusResponse>('deploymentstatus', {
        deployment_id: deploymentId
      })
      return data
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to get deployment status'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const startDeployment = useCallback(async (deploymentId: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentResponse>('deploymentstart', {
        deployment_id: deploymentId
      })
      // Refresh deployments list
      await fetchDeployments()
      return data
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to start deployment'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [fetchDeployments])

  const stopDeployment = useCallback(async (deploymentId: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentResponse>('deploymentstop', {
        deployment_id: deploymentId
      })
      // Refresh deployments list
      await fetchDeployments()
      return data
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to stop deployment'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [fetchDeployments])

  const deleteDeployment = useCallback(async (deploymentId: string) => {
    setLoading(true)
    setError(null)
    try {
      await api.post('deploymentdelete', { deployment_id: deploymentId })
      // Refresh deployments list
      await fetchDeployments()
      return true
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to delete deployment'
      setError(message)
      return false
    } finally {
      setLoading(false)
    }
  }, [fetchDeployments])

  const getDeploymentLogs = useCallback(async (deploymentId: string, logType = 'stdout') => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentLogs>('deploymentlogs', {
        deployment_id: deploymentId,
        log_type: logType
      })
      return data.logs || null
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to get deployment logs'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const quickDeploy = useCallback(async (request: QuickDeployRequest) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentResponse>('quickdeploy', request)
      // Refresh deployments list
      await fetchDeployments()
      return data
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to deploy model'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [fetchDeployments])

  const deployFromJob = useCallback(async (request: DeployFromJobRequest) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DeploymentResponse>('deployfromjob', request)
      // Refresh deployments list
      await fetchDeployments()
      return data
    } catch (err) {
      const message = getErrorMessage(err) || 'Failed to deploy from job'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [fetchDeployments])

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
