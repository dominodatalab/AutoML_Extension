import { useEffect, useMemo, useState } from 'react'
import { useExportDeployment } from '../../hooks/useExport'
import Button from '../common/Button'
import Input from '../common/Input'
import { getDefaultExportPath } from '../../utils/pathDefaults'

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

function sanitizePathSegment(value: string): string {
  return value.replace(/[^a-zA-Z0-9_-]/g, '_')
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
  projectName,
  modelType,
  onClose,
  onSuccess,
}: ExportDockerDialogProps) {
  const exportDeploymentMutation = useExportDeployment()

  const safeJobName = useMemo(() => sanitizePathSegment(jobName), [jobName])
  const safeProjectName = useMemo(
    () => sanitizePathSegment(projectName || 'automl'),
    [projectName],
  )
  const imageName = useMemo(() => toImageName(jobName), [jobName])
  const defaultOutputDir = useMemo(
    () => getDefaultExportPath(safeProjectName, safeJobName),
    [safeProjectName, safeJobName],
  )

  const [outputDir, setOutputDir] = useState(defaultOutputDir)
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [successData, setSuccessData] = useState<{
    outputDir: string
    files: string[]
  } | null>(null)

  useEffect(() => {
    setOutputDir(defaultOutputDir)
  }, [defaultOutputDir])

  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitError(null)

    const targetDir = outputDir.trim()
    if (!targetDir) {
      setSubmitError('Output directory is required')
      return
    }

    try {
      const result = await exportDeploymentMutation.mutateAsync({
        job_id: jobId,
        model_type: modelType,
        output_dir: targetDir,
      })

      if (!result.success) {
        setSubmitError(result.error || 'Failed to export Docker package')
        return
      }

      setSuccessData({
        outputDir: result.output_dir || `${targetDir}/deployment_package`,
        files: result.files || [],
      })
      onSuccess()
    } catch (error) {
      setSubmitError(error instanceof Error ? error.message : 'Failed to export Docker package')
    }
  }

  const dockerBuildCommand = successData
    ? `cd "${successData.outputDir}" && docker build -t ${imageName}:latest .`
    : ''

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

        {successData ? (
          <div className="px-6 pb-6 space-y-4">
            <div className="p-3 bg-domino-accent-green/5 border border-domino-accent-green/30 rounded text-sm text-domino-text-primary">
              Docker deployment package created at:
              <div className="mt-1 font-mono text-xs break-all">{successData.outputDir}</div>
            </div>

            {successData.files.length > 0 && (
              <div>
                <p className="text-sm font-medium text-domino-text-primary">Generated files</p>
                <ul className="list-disc list-inside text-sm text-domino-text-secondary mt-1">
                  {successData.files.map((file) => (
                    <li key={file}>{file}</li>
                  ))}
                </ul>
              </div>
            )}

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
          <form onSubmit={handleSubmit}>
            <div className="px-6 space-y-4">
              <p className="text-sm text-domino-text-secondary">
                Creates a Docker-ready deployment package for this trained model, including `Dockerfile`, `inference.py`, and model artifacts.
              </p>

              <div>
                <label className="label">Output Directory *</label>
                <Input
                  value={outputDir}
                  onChange={(e) => setOutputDir(e.target.value)}
                  placeholder="/mnt/data/<project>/exports/<job> (Domino) or ./local_data/exports/<project>/<job>"
                  required
                />
              </div>

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
              <Button variant="primary" type="submit" disabled={exportDeploymentMutation.isPending || !outputDir.trim()}>
                {exportDeploymentMutation.isPending ? 'Exporting...' : 'Export Docker Package'}
              </Button>
            </div>
          </form>
        )}
      </div>
    </div>
  )
}
