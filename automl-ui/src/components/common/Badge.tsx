import clsx from 'clsx'
import { JobStatus } from '../../types/job'
import { ReactNode } from 'react'

type BadgeVariant = 'default' | 'success' | 'warning' | 'error' | 'info' | 'muted'

interface BadgeProps {
  status?: JobStatus
  variant?: BadgeVariant
  children?: ReactNode
  className?: string
  isRegistered?: boolean
}

function Badge({ status, variant, children, className, isRegistered }: BadgeProps) {
  const statusVariants: Record<JobStatus, string> = {
    pending: 'bg-domino-accent-yellow/20 text-domino-accent-yellow',
    running: 'bg-domino-accent-purple/20 text-domino-accent-purple',
    completed: 'bg-domino-accent-green/20 text-domino-accent-green',
    failed: 'bg-domino-accent-red/20 text-domino-accent-red',
    cancelled: 'bg-domino-text-muted/20 text-domino-text-muted',
  }

  const variantStyles: Record<BadgeVariant, string> = {
    default: 'bg-domino-bg-tertiary text-domino-text-secondary',
    success: 'bg-domino-accent-green/20 text-domino-accent-green',
    warning: 'bg-domino-accent-yellow/20 text-domino-accent-yellow',
    error: 'bg-domino-accent-red/20 text-domino-accent-red',
    info: 'bg-domino-accent-purple/20 text-domino-accent-purple',
    muted: 'bg-domino-text-muted/20 text-domino-text-muted',
  }

  const labels: Record<JobStatus, string> = {
    pending: 'Pending',
    running: 'Running',
    completed: 'Completed',
    failed: 'Failed',
    cancelled: 'Cancelled',
  }

  // Determine styles based on props
  const badgeStyle = status
    ? statusVariants[status]
    : variant
      ? variantStyles[variant]
      : variantStyles.default

  // Determine content - show "Deployed" if completed and registered
  const getLabel = () => {
    if (status === 'completed' && isRegistered) return 'Deployed'
    return status ? labels[status] : null
  }
  const content = children ?? getLabel()

  return (
    <span
      className={clsx(
        'inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium',
        badgeStyle,
        className
      )}
    >
      {status === 'running' && (
        <span className="mr-1.5 h-2 w-2 rounded-full bg-current animate-pulse" />
      )}
      {content}
    </span>
  )
}

export default Badge
