// Model diagnostics types

export interface FeatureImportance {
  feature: string
  importance: number
  std?: number
  p_value?: number
}

export interface FeatureImportanceResult {
  model_path: string
  model_type: string
  method: string
  features: FeatureImportance[]
  chart?: string // base64 encoded PNG
  error?: string
}

export interface WeightedMetrics {
  precision: number
  recall: number
  'f1-score': number
  support?: number
}

export interface ConfusionMatrixMetrics {
  accuracy?: number
  precision?: number
  recall?: number
  f1?: number
  weighted_avg?: WeightedMetrics
}

export interface ConfusionMatrixResult {
  matrix?: number[][]
  labels: string[]
  chart?: string // base64 encoded PNG
  metrics: ConfusionMatrixMetrics
  error?: string
}

export interface ROCCurveResult {
  auc?: number
  fpr: number[]
  tpr: number[]
  chart?: string // base64 encoded PNG
  error?: string
}

export interface PrecisionRecallResult {
  average_precision?: number
  precision: number[]
  recall: number[]
  chart?: string // base64 encoded PNG
  error?: string
}

export interface RegressionDiagnosticsResult {
  metrics: {
    mse?: number
    rmse?: number
    mae?: number
    r2?: number
    median_ae?: number
    mape?: number
    [key: string]: number | undefined
  }
  predicted_vs_actual_chart?: string // base64 encoded PNG
  residuals_chart?: string // base64 encoded PNG
  residuals_histogram_chart?: string // base64 encoded PNG
  error?: string
}

export interface LeaderboardEntry {
  model: string
  score_val: number
  pred_time_val?: number
  fit_time?: number
  pred_time_val_marginal?: number
  fit_time_marginal?: number
  stack_level?: number
  can_infer?: boolean
  fit_order?: number
}

export interface LeaderboardResult {
  models: LeaderboardEntry[]
  chart?: string // base64 encoded PNG
  best_model?: string
  problem_type?: string
  eval_metric?: string
}

export interface PredictionRequest {
  model_id: string
  model_type: string
  data?: Record<string, unknown>[]
  file_path?: string
  return_probabilities?: boolean
}

export interface PredictionResult {
  model_id: string
  model_type: string
  num_rows: number
  predictions: unknown[]
  probabilities?: Record<string, number>[]
  problem_type?: string
  label?: string
}

export interface BatchPredictionRequest {
  model_id: string
  model_type: string
  input_file: string
  output_file: string
  return_probabilities?: boolean
}

export interface BatchPredictionResult {
  model_id: string
  output_file: string
  output_rows: number
  success: boolean
}

export interface ModelInfo {
  model_id: string
  model_type: string
  problem_type?: string
  label?: string
  features?: string[]
  model_names?: string[]
  best_model?: string
  leaderboard?: LeaderboardEntry[]
}
