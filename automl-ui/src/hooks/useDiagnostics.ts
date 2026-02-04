import { useState, useCallback } from 'react'
import api from '../api'
import type {
  FeatureImportanceResult,
  ConfusionMatrixResult,
  ROCCurveResult,
  PrecisionRecallResult,
  RegressionDiagnosticsResult,
  LeaderboardResult,
  PredictionResult,
  BatchPredictionResult,
  ModelInfo
} from '../types/diagnostics'

interface UseDiagnosticsResult {
  featureImportance: FeatureImportanceResult | null
  confusionMatrix: ConfusionMatrixResult | null
  rocCurve: ROCCurveResult | null
  precisionRecall: PrecisionRecallResult | null
  regressionDiagnostics: RegressionDiagnosticsResult | null
  leaderboard: LeaderboardResult | null
  modelInfo: ModelInfo | null
  predictions: PredictionResult | null
  loading: boolean
  error: string | null
  // Reset function to clear cached data when switching jobs
  reset: () => void
  // Updated to use job_id instead of model_path
  getFeatureImportance: (jobId: string, modelType?: string) => Promise<FeatureImportanceResult | null>
  getConfusionMatrix: (jobId: string, modelType?: string) => Promise<ConfusionMatrixResult | null>
  getROCCurve: (jobId: string, modelType?: string) => Promise<ROCCurveResult | null>
  getPrecisionRecall: (jobId: string, modelType?: string) => Promise<PrecisionRecallResult | null>
  getRegressionDiagnostics: (jobId: string, modelType?: string) => Promise<RegressionDiagnosticsResult | null>
  getLeaderboard: (jobId: string, modelType?: string) => Promise<LeaderboardResult | null>
  getModelInfo: (modelId: string, modelType: string) => Promise<ModelInfo | null>
  predict: (modelId: string, modelType: string, data: Record<string, unknown>[], returnProbs?: boolean) => Promise<PredictionResult | null>
  batchPredict: (modelId: string, modelType: string, inputFile: string, outputFile: string) => Promise<BatchPredictionResult | null>
}

export function useDiagnostics(): UseDiagnosticsResult {
  const [featureImportance, setFeatureImportance] = useState<FeatureImportanceResult | null>(null)
  const [confusionMatrix, setConfusionMatrix] = useState<ConfusionMatrixResult | null>(null)
  const [rocCurve, setROCCurve] = useState<ROCCurveResult | null>(null)
  const [precisionRecall, setPrecisionRecall] = useState<PrecisionRecallResult | null>(null)
  const [regressionDiagnostics, setRegressionDiagnostics] = useState<RegressionDiagnosticsResult | null>(null)
  const [leaderboard, setLeaderboard] = useState<LeaderboardResult | null>(null)
  const [modelInfo, setModelInfo] = useState<ModelInfo | null>(null)
  const [predictions, setPredictions] = useState<PredictionResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Reset all cached data - call when switching jobs
  const reset = useCallback(() => {
    setFeatureImportance(null)
    setConfusionMatrix(null)
    setROCCurve(null)
    setPrecisionRecall(null)
    setRegressionDiagnostics(null)
    setLeaderboard(null)
    setModelInfo(null)
    setPredictions(null)
    setError(null)
  }, [])

  const getFeatureImportance = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<FeatureImportanceResult>('featureimportance', {
        job_id: jobId,
        model_type: modelType
      })
      setFeatureImportance(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get feature importance'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getConfusionMatrix = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ConfusionMatrixResult>('confusionmatrix', {
        job_id: jobId,
        model_type: modelType
      })
      setConfusionMatrix(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get confusion matrix'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getROCCurve = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ROCCurveResult>('roccurve', {
        job_id: jobId,
        model_type: modelType
      })
      setROCCurve(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get ROC curve'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getPrecisionRecall = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<PrecisionRecallResult>('precisionrecall', {
        job_id: jobId,
        model_type: modelType
      })
      setPrecisionRecall(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get precision-recall curve'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getRegressionDiagnostics = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<RegressionDiagnosticsResult>('regressiondiagnostics', {
        job_id: jobId,
        model_type: modelType
      })
      setRegressionDiagnostics(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get regression diagnostics'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getLeaderboard = useCallback(async (jobId: string, modelType?: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<LeaderboardResult>('leaderboard', {
        job_id: jobId,
        model_type: modelType
      })
      setLeaderboard(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get leaderboard'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const getModelInfo = useCallback(async (modelId: string, modelType: string) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<ModelInfo>('modelinfo', {
        model_id: modelId,
        model_type: modelType
      })
      setModelInfo(data)
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to get model info'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const predict = useCallback(async (
    modelId: string,
    modelType: string,
    data: Record<string, unknown>[],
    returnProbs = false
  ) => {
    setLoading(true)
    setError(null)
    try {
      const { data: result } = await api.post<PredictionResult>('predict', {
        model_id: modelId,
        model_type: modelType,
        data,
        return_probabilities: returnProbs
      })
      setPredictions(result)
      return result
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to make predictions'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  const batchPredict = useCallback(async (
    modelId: string,
    modelType: string,
    inputFile: string,
    outputFile: string
  ) => {
    setLoading(true)
    setError(null)
    try {
      const { data } = await api.post<BatchPredictionResult>('predictbatch', {
        model_id: modelId,
        model_type: modelType,
        input_file: inputFile,
        output_file: outputFile
      })
      return data
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Failed to run batch predictions'
      setError(message)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  return {
    featureImportance,
    confusionMatrix,
    rocCurve,
    precisionRecall,
    regressionDiagnostics,
    leaderboard,
    modelInfo,
    predictions,
    loading,
    error,
    reset,
    getFeatureImportance,
    getConfusionMatrix,
    getROCCurve,
    getPrecisionRecall,
    getRegressionDiagnostics,
    getLeaderboard,
    getModelInfo,
    predict,
    batchPredict,
  }
}
