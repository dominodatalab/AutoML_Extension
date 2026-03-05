import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import api from '../api'

export interface DeploymentPackageRequest {
  job_id: string
  model_type?: string
  output_dir: string
}

export interface DeploymentPackageResponse {
  success: boolean
  output_dir?: string
  files: string[]
  error?: string
}

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
  training_history?: Record<string, unknown>  // Legacy support
  chart?: string  // Deprecated
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

// Hook for creating deployment package
export function useExportDeployment() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (request: DeploymentPackageRequest) => {
      const { data } = await api.post<DeploymentPackageResponse>('exportdeployment', request)
      return data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['exports'] })
    },
  })
}

// Hook for getting learning curves using job_id
export function useLearningCurves(jobId: string, modelType?: string, enabled = true) {
  return useQuery({
    queryKey: ['learningcurves', jobId, modelType],
    queryFn: async () => {
      const { data } = await api.post<LearningCurvesResponse>('learningcurves', {
        job_id: jobId,
        model_type: modelType,
      })
      return data
    },
    enabled: enabled && !!jobId,
    staleTime: 5 * 60 * 1000,
  })
}


// Hook for getting supported export formats
export function useSupportedFormats() {
  return useQuery({
    queryKey: ['exportformats'],
    queryFn: async () => {
      const { data } = await api.get<SupportedFormats>('exportformats')
      return data
    },
    staleTime: 30 * 60 * 1000,
  })
}

// Hook for exporting notebook
interface NotebookExportResponse {
  success: boolean
  filename: string
  notebook: Record<string, unknown>
}

// Hook for downloading deployment package as zip (binary response)
export function useDownloadDeploymentPackage() {
  return useMutation({
    mutationFn: async (outputDir: string) => {
      // Build URL the same way the api client does (Domino compat)
      const { getBasePath } = await import('../utils/basePath')
      const basePath = getBasePath()
      const url = `${basePath}/svcexportdeploymentdownload`

      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ output_dir: outputDir }),
      })

      if (!response.ok) {
        const errText = await response.text().catch(() => response.statusText)
        throw new Error(errText || 'Download failed')
      }

      const blob = await response.blob()
      const disposition = response.headers.get('Content-Disposition') || ''
      const match = disposition.match(/filename="?([^"]+)"?/)
      const filename = match?.[1] || 'deployment_package.zip'

      return { blob, filename }
    },
  })
}

export function useExportNotebook() {
  return useMutation({
    mutationFn: async (jobId: string) => {
      const { data } = await api.post<NotebookExportResponse>('exportnotebook', {
        job_id: jobId,
      })
      return data
    },
  })
}
