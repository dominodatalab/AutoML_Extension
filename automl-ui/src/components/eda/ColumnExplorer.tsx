import { useState, useMemo } from 'react'
import {
  MagnifyingGlassIcon,
  ExclamationTriangleIcon,
} from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import type { ColumnProfile } from '../../types/profiling'

interface ColumnExplorerProps {
  columns: ColumnProfile[]
  filePath: string
}

export function ColumnExplorer({ columns, filePath: _filePath }: ColumnExplorerProps) {
  void _filePath // Used for future API calls
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedColumn, setSelectedColumn] = useState<string | null>(
    columns[0]?.name || null
  )
  const [typeFilter, setTypeFilter] = useState<string>('all')

  // Get unique types for filter
  const uniqueTypes = useMemo(() => {
    const types = new Set(columns.map((c) => c.semantic_type))
    return Array.from(types).sort()
  }, [columns])

  // Filter columns
  const filteredColumns = useMemo(() => {
    return columns.filter((col) => {
      const matchesSearch = col.name.toLowerCase().includes(searchTerm.toLowerCase())
      const matchesType = typeFilter === 'all' || col.semantic_type === typeFilter
      return matchesSearch && matchesType
    })
  }, [columns, searchTerm, typeFilter])

  const selectedColumnData = columns.find((c) => c.name === selectedColumn)

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'numeric':
      case 'monetary':
        return 'bg-blue-100 text-blue-700 border-blue-200'
      case 'category':
      case 'binary':
        return 'bg-purple-100 text-purple-700 border-purple-200'
      case 'datetime':
        return 'bg-green-100 text-green-700 border-green-200'
      case 'text':
        return 'bg-orange-100 text-orange-700 border-orange-200'
      case 'identifier':
        return 'bg-gray-100 text-gray-700 border-gray-200'
      default:
        return 'bg-gray-100 text-gray-600 border-gray-200'
    }
  }

  return (
    <div className="flex gap-6 h-[450px]">
      {/* Column List */}
      <div className="w-80 flex flex-col border border-domino-border bg-white">
        {/* Search and Filter */}
        <div className="p-3 border-b border-domino-border space-y-2">
          <div className="relative">
            <MagnifyingGlassIcon className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-domino-text-muted" />
            <input
              type="text"
              placeholder="Search columns..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-3 py-2 text-sm border border-domino-border rounded focus:outline-none focus:border-domino-accent-purple"
            />
          </div>
          <Dropdown
            value={typeFilter}
            onChange={setTypeFilter}
            options={[
              { value: 'all', label: 'All Types' },
              ...uniqueTypes.map((type) => ({ value: type, label: type }))
            ]}
          />
        </div>

        {/* Column List */}
        <div className="flex-1 overflow-y-auto">
          {filteredColumns.map((col) => (
            <button
              key={col.name}
              onClick={() => setSelectedColumn(col.name)}
              className={`w-full px-3 py-3 text-left border-b border-domino-border hover:bg-domino-bg-tertiary transition-colors ${
                selectedColumn === col.name ? 'bg-domino-accent-purple/10 border-l-2 border-l-domino-accent-purple' : ''
              }`}
            >
              <div className="flex items-center justify-between">
                <span className="text-sm font-medium text-domino-text-primary truncate flex-1" title={col.name}>
                  {col.name}
                </span>
                {(col.issues?.length ?? 0) > 0 && (
                  <ExclamationTriangleIcon className="h-4 w-4 text-yellow-500 flex-shrink-0 ml-2" />
                )}
              </div>
              <div className="flex items-center gap-2 mt-1">
                <span className={`text-xs px-1.5 py-0.5 rounded border ${getTypeColor(col.semantic_type)}`}>
                  {col.semantic_type}
                </span>
                {col.missing_percentage > 0 && (
                  <span className="text-xs text-domino-text-muted">
                    {col.missing_percentage.toFixed(1)}% missing
                  </span>
                )}
              </div>
            </button>
          ))}
          {filteredColumns.length === 0 && (
            <p className="p-4 text-sm text-domino-text-muted text-center">
              No columns match your search
            </p>
          )}
        </div>
      </div>

      {/* Column Details */}
      <div className="flex-1 border border-domino-border bg-white overflow-y-auto">
        {selectedColumnData ? (
          <div className="p-6 space-y-6">
            {/* Header */}
            <div className="flex items-start justify-between">
              <div>
                <h3 className="text-lg font-medium text-domino-text-primary">
                  {selectedColumnData.name}
                </h3>
                <div className="flex items-center gap-2 mt-1">
                  <span className={`text-xs px-2 py-1 rounded border ${getTypeColor(selectedColumnData.semantic_type)}`}>
                    {selectedColumnData.semantic_type}
                  </span>
                  <span className="text-sm text-domino-text-muted">
                    {selectedColumnData.dtype}
                  </span>
                </div>
              </div>
            </div>

            {/* Issues */}
            {selectedColumnData.issues && selectedColumnData.issues.length > 0 && (
              <div className="bg-yellow-50 border border-yellow-200 rounded p-3">
                <div className="flex items-center gap-2 text-yellow-800 mb-2">
                  <ExclamationTriangleIcon className="h-4 w-4" />
                  <span className="text-sm font-medium">Potential Issues</span>
                </div>
                <ul className="space-y-1">
                  {selectedColumnData.issues.map((issue, idx) => (
                    <li key={idx} className="text-sm text-yellow-700">
                      {issue}
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Summary Stats */}
            <div className="grid grid-cols-3 gap-4">
              <div className="bg-domino-bg-tertiary p-3 rounded">
                <p className="text-xs text-domino-text-muted uppercase tracking-wide">Unique Values</p>
                <p className="text-lg font-semibold text-domino-text-primary">
                  {selectedColumnData.unique_count.toLocaleString()}
                  <span className="text-sm font-normal text-domino-text-muted ml-1">
                    ({selectedColumnData.unique_percentage.toFixed(1)}%)
                  </span>
                </p>
              </div>
              <div className="bg-domino-bg-tertiary p-3 rounded">
                <p className="text-xs text-domino-text-muted uppercase tracking-wide">Missing</p>
                <p className="text-lg font-semibold text-domino-text-primary">
                  {selectedColumnData.missing_count.toLocaleString()}
                  <span className="text-sm font-normal text-domino-text-muted ml-1">
                    ({selectedColumnData.missing_percentage.toFixed(1)}%)
                  </span>
                </p>
              </div>
              <div className="bg-domino-bg-tertiary p-3 rounded">
                <p className="text-xs text-domino-text-muted uppercase tracking-wide">Data Type</p>
                <p className="text-lg font-semibold text-domino-text-primary">
                  {selectedColumnData.dtype}
                </p>
              </div>
            </div>

            {/* Numeric Statistics */}
            {selectedColumnData.statistics && 'mean' in selectedColumnData.statistics && (
              <div className="border border-domino-border rounded">
                <div className="px-4 py-2 bg-domino-bg-tertiary border-b border-domino-border">
                  <h4 className="text-sm font-medium text-domino-text-primary">Statistics</h4>
                </div>
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-4">
                  <div>
                    <p className="text-xs text-domino-text-muted">Min</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.min?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Max</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.max?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Mean</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.mean?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Median</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.median?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Std Dev</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.std?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Skewness</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.skewness?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                  <div>
                    <p className="text-xs text-domino-text-muted">Kurtosis</p>
                    <p className="text-sm font-medium text-domino-text-primary">
                      {selectedColumnData.statistics.kurtosis?.toLocaleString(undefined, { maximumFractionDigits: 4 })}
                    </p>
                  </div>
                </div>
              </div>
            )}

            {/* Histogram for numeric */}
            {selectedColumnData.histogram && (
              <div className="border border-domino-border rounded">
                <div className="px-4 py-2 bg-domino-bg-tertiary border-b border-domino-border">
                  <h4 className="text-sm font-medium text-domino-text-primary">Distribution</h4>
                </div>
                <div className="p-4">
                  <SimpleHistogram
                    counts={selectedColumnData.histogram.counts}
                    binEdges={selectedColumnData.histogram.bin_edges}
                  />
                </div>
              </div>
            )}

            {/* Value Counts for categorical */}
            {selectedColumnData.value_counts && selectedColumnData.value_counts.length > 0 && (
              <div className="border border-domino-border rounded">
                <div className="px-4 py-2 bg-domino-bg-tertiary border-b border-domino-border">
                  <h4 className="text-sm font-medium text-domino-text-primary">Top Values</h4>
                </div>
                <div className="p-4 space-y-2">
                  {selectedColumnData.value_counts.map((vc, idx) => (
                    <div key={idx} className="flex items-center gap-3">
                      <span className="text-sm text-domino-text-primary w-32 truncate" title={String(vc.value)}>
                        {String(vc.value)}
                      </span>
                      <div className="flex-1 h-5 bg-domino-bg-tertiary rounded overflow-hidden">
                        <div
                          className="h-full bg-domino-accent-purple rounded flex items-center justify-end pr-2"
                          style={{ width: `${vc.percentage}%` }}
                        >
                          {vc.percentage > 10 && (
                            <span className="text-xs text-white font-medium">
                              {vc.percentage.toFixed(1)}%
                            </span>
                          )}
                        </div>
                      </div>
                      <span className="text-xs text-domino-text-muted w-16 text-right">
                        {vc.count.toLocaleString()}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        ) : (
          <div className="flex items-center justify-center h-full text-domino-text-muted">
            Select a column to view details
          </div>
        )}
      </div>
    </div>
  )
}

// Format number to avoid scientific notation
function formatNumber(num: number): string {
  if (num === undefined || num === null || isNaN(num)) return '0'
  const abs = Math.abs(num)
  if (abs >= 1000000) return (num / 1000000).toFixed(1) + 'M'
  if (abs >= 1000) return (num / 1000).toFixed(1) + 'K'
  if (abs < 0.01 && abs > 0) return num.toFixed(4)
  if (Number.isInteger(num)) return num.toLocaleString()
  return num.toFixed(2)
}

// Simple histogram component using divs with axis labels
function SimpleHistogram({ counts, binEdges }: { counts: number[]; binEdges: number[] }) {
  const maxCount = Math.max(...counts)
  const minEdge = binEdges[0]
  const maxEdge = binEdges[binEdges.length - 1]

  return (
    <div>
      {/* Y-axis label */}
      <div className="flex items-center gap-2 mb-2">
        <span className="text-xs text-domino-text-muted">Count</span>
        <span className="text-xs text-domino-text-secondary">max: {formatNumber(maxCount)}</span>
      </div>

      {/* Chart */}
      <div className="flex items-end gap-1 h-32">
        {counts.map((count, idx) => {
          const height = maxCount > 0 ? (count / maxCount) * 100 : 0
          return (
            <div
              key={idx}
              className="flex-1 bg-domino-accent-purple hover:bg-domino-accent-purple/80 transition-colors rounded-t cursor-pointer group relative"
              style={{ height: `${height}%`, minHeight: count > 0 ? '4px' : '0' }}
              title={`${formatNumber(binEdges[idx])} - ${formatNumber(binEdges[idx + 1])}: ${count.toLocaleString()}`}
            >
              <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1 bg-gray-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 whitespace-nowrap z-10 pointer-events-none">
                {formatNumber(binEdges[idx])} - {formatNumber(binEdges[idx + 1])}<br/>
                {count.toLocaleString()} values
              </div>
            </div>
          )
        })}
      </div>

      {/* X-axis labels */}
      <div className="flex justify-between mt-2 text-xs text-domino-text-muted">
        <span>{formatNumber(minEdge)}</span>
        <span className="text-domino-text-secondary">Value Range</span>
        <span>{formatNumber(maxEdge)}</span>
      </div>
    </div>
  )
}
