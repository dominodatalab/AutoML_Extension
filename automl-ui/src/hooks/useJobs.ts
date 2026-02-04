import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { getJobs, getJob, getJobStatus, getJobLogs, createJob, cancelJob, deleteJob } from '../api/jobs'
import { JobCreateRequest } from '../types/job'

export function useJobs(params?: { skip?: number; limit?: number; status?: string }) {
  return useQuery({
    queryKey: ['jobs', params],
    queryFn: () => getJobs(params),
  })
}

export function useJob(jobId: string) {
  return useQuery({
    queryKey: ['job', jobId],
    queryFn: () => getJob(jobId),
    enabled: !!jobId,
  })
}

export function useJobStatus(jobId: string, enabled = true) {
  return useQuery({
    queryKey: ['jobStatus', jobId],
    queryFn: () => getJobStatus(jobId),
    enabled: !!jobId && enabled,
    refetchInterval: (query) => {
      // Stop polling when job is complete
      const data = query.state.data
      if (data?.status && ['completed', 'failed', 'cancelled'].includes(data.status)) {
        return false
      }
      return 3000 // Poll every 3 seconds
    },
  })
}

export function useJobLogs(jobId: string, limit?: number) {
  return useQuery({
    queryKey: ['jobLogs', jobId, limit],
    queryFn: () => getJobLogs(jobId, limit),
    enabled: !!jobId,
    refetchInterval: 5000, // Refresh logs every 5 seconds
  })
}

export function useCreateJob() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (request: JobCreateRequest) => createJob(request),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
    },
  })
}

export function useCancelJob() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (jobId: string) => cancelJob(jobId),
    onSuccess: (_data, jobId) => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
      queryClient.invalidateQueries({ queryKey: ['job', jobId] })
    },
  })
}

export function useDeleteJob() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (jobId: string) => deleteJob(jobId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
    },
  })
}
