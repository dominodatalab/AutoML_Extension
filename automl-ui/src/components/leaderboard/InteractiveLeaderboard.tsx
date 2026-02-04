import { useState } from 'react'
import {
  ChevronDownIcon,
  ChevronUpIcon,
  ChartBarIcon,
  InformationCircleIcon,
} from '@heroicons/react/24/outline'
import Dropdown from '../common/Dropdown'
import type { LeaderboardModel } from '../../types/job'

interface ExtendedLeaderboardModel extends LeaderboardModel {
  pred_time_test?: number
  fit_time_marginal?: number
  stack_level?: number
  can_infer?: boolean
  is_ensemble?: boolean
  hyperparameters?: Record<string, unknown>
}

interface InteractiveLeaderboardProps {
  leaderboard: ExtendedLeaderboardModel[]
  onModelSelect?: (modelName: string) => void
  selectedModel?: string
}

function getModelFamily(modelName: string): string {
  const name = modelName.toLowerCase()
  if (name.includes('lightgbm') || name.includes('gbm')) return 'LightGBM'
  if (name.includes('xgboost') || name.includes('xgb')) return 'XGBoost'
  if (name.includes('catboost') || name.includes('cat')) return 'CatBoost'
  if (name.includes('randomforest') || name.includes('rf_')) return 'RandomForest'
  if (name.includes('extratrees') || name.includes('xt_')) return 'ExtraTrees'
  if (name.includes('nn') || name.includes('neural') || name.includes('mlp')) return 'NeuralNet'
  if (name.includes('knn')) return 'KNN'
  if (name.includes('lr_') || name.includes('linear')) return 'Linear'
  if (name.includes('ensemble') || name.includes('weighted')) return 'Ensemble'
  return 'Other'
}

function formatTime(seconds?: number | string): string {
  if (seconds === undefined || seconds === null) return '-'
  const num = typeof seconds === 'string' ? parseFloat(seconds) : seconds
  if (isNaN(num)) return '-'
  if (num < 1) return `${(num * 1000).toFixed(1)}ms`
  if (num < 60) return `${num.toFixed(1)}s`
  return `${(num / 60).toFixed(1)}m`
}

function safeNumber(value: unknown): number {
  if (typeof value === 'number' && !isNaN(value)) return value
  if (typeof value === 'string') {
    const num = parseFloat(value)
    if (!isNaN(num)) return num
  }
  return 0
}

export function InteractiveLeaderboard({
  leaderboard,
  onModelSelect,
  selectedModel,
}: InteractiveLeaderboardProps) {
  const [expandedModel, setExpandedModel] = useState<string | null>(null)
  const [sortBy, setSortBy] = useState<'score' | 'fit_time' | 'pred_time'>('score')
  const [sortDesc, setSortDesc] = useState(true)
  const [filterFamily, setFilterFamily] = useState<string | null>(null)

  // Get unique model families
  const modelFamilies = [...new Set(leaderboard.map((m) => getModelFamily(m.model)))]

  // Sort leaderboard
  const sortedLeaderboard = [...leaderboard].sort((a, b) => {
    let aVal: number, bVal: number
    switch (sortBy) {
      case 'score':
        aVal = safeNumber(a.score_val)
        bVal = safeNumber(b.score_val)
        break
      case 'fit_time':
        aVal = safeNumber(a.fit_time)
        bVal = safeNumber(b.fit_time)
        break
      case 'pred_time':
        aVal = safeNumber(a.pred_time_val)
        bVal = safeNumber(b.pred_time_val)
        break
      default:
        aVal = safeNumber(a.score_val)
        bVal = safeNumber(b.score_val)
    }
    return sortDesc ? bVal - aVal : aVal - bVal
  })

  // Filter by family
  const filteredLeaderboard = filterFamily
    ? sortedLeaderboard.filter((m) => getModelFamily(m.model) === filterFamily)
    : sortedLeaderboard

  const toggleSort = (column: typeof sortBy) => {
    if (sortBy === column) {
      setSortDesc(!sortDesc)
    } else {
      setSortBy(column)
      setSortDesc(true)
    }
  }

  return (
    <div>
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-normal text-domino-text-primary">Model Leaderboard</h3>
        <Dropdown
          value={filterFamily || ''}
          onChange={(val) => setFilterFamily(val || null)}
          className="w-[180px]"
          options={[
            { value: '', label: 'All Models' },
            ...modelFamilies.map((family) => ({ value: family, label: family }))
          ]}
        />
      </div>

      {/* Table */}
      <div className="bg-white border border-domino-border">
        <table className="w-full">
          <thead>
            <tr className="border-b border-domino-border">
              <th className="px-4 py-3 text-left text-xs font-normal text-domino-text-secondary uppercase tracking-wide w-16">
                Rank
              </th>
              <th className="px-4 py-3 text-left text-xs font-normal text-domino-text-secondary uppercase tracking-wide">
                Model
              </th>
              <th
                className="px-4 py-3 text-right text-xs font-normal text-domino-text-secondary uppercase tracking-wide cursor-pointer hover:text-domino-text-primary"
                onClick={() => toggleSort('score')}
              >
                <span className="inline-flex items-center gap-1 justify-end">
                  Score
                  <span className="flex flex-col -space-y-1">
                    <ChevronUpIcon className={`h-3 w-3 ${sortBy === 'score' && !sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                    <ChevronDownIcon className={`h-3 w-3 ${sortBy === 'score' && sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                  </span>
                </span>
              </th>
              <th
                className="px-4 py-3 text-right text-xs font-normal text-domino-text-secondary uppercase tracking-wide cursor-pointer hover:text-domino-text-primary"
                onClick={() => toggleSort('fit_time')}
              >
                <span className="inline-flex items-center gap-1 justify-end">
                  Fit Time
                  <span className="flex flex-col -space-y-1">
                    <ChevronUpIcon className={`h-3 w-3 ${sortBy === 'fit_time' && !sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                    <ChevronDownIcon className={`h-3 w-3 ${sortBy === 'fit_time' && sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                  </span>
                </span>
              </th>
              <th
                className="px-4 py-3 text-right text-xs font-normal text-domino-text-secondary uppercase tracking-wide cursor-pointer hover:text-domino-text-primary"
                onClick={() => toggleSort('pred_time')}
              >
                <span className="inline-flex items-center gap-1 justify-end">
                  Pred Time
                  <span className="flex flex-col -space-y-1">
                    <ChevronUpIcon className={`h-3 w-3 ${sortBy === 'pred_time' && !sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                    <ChevronDownIcon className={`h-3 w-3 ${sortBy === 'pred_time' && sortDesc ? 'text-domino-accent-purple' : 'text-domino-text-muted'}`} />
                  </span>
                </span>
              </th>
              <th className="px-4 py-3 text-center text-xs font-normal text-domino-text-secondary uppercase tracking-wide w-16">
                Details
              </th>
            </tr>
          </thead>
          <tbody>
            {filteredLeaderboard.map((model, index) => {
              const isExpanded = expandedModel === model.model
              const isSelected = selectedModel === model.model
              const originalRank =
                sortBy === 'score' && sortDesc
                  ? leaderboard.findIndex((m) => m.model === model.model) + 1
                  : index + 1

              return (
                <>
                  <tr
                    key={model.model}
                    className={`border-b border-domino-border hover:bg-domino-bg-tertiary cursor-pointer transition-colors ${
                      isSelected ? 'bg-domino-accent-purple/10' : ''
                    }`}
                    onClick={() => onModelSelect?.(model.model)}
                  >
                    <td className="px-4 py-3 text-sm text-domino-text-primary">{originalRank}</td>
                    <td className="px-4 py-3 text-sm text-domino-text-primary">{model.model}</td>
                    <td className="px-4 py-3 text-right text-sm text-domino-text-primary">
                      {safeNumber(model.score_val).toFixed(4)}
                    </td>
                    <td className="px-4 py-3 text-right text-sm text-domino-text-secondary">
                      {formatTime(model.fit_time)}
                    </td>
                    <td className="px-4 py-3 text-right text-sm text-domino-text-secondary">
                      {formatTime(model.pred_time_val)}
                    </td>
                    <td className="px-4 py-3 text-center">
                      <button
                        onClick={(e) => {
                          e.stopPropagation()
                          setExpandedModel(isExpanded ? null : model.model)
                        }}
                        className="p-1 hover:bg-domino-bg-tertiary rounded text-domino-text-muted hover:text-domino-text-primary"
                      >
                        {isExpanded ? (
                          <ChevronUpIcon className="h-4 w-4" />
                        ) : (
                          <ChevronDownIcon className="h-4 w-4" />
                        )}
                      </button>
                    </td>
                  </tr>

                  {/* Expanded details row */}
                  {isExpanded && (
                    <tr key={`${model.model}-details`} className="border-b border-domino-border bg-domino-bg-tertiary">
                      <td colSpan={6} className="px-4 py-4">
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                          {/* Performance Metrics */}
                          <div className="space-y-2">
                            <h4 className="text-sm font-medium text-domino-text-primary flex items-center gap-1">
                              <ChartBarIcon className="h-4 w-4" />
                              Performance
                            </h4>
                            <dl className="space-y-1 text-sm">
                              <div className="flex justify-between">
                                <dt className="text-domino-text-secondary">Validation Score</dt>
                                <dd className="text-domino-text-primary">{safeNumber(model.score_val).toFixed(4)}</dd>
                              </div>
                              {model.pred_time_test !== undefined && (
                                <div className="flex justify-between">
                                  <dt className="text-domino-text-secondary">Test Pred Time</dt>
                                  <dd className="text-domino-text-primary">{formatTime(model.pred_time_test)}</dd>
                                </div>
                              )}
                              {model.fit_time_marginal !== undefined && (
                                <div className="flex justify-between">
                                  <dt className="text-domino-text-secondary">Marginal Fit Time</dt>
                                  <dd className="text-domino-text-primary">
                                    {formatTime(model.fit_time_marginal)}
                                  </dd>
                                </div>
                              )}
                            </dl>
                          </div>

                          {/* Model Info */}
                          <div className="space-y-2">
                            <h4 className="text-sm font-medium text-domino-text-primary flex items-center gap-1">
                              <InformationCircleIcon className="h-4 w-4" />
                              Model Info
                            </h4>
                            <dl className="space-y-1 text-sm">
                              {model.stack_level !== undefined && (
                                <div className="flex justify-between">
                                  <dt className="text-domino-text-secondary">Stack Level</dt>
                                  <dd className="text-domino-text-primary">{model.stack_level}</dd>
                                </div>
                              )}
                              {model.can_infer !== undefined && (
                                <div className="flex justify-between">
                                  <dt className="text-domino-text-secondary">Can Infer</dt>
                                  <dd className="text-domino-text-primary">{model.can_infer ? 'Yes' : 'No'}</dd>
                                </div>
                              )}
                            </dl>
                          </div>

                          {/* Hyperparameters */}
                          {model.hyperparameters && (
                            <div className="space-y-2">
                              <h4 className="text-sm font-medium text-domino-text-primary">Hyperparameters</h4>
                              <div className="bg-white border border-domino-border p-2 max-h-32 overflow-auto">
                                <pre className="text-xs text-domino-text-primary whitespace-pre-wrap">
                                  {JSON.stringify(model.hyperparameters, null, 2)}
                                </pre>
                              </div>
                            </div>
                          )}
                        </div>
                      </td>
                    </tr>
                  )}
                </>
              )
            })}
          </tbody>
        </table>
      </div>

      {/* Summary stats */}
      <div className="flex items-center justify-between mt-4 text-sm text-domino-text-secondary">
        <span>Showing 1–{filteredLeaderboard.length} out of {filteredLeaderboard.length}</span>
        <div className="flex items-center gap-4">
          <span>
            Best: <span className="text-domino-text-primary">{safeNumber(sortedLeaderboard[0]?.score_val).toFixed(4)}</span>
          </span>
          <span>
            Total Training Time:{' '}
            <span className="text-domino-text-primary">
              {formatTime(leaderboard.reduce((acc, m) => acc + safeNumber(m.fit_time), 0))}
            </span>
          </span>
        </div>
      </div>
    </div>
  )
}

export default InteractiveLeaderboard
