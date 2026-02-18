export type JobStatus = 'pending' | 'running' | 'completed' | 'failed' | 'cancelled'

export function formatTimestamp(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

export function formatTimestampFull(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

export function formatTick(v: number): string {
  return Math.abs(v) >= 1000 ? `${(v / 1000).toFixed(1)}k` : v.toFixed(1)
}

export function formatTickPrecise(v: number): string {
  return Math.abs(v) >= 1000 ? `${(v / 1000).toFixed(1)}k` : v.toFixed(2)
}

export function formatDuration(startDate: string | null | undefined, endDate: string | null | undefined): string {
  if (!startDate || !endDate) return '—'
  const start = new Date(startDate).getTime()
  const end = new Date(endDate).getTime()
  const seconds = Math.floor((end - start) / 1000)
  if (seconds < 0 || seconds > 86400 * 365) return '—'
  if (seconds < 60) return `${seconds}s`
  const minutes = Math.floor(seconds / 60)
  const secs = seconds % 60
  if (minutes < 60) return `${minutes}m ${secs}s`
  const hours = Math.floor(minutes / 60)
  return `${hours}h ${minutes % 60}m`
}

export function formatFileSize(bytes: number): string {
  if (bytes === 0) return '0 B'
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
}

export function formatNumber(num: number, decimals = 2): string {
  if (Number.isInteger(num)) return num.toString()
  return num.toFixed(decimals)
}

export function formatCompactNumber(num: number | null | undefined): string {
  if (num === null || num === undefined || Number.isNaN(num)) return '-'
  const abs = Math.abs(num)
  if (abs >= 1e9) return (num / 1e9).toFixed(2) + 'B'
  if (abs >= 1e6) return (num / 1e6).toFixed(2) + 'M'
  if (abs >= 1e3) return num.toLocaleString(undefined, { maximumFractionDigits: 2 })
  if (abs < 0.001 && abs > 0) return num.toExponential(2)
  if (Number.isInteger(num)) return num.toLocaleString()
  return num.toFixed(4)
}

export function getStatusColor(status: string): string {
  switch (status?.toLowerCase()) {
    case 'completed':
      return 'text-domino-accent-green'
    case 'running':
      return 'text-domino-accent-green'
    case 'failed':
      return 'text-domino-accent-red'
    case 'cancelled':
      return 'text-domino-text-muted'
    case 'pending':
      return 'text-domino-text-muted'
    default:
      return 'text-domino-text-muted'
  }
}

export function getStatusIcon(status: JobStatus) {
  if (status === 'running') return (
    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path strokeLinecap="round" strokeLinejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
    </svg>
  )
  if (status === 'completed') return (
    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path strokeLinecap="round" strokeLinejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
  )
  if (status === 'failed') return (
    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
    </svg>
  )
  if (status === 'cancelled') return (
    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
    </svg>
  )
  return (
    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
      <circle cx="12" cy="12" r="10" />
      <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v6l4 2" />
    </svg>
  )
}
