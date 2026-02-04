import { useMemo } from 'react'
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts'
import { Card } from '../common/Card'
import Spinner from '../common/Spinner'
import type { FeatureImportanceResult } from '../../types/diagnostics'

// Safe number conversion helper
function safeNumber(value: unknown): number {
  if (typeof value === 'number' && !isNaN(value)) return value
  if (typeof value === 'string') {
    const num = parseFloat(value)
    if (!isNaN(num)) return num
  }
  return 0
}

interface FeatureImportanceChartProps {
  data: FeatureImportanceResult | null
  loading?: boolean
  error?: string | null
  maxFeatures?: number
}

export function FeatureImportanceChart({
  data,
  loading = false,
  error = null,
  maxFeatures = 20
}: FeatureImportanceChartProps) {
  const chartData = useMemo(() => {
    if (!data?.features) return []
    return [...data.features]
      .sort((a, b) => safeNumber(b.importance) - safeNumber(a.importance))
      .slice(0, maxFeatures)
      .map(f => ({
        feature: String(f.feature).length > 25 ? String(f.feature).substring(0, 22) + '...' : String(f.feature),
        fullName: String(f.feature),
        importance: safeNumber(f.importance),
        stddev: f.std ? safeNumber(f.std) : undefined
      }))
      .reverse() // Reverse for horizontal bar chart (highest at top)
  }, [data, maxFeatures])

  if (loading) {
    return (
      <Card>
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
        </div>
      </Card>
    )
  }

  if (error) {
    return (
      <Card>
        <div className="text-center py-8">
          <p className="text-domino-accent-red">{error}</p>
        </div>
      </Card>
    )
  }

  if (!data || chartData.length === 0) {
    return (
      <Card>
        <div className="text-center py-8 text-domino-text-muted">
          No feature importance data available
        </div>
      </Card>
    )
  }

  const chartHeight = Math.max(300, chartData.length * 28)

  return (
    <Card>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-domino-text-primary">Feature Importance</h3>
        <span className="text-sm text-domino-text-muted">Method: {data.method}</span>
      </div>

      <div style={{ height: chartHeight }}>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={chartData}
            layout="vertical"
            margin={{ top: 5, right: 30, left: 100, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
            <XAxis
              type="number"
              tick={{ fill: '#9CA3AF', fontSize: 12 }}
              tickFormatter={(value) => value.toFixed(3)}
            />
            <YAxis
              type="category"
              dataKey="feature"
              tick={{ fill: '#9CA3AF', fontSize: 11 }}
              width={95}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: '#1F2937',
                border: '1px solid #374151',
                borderRadius: '8px',
                color: '#F9FAFB'
              }}
              formatter={(value: number, _name: string, props: { payload?: { fullName?: string; stddev?: number } }) => [
                <span key="value">
                  {value.toFixed(4)}
                  {props.payload?.stddev !== undefined && (
                    <span className="text-gray-400"> ± {props.payload.stddev.toFixed(4)}</span>
                  )}
                </span>,
                props.payload?.fullName || 'Importance'
              ]}
            />
            <Bar dataKey="importance" radius={[0, 4, 4, 0]}>
              {chartData.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={entry.importance >= 0 ? '#6366F1' : '#EF4444'}
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      {data.features && data.features.length > maxFeatures && (
        <p className="mt-4 text-sm text-domino-text-muted text-center">
          Showing top {maxFeatures} of {data.features.length} features
        </p>
      )}
    </Card>
  )
}
