import api from './index'
import { Job, JobCreateRequest, JobLog } from '../types/job'

interface JobListResponse {
  jobs: Job[]
  total: number
  skip: number
  limit: number
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
  orphaned_uploads: OrphanArtifact[]
  orphaned_mlflow_runs: OrphanArtifact[]
  total_orphaned_model_size_bytes: number
  total_orphaned_upload_size_bytes: number
  total_orphaned_mlflow_run_size_bytes: number
}

export interface CleanupOrphansResponse {
  models_deleted: number
  uploads_deleted: number
  mlflow_runs_deleted: number
  total_size_freed_bytes: number
  errors: string[]
}

export async function getJobs(params?: { skip?: number; limit?: number; status?: string }): Promise<JobListResponse> {
  // Use POST for Domino compatibility (svcjobs is POST endpoint)
  const response = await api.post<JobListResponse>('/jobs', params || {})
  return response.data
}

export async function getJob(jobId: string): Promise<Job> {
  // Use POST with job_id in body (Domino doesn't support path params)
  const response = await api.post<Job>('/jobget', { job_id: jobId })
  return response.data
}

export async function getJobStatus(jobId: string): Promise<JobStatusResponse> {
  const response = await api.post<JobStatusResponse>('/jobstatus', { job_id: jobId })
  return response.data
}

export async function getJobLogs(jobId: string, _limit?: number): Promise<JobLog[]> {
  const response = await api.post<JobLog[]>('/joblogs', { job_id: jobId })
  return response.data
}

export async function createJob(request: JobCreateRequest): Promise<Job> {
  const response = await api.post<Job>('/jobcreate', request)
  return response.data
}

export async function cancelJob(jobId: string): Promise<void> {
  await api.post('/jobcancel', { job_id: jobId })
}

export async function deleteJob(jobId: string): Promise<void> {
  await api.post('/jobdelete', { job_id: jobId })
}

export interface BulkDeleteJobsResponse {
  deleted_job_ids: string[]
  failed: { job_id: string; error: string }[]
}

export async function bulkDeleteJobs(jobIds: string[]): Promise<BulkDeleteJobsResponse> {
  const response = await api.post<BulkDeleteJobsResponse>('/jobbulkdelete', { job_ids: jobIds })
  return response.data
}

export async function getOrphanPreview(): Promise<OrphanPreviewResponse> {
  const response = await api.post<OrphanPreviewResponse>('/joborphans', {})
  return response.data
}

export async function cleanupOrphans(): Promise<CleanupOrphansResponse> {
  const response = await api.post<CleanupOrphansResponse>('/jobcleanuporphans', {})
  return response.data
}
