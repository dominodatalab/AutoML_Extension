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
} from '../types/diagnostics'

interface UseDiagnosticsResult {
  featureImportance: FeatureImportanceResult | null
  confusionMatrix: ConfusionMatrixResult | null
  rocCurve: ROCCurveResult | null
  precisionRecall: PrecisionRecallResult | null
  regressionDiagnostics: RegressionDiagnosticsResult | null
  leaderboard: LeaderboardResult | null
  loading: boolean
  error: string | null
  reset: () => void
  getFeatureImportance: (jobId: string, modelType?: string) => Promise<FeatureImportanceResult | null>
  getConfusionMatrix: (jobId: string, modelType?: string) => Promise<ConfusionMatrixResult | null>
  getROCCurve: (jobId: string, modelType?: string) => Promise<ROCCurveResult | null>
  getPrecisionRecall: (jobId: string, modelType?: string) => Promise<PrecisionRecallResult | null>
  getRegressionDiagnostics: (jobId: string, modelType?: string) => Promise<RegressionDiagnosticsResult | null>
  getLeaderboard: (jobId: string, modelType?: string) => Promise<LeaderboardResult | null>
}

export function useDiagnostics(): UseDiagnosticsResult {
  const featureImportanceState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<FeatureImportanceResult>('predictions/model/feature-importance', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get feature importance'
  )

  const confusionMatrixState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<ConfusionMatrixResult>('predictions/model/confusion-matrix', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get confusion matrix'
  )

  const rocCurveState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<ROCCurveResult>('predictions/model/roc-curve', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get ROC curve'
  )

  const precisionRecallState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<PrecisionRecallResult>('predictions/model/precision-recall', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get precision-recall curve'
  )

  const regressionDiagnosticsState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<RegressionDiagnosticsResult>('predictions/model/regression-diagnostics', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get regression diagnostics'
  )

  const leaderboardState = useApiState(
    async (jobId: string, modelType?: string) => {
      const { data } = await api.post<LeaderboardResult>('predictions/model/leaderboard', { job_id: jobId, model_type: modelType })
      return data
    },
    'Failed to get leaderboard'
  )

  const allStates = [
    featureImportanceState,
    confusionMatrixState,
    rocCurveState,
    precisionRecallState,
    regressionDiagnosticsState,
    leaderboardState,
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
  ])

  return {
    featureImportance: featureImportanceState.data,
    confusionMatrix: confusionMatrixState.data,
    rocCurve: rocCurveState.data,
    precisionRecall: precisionRecallState.data,
    regressionDiagnostics: regressionDiagnosticsState.data,
    leaderboard: leaderboardState.data,
    loading,
    error,
    reset,
    getFeatureImportance: featureImportanceState.execute,
    getConfusionMatrix: confusionMatrixState.execute,
    getROCCurve: rocCurveState.execute,
    getPrecisionRecall: precisionRecallState.execute,
    getRegressionDiagnostics: regressionDiagnosticsState.execute,
    getLeaderboard: leaderboardState.execute,
  }
}
