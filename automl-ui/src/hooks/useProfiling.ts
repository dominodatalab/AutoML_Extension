import { useState, useCallback } from 'react'
import api from '../api'
import { aggregateAsyncState, orArray, useApiState } from './asyncHelpers'
import { useAsyncOperation } from './useAsyncOperation'
import type {
  AsyncProfileStartRequest,
  AsyncProfileStartResponse,
  AsyncProfileStatusResponse,
  DataProfile,
  TargetSuggestion,
  QuickProfile,
  ColumnProfile,
  MetricsByProblemType,
  PresetsByModelType,
  TimeSeriesProfile,
} from '../types/profiling'

interface UseProfilingResult {
  profile: DataProfile | null
  quickProfile: QuickProfile | null
  suggestions: TargetSuggestion[]
  columnProfile: ColumnProfile | null
  metrics: MetricsByProblemType | null
  presets: PresetsByModelType | null
  tsProfile: TimeSeriesProfile | null
  tsLoading: boolean
  tsError: string | null
  loading: boolean
  error: string | null
  profileFile: (filePath: string, sampleSize?: number, samplingStrategy?: string, stratifyColumn?: string) => Promise<DataProfile | null>
  quickProfileFile: (filePath: string) => Promise<QuickProfile | null>
  suggestTarget: (filePath: string) => Promise<TargetSuggestion[]>
  profileColumn: (filePath: string, columnName: string) => Promise<ColumnProfile | null>
  fetchMetrics: () => Promise<MetricsByProblemType | null>
  fetchPresets: () => Promise<PresetsByModelType | null>
  profileTimeSeries: (request: AsyncProfileStartRequest) => Promise<TimeSeriesProfile | null>
  startAsyncProfile: (request: AsyncProfileStartRequest) => Promise<AsyncProfileStartResponse>
  getAsyncProfileStatus: (requestId: string) => Promise<AsyncProfileStatusResponse>
  setProfileData: (value: DataProfile | null) => void
  setTsProfileData: (value: TimeSeriesProfile | null) => void
}

export function useProfiling(): UseProfilingResult {
  const [suggestions, setSuggestions] = useState<TargetSuggestion[]>([])

  const profileState = useApiState(
    async (filePath: string, sampleSize = 50000, samplingStrategy = 'random', stratifyColumn?: string) => {
      const payload: Record<string, unknown> = {
        file_path: filePath,
        sample_size: sampleSize,
        sampling_strategy: samplingStrategy,
      }
      if (stratifyColumn) payload.stratify_column = stratifyColumn
      const { data } = await api.post<DataProfile>('profile', payload)
      return data
    },
    'Failed to profile file'
  )

  const quickProfileState = useApiState(
    async (filePath: string) => {
      const { data } = await api.post<QuickProfile>('profilequick', { file_path: filePath })
      return data
    },
    'Failed to quick profile file'
  )

  const suggestTargetOp = useAsyncOperation(
    async (filePath: string) => {
      const { data } = await api.post<{ suggestions: TargetSuggestion[] }>('suggesttarget', { file_path: filePath })
      setSuggestions(data.suggestions)
      return data.suggestions
    },
    { errorMessage: 'Failed to suggest target' }
  )

  const columnProfileState = useApiState(
    async (filePath: string, columnName: string) => {
      const { data } = await api.post<ColumnProfile>('profilecolumn', { file_path: filePath, column_name: columnName })
      return data
    },
    'Failed to profile column'
  )

  const metricsState = useApiState(
    async () => {
      const { data } = await api.get<MetricsByProblemType>('metrics')
      return data
    },
    'Failed to fetch metrics'
  )

  const presetsState = useApiState(
    async () => {
      const { data } = await api.get<PresetsByModelType>('presets')
      return data
    },
    'Failed to fetch presets'
  )

  const tsProfileState = useApiState(
    async (request: AsyncProfileStartRequest) => {
      const { data } = await api.post<TimeSeriesProfile>('profiletimeseries', request)
      return data
    },
    'Failed to profile time series'
  )

  const { loading, error } = aggregateAsyncState([
    profileState,
    quickProfileState,
    suggestTargetOp,
    columnProfileState,
    metricsState,
    presetsState,
  ])

  const suggestTarget = useCallback(async (filePath: string) => {
    return orArray(suggestTargetOp.execute(filePath))
  }, [suggestTargetOp.execute])

  const startAsyncProfile = useCallback(async (request: AsyncProfileStartRequest) => {
    const { data } = await api.post<AsyncProfileStartResponse>('profileasyncstart', request)
    return data
  }, [])

  const getAsyncProfileStatus = useCallback(async (requestId: string) => {
    const { data } = await api.post<AsyncProfileStatusResponse>('profileasyncstatus', { request_id: requestId })
    return data
  }, [])

  return {
    profile: profileState.data,
    quickProfile: quickProfileState.data,
    suggestions,
    columnProfile: columnProfileState.data,
    metrics: metricsState.data,
    presets: presetsState.data,
    tsProfile: tsProfileState.data,
    tsLoading: tsProfileState.loading,
    tsError: tsProfileState.error ?? null,
    loading,
    error,
    profileFile: profileState.execute,
    quickProfileFile: quickProfileState.execute,
    suggestTarget,
    profileColumn: columnProfileState.execute,
    fetchMetrics: metricsState.execute,
    fetchPresets: presetsState.execute,
    profileTimeSeries: tsProfileState.execute,
    startAsyncProfile,
    getAsyncProfileStatus,
    setProfileData: profileState.setData,
    setTsProfileData: tsProfileState.setData,
  }
}
