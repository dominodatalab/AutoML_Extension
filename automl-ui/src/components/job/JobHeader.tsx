import { useRef, useEffect } from 'react'
import { StopIcon } from '@heroicons/react/24/outline'
import type { Job } from '../../types/job'

interface JobHeaderProps {
  job: Job | undefined
  currentStatus: string
  cancelIsPending: boolean
  showActionsDropdown: boolean
  onCancel: () => void
  onToggleActionsDropdown: () => void
  onCloseActionsDropdown: () => void
  onOpenDeleteConfirm: () => void
}

export function JobHeader({
  job,
  currentStatus,
  cancelIsPending,
  showActionsDropdown,
  onCancel,
  onToggleActionsDropdown,
  onCloseActionsDropdown,
  onOpenDeleteConfirm,
}: JobHeaderProps) {
  const actionsDropdownRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (actionsDropdownRef.current && !actionsDropdownRef.current.contains(event.target as Node)) {
        onCloseActionsDropdown()
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [onCloseActionsDropdown])

  return (
    <div className="flex items-center justify-between flex-wrap mb-5">
      <div>
        <h1 className="text-2xl font-normal text-domino-text-primary leading-tight">
          {job ? `Run: ${job.name}` : 'Training in Progress'}
        </h1>
      </div>
      <div className="flex items-center gap-3">
        {['pending', 'running'].includes(currentStatus) && (
          <button
            onClick={onCancel}
            disabled={cancelIsPending}
            className="h-[32px] px-[15px] text-sm font-normal border border-transparent rounded-[2px] text-white bg-domino-accent-red hover:bg-domino-accent-red/90 transition-all duration-200 inline-flex items-center"
          >
            <StopIcon className="h-4 w-4 inline mr-1" />
            Cancel
          </button>
        )}
<div className="relative" ref={actionsDropdownRef}>
          <button
            onClick={onToggleActionsDropdown}
            className="h-[32px] w-[32px] flex items-center justify-center border border-domino-border rounded-[2px] text-domino-text-secondary hover:border-domino-accent-purple hover:text-domino-accent-purple transition-all duration-200"
          >
            <svg className="w-4 h-4" viewBox="0 0 16 16" fill="currentColor">
              <circle cx="8" cy="3" r="1.5" />
              <circle cx="8" cy="8" r="1.5" />
              <circle cx="8" cy="13" r="1.5" />
            </svg>
          </button>
          {showActionsDropdown && (
            <div className="absolute right-0 mt-1 w-40 bg-white shadow-lg border border-domino-border py-1 z-50">
              <button
                onClick={onOpenDeleteConfirm}
                className="w-full px-4 py-2 text-left text-sm text-domino-accent-red hover:bg-domino-bg-tertiary transition-colors"
              >
                Delete
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
