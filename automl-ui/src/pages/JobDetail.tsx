import { Suspense, lazy, useEffect, useRef, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { format } from 'date-fns'
import { useJob, useJobLogs, useCancelJob, useDeleteJob } from '../hooks/useJobs'
import { SimpleProgressBar } from '../components/training/SimpleProgressBar'
import { DeployModelApiDialog } from '../components/deployment/DeployModelApiDialog'
import { ExportDockerDialog } from '../components/export/ExportDockerDialog'
import { ConfirmDialog } from '../components/common/ConfirmDialog'
import { JobHeader } from '../components/job/JobHeader'
import { JobTabNavigation } from '../components/job/JobTabNavigation'
import { JobOverviewTab } from '../components/job/JobOverviewTab'
import { useCapabilities } from '../hooks/useCapabilities'
import { useJobLiveUpdates } from '../hooks/useJobLiveUpdates'
import type { DetailTab } from '../components/job/JobTabNavigation'

const ModelDiagnosticsPanel = lazy(() => import('../components/diagnostics/ModelDiagnosticsPanel').then((module) => ({ default: module.ModelDiagnosticsPanel })))
const LearningCurvesPanel = lazy(() => import('../components/diagnostics/LearningCurvesPanel').then((module) => ({ default: module.LearningCurvesPanel })))
const ModelExportPanel = lazy(() => import('../components/export/ModelExportPanel').then((module) => ({ default: module.ModelExportPanel })))
const InteractiveLeaderboard = lazy(() => import('../components/leaderboard/InteractiveLeaderboard').then((module) => ({ default: module.InteractiveLeaderboard })))
const DominoIntegrationsTab = lazy(() => import('../components/job/DominoIntegrationsTab').then((module) => ({ default: module.DominoIntegrationsTab })))

function JobDetail() {
  const { jobId } = useParams<{ jobId: string }>()
  const { data: job, isLoading, refetch } = useJob(jobId!)
  const [activeTab, setActiveTab] = useState<DetailTab>('overview')
  const { data: logs } = useJobLogs(jobId!, 100, activeTab === 'logs')
  const cancelMutation = useCancelJob()

  const { dominoEnabled } = useCapabilities()
  const liveUpdatesEnabled = !!jobId && (!job || ['pending', 'running'].includes(job.status))
  const { liveUpdate } = useJobLiveUpdates(jobId, {
    enabled: liveUpdatesEnabled,
    onTerminal: () => {
      void refetch()
    },
  })
  const liveStatus = liveUpdate?.status
  const currentStatus = liveStatus || job?.status || 'running'
  const isTraining = ['pending', 'running'].includes(currentStatus)

  const [showDeployApiDialog, setShowDeployApiDialog] = useState(false)
  const [showDockerExportDialog, setShowDockerExportDialog] = useState(false)
  const [showDeployDropdown, setShowDeployDropdown] = useState(false)
  const [showActionsDropdown, setShowActionsDropdown] = useState(false)
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false)
  const [showCancelConfirm, setShowCancelConfirm] = useState(false)
  const [simulatedProgress, setSimulatedProgress] = useState(0)
  const simulationStartRef = useRef<number | null>(null)

  const navigate = useNavigate()
  const deleteJobMutation = useDeleteJob()

  useEffect(() => {
    setSimulatedProgress(0)
    simulationStartRef.current = null
  }, [jobId])

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

  const currentDominoStatus = liveUpdate?.domino_job_status || job?.domino_job_status
  const isJobTerminal = ['completed', 'failed', 'cancelled'].includes(currentStatus)
  const rawProgress = liveUpdate?.progress ?? job?.progress ?? 0

  useEffect(() => {
    if (!job || !isTraining) {
      return
    }

    const startTime = job.started_at
      ? new Date(job.started_at).getTime()
      : Date.now()

    if (!simulationStartRef.current) {
      simulationStartRef.current = startTime
      setSimulatedProgress(Math.max(1, rawProgress))
    }

    const timeLimit = job.time_limit || 3600

    const updateProgress = () => {
      const now = Date.now()
      const elapsed = (now - (simulationStartRef.current || now)) / 1000
      const timeRatio = Math.min(elapsed / timeLimit, 1)
      const derivedProgress = timeRatio < 0.5
        ? Math.floor((timeRatio / 0.5) * 70)
        : Math.floor(70 + ((timeRatio - 0.5) / 0.5) * 25)
      setSimulatedProgress((prev) => Math.max(prev, rawProgress, Math.max(1, Math.min(derivedProgress, 95))))
    }

    updateProgress()
    const interval = setInterval(updateProgress, 1000)
    return () => clearInterval(interval)
  }, [job?.id, job?.started_at, job?.time_limit, isTraining, rawProgress])

  useEffect(() => {
    if (!isJobTerminal) {
      return
    }
    if (currentStatus === 'completed') {
      const interval = setInterval(() => {
        setSimulatedProgress((prev) => (prev >= 100 ? 100 : Math.min(prev + 5, 100)))
      }, 50)
      const timeout = setTimeout(() => clearInterval(interval), 1000)
      return () => {
        clearInterval(interval)
        clearTimeout(timeout)
      }
    }
    setSimulatedProgress(rawProgress)
  }, [currentStatus, isJobTerminal, rawProgress])

  // Use simulated progress for smooth time-based animation
  const currentProgress = isJobTerminal
    ? (currentStatus === 'completed' ? 100 : rawProgress)
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

      <JobHeader
        job={job}
        currentStatus={currentStatus}
        standaloneMode={!dominoEnabled}
        cancelIsPending={cancelMutation.isPending}
        showDeployDropdown={showDeployDropdown}
        showActionsDropdown={showActionsDropdown}
        onCancel={handleCancel}
        onToggleDeployDropdown={() => setShowDeployDropdown(!showDeployDropdown)}
        onCloseDeployDropdown={() => setShowDeployDropdown(false)}
        onOpenDeployApiDialog={() => {
          setShowDeployDropdown(false)
          setShowDeployApiDialog(true)
        }}
        onOpenDockerExportDialog={() => {
          setShowDeployDropdown(false)
          setShowDockerExportDialog(true)
        }}
        onToggleActionsDropdown={() => setShowActionsDropdown(!showActionsDropdown)}
        onCloseActionsDropdown={() => setShowActionsDropdown(false)}
        onOpenDeleteConfirm={() => {
          setShowActionsDropdown(false)
          setShowDeleteConfirm(true)
        }}
      />

      <JobTabNavigation
        activeTab={activeTab}
        onTabChange={setActiveTab}
        currentStatus={currentStatus}
        dominoEnabled={dominoEnabled}
      />

      {/* Progress bar for active and failed jobs */}
      {['pending', 'running', 'failed', 'cancelled'].includes(currentStatus) && activeTab === 'overview' && (
        <div className="mb-6">
          <SimpleProgressBar
            progress={currentProgress}
            status={currentStatus}
          />
        </div>
      )}

      {/* Tab content */}
      {activeTab === 'overview' && (
        <JobOverviewTab
          job={job}
          isLoading={isLoading}
          currentStatus={currentStatus}
          currentDominoStatus={currentDominoStatus}
        />
      )}

      {activeTab === 'leaderboard' && currentStatus === 'completed' && job && (
        <Suspense fallback={<TabLoadingFallback />}>
          <InteractiveLeaderboard leaderboard={job.leaderboard || []} />
        </Suspense>
      )}

      {activeTab === 'diagnostics' && currentStatus === 'completed' && job && (
        <Suspense fallback={<TabLoadingFallback />}>
          <ModelDiagnosticsPanel job={job} />
        </Suspense>
      )}

      {activeTab === 'learning' && currentStatus === 'completed' && job && (
        <Suspense fallback={<TabLoadingFallback />}>
          <LearningCurvesPanel jobId={job.id} modelType={job.model_type} />
        </Suspense>
      )}

      {activeTab === 'export' && currentStatus === 'completed' && job && (
        <Suspense fallback={<TabLoadingFallback />}>
          <ModelExportPanel jobId={job.id} jobName={job.name} projectName={job.project_name} modelType={job.model_type} problemType={job.problem_type} />
        </Suspense>
      )}

      {activeTab === 'domino' && currentStatus === 'completed' && job && (
        <Suspense fallback={<TabLoadingFallback />}>
          <DominoIntegrationsTab job={job} />
        </Suspense>
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

      {/* Deploy Model API Dialog */}
      {showDeployApiDialog && job?.model_path && (
        <DeployModelApiDialog
          jobId={job.id}
          defaultModelName={job.name}
          onClose={() => setShowDeployApiDialog(false)}
          onSuccess={() => setShowDeployApiDialog(false)}
        />
      )}

      {/* Export Docker Container Dialog */}
      {showDockerExportDialog && job && (
        <ExportDockerDialog
          jobId={job.id}
          jobName={job.name}
          projectName={job.project_name}
          modelType={job.model_type}
          onClose={() => setShowDockerExportDialog(false)}
          onSuccess={() => {}}
        />
      )}

      {/* Delete Confirmation Modal */}
      {showDeleteConfirm && job && (
        <ConfirmDialog
          isOpen={true}
          onClose={() => setShowDeleteConfirm(false)}
          onConfirm={handleDeleteJob}
          title="Delete Job"
          message={`Are you sure you want to delete "${job.name}"? This action cannot be undone.`}
          confirmLabel={deleteJobMutation.isPending ? 'Deleting...' : 'Delete'}
          variant="danger"
          isLoading={deleteJobMutation.isPending}
        />
      )}

      {/* Cancel Confirmation Modal */}
      {showCancelConfirm && job && (
        <ConfirmDialog
          isOpen={true}
          onClose={() => setShowCancelConfirm(false)}
          onConfirm={confirmCancel}
          title="Cancel Job"
          message={`Are you sure you want to cancel "${job.name}"? The job will be stopped and any progress will be lost.`}
          confirmLabel={cancelMutation.isPending ? 'Cancelling...' : 'Cancel Job'}
          cancelLabel="Keep Running"
          variant="danger"
          isLoading={cancelMutation.isPending}
        />
      )}
    </div>
  )
}

function TabLoadingFallback() {
  return (
    <div className="border border-domino-border rounded p-6 text-sm text-domino-text-secondary">
      Loading tab...
    </div>
  )
}

export default JobDetail
