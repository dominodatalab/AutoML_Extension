import { useQuery, useMutation } from '@tanstack/react-query'
import api from '../api'
import { useStore } from '../store'
import { getErrorMessage } from '../utils/errors'

export interface LearningCurvesRequest {
  job_id: string
  model_type?: string
}

export interface LearningCurvesResponse {
  models?: Array<{
    model: string
    score_val: number
    fit_time: number
    pred_time_val?: number
  }>
  fit_summary?: string
  fit_summary_raw?: unknown
  training_history?: Record<string, unknown>
  chart?: string
  error?: string
}

export interface ExportFormat {
  supported: boolean
  description: string
  requirements?: string[]
}

export interface SupportedFormats {
  tabular: Record<string, ExportFormat>
  timeseries: Record<string, ExportFormat>
}

export function useLearningCurves(jobId: string, modelType?: string, enabled = true) {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['learningcurves', jobId, modelType],
    queryFn: async () => {
      try {
        const { data } = await api.post<LearningCurvesResponse>('export/learning-curves', {
          job_id: jobId,
          model_type: modelType,
        })
        if (data.error) {
          addNotification(data.error, 'error')
        }
        return data
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    enabled: enabled && !!jobId,
    staleTime: 5 * 60 * 1000,
    retry: false,
  })
}

export function useSupportedFormats() {
  const addNotification = useStore((state) => state.addNotification)

  return useQuery({
    queryKey: ['exportformats'],
    queryFn: async () => {
      try {
        const { data } = await api.get<SupportedFormats>('export/formats')
        return data
      } catch (error) {
        addNotification(getErrorMessage(error), 'error')
        throw error
      }
    },
    staleTime: 30 * 60 * 1000,
    retry: false,
  })
}

interface NotebookExportResponse {
  success: boolean
  filename: string
  notebook: Record<string, unknown>
}

export function useExportNotebook() {
  const addNotification = useStore((state) => state.addNotification)

  return useMutation({
    mutationFn: async (jobId: string) => {
      const { data } = await api.post<NotebookExportResponse>('export/notebook', {
        job_id: jobId,
      })
      return data
    },
    onError: (error) => {
      addNotification(getErrorMessage(error), 'error')
    },
  })
}
