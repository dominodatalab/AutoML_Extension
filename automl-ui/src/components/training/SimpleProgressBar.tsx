interface SimpleProgressBarProps {
  progress: number
  status: string
}

export function SimpleProgressBar({ progress, status }: SimpleProgressBarProps) {
  const getStatusColor = (value: string) => {
    switch (value) {
      case 'completed':
      case 'running':
        return 'bg-domino-accent-purple'
      case 'failed':
        return 'bg-domino-accent-red'
      case 'cancelled':
        return 'bg-domino-text-muted'
      default:
        return 'bg-domino-accent-yellow'
    }
  }

  const statusLabel = status === 'failed' ? 'Failed' : status === 'cancelled' ? 'Cancelled' : null
  const labelColor = status === 'failed' ? 'text-domino-accent-red' : status === 'cancelled' ? 'text-domino-text-muted' : ''

  return (
    <div>
      <div className="flex items-center justify-between text-sm mb-1">
        {statusLabel ? (
          <span className={`font-medium ${labelColor}`}>{statusLabel}</span>
        ) : (
          <span />
        )}
        <span className="font-medium">{progress}%</span>
      </div>
      <div className="h-2 bg-domino-border overflow-hidden">
        <div
          className={`h-full transition-all duration-300 ${getStatusColor(status)}`}
          style={{ width: `${progress}%` }}
        />
      </div>
    </div>
  )
}
