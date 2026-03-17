import { useState } from 'react'
import { ChartBarIcon, ArrowTrendingUpIcon, CalendarIcon, InformationCircleIcon } from '@heroicons/react/24/outline'
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card'
import Button from '../common/Button'
import Spinner from '../common/Spinner'
import { useMutation } from '@tanstack/react-query'
import api from '../../api'
import { useStore } from '../../store'
import type { Job } from '../../types/job'

interface TimeSeriesForecastPanelProps {
  job: Job
}

interface ForecastResult {
  predictions: Record<string, Array<number | null>>
  timestamps?: string[]
  quantiles?: Record<string, Array<number | null>>
  chart?: string
  error?: string
}

export function TimeSeriesForecastPanel({ job }: TimeSeriesForecastPanelProps) {
  const [predictionLength, setPredictionLength] = useState(job.prediction_length || 10)
  const [result, setResult] = useState<ForecastResult | null>(null)
  const addNotification = useStore((state) => state.addNotification)

  const forecastMutation = useMutation({
    mutationFn: async (data: { model_path: string; model_type: string; prediction_length: number }) => {
      const { data: response } = await api.post<ForecastResult>('predict', {
        model_id: data.model_path, // Backend uses model_id for the path
        model_type: data.model_type,
        prediction_length: data.prediction_length,
      })
      return response
    },
  })

  const handleForecast = async () => {
    if (!job.model_path) return

    try {
      const response = await forecastMutation.mutateAsync({
        model_path: job.model_path,
        model_type: job.model_type,
        prediction_length: predictionLength,
      })
      setResult(response)
    } catch (error) {
      console.error('Forecast failed:', error)
      addNotification(
        error instanceof Error ? error.message : 'Forecast generation failed. Please try again.',
        'error'
      )
    }
  }

  // Only show for time series jobs
  if (job.model_type !== 'timeseries') {
    return null
  }

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <ArrowTrendingUpIcon className="h-5 w-5" />
            Time Series Forecasting
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {/* Job Info */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-domino-bg-tertiary rounded-lg p-4">
                <p className="text-xs text-domino-text-muted mb-1">Target Column</p>
                <p className="font-medium">{job.target_column}</p>
              </div>
              {job.time_column && (
                <div className="bg-domino-bg-tertiary rounded-lg p-4">
                  <p className="text-xs text-domino-text-muted mb-1">Time Column</p>
                  <p className="font-medium">{job.time_column}</p>
                </div>
              )}
              {job.id_column && (
                <div className="bg-domino-bg-tertiary rounded-lg p-4">
                  <p className="text-xs text-domino-text-muted mb-1">ID Column</p>
                  <p className="font-medium">{job.id_column}</p>
                </div>
              )}
            </div>

            {/* Forecast Controls */}
            <div className="flex items-end gap-4">
              <div className="flex-1">
                <label className="block text-sm font-medium text-domino-text-secondary mb-2">
                  Prediction Horizon
                </label>
                <div className="flex items-center gap-2">
                  <input
                    type="number"
                    value={predictionLength}
                    onChange={(e) => setPredictionLength(Math.max(1, parseInt(e.target.value) || 1))}
                    min={1}
                    max={365}
                    className="w-24 px-3 py-2 text-sm bg-domino-bg-secondary border border-domino-border rounded-md focus:outline-none focus:ring-2 focus:ring-domino-accent-purple"
                  />
                  <span className="text-sm text-domino-text-secondary">time steps</span>
                </div>
              </div>

              <Button
                variant="primary"
                onClick={handleForecast}
                isLoading={forecastMutation.isPending}
                disabled={!job.model_path || forecastMutation.isPending}
              >
                <ChartBarIcon className="h-4 w-4 mr-2" />
                Generate Forecast
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Loading State */}
      {forecastMutation.isPending && (
        <Card>
          <CardContent className="py-12">
            <div className="flex flex-col items-center justify-center gap-4">
              <Spinner size="lg" />
              <p className="text-domino-text-secondary">Generating forecast...</p>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Forecast Results */}
      {result && !forecastMutation.isPending && (
        <>
          {/* Forecast Chart */}
          {result.chart && (
            <Card>
              <CardHeader>
                <CardTitle>Forecast Visualization</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex justify-center">
                  <img
                    src={result.chart}
                    alt="Time Series Forecast"
                    className="max-w-full h-auto rounded-lg"
                  />
                </div>
              </CardContent>
            </Card>
          )}

          {/* Predictions Table */}
          {result.predictions && Object.keys(result.predictions).length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <CalendarIcon className="h-5 w-5" />
                  Predicted Values
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="min-w-full">
                    <thead>
                      <tr className="bg-domino-bg-tertiary">
                        <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary">
                          Step
                        </th>
                        {result.timestamps && (
                          <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary">
                            Timestamp
                          </th>
                        )}
                        {Object.keys(result.predictions).map((key) => (
                          <th
                            key={key}
                            className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary"
                          >
                            {key}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-domino-border">
                      {Array.from(
                        { length: Math.max(...Object.values(result.predictions).map((v) => v.length)) },
                        (_, i) => (
                          <tr key={i}>
                            <td className="px-4 py-2 text-sm ">t+{i + 1}</td>
                            {result.timestamps && (
                              <td className="px-4 py-2 text-sm text-domino-text-secondary">
                                {result.timestamps[i] || '-'}
                              </td>
                            )}
                            {Object.entries(result.predictions).map(([key, values]) => (
                              <td key={key} className="px-4 py-2 text-right text-sm ">
                                {values[i] != null ? values[i].toFixed(4) : '-'}
                              </td>
                            ))}
                          </tr>
                        )
                      )}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          )}

          {/* Quantile Predictions */}
          {result.quantiles && Object.keys(result.quantiles).length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle>Prediction Intervals</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {Object.entries(result.quantiles).map(([quantile, values]) => (
                    <div key={quantile} className="bg-domino-bg-tertiary rounded-lg p-4">
                      <p className="text-sm font-medium mb-2">{quantile} Quantile</p>
                      <div className="space-y-1">
                        {values.slice(0, 5).map((value, index) => (
                          <div key={`${quantile}-${index}`} className="flex justify-between text-sm">
                            <span className="text-domino-text-muted">t+{index + 1}</span>
                            <span className="">
                              {value != null ? value.toFixed(2) : '-'}
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Error */}
          {result.error && (
            <Card>
              <CardContent className="py-4">
                <p className="text-domino-accent-red">{result.error}</p>
              </CardContent>
            </Card>
          )}
        </>
      )}

      {/* Time Series Info */}
      <Card>
        <CardContent className="py-4">
          <div className="flex items-start gap-3">
            <InformationCircleIcon className="h-5 w-5 text-domino-accent-purple flex-shrink-0 mt-0.5" />
            <div className="text-sm text-domino-text-secondary">
              <p className="font-medium text-domino-text-primary mb-1">About Time Series Forecasting</p>
              <ul className="list-disc list-inside space-y-1">
                <li>AutoGluon-TimeSeries supports multiple forecasting models</li>
                <li>Predictions include point estimates and prediction intervals</li>
                <li>The model automatically handles seasonality and trends</li>
                <li>For multi-step forecasting, each step is predicted recursively</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

export default TimeSeriesForecastPanel
