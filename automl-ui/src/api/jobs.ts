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

export async function getJobStatus(jobId: string): Promise<{ id: string; status: string; error_message?: string }> {
  const response = await api.post<{ id: string; status: string; error_message?: string }>('/jobstatus', { job_id: jobId })
  return response.data
}

export async function getJobMetrics(jobId: string): Promise<JobMetricsResponse> {
  const response = await api.post<JobMetricsResponse>('/jobmetrics', { job_id: jobId })
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
