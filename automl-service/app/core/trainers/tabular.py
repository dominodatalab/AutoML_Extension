"""Tabular prediction trainer."""

import logging
from typing import Any, Dict, Optional

import pandas as pd

from app.db.models import ProblemType
from .base import BaseTrainer, AdvancedConfig
from .callbacks import TrainingProgressCallback

logger = logging.getLogger(__name__)


class TabularTrainer(BaseTrainer):
    """Trainer for tabular prediction models."""

    async def train(
        self,
        df: pd.DataFrame,
        target_column: str,
        model_path: str,
        problem_type: Optional[ProblemType] = None,
        preset: str = "medium_quality_faster_train",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: Optional[AdvancedConfig] = None,
        progress: Optional[TrainingProgressCallback] = None,
    ) -> Dict[str, Any]:
        """Run tabular prediction training with advanced options."""
        from autogluon.tabular import TabularPredictor

        logger.info("Starting TabularPredictor training")
        if progress:
            progress.on_progress(5, "Initializing TabularPredictor")

        # Configure predictor
        predictor_kwargs = {
            "label": target_column,
            "path": model_path,
            "verbosity": advanced_config.verbosity if advanced_config else 2,
        }

        if problem_type:
            predictor_kwargs["problem_type"] = problem_type.value

        if eval_metric:
            predictor_kwargs["eval_metric"] = eval_metric

        # Create predictor
        predictor = TabularPredictor(**predictor_kwargs)

        # Configure fit parameters
        fit_kwargs = {
            "train_data": df,
            "presets": preset,
        }

        if time_limit:
            fit_kwargs["time_limit"] = time_limit

        # Apply advanced configuration
        if advanced_config:
            self._apply_advanced_config(fit_kwargs, advanced_config, problem_type)

        if progress:
            progress.on_progress(10, "Starting model training")

        # Train
        predictor.fit(**fit_kwargs)

        # NEW: Post-training decision threshold calibration
        if (advanced_config and
            advanced_config.threshold_config and
            advanced_config.threshold_config.enabled and
            problem_type and problem_type.value == "binary"):
            try:
                if progress:
                    progress.on_progress(85, "Calibrating decision threshold")
                threshold_config = advanced_config.threshold_config
                predictor.calibrate_decision_threshold(
                    metric=threshold_config.metric,
                    thresholds_to_try=threshold_config.thresholds_to_try,
                )
                logger.info(f"Decision threshold calibrated for {threshold_config.metric}")
            except Exception as e:
                logger.warning(f"Could not calibrate decision threshold: {e}")

        if progress:
            progress.on_progress(80, "Training complete, computing metrics")

        # Get results
        leaderboard = predictor.leaderboard(silent=True)
        best_model = leaderboard.iloc[0] if len(leaderboard) > 0 else None

        # Get feature importance
        feature_importance = None
        try:
            fi = predictor.feature_importance(silent=True)
            if fi is not None and len(fi) > 0:
                feature_importance = [
                    {"feature": idx, "importance": float(row.iloc[0]) if hasattr(row, 'iloc') else float(row)}
                    for idx, row in fi.iterrows()
                ]
                feature_importance.sort(key=lambda x: abs(x["importance"]), reverse=True)
        except Exception as e:
            logger.warning(f"Could not compute feature importance: {e}")

        metrics = {
            "best_model": best_model["model"] if best_model is not None else None,
            "best_score": float(best_model["score_val"]) if best_model is not None else None,
            "problem_type": predictor.problem_type,
            "eval_metric": str(predictor.eval_metric) if hasattr(predictor.eval_metric, '__str__') else predictor.eval_metric,
            "num_models": len(leaderboard),
            "num_features": len(predictor.feature_metadata.get_features()) if predictor.feature_metadata else 0,
        }

        # Return leaderboard as list (schema expects List[Dict])
        leaderboard_list = leaderboard.to_dict(orient="records")

        if progress:
            progress.on_progress(100, "Training completed successfully")

        logger.info(f"Training completed. Best model: {metrics['best_model']}")

        # Refit on full data if requested
        if advanced_config and advanced_config.refit_full:
            logger.info("Refitting best model on full dataset")
            predictor.refit_full()

        return {
            "metrics": metrics,
            "leaderboard": leaderboard_list,
            "model_path": model_path,
            "predictor": predictor,
            "feature_importance": feature_importance,
        }

    def _apply_advanced_config(
        self,
        fit_kwargs: Dict[str, Any],
        advanced_config: AdvancedConfig,
        problem_type: Optional[ProblemType] = None,
    ):
        """Apply advanced configuration to fit_kwargs."""
        if advanced_config.num_gpus > 0:
            fit_kwargs["num_gpus"] = advanced_config.num_gpus

        if advanced_config.num_cpus:
            fit_kwargs["num_cpus"] = advanced_config.num_cpus

        if advanced_config.num_bag_folds:
            fit_kwargs["num_bag_folds"] = advanced_config.num_bag_folds

        if advanced_config.num_bag_sets:
            fit_kwargs["num_bag_sets"] = advanced_config.num_bag_sets

        if advanced_config.num_stack_levels:
            fit_kwargs["num_stack_levels"] = advanced_config.num_stack_levels

        if advanced_config.holdout_frac:
            fit_kwargs["holdout_frac"] = advanced_config.holdout_frac

        if advanced_config.auto_stack:
            fit_kwargs["auto_stack"] = True

        if advanced_config.excluded_model_types:
            fit_kwargs["excluded_model_types"] = advanced_config.excluded_model_types

        if advanced_config.included_model_types:
            fit_kwargs["included_model_types"] = advanced_config.included_model_types

        if advanced_config.hyperparameters:
            fit_kwargs["hyperparameters"] = advanced_config.hyperparameters

        if advanced_config.hyperparameter_tune_kwargs:
            fit_kwargs["hyperparameter_tune_kwargs"] = advanced_config.hyperparameter_tune_kwargs

        if advanced_config.ag_args_fit:
            # Merge with existing ag_args_fit if present
            if "ag_args_fit" in fit_kwargs:
                fit_kwargs["ag_args_fit"].update(advanced_config.ag_args_fit)
            else:
                fit_kwargs["ag_args_fit"] = dict(advanced_config.ag_args_fit)

        if advanced_config.calibrate:
            fit_kwargs["calibrate"] = True

        if advanced_config.feature_prune:
            fit_kwargs["feature_prune"] = True

        # Feature generator kwargs
        if advanced_config.feature_generator_kwargs:
            fit_kwargs["feature_generator_kwargs"] = advanced_config.feature_generator_kwargs

        # Feature prune kwargs
        if advanced_config.feature_prune_kwargs:
            fit_kwargs["feature_prune_kwargs"] = advanced_config.feature_prune_kwargs

        # NEW: Dynamic stacking
        if advanced_config.dynamic_stacking:
            fit_kwargs["dynamic_stacking"] = True

        # NEW: Use bag holdout
        if advanced_config.use_bag_holdout:
            fit_kwargs["use_bag_holdout"] = True

        # NEW: Refit full
        if advanced_config.refit_full:
            fit_kwargs["refit_full"] = True

        # NEW: Set best to refit full
        if advanced_config.set_best_to_refit_full:
            fit_kwargs["set_best_to_refit_full"] = True

        # NEW: Inference limit
        if advanced_config.infer_limit:
            fit_kwargs["infer_limit"] = advanced_config.infer_limit

        # NEW: HPO configuration
        if advanced_config.hpo_config and advanced_config.hpo_config.enabled:
            hpo = advanced_config.hpo_config
            hpo_kwargs = {
                "scheduler": hpo.scheduler,
                "searcher": hpo.searcher,
                "num_trials": hpo.num_trials,
            }
            if hpo.max_t:
                hpo_kwargs["max_t"] = hpo.max_t
            if hpo.grace_period:
                hpo_kwargs["grace_period"] = hpo.grace_period
            if hpo.reduction_factor:
                hpo_kwargs["reduction_factor"] = hpo.reduction_factor
            fit_kwargs["hyperparameter_tune_kwargs"] = hpo_kwargs

        # NEW: Per-model hyperparameters
        if advanced_config.per_model_hyperparameters:
            model_hps = {}
            hp_map = {
                "lightgbm": "GBM",
                "catboost": "CAT",
                "xgboost": "XGB",
                "random_forest": "RF",
                "neural_network": "NN_TORCH",
                "tabpfn": "TABPFN",
            }
            # PerModelHyperparameters is a Pydantic model; dump to dict
            # excluding None values to iterate over provided overrides.
            per_model_dict = advanced_config.per_model_hyperparameters.model_dump(exclude_none=True)
            for model_key, hps in per_model_dict.items():
                if hps and model_key in hp_map:
                    model_hps[hp_map[model_key]] = hps
            if model_hps:
                fit_kwargs["hyperparameters"] = model_hps

        # NEW: Class imbalance handling
        if advanced_config.class_imbalance_strategy:
            strategy = advanced_config.class_imbalance_strategy
            # Ensure ag_args_fit exists
            if "ag_args_fit" not in fit_kwargs:
                fit_kwargs["ag_args_fit"] = {}

            if strategy == "focal_loss":
                # Use focal loss for neural networks
                fit_kwargs["ag_args_fit"]["use_focal_loss"] = True
                logger.info("Using focal loss for class imbalance")
            elif strategy == "oversample":
                fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"
                logger.info("Using oversampling via balanced class weights")
            elif strategy == "undersample":
                fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"
                logger.info("Using undersampling via balanced class weights")
            elif strategy == "smote":
                # SMOTE requires imblearn, log a warning if not available
                try:
                    from imblearn.over_sampling import SMOTE
                    fit_kwargs["ag_args_fit"]["use_smote"] = True
                    logger.info("SMOTE enabled for class imbalance")
                except ImportError:
                    logger.warning("SMOTE requires imblearn. Install with: pip install imbalanced-learn")
                    fit_kwargs["ag_args_fit"]["class_weight"] = "balanced"

        # NEW: Sample weight column
        if advanced_config.sample_weight_column:
            fit_kwargs["sample_weight"] = advanced_config.sample_weight_column

        # NEW: Drop unique/high-cardinality features
        if advanced_config.drop_unique:
            fit_kwargs["drop_unique"] = True

        # NEW: Cache data in memory
        if advanced_config.cache_data is False:
            fit_kwargs["cache_data"] = False

        # NEW: Feature metadata for custom column types
        if advanced_config.feature_metadata:
            from autogluon.common.features.types import R_CATEGORY, R_INT, R_FLOAT
            feature_metadata = {}
            type_map = {
                "category": R_CATEGORY,
                "int": R_INT,
                "float": R_FLOAT,
            }
            for col, col_type in advanced_config.feature_metadata.items():
                if col_type in type_map:
                    feature_metadata[col] = type_map[col_type]
            if feature_metadata:
                fit_kwargs["feature_metadata"] = feature_metadata

        # NEW: Foundation models (TabPFN, etc.)
        if advanced_config.use_tabular_foundation_models:
            if "hyperparameters" not in fit_kwargs:
                fit_kwargs["hyperparameters"] = {}
            # Add TabPFN to the hyperparameters
            fit_kwargs["hyperparameters"]["TABPFN"] = {}
            logger.info("Added TabPFN foundation model to training")

            # If using zeroshot preset, configure accordingly
            if advanced_config.foundation_model_preset:
                if advanced_config.foundation_model_preset == "zeroshot":
                    # Use only TabPFN for zero-shot
                    fit_kwargs["hyperparameters"] = {"TABPFN": {}}
                    fit_kwargs["num_bag_folds"] = 0
                    fit_kwargs["num_stack_levels"] = 0
                    logger.info("Using zero-shot foundation model preset")
                elif advanced_config.foundation_model_preset == "zeroshot_hpo":
                    fit_kwargs["hyperparameters"] = {"TABPFN": {}}
                    if "hyperparameter_tune_kwargs" not in fit_kwargs:
                        fit_kwargs["hyperparameter_tune_kwargs"] = {
                            "scheduler": "local",
                            "searcher": "auto",
                            "num_trials": 5,
                        }
                    logger.info("Using zero-shot + HPO foundation model preset")

        # NEW: Pseudo-labeling for semi-supervised learning
        if advanced_config.pseudo_labeling and advanced_config.unlabeled_data_path:
            try:
                unlabeled_df = self.load_data(advanced_config.unlabeled_data_path)
                fit_kwargs["unlabeled_data"] = unlabeled_df
                logger.info(f"Loaded {len(unlabeled_df)} rows of unlabeled data for pseudo-labeling")
            except Exception as e:
                logger.warning(f"Could not load unlabeled data: {e}")

        # NEW: Distillation
        if advanced_config.distill:
            fit_kwargs["ds_args"] = {"distill": True}
            if advanced_config.distill_time_limit:
                fit_kwargs["ds_args"]["time_limit"] = advanced_config.distill_time_limit
