import { useRef, useState, useCallback } from 'react'
import type { TimeSeriesProfile } from '../../types/profiling'

interface TimeSeriesOverviewProps {
  profile: TimeSeriesProfile
}

function SummaryCard({ label, value, subtext }: { label: string; value: string | number; subtext?: string }) {
  return (
    <div className="bg-domino-bg-tertiary border border-domino-border p-4">
      <p className="text-xs text-domino-text-muted uppercase">{label}</p>
      <p className="text-lg font-medium text-domino-text-primary mt-1">{value}</p>
      {subtext && <p className="text-xs text-domino-text-secondary mt-0.5">{subtext}</p>}
    </div>
  )
}

function Badge({ label, positive }: { label: string; positive: boolean }) {
  return (
    <span className={`inline-block px-2 py-0.5 text-xs rounded-[2px] font-medium ${
      positive ? 'bg-green-100 text-green-800' : 'bg-amber-100 text-amber-800'
    }`}>
      {label}
    </span>
  )
}

function formatTimestamp(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

function formatTimestampFull(ts: string): string {
  const d = new Date(ts)
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

function TargetLineChart({ profile }: { profile: TimeSeriesProfile }) {
  const svgRef = useRef<SVGSVGElement>(null)
  const [hoverIndex, setHoverIndex] = useState<number | null>(null)

  const data = profile.rolling_statistics
  if (!data || !data.rolling_mean.length) return null

  const values = data.rolling_mean.filter((v): v is number => v !== null)
  if (values.length < 2) return null

  const minVal = Math.min(...values)
  const maxVal = Math.max(...values)
  const range = maxVal - minVal || 1

  const width = 800
  const height = 150
  const pad = { top: 8, right: 10, bottom: 30, left: 60 }
  const plotW = width - pad.left - pad.right
  const plotH = height - pad.top - pad.bottom

  const toX = (i: number) => pad.left + (i / (values.length - 1)) * plotW
  const toY = (v: number) => pad.top + plotH - ((v - minVal) / range) * plotH
  const fmtTick = (v: number) => (Math.abs(v) >= 1000 ? `${(v / 1000).toFixed(1)}k` : v.toFixed(1))

  const points = values.map((v, i) => `${toX(i)},${toY(v)}`).join(' ')
  const yTicks = [minVal, minVal + range * 0.5, maxVal]

  // X-axis ticks: ~5 evenly spaced
  const xTickCount = Math.min(5, values.length)
  const xTicks = Array.from({ length: xTickCount }, (_, i) =>
    Math.round((i / (xTickCount - 1)) * (values.length - 1))
  )

  const onMouseMove = useCallback((e: React.MouseEvent<SVGSVGElement>) => {
    const svg = svgRef.current
    if (!svg) return
    const rect = svg.getBoundingClientRect()
    const svgX = ((e.clientX - rect.left) / rect.width) * width
    const frac = (svgX - pad.left) / plotW
    if (frac < 0 || frac > 1) { setHoverIndex(null); return }
    setHoverIndex(Math.round(frac * (values.length - 1)))
  }, [values.length, plotW, width])

  const onMouseLeave = useCallback(() => setHoverIndex(null), [])

  const tooltipLeft = hoverIndex !== null ? ((toX(hoverIndex) / width) * 100) : 0

  return (
    <div>
      <h3 className="text-sm font-medium text-domino-text-primary mb-2">{`Target Over Time (Rolling Mean, window=${data.window_size})`}</h3>
      <div className="relative">
        <svg
          ref={svgRef}
          viewBox={`0 0 ${width} ${height}`}
          className="w-full max-w-3xl mx-auto border border-domino-border bg-white"
          onMouseMove={onMouseMove}
          onMouseLeave={onMouseLeave}
        >
          {/* Grid lines + Y-axis labels */}
          {yTicks.map((tick, i) => {
            const y = toY(tick)
            return (
              <g key={i}>
                <line x1={pad.left} y1={y} x2={width - pad.right} y2={y} stroke="#e5e7eb" strokeWidth="1" />
                <text x={pad.left - 5} y={y + 4} textAnchor="end" className="text-[10px] fill-gray-500">
                  {fmtTick(tick)}
                </text>
              </g>
            )
          })}
          {/* X-axis ticks */}
          {xTicks.map((idx) => (
            <text key={idx} x={toX(idx)} y={pad.top + plotH + 16} textAnchor="middle" className="text-[10px] fill-gray-500">
              {data.timestamps?.[idx] ? formatTimestamp(data.timestamps[idx]) : idx}
            </text>
          ))}
          {/* Line */}
          <polyline points={points} fill="none" stroke="#7c3aed" strokeWidth="1.5" />
          {/* Hover crosshair + dot */}
          {hoverIndex !== null && (
            <>
              <line
                x1={toX(hoverIndex)} y1={pad.top}
                x2={toX(hoverIndex)} y2={pad.top + plotH}
                stroke="#9ca3af" strokeWidth="1" strokeDasharray="4 2"
              />
              <circle
                cx={toX(hoverIndex)} cy={toY(values[hoverIndex])}
                r="4" fill="#7c3aed" stroke="white" strokeWidth="1.5"
              />
            </>
          )}
          {/* Legend */}
          <line x1={pad.left} y1={height - 8} x2={pad.left + 20} y2={height - 8} stroke="#7c3aed" strokeWidth="2" />
          <text x={pad.left + 25} y={height - 4} className="text-[10px] fill-gray-600">Rolling Mean</text>
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
              {data.timestamps?.[hoverIndex] ? formatTimestampFull(data.timestamps[hoverIndex]) : `Index: ${hoverIndex}`}
            </div>
            <div className="flex items-center gap-1.5">
              <span className="inline-block w-2 h-2 rounded-full bg-[#7c3aed]" />
              <span className="text-gray-600">Rolling Mean: {fmtTick(values[hoverIndex])}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export function TimeSeriesOverview({ profile }: TimeSeriesOverviewProps) {
  const { temporal_summary: summary, gap_analysis: gaps, stationarity } = profile

  const dateRange = summary.date_range_start && summary.date_range_end
    ? `${summary.date_range_start.split('T')[0]} to ${summary.date_range_end.split('T')[0]}`
    : 'N/A'

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
        <SummaryCard label="Series" value={summary.num_series} />
        <SummaryCard label="Observations" value={summary.total_observations.toLocaleString()} subtext={`of ${summary.total_rows.toLocaleString()} total`} />
        <SummaryCard label="Date Range" value={dateRange} />
        <SummaryCard label="Frequency" value={summary.inferred_frequency || 'Unknown'} />
        <SummaryCard label="Gaps" value={gaps.total_gaps} subtext={gaps.irregular_intervals ? 'Irregular intervals' : 'Regular intervals'} />
        <div className="bg-domino-bg-tertiary border border-domino-border p-4">
          <p className="text-xs text-domino-text-muted uppercase">Stationarity</p>
          <div className="mt-1">
            {stationarity ? (
              <Badge label={stationarity.interpretation} positive={stationarity.is_stationary} />
            ) : (
              <span className="text-sm text-domino-text-secondary">N/A</span>
            )}
          </div>
        </div>
      </div>

      {/* Target line chart */}
      <TargetLineChart profile={profile} />

      {/* Gap Analysis Table */}
      {gaps.total_gaps > 0 && (
        <div>
          <h3 className="text-sm font-medium text-domino-text-primary mb-2">
            Gap Analysis ({gaps.total_gaps} gap{gaps.total_gaps !== 1 ? 's' : ''})
          </h3>
          <div className="overflow-auto border border-domino-border" style={{ maxHeight: '300px' }}>
            <table className="w-full text-sm">
              <thead className="sticky top-0 bg-domino-bg-tertiary">
                <tr>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Start</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">End</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Duration</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Missing Periods</th>
                </tr>
              </thead>
              <tbody>
                {gaps.gaps.map((gap, idx) => (
                  <tr key={idx} className="border-b border-domino-border hover:bg-domino-bg-tertiary">
                    <td className="px-3 py-2 text-domino-text-primary">{gap.start}</td>
                    <td className="px-3 py-2 text-domino-text-primary">{gap.end}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{gap.duration}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{gap.missing_periods}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Per-Series Summary */}
      {profile.per_series_summary && profile.per_series_summary.length > 0 && (
        <div>
          <h3 className="text-sm font-medium text-domino-text-primary mb-2">
            Per-Series Summary ({profile.per_series_summary.length} series)
          </h3>
          <div className="overflow-auto border border-domino-border" style={{ maxHeight: '300px' }}>
            <table className="w-full text-sm">
              <thead className="sticky top-0 bg-domino-bg-tertiary">
                <tr>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">ID</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Count</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Start</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">End</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Missing %</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Mean</th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase border-b border-domino-border">Std</th>
                </tr>
              </thead>
              <tbody>
                {profile.per_series_summary.map((s, idx) => (
                  <tr key={idx} className="border-b border-domino-border hover:bg-domino-bg-tertiary">
                    <td className="px-3 py-2 font-medium text-domino-text-primary">{s.id}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{s.count.toLocaleString()}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{s.date_range_start?.split('T')[0] ?? '-'}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{s.date_range_end?.split('T')[0] ?? '-'}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{(s.missing_rate * 100).toFixed(1)}%</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{s.mean?.toFixed(2) ?? '-'}</td>
                    <td className="px-3 py-2 text-domino-text-secondary">{s.std?.toFixed(2) ?? '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Recommendations & Warnings */}
      {(profile.recommendations.length > 0 || profile.warnings.length > 0) && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {profile.recommendations.length > 0 && (
            <div>
              <h3 className="text-sm font-medium text-domino-text-primary mb-2">Recommendations</h3>
              <div className="space-y-2">
                {profile.recommendations.map((r, i) => (
                  <div key={i} className="p-3 bg-blue-50 border border-blue-200 text-sm text-blue-800">
                    {r.message}
                  </div>
                ))}
              </div>
            </div>
          )}
          {profile.warnings.length > 0 && (
            <div>
              <h3 className="text-sm font-medium text-domino-text-primary mb-2">Warnings</h3>
              <div className="space-y-2">
                {profile.warnings.map((w, i) => (
                  <div key={i} className={`p-3 border text-sm ${
                    w.severity === 'error' ? 'bg-red-50 border-red-200 text-red-800' :
                    w.severity === 'warning' ? 'bg-amber-50 border-amber-200 text-amber-800' :
                    'bg-gray-50 border-gray-200 text-gray-700'
                  }`}>
                    {w.message}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
