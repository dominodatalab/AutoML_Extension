import { useState, useMemo } from 'react'
import type { ColumnProfile } from '../../types/profiling'

interface CorrelationMatrixProps {
  correlations: Record<string, Record<string, number>> | { matrix?: Record<string, Record<string, number>>; high_correlations?: Array<{ column1: string; column2: string; correlation: number }> }
  columns: ColumnProfile[]
}

export function CorrelationMatrix({ correlations, columns: _columns }: CorrelationMatrixProps) {
  void _columns // Available for future use with column metadata
  const [hoveredCell, setHoveredCell] = useState<{ row: string; col: string } | null>(null)
  const [minCorrelation, setMinCorrelation] = useState(0)

  // Extract matrix and high correlations with proper type handling
  const rawMatrix = 'matrix' in correlations ? correlations.matrix : correlations
  const matrix: Record<string, Record<string, number>> | undefined =
    rawMatrix && typeof rawMatrix === 'object' ? rawMatrix as Record<string, Record<string, number>> : undefined
  const highCorrelations: Array<{ column1: string; column2: string; correlation: number }> =
    ('high_correlations' in correlations && Array.isArray(correlations.high_correlations))
      ? correlations.high_correlations
      : []

  // Get numeric column names from matrix
  const numericColumns = useMemo(() => {
    if (!matrix) return []
    return Object.keys(matrix)
  }, [matrix])

  // Filter to show only correlations above threshold
  const filteredColumns = useMemo(() => {
    if (minCorrelation === 0) return numericColumns

    const relevantCols = new Set<string>()
    numericColumns.forEach((col1) => {
      numericColumns.forEach((col2) => {
        const corr = matrix?.[col1]?.[col2]
        if (corr !== undefined && col1 !== col2 && Math.abs(corr) >= minCorrelation) {
          relevantCols.add(col1)
          relevantCols.add(col2)
        }
      })
    })
    return numericColumns.filter((c) => relevantCols.has(c))
  }, [numericColumns, matrix, minCorrelation])

  const getCorrelationColor = (value: number) => {
    if (value === undefined || isNaN(value)) return 'bg-gray-100'
    if (value === 1) return 'bg-domino-accent-purple'

    const absValue = Math.abs(value)
    if (value > 0) {
      // Positive correlation - blue/purple shades
      if (absValue > 0.8) return 'bg-domino-accent-purple'
      if (absValue > 0.6) return 'bg-domino-accent-purple/80'
      if (absValue > 0.4) return 'bg-domino-accent-purple/60'
      if (absValue > 0.2) return 'bg-domino-accent-purple/40'
      return 'bg-domino-accent-purple/20'
    } else {
      // Negative correlation - red shades
      if (absValue > 0.8) return 'bg-red-600'
      if (absValue > 0.6) return 'bg-red-500'
      if (absValue > 0.4) return 'bg-red-400'
      if (absValue > 0.2) return 'bg-red-300'
      return 'bg-red-200'
    }
  }

  const getTextColor = (value: number) => {
    if (value === undefined || isNaN(value)) return 'text-gray-400'
    const absValue = Math.abs(value)
    if (absValue > 0.5 || value === 1) return 'text-white'
    return 'text-gray-700'
  }

  if (!matrix || numericColumns.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-12 text-domino-text-muted">
        <p>No correlation data available</p>
        <p className="text-sm mt-2">Correlations require at least 2 numeric columns</p>
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {/* Controls */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <label className="flex items-center gap-2 text-sm text-domino-text-secondary">
            <span>Min correlation:</span>
            <input
              type="range"
              min="0"
              max="0.9"
              step="0.1"
              value={minCorrelation}
              onChange={(e) => setMinCorrelation(parseFloat(e.target.value))}
              className="w-32"
            />
            <span className="w-8 text-domino-text-primary">{minCorrelation.toFixed(1)}</span>
          </label>
        </div>
        <div className="text-sm text-domino-text-muted">
          {filteredColumns.length} of {numericColumns.length} columns
        </div>
      </div>

      {/* Legend */}
      <div className="flex items-center gap-4 text-sm">
        <span className="text-domino-text-muted">Correlation:</span>
        <div className="flex items-center gap-1">
          <div className="w-4 h-4 bg-red-600 rounded" />
          <span className="text-xs">-1</span>
        </div>
        <div className="flex items-center gap-1">
          <div className="w-4 h-4 bg-red-300 rounded" />
          <span className="text-xs">-0.5</span>
        </div>
        <div className="flex items-center gap-1">
          <div className="w-4 h-4 bg-gray-200 rounded" />
          <span className="text-xs">0</span>
        </div>
        <div className="flex items-center gap-1">
          <div className="w-4 h-4 bg-domino-accent-purple/40 rounded" />
          <span className="text-xs">0.5</span>
        </div>
        <div className="flex items-center gap-1">
          <div className="w-4 h-4 bg-domino-accent-purple rounded" />
          <span className="text-xs">1</span>
        </div>
      </div>

      {/* Matrix */}
      <div className="overflow-auto" style={{ maxHeight: `${Math.min(800, 200 + filteredColumns.length * 56)}px` }}>
        <table className="text-sm border-collapse">
          <thead>
            <tr>
              <th className="sticky left-0 top-0 z-20 bg-white p-2 border-b border-r border-domino-border"></th>
              {filteredColumns.map((col) => (
                <th
                  key={col}
                  className="sticky top-0 z-10 bg-white p-2 text-xs font-medium text-domino-text-secondary border-b border-domino-border"
                  style={{ writingMode: 'vertical-rl', textOrientation: 'mixed', minHeight: '120px', maxWidth: '56px' }}
                >
                  <span className="block truncate" style={{ maxHeight: '120px' }} title={col}>
                    {col.length > 15 ? col.substring(0, 15) + '...' : col}
                  </span>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filteredColumns.map((row) => (
              <tr key={row}>
                <td className="sticky left-0 z-10 bg-white p-2 text-xs font-medium text-domino-text-secondary border-r border-domino-border whitespace-nowrap" title={row}>
                  {row.length > 18 ? row.substring(0, 18) + '...' : row}
                </td>
                {filteredColumns.map((col) => {
                  const value = matrix?.[row]?.[col]
                  const isHovered = hoveredCell?.row === row && hoveredCell?.col === col
                  return (
                    <td
                      key={col}
                      className={`p-1 text-center cursor-pointer transition-all ${
                        isHovered ? 'ring-2 ring-domino-accent-purple ring-offset-1' : ''
                      }`}
                      onMouseEnter={() => setHoveredCell({ row, col })}
                      onMouseLeave={() => setHoveredCell(null)}
                    >
                      <div
                        className={`w-12 h-12 flex items-center justify-center rounded text-xs font-medium ${getCorrelationColor(
                          value
                        )} ${getTextColor(value)}`}
                        title={`${row} vs ${col}: ${value?.toFixed(3) || 'N/A'}`}
                      >
                        {value !== undefined && value != null ? value.toFixed(2) : '-'}
                      </div>
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* High Correlations List */}
      {highCorrelations && highCorrelations.length > 0 && (
        <div className="border border-domino-border rounded">
          <div className="px-4 py-2 bg-domino-bg-tertiary border-b border-domino-border">
            <h4 className="text-sm font-medium text-domino-text-primary">
              Highly Correlated Pairs (|r| &gt; 0.8)
            </h4>
          </div>
          <div className="p-4 space-y-2 max-h-48 overflow-y-auto">
            {highCorrelations.map((pair, idx) => (
              <div key={idx} className="flex items-center gap-3">
                <span className="text-sm text-domino-text-primary">{pair.column1}</span>
                <span className="text-domino-text-muted">↔</span>
                <span className="text-sm text-domino-text-primary">{pair.column2}</span>
                <span
                  className={`ml-auto text-sm font-medium ${
                    pair.correlation > 0 ? 'text-domino-accent-purple' : 'text-red-600'
                  }`}
                >
                  {pair.correlation.toFixed(4)}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
