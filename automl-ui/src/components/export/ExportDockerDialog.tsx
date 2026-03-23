import { useEffect, useMemo, useState } from 'react'
import { useExportDeploymentZip } from '../../hooks/useExport'
import Button from '../common/Button'

// Helper to notify parent frame about modal state
function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}

interface ExportDockerDialogProps {
  jobId: string
  jobName: string
  projectName?: string
  modelType: string
  onClose: () => void
  onSuccess: () => void
}

function toImageName(value: string): string {
  const cleaned = value
    .toLowerCase()
    .replace(/[^a-z0-9-]+/g, '-')
    .replace(/-{2,}/g, '-')
    .replace(/^-+|-+$/g, '')
  if (!cleaned) {
    return 'automlapp-model'
  }
  return `automlapp-${cleaned}`.slice(0, 64)
}

export function ExportDockerDialog({
  jobId,
  jobName,
  modelType,
  onClose,
  onSuccess,
}: ExportDockerDialogProps) {
  const exportZipMutation = useExportDeploymentZip()
  const imageName = useMemo(() => toImageName(jobName), [jobName])

  const [submitError, setSubmitError] = useState<string | null>(null)
  const [downloaded, setDownloaded] = useState(false)

  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  const handleDownload = async () => {
    setSubmitError(null)

    try {
      const { blob, filename } = await exportZipMutation.mutateAsync({
        job_id: jobId,
        model_type: modelType,
      })

      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = filename
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)

      setDownloaded(true)
      onSuccess()
    } catch (error) {
      setSubmitError(error instanceof Error ? error.message : 'Failed to download Docker package')
    }
  }

  const dockerBuildCommand = `unzip deployment_package.zip -d deployment_package && cd deployment_package && docker build -t ${imageName}:latest .`

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white max-w-2xl w-full mx-4 flex flex-col">
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 className="text-xl font-semibold text-domino-text-primary">Export Docker Container</h3>
          <button onClick={onClose} className="text-domino-text-muted hover:text-domino-text-primary transition-colors">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {downloaded ? (
          <div className="px-6 pb-6 space-y-4">
            <div className="p-3 bg-domino-accent-green/5 border border-domino-accent-green/30 rounded text-sm text-domino-text-primary">
              Docker deployment package downloaded successfully.
            </div>

            <div>
              <p className="text-sm font-medium text-domino-text-primary">Build command</p>
              <pre className="mt-1 bg-domino-bg-tertiary border border-domino-border rounded p-3 text-xs overflow-auto">
                {dockerBuildCommand}
              </pre>
            </div>

            <div className="flex justify-end">
              <Button variant="primary" onClick={onClose}>
                Done
              </Button>
            </div>
          </div>
        ) : (
          <div>
            <div className="px-6 space-y-4">
              <p className="text-sm text-domino-text-secondary">
                Downloads a Docker-ready deployment package (.zip) for this trained model, including <code className="text-xs bg-domino-bg-tertiary px-1 py-0.5 rounded">Dockerfile</code>, <code className="text-xs bg-domino-bg-tertiary px-1 py-0.5 rounded">inference.py</code>, and model artifacts.
              </p>

              {submitError && (
                <div className="p-3 bg-domino-accent-red/5 border border-domino-accent-red/30 text-domino-accent-red text-sm rounded flex items-start gap-2">
                  <svg className="w-5 h-5 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span>{submitError}</span>
                </div>
              )}
            </div>

            <div className="flex justify-end items-center gap-3 px-6 py-4 mt-4 border-t border-domino-border">
              <button type="button" onClick={onClose} className="text-sm text-domino-accent-purple hover:underline">
                Cancel
              </button>
              <Button variant="primary" onClick={handleDownload} disabled={exportZipMutation.isPending}>
                {exportZipMutation.isPending ? 'Downloading...' : 'Download'}
              </Button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
