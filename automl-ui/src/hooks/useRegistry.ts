import { useState, useCallback } from 'react'
import api from '../api'
import type {
  RegisteredModel,
  ModelVersion,
  RegisterModelResult,
  TransitionStageResult,
  ModelCard,
  ModelStage,
  ModelsByStage
} from '../types/registry'

interface UseRegistryResult {
  registeredModels: RegisteredModel[]
  modelVersions: ModelVersion[]
  modelsByStage: ModelsByStage | null
  modelCard: ModelCard | null
  loading: boolean
  error: string | null
  fetchRegisteredModels: () => Promise<RegisteredModel[]>
  fetchModelVersions: (modelName: string) => Promise<ModelVersion[]>
  registerModel: (
    modelPath: string,
    modelName: string,
    modelType: string,
    description?: string,
    metrics?: Record<string, number>,
    jobId?: string
  ) => Promise<RegisterModelResult | null>
  transitionStage: (
    modelName: string,
    version: string,
    stage: ModelStage,
    archiveExisting?: boolean
  ) => Promise<TransitionStageResult | null>
  updateDescription: (
    modelName: string,
    description: string,
    version?: string
  ) => Promise<boolean>
  deleteModelVersion: (modelName: string, version: string) => Promise<boolean>
  deleteModel: (modelName: string) => Promise<boolean>
  fetchModelCard: (modelName: string, version: string) => Promise<ModelCard | null>
  fetchModelsByStage: (modelName: string) => Promise<ModelsByStage | null>
  downloadModel: (modelName: string, version: string) => Promise<string | null>
}

export function useRegistry(): UseRegistryResult {
  const [registeredModels, setRegisteredModels] = useState<RegisteredModel[]>([])
  const [modelVersions, setModelVersions] = useState<ModelVersion[]>([])
  const [modelsByStage, setModelsByStage] = useState<ModelsByStage | null>(null)
  const [modelCard, setModelCard] = useState<ModelCard | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchRegisteredModels = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get<RegisteredModel[]>('registeredmodels')
      // Filter to only show models deployed from this application (prefixed with automlapp-)
      const filteredModels = data.filter(model => model.name.startsWith('automlapp-'))
      setRegisteredModels(filteredModels)
      return filteredModels
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch registered models'
      setError(message)
      return []
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchModelVersions = useCallback(async (modelName: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ModelVersion[]>('modelversions', { model_name: modelName })
      setModelVersions(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch model versions'
      setError(message)
      return []
    } finally {
      setLoading(false)
    }
  }, [])

  const registerModel = useCallback(async (
    modelPath: string,
    modelName: string,
    modelType: string,
    description?: string,
    metrics?: Record<string, number>,
    jobId?: string
  ) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<RegisterModelResult>('registermodel', {
        model_path: modelPath,
        model_name: modelName,
        model_type: modelType,
        description,
        metrics,
        job_id: jobId
      })
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to register model'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const transitionStage = useCallback(async (
    modelName: string,
    version: string,
    stage: ModelStage,
    archiveExisting = false
  ) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<TransitionStageResult>('transitionstage', {
        model_name: modelName,
        version,
        stage,
        archive_existing: archiveExisting
      })
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to transition model stage'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const updateDescription = useCallback(async (
    modelName: string,
    description: string,
    version?: string
  ) => {
    setLoading(true)
    setError(null)
    try {
      await api.post('updatedescription', {
        model_name: modelName,
        description,
        version
      })
      return true
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to update description'
      setError(message)
      return false
    } finally {
      setLoading(false)
    }
  }, [])

  const deleteModelVersion = useCallback(async (modelName: string, version: string) => {
    setLoading(true)
    setError(null)
    try {
      await api.post('deleteversion', {
        model_name: modelName,
        version
      })
      return true
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to delete model version'
      setError(message)
      return false
    } finally {
      setLoading(false)
    }
  }, [])

  const deleteModel = useCallback(async (modelName: string) => {
    setLoading(true)
    setError(null)
    try {
      await api.post('deletemodel', { model_name: modelName })
      return true
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to delete model'
      setError(message)
      return false
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchModelCard = useCallback(async (modelName: string, version: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ModelCard>('modelcard', {
        model_name: modelName,
        version,
        job_info: {},
        metrics: {}
      })
      setModelCard(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch model card'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchModelsByStage = useCallback(async (modelName: string) => {
    setLoading(true)
    setError(null)
    try {
      // Fetch all versions and organize by stage
      const versions = await fetchModelVersions(modelName)
      const byStage: ModelsByStage = {
        model_name: modelName,
        stages: {
          None: [],
          Staging: [],
          Production: [],
          Archived: []
        }
      }

      versions.forEach(v => {
        const stage = v.stage as ModelStage
        if (byStage.stages[stage]) {
          byStage.stages[stage].push(v)
        }
      })

      setModelsByStage(byStage)
      return byStage
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch models by stage'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [fetchModelVersions])

  const downloadModel = useCallback(async (modelName: string, version: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<{ local_path: string }>('downloadmodel', {
        model_name: modelName,
        version
      })
      return data.local_path
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to download model'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  return {
    registeredModels,
    modelVersions,
    modelsByStage,
    modelCard,
    loading,
    error,
    fetchRegisteredModels,
    fetchModelVersions,
    registerModel,
    transitionStage,
    updateDescription,
    deleteModelVersion,
    deleteModel,
    fetchModelCard,
    fetchModelsByStage,
    downloadModel,
  }
}
