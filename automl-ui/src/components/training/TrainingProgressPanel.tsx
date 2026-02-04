import { useState, useEffect, useCallback } from 'react'
import { Card } from '../common/Card'
import Badge from '../common/Badge'
import Spinner from '../common/Spinner'
import api from '../../api'
import type { Job, JobProgress } from '../../types/job'

interface TrainingProgressPanelProps {
  job: Job
  onComplete?: () => void
}

export function TrainingProgressPanel({ job, onComplete }: TrainingProgressPanelProps) {
  const [progress, setProgress] = useState<JobProgress | null>(null)
  const [isPolling, setIsPolling] = useState(false)
  // Timer state for live elapsed time updates
  const [elapsedMs, setElapsedMs] = useState(0)

  const fetchProgress = useCallback(async () => {
    try {
      const { data } = await api.post<JobProgress>('jobprogress', { job_id: job.id })
      setProgress(data)

      if (data.status === 'completed' || data.status === 'failed' || data.status === 'cancelled') {
        setIsPolling(false)
        onComplete?.()
      }
    } catch (err) {
      console.error('Failed to fetch progress:', err)
    }
  }, [job.id, onComplete])

  useEffect(() => {
    if (job.status === 'running' || job.status === 'pending') {
      setIsPolling(true)
    }
  }, [job.status])

  // Update elapsed time every second for running jobs
  useEffect(() => {
    if ((job.status === 'running' || job.status === 'pending') && job.started_at) {
      const updateElapsed = () => {
        setElapsedMs(new Date().getTime() - new Date(job.started_at!).getTime())
      }
      updateElapsed() // Initial update
      const timer = setInterval(updateElapsed, 1000)
      return () => clearInterval(timer)
    } else if (job.status === 'completed' && job.started_at && job.completed_at) {
      // For completed jobs, show final elapsed time
      setElapsedMs(new Date(job.completed_at).getTime() - new Date(job.started_at).getTime())
    }
  }, [job.status, job.started_at, job.completed_at])

  useEffect(() => {
    if (isPolling) {
      fetchProgress()
      const progressInterval = setInterval(fetchProgress, 2000)
      return () => clearInterval(progressInterval)
    }
  }, [isPolling, fetchProgress])

  return (
    <div className="space-y-4">
      {/* Progress Overview */}
      <Card>
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">Training Progress</h3>
          <Badge
            variant={
              job.status === 'completed' ? 'success' :
              job.status === 'failed' ? 'error' :
              job.status === 'running' ? 'info' :
              'warning'
            }
          >
            {job.status.toUpperCase()}
          </Badge>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div className="text-center p-3 bg-domino-bg-tertiary border border-domino-border rounded">
            <div className="text-2xl font-bold text-domino-accent-purple">
              {progress?.models_trained ?? job.leaderboard?.length ?? 0}
            </div>
            <div className="text-xs text-domino-text-muted uppercase tracking-wide">Models Trained</div>
          </div>
          <div className="text-center p-3 bg-domino-bg-tertiary border border-domino-border rounded">
            <div className="text-lg font-medium text-domino-text-primary truncate">
              {progress?.current_model || (job.status === 'completed' && job.leaderboard?.[0]?.model) || '-'}
            </div>
            <div className="text-xs text-domino-text-muted uppercase tracking-wide">
              {job.status === 'completed' ? 'Best Model' : 'Current Model'}
            </div>
          </div>
          <div className="text-center p-3 bg-domino-bg-tertiary border border-domino-border rounded">
            <div className="text-lg font-medium text-domino-text-primary">
              {elapsedMs > 0 ? formatDuration(elapsedMs) : '-'}
            </div>
            <div className="text-xs text-domino-text-muted uppercase tracking-wide">Job Time</div>
          </div>
        </div>

        {/* Training Animation */}
        {job.status === 'running' && (
          <div className="mt-4 flex items-center justify-center">
            <Spinner size="sm" />
            <span className="ml-2 text-sm text-gray-600">Training in progress...</span>
          </div>
        )}
      </Card>

      {/* Training Steps Timeline */}
      <Card>
        <h4 className="font-semibold mb-4">Training Steps</h4>
        <TrainingStepsTimeline job={job} progress={progress} />
      </Card>
    </div>
  )
}

interface TrainingStepsTimelineProps {
  job: Job
  progress: JobProgress | null
}

function TrainingStepsTimeline({ job, progress }: TrainingStepsTimelineProps) {
  const steps = [
    { key: 'init', label: 'Initialize', threshold: 0 },
    { key: 'load', label: 'Load Data', threshold: 10 },
    { key: 'preprocess', label: 'Preprocess', threshold: 20 },
    { key: 'train', label: 'Train Models', threshold: 30 },
    { key: 'evaluate', label: 'Evaluate', threshold: 80 },
    { key: 'finalize', label: 'Finalize', threshold: 95 },
    { key: 'complete', label: 'Complete', threshold: 100 },
  ]

  const currentProgress = progress?.progress ?? job.progress ?? 0
  const isComplete = job.status === 'completed'
  const isFailed = job.status === 'failed'

  // Calculate visual progress based on step positions, not raw percentage
  // Steps are evenly distributed, so we map progress thresholds to visual positions
  const calculateVisualProgress = () => {
    if (isComplete) return 100

    // Find current step index based on progress
    let currentStepIndex = 0
    for (let i = 0; i < steps.length - 1; i++) {
      if (currentProgress >= steps[i].threshold && currentProgress < steps[i + 1].threshold) {
        currentStepIndex = i
        break
      }
    }
    if (currentProgress >= steps[steps.length - 1].threshold) {
      currentStepIndex = steps.length - 1
    }

    // Each step takes 1/(n-1) of the visual space (n-1 gaps between n steps)
    const stepWidth = 100 / (steps.length - 1)

    // Calculate progress within current step
    const stepStart = steps[currentStepIndex].threshold
    const stepEnd = steps[currentStepIndex + 1]?.threshold ?? 100
    const progressInStep = stepEnd > stepStart
      ? (currentProgress - stepStart) / (stepEnd - stepStart)
      : 0

    // Visual progress = completed steps + progress within current step
    return (currentStepIndex + progressInStep) * stepWidth
  }

  const visualProgress = calculateVisualProgress()

  return (
    <div className="relative flex items-center justify-between">
      {/* Background connector line */}
      <div className="absolute top-4 left-0 right-0 h-0.5 bg-gray-200" style={{ marginLeft: '2rem', marginRight: '2rem' }} />

      {/* Progress connector line */}
      <div
        className={`absolute top-4 left-0 h-0.5 transition-all duration-500 ${
          isFailed ? 'bg-red-500' : 'bg-domino-accent-purple'
        }`}
        style={{
          marginLeft: '2rem',
          width: `calc(${Math.min(visualProgress, 100)}% - 4rem)`
        }}
      />

      {steps.map((step, index) => {
        const isActive = currentProgress >= step.threshold && currentProgress < (steps[index + 1]?.threshold ?? 101)
        const isDone = currentProgress >= (steps[index + 1]?.threshold ?? 100) || (isComplete && index < steps.length - 1)
        const isCurrent = isActive && !isComplete

        return (
          <div key={step.key} className="relative flex flex-col items-center flex-1">
            {/* Step circle */}
            <div
              className={`relative z-10 w-8 h-8 rounded-full flex items-center justify-center transition-all ${
                isDone || isComplete
                  ? 'bg-domino-accent-purple text-white'
                  : isFailed && isActive
                  ? 'bg-red-500 text-white'
                  : isCurrent
                  ? 'bg-domino-accent-purple text-white ring-4 ring-domino-accent-purple/20'
                  : 'bg-gray-200 text-gray-500'
              }`}
            >
              {isDone || isComplete ? (
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              ) : isFailed && isActive ? (
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              ) : isCurrent ? (
                <div className="w-3 h-3 rounded-full bg-white animate-pulse" />
              ) : (
                <span className="text-xs">{index + 1}</span>
              )}
            </div>

            {/* Label */}
            <span
              className={`mt-2 text-xs text-center ${
                isDone || isComplete || isCurrent ? 'text-gray-900 font-medium' : 'text-gray-400'
              }`}
            >
              {step.label}
            </span>
          </div>
        )
      })}
    </div>
  )
}

function formatDuration(ms: number): string {
  // Handle negative values (clock sync issues between server and client)
  if (ms < 0) {
    return '0s'
  }

  const seconds = Math.floor(ms / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)

  if (hours > 0) {
    return `${hours}h ${minutes % 60}m`
  } else if (minutes > 0) {
    return `${minutes}m ${seconds % 60}s`
  } else {
    return `${seconds}s`
  }
}

// Export a simpler progress bar component for use elsewhere
interface SimpleProgressBarProps {
  progress: number
  status: string
  currentStep?: string
}

export function SimpleProgressBar({ progress, status }: SimpleProgressBarProps) {
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed': return 'bg-domino-accent-purple'
      case 'running': return 'bg-domino-accent-purple'
      case 'failed': return 'bg-domino-accent-red'
      case 'cancelled': return 'bg-gray-500'
      default: return 'bg-domino-accent-yellow'
    }
  }

  return (
    <div>
      <div className="flex items-center justify-end text-sm mb-1">
        <span className="font-medium">{progress}%</span>
      </div>
      <div className="h-2 bg-gray-200 overflow-hidden">
        <div
          className={`h-full transition-all duration-300 ${getStatusColor(status)}`}
          style={{ width: `${progress}%` }}
        />
      </div>
    </div>
  )
}
