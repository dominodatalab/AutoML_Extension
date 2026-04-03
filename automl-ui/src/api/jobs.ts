import api from './index'
import { Job, JobCreateRequest, JobLog } from '../types/job'

interface JobListResponse {
  jobs: Job[]
  total: number
  skip: number
  limit: number
}

interface JobMetricsResponse {
  id: string
  metrics: Record<string, unknown> | null
  leaderboard: Record<string, unknown>[] | null
}

export interface JobStatusResponse {
  id: string
  status: string
  domino_job_status?: string
  error_message?: string
  started_at?: string
  completed_at?: string
}

export interface OrphanArtifact {
  path: string
  size_bytes: number
  name: string
  run_id?: string
  experiment_id?: string
  job_id?: string | null
}

export interface OrphanPreviewResponse {
  orphaned_models: OrphanArtifact[]
  orphaned_mlflow_runs: OrphanArtifact[]
  total_orphaned_model_size_bytes: number
  total_orphaned_mlflow_run_size_bytes: number
}

export interface CleanupOrphansResponse {
  models_deleted: number
  mlflow_runs_deleted: number
  total_size_freed_bytes: number
  errors: string[]
}

export async function getJobs(params?: { skip?: number; limit?: number; status?: string }): Promise<JobListResponse> {
  const response = await api.get<JobListResponse>('jobs', { params })
  return response.data
}

export async function getJob(jobId: string): Promise<Job> {
  const response = await api.get<Job>(`jobs/${jobId}`)
  return response.data
}

export async function getJobStatus(jobId: string): Promise<JobStatusResponse> {
  const response = await api.get<JobStatusResponse>(`jobs/${jobId}/status`)
  return response.data
}

export async function getJobMetrics(jobId: string): Promise<JobMetricsResponse> {
  const response = await api.get<JobMetricsResponse>(`jobs/${jobId}/metrics`)
  return response.data
}

export async function getJobLogs(jobId: string, _limit?: number): Promise<JobLog[]> {
  const response = await api.get<JobLog[]>(`jobs/${jobId}/logs`)
  return response.data
}

export async function createJob(request: JobCreateRequest): Promise<Job> {
  const response = await api.post<Job>('jobs', request)
  return response.data
}

export async function cancelJob(jobId: string): Promise<void> {
  await api.post(`jobs/${jobId}/cancel`)
}

export async function deleteJob(jobId: string): Promise<void> {
  await api.delete(`jobs/${jobId}`)
}

export interface BulkDeleteJobsResponse {
  deleted_job_ids: string[]
  failed: { job_id: string; error: string }[]
}

export async function bulkDeleteJobs(jobIds: string[]): Promise<BulkDeleteJobsResponse> {
  const response = await api.post<BulkDeleteJobsResponse>('jobs/bulk-delete', { job_ids: jobIds })
  return response.data
}

export async function getOrphanPreview(): Promise<OrphanPreviewResponse> {
  const response = await api.get<OrphanPreviewResponse>('jobs/orphans/preview')
  return response.data
}

export async function cleanupOrphans(): Promise<CleanupOrphansResponse> {
  const response = await api.post<CleanupOrphansResponse>('jobs/cleanup/orphans')
  return response.data
}
