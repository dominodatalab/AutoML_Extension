/**
 * Types for Domino Model Deployment management
 */

export type DeploymentStatus =
  | 'pending'
  | 'building'
  | 'starting'
  | 'running'
  | 'stopping'
  | 'stopped'
  | 'failed'
  | 'unknown'

export interface ModelApi {
  id: string
  name: string
  description?: string
  projectId?: string
  ownerId?: string
  createdAt?: string
  updatedAt?: string
}

export interface ModelApiVersion {
  id: string
  modelApiId: string
  modelFile: string
  function: string
  description?: string
  environmentId?: string
  status?: string
  createdAt?: string
}

export interface Deployment {
  id: string
  name?: string
  description?: string
  modelApiId: string
  modelApiVersionId: string
  status: DeploymentStatus
  url?: string
  minReplicas: number
  maxReplicas: number
  currentReplicas?: number
  environmentId?: string
  hardwareTierId?: string
  createdAt?: string
  updatedAt?: string
}

export interface DeploymentListResponse {
  success: boolean
  data: Deployment[]
  error?: string
}

export interface DeploymentResponse {
  success: boolean
  deployment_id?: string
  status?: string
  message?: string
  url?: string
  error?: string
  data?: Record<string, unknown>
}

export interface QuickDeployRequest {
  model_name: string
  model_file: string
  function_name?: string
  description?: string
  environment_id?: string
  hardware_tier_id?: string
  min_replicas?: number
  max_replicas?: number
  auto_start?: boolean
}

export interface DeployFromJobRequest {
  job_id: string
  model_name?: string
  function_name?: string
  min_replicas?: number
  max_replicas?: number
}

export interface DeploymentLogs {
  success: boolean
  logs?: string
  error?: string
}

export interface DeploymentStatusResponse {
  success: boolean
  deployment_id: string
  status: DeploymentStatus
  replicas?: {
    min: number
    max: number
    current: number
  }
  url?: string
  created_at?: string
  updated_at?: string
  error?: string
}
