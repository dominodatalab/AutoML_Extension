import { format } from 'date-fns'
import { Link } from 'react-router-dom'
import Badge from '../common/Badge'
import type { Job, JobStatus } from '../../types/job'
import { formatDuration } from '../../utils/formatters'
import { getFileName } from '../../utils/path'
import { toDominoTenantUrl } from '../../utils/dominoLinks'
import { buildAppPath } from '../../utils/appPath'

interface JobOverviewTabProps {
  job: Job | undefined
  isLoading: boolean
  currentStatus: string
  currentDominoStatus?: string
}

export function JobOverviewTab({ job, isLoading, currentStatus, currentDominoStatus }: JobOverviewTabProps) {
  const datasetLabel = getDatasetLabel(job, isLoading)
  const datasetLink = getDatasetLink(job)
  const datasetDetails = job?.file_path || job?.dataset_id || ''
  const dominoJobUrl = toDominoTenantUrl(job?.domino_job_url)
  const experimentUrl = toDominoTenantUrl(job?.experiment_run_url)

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
            <MetadataRow label="Model type" value={job?.model_type || (isLoading ? 'Loading...' : '\u2014')} capitalize />
            {job?.problem_type && <MetadataRow label="Problem type" value={job.problem_type} capitalize />}
            <MetadataRow label="Target column" value={job?.target_column || (isLoading ? 'Loading...' : '\u2014')} />
            <MetadataRow label="Dataset used">
              {datasetLink ? (
                <Link
                  to={datasetLink}
                  className="text-domino-accent-purple hover:underline break-all"
                  title={datasetDetails}
                >
                  {datasetLabel}
                </Link>
              ) : (
                datasetLabel
              )}
            </MetadataRow>
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
              <MetadataRow label="Domino Job ID" mono>
                {dominoJobUrl ? (
                  <a
                    href={dominoJobUrl}
                    target="_blank"
                    rel="noreferrer"
                    className="text-domino-accent-purple hover:underline break-all"
                    title="Open Domino Job"
                  >
                    {job.domino_job_id}
                  </a>
                ) : (
                  job.domino_job_id
                )}
              </MetadataRow>
            )}
            {currentDominoStatus && (
              <MetadataRow label="Domino Job Status" value={currentDominoStatus} />
            )}
            {job?.experiment_name && (
              <MetadataRow label="Experiment" value={job.experiment_name} />
            )}
            {(job?.experiment_id || job?.experiment_run_id) && (
              <MetadataRow label="Experiment ID" mono>
                {experimentUrl ? (
                  <a
                    href={experimentUrl}
                    target="_blank"
                    rel="noreferrer"
                    className="text-domino-accent-purple hover:underline break-all"
                    title="Open Experiment Run"
                  >
                    {job.experiment_name || job.experiment_id || job.experiment_run_id}
                    {job.experiment_name && (job.experiment_id || job.experiment_run_id) && (
                      <span className="text-domino-text-muted ml-1">(#{job.experiment_id || job.experiment_run_id})</span>
                    )}
                  </a>
                ) : (
                  <>
                    {job.experiment_name || job.experiment_id || job.experiment_run_id}
                    {job.experiment_name && (job.experiment_id || job.experiment_run_id) && (
                      <span className="text-domino-text-muted ml-1">(#{job.experiment_id || job.experiment_run_id})</span>
                    )}
                  </>
                )}
              </MetadataRow>
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

function getDatasetLabel(job: Job | undefined, isLoading: boolean): string {
  if (!job) return isLoading ? 'Loading...' : '\u2014'
  if (job.file_path) return getFileName(job.file_path)
  if (job.dataset_id) return job.dataset_id.replace(/^domino:/, '')
  return '\u2014'
}

function getDatasetLink(job: Job | undefined): string | null {
  if (!job) return null
  const params = new URLSearchParams()
  if (job.data_source) params.set('data_source', job.data_source)
  if (job.dataset_id) params.set('dataset_id', job.dataset_id)
  if (job.file_path) params.set('file_path', job.file_path)
  return buildAppPath('/eda', params)
}
