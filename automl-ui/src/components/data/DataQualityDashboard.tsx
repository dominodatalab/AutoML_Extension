import { useState, useEffect } from 'react'
import {
  ExclamationTriangleIcon,
  CheckCircleIcon,
  InformationCircleIcon,
  ChartBarIcon,
  TableCellsIcon,
  ExclamationCircleIcon,
} from '@heroicons/react/24/outline'
import { Card, CardHeader, CardTitle, CardContent } from '../common/Card'
import Spinner from '../common/Spinner'

interface ColumnProfile {
  name: string
  dtype: string
  missing_count: number
  missing_pct: number
  unique_count: number
  unique_pct: number
  mean?: number
  std?: number
  min?: number
  max?: number
  mode?: string
  is_target_candidate?: boolean
  sample_values?: unknown[]
}

interface DataQualityProfile {
  row_count: number
  column_count: number
  memory_usage_mb: number
  duplicate_rows: number
  columns: ColumnProfile[]
  target_candidates: string[]
  data_quality_score: number
  warnings: string[]
  recommendations: string[]
}

interface DataQualityDashboardProps {
  filePath: string
  onProfileLoaded?: (profile: DataQualityProfile) => void
  onTargetSuggestion?: (column: string) => void
}

export function DataQualityDashboard({
  filePath,
  onProfileLoaded,
  onTargetSuggestion,
}: DataQualityDashboardProps) {
  const [profile, setProfile] = useState<DataQualityProfile | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [selectedColumn, setSelectedColumn] = useState<string | null>(null)

  useEffect(() => {
    if (filePath) {
      loadProfile()
    }
  }, [filePath])

  const loadProfile = async () => {
    setLoading(true)
    setError(null)
    try {
      // Get quick profile from backend
      const response = await fetch('/svcprofilequick', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_path: filePath }),
      })
      if (!response.ok) throw new Error('Failed to load profile')
      const data = await response.json()

      // Transform to our format
      const profileData: DataQualityProfile = {
        row_count: data.row_count || 0,
        column_count: data.column_count || 0,
        memory_usage_mb: data.memory_usage_mb || 0,
        duplicate_rows: data.duplicate_rows || 0,
        columns: data.columns || [],
        target_candidates: data.target_candidates || [],
        data_quality_score: calculateQualityScore(data),
        warnings: extractWarnings(data),
        recommendations: extractRecommendations(data),
      }

      setProfile(profileData)
      onProfileLoaded?.(profileData)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Failed to load profile')
    } finally {
      setLoading(false)
    }
  }

  const calculateQualityScore = (data: any): number => {
    if (!data.columns?.length) return 0

    const totalColumns = data.columns.length
    let score = 100

    // Penalize for missing values
    const avgMissingPct =
      data.columns.reduce((acc: number, col: ColumnProfile) => acc + (col.missing_pct || 0), 0) /
      totalColumns
    score -= avgMissingPct * 0.5

    // Penalize for duplicate rows
    if (data.duplicate_rows > 0) {
      const dupPct = (data.duplicate_rows / data.row_count) * 100
      score -= dupPct * 0.3
    }

    // Penalize for very high cardinality features
    const highCardinalityCount = data.columns.filter(
      (col: ColumnProfile) => col.unique_pct > 90 && col.dtype === 'object'
    ).length
    score -= highCardinalityCount * 2

    return Math.max(0, Math.min(100, Math.round(score)))
  }

  const extractWarnings = (data: any): string[] => {
    const warnings: string[] = []

    if (!data.columns) return warnings

    data.columns.forEach((col: ColumnProfile) => {
      if (col.missing_pct > 50) {
        warnings.push(`Column "${col.name}" has ${col.missing_pct.toFixed(1)}% missing values`)
      }
      if (col.unique_pct > 95 && col.dtype === 'object') {
        warnings.push(`Column "${col.name}" may be an ID column (${col.unique_pct.toFixed(1)}% unique)`)
      }
    })

    if (data.duplicate_rows > 0) {
      warnings.push(`Dataset contains ${data.duplicate_rows} duplicate rows`)
    }

    return warnings
  }

  const extractRecommendations = (data: any): string[] => {
    const recommendations: string[] = []

    if (!data.columns) return recommendations

    const highMissingCols = data.columns.filter((col: ColumnProfile) => col.missing_pct > 30)
    if (highMissingCols.length > 0) {
      recommendations.push(
        `Consider dropping or imputing columns with high missing values: ${highMissingCols
          .slice(0, 3)
          .map((c: ColumnProfile) => c.name)
          .join(', ')}`
      )
    }

    const idCols = data.columns.filter(
      (col: ColumnProfile) => col.unique_pct > 95 && col.dtype === 'object'
    )
    if (idCols.length > 0) {
      recommendations.push(
        `Consider excluding ID-like columns from features: ${idCols
          .slice(0, 3)
          .map((c: ColumnProfile) => c.name)
          .join(', ')}`
      )
    }

    return recommendations
  }

  const getQualityColor = (score: number): string => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  const getMissingColor = (pct: number): string => {
    if (pct === 0) return 'bg-green-100 text-green-800'
    if (pct < 10) return 'bg-yellow-100 text-yellow-800'
    return 'bg-red-100 text-red-800'
  }

  if (loading) {
    return (
      <Card>
        <CardContent className="flex items-center justify-center py-8">
          <Spinner />
          <span className="ml-2">Analyzing data quality...</span>
        </CardContent>
      </Card>
    )
  }

  if (error) {
    return (
      <Card>
        <CardContent className="text-center py-8 text-domino-accent-red">
          <ExclamationCircleIcon className="h-8 w-8 mx-auto mb-2" />
          {error}
        </CardContent>
      </Card>
    )
  }

  if (!profile) {
    return null
  }

  const selectedColumnData = selectedColumn
    ? profile.columns.find((c) => c.name === selectedColumn)
    : null

  return (
    <div className="space-y-4">
      {/* Summary Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="py-4 text-center">
            <div className={`text-3xl font-bold ${getQualityColor(profile.data_quality_score)}`}>
              {profile.data_quality_score}%
            </div>
            <div className="text-sm text-domino-text-secondary">Quality Score</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="py-4 text-center">
            <div className="text-3xl font-bold text-domino-text-primary">
              {profile.row_count.toLocaleString()}
            </div>
            <div className="text-sm text-domino-text-secondary">Rows</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="py-4 text-center">
            <div className="text-3xl font-bold text-domino-text-primary">
              {profile.column_count}
            </div>
            <div className="text-sm text-domino-text-secondary">Columns</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="py-4 text-center">
            <div className="text-3xl font-bold text-domino-text-primary">
              {profile.memory_usage_mb.toFixed(1)} MB
            </div>
            <div className="text-sm text-domino-text-secondary">Memory</div>
          </CardContent>
        </Card>
      </div>

      {/* Warnings and Recommendations */}
      {(profile.warnings.length > 0 || profile.recommendations.length > 0) && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {profile.warnings.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-yellow-600">
                  <ExclamationTriangleIcon className="h-5 w-5" />
                  Warnings
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  {profile.warnings.map((warning, idx) => (
                    <li key={idx} className="text-sm flex items-start gap-2">
                      <ExclamationTriangleIcon className="h-4 w-4 text-yellow-500 flex-shrink-0 mt-0.5" />
                      {warning}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )}

          {profile.recommendations.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-blue-600">
                  <InformationCircleIcon className="h-5 w-5" />
                  Recommendations
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2">
                  {profile.recommendations.map((rec, idx) => (
                    <li key={idx} className="text-sm flex items-start gap-2">
                      <CheckCircleIcon className="h-4 w-4 text-blue-500 flex-shrink-0 mt-0.5" />
                      {rec}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          )}
        </div>
      )}

      {/* Target Candidates */}
      {profile.target_candidates.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <ChartBarIcon className="h-5 w-5" />
              Suggested Target Columns
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-2">
              {profile.target_candidates.map((col) => (
                <button
                  key={col}
                  onClick={() => onTargetSuggestion?.(col)}
                  className="px-3 py-1.5 bg-domino-accent-purple/10 text-domino-accent-purple rounded-lg text-sm hover:bg-domino-accent-purple/20 transition-colors"
                >
                  {col}
                </button>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Column Details */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <TableCellsIcon className="h-5 w-5" />
            Column Analysis
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <table className="min-w-full">
              <thead>
                <tr className="bg-domino-bg-tertiary">
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary">
                    Column
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary">
                    Type
                  </th>
                  <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary">
                    Missing
                  </th>
                  <th className="px-4 py-2 text-right text-xs font-medium text-domino-text-secondary">
                    Unique
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary">
                    Stats
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-domino-border">
                {profile.columns.slice(0, 20).map((col) => (
                  <tr
                    key={col.name}
                    className={`hover:bg-domino-bg-secondary cursor-pointer ${
                      selectedColumn === col.name ? 'bg-domino-bg-secondary' : ''
                    }`}
                    onClick={() => setSelectedColumn(col.name === selectedColumn ? null : col.name)}
                  >
                    <td className="px-4 py-2 text-sm font-medium">{col.name}</td>
                    <td className="px-4 py-2">
                      <span className="px-2 py-0.5 bg-gray-100 text-gray-700 rounded text-xs">
                        {col.dtype}
                      </span>
                    </td>
                    <td className="px-4 py-2 text-right">
                      <span
                        className={`px-2 py-0.5 rounded text-xs ${getMissingColor(col.missing_pct)}`}
                      >
                        {col.missing_pct.toFixed(1)}%
                      </span>
                    </td>
                    <td className="px-4 py-2 text-right text-sm">
                      {col.unique_count.toLocaleString()} ({col.unique_pct.toFixed(1)}%)
                    </td>
                    <td className="px-4 py-2 text-sm text-domino-text-secondary">
                      {col.dtype.includes('float') || col.dtype.includes('int') ? (
                        <span>
                          μ={col.mean?.toFixed(2)}, σ={col.std?.toFixed(2)}
                        </span>
                      ) : (
                        <span>mode: {col.mode || '-'}</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          {profile.columns.length > 20 && (
            <p className="text-sm text-domino-text-muted text-center mt-2">
              Showing first 20 of {profile.columns.length} columns
            </p>
          )}
        </CardContent>
      </Card>

      {/* Selected Column Detail */}
      {selectedColumnData && (
        <Card>
          <CardHeader>
            <CardTitle>Column: {selectedColumnData.name}</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div>
                <div className="text-sm text-domino-text-secondary">Data Type</div>
                <div className="font-medium">{selectedColumnData.dtype}</div>
              </div>
              <div>
                <div className="text-sm text-domino-text-secondary">Missing Values</div>
                <div className="font-medium">
                  {selectedColumnData.missing_count.toLocaleString()} (
                  {selectedColumnData.missing_pct.toFixed(1)}%)
                </div>
              </div>
              <div>
                <div className="text-sm text-domino-text-secondary">Unique Values</div>
                <div className="font-medium">
                  {selectedColumnData.unique_count.toLocaleString()}
                </div>
              </div>
              {selectedColumnData.mean !== undefined && (
                <div>
                  <div className="text-sm text-domino-text-secondary">Mean</div>
                  <div className="font-medium ">{selectedColumnData.mean.toFixed(4)}</div>
                </div>
              )}
              {selectedColumnData.std !== undefined && (
                <div>
                  <div className="text-sm text-domino-text-secondary">Std Dev</div>
                  <div className="font-medium ">{selectedColumnData.std.toFixed(4)}</div>
                </div>
              )}
              {selectedColumnData.min !== undefined && (
                <div>
                  <div className="text-sm text-domino-text-secondary">Min</div>
                  <div className="font-medium ">{selectedColumnData.min}</div>
                </div>
              )}
              {selectedColumnData.max !== undefined && (
                <div>
                  <div className="text-sm text-domino-text-secondary">Max</div>
                  <div className="font-medium ">{selectedColumnData.max}</div>
                </div>
              )}
              {selectedColumnData.mode && (
                <div>
                  <div className="text-sm text-domino-text-secondary">Mode</div>
                  <div className="font-medium">{selectedColumnData.mode}</div>
                </div>
              )}
            </div>

            {selectedColumnData.sample_values && selectedColumnData.sample_values.length > 0 && (
              <div className="mt-4">
                <div className="text-sm text-domino-text-secondary mb-2">Sample Values</div>
                <div className="flex flex-wrap gap-2">
                  {selectedColumnData.sample_values.slice(0, 10).map((val, idx) => (
                    <span
                      key={idx}
                      className="px-2 py-1 bg-domino-bg-tertiary rounded text-sm "
                    >
                      {String(val)}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  )
}

export default DataQualityDashboard
