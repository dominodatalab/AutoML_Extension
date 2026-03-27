import { useState, useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import { format } from 'date-fns'
import {
  CubeIcon,
  DocumentTextIcon,
} from '@heroicons/react/24/outline'
import { Job } from '../../types/job'
import { getStatusColor, getStatusIcon } from '../../utils/formatters'
import { buildAppPath } from '../../utils/appPath'

function getDisplayStatus(job: Job): string {
  if (job.status === 'completed' && job.is_registered) return 'Deployed'
  return job.status
}

function getExecutionTarget(job: Job): string {
  return job.execution_target === 'domino_job' ? 'Domino Job' : 'Local'
}

interface JobCardViewProps {
  jobs: Job[]
  onDeleteRequest: (job: Job) => void
  selectedIds: Set<string>
  onToggleJob: (jobId: string) => void
}

export function JobCardView({ jobs, onDeleteRequest, selectedIds, onToggleJob }: JobCardViewProps) {
  const [openDropdownId, setOpenDropdownId] = useState<string | null>(null)

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
      {jobs.map((job) => (
        <div
          key={job.id}
          className={`bg-white shadow-sm hover:shadow-md transition-shadow relative ${selectedIds.has(job.id) ? 'ring-2 ring-domino-accent-purple' : ''}`}
        >
          <div className="absolute top-3 left-3 z-10">
            <input
              type="checkbox"
              checked={selectedIds.has(job.id)}
              onChange={() => onToggleJob(job.id)}
              className="h-4 w-4 rounded border-domino-border text-domino-accent-purple focus:ring-domino-accent-purple cursor-pointer"
              aria-label={`Select ${job.name}`}
            />
          </div>
          <div className="flex">
            {/* Thumbnail area */}
            <div className="w-[140px] min-h-[140px] bg-gradient-to-br from-domino-accent-purple/20 to-domino-accent-purple/5 flex items-center justify-center flex-shrink-0 self-stretch">
              <CubeIcon className="h-12 w-12 text-domino-accent-purple/60" />
            </div>

            {/* Info */}
            <div className="flex-1 min-w-0 p-4 flex flex-col">
              <div className="flex items-start justify-between gap-2">
                <div className="min-w-0">
                  <p className="text-xs text-domino-text-muted capitalize">{job.model_type}</p>
                  <p className="text-xs text-domino-text-secondary mt-0.5">
                    Execution: {getExecutionTarget(job)}
                  </p>
                  <Link
                    to={buildAppPath(`/jobs/${job.id}`)}
                    className="text-base font-medium text-domino-accent-purple hover:underline block truncate"
                  >
                    {job.name}
                  </Link>
                </div>
                <span className={`inline-flex items-center gap-1 text-sm whitespace-nowrap ${getStatusColor(job.status)}`}>
                  {getStatusIcon(job.status)}
                  <span className="capitalize">{getDisplayStatus(job)}</span>
                </span>
              </div>

              {job.leaderboard && job.leaderboard.length > 0 && (
                <p className="text-xs text-domino-text-secondary mt-2">
                  Best: {job.leaderboard[0].model} ({job.leaderboard[0].score_val.toFixed(4)})
                </p>
              )}

              {/* Footer actions */}
              <div className="flex items-center gap-4 mt-auto pt-3 border-t border-domino-border/50">
                <Link
                  to={buildAppPath(`/jobs/${job.id}`)}
                  className="inline-flex items-center gap-1 text-xs text-domino-accent-purple hover:underline"
                >
                  <DocumentTextIcon className="h-3.5 w-3.5" />
                  Model details
                </Link>
                <span className="text-xs text-domino-text-muted">
                  {format(new Date(job.created_at), 'MM/dd/yyyy h:mm a')}
                </span>
                <div className="ml-auto">
                  <ActionsDropdown
                    isOpen={openDropdownId === job.id}
                    onToggle={() => setOpenDropdownId(openDropdownId === job.id ? null : job.id)}
                    onClose={() => setOpenDropdownId(null)}
                    onDelete={() => {
                      setOpenDropdownId(null)
                      onDeleteRequest(job)
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

// Actions Dropdown Component
interface ActionsDropdownProps {
  isOpen: boolean
  onToggle: () => void
  onClose: () => void
  onDelete: () => void
}

function ActionsDropdown({ isOpen, onToggle, onClose, onDelete }: ActionsDropdownProps) {
  const dropdownRef = useRef<HTMLDivElement>(null)

  // Close dropdown when clicking outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        onClose()
      }
    }

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside)
      return () => document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [isOpen, onClose])

  return (
    <div className="relative" ref={dropdownRef}>
      <button
        onClick={onToggle}
        className="w-6 h-6 flex items-center justify-center text-domino-text-muted hover:text-domino-text-primary rounded transition-colors"
      >
        <svg className="w-4 h-4" viewBox="0 0 16 16" fill="currentColor">
          <circle cx="8" cy="3" r="1.5" />
          <circle cx="8" cy="8" r="1.5" />
          <circle cx="8" cy="13" r="1.5" />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-1 w-40 bg-white shadow-lg border border-domino-border py-1 z-[100]">
          <button
            onClick={onDelete}
            className="w-full px-4 py-2 text-left text-sm text-domino-accent-red hover:bg-domino-bg-tertiary transition-colors"
          >
            Delete
          </button>
        </div>
      )}
    </div>
  )
}
