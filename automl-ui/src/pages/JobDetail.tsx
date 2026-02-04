import { useState, useEffect, useCallback, useRef } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { format } from 'date-fns'
import { StopIcon, CloudArrowUpIcon } from '@heroicons/react/24/outline'
import { useJob, useJobStatus, useJobLogs, useCancelJob, useDeleteJob } from '../hooks/useJobs'
import Badge from '../components/common/Badge'
import Button from '../components/common/Button'
import { SimpleProgressBar } from '../components/training/TrainingProgressPanel'
import { ModelDiagnosticsPanel } from '../components/diagnostics/ModelDiagnosticsPanel'
import { LearningCurvesPanel } from '../components/diagnostics/LearningCurvesPanel'
import { RegisterModelDialog } from '../components/registry/ModelRegistryPanel'
import { ModelExportPanel } from '../components/export/ModelExportPanel'
import { TimeSeriesForecastPanel } from '../components/timeseries/TimeSeriesForecastPanel'
import { InteractiveLeaderboard } from '../components/leaderboard/InteractiveLeaderboard'
import api from '../api'
import type { JobProgress, JobStatus } from '../types/job'

// Helper to notify parent frame about modal state
function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}

type DetailTab = 'overview' | 'progress' | 'leaderboard' | 'diagnostics' | 'learning' | 'forecast' | 'export' | 'logs'

function getDuration(startedAt?: string, completedAt?: string): string {
  // Only show duration when job has finished (both timestamps available)
  if (!startedAt || !completedAt) return '—'
  const start = new Date(startedAt).getTime()
  const end = new Date(completedAt).getTime()
  const seconds = Math.floor((end - start) / 1000)
  // Handle invalid duration
  if (seconds < 0 || seconds > 86400 * 365) return '—'
  if (seconds < 60) return `${seconds}s`
  const minutes = Math.floor(seconds / 60)
  const secs = seconds % 60
  if (minutes < 60) return `${minutes}m ${secs}s`
  const hours = Math.floor(minutes / 60)
  return `${hours}h ${minutes % 60}m`
}

function JobDetail() {
  const { jobId } = useParams<{ jobId: string }>()
  const { data: job, isLoading, refetch } = useJob(jobId!)
  const { data: statusData } = useJobStatus(jobId!, !!job && ['pending', 'running'].includes(job.status))
  const { data: logs } = useJobLogs(jobId!, 100)
  const cancelMutation = useCancelJob()

  const [polledProgress, setPolledProgress] = useState<JobProgress | null>(null)
  const [progressJobId, setProgressJobId] = useState<string | null>(null)
  const [simulatedProgress, setSimulatedProgress] = useState(0)
  const currentJobIdRef = useRef<string | undefined>(jobId)
  const simulationStartRef = useRef<number | null>(null)

  const isTraining = !!job && ['pending', 'running'].includes(job.status)

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
      const { data } = await api.post<JobProgress>('jobprogress', { job_id: requestJobId })
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

  // Simulate progress based on time_limit - updates every second
  useEffect(() => {
    if (!job || !isTraining) {
      return
    }

    // Use started_at if available, otherwise track from now
    const startTime = job.started_at
      ? new Date(job.started_at).getTime()
      : Date.now()

    if (!simulationStartRef.current) {
      simulationStartRef.current = startTime
      // Start with 1% immediately to show activity
      setSimulatedProgress(1)
    }

    const timeLimit = job.time_limit || 3600 // Default to 1 hour if not set

    const updateProgress = () => {
      const now = Date.now()
      const elapsed = (now - (simulationStartRef.current || now)) / 1000

      // Calculate progress as percentage of time limit
      // Use a curve that starts faster: first 50% of time = 70% of progress bar
      // This makes early progress more visible
      const timeRatio = Math.min(elapsed / timeLimit, 1)
      let progress: number

      if (timeRatio < 0.5) {
        // First half of time: 0-70% of progress (faster start)
        progress = Math.floor((timeRatio / 0.5) * 70)
      } else {
        // Second half of time: 70-95% of progress (slower finish)
        progress = Math.floor(70 + ((timeRatio - 0.5) / 0.5) * 25)
      }

      // Ensure minimum of 1% and max of 95%
      progress = Math.max(1, Math.min(progress, 95))
      setSimulatedProgress(progress)
    }

    // Update immediately
    updateProgress()

    // Then update every second
    const interval = setInterval(updateProgress, 1000)

    return () => clearInterval(interval)
  }, [job?.id, job?.started_at, job?.time_limit, isTraining])

  // When job completes, quickly animate to 100%
  useEffect(() => {
    if (job && ['completed', 'failed', 'cancelled'].includes(job.status)) {
      // Animate from current progress to 100% (or stay at current for failed/cancelled)
      if (job.status === 'completed') {
        const animateToComplete = () => {
          setSimulatedProgress(prev => {
            if (prev >= 100) return 100
            return Math.min(prev + 5, 100) // Quick 5% jumps to 100%
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

  const [activeTab, setActiveTab] = useState<DetailTab>('overview')
  const [showRegisterDialog, setShowRegisterDialog] = useState(false)
  const [showRegisterDropdown, setShowRegisterDropdown] = useState(false)
  const [showActionsDropdown, setShowActionsDropdown] = useState(false)
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false)
  const [showCancelConfirm, setShowCancelConfirm] = useState(false)

  const navigate = useNavigate()
  const deleteJobMutation = useDeleteJob()
  const registerDropdownRef = useRef<HTMLDivElement>(null)
  const actionsDropdownRef = useRef<HTMLDivElement>(null)

  // Close dropdowns when clicking outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (registerDropdownRef.current && !registerDropdownRef.current.contains(event.target as Node)) {
        setShowRegisterDropdown(false)
      }
      if (actionsDropdownRef.current && !actionsDropdownRef.current.contains(event.target as Node)) {
        setShowActionsDropdown(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleDeleteJob = async () => {
    try {
      await deleteJobMutation.mutateAsync(job!.id)
      setShowDeleteConfirm(false)
      navigate('/dashboard')
    } catch (err) {
      console.error('Failed to delete job:', err)
    }
  }

  if (!job && !isLoading) {
    return (
      <div className="text-center py-12">
        <p className="text-domino-accent-red">Job not found</p>
        <Link to="/dashboard" className="text-domino-accent-purple hover:underline text-sm">
          Back to AutoML
        </Link>
      </div>
    )
  }

  // Handle loading state - use defaults when job not yet loaded
  const jobStatus = job?.status || 'running'
  const isJobTerminal = ['completed', 'failed', 'cancelled'].includes(jobStatus)
  const validPolledProgress = !isJobTerminal && progressJobId === jobId ? polledProgress : null
  const currentStatus = isJobTerminal ? jobStatus : (validPolledProgress?.status || statusData?.status || jobStatus)
  const rawProgress = validPolledProgress?.progress ?? job?.progress ?? 0

  // Use simulated progress for smooth time-based animation
  // Take the higher of simulated progress or actual backend progress
  const currentProgress = isJobTerminal
    ? (jobStatus === 'completed' ? 100 : rawProgress)
    : Math.max(simulatedProgress, rawProgress)

  const handleCancel = async () => {
    setShowCancelConfirm(true)
  }

  const confirmCancel = async () => {
    if (job) {
      await cancelMutation.mutateAsync(job.id)
    }
    setShowCancelConfirm(false)
  }

  interface TabConfig {
    key: string
    label: string
    showWhenDone?: boolean
    showForTimeseries?: boolean
  }

  const allTabs: TabConfig[] = [
    { key: 'overview', label: 'Overview' },
    { key: 'leaderboard', label: 'Leaderboard', showWhenDone: true },
    { key: 'diagnostics', label: 'Diagnostics', showWhenDone: true },
    { key: 'learning', label: 'Metrics', showWhenDone: true },
    { key: 'forecast', label: 'Forecast', showWhenDone: true, showForTimeseries: true },
    { key: 'export', label: 'Outputs', showWhenDone: true },
    { key: 'logs', label: 'Logs' },
  ]

  const tabs = allTabs.filter((tab) => {
    if (tab.showWhenDone && currentStatus !== 'completed') return false
    if (tab.showForTimeseries && job?.model_type !== 'timeseries') return false
    return true
  })

  return (
    <div>
      {/* Breadcrumb */}
      <nav className="flex items-center gap-2 text-sm mb-2">
        <Link to="/dashboard" className="text-domino-accent-purple hover:underline">
          AutoML
        </Link>
        <span className="text-domino-text-muted">/</span>
        <span className="text-domino-text-secondary">{job?.name || 'Training Job'}</span>
      </nav>

      {/* Header */}
      <div className="flex items-center justify-between flex-wrap mb-5">
        <div>
          <h1 className="text-2xl font-normal text-domino-text-primary leading-tight">
            {job ? `Run: ${job.name}` : 'Training in Progress'}
          </h1>
        </div>
        <div className="flex items-center gap-3">
          {['pending', 'running'].includes(currentStatus) && (
            <button
              onClick={handleCancel}
              disabled={cancelMutation.isPending}
              className="h-[32px] px-[15px] text-sm font-normal border border-transparent rounded-[2px] text-white bg-domino-accent-red hover:bg-domino-accent-red/90 transition-all duration-200 inline-flex items-center"
            >
              <StopIcon className="h-4 w-4 inline mr-1" />
              Cancel
            </button>
          )}
          {currentStatus === 'completed' && job?.model_path && (
            <div className="relative" ref={registerDropdownRef}>
              <button
                onClick={() => setShowRegisterDropdown(!showRegisterDropdown)}
                className="h-[32px] px-[15px] bg-domino-accent-purple text-white text-sm font-normal rounded-[2px] hover:bg-domino-accent-purple-hover transition-all duration-200 inline-flex items-center gap-1.5"
              >
                Register
                <svg className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {showRegisterDropdown && (
                <div className="absolute right-0 mt-1 w-48 bg-white shadow-lg border border-gray-200 py-1 z-50">
                  <button
                    onClick={() => {
                      setShowRegisterDropdown(false)
                      setShowRegisterDialog(true)
                    }}
                    className="w-full px-4 py-2 text-left text-sm text-domino-text-primary hover:bg-domino-bg-tertiary flex items-center gap-2 transition-colors"
                  >
                    <CloudArrowUpIcon className="w-4 h-4" />
                    Deploy to Registry
                  </button>
                </div>
              )}
            </div>
          )}
          <div className="relative" ref={actionsDropdownRef}>
            <button
              onClick={() => setShowActionsDropdown(!showActionsDropdown)}
              className="h-[32px] w-[32px] flex items-center justify-center border border-[#d9d9d9] rounded-[2px] text-domino-text-secondary hover:border-domino-accent-purple hover:text-domino-accent-purple transition-all duration-200"
            >
              <svg className="w-4 h-4" viewBox="0 0 16 16" fill="currentColor">
                <circle cx="8" cy="3" r="1.5" />
                <circle cx="8" cy="8" r="1.5" />
                <circle cx="8" cy="13" r="1.5" />
              </svg>
            </button>
            {showActionsDropdown && (
              <div className="absolute right-0 mt-1 w-40 bg-white shadow-lg border border-gray-200 py-1 z-50">
                <button
                  onClick={() => {
                    setShowActionsDropdown(false)
                    setShowDeleteConfirm(true)
                  }}
                  className="w-full px-4 py-2 text-left text-sm text-domino-accent-red hover:bg-domino-bg-tertiary transition-colors"
                >
                  Delete
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="border-b border-domino-border mb-6">
        <nav className="flex gap-6">
          {tabs.map((tab) => (
            <button
              key={tab.key}
              onClick={() => setActiveTab(tab.key as DetailTab)}
              className={`pb-3 text-sm border-b-2 -mb-px transition-colors ${
                activeTab === tab.key
                  ? 'border-domino-accent-purple text-domino-accent-purple font-medium'
                  : 'border-transparent text-domino-text-secondary hover:text-domino-text-primary font-normal'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Progress bar for running jobs */}
      {['pending', 'running'].includes(jobStatus) && activeTab === 'overview' && (
        <div className="mb-6">
          <SimpleProgressBar
            progress={currentProgress}
            status={currentStatus}
          />
        </div>
      )}

      {/* Tab content */}
      {activeTab === 'overview' && (
        <div>
          {/* Description */}
          <div className="mb-6">
            <h3 className="text-sm font-semibold text-domino-text-primary mb-1">Description</h3>
            <p className="text-sm text-domino-text-secondary">
              {job?.description || (isLoading ? 'Loading...' : 'No description available')}
            </p>
          </div>

          {/* Metadata table */}
          <div className="mb-6">
            <table className="w-full">
              <thead>
                <tr className="border-b border-domino-border">
                  <th className="px-4 py-3 text-left text-sm font-medium text-domino-text-primary w-48">Metadata</th>
                  <th className="px-4 py-3 text-left text-sm font-medium text-domino-text-primary border-l border-domino-border">Value</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-domino-border">
                <MetadataRow label="Run ID" value={job?.id || (isLoading ? 'Loading...' : '—')} mono />
                <MetadataRow label="Model type" value={job?.model_type || (isLoading ? 'Loading...' : '—')} capitalize />
                {job?.problem_type && <MetadataRow label="Problem type" value={job.problem_type} capitalize />}
                <MetadataRow label="Target column" value={job?.target_column || (isLoading ? 'Loading...' : '—')} />
                <MetadataRow label="Preset" value={job?.preset?.replace(/_/g, ' ') || (isLoading ? 'Loading...' : '—')} capitalize />
                {job?.eval_metric && <MetadataRow label="Eval metric" value={job.eval_metric} />}
                {job?.time_limit && <MetadataRow label="Time limit" value={`${job.time_limit}s`} />}
                {job?.created_at && (
                  <MetadataRow
                    label="Created"
                    value={format(new Date(job.created_at), 'MMM d, yyyy h:mm a')}
                  />
                )}
                {job?.started_at && (
                  <MetadataRow
                    label="Duration"
                    value={getDuration(job.started_at, job.completed_at)}
                  />
                )}
                <MetadataRow label="Status">
                  <Badge status={currentStatus as JobStatus} isRegistered={job?.is_registered} />
                </MetadataRow>
                {job?.experiment_name && (
                  <MetadataRow label="Experiment" value={job.experiment_name} />
                )}
                {job?.experiment_run_id && (
                  <MetadataRow label="MLflow run ID" value={job.experiment_run_id} mono />
                )}
              </tbody>
            </table>
          </div>

          {/* Metrics */}
          {job?.metrics && Object.keys(job.metrics).length > 0 && (
            <div className="mb-6">
              <table className="w-full">
                <thead>
                  <tr className="border-b border-domino-border">
                    <th className="px-4 py-3 text-left text-sm font-medium text-domino-text-primary w-48">Metric</th>
                    <th className="px-4 py-3 text-left text-sm font-medium text-domino-text-primary border-l border-domino-border">Value</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-domino-border">
                  {Object.entries(job.metrics).map(([key, value]) => {
                    let displayValue: string
                    if (typeof value === 'number' && !isNaN(value)) {
                      displayValue = value.toFixed(4)
                    } else if (typeof value === 'object' && value !== null) {
                      displayValue = JSON.stringify(value)
                    } else {
                      displayValue = String(value ?? '—')
                    }
                    return (
                      <MetadataRow
                        key={key}
                        label={key.replace(/_/g, ' ')}
                        value={displayValue}
                        mono
                        capitalize
                      />
                    )
                  })}
                </tbody>
              </table>
            </div>
          )}

          {/* Error */}
          {job?.error_message && (
            <div className="border border-domino-accent-red/30 bg-domino-accent-red/5 rounded p-4 mt-6">
              <p className="text-sm font-medium text-domino-accent-red mb-1">Error</p>
              <pre className="text-sm text-domino-accent-red  whitespace-pre-wrap">
                {job.error_message}
              </pre>
            </div>
          )}
        </div>
      )}

      {activeTab === 'leaderboard' && currentStatus === 'completed' && job && (
        <InteractiveLeaderboard leaderboard={job.leaderboard || []} />
      )}

      {activeTab === 'diagnostics' && currentStatus === 'completed' && job && (
        <ModelDiagnosticsPanel job={job} />
      )}

      {activeTab === 'learning' && currentStatus === 'completed' && job && (
        <LearningCurvesPanel jobId={job.id} modelType={job.model_type} />
      )}

      {activeTab === 'export' && currentStatus === 'completed' && job && (
        <ModelExportPanel jobId={job.id} jobName={job.name} projectName={job.project_name} modelType={job.model_type} problemType={job.problem_type} />
      )}

      {activeTab === 'forecast' && currentStatus === 'completed' && job?.model_type === 'timeseries' && (
        <TimeSeriesForecastPanel job={job} />
      )}

      {activeTab === 'logs' && (
        <div className="border border-domino-border rounded overflow-hidden">
          <div className="bg-domino-bg-secondary px-4 py-2.5 border-b border-domino-border">
            <h3 className="text-sm font-medium text-domino-text-primary">Training logs</h3>
          </div>
          <div className="p-4">
            {logs && logs.length > 0 ? (
              <div className="bg-domino-bg-tertiary rounded p-4 max-h-[500px] overflow-auto  text-xs leading-relaxed">
                {logs.map((log) => (
                  <div
                    key={log.id}
                    className={`py-0.5 ${
                      log.level === 'ERROR' ? 'text-domino-accent-red' :
                      log.level === 'WARNING' ? 'text-domino-accent-yellow' :
                      'text-domino-text-primary'
                    }`}
                  >
                    <span className="text-domino-text-muted">
                      [{format(new Date(log.timestamp), 'HH:mm:ss')}]
                    </span>{' '}
                    <span className="text-domino-text-secondary">[{log.level}]</span>{' '}
                    {log.message}
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-domino-text-muted text-sm text-center py-8">
                No logs available yet
              </p>
            )}
          </div>
        </div>
      )}

      {/* Register Model Dialog */}
      {showRegisterDialog && job?.model_path && (
        <RegisterModelDialog
          jobId={job.id}
          modelPath={job.model_path}
          onClose={() => setShowRegisterDialog(false)}
          onSuccess={() => setShowRegisterDialog(false)}
        />
      )}

      {/* Delete Confirmation Modal */}
      {showDeleteConfirm && job && (
        <DeleteJobModal
          jobName={job.name}
          onConfirm={handleDeleteJob}
          onCancel={() => setShowDeleteConfirm(false)}
          isDeleting={deleteJobMutation.isPending}
        />
      )}

      {/* Cancel Confirmation Modal */}
      {showCancelConfirm && job && (
        <CancelJobModal
          jobName={job.name}
          onConfirm={confirmCancel}
          onCancel={() => setShowCancelConfirm(false)}
          isCancelling={cancelMutation.isPending}
        />
      )}
    </div>
  )
}

// Delete Confirmation Modal
interface DeleteJobModalProps {
  jobName: string
  onConfirm: () => void
  onCancel: () => void
  isDeleting: boolean
}

function DeleteJobModal({ jobName, onConfirm, onCancel, isDeleting }: DeleteJobModalProps) {
  // Notify parent frame about modal open/close
  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50" role="dialog" aria-modal="true" aria-labelledby="delete-modal-title">
      <div className="bg-white max-w-md w-full mx-4 flex flex-col rounded">
        {/* Header */}
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 id="delete-modal-title" className="text-xl font-semibold text-domino-text-primary">Delete Job</h3>
          <button onClick={onCancel} className="text-domino-text-muted hover:text-domino-text-primary transition-colors" aria-label="Close dialog">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        {/* Content */}
        <div className="px-6 pb-4">
          <p className="text-sm text-domino-text-secondary">
            Are you sure you want to delete <span className="font-medium text-domino-text-primary">"{jobName}"</span>?
            This action cannot be undone.
          </p>
        </div>
        {/* Footer */}
        <div className="flex justify-end items-center gap-3 px-6 py-4 border-t border-domino-border">
          <button onClick={onCancel} className="text-sm text-domino-accent-purple hover:underline">
            Cancel
          </button>
          <Button variant="danger" onClick={onConfirm} disabled={isDeleting}>
            {isDeleting ? 'Deleting...' : 'Delete'}
          </Button>
        </div>
      </div>
    </div>
  )
}

// Cancel Confirmation Modal
interface CancelJobModalProps {
  jobName: string
  onConfirm: () => void
  onCancel: () => void
  isCancelling: boolean
}

function CancelJobModal({ jobName, onConfirm, onCancel, isCancelling }: CancelJobModalProps) {
  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50" role="dialog" aria-modal="true" aria-labelledby="cancel-modal-title">
      <div className="bg-white max-w-md w-full mx-4 flex flex-col rounded">
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 id="cancel-modal-title" className="text-xl font-semibold text-domino-text-primary">Cancel Job</h3>
          <button
            onClick={onCancel}
            className="text-domino-text-muted hover:text-domino-text-primary transition-colors"
            aria-label="Close dialog"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div className="px-6 pb-4">
          <p className="text-sm text-domino-text-secondary">
            Are you sure you want to cancel <span className="font-medium text-domino-text-primary">"{jobName}"</span>?
            The job will be stopped and any progress will be lost.
          </p>
        </div>
        <div className="flex justify-end items-center gap-3 px-6 py-4 border-t border-domino-border">
          <button onClick={onCancel} className="text-sm text-domino-accent-purple hover:underline">
            Keep Running
          </button>
          <Button variant="danger" onClick={onConfirm} disabled={isCancelling}>
            {isCancelling ? 'Cancelling...' : 'Cancel Job'}
          </Button>
        </div>
      </div>
    </div>
  )
}

function MetadataRow({
  label,
  value,
  mono,
  capitalize: cap,
  children,
}: {
  label: string
  value?: string
  mono?: boolean
  capitalize?: boolean
  children?: React.ReactNode
}) {
  return (
    <tr className="hover:bg-domino-bg-secondary transition-colors">
      <td className={`px-4 py-3 text-sm text-domino-text-secondary ${cap ? 'capitalize' : ''}`}>
        {label}
      </td>
      <td className={`px-4 py-3 text-sm text-domino-text-primary border-l border-domino-border ${mono ? '' : ''} ${cap ? 'capitalize' : ''}`}>
        {children || value || '—'}
      </td>
    </tr>
  )
}

export default JobDetail
