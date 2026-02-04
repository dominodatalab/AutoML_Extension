import { useMemo, useState } from 'react'
import Dropdown from '../common/Dropdown'
import type { ColumnProfile } from '../../types/profiling'

interface MissingValuesChartProps {
  columns: ColumnProfile[]
}

export function MissingValuesChart({ columns }: MissingValuesChartProps) {
  const [sortBy, setSortBy] = useState<'name' | 'missing'>('missing')
  const [showOnlyMissing, setShowOnlyMissing] = useState(true)

  const sortedColumns = useMemo(() => {
    let filtered = showOnlyMissing
      ? columns.filter((c) => c.missing_count > 0)
      : columns

    return [...filtered].sort((a, b) => {
      if (sortBy === 'missing') {
        return b.missing_percentage - a.missing_percentage
      }
      return a.name.localeCompare(b.name)
    })
  }, [columns, sortBy, showOnlyMissing])

  const summary = useMemo(() => {
    const withMissing = columns.filter((c) => c.missing_count > 0)
    const totalMissing = columns.reduce((acc, c) => acc + c.missing_count, 0)

    return {
      columnsWithMissing: withMissing.length,
      columnsComplete: columns.length - withMissing.length,
      totalMissingCells: totalMissing,
      avgMissingPerColumn: withMissing.length > 0
        ? totalMissing / withMissing.length
        : 0,
    }
  }, [columns])

  const getBarColor = (percentage: number) => {
    if (percentage > 50) return 'bg-domino-accent-red'
    if (percentage > 20) return 'bg-yellow-500'
    if (percentage > 5) return 'bg-orange-400'
    return 'bg-domino-accent-purple'
  }

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-domino-bg-tertiary border border-domino-border p-4 rounded">
          <p className="text-xs text-domino-text-muted uppercase tracking-wide">
            Columns with Missing
          </p>
          <p className="text-2xl font-semibold text-domino-text-primary mt-1">
            {summary.columnsWithMissing}
            <span className="text-sm font-normal text-domino-text-muted ml-1">
              / {columns.length}
            </span>
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4 rounded">
          <p className="text-xs text-domino-text-muted uppercase tracking-wide">
            Complete Columns
          </p>
          <p className="text-2xl font-semibold text-domino-accent-green mt-1">
            {summary.columnsComplete}
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4 rounded">
          <p className="text-xs text-domino-text-muted uppercase tracking-wide">
            Total Missing Cells
          </p>
          <p className="text-2xl font-semibold text-domino-text-primary mt-1">
            {summary.totalMissingCells.toLocaleString()}
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4 rounded">
          <p className="text-xs text-domino-text-muted uppercase tracking-wide">
            Avg Missing per Column
          </p>
          <p className="text-2xl font-semibold text-domino-text-primary mt-1">
            {summary.avgMissingPerColumn.toLocaleString(undefined, { maximumFractionDigits: 0 })}
          </p>
        </div>
      </div>

      {/* Controls */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <label className="flex items-center gap-2 text-sm">
            <input
              type="checkbox"
              checked={showOnlyMissing}
              onChange={(e) => setShowOnlyMissing(e.target.checked)}
              className="rounded border-domino-border text-domino-accent-purple"
            />
            <span className="text-domino-text-secondary">Show only columns with missing values</span>
          </label>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-sm text-domino-text-muted">Sort by:</span>
          <Dropdown
            value={sortBy}
            onChange={(val) => setSortBy(val as 'name' | 'missing')}
            className="w-[180px]"
            options={[
              { value: 'missing', label: 'Missing % (descending)' },
              { value: 'name', label: 'Column Name' },
            ]}
          />
        </div>
      </div>

      {/* Missing Values Chart */}
      <div className="border border-domino-border rounded bg-white">
        <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border">
          <h4 className="text-sm font-medium text-domino-text-primary">Missing Values by Column</h4>
        </div>

        {sortedColumns.length === 0 ? (
          <div className="p-8 text-center text-domino-text-muted">
            <p className="text-lg mb-2">No missing values detected</p>
            <p className="text-sm">All columns are complete</p>
          </div>
        ) : (
          <div className="p-4 space-y-3 max-h-[400px] overflow-y-auto">
            {sortedColumns.map((col) => (
              <div key={col.name} className="flex items-center gap-4">
                <span
                  className="text-sm text-domino-text-primary w-48 truncate text-right"
                  title={col.name}
                >
                  {col.name}
                </span>
                <div className="flex-1 flex items-center gap-2">
                  <div className="flex-1 h-6 bg-domino-bg-tertiary rounded overflow-hidden">
                    <div
                      className={`h-full ${getBarColor(col.missing_percentage)} transition-all duration-300 flex items-center justify-end pr-2`}
                      style={{ width: `${Math.max(col.missing_percentage, 1)}%` }}
                    >
                      {col.missing_percentage > 5 && (
                        <span className="text-xs text-white font-medium">
                          {col.missing_percentage.toFixed(1)}%
                        </span>
                      )}
                    </div>
                  </div>
                  <span className="text-xs text-domino-text-muted w-20 text-right">
                    {col.missing_count.toLocaleString()} missing
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Matrix View (for pattern detection) */}
      {summary.columnsWithMissing > 1 && summary.columnsWithMissing <= 15 && (
        <div className="border border-domino-border rounded bg-white">
          <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border">
            <h4 className="text-sm font-medium text-domino-text-primary">Missing Value Pattern</h4>
            <p className="text-xs text-domino-text-muted mt-1">
              Visual representation of missing values across columns
            </p>
          </div>
          <div className="p-4 overflow-x-auto">
            <div className="flex flex-wrap gap-2">
              {columns
                .filter((c) => c.missing_count > 0)
                .slice(0, 15)
                .map((col) => (
                  <div key={col.name} className="flex flex-col items-center">
                    <div
                      className="w-8 h-24 rounded overflow-hidden flex flex-col-reverse bg-domino-bg-tertiary border border-domino-border"
                      title={`${col.name}: ${col.missing_percentage.toFixed(1)}% missing`}
                    >
                      <div
                        className={`w-full ${getBarColor(col.missing_percentage)}`}
                        style={{ height: `${col.missing_percentage}%` }}
                      />
                    </div>
                    <span
                      className="text-xs text-domino-text-muted mt-1 w-8 truncate text-center"
                      title={col.name}
                    >
                      {col.name.slice(0, 4)}
                    </span>
                  </div>
                ))}
            </div>
          </div>
        </div>
      )}

      {/* Legend */}
      <div className="flex items-center justify-center gap-6 text-sm text-domino-text-muted">
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 rounded bg-domino-accent-purple" />
          <span>&lt; 5% missing</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 rounded bg-orange-400" />
          <span>5-20% missing</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 rounded bg-yellow-500" />
          <span>20-50% missing</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-4 h-4 rounded bg-domino-accent-red" />
          <span>&gt; 50% missing</span>
        </div>
      </div>
    </div>
  )
}
