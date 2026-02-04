// Model registry types

export type ModelStage = 'None' | 'Staging' | 'Production' | 'Archived'

export interface ModelVersion {
  version: string
  name: string
  status: string
  stage: ModelStage
  description?: string
  creation_timestamp?: number
  last_updated_timestamp?: number
  run_id?: string
  source?: string
  run_link?: string
  tags: Record<string, string>
}

export interface RegisteredModel {
  name: string
  description?: string
  creation_timestamp?: number
  last_updated_timestamp?: number
  tags: Record<string, string>
  latest_versions: Array<{
    version: string
    status: string
    stage: ModelStage
    creation_timestamp?: number
    run_id?: string
    source?: string
  }>
}

export interface RegisterModelRequest {
  model_path: string
  model_name: string
  model_type: string
  description?: string
  tags?: Record<string, string>
  metrics?: Record<string, number>
  params?: Record<string, unknown>
}

export interface RegisterModelResult {
  success: boolean
  model_name: string
  model_version?: string
  run_id?: string
  artifact_uri?: string
  error?: string
}

export interface TransitionStageRequest {
  model_name: string
  version: string
  stage: ModelStage
  archive_existing?: boolean
}

export interface TransitionStageResult {
  success: boolean
  model_name: string
  version: string
  new_stage: ModelStage
  previous_stage?: ModelStage
  error?: string
}

export interface ModelCard {
  model_name: string
  version: string
  card: string // Markdown content
}

export interface ModelsByStage {
  model_name: string
  stages: {
    None: ModelVersion[]
    Staging: ModelVersion[]
    Production: ModelVersion[]
    Archived: ModelVersion[]
  }
}
