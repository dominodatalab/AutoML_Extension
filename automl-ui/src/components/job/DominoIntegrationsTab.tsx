import { useEffect } from 'react'
import type { Job } from '../../types/job'
import type { ModelApi, Deployment } from '../../types/deployment'
import { useDeployments } from '../../hooks/useDeployments'
import { toDominoTenantUrl } from '../../utils/dominoLinks'

interface DominoIntegrationsTabProps {
  job: Job
}

const STATUS_STYLES: Record<string, string> = {
  running: 'bg-domino-accent-green/10 text-domino-accent-green',
  starting: 'bg-domino-accent-purple/10 text-domino-accent-purple',
  building: 'bg-domino-accent-purple/10 text-domino-accent-purple',
  pending: 'bg-domino-accent-yellow/15 text-[#998A12]',
  stopped: 'bg-domino-text-muted/15 text-domino-text-muted',
  stopping: 'bg-domino-text-muted/15 text-domino-text-muted',
  failed: 'bg-domino-accent-red/10 text-domino-accent-red',
}

function StatusBadge({ status }: { status: string }) {
  const style = STATUS_STYLES[status] || 'bg-domino-text-muted/15 text-domino-text-muted'
  return (
    <span className={`inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium capitalize ${style}`}>
      {status}
    </span>
  )
}

export function DominoIntegrationsTab({ job }: DominoIntegrationsTabProps) {
  const { modelApis, deployments, loading, fetchModelApis, fetchDeployments } = useDeployments()
  const experimentUrl = toDominoTenantUrl(job.experiment_run_url)
  const modelRegistryUrl = toDominoTenantUrl(job.model_registry_url)

  useEffect(() => {
    fetchModelApis()
    fetchDeployments()
  }, [fetchModelApis, fetchDeployments])

  // Build a map of modelApiId → deployments for that API
  const deploymentsByApi = new Map<string, Deployment[]>()
  for (const d of deployments) {
    const list = deploymentsByApi.get(d.modelApiId) || []
    list.push(d)
    deploymentsByApi.set(d.modelApiId, list)
  }

  return (
    <div className="space-y-6">
      {/* Model Registry */}
      <SectionCard
        title="Model Registry"
        description="Registered model versions tracked in Domino."
      >
        {job.is_registered && job.registered_model_name ? (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-domino-accent-green/10 text-domino-accent-green">
                <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                </svg>
                Registered
              </span>
            </div>
            <dl className="grid grid-cols-[auto_1fr] gap-x-6 gap-y-2 text-sm">
              <dt className="text-domino-text-secondary">Model name</dt>
              <dd className="text-domino-text-primary font-medium">
                {modelRegistryUrl ? (
                  <a href={modelRegistryUrl} target="_blank" rel="noreferrer" className="text-[#3B3BD3] hover:underline">
                    {job.registered_model_name}
                    <ExternalLinkIcon className="inline ml-1 -mt-0.5" />
                  </a>
                ) : (
                  job.registered_model_name
                )}
              </dd>
              <dt className="text-domino-text-secondary">Version</dt>
              <dd className="text-domino-text-primary">{job.registered_model_version || '\u2014'}</dd>
            </dl>
          </div>
        ) : (
          <EmptyState
            message="No model registered in Domino yet."
            action="Register via the Deploy menu in the header."
          />
        )}
      </SectionCard>

      {/* Model APIs & Deployments */}
      <SectionCard
        title="Model APIs"
        description="Domino Model API endpoints available in this project."
      >
        {loading ? (
          <div className="text-center py-4">
            <p className="text-sm text-domino-text-muted">Loading model APIs...</p>
          </div>
        ) : modelApis.length > 0 ? (
          <div className="space-y-4">
            {modelApis.map((api) => (
              <ModelApiRow
                key={api.id}
                api={api}
                deployments={deploymentsByApi.get(api.id) || []}
              />
            ))}
          </div>
        ) : (
          <EmptyState
            message="No Model APIs in this project yet."
            action="Publish via the Deploy menu in the header."
          />
        )}
      </SectionCard>

      {/* Experiment Tracking */}
      <SectionCard
        title="Experiment Tracking"
        description="MLflow experiment runs and metrics logged during training."
      >
        {experimentUrl ? (
          <div className="space-y-3">
            <dl className="grid grid-cols-[auto_1fr] gap-x-6 gap-y-2 text-sm">
              {job.experiment_name && (
                <>
                  <dt className="text-domino-text-secondary">Experiment</dt>
                  <dd>
                    <a href={experimentUrl} target="_blank" rel="noreferrer" className="text-sm text-[#3B3BD3] hover:underline">
                      {job.experiment_name}
                      <ExternalLinkIcon className="inline ml-1 -mt-0.5" />
                    </a>
                  </dd>
                </>
              )}
              {(job.experiment_id || job.experiment_run_id) && (
                <>
                  <dt className="text-domino-text-secondary">Run</dt>
                  <dd>
                    <a href={experimentUrl} target="_blank" rel="noreferrer" className="text-sm text-[#3B3BD3] hover:underline">
                      {job.name}
                      <ExternalLinkIcon className="inline ml-1 -mt-0.5" />
                    </a>
                    <div className="text-xs font-mono text-domino-text-muted mt-0.5 break-all">
                      {job.experiment_run_id || job.experiment_id}
                    </div>
                  </dd>
                </>
              )}
            </dl>
          </div>
        ) : (
          <EmptyState message="No experiment tracking data for this job." />
        )}
      </SectionCard>
    </div>
  )
}

function ModelApiRow({ api, deployments }: { api: ModelApi; deployments: Deployment[] }) {
  return (
    <div className="border border-domino-border rounded p-3 space-y-2">
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium text-domino-text-primary">{api.name}</span>
        {api.createdAt && (
          <span className="text-xs text-domino-text-muted">
            {new Date(api.createdAt).toLocaleDateString()}
          </span>
        )}
      </div>
      {api.description && (
        <p className="text-xs text-domino-text-secondary">{api.description}</p>
      )}
      {deployments.length > 0 ? (
        <div className="space-y-1.5 pt-1">
          {deployments.map((d) => (
            <div key={d.id} className="flex items-center gap-3 text-xs">
              <StatusBadge status={d.status} />
              {d.url ? (
                <a
                  href={toDominoTenantUrl(d.url) || d.url}
                  target="_blank"
                  rel="noreferrer"
                  className="text-[#3B3BD3] hover:underline truncate"
                >
                  {d.url}
                  <ExternalLinkIcon className="inline ml-1 -mt-0.5" />
                </a>
              ) : (
                <span className="text-domino-text-muted">No endpoint URL</span>
              )}
            </div>
          ))}
        </div>
      ) : (
        <p className="text-xs text-domino-text-muted pt-1">No active deployments</p>
      )}
    </div>
  )
}

function SectionCard({
  title,
  description,
  children,
}: {
  title: string
  description: string
  children: React.ReactNode
}) {
  return (
    <div className="border border-domino-border rounded overflow-hidden">
      <div className="bg-domino-bg-secondary px-4 py-2.5 border-b border-domino-border">
        <h3 className="text-sm font-medium text-domino-text-primary">{title}</h3>
        <p className="text-xs text-domino-text-muted mt-0.5">{description}</p>
      </div>
      <div className="px-4 py-4">{children}</div>
    </div>
  )
}

function EmptyState({ message, action }: { message: string; action?: string }) {
  return (
    <div className="text-center py-4">
      <p className="text-sm text-domino-text-muted">{message}</p>
      {action && (
        <p className="text-xs text-domino-text-muted mt-1">{action}</p>
      )}
    </div>
  )
}

function ExternalLinkIcon({ className = '' }: { className?: string }) {
  return (
    <svg className={`w-3.5 h-3.5 ${className}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
      <path strokeLinecap="round" strokeLinejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
    </svg>
  )
}
