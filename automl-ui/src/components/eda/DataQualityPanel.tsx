import {
  ExclamationTriangleIcon,
  LightBulbIcon,
  CheckCircleIcon,
  ExclamationCircleIcon,
  InformationCircleIcon,
  CpuChipIcon,
  KeyIcon,
  DocumentTextIcon,
  CalendarIcon,
  CursorArrowRaysIcon,
  WrenchScrewdriverIcon,
} from '@heroicons/react/24/outline'
import type { DataWarning, DataRecommendation, ColumnProfile } from '../../types/profiling'

interface DataQualityPanelProps {
  warnings: DataWarning[]
  recommendations: DataRecommendation[]
  columns: ColumnProfile[]
}

export function DataQualityPanel({ warnings, recommendations, columns }: DataQualityPanelProps) {
  // Compute quality issues by column
  const columnIssues = columns.filter((c) => (c.issues?.length ?? 0) > 0)

  const getSeverityIcon = (severity: string) => {
    switch (severity) {
      case 'error':
        return <ExclamationCircleIcon className="h-5 w-5 text-domino-accent-red" />
      case 'warning':
        return <ExclamationTriangleIcon className="h-5 w-5 text-yellow-500" />
      default:
        return <InformationCircleIcon className="h-5 w-5 text-blue-500" />
    }
  }

  const getSeverityBg = (severity: string) => {
    switch (severity) {
      case 'error':
        return 'bg-red-50 border-red-200'
      case 'warning':
        return 'bg-yellow-50 border-yellow-200'
      default:
        return 'bg-blue-50 border-blue-200'
    }
  }

  const getPriorityBg = (priority: string) => {
    switch (priority) {
      case 'high':
        return 'bg-red-100 text-red-700'
      case 'medium':
        return 'bg-yellow-100 text-yellow-700'
      default:
        return 'bg-gray-100 text-gray-700'
    }
  }

  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'target':
        return <CursorArrowRaysIcon className="h-5 w-5 text-domino-accent-purple" />
      case 'preprocessing':
        return <WrenchScrewdriverIcon className="h-5 w-5 text-domino-accent-purple" />
      case 'model':
        return <CpuChipIcon className="h-5 w-5 text-domino-accent-purple" />
      default:
        return <LightBulbIcon className="h-5 w-5 text-domino-accent-purple" />
    }
  }

  return (
    <div className="space-y-6">
      {/* Overall Status */}
      <div className="flex items-center gap-6">
        <div className="flex items-center gap-2">
          {warnings.filter((w) => w.severity === 'error').length > 0 ? (
            <ExclamationCircleIcon className="h-8 w-8 text-domino-accent-red" />
          ) : warnings.filter((w) => w.severity === 'warning').length > 0 ? (
            <ExclamationTriangleIcon className="h-8 w-8 text-yellow-500" />
          ) : (
            <CheckCircleIcon className="h-8 w-8 text-domino-accent-green" />
          )}
          <div>
            <p className="text-lg font-medium text-domino-text-primary">
              {warnings.filter((w) => w.severity === 'error').length > 0
                ? 'Critical Issues Found'
                : warnings.filter((w) => w.severity === 'warning').length > 0
                ? 'Some Warnings'
                : 'Data Looks Good'}
            </p>
            <p className="text-sm text-domino-text-muted">
              {warnings.length} warnings, {recommendations.length} recommendations, {columnIssues.length} columns with issues
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Warnings */}
        <div className="border border-domino-border rounded">
          <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border flex items-center gap-2">
            <ExclamationTriangleIcon className="h-5 w-5 text-yellow-500" />
            <h4 className="text-sm font-medium text-domino-text-primary">Warnings</h4>
            <span className="ml-auto text-xs text-domino-text-muted">
              {warnings.length} total
            </span>
          </div>
          <div className="p-4 space-y-3 max-h-64 overflow-y-auto">
            {warnings.length === 0 ? (
              <div className="flex items-center gap-2 text-sm text-domino-text-muted">
                <CheckCircleIcon className="h-5 w-5 text-domino-accent-green" />
                No warnings detected
              </div>
            ) : (
              warnings.map((warning, idx) => (
                <div
                  key={idx}
                  className={`p-3 rounded border ${getSeverityBg(warning.severity)}`}
                >
                  <div className="flex items-start gap-2">
                    {getSeverityIcon(warning.severity)}
                    <div className="flex-1">
                      <p className="text-sm text-gray-800">{warning.message}</p>
                      <p className="text-xs text-gray-500 mt-1 capitalize">
                        {warning.type.replace(/_/g, ' ')}
                      </p>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>

        {/* Recommendations */}
        <div className="border border-domino-border rounded">
          <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border flex items-center gap-2">
            <LightBulbIcon className="h-5 w-5 text-domino-accent-purple" />
            <h4 className="text-sm font-medium text-domino-text-primary">Recommendations</h4>
            <span className="ml-auto text-xs text-domino-text-muted">
              {recommendations.length} total
            </span>
          </div>
          <div className="p-4 space-y-3 max-h-64 overflow-y-auto">
            {recommendations.length === 0 ? (
              <div className="flex items-center gap-2 text-sm text-domino-text-muted">
                <CheckCircleIcon className="h-5 w-5 text-domino-accent-green" />
                No specific recommendations
              </div>
            ) : (
              recommendations.map((rec, idx) => (
                <div
                  key={idx}
                  className="p-3 bg-domino-bg-tertiary rounded border border-domino-border"
                >
                  <div className="flex items-start gap-2">
                    {getTypeIcon(rec.type)}
                    <div className="flex-1">
                      <p className="text-sm text-domino-text-primary">{rec.message}</p>
                      <div className="flex items-center gap-2 mt-2">
                        <span className={`text-xs px-2 py-0.5 rounded ${getPriorityBg(rec.priority)}`}>
                          {rec.priority} priority
                        </span>
                        <span className="text-xs text-domino-text-muted capitalize">
                          {rec.type}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Column Issues */}
      {columnIssues.length > 0 && (
        <div className="border border-domino-border rounded">
          <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border flex items-center gap-2">
            <ExclamationCircleIcon className="h-5 w-5 text-yellow-500" />
            <h4 className="text-sm font-medium text-domino-text-primary">Column-Level Issues</h4>
            <span className="ml-auto text-xs text-domino-text-muted">
              {columnIssues.length} columns affected
            </span>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-domino-border">
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase">
                    Column
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase">
                    Type
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-domino-text-secondary uppercase">
                    Issues
                  </th>
                </tr>
              </thead>
              <tbody>
                {columnIssues.map((col) => (
                  <tr key={col.name} className="border-b border-domino-border hover:bg-domino-bg-tertiary">
                    <td className="px-4 py-3 font-medium text-domino-text-primary">
                      {col.name}
                    </td>
                    <td className="px-4 py-3 text-domino-text-secondary">
                      {col.semantic_type}
                    </td>
                    <td className="px-4 py-3">
                      <div className="space-y-1">
                        {col.issues?.map((issue, idx) => (
                          <span
                            key={idx}
                            className="inline-block px-2 py-0.5 text-xs bg-yellow-100 text-yellow-700 rounded mr-2"
                          >
                            {issue}
                          </span>
                        ))}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Quick Actions */}
      <div className="border border-domino-border rounded">
        <div className="px-4 py-3 bg-domino-bg-tertiary border-b border-domino-border">
          <h4 className="text-sm font-medium text-domino-text-primary">Suggested Actions</h4>
        </div>
        <div className="p-4 space-y-2">
          {columnIssues.some((c) => c.semantic_type === 'identifier') && (
            <div className="flex items-center gap-3 p-3 bg-blue-50 rounded border border-blue-200">
              <KeyIcon className="h-5 w-5 text-blue-600 flex-shrink-0" />
              <div className="flex-1">
                <p className="text-sm text-blue-800">
                  Identifier columns detected - these will be automatically excluded from training
                </p>
              </div>
              <span className="text-xs px-2 py-1 bg-blue-100 text-blue-700 rounded">AutoGluon handles this</span>
            </div>
          )}

          {columns.some((c) => c.missing_percentage > 30) && (
            <div className="flex items-center gap-3 p-3 bg-yellow-50 rounded border border-yellow-200">
              <ExclamationTriangleIcon className="h-5 w-5 text-yellow-600 flex-shrink-0" />
              <div className="flex-1">
                <p className="text-sm text-yellow-800">
                  High missing data in some columns - consider dropping or using advanced imputation
                </p>
              </div>
              <span className="text-xs px-2 py-1 bg-yellow-100 text-yellow-700 rounded">Review in Advanced Settings</span>
            </div>
          )}

          {columns.some((c) => c.semantic_type === 'text') && (
            <div className="flex items-center gap-3 p-3 bg-purple-50 rounded border border-purple-200">
              <DocumentTextIcon className="h-5 w-5 text-purple-600 flex-shrink-0" />
              <div className="flex-1">
                <p className="text-sm text-purple-800">
                  Text columns detected - consider using Multimodal model type for better text handling
                </p>
              </div>
              <span className="text-xs px-2 py-1 bg-purple-100 text-purple-700 rounded">Suggestion</span>
            </div>
          )}

          {columns.some((c) => c.semantic_type === 'datetime') && (
            <div className="flex items-center gap-3 p-3 bg-green-50 rounded border border-green-200">
              <CalendarIcon className="h-5 w-5 text-green-600 flex-shrink-0" />
              <div className="flex-1">
                <p className="text-sm text-green-800">
                  Datetime columns detected - consider TimeSeries model if doing forecasting
                </p>
              </div>
              <span className="text-xs px-2 py-1 bg-green-100 text-green-700 rounded">Suggestion</span>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
