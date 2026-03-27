import { useMemo } from 'react'
import { ChartBarIcon, ClockIcon } from '@heroicons/react/24/outline'
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
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card'
import Spinner from '../common/Spinner'
import { useLearningCurves } from '../../hooks/useExport'

// Safe number conversion helper
function safeNumber(value: unknown): number {
  if (typeof value === 'number' && !isNaN(value)) return value
  if (typeof value === 'string') {
    const num = parseFloat(value)
    if (!isNaN(num)) return num
  }
  return 0
}

function resolveFitTime(model: Record<string, unknown>): number {
  return safeNumber(model.fit_time ?? model.fit_time_marginal)
}

interface LearningCurvesPanelProps {
  jobId: string
  modelType: string
}

export function LearningCurvesPanel({ jobId, modelType }: LearningCurvesPanelProps) {
  const { data, isLoading, error } = useLearningCurves(jobId, modelType)

  // Parse models data from new API format
  const modelsArray = useMemo(() => {
    if (!data) return []
    // New format returns models array directly
    if (Array.isArray(data.models)) {
      return data.models.map((m: Record<string, unknown>) => ({
        model: String(m.model || 'Unknown'),
        score_val: safeNumber(m.score_val),
        fit_time: resolveFitTime(m),
        pred_time_val: safeNumber(m.pred_time_val)
      }))
    }
    // Legacy format with training_history
    if (data.training_history) {
      const history = data.training_history as {
        models?: Record<string, { fit_time: number; score_val: number }> | Array<Record<string, unknown>>
      }
      if (Array.isArray(history.models)) {
        return history.models.map((m: Record<string, unknown>) => ({
          model: String(m.model || 'Unknown'),
          score_val: safeNumber(m.score_val),
          fit_time: resolveFitTime(m),
          pred_time_val: safeNumber(m.pred_time_val)
        }))
      }
      if (history.models) {
        return Object.entries(history.models).map(([name, info]) => ({
          model: name,
          score_val: safeNumber(info.score_val),
          fit_time: safeNumber(info.fit_time ?? (info as { fit_time_marginal?: number }).fit_time_marginal),
          pred_time_val: 0
        }))
      }
    }
    return []
  }, [data])

  // Prepare chart data (truncate model names for display)
  const chartData = useMemo(() => {
    return modelsArray.map((m, index) => ({
      ...m,
      displayName: m.model.length > 20 ? m.model.substring(0, 17) + '...' : m.model,
      isBest: index === 0
    }))
  }, [modelsArray])

  // Get fit summary from new or legacy format
  const fitSummary = useMemo(() => {
    if (!data) return null
    if (data.fit_summary_raw) return data.fit_summary_raw
    if (data.training_history) {
      const history = data.training_history as { fit_summary?: unknown }
      return history.fit_summary
    }
    return null
  }, [data])

  if (isLoading) {
    return (
      <Card>
        <CardContent className="py-12">
          <div className="flex items-center justify-center">
            <Spinner size="lg" />
          </div>
        </CardContent>
      </Card>
    )
  }

  if (error) {
    return (
      <Card>
        <CardContent className="py-8">
          <p className="text-domino-accent-red text-center">
            Error loading learning curves: {error.message}
          </p>
        </CardContent>
      </Card>
    )
  }

  if (!data || modelsArray.length === 0) {
    return (
      <Card>
        <CardContent className="py-8">
          <p className="text-domino-text-muted text-center">
            No training history available
          </p>
        </CardContent>
      </Card>
    )
  }

  const chartHeight = Math.max(250, Math.min(400, chartData.length * 30))

  return (
    <div className="space-y-6">
      {/* Training Progress Charts - Rendered with Recharts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Validation Score Chart */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <ChartBarIcon className="h-5 w-5" />
              Validation Scores
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div style={{ height: chartHeight }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={chartData}
                  layout="vertical"
                  margin={{ top: 5, right: 30, left: 80, bottom: 5 }}
                >
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                  <XAxis
                    type="number"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    tickFormatter={(v) => v.toFixed(3)}
                  />
                  <YAxis
                    type="category"
                    dataKey="displayName"
                    tick={{ fill: '#9CA3AF', fontSize: 10 }}
                    width={75}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#1F2937',
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }}
                    formatter={(value: number) => value.toFixed(4)}
                    labelFormatter={(label: string) => label}
                  />
                  <Bar dataKey="score_val" radius={[0, 4, 4, 0]}>
                    {chartData.map((entry, index) => (
                      <Cell
                        key={`cell-${index}`}
                        fill={entry.isBest ? '#10B981' : '#6366F1'}
                      />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Fit Time Chart */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <ClockIcon className="h-5 w-5" />
              Training Times
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div style={{ height: chartHeight }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={chartData}
                  layout="vertical"
                  margin={{ top: 5, right: 30, left: 80, bottom: 5 }}
                >
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                  <XAxis
                    type="number"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    tickFormatter={(v) => `${v.toFixed(1)}s`}
                  />
                  <YAxis
                    type="category"
                    dataKey="displayName"
                    tick={{ fill: '#9CA3AF', fontSize: 10 }}
                    width={75}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#1F2937',
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }}
                    formatter={(value: number) => `${value.toFixed(2)}s`}
                    labelFormatter={(label: string) => label}
                  />
                  <Bar dataKey="fit_time" fill="#F59E0B" radius={[0, 4, 4, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Training Statistics */}
      <Card>
        <CardHeader>
          <CardTitle>Training Statistics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="border border-domino-border p-4 text-center">
              <p className="text-2xl font-medium text-domino-text-primary">
                {modelsArray.length}
              </p>
              <p className="text-sm text-domino-text-secondary">Models Trained</p>
            </div>
            <div className="border border-domino-border p-4 text-center">
              <p className="text-2xl font-medium text-domino-text-primary">
                {Math.max(...modelsArray.map((m) => m.score_val)).toFixed(3)}
              </p>
              <p className="text-sm text-domino-text-secondary">Best Score</p>
            </div>
            <div className="border border-domino-border p-4 text-center">
              <p className="text-2xl font-medium text-domino-text-primary">
                {modelsArray.reduce((acc, m) => acc + m.fit_time, 0).toFixed(0)}s
              </p>
              <p className="text-sm text-domino-text-secondary">Total Train Time</p>
            </div>
            <div className="border border-domino-border p-4 text-center">
              <p className="text-2xl font-medium text-domino-text-primary">
                {(modelsArray.reduce((acc, m) => acc + m.fit_time, 0) / Math.max(modelsArray.length, 1)).toFixed(1)}s
              </p>
              <p className="text-sm text-domino-text-secondary">Avg Train Time</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Fit Summary */}
      {fitSummary !== null && fitSummary !== undefined && (
        <Card>
          <CardHeader>
            <CardTitle>Fit Summary</CardTitle>
          </CardHeader>
          <CardContent>
            <pre className="bg-domino-bg-tertiary rounded-lg p-4 text-sm  overflow-x-auto whitespace-pre-wrap text-domino-text-primary">
              {typeof fitSummary === 'object'
                ? JSON.stringify(fitSummary, null, 2)
                : String(fitSummary as string | number | boolean)}
            </pre>
          </CardContent>
        </Card>
      )}

      {/* Error */}
      {data.error && (
        <Card>
          <CardContent className="py-4">
            <p className="text-domino-accent-red">{data.error}</p>
          </CardContent>
        </Card>
      )}
    </div>
  )
}

export default LearningCurvesPanel
