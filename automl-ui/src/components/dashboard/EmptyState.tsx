import { Link } from 'react-router-dom'
import { BoltIcon } from '@heroicons/react/24/outline'
import { buildAppPath } from '../../utils/appPath'

interface EmptyStateProps {
  hasJobs: boolean
}

export function EmptyState({ hasJobs }: EmptyStateProps) {
  return (
    <div className="bg-white border border-domino-border">
      {/* Table header placeholder */}
      <div className="flex items-center gap-6 px-4 py-3 border-b border-domino-border">
        <span className="text-xs font-normal text-domino-text-secondary uppercase tracking-wide">Name</span>
        <span className="text-xs font-normal text-domino-text-secondary uppercase tracking-wide">Type</span>
        <span className="text-xs font-normal text-domino-text-secondary uppercase tracking-wide">Status</span>
        <span className="text-xs font-normal text-domino-text-secondary uppercase tracking-wide">Best model</span>
        <span className="text-xs font-normal text-domino-text-secondary uppercase tracking-wide">Created</span>
      </div>

      <div className="flex flex-col items-center py-16">
        <div className="w-20 h-20 bg-domino-bg-tertiary flex items-center justify-center mb-6">
          <BoltIcon className="h-10 w-10 text-domino-text-muted" />
        </div>
        <p className="text-domino-text-secondary text-sm mb-6">
          {hasJobs
            ? 'No jobs match your current filters.'
            : 'Train models to manage and track them through a unified interface.'}
        </p>
        <Link to={buildAppPath('/jobs/new')}>
          <button className="h-[32px] px-[15px] bg-domino-accent-purple text-white text-sm font-normal hover:bg-domino-accent-purple-hover transition-all duration-200 inline-flex items-center">
            New training job
          </button>
        </Link>
      </div>
    </div>
  )
}
