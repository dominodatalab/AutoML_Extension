import { useState, useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import { format } from 'date-fns'
import { Job } from '../../types/job'
import { formatDuration, getStatusColor, getStatusIcon } from '../../utils/formatters'
import { buildAppPath } from '../../utils/appPath'

function getDisplayStatus(job: Job): string {
  if (job.status === 'completed' && job.is_registered) return 'Deployed'
  return job.status
}

function getDuration(job: Job): string {
  if (!['completed', 'failed', 'cancelled'].includes(job.status)) return '\u2014'
  return formatDuration(job.started_at, job.completed_at)
}

function getBestModel(job: Job): string {
  if (!job.leaderboard || job.leaderboard.length === 0) return '\u2014'
  return job.leaderboard[0].model
}

function getBestScore(job: Job): string {
  if (!job.leaderboard || job.leaderboard.length === 0) return '\u2014'
  return job.leaderboard[0].score_val.toFixed(4)
}

interface JobTableViewProps {
  jobs: Job[]
  onDeleteRequest: (job: Job) => void
  selectedIds: Set<string>
  isAllSelected: boolean
  isIndeterminate: boolean
  onToggleJob: (jobId: string) => void
  onToggleAll: () => void
}

export function JobTableView({ jobs, onDeleteRequest, selectedIds, isAllSelected, isIndeterminate, onToggleJob, onToggleAll }: JobTableViewProps) {
  const [openDropdownId, setOpenDropdownId] = useState<string | null>(null)
  const selectAllRef = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (selectAllRef.current) {
      selectAllRef.current.indeterminate = isIndeterminate
    }
  }, [isIndeterminate])

  return (
    <div className="bg-white border border-domino-border">
      <table className="w-full">
        <thead>
          <tr className="border-b border-domino-border">
            <th className="px-4 py-3 w-10">
              <input
                ref={selectAllRef}
                type="checkbox"
                checked={isAllSelected}
                onChange={onToggleAll}
                className="h-4 w-4 rounded border-domino-border text-domino-accent-purple focus:ring-domino-accent-purple cursor-pointer"
                aria-label="Select all jobs"
              />
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              <span className="inline-flex items-center gap-1 cursor-pointer hover:text-domino-text-primary">
                Name
                <svg className="w-3 h-3" viewBox="0 0 12 12" fill="currentColor">
                  <path d="M6 2l3 4H3l3-4zM6 10l-3-4h6l-3 4z" />
                </svg>
              </span>
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              Type
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              <span className="inline-flex items-center gap-1 cursor-pointer hover:text-domino-text-primary">
                Status
                <svg className="w-3 h-3" viewBox="0 0 12 12" fill="currentColor">
                  <path d="M6 2l3 4H3l3-4zM6 10l-3-4h6l-3 4z" />
                </svg>
              </span>
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              Best model
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              Score
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              <span className="inline-flex items-center gap-1 cursor-pointer hover:text-domino-text-primary">
                Created
                <svg className="w-3 h-3" viewBox="0 0 12 12" fill="currentColor">
                  <path d="M6 2l3 4H3l3-4zM6 10l-3-4h6l-3 4z" />
                </svg>
              </span>
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide">
              Duration
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-domino-text-secondary uppercase tracking-wide w-16">
            </th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((job) => (
            <tr key={job.id} className={`border-b border-domino-border hover:bg-domino-bg-tertiary transition-colors ${selectedIds.has(job.id) ? 'bg-domino-accent-purple/5' : ''}`}>
              <td className="px-4 py-3 w-10">
                <input
                  type="checkbox"
                  checked={selectedIds.has(job.id)}
                  onChange={() => onToggleJob(job.id)}
                  className="h-4 w-4 rounded border-domino-border text-domino-accent-purple focus:ring-domino-accent-purple cursor-pointer"
                  aria-label={`Select ${job.name}`}
                />
              </td>
              <td className="px-4 py-3">
                <Link
                  to={buildAppPath(`/jobs/${job.id}`)}
                  className="text-sm font-normal text-domino-accent-purple hover:underline"
                >
                  {job.name}
                </Link>
              </td>
              <td className="px-4 py-3 text-sm text-domino-text-primary capitalize">
                {job.model_type}
              </td>
              <td className="px-4 py-3">
                <span className={`inline-flex items-center gap-1.5 text-sm ${getStatusColor(job.status)}`}>
                  {getStatusIcon(job.status)}
                  <span className="capitalize">{getDisplayStatus(job)}</span>
                </span>
              </td>
              <td className="px-4 py-3 text-sm text-domino-text-primary ">
                {getBestModel(job)}
              </td>
              <td className="px-4 py-3 text-sm text-domino-text-primary ">
                {getBestScore(job)}
              </td>
              <td className="px-4 py-3 text-sm text-domino-text-secondary">
                {format(new Date(job.created_at), 'MM/dd/yyyy h:mm a')}
              </td>
              <td className="px-4 py-3 text-sm text-domino-text-secondary">
                {getDuration(job)}
              </td>
              <td className="px-4 py-3">
                <ActionsDropdown
                  isOpen={openDropdownId === job.id}
                  onToggle={() => setOpenDropdownId(openDropdownId === job.id ? null : job.id)}
                  onClose={() => setOpenDropdownId(null)}
                  onDelete={() => {
                    setOpenDropdownId(null)
                    onDeleteRequest(job)
                  }}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
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
