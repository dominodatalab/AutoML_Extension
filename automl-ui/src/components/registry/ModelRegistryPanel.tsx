import { useState, useEffect } from 'react'
import { useRegistry } from '../../hooks/useRegistry'

// Helper to notify parent frame about modal state
function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}
import { Card } from '../common/Card'
import Button from '../common/Button'
import Badge from '../common/Badge'
import Spinner from '../common/Spinner'
import Input from '../common/Input'
import Select from '../common/Select'
import type { ModelVersion, ModelStage } from '../../types/registry'

interface ModelRegistryPanelProps {
  onModelSelect?: (modelName: string, version: string) => void
}

export function ModelRegistryPanel({ onModelSelect }: ModelRegistryPanelProps) {
  const {
    registeredModels,
    modelVersions,
    loading,
    error,
    fetchRegisteredModels,
    fetchModelVersions,
    transitionStage,
    deleteModelVersion,
    deleteModel,
  } = useRegistry()

  const [selectedModel, setSelectedModel] = useState<string | null>(null)
  const [showDeleteConfirm, setShowDeleteConfirm] = useState<string | null>(null)

  useEffect(() => {
    fetchRegisteredModels()
  }, [fetchRegisteredModels])

  useEffect(() => {
    if (selectedModel) {
      fetchModelVersions(selectedModel)
    }
  }, [selectedModel, fetchModelVersions])

  const handleStageChange = async (modelName: string, version: string, newStage: ModelStage) => {
    const result = await transitionStage(modelName, version, newStage, newStage === 'Production')
    if (result?.success) {
      fetchModelVersions(modelName)
    }
  }

  const handleDeleteVersion = async (modelName: string, version: string) => {
    const success = await deleteModelVersion(modelName, version)
    if (success) {
      fetchModelVersions(modelName)
      setShowDeleteConfirm(null)
    }
  }

  const handleDeleteModel = async (modelName: string) => {
    const success = await deleteModel(modelName)
    if (success) {
      fetchRegisteredModels()
      setSelectedModel(null)
      setShowDeleteConfirm(null)
    }
  }

  if (loading && registeredModels.length === 0) {
    return (
      <div className="flex items-center justify-center py-12">
        <Spinner size="lg" />
        <span className="ml-3 text-gray-600">Loading model registry...</span>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Model List */}
      <Card className="lg:col-span-1">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">Registered Models</h3>
          <Button variant="ghost" size="sm" onClick={() => fetchRegisteredModels()}>
            Refresh
          </Button>
        </div>

        {error && (
          <div className="p-3 bg-red-50 text-red-700 rounded mb-4">
            {error}
          </div>
        )}

        {registeredModels.length === 0 ? (
          <p className="text-gray-500 text-center py-8">
            No models registered yet
          </p>
        ) : (
          <div className="space-y-2 max-h-96 overflow-y-auto">
            {registeredModels.map((model) => (
              <div
                key={model.name}
                className={`p-3 rounded-lg cursor-pointer transition-colors ${
                  selectedModel === model.name
                    ? 'bg-blue-100 border border-blue-300'
                    : 'bg-gray-50 hover'
                }`}
                onClick={() => setSelectedModel(model.name)}
              >
                <div className="font-medium">{model.name}</div>
                <div className="text-sm text-gray-500 mt-1">
                  {model.latest_versions.length} version(s)
                </div>
                {model.latest_versions.some(v => v.stage === 'Production') && (
                  <Badge variant="success" className="mt-1">Production</Badge>
                )}
              </div>
            ))}
          </div>
        )}
      </Card>

      {/* Model Versions */}
      <Card className="lg:col-span-2">
        {selectedModel ? (
          <div>
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-lg font-semibold">{selectedModel}</h3>
                <p className="text-sm text-gray-500">
                  {modelVersions.length} version(s)
                </p>
              </div>
              <div className="flex space-x-2">
                <Button
                  variant="danger"
                  size="sm"
                  onClick={() => setShowDeleteConfirm(selectedModel)}
                >
                  Delete Model
                </Button>
              </div>
            </div>

            {modelVersions.length === 0 ? (
              <p className="text-gray-500 text-center py-8">
                No versions found
              </p>
            ) : (
              <div className="space-y-4">
                {modelVersions.map((version) => (
                  <VersionCard
                    key={version.version}
                    version={version}
                    modelName={selectedModel}
                    onStageChange={handleStageChange}
                    onDelete={(v) => setShowDeleteConfirm(`${selectedModel}:${v}`)}
                    onSelect={onModelSelect}
                  />
                ))}
              </div>
            )}
          </div>
        ) : (
          <div className="text-center py-12 text-gray-500">
            Select a model to view its versions
          </div>
        )}
      </Card>

      {/* Delete Confirmation Modal */}
      {showDeleteConfirm && (
        <DeleteConfirmModal
          item={showDeleteConfirm}
          onConfirm={() => {
            if (showDeleteConfirm.includes(':')) {
              const [model, version] = showDeleteConfirm.split(':')
              handleDeleteVersion(model, version)
            } else {
              handleDeleteModel(showDeleteConfirm)
            }
          }}
          onCancel={() => setShowDeleteConfirm(null)}
        />
      )}
    </div>
  )
}

interface VersionCardProps {
  version: ModelVersion
  modelName: string
  onStageChange: (modelName: string, version: string, stage: ModelStage) => void
  onDelete: (version: string) => void
  onSelect?: (modelName: string, version: string) => void
}

function VersionCard({ version, modelName, onStageChange, onDelete, onSelect }: VersionCardProps) {
  const [showStageSelect, setShowStageSelect] = useState(false)

  const getStageBadgeVariant = (stage: ModelStage) => {
    switch (stage) {
      case 'Production': return 'success'
      case 'Staging': return 'warning'
      case 'Archived': return 'error'
      default: return 'info'
    }
  }

  return (
    <div className="border rounded-lg p-4 bg-white">
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center space-x-2">
            <span className="font-medium">Version {version.version}</span>
            <Badge variant={getStageBadgeVariant(version.stage)}>
              {version.stage}
            </Badge>
          </div>
          {version.description && (
            <p className="text-sm text-gray-500 mt-1">{version.description}</p>
          )}
          <div className="text-xs text-gray-400 mt-2">
            Created: {version.creation_timestamp
              ? new Date(version.creation_timestamp).toLocaleString()
              : 'Unknown'}
          </div>
          {version.run_id && (
            <div className="text-xs text-gray-400">
              Run ID: {version.run_id.slice(0, 8)}...
            </div>
          )}
        </div>

        <div className="flex space-x-2">
          {onSelect && (
            <Button
              variant="primary"
              size="sm"
              onClick={() => onSelect(modelName, version.version)}
            >
              Use
            </Button>
          )}

          <div className="relative">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setShowStageSelect(!showStageSelect)}
            >
              Stage ▼
            </Button>
            {showStageSelect && (
              <div className="absolute right-0 mt-1 w-32 bg-white border rounded-lg shadow-lg z-10">
                {(['None', 'Staging', 'Production', 'Archived'] as ModelStage[]).map((stage) => (
                  <button
                    key={stage}
                    className={`w-full text-left px-3 py-2 text-sm hover ${
                      version.stage === stage ? 'bg-blue-50 text-blue-700' : 'dark'
                    }`}
                    onClick={() => {
                      onStageChange(modelName, version.version, stage)
                      setShowStageSelect(false)
                    }}
                  >
                    {stage}
                  </button>
                ))}
              </div>
            )}
          </div>

          <Button
            variant="danger"
            size="sm"
            onClick={() => onDelete(version.version)}
          >
            Delete
          </Button>
        </div>
      </div>

      {/* Tags */}
      {Object.keys(version.tags).length > 0 && (
        <div className="mt-3 flex flex-wrap gap-1">
          {Object.entries(version.tags).slice(0, 5).map(([key, value]) => (
            <span
              key={key}
              className="px-2 py-0.5 bg-gray-100 rounded text-xs"
              title={`${key}: ${value}`}
            >
              {key}: {value.slice(0, 20)}
            </span>
          ))}
        </div>
      )}
    </div>
  )
}

interface DeleteConfirmModalProps {
  item: string
  onConfirm: () => void
  onCancel: () => void
}

function DeleteConfirmModal({ item, onConfirm, onCancel }: DeleteConfirmModalProps) {
  const isVersion = item.includes(':')
  const displayName = isVersion ? `version ${item.split(':')[1]}` : `model "${item}"`

  // Notify parent frame about modal open/close
  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white max-w-md w-full mx-4 flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 className="text-xl font-semibold text-domino-text-primary">Confirm Delete</h3>
          <button onClick={onCancel} className="text-domino-text-muted hover:text-domino-text-primary transition-colors">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        {/* Content */}
        <div className="px-6 pb-4">
          <p className="text-sm text-domino-text-secondary">
            Are you sure you want to delete {displayName}?
            {!isVersion && ' This will delete all versions.'}
            This action cannot be undone.
          </p>
        </div>
        {/* Footer */}
        <div className="flex justify-end items-center gap-3 px-6 py-4 border-t border-domino-border">
          <button onClick={onCancel} className="text-sm text-domino-accent-purple hover:underline">
            Cancel
          </button>
          <Button variant="danger" onClick={onConfirm}>
            Delete
          </Button>
        </div>
      </div>
    </div>
  )
}

// Register Model Dialog
interface RegisterModelDialogProps {
  jobId: string
  modelPath: string
  onClose: () => void
  onSuccess: () => void
}

export function RegisterModelDialog({ jobId, modelPath, onClose, onSuccess }: RegisterModelDialogProps) {
  const { registerModel, loading, error } = useRegistry()
  const [modelName, setModelName] = useState('')
  const [description, setDescription] = useState('')
  const [modelType, setModelType] = useState('tabular')
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)

  // Notify parent frame about modal open/close
  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSubmitError(null)

    try {
      const result = await registerModel(modelPath, modelName, modelType, description, undefined, jobId)
      if (result?.success) {
        setSuccess(true)
        // Show success for a moment before closing
        setTimeout(() => {
          onSuccess()
          onClose()
        }, 1500)
      } else {
        setSubmitError(result?.error || 'Failed to register model')
      }
    } catch (err) {
      setSubmitError(err instanceof Error ? err.message : 'Failed to register model')
    }
  }

  const displayError = submitError || error

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white max-w-md w-full mx-4 flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 pt-6 pb-4">
          <h3 className="text-xl font-semibold text-domino-text-primary">Deploy to Model Registry</h3>
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
            <p className="text-lg font-medium text-domino-text-primary">Model Registered Successfully!</p>
            <p className="text-sm text-domino-text-secondary mt-1">
              {modelName} has been added to the registry.
            </p>
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            <div className="px-6 space-y-4">
              <div>
                <label className="label">Model Name *</label>
                <Input
                  value={modelName}
                  onChange={(e) => setModelName(e.target.value)}
                  placeholder="my-model"
                  required
                />
              </div>

              <div>
                <label className="label">Model Type</label>
                <Select
                  value={modelType}
                  onChange={(e) => setModelType(e.target.value)}
                  options={[
                    { value: 'tabular', label: 'Tabular' },
                    { value: 'timeseries', label: 'Time Series' },
                    { value: 'multimodal', label: 'Multimodal' },
                  ]}
                />
              </div>

              <div>
                <label className="label">Description</label>
                <textarea
                  className="w-full px-[11px] py-[4px] border border-[#d9d9d9] rounded-[2px] text-sm text-domino-text-primary placeholder-domino-text-muted focus:outline-none focus:border-domino-accent-purple transition-all duration-200"
                  rows={3}
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                  placeholder="Model description..."
                />
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

            {/* Footer */}
            <div className="flex justify-end items-center gap-3 px-6 py-4 mt-4 border-t border-domino-border">
              <button type="button" onClick={onClose} className="text-sm text-domino-accent-purple hover:underline">
                Cancel
              </button>
              <Button variant="primary" type="submit" disabled={loading || !modelName}>
                {loading ? 'Registering...' : 'Register'}
              </Button>
            </div>
          </form>
        )}
      </div>
    </div>
  )
}
