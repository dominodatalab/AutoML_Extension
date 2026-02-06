import { useRef, useState, useCallback } from 'react'
import type { TimeSeriesProfile } from '../../types/profiling'

interface StationarityTrendPanelProps {
  profile: TimeSeriesProfile
}

function StatCard({ label, value, color }: { label: string; value: string | number; color?: string }) {
  return (
    <div className="flex justify-between items-center py-1.5">
      <span className="text-sm text-domino-text-secondary">{label}</span>
      <span className={`text-sm font-medium ${color || 'text-domino-text-primary'}`}>{value}</span>
    </div>
  )
}

function formatTick(v: number): string {
  return Math.abs(v) >= 1000 ? `${(v / 1000).toFixed(1)}k` : v.toFixed(2)
}

function formatTimestamp(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

function formatTimestampFull(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

function SVGLineChart({
  title,
  datasets,
  timestamps,
  fullWidth,
}: {
  title: string
  datasets: { label: string; values: (number | null)[]; color: string }[]
  timestamps?: string[]
  fullWidth?: boolean
}) {
  const svgRef = useRef<SVGSVGElement>(null)
  const [hoverIndex, setHoverIndex] = useState<number | null>(null)

  // Each dataset's valid (non-null) values
  const validSets = datasets.map((d) => d.values.filter((v): v is number => v !== null))
  const maxLen = Math.max(...validSets.map((v) => v.length))
  const allValues = validSets.flat()
  if (allValues.length < 2 || maxLen < 2) return null

  const minVal = Math.min(...allValues)
  const maxVal = Math.max(...allValues)
  const range = maxVal - minVal || 1

  const width = 800
  const height = 140
  const pad = { top: 8, right: 10, bottom: 30, left: 60 }
  const plotW = width - pad.left - pad.right
  const plotH = height - pad.top - pad.bottom

  const toX = (i: number, len: number) => pad.left + (i / (len - 1)) * plotW
  const toY = (v: number) => pad.top + plotH - ((v - minVal) / range) * plotH

  // X-axis ticks: ~5 evenly spaced
  const xTickCount = Math.min(5, maxLen)
  const xTicks = Array.from({ length: xTickCount }, (_, i) =>
    Math.round((i / (xTickCount - 1)) * (maxLen - 1))
  )

  const onMouseMove = useCallback((e: React.MouseEvent<SVGSVGElement>) => {
    const svg = svgRef.current
    if (!svg) return
    const rect = svg.getBoundingClientRect()
    const svgX = ((e.clientX - rect.left) / rect.width) * width
    const frac = (svgX - pad.left) / plotW
    if (frac < 0 || frac > 1) { setHoverIndex(null); return }
    setHoverIndex(Math.round(frac * (maxLen - 1)))
  }, [maxLen, plotW, width])

  const onMouseLeave = useCallback(() => setHoverIndex(null), [])

  // Tooltip position as percentage for CSS positioning
  const tooltipLeft = hoverIndex !== null ? ((toX(hoverIndex, maxLen) / width) * 100) : 0

  return (
    <div>
      <h4 className="text-xs font-medium text-domino-text-secondary mb-1">{title}</h4>
      <div className="relative">
        <svg
          ref={svgRef}
          viewBox={`0 0 ${width} ${height}`}
          className={`w-full border border-domino-border bg-white ${fullWidth ? '' : 'max-w-3xl mx-auto'}`}
          onMouseMove={onMouseMove}
          onMouseLeave={onMouseLeave}
        >
          {/* Zero line */}
          {minVal < 0 && maxVal > 0 && (
            <line
              x1={pad.left} y1={toY(0)} x2={width - pad.right} y2={toY(0)}
              stroke="#d1d5db" strokeDasharray="4 2"
            />
          )}
          {/* Y-axis labels */}
          {[minVal, (minVal + maxVal) / 2, maxVal].map((tick, i) => (
            <text key={i} x={pad.left - 5} y={toY(tick) + 4} textAnchor="end" className="text-[10px] fill-gray-500">
              {formatTick(tick)}
            </text>
          ))}
          {/* X-axis ticks */}
          {xTicks.map((idx) => (
            <text key={idx} x={toX(idx, maxLen)} y={pad.top + plotH + 16} textAnchor="middle" className="text-[10px] fill-gray-500">
              {timestamps?.[idx] ? formatTimestamp(timestamps[idx]) : idx}
            </text>
          ))}
          {/* Lines */}
          {validSets.map((vals, di) => {
            if (vals.length < 2) return null
            const points = vals.map((v, i) => `${toX(i, vals.length)},${toY(v)}`).join(' ')
            return <polyline key={di} points={points} fill="none" stroke={datasets[di].color} strokeWidth="1.5" />
          })}
          {/* Hover crosshair + dots */}
          {hoverIndex !== null && (
            <>
              <line
                x1={toX(hoverIndex, maxLen)} y1={pad.top}
                x2={toX(hoverIndex, maxLen)} y2={pad.top + plotH}
                stroke="#9ca3af" strokeWidth="1" strokeDasharray="4 2"
              />
              {validSets.map((vals, di) => {
                if (hoverIndex >= vals.length) return null
                return (
                  <circle
                    key={di}
                    cx={toX(hoverIndex, vals.length)}
                    cy={toY(vals[hoverIndex])}
                    r="4" fill={datasets[di].color} stroke="white" strokeWidth="1.5"
                  />
                )
              })}
            </>
          )}
          {/* Legend — always show */}
          {datasets.map((d, i) => (
            <g key={i}>
              <line x1={pad.left + i * 120} y1={height - 8} x2={pad.left + i * 120 + 20} y2={height - 8} stroke={d.color} strokeWidth="2" />
              <text x={pad.left + i * 120 + 25} y={height - 4} className="text-[10px] fill-gray-600">{d.label}</text>
            </g>
          ))}
        </svg>
        {/* Tooltip */}
        {hoverIndex !== null && (
          <div
            className="absolute top-2 pointer-events-none bg-white border border-gray-200 shadow-sm px-2 py-1.5 text-xs whitespace-nowrap z-10"
            style={{
              left: `${tooltipLeft}%`,
              transform: tooltipLeft > 75 ? 'translateX(-100%)' : tooltipLeft < 25 ? 'none' : 'translateX(-50%)',
            }}
          >
            <div className="font-medium text-gray-700 mb-0.5">
              {timestamps?.[hoverIndex] ? formatTimestampFull(timestamps[hoverIndex]) : `Index: ${hoverIndex}`}
            </div>
            {validSets.map((vals, di) => {
              if (hoverIndex >= vals.length) return null
              return (
                <div key={di} className="flex items-center gap-1.5">
                  <span className="inline-block w-2 h-2 rounded-full" style={{ backgroundColor: datasets[di].color }} />
                  <span className="text-gray-600">{datasets[di].label}: {formatTick(vals[hoverIndex])}</span>
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}

export function StationarityTrendPanel({ profile }: StationarityTrendPanelProps) {
  const { stationarity, trend_analysis: trend, rolling_statistics: rolling, seasonality } = profile

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* ADF Test Results */}
        <div className="border border-domino-border p-4">
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">ADF Stationarity Test</h3>
          {stationarity ? (
            <div className="space-y-1">
              <div className="mb-3">
                <span className={`inline-block px-2 py-0.5 text-xs rounded-[2px] font-medium ${
                  stationarity.is_stationary ? 'bg-green-100 text-green-800' : 'bg-amber-100 text-amber-800'
                }`}>
                  {stationarity.interpretation}
                </span>
              </div>
              <StatCard label="Test Statistic" value={stationarity.adf_statistic} />
              <StatCard
                label="p-value"
                value={stationarity.p_value < 0.001 ? '< 0.001' : stationarity.p_value.toFixed(4)}
                color={stationarity.p_value < 0.05 ? 'text-green-700' : 'text-amber-700'}
              />
              <StatCard label="Observations" value={stationarity.num_observations.toLocaleString()} />
              <div className="border-t border-domino-border mt-2 pt-2">
                <p className="text-xs text-domino-text-muted mb-1">Critical Values</p>
                {Object.entries(stationarity.critical_values).map(([key, val]) => (
                  <StatCard key={key} label={key} value={val} />
                ))}
              </div>
            </div>
          ) : (
            <p className="text-sm text-domino-text-muted">Insufficient data for stationarity test</p>
          )}
        </div>

        {/* Trend Analysis */}
        <div className="border border-domino-border p-4">
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">Trend Analysis</h3>
          {trend ? (
            <div className="space-y-1">
              <div className="mb-3">
                <span className="text-2xl mr-2">
                  {trend.direction === 'upward' ? '\u2197' : trend.direction === 'downward' ? '\u2198' : '\u2192'}
                </span>
                <span className="text-sm font-medium text-domino-text-primary capitalize">{trend.direction} Trend</span>
              </div>
              <StatCard label="Slope" value={trend.slope.toExponential(3)} />
              <StatCard
                label="R-squared"
                value={trend.r_squared.toFixed(4)}
                color={trend.r_squared > 0.5 ? 'text-domino-accent-purple' : undefined}
              />
              <p className="text-xs text-domino-text-muted mt-3">
                {trend.r_squared > 0.7
                  ? 'Strong linear trend detected'
                  : trend.r_squared > 0.3
                  ? 'Moderate linear trend'
                  : 'Weak or no linear trend'}
              </p>
            </div>
          ) : (
            <p className="text-sm text-domino-text-muted">Insufficient data for trend analysis</p>
          )}
        </div>
      </div>

      {/* Rolling Statistics Chart */}
      {rolling && (
        <SVGLineChart
          title={`Rolling Mean & Standard Deviation (window=${rolling.window_size})`}
          datasets={[
            { label: 'Rolling Mean', values: rolling.rolling_mean, color: '#7c3aed' },
            { label: 'Rolling Std', values: rolling.rolling_std, color: '#f59e0b' },
          ]}
          timestamps={rolling.timestamps}
        />
      )}

      {/* Decomposition Charts */}
      {seasonality && (
        <div>
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">
            Seasonal Decomposition ({seasonality.model}, period={seasonality.period})
          </h3>
          <div className="flex flex-wrap gap-4">
            <div className="flex-1 min-w-[420px]">
              <SVGLineChart
                title="Trend Component"
                datasets={[{ label: 'Trend', values: seasonality.trend.values, color: '#2563eb' }]}
                timestamps={seasonality.trend.timestamps}
                fullWidth
              />
            </div>
            <div className="flex-1 min-w-[420px]">
              <SVGLineChart
                title="Seasonal Component"
                datasets={[{ label: 'Seasonal', values: seasonality.seasonal.values, color: '#16a34a' }]}
                timestamps={seasonality.seasonal.timestamps}
                fullWidth
              />
            </div>
            <div className="flex-1 min-w-[420px]">
              <SVGLineChart
                title="Residual Component"
                datasets={[{ label: 'Residual', values: seasonality.residual.values, color: '#dc2626' }]}
                timestamps={seasonality.residual.timestamps}
                fullWidth
              />
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
