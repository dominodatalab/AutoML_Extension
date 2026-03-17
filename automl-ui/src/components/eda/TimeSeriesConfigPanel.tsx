import { useState, useMemo } from 'react'
import { ExclamationTriangleIcon, CheckCircleIcon } from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import type { ColumnProfile } from '../../types/profiling'

interface TimeSeriesConfigPanelProps {
  columns: ColumnProfile[]
  totalRows: number
  onRunAnalysis: (timeColumn: string, targetColumn: string, idColumn: string, sampleSize: number, samplingStrategy: string, rollingWindow: string) => void
  loading: boolean
  timeColumn: string
  targetColumn: string
  idColumn: string
  onTimeColumnChange: (col: string) => void
  onTargetColumnChange: (col: string) => void
  onIdColumnChange: (col: string) => void
  rollingWindow: string
  onRollingWindowChange: (val: string) => void
  analysisComplete?: boolean
  error?: string | null
}

export function TimeSeriesConfigPanel({
  columns,
  totalRows,
  onRunAnalysis,
  loading,
  timeColumn,
  targetColumn,
  idColumn,
  onTimeColumnChange,
  onTargetColumnChange,
  onIdColumnChange,
  rollingWindow,
  onRollingWindowChange,
  analysisComplete,
  error,
}: TimeSeriesConfigPanelProps) {
  const [sampleSize, setSampleSize] = useState('100000')
  const [samplingStrategy, setSamplingStrategy] = useState('recent')

  const datetimeColumns = useMemo(() => {
    const dtCols = columns.filter(
      (c) => c.semantic_type === 'datetime' || c.dtype.includes('datetime')
    )
    const otherCols = columns.filter(
      (c) => c.semantic_type !== 'datetime' && !c.dtype.includes('datetime')
    )
    return [...dtCols, ...otherCols].map((c) => ({ value: c.name, label: c.name }))
  }, [columns])

  const numericColumns = useMemo(() => {
    const numCols = columns.filter(
      (c) => c.dtype.startsWith('int') || c.dtype.startsWith('float') || c.semantic_type === 'numeric'
    )
    const otherCols = columns.filter(
      (c) => !c.dtype.startsWith('int') && !c.dtype.startsWith('float') && c.semantic_type !== 'numeric'
    )
    return [...numCols, ...otherCols].map((c) => ({ value: c.name, label: c.name }))
  }, [columns])

  const idOptions = useMemo(() => {
    return [
      { value: '', label: '(None)' },
      ...columns.map((c) => ({ value: c.name, label: c.name })),
    ]
  }, [columns])

  const needsSampling = totalRows > Number(sampleSize || 100000)

  const handleRun = () => {
    if (!timeColumn || !targetColumn) return
    onRunAnalysis(timeColumn, targetColumn, idColumn, Number(sampleSize) || 100000, samplingStrategy, rollingWindow)
  }

  return (
    <div className="bg-domino-bg-tertiary border border-domino-border p-4 space-y-4">
      <div className="flex items-center gap-4 flex-wrap">
        <div className="min-w-[180px]">
          <label className="block text-xs text-domino-text-muted mb-1">Time Column</label>
          <Dropdown
            value={timeColumn}
            onChange={onTimeColumnChange}
            placeholder="Select datetime column..."
            options={datetimeColumns}
          />
        </div>
        <div className="min-w-[180px]">
          <label className="block text-xs text-domino-text-muted mb-1">Target Column</label>
          <Dropdown
            value={targetColumn}
            onChange={onTargetColumnChange}
            placeholder="Select numeric target..."
            options={numericColumns}
          />
        </div>
        <div className="min-w-[180px]">
          <label className="block text-xs text-domino-text-muted mb-1">ID Column (optional)</label>
          <Dropdown
            value={idColumn}
            onChange={onIdColumnChange}
            placeholder="(None)"
            options={idOptions}
          />
        </div>
        <div className="min-w-[100px]">
          <label className="block text-xs text-domino-text-muted mb-1">Rolling Window</label>
          <input
            type="number"
            min="2"
            value={rollingWindow}
            onChange={(e) => onRollingWindowChange(e.target.value)}
            placeholder="Auto"
            className="h-[32px] w-full px-2 text-sm border border-domino-border rounded-[2px]"
          />
        </div>
        <div>
          <label className="block text-xs text-domino-text-muted mb-1">&nbsp;</label>
          <div className="flex items-center gap-2">
            <button
              onClick={handleRun}
              disabled={!timeColumn || !targetColumn || loading}
              className="h-[32px] px-4 text-sm bg-domino-accent-purple text-white rounded-[2px] hover:bg-domino-accent-purple-hover disabled:opacity-50 whitespace-nowrap"
            >
              {loading ? 'Analyzing...' : 'Run Analysis'}
            </button>
            {!loading && analysisComplete && !error && (
              <span className="flex items-center gap-1 text-sm text-green-700">
                <CheckCircleIcon className="h-4 w-4" />
                Analysis complete
              </span>
            )}
            {!loading && error && (
              <span className="flex items-center gap-1 text-sm text-domino-accent-red">
                <ExclamationTriangleIcon className="h-4 w-4" />
                Analysis failed
              </span>
            )}
          </div>
        </div>
      </div>

      {needsSampling && (
        <div className="flex items-center gap-4 pt-2 border-t border-domino-border flex-wrap">
          <span className="text-xs text-domino-text-secondary font-medium">Sampling:</span>
          <div className="flex items-center border border-domino-border rounded-[2px] overflow-hidden">
            {(['recent', 'oldest', 'uniform', 'full'] as const).map((s) => (
              <button
                key={s}
                onClick={() => setSamplingStrategy(s)}
                className={`px-3 py-1 text-xs border-r last:border-r-0 ${
                  samplingStrategy === s
                    ? 'bg-domino-accent-purple text-white'
                    : 'bg-white text-domino-text-secondary hover:bg-domino-bg-tertiary'
                }`}
              >
                {s === 'recent' ? 'Most Recent' : s === 'oldest' ? 'Oldest' : s === 'uniform' ? 'Evenly Spaced' : 'Full Dataset'}
              </button>
            ))}
          </div>
          {samplingStrategy !== 'full' && (
            <div className="flex items-center gap-1">
              <label className="text-xs text-domino-text-secondary">Size:</label>
              <input
                type="number"
                value={sampleSize}
                onChange={(e) => setSampleSize(e.target.value)}
                className="h-[26px] w-[90px] px-2 text-xs border border-domino-border rounded-[2px]"
              />
            </div>
          )}
          {samplingStrategy === 'full' && totalRows > 500000 && (
            <span className="flex items-center gap-1 text-xs text-amber-700">
              <ExclamationTriangleIcon className="h-3.5 w-3.5" />
              Large dataset — analysis may take longer
            </span>
          )}
        </div>
      )}
    </div>
  )
}
