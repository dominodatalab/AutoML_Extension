import { useEffect, useMemo, useState } from 'react'
import { useDeployments } from '../../hooks/useDeployments'
import Button from '../common/Button'
import Input from '../common/Input'

// Helper to notify parent frame about modal state
function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}

interface DeployModelApiDialogProps {
  jobId: string
  defaultModelName: string
  onClose: () => void
  onSuccess: () => void
}

function toModelApiName(name: string): string {
  const normalized = name
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9-]+/g, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-+|-+$/g, '')

  if (!normalized) {
    return 'automlapp-model-api'
  }

  return `automlapp-${normalized}`.slice(0, 64)
}

const PYTHON_IDENTIFIER = /^[A-Za-z_][A-Za-z0-9_]*$/

export function DeployModelApiDialog({
  jobId,
  defaultModelName,
  onClose,
  onSuccess,
}: DeployModelApiDialogProps) {
  const { deployFromJob, loading, error } = useDeployments()
  const defaultApiName = useMemo(() => toModelApiName(defaultModelName), [defaultModelName])

  const [modelName, setModelName] = useState(defaultApiName)
  const [functionName, setFunctionName] = useState('predict')
  const [minReplicas, setMinReplicas] = useState(1)
  const [maxReplicas, setMaxReplicas] = useState(1)
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)
  const [endpointUrl, setEndpointUrl] = useState<string | null>(null)

  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitError(null)

    const name = modelName.trim()
    const fn = functionName.trim()

    if (!name) {
      setSubmitError('Model API name is required')
      return
    }

    if (!fn) {
      setSubmitError('Prediction function is required')
      return
    }

    if (!PYTHON_IDENTIFIER.test(fn)) {
      setSubmitError('Prediction function must be a valid Python identifier')
      return
    }

    if (maxReplicas < minReplicas) {
      setSubmitError('Max replicas must be greater than or equal to min replicas')
      return
    }

    const result = await deployFromJob({
      job_id: jobId,
      model_name: name,
      function_name: fn,
      min_replicas: minReplicas,
      max_replicas: maxReplicas,
    })

    if (result?.success) {
      setSuccess(true)
      setEndpointUrl(result.url || result.endpoint_url || null)
      setTimeout(() => {
        onSuccess()
        onClose()
      }, 1500)
      return
    }

    // If the request threw, useDeployments.error carries the backend message.
    if (!result) {
      return
    }

    setSubmitError(result.error || result.message || 'Failed to publish Domino Model API')
  }

  const displayError = submitError || error

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white max-w-md w-full mx-4 flex flex-col">
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 className="text-xl font-semibold text-domino-text-primary">Publish Domino Model API</h3>
          <button onClick={onClose} className="text-domino-text-muted hover:text-domino-text-primary transition-colors">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {success ? (
          <div className="px-6 py-8 text-center">
            <div className="w-16 h-16 mx-auto bg-domino-accent-green/10 rounded-full flex items-center justify-center mb-4">
              <svg className="w-8 h-8 text-domino-accent-green" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <p className="text-lg font-medium text-domino-text-primary">Model API Deployment Started</p>
            <p className="text-sm text-domino-text-secondary mt-1">
              Domino is provisioning your Model API.
            </p>
            {endpointUrl && (
              <p className="text-xs text-domino-text-secondary mt-3 break-all">
                Endpoint: <span className="text-domino-text-primary">{endpointUrl}</span>
              </p>
            )}
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            <div className="px-6 space-y-4">
              <p className="text-sm text-domino-text-secondary">
                Create and deploy a Domino Model API directly from this completed AutoML job.
              </p>

              <div>
                <label className="label">Model API Name *</label>
                <Input
                  value={modelName}
                  onChange={(e) => setModelName(e.target.value)}
                  placeholder="automlapp-my-model"
                  required
                />
              </div>

              <div>
                <label className="label">Prediction Function</label>
                <Input
                  value={functionName}
                  onChange={(e) => setFunctionName(e.target.value)}
                  placeholder="predict"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="label">Min Replicas</label>
                  <Input
                    type="number"
                    min={0}
                    value={minReplicas}
                    onChange={(e) => setMinReplicas(Number(e.target.value) || 0)}
                  />
                </div>
                <div>
                  <label className="label">Max Replicas</label>
                  <Input
                    type="number"
                    min={1}
                    value={maxReplicas}
                    onChange={(e) => setMaxReplicas(Number(e.target.value) || 1)}
                  />
                </div>
              </div>

              {displayError && (
                <div className="p-3 bg-domino-accent-red/5 border border-domino-accent-red/30 text-domino-accent-red text-sm rounded flex items-start gap-2">
                  <svg className="w-5 h-5 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span>{displayError}</span>
                </div>
              )}
            </div>

            <div className="flex justify-end items-center gap-3 px-6 py-4 mt-4 border-t border-domino-border">
              <button type="button" onClick={onClose} className="text-sm text-domino-accent-purple hover:underline">
                Cancel
              </button>
              <Button variant="primary" type="submit" disabled={loading || !modelName.trim()}>
                {loading ? 'Publishing...' : 'Publish API'}
              </Button>
            </div>
          </form>
        )}
      </div>
    </div>
  )
}
