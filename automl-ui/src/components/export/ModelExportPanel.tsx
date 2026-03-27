import { useMemo, useState } from 'react'
import { ArrowDownTrayIcon, CheckCircleIcon, XCircleIcon, DocumentTextIcon, CubeIcon } from '@heroicons/react/24/outline'
import { Card, CardContent } from '../common/Card'
import Button from '../common/Button'
import { useExportNotebook, useExportDeploymentZip } from '../../hooks/useExport'

function normalizeModelType(rawModelType: string | null | undefined): 'tabular' | 'timeseries' | null {
  if (!rawModelType) {
    return null
  }

  let normalized = rawModelType.trim().toLowerCase()
  if (normalized.startsWith('modeltype.')) {
    normalized = normalized.split('.', 2)[1] || normalized
  }

  const compact = normalized.replace(/[_\-\s]/g, '')
  if (compact === 'tabular') {
    return 'tabular'
  }
  if (compact === 'timeseries') {
    return 'timeseries'
  }

  return null
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

interface ModelExportPanelProps {
  jobId: string
  jobName: string
  projectName?: string
  modelType: string
  problemType?: string | null
  onExportComplete?: (result: { success: boolean; path?: string; error?: string }) => void
}

export function ModelExportPanel({
  jobId,
  jobName,
  projectName: _projectName,
  modelType,
  problemType: _problemType,
  onExportComplete,
}: ModelExportPanelProps) {
  const [exportResult, setExportResult] = useState<{
    type: 'notebook' | null
    success: boolean
    message: string
  } | null>(null)

  const exportNotebookMutation = useExportNotebook()
  const normalizedModelType = normalizeModelType(modelType)
  const notebookSupported = normalizedModelType === 'tabular' || normalizedModelType === 'timeseries'

  // Docker export state (combined build + download)
  const exportZipMutation = useExportDeploymentZip()
  const imageName = useMemo(() => toImageName(jobName), [jobName])
  const [dockerError, setDockerError] = useState<string | null>(null)
  const [dockerDownloaded, setDockerDownloaded] = useState(false)

  const handleExportNotebook = async () => {
    try {
      const response = await exportNotebookMutation.mutateAsync(jobId)

      // Convert notebook JSON to blob and trigger download
      const notebookJson = JSON.stringify(response.notebook, null, 2)
      const blob = new Blob([notebookJson], { type: 'application/x-ipynb+json' })
      const url = window.URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = response.filename || 'automl_notebook.ipynb'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)

      setExportResult({
        type: 'notebook',
        success: true,
        message: `Notebook downloaded: ${response.filename}`,
      })
      onExportComplete?.({ success: true })
    } catch (error) {
      setExportResult({
        type: 'notebook',
        success: false,
        message: error instanceof Error ? error.message : 'Notebook export failed',
      })
      onExportComplete?.({
        success: false,
        error: error instanceof Error ? error.message : 'Notebook export failed',
      })
    }
  }

  const handleExportDocker = async () => {
    setDockerError(null)
    setDockerDownloaded(false)

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

      setDockerDownloaded(true)
      onExportComplete?.({ success: true })
    } catch (error) {
      setDockerError(error instanceof Error ? error.message : 'Failed to export Docker package')
      onExportComplete?.({
        success: false,
        error: error instanceof Error ? error.message : 'Failed to export Docker package',
      })
    }
  }

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {notebookSupported ? (
          <div className="border border-domino-border rounded-lg p-4">
            <div className="flex items-center gap-2 mb-3">
              <DocumentTextIcon className="h-5 w-5 text-domino-accent-green" />
              <h3 className="font-medium">Training Notebook</h3>
            </div>
            <p className="text-sm text-domino-text-secondary mb-4">
              Download a Jupyter notebook with the training configuration and evaluation workflow.
            </p>
            <Button
              variant="primary"
              size="sm"
              onClick={handleExportNotebook}
              isLoading={exportNotebookMutation.isPending}
              disabled={exportNotebookMutation.isPending}
            >
              <ArrowDownTrayIcon className="h-4 w-4 mr-1" />
              Download Notebook
            </Button>
          </div>
        ) : (
          <div className="border border-domino-border rounded-lg p-4">
            <p className="text-sm text-domino-text-secondary">
              Notebook export is available for tabular and time series models.
            </p>
          </div>
        )}

        {/* Docker Container Export */}
        <div className="border border-domino-border rounded-lg p-4">
        <div className="flex items-center gap-2 mb-3">
          <CubeIcon className="h-5 w-5 text-domino-accent-purple" />
          <h3 className="font-medium">Docker Container</h3>
        </div>
        <p className="text-sm text-domino-text-secondary mb-4">
          Export a Docker-ready deployment package with Dockerfile, inference script, and model artifacts.
        </p>

        <div className="space-y-3">
          {dockerDownloaded && (
            <div className="p-3 bg-domino-accent-green/5 border border-domino-accent-green/30 rounded text-sm text-domino-text-primary">
              Deployment package downloaded. Unzip and build:
              <pre className="mt-1 bg-domino-bg-tertiary border border-domino-border rounded p-3 text-xs overflow-auto">
                {`unzip deployment_${jobId}.zip -d deployment_package && cd deployment_package && docker build -t ${imageName}:latest .`}
              </pre>
            </div>
          )}

          {dockerError && (
            <div className="p-3 bg-domino-accent-red/5 border border-domino-accent-red/30 text-domino-accent-red text-sm rounded flex items-start gap-2">
              <XCircleIcon className="w-5 h-5 flex-shrink-0 mt-0.5" />
              <span>{dockerError}</span>
            </div>
          )}

          <Button
            variant="secondary"
            size="sm"
            onClick={handleExportDocker}
            isLoading={exportZipMutation.isPending}
            disabled={exportZipMutation.isPending}
          >
            <ArrowDownTrayIcon className="h-4 w-4 mr-1" />
            Download Docker Package (.zip)
          </Button>
        </div>
        </div>
      </div>

      {/* Notebook Export Result */}
      {exportResult && (
        <Card>
          <CardContent className="py-4">
            <div className={`flex items-start gap-3 ${exportResult.success ? 'text-domino-accent-green' : 'text-domino-accent-red'}`}>
              {exportResult.success ? (
                <CheckCircleIcon className="h-6 w-6 flex-shrink-0" />
              ) : (
                <XCircleIcon className="h-6 w-6 flex-shrink-0" />
              )}
              <div>
                <p className="font-medium">
                  {exportResult.success ? 'Export Successful' : 'Export Failed'}
                </p>
                <p className="text-sm text-domino-text-secondary mt-1">
                  {exportResult.message}
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  )
}

export default ModelExportPanel
