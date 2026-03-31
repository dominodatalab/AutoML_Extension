import { useState, useEffect, useCallback, useRef } from 'react'
import api from '../api'
import type { JobProgress, Job } from '../types/job'

interface UseJobProgressReturn {
  polledProgress: JobProgress | null
  progressJobId: string | null
  simulatedProgress: number
}

export function useJobProgress(jobId: string | undefined, job: Job | undefined, isTraining: boolean, refetch: () => void): UseJobProgressReturn {
  const [polledProgress, setPolledProgress] = useState<JobProgress | null>(null)
  const [progressJobId, setProgressJobId] = useState<string | null>(null)
  const [simulatedProgress, setSimulatedProgress] = useState(0)
  const currentJobIdRef = useRef<string | undefined>(jobId)
  const simulationStartRef = useRef<number | null>(null)

  useEffect(() => {
    currentJobIdRef.current = jobId
  }, [jobId])

  useEffect(() => {
    setPolledProgress(null)
    setProgressJobId(null)
    setSimulatedProgress(0)
    simulationStartRef.current = null
  }, [jobId])

  const fetchProgress = useCallback(async () => {
    const requestJobId = currentJobIdRef.current
    if (!requestJobId) return
    try {
      const { data } = await api.get<JobProgress>(`jobs/${requestJobId}/progress`)
      if (currentJobIdRef.current === requestJobId) {
        setPolledProgress(data)
        setProgressJobId(requestJobId)
        if (data.status === 'completed' || data.status === 'failed') {
          refetch()
        }
      }
    } catch (err) {
      console.error('Failed to fetch progress:', err)
    }
  }, [refetch])

  useEffect(() => {
    if (isTraining && jobId) {
      fetchProgress()
      const interval = setInterval(() => {
        if (currentJobIdRef.current === jobId) fetchProgress()
      }, 1000)
      return () => clearInterval(interval)
    }
  }, [isTraining, jobId, fetchProgress])

  useEffect(() => {
    if (!job || !isTraining) {
      return
    }

    const startTime = job.started_at
      ? new Date(job.started_at).getTime()
      : Date.now()

    if (!simulationStartRef.current) {
      simulationStartRef.current = startTime
      setSimulatedProgress(1)
    }

    const timeLimit = job.time_limit || 3600

    const updateProgress = () => {
      const now = Date.now()
      const elapsed = (now - (simulationStartRef.current || now)) / 1000

      const timeRatio = Math.min(elapsed / timeLimit, 1)
      let progress: number

      if (timeRatio < 0.5) {
        progress = Math.floor((timeRatio / 0.5) * 70)
      } else {
        progress = Math.floor(70 + ((timeRatio - 0.5) / 0.5) * 25)
      }

      progress = Math.max(1, Math.min(progress, 95))
      setSimulatedProgress(progress)
    }

    updateProgress()

    const interval = setInterval(updateProgress, 1000)

    return () => clearInterval(interval)
  }, [job?.id, job?.started_at, job?.time_limit, isTraining])

  useEffect(() => {
    if (job && ['completed', 'failed', 'cancelled'].includes(job.status)) {
      if (job.status === 'completed') {
        const animateToComplete = () => {
          setSimulatedProgress(prev => {
            if (prev >= 100) return 100
            return Math.min(prev + 5, 100)
          })
        }
        const interval = setInterval(animateToComplete, 50)
        const timeout = setTimeout(() => clearInterval(interval), 1000)
        return () => {
          clearInterval(interval)
          clearTimeout(timeout)
        }
      }
    }
  }, [job?.status])

  return {
    polledProgress,
    progressJobId,
    simulatedProgress,
  }
}
