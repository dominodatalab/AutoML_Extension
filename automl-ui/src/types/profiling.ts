// Data profiling types

export interface ColumnProfile {
  name: string
  dtype: string
  missing_count: number
  missing_percentage: number
  unique_count: number
  unique_percentage: number
  semantic_type: string
  statistics?: {
    // Numeric statistics
    mean?: number
    std?: number
    variance?: number
    min?: number
    max?: number
    median?: number
    skewness?: number
    kurtosis?: number
    zeros_count?: number
    zeros_percentage?: number
    negative_count?: number
    positive_count?: number
    outliers_count?: number
    outliers_percentage?: number
    percentiles?: Record<string, number>
    // Categorical statistics
    unique_count?: number
    most_common?: string
    most_common_count?: number
    least_common?: string
    least_common_count?: number
    avg_string_length?: number
    max_string_length?: number
    // Datetime statistics
    range_days?: number
  }
  histogram?: {
    counts: number[]
    bin_edges: number[]
  }
  value_counts?: Array<{
    value: unknown
    count: number
    percentage: number
  }>
  issues?: string[]
}

export interface DataSummary {
  total_rows: number
  total_columns: number
  sampled: boolean
  sample_size: number
  memory_usage_mb: number
  duplicate_rows: number
  duplicate_percentage: number
}

export interface DataRecommendation {
  type: string
  message: string
  priority: 'low' | 'medium' | 'high'
}

export interface DataWarning {
  type: string
  message: string
  severity: 'info' | 'warning' | 'error'
}

export interface CorrelationData {
  matrix?: Record<string, Record<string, number>>
  high_correlations?: Array<{
    column1: string
    column2: string
    correlation: number
  }>
}

export interface DataProfile {
  summary: DataSummary
  columns: ColumnProfile[]
  correlations: CorrelationData | Record<string, Record<string, number>>
  recommendations: DataRecommendation[]
  warnings: DataWarning[]
}

export interface TargetSuggestion {
  column: string
  score: number
  reasons: string[]
  problem_type: 'binary' | 'multiclass' | 'regression'
}

export interface QuickProfile {
  rows: number
  columns: number
  memory_mb: number
  column_types: Record<string, string>
  missing_columns: string[]
  potential_targets: string[]
}

export interface MetricInfo {
  value: string
  label: string
  description: string
}

export interface PresetInfo {
  value: string
  label: string
  description: string
  time_multiplier: number
}

export type MetricsByProblemType = Record<string, MetricInfo[]>
export type PresetsByModelType = Record<string, PresetInfo[]>
