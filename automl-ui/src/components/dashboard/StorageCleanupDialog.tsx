import { useEffect, useMemo, useState } from 'react'
import {
  ArchiveBoxXMarkIcon,
  ArrowPathIcon,
  CircleStackIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline'
import { ConfirmDialog } from '../common/ConfirmDialog'
import Button from '../common/Button'
import Spinner from '../common/Spinner'
import { useCleanupOrphans, useOrphanPreview } from '../../hooks/useJobs'
import { useStore } from '../../store'
import { getErrorMessage } from '../../utils/errors'
import { formatFileSize } from '../../utils/formatters'
import { OrphanArtifact } from '../../api/jobs'

interface StorageCleanupDialogProps {
  isOpen: boolean
  onClose: () => void
}

function notifyModalOpen() {
  window.parent.postMessage({ type: 'domino-modal-open' }, '*')
}

function notifyModalClose() {
  window.parent.postMessage({ type: 'domino-modal-close' }, '*')
}

function SummaryStat({
  label,
  count,
  sizeLabel,
}: {
  label: string
  count: number
  sizeLabel: string
}) {
  return (
    <div className="bg-domino-bg-tertiary border border-domino-border p-3">
      <p className="text-xs uppercase tracking-wide text-domino-text-secondary">{label}</p>
      <p className="text-2xl text-domino-text-primary mt-1">{count}</p>
      <p className="text-xs text-domino-text-muted mt-1">{sizeLabel}</p>
    </div>
  )
}

function ArtifactSection({
  title,
  items,
  emptyText,
}: {
  title: string
  items: OrphanArtifact[]
  emptyText: string
}) {
  const visibleItems = items.slice(0, 20)
  const hiddenCount = Math.max(items.length - visibleItems.length, 0)

  return (
    <div className="border border-domino-border">
      <div className="px-4 py-3 border-b border-domino-border bg-domino-bg-tertiary">
        <h4 className="text-sm font-medium text-domino-text-primary">{title} ({items.length})</h4>
      </div>
      {items.length === 0 ? (
        <div className="px-4 py-5 text-sm text-domino-text-secondary">{emptyText}</div>
      ) : (
        <div className="max-h-48 overflow-y-auto divide-y divide-domino-border">
          {visibleItems.map((artifact) => (
            <div key={artifact.path} className="px-4 py-3">
              <div className="flex items-center justify-between gap-3">
                <p className="text-sm text-domino-text-primary truncate" title={artifact.name}>
                  {artifact.name}
                </p>
                <span className="text-xs text-domino-text-secondary whitespace-nowrap">
                  {formatFileSize(artifact.size_bytes)}
                </span>
              </div>
              <p className="text-xs text-domino-text-muted truncate mt-1" title={artifact.path}>
                {artifact.path}
              </p>
            </div>
          ))}
          {hiddenCount > 0 && (
            <div className="px-4 py-3 text-xs text-domino-text-secondary">
              {hiddenCount} additional items hidden. Run cleanup to remove all orphaned artifacts.
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export function StorageCleanupDialog({ isOpen, onClose }: StorageCleanupDialogProps) {
  const addNotification = useStore((state) => state.addNotification)
  const [confirmOpen, setConfirmOpen] = useState(false)
  const {
    data: preview,
    isLoading,
    isFetching,
    error,
    refetch,
  } = useOrphanPreview(isOpen)
  const cleanupMutation = useCleanupOrphans()

  useEffect(() => {
    if (isOpen) {
      notifyModalOpen()
      return () => {
        notifyModalClose()
      }
    }
  }, [isOpen])

  const stats = useMemo(() => {
    const modelCount = preview?.orphaned_models.length ?? 0
    const mlflowCount = preview?.orphaned_mlflow_runs.length ?? 0
    const totalModelSize = preview?.total_orphaned_model_size_bytes ?? 0
    const totalMlflowSize = preview?.total_orphaned_mlflow_run_size_bytes ?? 0

    return {
      modelCount,
      mlflowCount,
      totalCount: modelCount + mlflowCount,
      totalModelSize,
      totalMlflowSize,
      totalSize: totalModelSize + totalMlflowSize,
    }
  }, [preview])

  const handleRunCleanup = async () => {
    try {
      const result = await cleanupMutation.mutateAsync()
      const deletedCount =
        result.models_deleted + result.mlflow_runs_deleted
      const freedSize = formatFileSize(result.total_size_freed_bytes)

      if (deletedCount > 0) {
        addNotification(
          `Removed ${deletedCount} orphaned artifacts and freed ${freedSize}.`,
          'success'
        )
      } else {
        addNotification('No orphaned artifacts were deleted.', 'info')
      }

      if (result.errors.length > 0) {
        addNotification(
          `Cleanup finished with ${result.errors.length} warning(s). Check service logs for details.`,
          'info'
        )
      }

      await refetch()
      setConfirmOpen(false)
    } catch (cleanupError) {
      addNotification(`Storage cleanup failed: ${getErrorMessage(cleanupError)}`, 'error')
    }
  }

  if (!isOpen) {
    return null
  }

  const refreshPreview = () => {
    refetch()
      .catch(() => {
        // Query-level error handling is shown in the UI
      })
  }

  return (
    <>
      <div
        className="fixed inset-0 bg-black/50 flex items-center justify-center z-50"
        role="dialog"
        aria-modal="true"
        aria-labelledby="storage-cleanup-title"
      >
        <div className="bg-white max-w-4xl w-full mx-4 flex flex-col rounded-sm shadow-lg max-h-[85vh]">
          <div className="flex items-center justify-between px-6 pt-6 pb-4 border-b border-domino-border">
            <div>
              <h3 id="storage-cleanup-title" className="text-xl font-semibold text-domino-text-primary">
                Storage cleanup
              </h3>
              <p className="text-sm text-domino-text-secondary mt-1">
                Review and remove orphaned artifacts not referenced by any AutoML job.
                Pending Domino jobs and deleted data references are reconciled before each scan.
              </p>
            </div>
            <button
              onClick={onClose}
              className="w-8 h-8 flex items-center justify-center text-domino-text-muted hover:text-domino-text-primary transition-colors rounded-full hover:bg-domino-bg-tertiary"
              aria-label="Close storage cleanup dialog"
            >
              <XMarkIcon className="w-5 h-5" />
            </button>
          </div>

          <div className="px-6 py-5 overflow-y-auto space-y-5">
            <div className="flex items-center justify-between">
              <p className="text-sm text-domino-text-secondary">
                Orphan preview scans model folders and local MLflow run artifacts.
              </p>
              <Button
                variant="ghost"
                size="sm"
                onClick={refreshPreview}
                disabled={isFetching || cleanupMutation.isPending}
                className="inline-flex items-center gap-1"
              >
                <ArrowPathIcon className="h-4 w-4" />
                Refresh
              </Button>
            </div>

            {isLoading ? (
              <div className="min-h-[140px] flex items-center justify-center">
                <Spinner />
              </div>
            ) : error ? (
              <div className="border border-domino-accent-red/30 bg-red-50 p-4">
                <p className="text-sm text-domino-accent-red">
                  Failed to load orphan preview: {getErrorMessage(error)}
                </p>
              </div>
            ) : (
              <>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                  <SummaryStat
                    label="Orphan models"
                    count={stats.modelCount}
                    sizeLabel={formatFileSize(stats.totalModelSize)}
                  />
                  <SummaryStat
                    label="Orphan MLflow runs"
                    count={stats.mlflowCount}
                    sizeLabel={formatFileSize(stats.totalMlflowSize)}
                  />
                  <SummaryStat
                    label="Total orphaned"
                    count={stats.totalCount}
                    sizeLabel={formatFileSize(stats.totalSize)}
                  />
                </div>

                <div className="grid grid-cols-1 gap-4">
                  <ArtifactSection
                    title="Orphaned model directories"
                    items={preview?.orphaned_models ?? []}
                    emptyText="No orphaned model directories found."
                  />
                  <ArtifactSection
                    title="Orphaned MLflow runs"
                    items={preview?.orphaned_mlflow_runs ?? []}
                    emptyText="No orphaned MLflow runs found."
                  />
                </div>
              </>
            )}
          </div>

          <div className="flex items-center justify-between gap-3 px-6 py-4 border-t border-domino-border">
            <div className="flex items-center gap-2 text-xs text-domino-text-secondary">
              <CircleStackIcon className="h-4 w-4" />
              <span>Only artifacts with no matching DB job references are deleted.</span>
            </div>
            <div className="flex items-center gap-3">
              <Button variant="ghost" onClick={onClose} disabled={cleanupMutation.isPending}>
                Close
              </Button>
              <Button
                variant="danger"
                onClick={() => setConfirmOpen(true)}
                disabled={stats.totalCount === 0 || isLoading || cleanupMutation.isPending}
                className="inline-flex items-center gap-2"
              >
                <ArchiveBoxXMarkIcon className="h-4 w-4" />
                Clean orphaned artifacts
              </Button>
            </div>
          </div>
        </div>
      </div>

      <ConfirmDialog
        isOpen={confirmOpen}
        onClose={() => setConfirmOpen(false)}
        onConfirm={handleRunCleanup}
        title="Clean orphaned artifacts"
        message={`Delete ${stats.totalCount} orphaned artifacts and free up to ${formatFileSize(stats.totalSize)}. This action cannot be undone.`}
        confirmLabel={cleanupMutation.isPending ? 'Cleaning...' : 'Clean now'}
        variant="danger"
        isLoading={cleanupMutation.isPending}
      />
    </>
  )
}
