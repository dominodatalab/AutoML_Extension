import { format } from 'date-fns'
import Badge from '../common/Badge'
import type { Job, JobStatus } from '../../types/job'
import { formatDuration } from '../../utils/formatters'

interface JobOverviewTabProps {
  job: Job | undefined
  isLoading: boolean
  currentStatus: string
}

export function JobOverviewTab({ job, isLoading, currentStatus }: JobOverviewTabProps) {
  return (
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
            <MetadataRow label="Run ID" value={job?.id || (isLoading ? 'Loading...' : '\u2014')} mono />
            <MetadataRow label="Model type" value={job?.model_type || (isLoading ? 'Loading...' : '\u2014')} capitalize />
            {job?.problem_type && <MetadataRow label="Problem type" value={job.problem_type} capitalize />}
            <MetadataRow label="Target column" value={job?.target_column || (isLoading ? 'Loading...' : '\u2014')} />
            <MetadataRow label="Preset" value={job?.preset?.replace(/_/g, ' ') || (isLoading ? 'Loading...' : '\u2014')} capitalize />
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
                value={formatDuration(job.started_at, job.completed_at)}
              />
            )}
            <MetadataRow label="Status">
              <Badge status={currentStatus as JobStatus} isRegistered={job?.is_registered} />
            </MetadataRow>
            <MetadataRow
              label="Execution target"
              value={job?.execution_target === 'domino_job' ? 'Domino Job' : 'Local'}
            />
            {job?.domino_job_id && (
              <MetadataRow label="Domino Job ID" value={job.domino_job_id} mono />
            )}
            {job?.domino_job_status && (
              <MetadataRow label="Domino Job Status" value={job.domino_job_status} />
            )}
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
                  displayValue = String(value ?? '\u2014')
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
        {children || value || '\u2014'}
      </td>
    </tr>
  )
}
