import { useRef, useState, useCallback } from 'react'
import type { TimeSeriesProfile } from '../../types/profiling'
import { getTooltipStyle } from '../../hooks/useSVGHover'

interface ACFPanelProps {
  profile: TimeSeriesProfile
}

function ACFBarChart({
  title,
  values,
  confidenceInterval,
  fullWidth,
}: {
  title: string
  values: number[]
  confidenceInterval: number
  fullWidth?: boolean
}) {
  const svgRef = useRef<SVGSVGElement>(null)
  const [hoverBar, setHoverBar] = useState<number | null>(null)

  if (!values || values.length < 2) return null

  const width = 800
  const height = 140
  const pad = { top: 10, right: 10, bottom: 25, left: 50 }
  const plotW = width - pad.left - pad.right
  const plotH = height - pad.top - pad.bottom

  // Skip lag 0 for display (it's always 1.0 for ACF)
  const displayValues = values.slice(1)
  const barWidth = Math.max(2, Math.min(12, plotW / displayValues.length - 2))
  const maxAbs = Math.max(1.0, ...displayValues.map(Math.abs))
  const slotW = plotW / displayValues.length

  const zeroY = pad.top + plotH / 2

  const getBarX = (i: number) => pad.left + i * slotW + (slotW - barWidth) / 2

  const onMouseMove = useCallback((e: React.MouseEvent<SVGSVGElement>) => {
    const svg = svgRef.current
    if (!svg) return
    const rect = svg.getBoundingClientRect()
    const svgX = ((e.clientX - rect.left) / rect.width) * width
    const idx = Math.floor((svgX - pad.left) / slotW)
    if (idx < 0 || idx >= displayValues.length) { setHoverBar(null); return }
    setHoverBar(idx)
  }, [displayValues.length, slotW, width])

  const onMouseLeave = useCallback(() => setHoverBar(null), [])

  const tooltipX = hoverBar !== null ? getBarX(hoverBar) + barWidth / 2 : 0

  return (
    <div>
      <h3 className="text-sm font-medium text-domino-text-primary mb-2">{title}</h3>
      <div className="relative">
        <svg
          ref={svgRef}
          viewBox={`0 0 ${width} ${height}`}
          className={`w-full border border-domino-border bg-white ${fullWidth ? '' : 'max-w-3xl mx-auto'}`}
          onMouseMove={onMouseMove}
          onMouseLeave={onMouseLeave}
        >
          {/* Zero line */}
          <line x1={pad.left} y1={zeroY} x2={width - pad.right} y2={zeroY} stroke="#374151" strokeWidth="1" />

          {/* Confidence interval bands */}
          <rect
            x={pad.left}
            y={zeroY - (confidenceInterval / maxAbs) * (plotH / 2)}
            width={plotW}
            height={(confidenceInterval / maxAbs) * plotH}
            fill="#dbeafe"
            opacity="0.5"
          />
          <line
            x1={pad.left}
            y1={zeroY - (confidenceInterval / maxAbs) * (plotH / 2)}
            x2={width - pad.right}
            y2={zeroY - (confidenceInterval / maxAbs) * (plotH / 2)}
            stroke="#93c5fd"
            strokeDasharray="4 2"
          />
          <line
            x1={pad.left}
            y1={zeroY + (confidenceInterval / maxAbs) * (plotH / 2)}
            x2={width - pad.right}
            y2={zeroY + (confidenceInterval / maxAbs) * (plotH / 2)}
            stroke="#93c5fd"
            strokeDasharray="4 2"
          />

          {/* Bars */}
          {displayValues.map((v, i) => {
            const x = getBarX(i)
            const barH = Math.abs(v / maxAbs) * (plotH / 2)
            const y = v >= 0 ? zeroY - barH : zeroY
            const isSignificant = Math.abs(v) > confidenceInterval
            const isHovered = hoverBar === i

            return (
              <rect
                key={i}
                x={x}
                y={y}
                width={barWidth}
                height={barH}
                fill={isSignificant ? '#7c3aed' : '#c4b5fd'}
                stroke={isHovered ? '#374151' : 'none'}
                strokeWidth={isHovered ? 1.5 : 0}
                rx="1"
              />
            )
          })}

          {/* Y-axis labels */}
          {[-1, -0.5, 0, 0.5, 1].filter(v => Math.abs(v) <= maxAbs).map((tick) => {
            const y = zeroY - (tick / maxAbs) * (plotH / 2)
            return (
              <text key={tick} x={pad.left - 5} y={y + 4} textAnchor="end" className="text-[10px] fill-gray-500">
                {tick.toFixed(1)}
              </text>
            )
          })}

          {/* X-axis labels (every 5th) */}
          {displayValues.map((_, i) => {
            if ((i + 1) % 5 !== 0) return null
            const x = pad.left + i * slotW + slotW / 2
            return (
              <text key={i} x={x} y={height - 5} textAnchor="middle" className="text-[10px] fill-gray-500">
                {i + 1}
              </text>
            )
          })}

          {/* X-axis label */}
          <text x={width / 2} y={height - 1} textAnchor="middle" className="text-[10px] fill-gray-400">
            Lag
          </text>
        </svg>
        {hoverBar !== null && (
          <div
            className="absolute top-2 pointer-events-none bg-white border border-gray-200 shadow-sm px-2 py-1.5 text-xs whitespace-nowrap z-10"
            style={getTooltipStyle(tooltipX, width)}
          >
            <div className="font-medium text-gray-700">Lag {hoverBar + 1}: {displayValues[hoverBar].toFixed(4)}</div>
            <div className="text-gray-500">
              {Math.abs(displayValues[hoverBar]) > confidenceInterval ? 'Significant' : 'Not significant'}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export function ACFPanel({ profile }: ACFPanelProps) {
  const { autocorrelation, seasonality } = profile

  if (!autocorrelation) {
    return (
      <div className="text-center py-20 text-domino-text-muted">
        Insufficient data for autocorrelation analysis (need at least 20 observations)
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-6">
        <div className="flex-1 min-w-[420px]">
          <ACFBarChart
            title="Autocorrelation Function (ACF)"
            values={autocorrelation.acf}
            confidenceInterval={autocorrelation.confidence_interval}
            fullWidth
          />
        </div>
        <div className="flex-1 min-w-[420px]">
          <ACFBarChart
            title="Partial Autocorrelation Function (PACF)"
            values={autocorrelation.pacf}
            confidenceInterval={autocorrelation.confidence_interval}
            fullWidth
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Seasonality Summary */}
        {seasonality && (
          <div className="border border-domino-border p-4">
            <h3 className="text-sm font-medium text-domino-text-primary mb-3">Seasonality Summary</h3>
            <div className="space-y-2">
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Model</span>
                <span className="text-sm font-medium text-domino-text-primary capitalize">{seasonality.model}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Period</span>
                <span className="text-sm font-medium text-domino-text-primary">{seasonality.period}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-domino-text-secondary">Seasonal Strength</span>
                <span className="text-sm font-medium text-domino-text-primary">
                  {(seasonality.seasonal_strength * 100).toFixed(1)}%
                </span>
              </div>
              <div className="mt-2 w-full bg-gray-200 h-2 rounded-full">
                <div
                  className="bg-domino-accent-purple h-2 rounded-full"
                  style={{ width: `${Math.min(100, seasonality.seasonal_strength * 100)}%` }}
                />
              </div>
            </div>
          </div>
        )}

        {/* Significant Lags */}
        <div className="border border-domino-border p-4">
          <h3 className="text-sm font-medium text-domino-text-primary mb-3">Significant Lags</h3>
          {autocorrelation.significant_lags.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              {autocorrelation.significant_lags.map((lag) => (
                <span key={lag} className="inline-block px-2 py-1 bg-domino-accent-purple/10 text-domino-accent-purple text-xs font-medium rounded-[2px]">
                  Lag {lag} ({autocorrelation.acf[lag]?.toFixed(3)})
                </span>
              ))}
            </div>
          ) : (
            <p className="text-sm text-domino-text-muted">No significant autocorrelation detected</p>
          )}
          <p className="text-xs text-domino-text-muted mt-3">
            Bars exceeding the blue dashed lines (95% CI = \u00B1{autocorrelation.confidence_interval.toFixed(3)}) are statistically significant
          </p>
        </div>
      </div>
    </div>
  )
}
