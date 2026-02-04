import { useState, useEffect } from 'react'
import Input from '../common/Input'
import Select from '../common/Select'
import Button from '../common/Button'
import type {
  AdvancedAutoGluonConfig,
  TimeSeriesAdvancedConfig,
  MultimodalAdvancedConfig,
  ModelType,
  HyperparameterTuningConfig,
  PerModelHyperparameters,
  DecisionThresholdConfig
} from '../../types/job'

interface AdvancedConfigPanelProps {
  modelType: ModelType
  advancedConfig: AdvancedAutoGluonConfig
  timeseriesConfig?: TimeSeriesAdvancedConfig
  multimodalConfig?: MultimodalAdvancedConfig
  onAdvancedConfigChange: (config: AdvancedAutoGluonConfig) => void
  onTimeseriesConfigChange?: (config: TimeSeriesAdvancedConfig) => void
  onMultimodalConfigChange?: (config: MultimodalAdvancedConfig) => void
}

const MODEL_TYPES_OPTIONS = [
  { value: 'GBM', label: 'LightGBM' },
  { value: 'CAT', label: 'CatBoost' },
  { value: 'XGB', label: 'XGBoost' },
  { value: 'RF', label: 'Random Forest' },
  { value: 'XT', label: 'Extra Trees' },
  { value: 'KNN', label: 'K-Nearest Neighbors' },
  { value: 'LR', label: 'Linear Regression' },
  { value: 'NN_TORCH', label: 'Neural Network (PyTorch)' },
  { value: 'FASTAI', label: 'Neural Network (FastAI)' },
]

const CHRONOS_SIZES = [
  { value: 'tiny', label: 'Tiny (8M params)' },
  { value: 'mini', label: 'Mini (20M params)' },
  { value: 'small', label: 'Small (46M params)' },
  { value: 'base', label: 'Base (200M params)' },
  { value: 'large', label: 'Large (710M params)' },
]

const HPO_SCHEDULERS = [
  { value: 'local', label: 'Local (single machine)' },
  { value: 'ray', label: 'Ray (distributed)' },
]

const HPO_SEARCHERS = [
  { value: 'auto', label: 'Auto (recommended)' },
  { value: 'random', label: 'Random Search' },
  { value: 'bayes', label: 'Bayesian Optimization' },
  { value: 'grid', label: 'Grid Search' },
]

const THRESHOLD_METRICS = [
  { value: 'balanced_accuracy', label: 'Balanced Accuracy (default)' },
  { value: 'f1', label: 'F1 Score' },
  { value: 'precision', label: 'Precision' },
  { value: 'recall', label: 'Recall' },
  { value: 'mcc', label: 'Matthews Correlation Coefficient' },
]

export function AdvancedConfigPanel({
  modelType,
  advancedConfig,
  timeseriesConfig,
  multimodalConfig,
  onAdvancedConfigChange,
  onTimeseriesConfigChange,
  onMultimodalConfigChange,
}: AdvancedConfigPanelProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [activeSection, setActiveSection] = useState<'resources' | 'models' | 'training' | 'hpo' | 'threshold' | 'imbalance' | 'foundation' | 'advanced' | 'specific'>('resources')

  // Notify parent frame about modal open/close
  useEffect(() => {
    if (isOpen) {
      window.parent.postMessage({ type: 'domino-modal-open' }, '*')
      return () => {
        window.parent.postMessage({ type: 'domino-modal-close' }, '*')
      }
    }
  }, [isOpen])

  // Nested config updaters
  const updateHpoConfig = (key: keyof HyperparameterTuningConfig, value: unknown) => {
    const current = advancedConfig.hpo_config || { enabled: false }
    onAdvancedConfigChange({
      ...advancedConfig,
      hpo_config: { ...current, [key]: value }
    })
  }

  const updateThresholdConfig = (key: keyof DecisionThresholdConfig, value: unknown) => {
    const current = advancedConfig.threshold_config || { enabled: false }
    onAdvancedConfigChange({
      ...advancedConfig,
      threshold_config: { ...current, [key]: value }
    })
  }

  const updatePerModelHp = (model: keyof PerModelHyperparameters, params: Record<string, unknown> | undefined) => {
    const current = advancedConfig.per_model_hyperparameters || {}
    onAdvancedConfigChange({
      ...advancedConfig,
      per_model_hyperparameters: { ...current, [model]: params }
    })
  }

  const updateAdvanced = (key: keyof AdvancedAutoGluonConfig, value: unknown) => {
    onAdvancedConfigChange({ ...advancedConfig, [key]: value })
  }

  const updateTimeseries = (key: keyof TimeSeriesAdvancedConfig, value: unknown) => {
    if (onTimeseriesConfigChange && timeseriesConfig) {
      onTimeseriesConfigChange({ ...timeseriesConfig, [key]: value })
    }
  }

  const updateMultimodal = (key: keyof MultimodalAdvancedConfig, value: unknown) => {
    if (onMultimodalConfigChange && multimodalConfig) {
      onMultimodalConfigChange({ ...multimodalConfig, [key]: value })
    }
  }

  // Count configured options for summary (model-type specific)
  const getConfiguredCount = () => {
    // Common settings (all model types)
    const commonSettings = [
      advancedConfig.num_gpus !== undefined && advancedConfig.num_gpus !== 0,
      advancedConfig.num_cpus !== undefined,
    ]

    // Tabular-specific settings
    const tabularSettings = modelType === 'tabular' ? [
      advancedConfig.excluded_model_types && advancedConfig.excluded_model_types.length > 0,
      advancedConfig.included_model_types && advancedConfig.included_model_types.length > 0,
      advancedConfig.num_bag_folds !== undefined,
      advancedConfig.num_stack_levels !== undefined,
      advancedConfig.dynamic_stacking,
      advancedConfig.holdout_frac !== undefined,
      advancedConfig.calibrate,
      advancedConfig.refit_full,
      advancedConfig.class_imbalance_strategy !== undefined,
      advancedConfig.distill,
      advancedConfig.sample_weight_column !== undefined,
      advancedConfig.hpo_config?.enabled,
      advancedConfig.threshold_config?.enabled,
      advancedConfig.use_tabular_foundation_models,
      advancedConfig.pseudo_labeling,
      advancedConfig.drop_unique,
    ] : []

    // Timeseries-specific settings
    const timeseriesSettings = modelType === 'timeseries' && timeseriesConfig ? [
      timeseriesConfig.freq !== undefined,
      timeseriesConfig.target_scaler !== undefined,
      timeseriesConfig.use_chronos,
      timeseriesConfig.enable_ensemble === false,
    ] : []

    // Multimodal-specific settings
    const multimodalSettings = modelType === 'multimodal' && multimodalConfig ? [
      multimodalConfig.text_backbone !== undefined,
      multimodalConfig.image_backbone !== undefined,
      multimodalConfig.learning_rate !== undefined,
      multimodalConfig.batch_size !== undefined,
      multimodalConfig.max_epochs !== undefined,
    ] : []

    return [...commonSettings, ...tabularSettings, ...timeseriesSettings, ...multimodalSettings].filter(Boolean).length
  }

  const configuredCount = getConfiguredCount()

  return (
    <>
      {/* Trigger Button */}
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        className="flex items-center gap-2 text-sm text-domino-accent-purple hover:text-domino-accent-purple/80 transition-colors"
      >
        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        Advanced Configuration
        {configuredCount > 0 && (
          <span className="px-1.5 py-0.5 bg-domino-accent-purple text-white text-xs rounded-full">
            {configuredCount}
          </span>
        )}
      </button>

      {/* Modal */}
      {isOpen && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="bg-white w-full max-w-4xl h-[85vh] overflow-hidden flex flex-col">
            {/* Modal Header */}
            <div className="flex items-center justify-between px-6 pt-6 pb-4">
              <h2 className="text-xl font-semibold text-domino-text-primary">Advanced Configuration</h2>
              <button
                onClick={() => setIsOpen(false)}
                className="text-domino-text-muted hover:text-domino-text-primary transition-colors"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            {/* Section Tabs */}
            <div className="flex flex-wrap gap-1 px-4 pt-4 border-b border-domino-border">
              <button
                className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                  activeSection === 'resources'
                    ? 'bg-domino-accent-purple text-white'
                    : 'text-gray-600 hover'
                }`}
                onClick={() => setActiveSection('resources')}
              >
                Resources
              </button>
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'models'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('models')}
                >
                  Models
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'training'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('training')}
                >
                  Training
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'hpo'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('hpo')}
                >
                  HPO
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'threshold'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('threshold')}
                >
                  Threshold
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'imbalance'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('imbalance')}
                >
                  Imbalance
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'foundation'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('foundation')}
                >
                  Foundation
                </button>
              )}
              {modelType === 'tabular' && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'advanced'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('advanced')}
                >
                  Advanced
                </button>
              )}
              {(modelType === 'timeseries' || modelType === 'multimodal') && (
                <button
                  className={`px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
                    activeSection === 'specific'
                      ? 'bg-domino-accent-purple text-white'
                      : 'text-gray-600 hover'
                  }`}
                  onClick={() => setActiveSection('specific')}
                >
                  {modelType === 'timeseries' ? 'Time Series' : 'Multimodal'}
                </button>
              )}
            </div>

            {/* Modal Content */}
            <div className="flex-1 overflow-y-auto p-6">
              {/* Resources Section */}
              {activeSection === 'resources' && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Number of GPUs
                    </label>
                    <Input
                      type="number"
                      min={0}
                      value={advancedConfig.num_gpus || 0}
                      onChange={(e) => updateAdvanced('num_gpus', parseInt(e.target.value) || 0)}
                    />
                    <p className="text-xs text-gray-500 mt-1">
                      Set to 0 for CPU-only training
                    </p>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Number of CPUs
                    </label>
                    <Input
                      type="number"
                      min={1}
                      value={advancedConfig.num_cpus || ''}
                      placeholder="Auto-detect"
                      onChange={(e) => updateAdvanced('num_cpus', e.target.value ? parseInt(e.target.value) : undefined)}
                    />
                    <p className="text-xs text-gray-500 mt-1">
                      Leave empty for automatic detection
                    </p>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Verbosity Level
                    </label>
                    <Select
                      value={String(advancedConfig.verbosity || 2)}
                      onChange={(e) => updateAdvanced('verbosity', parseInt(e.target.value))}
                      options={[
                        { value: '0', label: '0 - Silent' },
                        { value: '1', label: '1 - Errors only' },
                        { value: '2', label: '2 - Normal (default)' },
                        { value: '3', label: '3 - Detailed' },
                        { value: '4', label: '4 - Debug' },
                      ]}
                    />
                  </div>

                  <div className="flex items-start pt-6">
                    <label className="flex items-center space-x-2">
                      <input
                        type="checkbox"
                        checked={advancedConfig.cache_data !== false}
                        onChange={(e) => updateAdvanced('cache_data', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <span className="text-sm font-medium text-gray-700">
                        Cache data in memory
                      </span>
                    </label>
                  </div>
                </div>
              )}

              {/* Model Selection Section (Tabular only) */}
              {activeSection === 'models' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-3">
                      Excluded Model Types
                    </label>
                    <p className="text-xs text-gray-500 mb-3">
                      Click to exclude model types from training. Excluded models are highlighted in red.
                    </p>
                    <div className="flex flex-wrap gap-2">
                      {MODEL_TYPES_OPTIONS.map((model) => (
                        <label
                          key={model.value}
                          className={`px-3 py-2 rounded-lg text-sm cursor-pointer transition-colors border ${
                            advancedConfig.excluded_model_types?.includes(model.value)
                              ? 'bg-red-100 text-red-800 border-red-300'
                              : 'bg-domino-bg-tertiary hover border-domino-border'
                          }`}
                        >
                          <input
                            type="checkbox"
                            className="hidden"
                            checked={advancedConfig.excluded_model_types?.includes(model.value) || false}
                            onChange={(e) => {
                              const current = advancedConfig.excluded_model_types || []
                              if (e.target.checked) {
                                updateAdvanced('excluded_model_types', [...current, model.value])
                              } else {
                                updateAdvanced('excluded_model_types', current.filter(m => m !== model.value))
                              }
                            }}
                          />
                          {model.label}
                        </label>
                      ))}
                    </div>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Bagging Folds
                      </label>
                      <Input
                        type="number"
                        min={2}
                        max={10}
                        value={advancedConfig.num_bag_folds || ''}
                        placeholder="Auto (typically 5-8)"
                        onChange={(e) => updateAdvanced('num_bag_folds', e.target.value ? parseInt(e.target.value) : undefined)}
                      />
                      <p className="text-xs text-gray-500 mt-1">
                        Number of folds for bagging (2-10)
                      </p>
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Stack Levels
                      </label>
                      <Input
                        type="number"
                        min={0}
                        max={3}
                        value={advancedConfig.num_stack_levels ?? ''}
                        placeholder="Auto (preset-dependent)"
                        onChange={(e) => updateAdvanced('num_stack_levels', e.target.value ? parseInt(e.target.value) : undefined)}
                      />
                      <p className="text-xs text-gray-500 mt-1">
                        Number of stacking levels (0-3)
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center">
                    <label className="flex items-center space-x-2">
                      <input
                        type="checkbox"
                        checked={advancedConfig.auto_stack || false}
                        onChange={(e) => updateAdvanced('auto_stack', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <span className="text-sm font-medium text-gray-700">Auto Stack</span>
                    </label>
                    <p className="text-xs text-gray-500 ml-4">
                      Automatically determine optimal stacking configuration
                    </p>
                  </div>
                </div>
              )}

              {/* Training Section (Tabular only) */}
              {activeSection === 'training' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Holdout Fraction
                      </label>
                      <Input
                        type="number"
                        min={0.01}
                        max={0.5}
                        step={0.01}
                        value={advancedConfig.holdout_frac || ''}
                        placeholder="Auto (typically 0.1-0.2)"
                        onChange={(e) => updateAdvanced('holdout_frac', e.target.value ? parseFloat(e.target.value) : undefined)}
                      />
                      <p className="text-xs text-gray-500 mt-1">
                        Fraction of data reserved for validation (0.01-0.5)
                      </p>
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Inference Time Limit (s/row)
                      </label>
                      <Input
                        type="number"
                        min={0.001}
                        step={0.001}
                        value={advancedConfig.infer_limit || ''}
                        placeholder="No limit"
                        onChange={(e) => updateAdvanced('infer_limit', e.target.value ? parseFloat(e.target.value) : undefined)}
                      />
                      <p className="text-xs text-gray-500 mt-1">
                        Maximum inference time per row in seconds
                      </p>
                    </div>
                  </div>

                  <div className="space-y-3">
                    <label className="flex items-center space-x-3">
                      <input
                        type="checkbox"
                        checked={advancedConfig.calibrate || false}
                        onChange={(e) => updateAdvanced('calibrate', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <div>
                        <span className="text-sm font-medium text-gray-700">Calibrate Probabilities</span>
                        <p className="text-xs text-gray-500">Calibrate predicted probabilities for better reliability</p>
                      </div>
                    </label>

                    <label className="flex items-center space-x-3">
                      <input
                        type="checkbox"
                        checked={advancedConfig.refit_full || false}
                        onChange={(e) => updateAdvanced('refit_full', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <div>
                        <span className="text-sm font-medium text-gray-700">Refit on Full Data</span>
                        <p className="text-xs text-gray-500">After training, refit best models on full dataset</p>
                      </div>
                    </label>

                    <label className="flex items-center space-x-3">
                      <input
                        type="checkbox"
                        checked={advancedConfig.use_bag_holdout || false}
                        onChange={(e) => updateAdvanced('use_bag_holdout', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <div>
                        <span className="text-sm font-medium text-gray-700">Use Bag Holdout</span>
                        <p className="text-xs text-gray-500">Use separate holdout for bagged models</p>
                      </div>
                    </label>
                  </div>
                </div>
              )}

              {/* HPO Section */}
              {activeSection === 'hpo' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="p-4 bg-purple-50 rounded-lg">
                    <h4 className="font-medium text-purple-900 mb-2">Hyperparameter Optimization (HPO)</h4>
                    <p className="text-sm text-purple-700">
                      Automatically search for optimal hyperparameters for each model type. This can significantly improve model performance but increases training time.
                    </p>
                  </div>

                  <label className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      checked={advancedConfig.hpo_config?.enabled || false}
                      onChange={(e) => updateHpoConfig('enabled', e.target.checked)}
                      className="rounded border-gray-300"
                    />
                    <div>
                      <span className="text-sm font-medium text-gray-700">Enable HPO</span>
                      <p className="text-xs text-gray-500">Search for optimal hyperparameters during training</p>
                    </div>
                  </label>

                  {advancedConfig.hpo_config?.enabled && (
                    <div className="space-y-6 border-l-4 border-purple-200 pl-4">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            HPO Scheduler
                          </label>
                          <Select
                            value={advancedConfig.hpo_config?.scheduler || 'local'}
                            onChange={(e) => updateHpoConfig('scheduler', e.target.value)}
                            options={HPO_SCHEDULERS}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Use Ray for distributed HPO across multiple workers
                          </p>
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Search Algorithm
                          </label>
                          <Select
                            value={advancedConfig.hpo_config?.searcher || 'auto'}
                            onChange={(e) => updateHpoConfig('searcher', e.target.value)}
                            options={HPO_SEARCHERS}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Bayesian optimization is typically most efficient
                          </p>
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Number of Trials
                          </label>
                          <Input
                            type="number"
                            min={1}
                            max={100}
                            value={advancedConfig.hpo_config?.num_trials || 10}
                            onChange={(e) => updateHpoConfig('num_trials', parseInt(e.target.value) || 10)}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            More trials = better results but longer training (1-100)
                          </p>
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Max Iterations per Trial
                          </label>
                          <Input
                            type="number"
                            min={1}
                            value={advancedConfig.hpo_config?.max_t || ''}
                            placeholder="Auto"
                            onChange={(e) => updateHpoConfig('max_t', e.target.value ? parseInt(e.target.value) : undefined)}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Maximum training iterations for each trial
                          </p>
                        </div>
                      </div>

                      <div className="border-t pt-4">
                        <h5 className="text-sm font-medium text-gray-700 mb-3">Early Stopping (ASHA)</h5>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                          <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                              Grace Period
                            </label>
                            <Input
                              type="number"
                              min={1}
                              value={advancedConfig.hpo_config?.grace_period || ''}
                              placeholder="Auto"
                              onChange={(e) => updateHpoConfig('grace_period', e.target.value ? parseInt(e.target.value) : undefined)}
                            />
                            <p className="text-xs text-gray-500 mt-1">
                              Minimum iterations before early stopping can occur
                            </p>
                          </div>

                          <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                              Reduction Factor
                            </label>
                            <Input
                              type="number"
                              min={1}
                              step={0.5}
                              value={advancedConfig.hpo_config?.reduction_factor || ''}
                              placeholder="Auto (typically 3)"
                              onChange={(e) => updateHpoConfig('reduction_factor', e.target.value ? parseFloat(e.target.value) : undefined)}
                            />
                            <p className="text-xs text-gray-500 mt-1">
                              Factor by which to reduce number of trials at each rung
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}

                  {/* Per-Model Hyperparameters */}
                  <div className="border rounded-lg p-4">
                    <h4 className="font-medium mb-3">Per-Model Hyperparameters</h4>
                    <p className="text-xs text-gray-500 mb-4">
                      Override default hyperparameters for specific model types (JSON format)
                    </p>

                    <div className="space-y-4">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          LightGBM
                        </label>
                        <Input
                          type="text"
                          value={advancedConfig.per_model_hyperparameters?.lightgbm ? JSON.stringify(advancedConfig.per_model_hyperparameters.lightgbm) : ''}
                          placeholder='{"num_leaves": 31, "learning_rate": 0.05}'
                          onChange={(e) => {
                            try {
                              updatePerModelHp('lightgbm', e.target.value ? JSON.parse(e.target.value) : undefined)
                            } catch { /* ignore parse errors */ }
                          }}
                        />
                      </div>

                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          XGBoost
                        </label>
                        <Input
                          type="text"
                          value={advancedConfig.per_model_hyperparameters?.xgboost ? JSON.stringify(advancedConfig.per_model_hyperparameters.xgboost) : ''}
                          placeholder='{"max_depth": 6, "eta": 0.3}'
                          onChange={(e) => {
                            try {
                              updatePerModelHp('xgboost', e.target.value ? JSON.parse(e.target.value) : undefined)
                            } catch { /* ignore parse errors */ }
                          }}
                        />
                      </div>

                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          CatBoost
                        </label>
                        <Input
                          type="text"
                          value={advancedConfig.per_model_hyperparameters?.catboost ? JSON.stringify(advancedConfig.per_model_hyperparameters.catboost) : ''}
                          placeholder='{"depth": 6, "learning_rate": 0.03}'
                          onChange={(e) => {
                            try {
                              updatePerModelHp('catboost', e.target.value ? JSON.parse(e.target.value) : undefined)
                            } catch { /* ignore parse errors */ }
                          }}
                        />
                      </div>

                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          Neural Network
                        </label>
                        <Input
                          type="text"
                          value={advancedConfig.per_model_hyperparameters?.neural_network ? JSON.stringify(advancedConfig.per_model_hyperparameters.neural_network) : ''}
                          placeholder='{"num_epochs": 50, "learning_rate": 0.001}'
                          onChange={(e) => {
                            try {
                              updatePerModelHp('neural_network', e.target.value ? JSON.parse(e.target.value) : undefined)
                            } catch { /* ignore parse errors */ }
                          }}
                        />
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {/* Threshold Calibration Section */}
              {activeSection === 'threshold' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="p-4 bg-green-50 rounded-lg">
                    <h4 className="font-medium text-green-900 mb-2">Decision Threshold Calibration</h4>
                    <p className="text-sm text-green-700">
                      For binary classification, optimize the decision threshold to maximize a specific metric instead of using the default 0.5 threshold.
                    </p>
                  </div>

                  <label className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      checked={advancedConfig.threshold_config?.enabled || false}
                      onChange={(e) => updateThresholdConfig('enabled', e.target.checked)}
                      className="rounded border-gray-300"
                    />
                    <div>
                      <span className="text-sm font-medium text-gray-700">Enable Threshold Calibration</span>
                      <p className="text-xs text-gray-500">Find optimal decision threshold for binary classification</p>
                    </div>
                  </label>

                  {advancedConfig.threshold_config?.enabled && (
                    <div className="space-y-6 border-l-4 border-green-200 pl-4">
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Optimization Metric
                          </label>
                          <Select
                            value={advancedConfig.threshold_config?.metric || 'balanced_accuracy'}
                            onChange={(e) => updateThresholdConfig('metric', e.target.value)}
                            options={THRESHOLD_METRICS}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Metric to optimize when finding the best threshold
                          </p>
                        </div>

                        <div>
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Thresholds to Try
                          </label>
                          <Input
                            type="number"
                            min={10}
                            max={1000}
                            value={advancedConfig.threshold_config?.thresholds_to_try || 100}
                            onChange={(e) => updateThresholdConfig('thresholds_to_try', parseInt(e.target.value) || 100)}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Number of threshold values to evaluate (10-1000)
                          </p>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Foundation Models Section */}
              {activeSection === 'foundation' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="p-4 bg-indigo-50 rounded-lg">
                    <h4 className="font-medium text-indigo-900 mb-2">Foundation Models (2025)</h4>
                    <p className="text-sm text-indigo-700">
                      Use state-of-the-art tabular foundation models like TabPFN for zero-shot or few-shot learning on your data.
                    </p>
                  </div>

                  <label className="flex items-center space-x-3">
                    <input
                      type="checkbox"
                      checked={advancedConfig.use_tabular_foundation_models || false}
                      onChange={(e) => updateAdvanced('use_tabular_foundation_models', e.target.checked)}
                      className="rounded border-gray-300"
                    />
                    <div>
                      <span className="text-sm font-medium text-gray-700">Use Tabular Foundation Models</span>
                      <p className="text-xs text-gray-500">Include TabPFN and other foundation models in training</p>
                    </div>
                  </label>

                  {advancedConfig.use_tabular_foundation_models && (
                    <div className="border-l-4 border-indigo-200 pl-4">
                      <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                          Foundation Model Preset
                        </label>
                        <Select
                          value={advancedConfig.foundation_model_preset || ''}
                          onChange={(e) => updateAdvanced('foundation_model_preset', e.target.value || undefined)}
                          options={[
                            { value: '', label: 'None (use with other models)' },
                            { value: 'zeroshot', label: 'Zero-shot - No training, instant predictions' },
                            { value: 'zeroshot_hpo', label: 'Zero-shot + HPO - Optimize foundation model params' },
                          ]}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                          Zero-shot mode provides instant predictions without training
                        </p>
                      </div>
                    </div>
                  )}

                  <div className="border-t pt-6">
                    <h4 className="font-medium mb-4">Additional Options</h4>

                    <div className="space-y-4">
                      <label className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={advancedConfig.dynamic_stacking || false}
                          onChange={(e) => updateAdvanced('dynamic_stacking', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <div>
                          <span className="text-sm font-medium text-gray-700">Dynamic Stacking</span>
                          <p className="text-xs text-gray-500">Use dynamic stacking for adaptive ensemble configurations</p>
                        </div>
                      </label>

                      <label className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={advancedConfig.pseudo_labeling || false}
                          onChange={(e) => updateAdvanced('pseudo_labeling', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <div>
                          <span className="text-sm font-medium text-gray-700">Pseudo-Labeling</span>
                          <p className="text-xs text-gray-500">Enable semi-supervised learning with unlabeled data</p>
                        </div>
                      </label>

                      {advancedConfig.pseudo_labeling && (
                        <div className="ml-6">
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Unlabeled Data Path
                          </label>
                          <Input
                            type="text"
                            value={advancedConfig.unlabeled_data_path || ''}
                            placeholder="/path/to/unlabeled_data.csv"
                            onChange={(e) => updateAdvanced('unlabeled_data_path', e.target.value || undefined)}
                          />
                        </div>
                      )}

                      <label className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={advancedConfig.drop_unique || false}
                          onChange={(e) => updateAdvanced('drop_unique', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <div>
                          <span className="text-sm font-medium text-gray-700">Drop Unique Features</span>
                          <p className="text-xs text-gray-500">Automatically drop high-cardinality unique features (like IDs)</p>
                        </div>
                      </label>
                    </div>
                  </div>
                </div>
              )}

              {/* Class Imbalance Section */}
              {activeSection === 'imbalance' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-medium text-blue-900 mb-2">Class Imbalance Handling</h4>
                    <p className="text-sm text-blue-700">
                      Configure strategies to handle imbalanced datasets where one class is significantly more common than others.
                    </p>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Imbalance Strategy
                    </label>
                    <Select
                      value={advancedConfig.class_imbalance_strategy || ''}
                      onChange={(e) => updateAdvanced('class_imbalance_strategy', e.target.value || undefined)}
                      options={[
                        { value: '', label: 'None (default)' },
                        { value: 'oversample', label: 'Oversample - Duplicate minority class samples' },
                        { value: 'undersample', label: 'Undersample - Reduce majority class samples' },
                        { value: 'smote', label: 'SMOTE - Synthetic minority oversampling' },
                        { value: 'focal_loss', label: 'Focal Loss - Down-weight easy examples' },
                      ]}
                    />
                    <p className="text-xs text-gray-500 mt-1">
                      Select a strategy to handle class imbalance in your dataset
                    </p>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Sample Weight Column
                    </label>
                    <Input
                      type="text"
                      value={advancedConfig.sample_weight_column || ''}
                      placeholder="Column name (optional)"
                      onChange={(e) => updateAdvanced('sample_weight_column', e.target.value || undefined)}
                    />
                    <p className="text-xs text-gray-500 mt-1">
                      Name of a column in your data containing sample weights for weighted training
                    </p>
                  </div>
                </div>
              )}

              {/* Advanced Section (Tabular only) */}
              {activeSection === 'advanced' && modelType === 'tabular' && (
                <div className="space-y-6">
                  <div className="p-4 bg-amber-50 rounded-lg">
                    <h4 className="font-medium text-amber-900 mb-2">Expert Options</h4>
                    <p className="text-sm text-amber-700">
                      These advanced options are for experienced users. Modifying them may significantly impact training behavior.
                    </p>
                  </div>

                  {/* Knowledge Distillation */}
                  <div className="border rounded-lg p-4">
                    <h4 className="font-medium mb-3">Knowledge Distillation</h4>
                    <p className="text-xs text-gray-500 mb-4">
                      Transfer knowledge from the ensemble to a single faster model for deployment
                    </p>

                    <div className="space-y-4">
                      <label className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={advancedConfig.distill || false}
                          onChange={(e) => updateAdvanced('distill', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <div>
                          <span className="text-sm font-medium text-gray-700">Enable Distillation</span>
                          <p className="text-xs text-gray-500">Create a faster student model from the ensemble</p>
                        </div>
                      </label>

                      {advancedConfig.distill && (
                        <div className="ml-6">
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Distillation Time Limit (seconds)
                          </label>
                          <Input
                            type="number"
                            min={60}
                            value={advancedConfig.distill_time_limit || ''}
                            placeholder="Auto (based on training time)"
                            onChange={(e) => updateAdvanced('distill_time_limit', e.target.value ? parseInt(e.target.value) : undefined)}
                          />
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Include Model Types */}
                  <div className="border rounded-lg p-4">
                    <h4 className="font-medium mb-3">Include Only Specific Models</h4>
                    <p className="text-xs text-gray-500 mb-4">
                      Whitelist specific model types to include (overrides excluded models)
                    </p>
                    <div className="flex flex-wrap gap-2">
                      {MODEL_TYPES_OPTIONS.map((model) => (
                        <label
                          key={model.value}
                          className={`px-3 py-2 rounded-lg text-sm cursor-pointer transition-colors border ${
                            advancedConfig.included_model_types?.includes(model.value)
                              ? 'bg-green-100 text-green-800 border-green-300'
                              : 'bg-domino-bg-tertiary hover border-domino-border'
                          }`}
                        >
                          <input
                            type="checkbox"
                            className="hidden"
                            checked={advancedConfig.included_model_types?.includes(model.value) || false}
                            onChange={(e) => {
                              const current = advancedConfig.included_model_types || []
                              if (e.target.checked) {
                                updateAdvanced('included_model_types', [...current, model.value])
                              } else {
                                updateAdvanced('included_model_types', current.filter(m => m !== model.value))
                              }
                            }}
                          />
                          {model.label}
                        </label>
                      ))}
                    </div>
                    <p className="text-xs text-gray-500 mt-2">
                      If any models are selected, only those will be trained (green = included)
                    </p>
                  </div>

                  {/* Ensemble Configuration */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Bagging Sets
                      </label>
                      <Input
                        type="number"
                        min={1}
                        max={20}
                        value={advancedConfig.num_bag_sets || ''}
                        placeholder="Auto"
                        onChange={(e) => updateAdvanced('num_bag_sets', e.target.value ? parseInt(e.target.value) : undefined)}
                      />
                      <p className="text-xs text-gray-500 mt-1">
                        Number of complete bagging sets (increases diversity)
                      </p>
                    </div>

                    <div className="flex items-center pt-6">
                      <label className="flex items-center space-x-3">
                        <input
                          type="checkbox"
                          checked={advancedConfig.set_best_to_refit_full || false}
                          onChange={(e) => updateAdvanced('set_best_to_refit_full', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <div>
                          <span className="text-sm font-medium text-gray-700">Use Refit as Best</span>
                          <p className="text-xs text-gray-500">Use refitted model as final predictor</p>
                        </div>
                      </label>
                    </div>
                  </div>
                </div>
              )}

              {/* Time Series Specific */}
              {activeSection === 'specific' && modelType === 'timeseries' && timeseriesConfig && (
                <div className="space-y-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Frequency
                      </label>
                      <Select
                        value={timeseriesConfig.freq || ''}
                        onChange={(e) => updateTimeseries('freq', e.target.value || undefined)}
                        options={[
                          { value: '', label: 'Auto-detect' },
                          { value: 'D', label: 'Daily' },
                          { value: 'W', label: 'Weekly' },
                          { value: 'M', label: 'Monthly' },
                          { value: 'H', label: 'Hourly' },
                          { value: 'T', label: 'Minutely' },
                          { value: 'Q', label: 'Quarterly' },
                          { value: 'Y', label: 'Yearly' },
                        ]}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Target Scaler
                      </label>
                      <Select
                        value={timeseriesConfig.target_scaler || ''}
                        onChange={(e) => updateTimeseries('target_scaler', e.target.value || undefined)}
                        options={[
                          { value: '', label: 'Default' },
                          { value: 'mean_abs', label: 'Mean Absolute' },
                          { value: 'standard', label: 'Standard' },
                          { value: 'min_max', label: 'Min-Max' },
                          { value: 'identity', label: 'No Scaling' },
                        ]}
                      />
                    </div>
                  </div>

                  <div className="border-t pt-6">
                    <h4 className="font-medium mb-4">Chronos Foundation Model</h4>
                    <div className="space-y-4">
                      <label className="flex items-center space-x-2">
                        <input
                          type="checkbox"
                          checked={timeseriesConfig.use_chronos || false}
                          onChange={(e) => updateTimeseries('use_chronos', e.target.checked)}
                          className="rounded border-gray-300"
                        />
                        <span className="text-sm font-medium text-gray-700">Use Chronos</span>
                      </label>

                      {timeseriesConfig.use_chronos && (
                        <div className="ml-6">
                          <label className="block text-sm font-medium text-gray-700 mb-1">
                            Model Size
                          </label>
                          <Select
                            value={timeseriesConfig.chronos_model_size || 'tiny'}
                            onChange={(e) => updateTimeseries('chronos_model_size', e.target.value)}
                            options={CHRONOS_SIZES}
                          />
                          <p className="text-xs text-gray-500 mt-1">
                            Larger models are more accurate but require more memory
                          </p>
                        </div>
                      )}
                    </div>
                  </div>

                  <div>
                    <label className="flex items-center space-x-2">
                      <input
                        type="checkbox"
                        checked={timeseriesConfig.enable_ensemble !== false}
                        onChange={(e) => updateTimeseries('enable_ensemble', e.target.checked)}
                        className="rounded border-gray-300"
                      />
                      <span className="text-sm font-medium text-gray-700">Enable Ensemble</span>
                    </label>
                  </div>
                </div>
              )}

              {/* Multimodal Specific */}
              {activeSection === 'specific' && modelType === 'multimodal' && multimodalConfig && (
                <div className="space-y-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Text Backbone
                      </label>
                      <Input
                        type="text"
                        value={multimodalConfig.text_backbone || ''}
                        placeholder="e.g., google/electra-base-discriminator"
                        onChange={(e) => updateMultimodal('text_backbone', e.target.value || undefined)}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Image Backbone
                      </label>
                      <Input
                        type="text"
                        value={multimodalConfig.image_backbone || ''}
                        placeholder="e.g., swin_base_patch4_window7_224"
                        onChange={(e) => updateMultimodal('image_backbone', e.target.value || undefined)}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Max Text Length
                      </label>
                      <Input
                        type="number"
                        min={32}
                        max={2048}
                        value={multimodalConfig.text_max_length || 512}
                        onChange={(e) => updateMultimodal('text_max_length', parseInt(e.target.value))}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Image Size
                      </label>
                      <Input
                        type="number"
                        min={32}
                        max={512}
                        value={multimodalConfig.image_size || 224}
                        onChange={(e) => updateMultimodal('image_size', parseInt(e.target.value))}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Batch Size
                      </label>
                      <Input
                        type="number"
                        min={1}
                        max={128}
                        value={multimodalConfig.batch_size || ''}
                        placeholder="Auto"
                        onChange={(e) => updateMultimodal('batch_size', e.target.value ? parseInt(e.target.value) : undefined)}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Max Epochs
                      </label>
                      <Input
                        type="number"
                        min={1}
                        max={1000}
                        value={multimodalConfig.max_epochs || ''}
                        placeholder="Auto"
                        onChange={(e) => updateMultimodal('max_epochs', e.target.value ? parseInt(e.target.value) : undefined)}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Learning Rate
                      </label>
                      <Input
                        type="number"
                        step="0.0001"
                        value={multimodalConfig.learning_rate || ''}
                        placeholder="Auto"
                        onChange={(e) => updateMultimodal('learning_rate', e.target.value ? parseFloat(e.target.value) : undefined)}
                      />
                    </div>

                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">
                        Fusion Method
                      </label>
                      <Select
                        value={multimodalConfig.fusion_method || 'late'}
                        onChange={(e) => updateMultimodal('fusion_method', e.target.value as 'late' | 'early')}
                        options={[
                          { value: 'late', label: 'Late Fusion' },
                          { value: 'early', label: 'Early Fusion' },
                        ]}
                      />
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Modal Footer */}
            <div className="flex justify-end items-center gap-3 px-6 py-4 border-t border-domino-border">
              <button onClick={() => setIsOpen(false)} className="text-sm text-domino-accent-purple hover:underline">
                Cancel
              </button>
              <Button variant="primary" onClick={() => setIsOpen(false)}>
                Apply Configuration
              </Button>
            </div>
          </div>
        </div>
      )}
    </>
  )
}
