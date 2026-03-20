import { useState, useMemo, useEffect, useCallback } from 'react'
import { useJobs, useDeleteJob, useBulkDeleteJobs } from '../hooks/useJobs'
import Spinner from '../components/common/Spinner'
import { ConfirmDialog } from '../components/common/ConfirmDialog'
import { Job } from '../types/job'
import { DashboardFilters } from '../components/dashboard/DashboardFilters'
import { EmptyState } from '../components/dashboard/EmptyState'
import { JobTableView } from '../components/dashboard/JobTableView'
import { JobCardView } from '../components/dashboard/JobCardView'
import { BulkActionBar } from '../components/dashboard/BulkActionBar'
import { StorageCleanupDialog } from '../components/dashboard/StorageCleanupDialog'
import { useCapabilities } from '../hooks/useCapabilities'

type ViewMode = 'table' | 'card'

function Dashboard() {
  const { storageCleanup } = useCapabilities()
  const [viewMode, setViewMode] = useState<ViewMode>('table')
  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState<string>('')
  const [typeFilter, setTypeFilter] = useState<string>('')
  const [deleteConfirmJob, setDeleteConfirmJob] = useState<Job | null>(null)
  const [bulkDeleteConfirmOpen, setBulkDeleteConfirmOpen] = useState(false)
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set())
  const [storageCleanupOpen, setStorageCleanupOpen] = useState(false)

  const { data, isLoading, error } = useJobs({ limit: 100 })
  const deleteJobMutation = useDeleteJob()
  const bulkDeleteMutation = useBulkDeleteJobs()
  const allJobs = data?.jobs || []

  const handleDeleteJob = async (job: Job) => {
    try {
      await deleteJobMutation.mutateAsync(job.id)
      setDeleteConfirmJob(null)
    } catch (err) {
      console.error('Failed to delete job:', err)
    }
  }

  const filteredJobs = useMemo(() => {
    return allJobs.filter((job: Job) => {
      if (search && !job.name.toLowerCase().includes(search.toLowerCase())) return false
      if (statusFilter && job.status !== statusFilter) return false
      if (typeFilter && job.model_type !== typeFilter) return false
      return true
    })
  }, [allJobs, search, statusFilter, typeFilter])

  // Clear selection when filters or view mode change
  useEffect(() => {
    setSelectedIds(new Set())
  }, [search, statusFilter, typeFilter, viewMode])

  useEffect(() => {
    if (!storageCleanup && storageCleanupOpen) {
      setStorageCleanupOpen(false)
    }
  }, [storageCleanup, storageCleanupOpen])

  // Prune selection to only include visible job IDs
  useEffect(() => {
    const visibleIds = new Set(filteredJobs.map((j) => j.id))
    setSelectedIds((prev) => {
      const pruned = new Set([...prev].filter((id) => visibleIds.has(id)))
      return pruned.size === prev.size ? prev : pruned
    })
  }, [filteredJobs])

  const toggleJob = useCallback((jobId: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev)
      if (next.has(jobId)) next.delete(jobId)
      else next.add(jobId)
      return next
    })
  }, [])

  const toggleAll = useCallback(() => {
    setSelectedIds((prev) => {
      const allVisible = filteredJobs.map((j) => j.id)
      if (prev.size === allVisible.length) return new Set()
      return new Set(allVisible)
    })
  }, [filteredJobs])

  const isAllSelected = filteredJobs.length > 0 && selectedIds.size === filteredJobs.length
  const isIndeterminate = selectedIds.size > 0 && selectedIds.size < filteredJobs.length

  const activeSelectedCount = filteredJobs.filter(
    (j) => selectedIds.has(j.id) && ['pending', 'running'].includes(j.status)
  ).length

  const handleBulkDelete = async () => {
    try {
      const result = await bulkDeleteMutation.mutateAsync([...selectedIds])
      setBulkDeleteConfirmOpen(false)
      setSelectedIds(new Set())
      if (result.failed.length > 0) {
        console.error('Some jobs failed to delete:', result.failed)
      }
    } catch (err) {
      console.error('Bulk delete failed:', err)
    }
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <Spinner size="lg" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-domino-accent-red">Failed to load jobs</p>
      </div>
    )
  }

  return (
    <div>
      <DashboardFilters
        search={search}
        onSearchChange={setSearch}
        statusFilter={statusFilter}
        onStatusFilterChange={setStatusFilter}
        typeFilter={typeFilter}
        onTypeFilterChange={setTypeFilter}
        viewMode={viewMode}
        onViewModeChange={setViewMode}
        showStorageCleanup={storageCleanup}
        onStorageCleanupClick={() => setStorageCleanupOpen(true)}
      />

      {/* Bulk Action Bar */}
      <BulkActionBar
        selectedCount={selectedIds.size}
        onClearSelection={() => setSelectedIds(new Set())}
        onBulkDelete={() => setBulkDeleteConfirmOpen(true)}
        isDeleting={bulkDeleteMutation.isPending}
      />

      {/* Content */}
      {filteredJobs.length === 0 ? (
        <EmptyState hasJobs={allJobs.length > 0} />
      ) : viewMode === 'table' ? (
        <JobTableView
          jobs={filteredJobs}
          onDeleteRequest={setDeleteConfirmJob}
          selectedIds={selectedIds}
          isAllSelected={isAllSelected}
          isIndeterminate={isIndeterminate}
          onToggleJob={toggleJob}
          onToggleAll={toggleAll}
        />
      ) : (
        <JobCardView
          jobs={filteredJobs}
          onDeleteRequest={setDeleteConfirmJob}
          selectedIds={selectedIds}
          onToggleJob={toggleJob}
        />
      )}

      {/* Single Delete Confirmation Modal */}
      {deleteConfirmJob && (
        <ConfirmDialog
          isOpen={true}
          onClose={() => setDeleteConfirmJob(null)}
          onConfirm={() => handleDeleteJob(deleteConfirmJob)}
          title="Delete Job"
          message={`Are you sure you want to delete "${deleteConfirmJob.name}"? This action cannot be undone.`}
          confirmLabel={deleteJobMutation.isPending ? 'Deleting...' : 'Delete'}
          variant="danger"
          isLoading={deleteJobMutation.isPending}
        />
      )}

      {/* Bulk Delete Confirmation Modal */}
      {bulkDeleteConfirmOpen && (
        <ConfirmDialog
          isOpen={true}
          onClose={() => setBulkDeleteConfirmOpen(false)}
          onConfirm={handleBulkDelete}
          title="Delete Jobs"
          message={`Are you sure you want to delete ${selectedIds.size} ${selectedIds.size === 1 ? 'job' : 'jobs'}?${activeSelectedCount > 0 ? ` ${activeSelectedCount} active ${activeSelectedCount === 1 ? 'job' : 'jobs'} will be cancelled first.` : ''} This action cannot be undone.`}
          confirmLabel={bulkDeleteMutation.isPending ? 'Deleting...' : `Delete ${selectedIds.size} ${selectedIds.size === 1 ? 'job' : 'jobs'}`}
          variant="danger"
          isLoading={bulkDeleteMutation.isPending}
        />
      )}

      {/* Pagination info */}
      {filteredJobs.length > 0 && (
        <div className="flex items-center justify-end gap-2 mt-4 text-sm text-domino-text-secondary">
          <span>Showing 1–{filteredJobs.length} out of {filteredJobs.length}</span>
          <button className="h-[32px] w-[32px] flex items-center justify-center border border-domino-border rounded-[2px] text-domino-text-muted" disabled>
            &lt;
          </button>
          <button className="h-[32px] w-[32px] flex items-center justify-center border border-domino-accent-purple rounded-[2px] text-domino-accent-purple">
            1
          </button>
          <button className="h-[32px] w-[32px] flex items-center justify-center border border-domino-border rounded-[2px] text-domino-text-muted" disabled>
            &gt;
          </button>
        </div>
      )}

      {storageCleanup && (
        <StorageCleanupDialog
          isOpen={storageCleanupOpen}
          onClose={() => setStorageCleanupOpen(false)}
        />
      )}
    </div>
  )
}

export default Dashboard
