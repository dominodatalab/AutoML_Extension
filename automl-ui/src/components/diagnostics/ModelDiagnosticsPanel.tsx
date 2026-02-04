import { useState, useEffect, useMemo, useRef } from 'react'
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
  LineChart,
  Line,
  ScatterChart,
  Scatter,
  ReferenceLine
} from 'recharts'
import { useDiagnostics } from '../../hooks/useDiagnostics'
import type { ConfusionMatrixResult, ROCCurveResult } from '../../types/diagnostics'
import { Card } from '../common/Card'
import Button from '../common/Button'
import Spinner from '../common/Spinner'
import { FeatureImportanceChart } from './FeatureImportanceChart'
import type { Job } from '../../types/job'

interface ModelDiagnosticsPanelProps {
  job: Job
}

type DiagnosticTab = 'importance' | 'leaderboard' | 'classification' | 'regression'

export function ModelDiagnosticsPanel({ job }: ModelDiagnosticsPanelProps) {
  const {
    featureImportance,
    confusionMatrix,
    rocCurve,
    regressionDiagnostics,
    leaderboard,
    loading,
    error,
    reset,
    getFeatureImportance,
    getConfusionMatrix,
    getROCCurve,
    getRegressionDiagnostics,
    getLeaderboard,
  } = useDiagnostics()

  const [activeTab, setActiveTab] = useState<DiagnosticTab>('importance')

  const jobId = job.id
  const modelType = job.model_type
  const problemType = job.problem_type

  // Track which job we last fetched for to avoid duplicate fetches
  const lastFetchedRef = useRef<{ jobId: string; tab: string } | null>(null)

  // Determine which tabs to show based on problem type
  const tabs: { key: DiagnosticTab; label: string }[] = [
    { key: 'importance', label: 'Feature Importance' },
    { key: 'leaderboard', label: 'Model Comparison' },
  ]

  if (problemType === 'binary' || problemType === 'multiclass') {
    tabs.push({ key: 'classification', label: 'Classification Metrics' })
  }
  if (problemType === 'regression') {
    tabs.push({ key: 'regression', label: 'Regression Diagnostics' })
  }

  // Single effect to handle reset and fetch
  useEffect(() => {
    const needsFetch = !lastFetchedRef.current ||
      lastFetchedRef.current.jobId !== jobId ||
      lastFetchedRef.current.tab !== activeTab

    if (needsFetch) {
      // Reset data first if job changed
      if (!lastFetchedRef.current || lastFetchedRef.current.jobId !== jobId) {
        reset()
      }

      // Fetch data for current tab
      if (activeTab === 'importance') {
        getFeatureImportance(jobId, modelType)
      } else if (activeTab === 'leaderboard') {
        getLeaderboard(jobId, modelType)
      } else if (activeTab === 'classification') {
        getConfusionMatrix(jobId, modelType)
        if (problemType === 'binary') {
          getROCCurve(jobId, modelType)
        }
      } else if (activeTab === 'regression') {
        getRegressionDiagnostics(jobId, modelType)
      }

      lastFetchedRef.current = { jobId, tab: activeTab }
    }
  }, [activeTab, jobId, modelType, problemType, reset, getFeatureImportance, getLeaderboard, getConfusionMatrix, getROCCurve, getRegressionDiagnostics])

  if (job.status !== 'completed') {
    return (
      <Card>
        <div className="text-center py-8 text-gray-500">
          Model diagnostics will be available after training completes
        </div>
      </Card>
    )
  }

  return (
    <div className="space-y-4">
      {/* Tab Navigation */}
      <div className="flex space-x-2 border-b border-gray-200 pb-2">
        {tabs.map((tab) => (
          <Button
            key={tab.key}
            variant={activeTab === tab.key ? 'primary' : 'ghost'}
            size="sm"
            onClick={() => setActiveTab(tab.key)}
          >
            {tab.label}
          </Button>
        ))}
      </div>

      {error && (
        <div className="p-3 bg-red-50 border border-red-200 rounded text-red-700">
          {error}
        </div>
      )}

      {/* Tab Content */}
      {activeTab === 'importance' && (
        <FeatureImportanceChart
          data={featureImportance}
          loading={loading}
          error={error}
        />
      )}

      {activeTab === 'leaderboard' && (
        <LeaderboardView data={leaderboard} loading={loading} />
      )}

      {activeTab === 'classification' && (
        <ClassificationMetrics
          confusionMatrix={confusionMatrix}
          rocCurve={rocCurve}
          loading={loading}
          isBinary={problemType === 'binary'}
        />
      )}

      {activeTab === 'regression' && (
        <RegressionMetrics data={regressionDiagnostics} loading={loading} />
      )}
    </div>
  )
}

// Safe number conversion helper
function safeNumber(value: unknown): number {
  if (typeof value === 'number' && !isNaN(value)) return value
  if (typeof value === 'string') {
    const num = parseFloat(value)
    if (!isNaN(num)) return num
  }
  return 0
}

interface LeaderboardViewProps {
  data: {
    models: Array<{
      model: string
      score_val: number
      pred_time_val?: number
      fit_time?: number
      stack_level?: number
    }>
    best_model?: string
    eval_metric?: string
  } | null
  loading: boolean
}

function LeaderboardView({ data, loading }: LeaderboardViewProps) {
  // Prepare chart data
  const chartData = useMemo(() => {
    if (!data?.models) return []
    return data.models.slice(0, 10).map((m, index) => ({
      model: m.model.length > 15 ? m.model.substring(0, 12) + '...' : m.model,
      fullName: m.model,
      score: safeNumber(m.score_val),
      isBest: index === 0
    }))
  }, [data])

  if (loading) {
    return (
      <Card>
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
        </div>
      </Card>
    )
  }

  if (!data || !data.models || data.models.length === 0) {
    return (
      <Card>
        <div className="text-center py-8 text-domino-text-muted">
          No model comparison data available
        </div>
      </Card>
    )
  }

  return (
    <div className="space-y-4">
      {/* Score Comparison Chart */}
      <Card>
        <h3 className="text-lg font-semibold mb-4 text-domino-text-primary">Model Comparison</h3>
        <div style={{ height: Math.max(250, chartData.length * 28) }}>
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
                dataKey="model"
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
                formatter={(value: number, _name: string, props: { payload?: { fullName?: string } }) => [
                  value.toFixed(4),
                  props.payload?.fullName || 'Score'
                ]}
              />
              <Bar dataKey="score" radius={[0, 4, 4, 0]}>
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
        {data.eval_metric && (
          <p className="text-sm text-domino-text-muted text-center mt-2">
            Metric: {data.eval_metric}
          </p>
        )}
      </Card>

    </div>
  )
}

interface ClassificationMetricsProps {
  confusionMatrix: (ConfusionMatrixResult & {
    curve_data?: Array<{ fpr: number; tpr: number }>
  }) | null
  rocCurve: (ROCCurveResult & {
    curve_data?: Array<{ fpr: number; tpr: number }>
  }) | null
  loading: boolean
  isBinary: boolean
}

function ClassificationMetrics({ confusionMatrix, rocCurve, loading, isBinary }: ClassificationMetricsProps) {
  // Prepare ROC curve data for recharts
  const rocChartData = useMemo(() => {
    if (rocCurve?.curve_data) return rocCurve.curve_data
    if (rocCurve?.fpr && rocCurve?.tpr) {
      return rocCurve.fpr.map((fpr, i) => ({
        fpr,
        tpr: rocCurve.tpr![i]
      }))
    }
    return []
  }, [rocCurve])

  // Find max value in confusion matrix for color scaling
  const maxValue = useMemo(() => {
    if (!confusionMatrix?.matrix) return 1
    return Math.max(...confusionMatrix.matrix.flat())
  }, [confusionMatrix])

  if (loading) {
    return (
      <Card>
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
        </div>
      </Card>
    )
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
      {/* Confusion Matrix */}
      <Card>
        <h3 className="text-lg font-semibold mb-4 text-domino-text-primary">Confusion Matrix</h3>
        {confusionMatrix?.matrix ? (
          <div className="overflow-x-auto">
            <table className="min-w-full">
              <thead>
                <tr>
                  <th className="px-3 py-2 text-domino-text-secondary"></th>
                  {confusionMatrix.labels.map(label => (
                    <th key={label} className="px-3 py-2 text-xs font-medium text-domino-text-secondary text-center">
                      Pred: {label}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {confusionMatrix.matrix.map((row, i) => (
                  <tr key={i}>
                    <td className="px-3 py-2 text-xs font-medium text-domino-text-secondary whitespace-nowrap">
                      True: {confusionMatrix.labels[i]}
                    </td>
                    {row.map((cell, j) => {
                      const intensity = cell / maxValue
                      // Domino colors: purple (#543FDE) for diagonal, red (#C20A29) for off-diagonal
                      const bgColor = i === j
                        ? `rgba(84, 63, 222, ${0.15 + intensity * 0.5})`  // Domino purple for diagonal
                        : `rgba(194, 10, 41, ${intensity * 0.4})`  // Domino red for off-diagonal
                      return (
                        <td
                          key={j}
                          className="px-3 py-2 text-center text-sm"
                          style={{ backgroundColor: bgColor }}
                        >
                          <span className="text-domino-text-primary font-semibold">{cell}</span>
                        </td>
                      )
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <p className="text-domino-text-muted">No confusion matrix available</p>
        )}

        {/* Metrics */}
        {confusionMatrix?.metrics && (
          <div className="mt-4 grid grid-cols-2 gap-2">
            {typeof confusionMatrix.metrics.accuracy === 'number' && (
              <div className="bg-domino-bg-tertiary p-3 rounded">
                <div className="text-xs text-domino-text-secondary">Accuracy</div>
                <div className="font-bold text-domino-text-primary">{safeNumber(confusionMatrix.metrics.accuracy).toFixed(4)}</div>
              </div>
            )}
            {confusionMatrix.metrics.weighted_avg && (
              <>
                <div className="bg-domino-bg-tertiary p-3 rounded">
                  <div className="text-xs text-domino-text-secondary">Precision (Weighted)</div>
                  <div className="font-bold text-domino-text-primary">
                    {safeNumber(confusionMatrix.metrics.weighted_avg.precision).toFixed(4)}
                  </div>
                </div>
                <div className="bg-domino-bg-tertiary p-3 rounded">
                  <div className="text-xs text-domino-text-secondary">Recall (Weighted)</div>
                  <div className="font-bold text-domino-text-primary">
                    {safeNumber(confusionMatrix.metrics.weighted_avg.recall).toFixed(4)}
                  </div>
                </div>
                <div className="bg-domino-bg-tertiary p-3 rounded">
                  <div className="text-xs text-domino-text-secondary">F1 (Weighted)</div>
                  <div className="font-bold text-domino-text-primary">
                    {safeNumber(confusionMatrix.metrics.weighted_avg['f1-score']).toFixed(4)}
                  </div>
                </div>
              </>
            )}
          </div>
        )}
      </Card>

      {/* ROC Curve (for binary classification) */}
      {isBinary && (
        <Card>
          <h3 className="text-lg font-semibold mb-4 text-domino-text-primary">ROC Curve</h3>
          {rocChartData.length > 0 ? (
            <div>
              <div style={{ height: 300 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart
                    data={rocChartData}
                    margin={{ top: 5, right: 30, left: 20, bottom: 30 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                    <XAxis
                      dataKey="fpr"
                      type="number"
                      domain={[0, 1]}
                      tick={{ fill: '#9CA3AF', fontSize: 11 }}
                      label={{ value: 'False Positive Rate', position: 'bottom', fill: '#9CA3AF', fontSize: 12 }}
                    />
                    <YAxis
                      dataKey="tpr"
                      type="number"
                      domain={[0, 1]}
                      tick={{ fill: '#9CA3AF', fontSize: 11 }}
                      label={{ value: 'True Positive Rate', angle: -90, position: 'insideLeft', fill: '#9CA3AF', fontSize: 12 }}
                    />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: '#1F2937',
                        border: '1px solid #374151',
                        borderRadius: '8px',
                        color: '#F9FAFB'
                      }}
                      formatter={(value: number) => value.toFixed(4)}
                    />
                    {/* Diagonal reference line */}
                    <ReferenceLine
                      segment={[{ x: 0, y: 0 }, { x: 1, y: 1 }]}
                      stroke="#6B7280"
                      strokeDasharray="5 5"
                    />
                    <Line
                      type="monotone"
                      dataKey="tpr"
                      stroke="#6366F1"
                      strokeWidth={2}
                      dot={false}
                      fill="url(#colorAuc)"
                    />
                  </LineChart>
                </ResponsiveContainer>
              </div>
              {rocCurve?.auc !== undefined && (
                <div className="mt-4 text-sm">
                  <span className="text-domino-text-secondary">AUC Score:</span>{' '}
                  <span className="text-domino-text-primary">{safeNumber(rocCurve.auc).toFixed(4)}</span>
                </div>
              )}
            </div>
          ) : (
            <p className="text-domino-text-muted">No ROC curve data available</p>
          )}
        </Card>
      )}
    </div>
  )
}

interface RegressionMetricsProps {
  data: {
    metrics: Record<string, number | undefined>
    scatter_data?: Array<{ actual: number; predicted: number }>
    residuals_data?: Array<{ predicted: number; residual: number }>
    histogram_data?: Array<{ bin: number; count: number }>
  } | null
  loading: boolean
}

function RegressionMetrics({ data, loading }: RegressionMetricsProps) {
  if (loading) {
    return (
      <Card>
        <div className="flex items-center justify-center py-12">
          <Spinner size="lg" />
        </div>
      </Card>
    )
  }

  if (!data) {
    return (
      <Card>
        <div className="text-center py-8 text-domino-text-muted">
          No regression diagnostics available
        </div>
      </Card>
    )
  }

  // Get min/max for reference line in scatter plot
  const minVal = data.metrics?.min_actual ?? 0
  const maxVal = data.metrics?.max_actual ?? 1

  return (
    <div className="space-y-4">
      {/* Metrics */}
      <Card>
        <h3 className="text-lg font-semibold mb-4 text-domino-text-primary">Regression Metrics</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {['r2', 'rmse', 'mae', 'mse'].map((key) => {
            const value = data.metrics[key]
            if (value === undefined) return null
            return (
              <div key={key} className="bg-domino-bg-tertiary p-3 rounded text-center">
                <div className="text-xs text-domino-text-secondary uppercase">{key}</div>
                <div className="text-xl font-bold text-domino-text-primary">{safeNumber(value).toFixed(4)}</div>
              </div>
            )
          })}
        </div>
      </Card>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Predicted vs Actual Scatter Plot */}
        {data.scatter_data && data.scatter_data.length > 0 && (
          <Card>
            <h4 className="font-semibold mb-2 text-domino-text-primary">Predicted vs Actual</h4>
            <div style={{ height: 300 }}>
              <ResponsiveContainer width="100%" height="100%">
                <ScatterChart margin={{ top: 20, right: 20, bottom: 30, left: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                  <XAxis
                    type="number"
                    dataKey="actual"
                    name="Actual"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    label={{ value: 'Actual', position: 'bottom', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <YAxis
                    type="number"
                    dataKey="predicted"
                    name="Predicted"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    label={{ value: 'Predicted', angle: -90, position: 'insideLeft', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#1F2937',
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }}
                    formatter={(value: number) => value.toFixed(4)}
                  />
                  {/* Perfect prediction line */}
                  <ReferenceLine
                    segment={[{ x: minVal, y: minVal }, { x: maxVal, y: maxVal }]}
                    stroke="#EF4444"
                    strokeDasharray="5 5"
                  />
                  <Scatter data={data.scatter_data} fill="#6366F1" fillOpacity={0.6} />
                </ScatterChart>
              </ResponsiveContainer>
            </div>
          </Card>
        )}

        {/* Residuals Scatter Plot */}
        {data.residuals_data && data.residuals_data.length > 0 && (
          <Card>
            <h4 className="font-semibold mb-2 text-domino-text-primary">Residuals vs Predicted</h4>
            <div style={{ height: 300 }}>
              <ResponsiveContainer width="100%" height="100%">
                <ScatterChart margin={{ top: 20, right: 20, bottom: 30, left: 20 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                  <XAxis
                    type="number"
                    dataKey="predicted"
                    name="Predicted"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    label={{ value: 'Predicted', position: 'bottom', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <YAxis
                    type="number"
                    dataKey="residual"
                    name="Residual"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    label={{ value: 'Residual', angle: -90, position: 'insideLeft', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#1F2937',
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }}
                    formatter={(value: number) => value.toFixed(4)}
                  />
                  {/* Zero reference line */}
                  <ReferenceLine y={0} stroke="#EF4444" strokeDasharray="5 5" />
                  <Scatter data={data.residuals_data} fill="#6366F1" fillOpacity={0.6} />
                </ScatterChart>
              </ResponsiveContainer>
            </div>
          </Card>
        )}

        {/* Residuals Histogram */}
        {data.histogram_data && data.histogram_data.length > 0 && (
          <Card className="lg:col-span-2">
            <h4 className="font-semibold mb-2 text-domino-text-primary">Residuals Distribution</h4>
            <div style={{ height: 250 }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart
                  data={data.histogram_data}
                  margin={{ top: 20, right: 30, left: 20, bottom: 30 }}
                >
                  <CartesianGrid strokeDasharray="3 3" stroke="#374151" opacity={0.3} />
                  <XAxis
                    dataKey="bin"
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    tickFormatter={(v) => v.toFixed(2)}
                    label={{ value: 'Residual Value', position: 'bottom', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <YAxis
                    tick={{ fill: '#9CA3AF', fontSize: 11 }}
                    label={{ value: 'Frequency', angle: -90, position: 'insideLeft', fill: '#9CA3AF', fontSize: 12 }}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: '#1F2937',
                      border: '1px solid #374151',
                      borderRadius: '8px',
                      color: '#F9FAFB'
                    }}
                    formatter={(value: number) => [value, 'Count']}
                    labelFormatter={(label) => `Residual: ${Number(label).toFixed(4)}`}
                  />
                  <ReferenceLine x={0} stroke="#EF4444" strokeDasharray="5 5" />
                  <Bar dataKey="count" fill="#6366F1" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </Card>
        )}
      </div>
    </div>
  )
}
