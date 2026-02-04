import { useState, useEffect } from 'react'
import { useProfiling } from '../../hooks/useProfiling'
import { Card } from '../common/Card'
import Spinner from '../common/Spinner'
import Badge from '../common/Badge'
import type { DataProfile, ColumnProfile, CorrelationData } from '../../types/profiling'

interface DataProfileViewProps {
  filePath: string
  onTargetSelect?: (column: string, problemType: string) => void
}

export function DataProfileView({ filePath, onTargetSelect }: DataProfileViewProps) {
  const { profile, suggestions, loading, error, profileFile, suggestTarget } = useProfiling()
  const [selectedColumn, setSelectedColumn] = useState<ColumnProfile | null>(null)
  const [activeTab, setActiveTab] = useState<'overview' | 'columns' | 'correlations' | 'issues'>('overview')

  useEffect(() => {
    if (filePath) {
      profileFile(filePath)
      suggestTarget(filePath)
    }
  }, [filePath, profileFile, suggestTarget])

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <Spinner size="lg" />
        <span className="ml-3 text-gray-600">Analyzing data...</span>
      </div>
    )
  }

  if (error) {
    return (
      <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
        <p className="text-red-700">{error}</p>
      </div>
    )
  }

  if (!profile) {
    return null
  }

  return (
    <div className="space-y-6">
      {/* Tab Navigation */}
      <div className="border-b border-gray-200">
        <nav className="flex space-x-8">
          {['overview', 'columns', 'correlations', 'issues'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab as typeof activeTab)}
              className={`py-2 px-1 border-b-2 font-medium text-sm capitalize ${
                activeTab === tab
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700'
              }`}
            >
              {tab}
              {tab === 'issues' && profile.warnings.length > 0 && (
                <Badge variant="warning" className="ml-2">{profile.warnings.length}</Badge>
              )}
            </button>
          ))}
        </nav>
      </div>

      {activeTab === 'overview' && (
        <OverviewTab profile={profile} suggestions={suggestions} onTargetSelect={onTargetSelect} />
      )}

      {activeTab === 'columns' && (
        <ColumnsTab
          columns={profile.columns}
          selectedColumn={selectedColumn}
          onSelectColumn={setSelectedColumn}
        />
      )}

      {activeTab === 'correlations' && (
        <CorrelationsTab correlations={profile.correlations} columns={profile.columns} />
      )}

      {activeTab === 'issues' && (
        <IssuesTab warnings={profile.warnings} recommendations={profile.recommendations} />
      )}
    </div>
  )
}

interface OverviewTabProps {
  profile: DataProfile
  suggestions: { column: string; score: number; reasons: string[]; problem_type: string }[]
  onTargetSelect?: (column: string, problemType: string) => void
}

function OverviewTab({ profile, suggestions, onTargetSelect }: OverviewTabProps) {
  const { summary } = profile

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {/* Dataset Summary */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">Dataset Summary</h3>
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-gray-50 p-3 rounded">
            <div className="text-2xl font-bold text-blue-600">{summary.total_rows.toLocaleString()}</div>
            <div className="text-sm text-gray-500">Total Rows</div>
          </div>
          <div className="bg-gray-50 p-3 rounded">
            <div className="text-2xl font-bold text-blue-600">{summary.total_columns}</div>
            <div className="text-sm text-gray-500">Columns</div>
          </div>
          <div className="bg-gray-50 p-3 rounded">
            <div className="text-2xl font-bold text-blue-600">{summary.memory_usage_mb.toFixed(1)} MB</div>
            <div className="text-sm text-gray-500">Memory Usage</div>
          </div>
          <div className="bg-gray-50 p-3 rounded">
            <div className="text-2xl font-bold text-orange-600">{summary.duplicate_percentage.toFixed(1)}%</div>
            <div className="text-sm text-gray-500">Duplicate Rows</div>
          </div>
        </div>
        {summary.sampled && (
          <p className="mt-4 text-sm text-gray-500">
            Profiled on sample of {summary.sample_size.toLocaleString()} rows
          </p>
        )}
      </Card>

      {/* Target Suggestions */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">Suggested Targets</h3>
        {suggestions.length === 0 ? (
          <p className="text-gray-500">No target suggestions available</p>
        ) : (
          <div className="space-y-3">
            {suggestions.slice(0, 5).map((suggestion) => (
              <div
                key={suggestion.column}
                className="p-3 bg-gray-50 rounded-lg hover:bg-blue-50 cursor-pointer transition-colors"
                onClick={() => onTargetSelect?.(suggestion.column, suggestion.problem_type)}
              >
                <div className="flex items-center justify-between">
                  <span className="font-medium">{suggestion.column}</span>
                  <div className="flex items-center space-x-2">
                    <Badge variant="info">{suggestion.problem_type}</Badge>
                    <span className="text-sm text-gray-500">Score: {suggestion.score}</span>
                  </div>
                </div>
                <ul className="mt-2 text-sm text-gray-600">
                  {suggestion.reasons.slice(0, 2).map((reason, i) => (
                    <li key={i} className="flex items-center">
                      <span className="w-1.5 h-1.5 bg-green-500 rounded-full mr-2" />
                      {reason}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        )}
      </Card>

      {/* Column Type Distribution */}
      <Card className="lg:col-span-2">
        <h3 className="text-lg font-semibold mb-4">Column Types</h3>
        <div className="flex flex-wrap gap-2">
          {Object.entries(
            profile.columns.reduce((acc, col) => {
              acc[col.semantic_type] = (acc[col.semantic_type] || 0) + 1
              return acc
            }, {} as Record<string, number>)
          ).map(([type, count]) => (
            <div key={type} className="px-3 py-2 bg-gray-100 rounded-lg">
              <span className="font-medium capitalize">{type}</span>
              <span className="ml-2 text-gray-500">({count})</span>
            </div>
          ))}
        </div>
      </Card>
    </div>
  )
}

interface ColumnsTabProps {
  columns: ColumnProfile[]
  selectedColumn: ColumnProfile | null
  onSelectColumn: (column: ColumnProfile | null) => void
}

function ColumnsTab({ columns, selectedColumn, onSelectColumn }: ColumnsTabProps) {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Column List */}
      <div className="lg:col-span-1">
        <Card>
          <h3 className="text-lg font-semibold mb-4">Columns ({columns.length})</h3>
          <div className="max-h-96 overflow-y-auto space-y-1">
            {columns.map((col) => (
              <button
                key={col.name}
                onClick={() => onSelectColumn(col)}
                className={`w-full text-left px-3 py-2 rounded transition-colors ${
                  selectedColumn?.name === col.name
                    ? 'bg-blue-100 text-blue-800'
                    : 'hover:bg-gray-100'
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="font-medium truncate">{col.name}</span>
                  <Badge variant={(col.issues?.length ?? 0) > 0 ? 'warning' : 'success'} className="text-xs">
                    {col.semantic_type}
                  </Badge>
                </div>
                <div className="text-xs text-gray-500 mt-1">
                  {col.dtype} | {col.missing_percentage.toFixed(1)}% missing
                </div>
              </button>
            ))}
          </div>
        </Card>
      </div>

      {/* Column Details */}
      <div className="lg:col-span-2">
        {selectedColumn ? (
          <ColumnDetails column={selectedColumn} />
        ) : (
          <Card>
            <div className="text-center text-gray-500 py-8">
              Select a column to view details
            </div>
          </Card>
        )}
      </div>
    </div>
  )
}

function ColumnDetails({ column }: { column: ColumnProfile }) {
  return (
    <Card>
      <h3 className="text-lg font-semibold mb-4">{column.name}</h3>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
        <div className="text-center p-3 bg-gray-50 rounded">
          <div className="text-lg font-bold">{column.dtype}</div>
          <div className="text-xs text-gray-500">Data Type</div>
        </div>
        <div className="text-center p-3 bg-gray-50 rounded">
          <div className="text-lg font-bold capitalize">{column.semantic_type}</div>
          <div className="text-xs text-gray-500">Semantic Type</div>
        </div>
        <div className="text-center p-3 bg-gray-50 rounded">
          <div className="text-lg font-bold text-orange-600">{column.missing_percentage.toFixed(1)}%</div>
          <div className="text-xs text-gray-500">Missing ({column.missing_count})</div>
        </div>
        <div className="text-center p-3 bg-gray-50 rounded">
          <div className="text-lg font-bold text-blue-600">{column.unique_count}</div>
          <div className="text-xs text-gray-500">Unique ({column.unique_percentage.toFixed(1)}%)</div>
        </div>
      </div>

      {/* Statistics */}
      {column.statistics && Object.keys(column.statistics).length > 0 && (
        <div className="mb-6">
          <h4 className="font-medium mb-2">Statistics</h4>
          <div className="grid grid-cols-4 gap-2">
            {Object.entries(column.statistics).map(([key, value]) => (
              <div key={key} className="text-sm">
                <span className="text-gray-500 capitalize">{key}:</span>{' '}
                <span className="font-medium">
                  {typeof value === 'number' ? value.toFixed(2) : String(value)}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Value Counts */}
      {column.value_counts && column.value_counts.length > 0 && (
        <div className="mb-6">
          <h4 className="font-medium mb-2">Top Values</h4>
          <div className="space-y-1">
            {column.value_counts.slice(0, 10).map((vc, i) => (
              <div key={i} className="flex items-center">
                <div className="w-32 truncate text-sm">{String(vc.value)}</div>
                <div className="flex-1 mx-2">
                  <div
                    className="h-4 bg-blue-200 rounded"
                    style={{ width: `${vc.percentage}%` }}
                  />
                </div>
                <div className="text-sm text-gray-500 w-16 text-right">
                  {vc.percentage.toFixed(1)}%
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Issues */}
      {column.issues && column.issues.length > 0 && (
        <div>
          <h4 className="font-medium mb-2 text-orange-600">Issues</h4>
          <ul className="space-y-1">
            {column.issues.map((issue, i) => (
              <li key={i} className="flex items-center text-sm text-orange-700">
                <span className="w-1.5 h-1.5 bg-orange-500 rounded-full mr-2" />
                {issue}
              </li>
            ))}
          </ul>
        </div>
      )}
    </Card>
  )
}

interface CorrelationsTabProps {
  correlations: CorrelationData | Record<string, Record<string, number>>
  columns: ColumnProfile[]
}

function CorrelationsTab({ correlations, columns }: CorrelationsTabProps) {
  // Extract the matrix from either format
  const rawMatrix = 'matrix' in correlations ? correlations.matrix : correlations
  const corrMatrix: Record<string, Record<string, number>> | undefined =
    rawMatrix && typeof rawMatrix === 'object'
      ? (rawMatrix as Record<string, Record<string, number>>)
      : undefined
  const numericColumns = columns.filter(c =>
    ['numeric', 'integer', 'float'].includes(c.semantic_type)
  ).map(c => c.name)

  if (numericColumns.length === 0) {
    return (
      <Card>
        <div className="text-center text-gray-500 py-8">
          No numeric columns available for correlation analysis
        </div>
      </Card>
    )
  }

  const getCorrelationColor = (value: number) => {
    if (Math.abs(value) > 0.7) return value > 0 ? 'bg-blue-600 text-white' : 'bg-red-600 text-white'
    if (Math.abs(value) > 0.4) return value > 0 ? 'bg-blue-300' : 'bg-red-300'
    return 'bg-gray-100'
  }

  return (
    <Card>
      <h3 className="text-lg font-semibold mb-4">Correlation Matrix</h3>
      <div className="overflow-x-auto">
        <table className="min-w-full">
          <thead>
            <tr>
              <th className="px-2 py-1" />
              {numericColumns.slice(0, 10).map(col => (
                <th key={col} className="px-2 py-1 text-xs font-medium text-gray-500 truncate max-w-20">
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {numericColumns.slice(0, 10).map(row => (
              <tr key={row}>
                <td className="px-2 py-1 text-xs font-medium text-gray-500 truncate max-w-20">{row}</td>
                {numericColumns.slice(0, 10).map(col => {
                  const value = corrMatrix?.[row]?.[col] ?? 0
                  return (
                    <td
                      key={col}
                      className={`px-2 py-1 text-center text-xs ${getCorrelationColor(value)}`}
                      title={`${row} vs ${col}: ${value.toFixed(3)}`}
                    >
                      {value.toFixed(2)}
                    </td>
                  )
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {numericColumns.length > 10 && (
        <p className="mt-2 text-sm text-gray-500">
          Showing first 10 of {numericColumns.length} numeric columns
        </p>
      )}
    </Card>
  )
}

interface IssuesTabProps {
  warnings: { type: string; message: string; severity: string }[]
  recommendations: { type: string; message: string; priority: string }[]
}

function IssuesTab({ warnings, recommendations }: IssuesTabProps) {
  return (
    <div className="space-y-6">
      {/* Warnings */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">
          Warnings ({warnings.length})
        </h3>
        {warnings.length === 0 ? (
          <p className="text-green-600">No data quality warnings found</p>
        ) : (
          <div className="space-y-2">
            {warnings.map((warning, i) => (
              <div
                key={i}
                className={`p-3 rounded-lg ${
                  warning.severity === 'error' ? 'bg-red-50 border-l-4 border-red-500' :
                  warning.severity === 'warning' ? 'bg-yellow-50 border-l-4 border-yellow-500' :
                  'bg-blue-50 border-l-4 border-blue-500'
                }`}
              >
                <div className="font-medium capitalize">{warning.type}</div>
                <div className="text-sm text-gray-600">{warning.message}</div>
              </div>
            ))}
          </div>
        )}
      </Card>

      {/* Recommendations */}
      <Card>
        <h3 className="text-lg font-semibold mb-4">
          Recommendations ({recommendations.length})
        </h3>
        {recommendations.length === 0 ? (
          <p className="text-gray-500">No recommendations at this time</p>
        ) : (
          <div className="space-y-2">
            {recommendations.map((rec, i) => (
              <div
                key={i}
                className={`p-3 rounded-lg ${
                  rec.priority === 'high' ? 'bg-purple-50 border-l-4 border-purple-500' :
                  rec.priority === 'medium' ? 'bg-blue-50 border-l-4 border-blue-500' :
                  'bg-gray-50 border-l-4 border-gray-500'
                }`}
              >
                <div className="flex items-center justify-between">
                  <div className="font-medium capitalize">{rec.type}</div>
                  <Badge variant={rec.priority === 'high' ? 'error' : 'info'}>
                    {rec.priority}
                  </Badge>
                </div>
                <div className="text-sm text-gray-600 mt-1">{rec.message}</div>
              </div>
            ))}
          </div>
        )}
      </Card>
    </div>
  )
}
