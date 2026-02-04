import { useState, useMemo } from 'react'
import {
  ChartBarIcon,
  PresentationChartLineIcon,
  ChartPieIcon,
  ArrowsPointingOutIcon,
  PlusIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import type { ColumnProfile } from '../../types/profiling'

interface InteractiveChartsProps {
  columns: ColumnProfile[]
  filePath: string
}

type ChartType = 'bar' | 'histogram' | 'scatter' | 'pie' | 'box'

interface ChartConfig {
  id: string
  type: ChartType
  xAxis: string
  yAxis: string | null
  colorBy: string | null
  title: string
}

export function InteractiveCharts({ columns, filePath }: InteractiveChartsProps) {
  const [charts, setCharts] = useState<ChartConfig[]>([
    {
      id: '1',
      type: 'histogram',
      xAxis: columns.find((c) => c.semantic_type === 'numeric')?.name || columns[0]?.name || '',
      yAxis: null,
      colorBy: null,
      title: 'Distribution',
    },
  ])
  const [activeChartId, setActiveChartId] = useState('1')

  const numericColumns = useMemo(
    () => columns.filter((c) => ['numeric', 'monetary', 'percentage', 'count'].includes(c.semantic_type)),
    [columns]
  )

  const categoricalColumns = useMemo(
    () => columns.filter((c) => ['category', 'binary', 'boolean'].includes(c.semantic_type)),
    [columns]
  )

  const addChart = () => {
    const newId = String(Date.now())
    setCharts([
      ...charts,
      {
        id: newId,
        type: 'bar',
        xAxis: categoricalColumns[0]?.name || columns[0]?.name || '',
        yAxis: numericColumns[0]?.name || null,
        colorBy: null,
        title: `Chart ${charts.length + 1}`,
      },
    ])
    setActiveChartId(newId)
  }

  const removeChart = (id: string) => {
    if (charts.length <= 1) return
    const newCharts = charts.filter((c) => c.id !== id)
    setCharts(newCharts)
    if (activeChartId === id) {
      setActiveChartId(newCharts[0].id)
    }
  }

  const updateChart = (id: string, updates: Partial<ChartConfig>) => {
    setCharts(charts.map((c) => (c.id === id ? { ...c, ...updates } : c)))
  }

  const activeChart = charts.find((c) => c.id === activeChartId) || charts[0]

  const chartTypes: { type: ChartType; label: string; icon: typeof ChartBarIcon }[] = [
    { type: 'histogram', label: 'Histogram', icon: ChartBarIcon },
    { type: 'bar', label: 'Bar Chart', icon: ChartBarIcon },
    { type: 'scatter', label: 'Scatter Plot', icon: ArrowsPointingOutIcon },
    { type: 'pie', label: 'Pie Chart', icon: ChartPieIcon },
    { type: 'box', label: 'Box Plot', icon: PresentationChartLineIcon },
  ]

  return (
    <div className="space-y-4">
      {/* Chart Tabs */}
      <div className="flex items-center gap-2 border-b border-domino-border pb-2">
        {charts.map((chart) => (
          <button
            key={chart.id}
            onClick={() => setActiveChartId(chart.id)}
            className={`flex items-center gap-2 px-3 py-2 text-sm rounded-t transition-colors ${
              activeChartId === chart.id
                ? 'bg-domino-accent-purple text-white'
                : 'bg-domino-bg-tertiary text-domino-text-secondary hover:bg-gray-200'
            }`}
          >
            {chart.title}
            {charts.length > 1 && (
              <button
                onClick={(e) => {
                  e.stopPropagation()
                  removeChart(chart.id)
                }}
                className="hover:text-domino-accent-red"
              >
                <XMarkIcon className="h-3 w-3" />
              </button>
            )}
          </button>
        ))}
        <button
          onClick={addChart}
          className="flex items-center gap-1 px-3 py-2 text-sm text-domino-accent-purple hover:bg-domino-accent-purple/10 rounded transition-colors"
        >
          <PlusIcon className="h-4 w-4" />
          Add Chart
        </button>
      </div>

      {activeChart && (
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
          {/* Chart Configuration */}
          <div className="lg:col-span-1 space-y-4 border border-domino-border p-4 bg-domino-bg-tertiary rounded">
            <div>
              <label className="block text-xs font-medium text-domino-text-secondary uppercase tracking-wide mb-2">
                Chart Type
              </label>
              <div className="grid grid-cols-2 gap-2">
                {chartTypes.map(({ type, label, icon: Icon }) => (
                  <button
                    key={type}
                    onClick={() => updateChart(activeChart.id, { type })}
                    className={`flex flex-col items-center gap-1 p-2 rounded border transition-colors ${
                      activeChart.type === type
                        ? 'border-domino-accent-purple bg-domino-accent-purple/10 text-domino-accent-purple'
                        : 'border-domino-border bg-white hover:border-domino-text-muted'
                    }`}
                  >
                    <Icon className="h-5 w-5" />
                    <span className="text-xs">{label}</span>
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-domino-text-secondary uppercase tracking-wide mb-2">
                X-Axis
              </label>
              <Dropdown
                value={activeChart.xAxis}
                onChange={(val) => updateChart(activeChart.id, { xAxis: val })}
                options={columns.map((col) => ({
                  value: col.name,
                  label: `${col.name} (${col.semantic_type})`
                }))}
              />
            </div>

            {(activeChart.type === 'scatter' || activeChart.type === 'bar') && (
              <div>
                <label className="block text-xs font-medium text-domino-text-secondary uppercase tracking-wide mb-2">
                  Y-Axis
                </label>
                <Dropdown
                  value={activeChart.yAxis || ''}
                  onChange={(val) => updateChart(activeChart.id, { yAxis: val || null })}
                  options={[
                    { value: '', label: 'Count (default)' },
                    ...numericColumns.map((col) => ({ value: col.name, label: col.name }))
                  ]}
                />
              </div>
            )}

            <div>
              <label className="block text-xs font-medium text-domino-text-secondary uppercase tracking-wide mb-2">
                Color By
              </label>
              <Dropdown
                value={activeChart.colorBy || ''}
                onChange={(val) => updateChart(activeChart.id, { colorBy: val || null })}
                options={[
                  { value: '', label: 'None' },
                  ...categoricalColumns.map((col) => ({ value: col.name, label: col.name }))
                ]}
              />
            </div>

            <div>
              <label className="block text-xs font-medium text-domino-text-secondary uppercase tracking-wide mb-2">
                Chart Title
              </label>
              <input
                type="text"
                value={activeChart.title}
                onChange={(e) => updateChart(activeChart.id, { title: e.target.value })}
                className="w-full px-3 py-2 text-sm border border-domino-border rounded focus:outline-none focus:border-domino-accent-purple"
              />
            </div>
          </div>

          {/* Chart Display */}
          <div className="lg:col-span-3 border border-domino-border bg-white rounded p-4">
            <h3 className="text-sm font-medium text-domino-text-primary mb-4">{activeChart.title}</h3>
            <ChartRenderer
              config={activeChart}
              columns={columns}
              filePath={filePath}
            />
          </div>
        </div>
      )}
    </div>
  )
}

// Chart renderer component
function ChartRenderer({
  config,
  columns,
  filePath: _filePath,
}: {
  config: ChartConfig
  columns: ColumnProfile[]
  filePath: string
}) {
  void _filePath // Used for future API calls to fetch chart data
  const column = columns.find((c) => c.name === config.xAxis)

  if (!column) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        Select a column to visualize
      </div>
    )
  }

  switch (config.type) {
    case 'histogram':
      return <HistogramChart column={column} />
    case 'bar':
      return <BarChart column={column} />
    case 'pie':
      return <PieChart column={column} />
    case 'box':
      return <BoxPlot column={column} />
    case 'scatter':
      const yColumn = columns.find((c) => c.name === config.yAxis)
      return <ScatterPlot xColumn={column} yColumn={yColumn} />
    default:
      return null
  }
}

// Format number to avoid scientific notation
function formatNum(num: number | undefined): string {
  if (num === undefined || num === null || isNaN(num)) return '0'
  const abs = Math.abs(num)
  if (abs >= 1000000) return (num / 1000000).toFixed(1) + 'M'
  if (abs >= 1000) return (num / 1000).toFixed(1) + 'K'
  if (abs < 0.01 && abs > 0) return num.toFixed(4)
  if (Number.isInteger(num)) return num.toLocaleString()
  return num.toFixed(2)
}

// Histogram Chart
function HistogramChart({ column }: { column: ColumnProfile }) {
  if (!column.histogram) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        No histogram data available for this column
      </div>
    )
  }

  const { counts, bin_edges } = column.histogram
  const maxCount = Math.max(...counts)

  return (
    <div className="space-y-2">
      {/* Y-axis label */}
      <div className="flex items-center justify-between px-4">
        <span className="text-xs font-medium text-domino-text-secondary">Count (max: {formatNum(maxCount)})</span>
        <span className="text-xs text-domino-accent-purple font-medium">Column: {column.name}</span>
      </div>

      {/* Chart */}
      <div className="flex items-end gap-1 h-56 px-4">
        {counts.map((count, idx) => {
          const height = maxCount > 0 ? (count / maxCount) * 100 : 0
          const binStart = bin_edges[idx]
          const binEnd = bin_edges[idx + 1]
          return (
            <div
              key={idx}
              className="flex-1 bg-domino-accent-purple hover:bg-domino-accent-purple/80 transition-colors rounded-t cursor-pointer group relative"
              style={{ height: `${height}%`, minHeight: count > 0 ? '4px' : '0' }}
            >
              <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 px-2 py-1 bg-gray-800 text-white text-xs rounded opacity-0 group-hover:opacity-100 whitespace-nowrap z-10 pointer-events-none">
                Range: {formatNum(binStart)} - {formatNum(binEnd)}<br />
                Count: {count.toLocaleString()}
              </div>
            </div>
          )
        })}
      </div>

      {/* X-axis label */}
      <div className="flex justify-between items-center text-xs px-4 pt-2 border-t border-domino-border">
        <span className="text-domino-text-muted">{formatNum(bin_edges[0])}</span>
        <span className="font-medium text-domino-text-secondary">{column.name}</span>
        <span className="text-domino-text-muted">{formatNum(bin_edges[bin_edges.length - 1])}</span>
      </div>
    </div>
  )
}

// Bar Chart
function BarChart({ column }: { column: ColumnProfile }) {
  const data = column.value_counts?.slice(0, 15) || []

  if (data.length === 0) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        No value counts available for this column
      </div>
    )
  }

  const maxPercentage = Math.max(...data.map((d) => d.percentage))

  return (
    <div className="space-y-2">
      {/* Header */}
      <div className="flex items-center justify-between px-2 pb-2 border-b border-domino-border">
        <span className="text-xs font-medium text-domino-text-secondary">Top values in: <span className="text-domino-accent-purple">{column.name}</span></span>
        <span className="text-xs text-domino-text-muted">{data.length} of {column.unique_count} unique values</span>
      </div>

      {/* Bars */}
      <div className="space-y-2 h-56 overflow-y-auto">
        {data.map((item, idx) => (
          <div key={idx} className="flex items-center gap-3">
            <span className="text-sm text-domino-text-primary w-32 truncate text-right" title={String(item.value)}>
              {String(item.value)}
            </span>
            <div className="flex-1 h-6 bg-domino-bg-tertiary rounded overflow-hidden">
              <div
                className="h-full bg-domino-accent-purple rounded flex items-center justify-end pr-2 transition-all"
                style={{ width: `${(item.percentage / maxPercentage) * 100}%` }}
              >
                {item.percentage > 10 && (
                  <span className="text-xs text-white font-medium">
                    {item.percentage.toFixed(1)}%
                  </span>
                )}
              </div>
            </div>
            <span className="text-xs text-domino-text-muted w-16 text-right">
              {item.count.toLocaleString()}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}

// Pie Chart (using CSS)
function PieChart({ column }: { column: ColumnProfile }) {
  const data = column.value_counts?.slice(0, 8) || []

  if (data.length === 0) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        No value counts available for this column
      </div>
    )
  }

  const colors = [
    '#5046e4', '#22c55e', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4', '#ec4899', '#84cc16'
  ]

  // Create conic gradient for pie chart
  let gradientParts: string[] = []
  let currentAngle = 0
  data.forEach((item, idx) => {
    const angle = (item.percentage / 100) * 360
    gradientParts.push(`${colors[idx % colors.length]} ${currentAngle}deg ${currentAngle + angle}deg`)
    currentAngle += angle
  })

  return (
    <div className="flex items-center justify-center gap-8 h-64">
      <div
        className="w-48 h-48 rounded-full shadow-lg"
        style={{
          background: `conic-gradient(${gradientParts.join(', ')})`,
        }}
      />
      <div className="space-y-2">
        {data.map((item, idx) => (
          <div key={idx} className="flex items-center gap-2">
            <div
              className="w-3 h-3 rounded"
              style={{ backgroundColor: colors[idx % colors.length] }}
            />
            <span className="text-sm text-domino-text-primary truncate max-w-[120px]" title={String(item.value)}>
              {String(item.value)}
            </span>
            <span className="text-xs text-domino-text-muted">
              {item.percentage.toFixed(1)}%
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}

// Box Plot (simplified)
function BoxPlot({ column }: { column: ColumnProfile }) {
  const stats = column.statistics

  if (!stats || stats.min === undefined) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        No statistics available for this column
      </div>
    )
  }

  const { min, max, q1, median, q3 } = stats as { min: number; max: number; q1?: number; median?: number; q3?: number }
  const range = max - min

  if (range === 0) {
    return (
      <div className="flex items-center justify-center h-64 text-domino-text-muted">
        All values are identical
      </div>
    )
  }

  const getPosition = (value: number) => ((value - min) / range) * 100

  return (
    <div className="flex flex-col items-center justify-center h-64 px-8">
      <div className="w-full h-20 relative">
        {/* Whiskers */}
        <div
          className="absolute h-0.5 bg-domino-text-muted top-1/2 -translate-y-1/2"
          style={{
            left: '0%',
            right: `${100 - (q3 !== undefined ? getPosition(q3) : getPosition(max))}%`,
          }}
        />

        {/* Min line */}
        <div className="absolute w-0.5 h-4 bg-domino-text-muted top-1/2 -translate-y-1/2" style={{ left: '0%' }} />

        {/* Box */}
        {q1 !== undefined && q3 !== undefined && (
          <div
            className="absolute h-12 bg-domino-accent-purple/20 border-2 border-domino-accent-purple top-1/2 -translate-y-1/2 rounded"
            style={{
              left: `${getPosition(q1)}%`,
              width: `${getPosition(q3) - getPosition(q1)}%`,
            }}
          />
        )}

        {/* Median line */}
        {median !== undefined && (
          <div
            className="absolute w-1 h-12 bg-domino-accent-purple top-1/2 -translate-y-1/2"
            style={{ left: `${getPosition(median)}%` }}
          />
        )}

        {/* Max line */}
        <div className="absolute w-0.5 h-4 bg-domino-text-muted top-1/2 -translate-y-1/2" style={{ left: '100%' }} />
      </div>

      {/* Labels */}
      <div className="w-full flex justify-between text-xs text-domino-text-muted mt-4">
        <span>{min.toFixed(2)}</span>
        {q1 !== undefined && <span>Q1: {q1.toFixed(2)}</span>}
        {median !== undefined && <span>Med: {median.toFixed(2)}</span>}
        {q3 !== undefined && <span>Q3: {q3.toFixed(2)}</span>}
        <span>{max.toFixed(2)}</span>
      </div>
    </div>
  )
}

// Scatter Plot (simplified - would need actual data)
function ScatterPlot({
  xColumn,
  yColumn,
}: {
  xColumn: ColumnProfile
  yColumn?: ColumnProfile
}) {
  return (
    <div className="flex items-center justify-center h-64 text-domino-text-muted">
      <div className="text-center">
        <p>Scatter plot visualization</p>
        <p className="text-sm mt-2">
          X: {xColumn.name}
          {yColumn && <span> | Y: {yColumn.name}</span>}
        </p>
        <p className="text-xs mt-4 text-domino-text-muted">
          (Full scatter plot requires loading raw data points)
        </p>
      </div>
    </div>
  )
}
