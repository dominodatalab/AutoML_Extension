import { useState } from 'react'
import { ArrowDownTrayIcon, DocumentDuplicateIcon, CheckCircleIcon, XCircleIcon, DocumentTextIcon } from '@heroicons/react/24/outline'
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card'
import Button from '../common/Button'
import Spinner from '../common/Spinner'
import { useExportDeployment, useSupportedFormats, useExportNotebook } from '../../hooks/useExport'

interface ModelExportPanelProps {
  jobId: string
  jobName: string
  projectName?: string
  modelType: string
  problemType?: string | null
  onExportComplete?: (result: { success: boolean; path?: string; error?: string }) => void
}

export function ModelExportPanel({ jobId, jobName, projectName, modelType, problemType, onExportComplete }: ModelExportPanelProps) {
  // Sanitize names for file paths (replace spaces with underscores, remove special chars)
  const sanitizeName = (name: string) => name.replace(/[^a-zA-Z0-9_-]/g, '_')
  const safeJobName = sanitizeName(jobName)
  const safeProjectName = projectName ? sanitizeName(projectName) : 'automl'

  const [outputDir, setOutputDir] = useState(`/domino/datasets/local/${safeProjectName}/${safeJobName}`)
  const [optimizeForInference, setOptimizeForInference] = useState(true)
  const [exportResult, setExportResult] = useState<{
    type: 'deployment' | 'notebook' | null
    success: boolean
    message: string
    files?: string[]
  } | null>(null)

  const { data: formats, isLoading: formatsLoading } = useSupportedFormats()
  const exportDeploymentMutation = useExportDeployment()
  const exportNotebookMutation = useExportNotebook()

  const handleExportDeployment = async () => {
    try {
      const result = await exportDeploymentMutation.mutateAsync({
        job_id: jobId,
        model_type: modelType,
        output_dir: outputDir,
        optimize_for_inference: optimizeForInference,
      })

      setExportResult({
        type: 'deployment',
        success: result.success,
        message: result.success
          ? `Deployment package created: ${result.output_dir}`
          : result.error || 'Export failed',
        files: result.files,
      })

      onExportComplete?.({
        success: result.success,
        path: result.output_dir,
        error: result.error,
      })
    } catch (error) {
      setExportResult({
        type: 'deployment',
        success: false,
        message: error instanceof Error ? error.message : 'Export failed',
      })
    }
  }

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
    } catch (error) {
      setExportResult({
        type: 'notebook',
        success: false,
        message: error instanceof Error ? error.message : 'Notebook export failed',
      })
    }
  }

  const formatInfo = formats?.[modelType as keyof typeof formats]
  const deploymentSupported = formatInfo?.deployment_package?.supported
  // Notebook export is only available for tabular models with binary problem type
  const notebookSupported = modelType === 'tabular' && problemType === 'binary'

  if (formatsLoading) {
    return (
      <div className="flex items-center justify-center py-8">
        <Spinner size="lg" />
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <ArrowDownTrayIcon className="h-5 w-5" />
            Export Model
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {/* Deployment Package */}
              <div className="border border-domino-border rounded-lg p-4">
                <div className="flex items-center gap-2 mb-3">
                  <DocumentDuplicateIcon className="h-5 w-5 text-domino-accent-purple" />
                  <h3 className="font-medium">Deployment Package</h3>
                </div>
                <p className="text-sm text-domino-text-secondary mb-4">
                  {formatInfo?.deployment_package?.description || 'Create complete deployment package with inference script'}
                </p>

                <div className="space-y-3 mb-4">
                  <div>
                    <label className="block text-xs text-domino-text-secondary mb-1">
                      Output Directory
                    </label>
                    <input
                      type="text"
                      value={outputDir}
                      onChange={(e) => setOutputDir(e.target.value)}
                      className="w-full px-3 py-2 text-sm bg-domino-bg-secondary border border-domino-border rounded-md focus:outline-none focus:ring-2 focus:ring-domino-accent-purple"
                    />
                  </div>

                  <label className="flex items-center gap-2">
                    <input
                      type="checkbox"
                      checked={optimizeForInference}
                      onChange={(e) => setOptimizeForInference(e.target.checked)}
                      className="rounded border-domino-border"
                    />
                    <span className="text-sm text-domino-text-secondary">
                      Optimize for inference
                    </span>
                  </label>
                </div>

                <Button
                  variant={deploymentSupported ? 'primary' : 'secondary'}
                  size="sm"
                  onClick={handleExportDeployment}
                  isLoading={exportDeploymentMutation.isPending}
                  disabled={!deploymentSupported || exportDeploymentMutation.isPending}
                >
                  {deploymentSupported ? 'Create Package' : 'Not Supported'}
                </Button>
              </div>

              {/* Notebook Export - Only for binary classification */}
              {notebookSupported && (
                <div className="border border-domino-border rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-3">
                    <DocumentTextIcon className="h-5 w-5 text-domino-accent-green" />
                    <h3 className="font-medium">Training Notebook</h3>
                  </div>
                  <p className="text-sm text-domino-text-secondary mb-4">
                    Download a Jupyter notebook with the training configuration, evaluation, and deployment code.
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
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Export Result */}
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
                {exportResult.files && exportResult.files.length > 0 && (
                  <div className="mt-3">
                    <p className="text-sm text-domino-text-secondary">Files created:</p>
                    <ul className="list-disc list-inside text-sm text-domino-text-primary mt-1">
                      {exportResult.files.map((file) => (
                        <li key={file} className="">{file}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Package Contents Info */}
      <Card>
        <CardHeader>
          <CardTitle>Deployment Package Contents</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="bg-domino-bg-tertiary rounded-lg p-3">
              <p className="font-medium text-sm">model/</p>
              <p className="text-xs text-domino-text-muted mt-1">
                Trained model artifacts
              </p>
            </div>
            <div className="bg-domino-bg-tertiary rounded-lg p-3">
              <p className="font-medium text-sm">inference.py</p>
              <p className="text-xs text-domino-text-muted mt-1">
                Python inference script
              </p>
            </div>
            <div className="bg-domino-bg-tertiary rounded-lg p-3">
              <p className="font-medium text-sm">requirements.txt</p>
              <p className="text-xs text-domino-text-muted mt-1">
                Python dependencies
              </p>
            </div>
            <div className="bg-domino-bg-tertiary rounded-lg p-3">
              <p className="font-medium text-sm">Dockerfile</p>
              <p className="text-xs text-domino-text-muted mt-1">
                Container configuration
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

export default ModelExportPanel
