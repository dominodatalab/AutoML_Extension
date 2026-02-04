import { useState, useCallback } from 'react'
import api from '../api'
import type {
  DataProfile,
  TargetSuggestion,
  QuickProfile,
  ColumnProfile,
  MetricsByProblemType,
  PresetsByModelType
} from '../types/profiling'

interface UseProfilingResult {
  profile: DataProfile | null
  quickProfile: QuickProfile | null
  suggestions: TargetSuggestion[]
  columnProfile: ColumnProfile | null
  metrics: MetricsByProblemType | null
  presets: PresetsByModelType | null
  loading: boolean
  error: string | null
  profileFile: (filePath: string, sampleSize?: number) => Promise<DataProfile | null>
  quickProfileFile: (filePath: string) => Promise<QuickProfile | null>
  suggestTarget: (filePath: string) => Promise<TargetSuggestion[]>
  profileColumn: (filePath: string, columnName: string) => Promise<ColumnProfile | null>
  fetchMetrics: () => Promise<MetricsByProblemType | null>
  fetchPresets: () => Promise<PresetsByModelType | null>
}

export function useProfiling(): UseProfilingResult {
  const [profile, setProfile] = useState<DataProfile | null>(null)
  const [quickProfile, setQuickProfile] = useState<QuickProfile | null>(null)
  const [suggestions, setSuggestions] = useState<TargetSuggestion[]>([])
  const [columnProfile, setColumnProfile] = useState<ColumnProfile | null>(null)
  const [metrics, setMetrics] = useState<MetricsByProblemType | null>(null)
  const [presets, setPresets] = useState<PresetsByModelType | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const profileFile = useCallback(async (filePath: string, sampleSize = 10000) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<DataProfile>('profile', {
        file_path: filePath,
        sample_size: sampleSize
      })
      setProfile(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to profile file'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const quickProfileFile = useCallback(async (filePath: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<QuickProfile>('profilequick', { file_path: filePath })
      setQuickProfile(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to quick profile file'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const suggestTarget = useCallback(async (filePath: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<{ suggestions: TargetSuggestion[] }>('suggesttarget', {
        file_path: filePath
      })
      setSuggestions(data.suggestions)
      return data.suggestions
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to suggest target'
      setError(message)
      return []
    } finally {
      setLoading(false)
    }
  }, [])

  const profileColumn = useCallback(async (filePath: string, columnName: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ColumnProfile>('profilecolumn', {
        file_path: filePath,
        column_name: columnName
      })
      setColumnProfile(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to profile column'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchMetrics = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get<MetricsByProblemType>('metrics')
      setMetrics(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch metrics'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchPresets = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.get<PresetsByModelType>('presets')
      setPresets(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to fetch presets'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  return {
    profile,
    quickProfile,
    suggestions,
    columnProfile,
    metrics,
    presets,
    loading,
    error,
    profileFile,
    quickProfileFile,
    suggestTarget,
    profileColumn,
    fetchMetrics,
    fetchPresets,
  }
}
