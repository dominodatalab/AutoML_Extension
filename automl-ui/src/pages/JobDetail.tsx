import { useEffect, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { format } from 'date-fns'
import { useJob, useJobStatus, useJobLogs, useCancelJob, useDeleteJob } from '../hooks/useJobs'
import { SimpleProgressBar } from '../components/training/SimpleProgressBar'
import { ModelDiagnosticsPanel } from '../components/diagnostics/ModelDiagnosticsPanel'
import { LearningCurvesPanel } from '../components/diagnostics/LearningCurvesPanel'
import { DeployModelApiDialog } from '../components/deployment/DeployModelApiDialog'
import { ExportDockerDialog } from '../components/export/ExportDockerDialog'
import { ModelExportPanel } from '../components/export/ModelExportPanel'
import { TimeSeriesForecastPanel } from '../components/timeseries/TimeSeriesForecastPanel'
import { InteractiveLeaderboard } from '../components/leaderboard/InteractiveLeaderboard'
import { ConfirmDialog } from '../components/common/ConfirmDialog'
import { useJobProgress } from '../hooks/useJobProgress'
import { JobHeader } from '../components/job/JobHeader'
import { JobTabNavigation } from '../components/job/JobTabNavigation'
import { JobOverviewTab } from '../components/job/JobOverviewTab'
import { DominoIntegrationsTab } from '../components/job/DominoIntegrationsTab'
import { useCapabilities } from '../hooks/useCapabilities'
import type { DetailTab } from '../components/job/JobTabNavigation'

function JobDetail() {
  const { jobId } = useParams<{ jobId: string }>()
  const { data: job, isLoading, refetch } = useJob(jobId!)
  const { data: statusData } = useJobStatus(jobId!, !!job && ['pending', 'running'].includes(job.status))
  const { data: logs } = useJobLogs(jobId!, 100)
  const cancelMutation = useCancelJob()

  const { dominoEnabled } = useCapabilities()
  const isTraining = !!job && ['pending', 'running'].includes(job.status)
  const { polledProgress, progressJobId, simulatedProgress } = useJobProgress(jobId, job, isTraining, refetch)

  const [activeTab, setActiveTab] = useState<DetailTab>('overview')
  const [showDeployApiDialog, setShowDeployApiDialog] = useState(false)
  const [showDockerExportDialog, setShowDockerExportDialog] = useState(false)
  const [showDeployDropdown, setShowDeployDropdown] = useState(false)
  const [showActionsDropdown, setShowActionsDropdown] = useState(false)
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false)
  const [showCancelConfirm, setShowCancelConfirm] = useState(false)

  const navigate = useNavigate()
  const deleteJobMutation = useDeleteJob()

  useEffect(() => {
    if (!job || !statusData?.status) {
      return
    }
    if (statusData.status !== job.status) {
      refetch()
    }
  }, [job?.status, statusData?.status, refetch])

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
  const validPolledProgress = progressJobId === jobId ? polledProgress : null
  const currentStatus = statusData?.status || validPolledProgress?.status || jobStatus
  const currentDominoStatus = statusData?.domino_job_status || job?.domino_job_status
  const isJobTerminal = ['completed', 'failed', 'cancelled'].includes(currentStatus)
  const rawProgress = validPolledProgress?.progress ?? job?.progress ?? 0

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
        modelType={job?.model_type}
        dominoEnabled={dominoEnabled}
      />

      {/* Progress bar for running jobs */}
      {['pending', 'running'].includes(currentStatus) && activeTab === 'overview' && (
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

      {activeTab === 'domino' && currentStatus === 'completed' && job && (
        <DominoIntegrationsTab job={job} />
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

export default JobDetail
