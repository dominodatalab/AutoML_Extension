"""Time series prediction trainer."""

import logging
from typing import Any, Dict, List, Optional

import pandas as pd

from .base import BaseTrainer, AdvancedConfig
from .callbacks import TrainingProgressCallback

logger = logging.getLogger(__name__)


class TimeSeriesTrainer(BaseTrainer):
    """Trainer for time series prediction models."""

    async def train(
        self,
        df: pd.DataFrame,
        target_column: str,
        time_column: Optional[str],
        id_column: Optional[str],
        prediction_length: Optional[int],
        model_path: str,
        preset: str = "medium_quality",
        time_limit: Optional[int] = None,
        eval_metric: Optional[str] = None,
        advanced_config: Optional[AdvancedConfig] = None,
        timeseries_config: Optional[Dict[str, Any]] = None,
        feature_columns: Optional[List[str]] = None,
        progress: Optional[TrainingProgressCallback] = None,
    ) -> Dict[str, Any]:
        """Run time series prediction training."""
        from autogluon.timeseries import TimeSeriesPredictor, TimeSeriesDataFrame

        logger.info("Starting TimeSeriesPredictor training")
        if progress:
            progress.on_progress(5, "Initializing TimeSeriesPredictor")

        if not time_column:
            raise ValueError("time_column is required for timeseries models")
        if not prediction_length:
            raise ValueError("prediction_length is required for timeseries models")

        # Filter to selected feature columns if specified
        if feature_columns:
            required = {target_column, time_column}
            if id_column:
                required.add(id_column)
            keep_cols = list(required | set(feature_columns))
            missing = [c for c in keep_cols if c not in df.columns]
            if missing:
                raise ValueError(f"Feature columns not found in data: {missing}")
            df = df[keep_cols]
            logger.info(f"Filtered to {len(keep_cols)} columns (including required columns)")

        # Ensure time column is datetime and sort by it to prevent data leakage
        df = df.copy()
        if not pd.api.types.is_datetime64_any_dtype(df[time_column]):
            df[time_column] = pd.to_datetime(df[time_column], errors="coerce")
        df = df.sort_values(time_column).reset_index(drop=True)

        # Validate prediction_length is reasonable relative to data size
        min_rows_per_series = len(df)
        if id_column and id_column in df.columns:
            min_rows_per_series = df.groupby(id_column).size().min()
        if prediction_length >= min_rows_per_series:
            raise ValueError(
                f"prediction_length ({prediction_length}) must be less than the "
                f"shortest series length ({min_rows_per_series}). "
                f"Reduce prediction_length or provide more data."
            )

        # Add a synthetic item_id for single-series data when no id_column provided
        if not id_column:
            df["item_id"] = "default"
            id_column = "item_id"

        # Validate multi-series data: check for duplicate timestamps within each series
        dup_check = df.groupby(id_column)[time_column].apply(lambda s: s.duplicated().sum())
        series_with_dups = dup_check[dup_check > 0]
        if len(series_with_dups) > 0:
            dup_ids = list(series_with_dups.index[:5])
            logger.warning(
                f"Duplicate timestamps found in {len(series_with_dups)} series "
                f"(e.g. {dup_ids}). Keeping last occurrence."
            )
            df = df.drop_duplicates(subset=[id_column, time_column], keep="last")

        # Convert to TimeSeriesDataFrame
        ts_df = TimeSeriesDataFrame.from_data_frame(
            df,
            id_column=id_column,
            timestamp_column=time_column,
        )

        # Auto-detect frequency if not explicitly provided
        detected_freq = None
        if not (timeseries_config and timeseries_config.get("freq")):
            try:
                timestamps = pd.to_datetime(ts_df.index.get_level_values("timestamp"))
                detected_freq = pd.infer_freq(timestamps)
            except Exception:
                pass
            if not detected_freq:
                # Infer from median time delta per series to avoid cross-series artifacts
                try:
                    reset_df = ts_df.reset_index()
                    first_id = reset_df[id_column].iloc[0] if id_column in reset_df.columns else None
                    if first_id is not None:
                        series_ts = reset_df[reset_df[id_column] == first_id]["timestamp"].sort_values()
                    else:
                        series_ts = reset_df["timestamp"].sort_values()
                    median_delta = series_ts.diff().median()
                    if median_delta <= pd.Timedelta(hours=1):
                        detected_freq = "h"
                    elif median_delta <= pd.Timedelta(days=1):
                        detected_freq = "D"
                    elif median_delta <= pd.Timedelta(days=3):
                        detected_freq = "D"
                    elif median_delta <= pd.Timedelta(days=8):
                        detected_freq = "W"
                    elif median_delta <= pd.Timedelta(days=35):
                        detected_freq = "MS"
                    elif median_delta <= pd.Timedelta(days=100):
                        detected_freq = "QS"
                    else:
                        detected_freq = "YS"
                    logger.info(f"Auto-detected frequency from median delta ({median_delta}): {detected_freq}")
                except Exception:
                    detected_freq = "D"
                    logger.warning("Could not infer frequency, defaulting to 'D'")

        # Configure predictor
        predictor_kwargs = {
            "target": target_column,
            "prediction_length": prediction_length,
            "path": model_path,
            "verbosity": advanced_config.verbosity if advanced_config else 2,
        }

        if eval_metric:
            predictor_kwargs["eval_metric"] = eval_metric

        # Apply timeseries-specific config to predictor
        if timeseries_config:
            if timeseries_config.get("freq"):
                predictor_kwargs["freq"] = timeseries_config["freq"]
            if timeseries_config.get("quantile_levels"):
                predictor_kwargs["quantile_levels"] = timeseries_config["quantile_levels"]

        # Use auto-detected freq if none was set by config
        if "freq" not in predictor_kwargs and detected_freq:
            predictor_kwargs["freq"] = detected_freq

        # Create predictor
        predictor = TimeSeriesPredictor(**predictor_kwargs)

        # Map tabular presets to valid TS presets
        ts_preset_map = {
            "medium_quality_faster_train": "medium_quality",
            "good_quality": "medium_quality",
            "optimize_for_deployment": "fast_training",
        }
        ts_preset = ts_preset_map.get(preset, preset)

        # Configure fit parameters
        fit_kwargs = {
            "train_data": ts_df,
            "presets": ts_preset,
        }

        if time_limit:
            fit_kwargs["time_limit"] = time_limit

        # Apply advanced configuration
        if advanced_config:
            if advanced_config.num_gpus > 0:
                fit_kwargs["num_gpus"] = advanced_config.num_gpus

            if advanced_config.excluded_model_types:
                fit_kwargs["excluded_model_types"] = advanced_config.excluded_model_types

            if advanced_config.hyperparameters:
                fit_kwargs["hyperparameters"] = advanced_config.hyperparameters

        # Apply timeseries-specific config to fit
        if timeseries_config:
            reserved_cols = {target_column, time_column, id_column}

            # Known covariates
            if timeseries_config.get("known_covariates_names"):
                cov_names = timeseries_config["known_covariates_names"]
                available_cols = set(ts_df.columns)
                invalid = [c for c in cov_names if c not in available_cols]
                if invalid:
                    raise ValueError(f"known_covariates_names columns not found in data: {invalid}")
                conflict = [c for c in cov_names if c in reserved_cols]
                if conflict:
                    raise ValueError(f"known_covariates_names cannot include target/time/id columns: {conflict}")
                fit_kwargs["known_covariates_names"] = cov_names

            # Static features
            if timeseries_config.get("static_features_names"):
                sf_names = timeseries_config["static_features_names"]
                available_cols = set(ts_df.columns)
                invalid = [c for c in sf_names if c not in available_cols]
                if invalid:
                    raise ValueError(f"static_features_names columns not found in data: {invalid}")
                fit_kwargs["static_features_names"] = sf_names

            # Target scaler
            if timeseries_config.get("target_scaler"):
                fit_kwargs["target_scaler"] = timeseries_config["target_scaler"]

            # Enable ensemble
            if timeseries_config.get("enable_ensemble") is False:
                fit_kwargs["enable_ensemble"] = False

            # Skip model selection
            if timeseries_config.get("skip_model_selection"):
                fit_kwargs["skip_model_selection"] = True

            # Chronos foundation model
            if timeseries_config.get("use_chronos"):
                chronos_size = timeseries_config.get("chronos_model_size", "tiny")
                # Add Chronos to hyperparameters
                if "hyperparameters" not in fit_kwargs:
                    fit_kwargs["hyperparameters"] = {}
                fit_kwargs["hyperparameters"]["Chronos"] = {
                    "model_path": f"amazon/chronos-t5-{chronos_size}"
                }
                logger.info(f"Added Chronos model: amazon/chronos-t5-{chronos_size}")

        if progress:
            progress.on_progress(10, "Starting model training")

        # Train
        predictor.fit(**fit_kwargs)

        if progress:
            progress.on_progress(90, "Training complete, computing metrics")

        # Get results
        leaderboard = predictor.leaderboard(silent=True)
        best_model = leaderboard.iloc[0] if len(leaderboard) > 0 else None

        metrics = {
            "best_model": best_model["model"] if best_model is not None else None,
            "best_score": float(best_model["score_val"]) if best_model is not None else None,
            "prediction_length": prediction_length,
            "eval_metric": str(predictor.eval_metric),
            "num_models": len(leaderboard),
        }

        # Return leaderboard as list (schema expects List[Dict])
        leaderboard_list = leaderboard.to_dict(orient="records")

        if progress:
            progress.on_progress(100, "Training completed successfully")

        logger.info(f"Training completed. Best model: {metrics['best_model']}")

        return {
            "metrics": metrics,
            "leaderboard": leaderboard_list,
            "model_path": model_path,
            "predictor": predictor,
        }
