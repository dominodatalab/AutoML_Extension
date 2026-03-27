import { useMemo } from 'react'
import { ExclamationTriangleIcon, CheckCircleIcon } from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import type { ColumnProfile } from '../../types/profiling'

interface TimeSeriesConfigPanelProps {
  columns: ColumnProfile[]
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

  const sameColumnError = timeColumn && targetColumn && timeColumn === targetColumn

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
        {!loading && analysisComplete && !error && (
          <div className="flex items-center self-end pb-1">
            <span className="flex items-center gap-1 text-sm text-green-700">
              <CheckCircleIcon className="h-4 w-4" />
              Analysis complete
            </span>
          </div>
        )}
        {!loading && error && (
          <div className="flex items-center self-end pb-1">
            <span className="flex items-center gap-1 text-sm text-domino-accent-red">
              <ExclamationTriangleIcon className="h-4 w-4" />
              Analysis failed
            </span>
          </div>
        )}
      </div>

      {sameColumnError && (
        <p className="text-xs text-domino-accent-red">
          Time column and target column must be different.
        </p>
      )}

    </div>
  )
}
