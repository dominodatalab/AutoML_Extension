import { ModelType, ProblemType, Preset, ExecutionTarget, AdvancedAutoGluonConfig, TimeSeriesAdvancedConfig, MultimodalAdvancedConfig } from './job'

export interface DataSourceConfig {
  type: 'upload' | 'domino_dataset'
  datasetId?: string
  filePath?: string
  fileName?: string
  columns?: string[]
  rowCount?: number
}

export interface ModelTypeConfig {
  modelType: ModelType
  problemType?: ProblemType
}

export interface TrainingConfig {
  executionTarget: ExecutionTarget
  targetColumn: string
  timeColumn?: string
  idColumn?: string
  predictionLength?: number
  preset: Preset
  timeLimit?: number
  evalMetric?: string
  experimentName?: string
  advancedConfig?: AdvancedAutoGluonConfig
  timeseriesConfig?: TimeSeriesAdvancedConfig
  multimodalConfig?: MultimodalAdvancedConfig
}

export interface WizardState {
  currentStep: number
  dataSource: DataSourceConfig | null
  modelType: ModelTypeConfig | null
  training: TrainingConfig | null
  jobName: string
  jobDescription: string
}
