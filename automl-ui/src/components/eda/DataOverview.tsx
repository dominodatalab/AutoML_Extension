import { useMemo } from 'react'
import {
  TableCellsIcon,
  DocumentDuplicateIcon,
  ExclamationCircleIcon,
  CheckCircleIcon,
  HashtagIcon,
  CalendarIcon,
  Bars3BottomLeftIcon,
} from '@heroicons/react/24/outline'
import type { DataProfile } from '../../types/profiling'

interface DataOverviewProps {
  profile: DataProfile
}

export function DataOverview({ profile }: DataOverviewProps) {
  const { summary, columns } = profile

  // Compute type breakdown
  const typeBreakdown = useMemo(() => {
    const types: Record<string, number> = {}
    columns.forEach((col) => {
      const type = col.semantic_type || 'unknown'
      types[type] = (types[type] || 0) + 1
    })
    return Object.entries(types).sort((a, b) => b[1] - a[1])
  }, [columns])

  // Compute missing data summary
  const missingStats = useMemo(() => {
    const withMissing = columns.filter((c) => c.missing_count > 0)
    const totalMissing = columns.reduce((acc, c) => acc + c.missing_count, 0)
    const totalCells = summary.total_rows * summary.total_columns
    return {
      columnsWithMissing: withMissing.length,
      totalMissingCells: totalMissing,
      missingPercentage: totalCells > 0 ? (totalMissing / totalCells) * 100 : 0,
    }
  }, [columns, summary])

  // Compute quality score
  const qualityScore = useMemo(() => {
    let score = 100

    // Deduct for missing data
    score -= Math.min(missingStats.missingPercentage * 2, 30)

    // Deduct for duplicates
    score -= Math.min(summary.duplicate_percentage * 0.5, 15)

    // Deduct for columns with issues
    const issueCount = columns.filter((c) => (c.issues?.length ?? 0) > 0).length
    score -= Math.min((issueCount / columns.length) * 20, 20)

    return Math.max(Math.round(score), 0)
  }, [missingStats, summary, columns])

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-domino-accent-green'
    if (score >= 60) return 'text-yellow-500'
    return 'text-domino-accent-red'
  }

  const getScoreLabel = (score: number) => {
    if (score >= 80) return 'Good'
    if (score >= 60) return 'Fair'
    return 'Needs Attention'
  }

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'numeric':
      case 'monetary':
      case 'percentage':
        return HashtagIcon
      case 'datetime':
        return CalendarIcon
      case 'category':
      case 'binary':
        return Bars3BottomLeftIcon
      default:
        return TableCellsIcon
    }
  }

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'numeric':
      case 'monetary':
        return 'bg-blue-100 text-blue-700'
      case 'category':
      case 'binary':
        return 'bg-purple-100 text-purple-700'
      case 'datetime':
        return 'bg-green-100 text-green-700'
      case 'text':
        return 'bg-orange-100 text-orange-700'
      case 'identifier':
        return 'bg-gray-100 text-gray-700'
      default:
        return 'bg-gray-100 text-gray-600'
    }
  }

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-domino-bg-tertiary border border-domino-border p-4">
          <div className="flex items-center gap-2 text-domino-text-secondary mb-2">
            <TableCellsIcon className="h-4 w-4" />
            <span className="text-xs uppercase tracking-wide">Rows</span>
          </div>
          <p className="text-2xl font-semibold text-domino-text-primary">
            {summary.total_rows.toLocaleString()}
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4">
          <div className="flex items-center gap-2 text-domino-text-secondary mb-2">
            <Bars3BottomLeftIcon className="h-4 w-4" />
            <span className="text-xs uppercase tracking-wide">Columns</span>
          </div>
          <p className="text-2xl font-semibold text-domino-text-primary">
            {summary.total_columns}
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4">
          <div className="flex items-center gap-2 text-domino-text-secondary mb-2">
            <DocumentDuplicateIcon className="h-4 w-4" />
            <span className="text-xs uppercase tracking-wide">Duplicates</span>
          </div>
          <p className="text-2xl font-semibold text-domino-text-primary">
            {summary.duplicate_rows.toLocaleString()}
            <span className="text-sm font-normal text-domino-text-muted ml-1">
              ({summary.duplicate_percentage.toFixed(1)}%)
            </span>
          </p>
        </div>

        <div className="bg-domino-bg-tertiary border border-domino-border p-4">
          <div className="flex items-center gap-2 text-domino-text-secondary mb-2">
            {qualityScore >= 80 ? (
              <CheckCircleIcon className="h-4 w-4 text-domino-accent-green" />
            ) : (
              <ExclamationCircleIcon className="h-4 w-4 text-yellow-500" />
            )}
            <span className="text-xs uppercase tracking-wide">Quality Score</span>
          </div>
          <p className={`text-2xl font-semibold ${getScoreColor(qualityScore)}`}>
            {qualityScore}
            <span className="text-sm font-normal text-domino-text-muted ml-1">
              / 100
            </span>
          </p>
          <p className={`text-xs ${getScoreColor(qualityScore)}`}>
            {getScoreLabel(qualityScore)}
          </p>
        </div>
      </div>

      {/* Type Breakdown and Missing Data */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Column Types */}
        <div className="border border-domino-border bg-white">
          <div className="px-4 py-3 border-b border-domino-border bg-domino-bg-tertiary">
            <h4 className="text-sm font-medium text-domino-text-primary">Column Types</h4>
          </div>
          <div className="p-4 space-y-3">
            {typeBreakdown.map(([type, count]) => {
              const Icon = getTypeIcon(type)
              const percentage = (count / summary.total_columns) * 100
              return (
                <div key={type} className="flex items-center gap-3">
                  <span className={`inline-flex items-center gap-1 px-2 py-1 rounded text-xs font-medium ${getTypeColor(type)}`}>
                    <Icon className="h-3 w-3" />
                    {type}
                  </span>
                  <div className="flex-1 h-2 bg-domino-bg-tertiary rounded overflow-hidden">
                    <div
                      className="h-full bg-domino-accent-purple rounded"
                      style={{ width: `${percentage}%` }}
                    />
                  </div>
                  <span className="text-sm text-domino-text-secondary w-12 text-right">
                    {count}
                  </span>
                </div>
              )
            })}
          </div>
        </div>

        {/* Missing Data Summary */}
        <div className="border border-domino-border bg-white">
          <div className="px-4 py-3 border-b border-domino-border bg-domino-bg-tertiary">
            <h4 className="text-sm font-medium text-domino-text-primary">Missing Data</h4>
          </div>
          <div className="p-4">
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Columns with missing values</span>
                <span className="text-sm font-medium text-domino-text-primary">
                  {missingStats.columnsWithMissing} / {summary.total_columns}
                </span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Total missing cells</span>
                <span className="text-sm font-medium text-domino-text-primary">
                  {missingStats.totalMissingCells.toLocaleString()}
                </span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Overall missing rate</span>
                <span className={`text-sm font-medium ${
                  missingStats.missingPercentage > 10 ? 'text-domino-accent-red' : 'text-domino-text-primary'
                }`}>
                  {missingStats.missingPercentage.toFixed(2)}%
                </span>
              </div>

              {/* Missing by column - top 5 */}
              {missingStats.columnsWithMissing > 0 && (
                <div className="pt-4 border-t border-domino-border">
                  <p className="text-xs text-domino-text-muted mb-3 uppercase tracking-wide">
                    Highest Missing Rates
                  </p>
                  <div className="space-y-2">
                    {columns
                      .filter((c) => c.missing_percentage > 0)
                      .sort((a, b) => b.missing_percentage - a.missing_percentage)
                      .slice(0, 5)
                      .map((col) => (
                        <div key={col.name} className="flex items-center gap-2">
                          <span className="text-sm text-domino-text-primary truncate flex-1" title={col.name}>
                            {col.name}
                          </span>
                          <div className="w-24 h-2 bg-domino-bg-tertiary rounded overflow-hidden">
                            <div
                              className={`h-full rounded ${
                                col.missing_percentage > 50 ? 'bg-domino-accent-red' :
                                col.missing_percentage > 20 ? 'bg-yellow-500' : 'bg-domino-accent-purple'
                              }`}
                              style={{ width: `${Math.min(col.missing_percentage, 100)}%` }}
                            />
                          </div>
                          <span className="text-xs text-domino-text-muted w-12 text-right">
                            {col.missing_percentage.toFixed(1)}%
                          </span>
                        </div>
                      ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Quick Stats Grid */}
      <div className="border border-domino-border bg-white">
        <div className="px-4 py-3 border-b border-domino-border bg-domino-bg-tertiary">
          <h4 className="text-sm font-medium text-domino-text-primary">Numeric Column Statistics</h4>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-domino-border">
                <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase">Column</th>
                <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary uppercase">Min</th>
                <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary uppercase">Max</th>
                <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary uppercase">Mean</th>
                <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary uppercase">Median</th>
                <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary uppercase">Std Dev</th>
              </tr>
            </thead>
            <tbody>
              {columns
                .filter((c) => c.statistics?.min !== undefined)
                .slice(0, 10)
                .map((col) => (
                  <tr key={col.name} className="border-b border-domino-border hover:bg-domino-bg-tertiary">
                    <td className="px-4 py-2 text-domino-text-primary font-medium truncate max-w-[200px]" title={col.name}>
                      {col.name}
                    </td>
                    <td className="px-4 py-2 text-right text-domino-text-secondary">
                      {col.statistics?.min?.toLocaleString(undefined, { maximumFractionDigits: 4 }) ?? '-'}
                    </td>
                    <td className="px-4 py-2 text-right text-domino-text-secondary">
                      {col.statistics?.max?.toLocaleString(undefined, { maximumFractionDigits: 4 }) ?? '-'}
                    </td>
                    <td className="px-4 py-2 text-right text-domino-text-secondary">
                      {col.statistics?.mean?.toLocaleString(undefined, { maximumFractionDigits: 4 }) ?? '-'}
                    </td>
                    <td className="px-4 py-2 text-right text-domino-text-secondary">
                      {col.statistics?.median?.toLocaleString(undefined, { maximumFractionDigits: 4 }) ?? '-'}
                    </td>
                    <td className="px-4 py-2 text-right text-domino-text-secondary">
                      {col.statistics?.std?.toLocaleString(undefined, { maximumFractionDigits: 4 }) ?? '-'}
                    </td>
                  </tr>
                ))}
            </tbody>
          </table>
          {columns.filter((c) => c.statistics?.min !== undefined).length > 10 && (
            <p className="px-4 py-2 text-xs text-domino-text-muted">
              Showing 10 of {columns.filter((c) => c.statistics?.min !== undefined).length} numeric columns
            </p>
          )}
        </div>
      </div>
    </div>
  )
}
