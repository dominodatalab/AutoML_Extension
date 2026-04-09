import { useCallback } from 'react'
import api from '../api'
import { useAsyncOperation } from './useAsyncOperation'
import type { RegisterModelResult } from '../types/registry'

interface UseRegistryResult {
  loading: boolean
  error: string | null
  registerModel: (
    jobId: string,
    modelName: string,
    description?: string
  ) => Promise<RegisterModelResult | null>
}

export function useRegistry(): UseRegistryResult {
  const registerModelOp = useAsyncOperation(
    async (
      jobId: string,
      modelName: string,
      description?: string,
    ) => {
      const { data } = await api.post<RegisterModelResult>('registry/register', {
        job_id: jobId,
        model_name: modelName,
        description,
      })
      return data
    },
    { errorMessage: 'Failed to register model' }
  )

  const registerModel = useCallback(async (
    jobId: string,
    modelName: string,
    description?: string,
  ) => {
    const result = await registerModelOp.execute(jobId, modelName, description)
    return result ?? null
  }, [registerModelOp.execute])

  return {
    loading: registerModelOp.loading,
    error: registerModelOp.error,
    registerModel,
  }
}
