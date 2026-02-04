// Types for local/job-based models (distinct from MLflow registry types in registry.ts)

/**
 * A model that was trained by a job (local model, not in MLflow registry)
 */
export interface TrainedModel {
  id: string
  name: string
  description?: string
  job_id?: string
  version?: number
  mlflow_model_uri?: string
  domino_model_id?: string
  deployed?: boolean
  created_at?: string
  // Properties that may come from job data
  model_path?: string
  model_type?: string
  metrics?: Record<string, number>
}

/**
 * Version info for a trained model (simpler than MLflow ModelVersion)
 */
export interface TrainedModelVersion {
  version: number
  created_at: string
  run_id?: string
  status: string
}

/**
 * Request to deploy a model
 */
export interface DeploymentRequest {
  model_version: number
  environment_id?: string
  hardware_tier_id?: string
  description?: string
}

/**
 * Result of a deployment operation
 */
export interface DeploymentResult {
  success: boolean
  model_name: string
  model_version: number
  deployment_id?: string
  endpoint_url?: string
  status: string
  message?: string
}

// Re-export for backwards compatibility (deprecated - use TrainedModel instead)
export type RegisteredModel = TrainedModel
export type ModelVersion = TrainedModelVersion
export type Deployment = DeploymentResult
