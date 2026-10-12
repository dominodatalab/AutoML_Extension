import { useCallback, useEffect, useRef } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import {
  getJobs,
  getJob,
  getJobStatus,
  getJobLogs,
  createJob,
  cancelJob,
  deleteJob,
  bulkDeleteJobs,
  getOrphanPreview,
  cleanupOrphans,
} from '../api/jobs'
import { JobCreateRequest } from '../types/job'
import { useStore } from '../store'
import { getErrorMessage } from '../utils/errors'

function useQueryWithErrorToast(resetKey: string) {
  const addNotification = useStore((state) => state.addNotification)
  const hasNotifiedError = useRef(false)

  useEffect(() => {
    hasNotifiedError.current = false
  }, [resetKey])

  return useCallback(async <T,>(query: () => Promise<T>): Promise<T> => {
    try {
      const result = await query()
      hasNotifiedError.current = false
      return result
    } catch (error) {
      if (!hasNotifiedError.current) {
        addNotification(getErrorMessage(error), 'error')
        hasNotifiedError.current = true
      }
      throw error
    }
  }, [addNotification])
}

function useMutationErrorToast() {
  const addNotification = useStore((state) => state.addNotification)

  return useCallback((error: Error) => {
    addNotification(getErrorMessage(error), 'error')
  }, [addNotification])
}

export function useJobs(params?: { skip?: number; limit?: number; status?: string }) {
  const resetKey = `${params?.skip ?? ''}:${params?.limit ?? ''}:${params?.status ?? ''}`
  const queryWithErrorToast = useQueryWithErrorToast(resetKey)

  return useQuery({
    queryKey: ['jobs', params],
    queryFn: () => queryWithErrorToast(() => getJobs(params)),
    refetchInterval: (query) => {
      const jobs = query.state.data?.jobs ?? []
      const hasActiveJobs = jobs.some((job) => ['pending', 'running'].includes(job.status))
      return hasActiveJobs ? 5000 : false
    },
    retry: false,
  })
}

export function useJob(jobId: string) {
  const queryWithErrorToast = useQueryWithErrorToast(jobId)

  return useQuery({
    queryKey: ['job', jobId],
    queryFn: () => queryWithErrorToast(() => getJob(jobId)),
    enabled: !!jobId,
    retry: false,
  })
}

export function useJobStatus(jobId: string, enabled = true) {
  const queryWithErrorToast = useQueryWithErrorToast(`${jobId}:${enabled}`)

  return useQuery({
    queryKey: ['jobStatus', jobId],
    queryFn: () => queryWithErrorToast(() => getJobStatus(jobId)),
    enabled: !!jobId && enabled,
    refetchInterval: (query) => {
      // Stop polling when job is complete
      const data = query.state.data
      if (data?.status && ['completed', 'failed', 'cancelled'].includes(data.status)) {
        return false
      }
      return 3000 // Poll every 3 seconds
    },
    retry: false,
  })
}

export function useJobLogs(jobId: string, limit?: number) {
  const queryWithErrorToast = useQueryWithErrorToast(`${jobId}:${limit ?? ''}`)

  return useQuery({
    queryKey: ['jobLogs', jobId, limit],
    queryFn: () => queryWithErrorToast(() => getJobLogs(jobId, limit)),
    enabled: !!jobId,
    refetchInterval: 5000, // Refresh logs every 5 seconds
    retry: false,
  })
}

export function useCreateJob() {
  const queryClient = useQueryClient()
  const showErrorToast = useMutationErrorToast()

  return useMutation({
    mutationFn: (request: JobCreateRequest) => createJob(request),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
    },
    onError: showErrorToast,
  })
}

export function useCancelJob() {
  const queryClient = useQueryClient()
  const showErrorToast = useMutationErrorToast()

  return useMutation({
    mutationFn: (jobId: string) => cancelJob(jobId),
    onSuccess: (_data, jobId) => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
      queryClient.invalidateQueries({ queryKey: ['job', jobId] })
    },
    onError: showErrorToast,
  })
}

export function useDeleteJob() {
  const queryClient = useQueryClient()
  const showErrorToast = useMutationErrorToast()

  return useMutation({
    mutationFn: (jobId: string) => deleteJob(jobId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
    },
    onError: showErrorToast,
  })
}

export function useBulkDeleteJobs() {
  const queryClient = useQueryClient()
  const addNotification = useStore((state) => state.addNotification)
  const showErrorToast = useMutationErrorToast()

  return useMutation({
    mutationFn: (jobIds: string[]) => bulkDeleteJobs(jobIds),
    onSuccess: (result) => {
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
      if (result.failed.length > 0) {
        const plural = result.failed.length === 1 ? 'job' : 'jobs'
        addNotification(`Failed to delete ${result.failed.length} ${plural}.`, 'error')
      }
    },
    onError: showErrorToast,
  })
}

export function useOrphanPreview(enabled = true) {
  const queryWithErrorToast = useQueryWithErrorToast(String(enabled))

  return useQuery({
    queryKey: ['orphanPreview'],
    queryFn: () => queryWithErrorToast(() => getOrphanPreview()),
    enabled,
    retry: false,
  })
}

export function useCleanupOrphans() {
  const queryClient = useQueryClient()
  const showErrorToast = useMutationErrorToast()

  return useMutation({
    mutationFn: () => cleanupOrphans(),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['orphanPreview'] })
      queryClient.invalidateQueries({ queryKey: ['jobs'] })
    },
    onError: showErrorToast,
  })
}
