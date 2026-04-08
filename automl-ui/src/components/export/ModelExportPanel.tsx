import { useState } from 'react'
import { ArrowDownTrayIcon, CheckCircleIcon, XCircleIcon, DocumentTextIcon } from '@heroicons/react/24/outline'
import { Card, CardContent } from '../common/Card'
import Button from '../common/Button'
import { useExportNotebook } from '../../hooks/useExport'

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

interface ModelExportPanelProps {
  jobId: string
  modelType: string
  onExportComplete?: (result: { success: boolean; path?: string; error?: string }) => void
}

export function ModelExportPanel({
  jobId,
  modelType,
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

  const handleExportNotebook = async () => {
    try {
      const response = await exportNotebookMutation.mutateAsync(jobId)

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

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 gap-4">
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
      </div>

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
