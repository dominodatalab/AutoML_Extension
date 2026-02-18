import { useCallback } from 'react'
import api from '../api'
import { aggregateAsyncState, useApiState } from './asyncHelpers'
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
  reset: () => void
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
  const featureImportanceState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<FeatureImportanceResult>('featureimportance', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get feature importance'
  )

  const confusionMatrixState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<ConfusionMatrixResult>('confusionmatrix', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get confusion matrix'
  )

  const rocCurveState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<ROCCurveResult>('roccurve', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get ROC curve'
  )

  const precisionRecallState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<PrecisionRecallResult>('precisionrecall', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get precision-recall curve'
  )

  const regressionDiagnosticsState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<RegressionDiagnosticsResult>('regressiondiagnostics', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get regression diagnostics'
  )

  const leaderboardState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<LeaderboardResult>('leaderboard', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get leaderboard'
  )

  const modelInfoState = useApiState(
    async (modelId: string, modelType: string) => {
      const { data } = await api.post<ModelInfo>('modelinfo', { model_id: modelId, model_type: modelType })
      return data
    },
    'Failed to get model info'
  )

  const predictState = useApiState(
    async (modelId: string, modelType: string, inputData: Record<string, unknown>[], returnProbs = false) => {
      const { data } = await api.post<PredictionResult>('predict', {
        model_id: modelId,
        model_type: modelType,
        data: inputData,
        return_probabilities: returnProbs
      })
      return data
    },
    'Failed to make predictions'
  )

  const batchPredictState = useApiState(
    async (modelId: string, modelType: string, inputFile: string, outputFile: string) => {
      const { data } = await api.post<BatchPredictionResult>('predictbatch', {
        model_id: modelId,
        model_type: modelType,
        input_file: inputFile,
        output_file: outputFile
      })
      return data
    },
    'Failed to run batch predictions'
  )

  const allStates = [
    featureImportanceState,
    confusionMatrixState,
    rocCurveState,
    precisionRecallState,
    regressionDiagnosticsState,
    leaderboardState,
    modelInfoState,
    predictState,
    batchPredictState,
  ]
  const { loading, error } = aggregateAsyncState(allStates)

  const reset = useCallback(() => {
    for (const s of allStates) {
      s.setData(null)
      s.reset()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [
    featureImportanceState, confusionMatrixState, rocCurveState,
    precisionRecallState, regressionDiagnosticsState, leaderboardState,
    modelInfoState, predictState, batchPredictState,
  ])

  return {
    featureImportance: featureImportanceState.data,
    confusionMatrix: confusionMatrixState.data,
    rocCurve: rocCurveState.data,
    precisionRecall: precisionRecallState.data,
    regressionDiagnostics: regressionDiagnosticsState.data,
    leaderboard: leaderboardState.data,
    modelInfo: modelInfoState.data,
    predictions: predictState.data,
    loading,
    error,
    reset,
    getFeatureImportance: featureImportanceState.execute,
    getConfusionMatrix: confusionMatrixState.execute,
    getROCCurve: rocCurveState.execute,
    getPrecisionRecall: precisionRecallState.execute,
    getRegressionDiagnostics: regressionDiagnosticsState.execute,
    getLeaderboard: leaderboardState.execute,
    getModelInfo: modelInfoState.execute,
    predict: predictState.execute,
    batchPredict: batchPredictState.execute,
  }
}
