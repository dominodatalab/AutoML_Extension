export type JobStatus = 'pending' | 'running' | 'completed' | 'failed' | 'cancelled'
export type ModelType = 'tabular' | 'timeseries' | 'multimodal'
export type ProblemType = 'binary' | 'multiclass' | 'regression' | 'quantile'
export type ExecutionTarget = 'local' | 'domino_job'
export type Preset =
  | 'best_quality'
  | 'high_quality'
  | 'good_quality'
  | 'medium_quality_faster_train'
  | 'optimize_for_deployment'
  | 'chronos'
  | 'fast_training'
  // 2025 Foundation model presets
  | 'zeroshot'
  | 'zeroshot_hpo'
  | 'experimental_tabfm'

// Hyperparameter Tuning (HPO) Configuration
export interface HyperparameterTuningConfig {
  enabled: boolean
  scheduler?: 'local' | 'ray'
  searcher?: 'auto' | 'random' | 'bayes' | 'grid'
  num_trials?: number
  max_t?: number
  grace_period?: number
  reduction_factor?: number
}

// Per-model hyperparameter overrides
export interface PerModelHyperparameters {
  lightgbm?: Record<string, unknown>
  catboost?: Record<string, unknown>
  xgboost?: Record<string, unknown>
  random_forest?: Record<string, unknown>
  neural_network?: Record<string, unknown>
  tabpfn?: Record<string, unknown>
}

// Decision threshold calibration for binary classification
export interface DecisionThresholdConfig {
  enabled: boolean
  metric?: 'f1' | 'balanced_accuracy' | 'precision' | 'recall' | 'mcc'
  thresholds_to_try?: number
}

// Advanced AutoGluon configuration
export interface AdvancedAutoGluonConfig {
  // Resource allocation
  num_gpus?: number
  num_cpus?: number

  // Bagging and stacking
  num_bag_folds?: number
  num_bag_sets?: number
  num_stack_levels?: number
  auto_stack?: boolean
  dynamic_stacking?: boolean

  // Model selection
  excluded_model_types?: string[]
  included_model_types?: string[]

  // Hyperparameters
  hyperparameters?: Record<string, unknown>
  hyperparameter_tune_kwargs?: Record<string, unknown>

  // NEW: HPO configuration
  hpo_config?: HyperparameterTuningConfig

  // NEW: Per-model hyperparameters
  per_model_hyperparameters?: PerModelHyperparameters

  // Post-training
  calibrate?: boolean
  refit_full?: boolean
  set_best_to_refit_full?: boolean

  // NEW: Decision threshold calibration
  threshold_config?: DecisionThresholdConfig

  // Training behavior
  holdout_frac?: number
  use_bag_holdout?: boolean

  // NEW: Pseudo-labeling for semi-supervised learning
  pseudo_labeling?: boolean
  unlabeled_data_path?: string

  // Feature engineering
  feature_generator_kwargs?: Record<string, unknown>
  feature_prune_kwargs?: Record<string, unknown>

  // NEW: Feature metadata for custom column types
  feature_metadata?: Record<string, string>

  // NEW: Drop unique/high-cardinality features
  drop_unique?: boolean

  // Memory optimization
  cache_data?: boolean
  infer_limit?: number

  // Verbosity
  verbosity?: number

  // Class imbalance handling
  class_imbalance_strategy?: 'oversample' | 'undersample' | 'smote' | 'focal_loss'
  sample_weight_column?: string

  // Knowledge distillation
  distill?: boolean
  distill_time_limit?: number

  // NEW: Foundation model options (2025 presets)
  use_tabular_foundation_models?: boolean
  foundation_model_preset?: 'zeroshot' | 'zeroshot_hpo'
}

export interface TimeSeriesAdvancedConfig {
  freq?: string
  known_covariates_names?: string[]
  static_features_names?: string[]
  quantile_levels?: number[]
  target_scaler?: string
  enable_ensemble?: boolean
  skip_model_selection?: boolean
  use_chronos?: boolean
  chronos_model_size?: 'tiny' | 'mini' | 'small' | 'base' | 'large'
}

export interface MultimodalAdvancedConfig {
  text_backbone?: string
  text_max_length?: number
  image_backbone?: string
  image_size?: number
  learning_rate?: number
  batch_size?: number
  max_epochs?: number
  warmup_steps?: number
  weight_decay?: number
  gradient_clip_val?: number
  fusion_method?: 'late' | 'early'
}

export interface Job {
  id: string
  name: string
  description?: string
  project_name?: string
  model_type: ModelType
  problem_type?: ProblemType
  status: JobStatus
  execution_target?: ExecutionTarget
  domino_job_id?: string
  domino_job_status?: string
  progress?: number
  current_step?: string
  data_source: 'upload' | 'domino_dataset' | 'mounted'
  dataset_id?: string
  file_path?: string
  target_column: string
  time_column?: string
  id_column?: string
  prediction_length?: number
  feature_columns?: string[]
  preset: Preset
  time_limit?: number
  eval_metric?: string
  metrics?: Record<string, unknown>
  leaderboard?: LeaderboardModel[]
  model_path?: string
  experiment_name?: string
  experiment_run_id?: string
  error_message?: string
  advanced_config?: AdvancedAutoGluonConfig
  timeseries_config?: TimeSeriesAdvancedConfig
  multimodal_config?: MultimodalAdvancedConfig
  is_registered?: boolean
  registered_model_name?: string
  registered_model_version?: string
  created_at: string
  started_at?: string
  completed_at?: string
}

export interface JobCreateRequest {
  name: string
  description?: string
  model_type: ModelType
  problem_type?: ProblemType
  execution_target?: ExecutionTarget
  run_as_domino_job?: boolean
  domino_hardware_tier_name?: string
  domino_environment_id?: string
  data_source: 'upload' | 'domino_dataset' | 'mounted'
  dataset_id?: string
  file_path?: string
  target_column: string
  time_column?: string
  id_column?: string
  prediction_length?: number
  feature_columns?: string[]
  preset: Preset
  time_limit?: number
  eval_metric?: string
  experiment_name?: string
  advanced_config?: AdvancedAutoGluonConfig
  timeseries_config?: TimeSeriesAdvancedConfig
  multimodal_config?: MultimodalAdvancedConfig
  auto_register?: boolean
  register_name?: string
}

export interface JobProgress {
  id: string
  status: JobStatus
  progress: number
  current_step?: string
  models_trained: number
  current_model?: string
  eta_seconds?: number
  started_at?: string
}

export interface JobLog {
  id: number
  job_id: string
  level: string
  message: string
  timestamp: string
}

export interface LeaderboardModel {
  model: string
  score_val: number
  pred_time_val?: number
  fit_time?: number
}
