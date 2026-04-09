import { useState, useEffect, FormEvent } from 'react'
import { useRegistry } from '../../hooks/useRegistry'

// Helper to notify parent frame about modal state
function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}
import Button from '../common/Button'
import Input from '../common/Input'

interface RegisterModelDialogProps {
  jobId: string
  onClose: () => void
  onSuccess: () => void
}

export function RegisterModelDialog({ jobId, onClose, onSuccess }: RegisterModelDialogProps) {
  const { registerModel, loading, error } = useRegistry()
  const [modelName, setModelName] = useState('')
  const [description, setDescription] = useState('')
  const [submitError, setSubmitError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)

  // Notify parent frame about modal open/close
  useEffect(() => {
    notifyModalOpen()
    return () => {
      notifyModalClose()
    }
  }, [])

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setSubmitError(null)

    try {
      const result = await registerModel(jobId, modelName, description)
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
          <h3 className="text-xl font-semibold text-domino-text-primary">Register in Domino Model Registry</h3>
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
            <p className="text-lg font-medium text-domino-text-primary">Model Registered Successfully</p>
            <p className="text-sm text-domino-text-secondary mt-1">
              {modelName} has been added to Domino Model Registry.
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
                <label className="label">Description</label>
                <textarea
                  className="w-full px-[11px] py-[4px] border border-domino-border rounded-[2px] text-sm text-domino-text-primary placeholder-domino-text-muted focus:outline-none focus:border-domino-accent-purple transition-all duration-200"
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
