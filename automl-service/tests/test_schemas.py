"""Tests for Pydantic schema validation in app.api.schemas.job."""

import pytest
from pydantic import ValidationError

from app.api.schemas.job import (
    AdvancedAutoGluonConfig,
    CleanupRequest,
    DecisionThresholdConfig,
    HyperparameterTuningConfig,
    JobCreateRequest,
    JobListRequest,
    TimeSeriesAdvancedConfig,
)


# ---------------------------------------------------------------------------
# JobCreateRequest
# ---------------------------------------------------------------------------


class TestJobCreateRequest:
    """Test JobCreateRequest validation."""

    def test_valid_tabular_minimal(self):
        """Minimal valid tabular request."""
        req = JobCreateRequest(
            name="my-job",
            model_type="tabular",
            data_source="upload",
            target_column="target",
        )
        assert req.name == "my-job"
        assert req.model_type == "tabular"
        assert req.data_source == "upload"
        assert req.target_column == "target"
        assert req.preset == "medium_quality_faster_train"  # default
        assert req.time_limit == 3600  # default
        assert req.auto_register is False

    def test_valid_tabular_full(self):
        """Tabular request with all common fields populated."""
        req = JobCreateRequest(
            name="full-job",
            description="A full test",
            model_type="tabular",
            problem_type="binary",
            data_source="mounted",
            file_path="/data/train.csv",
            target_column="label",
            feature_columns=["age", "income"],
            preset="best_quality",
            time_limit=7200,
            eval_metric="f1",
            experiment_name="exp-1",
            auto_register=True,
            register_name="my-model",
        )
        assert req.description == "A full test"
        assert req.problem_type == "binary"
        assert req.file_path == "/data/train.csv"
        assert req.feature_columns == ["age", "income"]
        assert req.preset == "best_quality"
        assert req.time_limit == 7200

    def test_valid_timeseries(self):
        """Valid timeseries request with time_column and prediction_length."""
        req = JobCreateRequest(
            name="ts-job",
            model_type="timeseries",
            data_source="upload",
            target_column="value",
            time_column="timestamp",
            id_column="item_id",
            prediction_length=30,
        )
        assert req.model_type == "timeseries"
        assert req.time_column == "timestamp"
        assert req.id_column == "item_id"
        assert req.prediction_length == 30

    def test_timeseries_without_time_column_passes_schema(self):
        """Schema level allows time_column=None; service layer validates it."""
        req = JobCreateRequest(
            name="ts-no-time",
            model_type="timeseries",
            data_source="upload",
            target_column="value",
        )
        assert req.time_column is None

    def test_missing_required_name(self):
        """name is required."""
        with pytest.raises(ValidationError) as exc_info:
            JobCreateRequest(
                model_type="tabular",
                data_source="upload",
                target_column="target",
            )
        errors = exc_info.value.errors()
        assert any(e["loc"] == ("name",) for e in errors)

    def test_missing_required_model_type(self):
        """model_type is required."""
        with pytest.raises(ValidationError) as exc_info:
            JobCreateRequest(
                name="test",
                data_source="upload",
                target_column="target",
            )
        errors = exc_info.value.errors()
        assert any(e["loc"] == ("model_type",) for e in errors)

    def test_missing_required_data_source(self):
        """data_source is required."""
        with pytest.raises(ValidationError) as exc_info:
            JobCreateRequest(
                name="test",
                model_type="tabular",
                target_column="target",
            )
        errors = exc_info.value.errors()
        assert any(e["loc"] == ("data_source",) for e in errors)

    def test_missing_required_target_column(self):
        """target_column is required."""
        with pytest.raises(ValidationError) as exc_info:
            JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
            )
        errors = exc_info.value.errors()
        assert any(e["loc"] == ("target_column",) for e in errors)

    def test_invalid_model_type(self):
        """model_type must be 'tabular' or 'timeseries'."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="test",
                model_type="image",
                data_source="upload",
                target_column="target",
            )

    def test_invalid_data_source(self):
        """data_source must be one of the allowed literals."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="s3_bucket",
                target_column="target",
            )

    def test_invalid_preset(self):
        """preset must be one of the allowed literals."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
                target_column="target",
                preset="ultra_quality",
            )

    def test_name_empty_string_rejected(self):
        """name has min_length=1, so empty string fails."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="",
                model_type="tabular",
                data_source="upload",
                target_column="target",
            )

    def test_name_too_long_rejected(self):
        """name has max_length=255."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="x" * 256,
                model_type="tabular",
                data_source="upload",
                target_column="target",
            )

    def test_time_limit_below_minimum(self):
        """time_limit has ge=60."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
                target_column="target",
                time_limit=30,
            )

    def test_prediction_length_must_be_positive(self):
        """prediction_length has ge=1."""
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="ts-test",
                model_type="timeseries",
                data_source="upload",
                target_column="value",
                prediction_length=0,
            )

    def test_all_valid_presets(self):
        """Every allowed preset should be accepted."""
        presets = [
            "best_quality",
            "high_quality",
            "good_quality",
            "medium_quality_faster_train",
            "optimize_for_deployment",
            "chronos",
            "fast_training",
            "zeroshot",
            "zeroshot_hpo",
            "experimental_tabfm",
        ]
        for preset in presets:
            req = JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
                target_column="target",
                preset=preset,
            )
            assert req.preset == preset

    def test_problem_type_literals(self):
        """All valid problem types should be accepted."""
        for pt in ["binary", "multiclass", "regression", "quantile"]:
            req = JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
                target_column="target",
                problem_type=pt,
            )
            assert req.problem_type == pt

    def test_invalid_problem_type(self):
        with pytest.raises(ValidationError):
            JobCreateRequest(
                name="test",
                model_type="tabular",
                data_source="upload",
                target_column="target",
                problem_type="clustering",
            )


# ---------------------------------------------------------------------------
# AdvancedAutoGluonConfig
# ---------------------------------------------------------------------------


class TestAdvancedAutoGluonConfig:
    """Test AdvancedAutoGluonConfig validation."""

    def test_defaults(self):
        """Default instance should have sensible defaults."""
        cfg = AdvancedAutoGluonConfig()
        assert cfg.num_gpus == 0
        assert cfg.num_cpus is None
        assert cfg.num_bag_folds is None
        assert cfg.num_stack_levels is None
        assert cfg.auto_stack is False
        assert cfg.excluded_model_types == []
        assert cfg.included_model_types == []
        assert cfg.verbosity == 2
        assert cfg.calibrate is False
        assert cfg.refit_full is False
        assert cfg.distill is False
        assert cfg.pseudo_labeling is False
        assert cfg.cache_data is True
        assert cfg.feature_prune is False

    def test_num_gpus_negative_rejected(self):
        """num_gpus has ge=0."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_gpus=-1)

    def test_num_cpus_zero_rejected(self):
        """num_cpus has ge=1."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_cpus=0)

    def test_num_bag_folds_bounds(self):
        """num_bag_folds must be 2-10."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_bag_folds=1)
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_bag_folds=11)
        cfg = AdvancedAutoGluonConfig(num_bag_folds=2)
        assert cfg.num_bag_folds == 2
        cfg = AdvancedAutoGluonConfig(num_bag_folds=10)
        assert cfg.num_bag_folds == 10

    def test_num_stack_levels_bounds(self):
        """num_stack_levels must be 0-3."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_stack_levels=-1)
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(num_stack_levels=4)
        cfg = AdvancedAutoGluonConfig(num_stack_levels=0)
        assert cfg.num_stack_levels == 0
        cfg = AdvancedAutoGluonConfig(num_stack_levels=3)
        assert cfg.num_stack_levels == 3

    def test_verbosity_bounds(self):
        """verbosity must be 0-4."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(verbosity=-1)
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(verbosity=5)
        for v in range(5):
            assert AdvancedAutoGluonConfig(verbosity=v).verbosity == v

    def test_holdout_frac_bounds(self):
        """holdout_frac must be 0.01-0.5."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(holdout_frac=0.005)
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(holdout_frac=0.6)
        cfg = AdvancedAutoGluonConfig(holdout_frac=0.2)
        assert cfg.holdout_frac == 0.2

    def test_extra_fields_ignored(self):
        """model_config has extra='ignore', so unknown fields are dropped."""
        cfg = AdvancedAutoGluonConfig(
            num_gpus=1,
            totally_fake_field="should be ignored",
            another_unknown=42,
        )
        assert cfg.num_gpus == 1
        assert not hasattr(cfg, "totally_fake_field")
        assert not hasattr(cfg, "another_unknown")

    def test_infer_limit_minimum(self):
        """infer_limit has ge=0.001."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(infer_limit=0.0001)
        cfg = AdvancedAutoGluonConfig(infer_limit=0.001)
        assert cfg.infer_limit == 0.001

    def test_distill_time_limit_minimum(self):
        """distill_time_limit has ge=60."""
        with pytest.raises(ValidationError):
            AdvancedAutoGluonConfig(distill_time_limit=30)
        cfg = AdvancedAutoGluonConfig(distill_time_limit=60)
        assert cfg.distill_time_limit == 60


# ---------------------------------------------------------------------------
# HyperparameterTuningConfig
# ---------------------------------------------------------------------------


class TestHyperparameterTuningConfig:
    """Test HyperparameterTuningConfig validation."""

    def test_defaults(self):
        cfg = HyperparameterTuningConfig()
        assert cfg.enabled is False
        assert cfg.scheduler == "local"
        assert cfg.searcher == "auto"
        assert cfg.num_trials == 10
        assert cfg.max_t is None
        assert cfg.grace_period is None
        assert cfg.reduction_factor is None

    def test_num_trials_lower_bound(self):
        """num_trials has ge=1."""
        with pytest.raises(ValidationError):
            HyperparameterTuningConfig(num_trials=0)
        cfg = HyperparameterTuningConfig(num_trials=1)
        assert cfg.num_trials == 1

    def test_num_trials_upper_bound(self):
        """num_trials has le=100."""
        with pytest.raises(ValidationError):
            HyperparameterTuningConfig(num_trials=101)
        cfg = HyperparameterTuningConfig(num_trials=100)
        assert cfg.num_trials == 100

    def test_max_t_must_be_positive(self):
        """max_t has ge=1."""
        with pytest.raises(ValidationError):
            HyperparameterTuningConfig(max_t=0)
        cfg = HyperparameterTuningConfig(max_t=1)
        assert cfg.max_t == 1

    def test_grace_period_must_be_positive(self):
        """grace_period has ge=1."""
        with pytest.raises(ValidationError):
            HyperparameterTuningConfig(grace_period=0)

    def test_reduction_factor_must_be_ge_one(self):
        """reduction_factor has ge=1.0."""
        with pytest.raises(ValidationError):
            HyperparameterTuningConfig(reduction_factor=0.5)
        cfg = HyperparameterTuningConfig(reduction_factor=1.0)
        assert cfg.reduction_factor == 1.0


# ---------------------------------------------------------------------------
# DecisionThresholdConfig
# ---------------------------------------------------------------------------


class TestDecisionThresholdConfig:
    """Test DecisionThresholdConfig validation."""

    def test_defaults(self):
        cfg = DecisionThresholdConfig()
        assert cfg.enabled is False
        assert cfg.metric == "balanced_accuracy"
        assert cfg.thresholds_to_try == 100

    def test_thresholds_to_try_lower_bound(self):
        """thresholds_to_try has ge=10."""
        with pytest.raises(ValidationError):
            DecisionThresholdConfig(thresholds_to_try=9)
        cfg = DecisionThresholdConfig(thresholds_to_try=10)
        assert cfg.thresholds_to_try == 10

    def test_thresholds_to_try_upper_bound(self):
        """thresholds_to_try has le=1000."""
        with pytest.raises(ValidationError):
            DecisionThresholdConfig(thresholds_to_try=1001)
        cfg = DecisionThresholdConfig(thresholds_to_try=1000)
        assert cfg.thresholds_to_try == 1000

    def test_custom_metric(self):
        cfg = DecisionThresholdConfig(metric="f1", thresholds_to_try=50)
        assert cfg.metric == "f1"
        assert cfg.thresholds_to_try == 50


# ---------------------------------------------------------------------------
# CleanupRequest
# ---------------------------------------------------------------------------


class TestCleanupRequest:
    """Test CleanupRequest defaults and validation."""

    def test_defaults(self):
        req = CleanupRequest()
        assert req.statuses == ["failed", "cancelled"]
        assert req.older_than_days is None
        assert req.include_orphans is False

    def test_custom_values(self):
        req = CleanupRequest(
            statuses=["failed", "completed"],
            older_than_days=30,
            include_orphans=True,
        )
        assert req.statuses == ["failed", "completed"]
        assert req.older_than_days == 30
        assert req.include_orphans is True

    def test_empty_statuses(self):
        """Empty statuses list should be allowed by schema."""
        req = CleanupRequest(statuses=[])
        assert req.statuses == []


# ---------------------------------------------------------------------------
# JobListRequest
# ---------------------------------------------------------------------------


class TestJobListRequest:
    """Test JobListRequest pagination and filter validation."""

    def test_defaults(self):
        req = JobListRequest()
        assert req.skip == 0
        assert req.limit == 100
        assert req.status is None
        assert req.model_type is None
        assert req.owner is None
        assert req.project_id is None
        assert req.project_name is None

    def test_skip_negative_rejected(self):
        """skip has ge=0."""
        with pytest.raises(ValidationError):
            JobListRequest(skip=-1)

    def test_limit_zero_rejected(self):
        """limit has ge=1."""
        with pytest.raises(ValidationError):
            JobListRequest(limit=0)

    def test_limit_above_max_rejected(self):
        """limit has le=1000."""
        with pytest.raises(ValidationError):
            JobListRequest(limit=1001)

    def test_limit_boundary_values(self):
        req_min = JobListRequest(limit=1)
        assert req_min.limit == 1
        req_max = JobListRequest(limit=1000)
        assert req_max.limit == 1000

    def test_with_filters(self):
        req = JobListRequest(
            skip=10,
            limit=50,
            status="completed",
            model_type="tabular",
            owner="alice",
            project_id="proj-123",
            project_name="my-project",
        )
        assert req.skip == 10
        assert req.limit == 50
        assert req.status == "completed"
        assert req.model_type == "tabular"
        assert req.owner == "alice"
        assert req.project_id == "proj-123"
        assert req.project_name == "my-project"


# ---------------------------------------------------------------------------
# TimeSeriesAdvancedConfig
# ---------------------------------------------------------------------------


class TestTimeSeriesAdvancedConfig:
    """Test TimeSeriesAdvancedConfig validation."""

    def test_defaults(self):
        cfg = TimeSeriesAdvancedConfig()
        assert cfg.freq is None
        assert cfg.known_covariates_names == []
        assert cfg.static_features_names == []
        assert cfg.quantile_levels == [0.1, 0.5, 0.9]
        assert cfg.target_scaler is None
        assert cfg.enable_ensemble is True
        assert cfg.skip_model_selection is False
        assert cfg.use_chronos is False
        assert cfg.chronos_model_size == "tiny"

    def test_quantile_levels_default(self):
        """Default quantile levels should be [0.1, 0.5, 0.9]."""
        cfg = TimeSeriesAdvancedConfig()
        assert cfg.quantile_levels == [0.1, 0.5, 0.9]

    def test_custom_quantile_levels(self):
        cfg = TimeSeriesAdvancedConfig(quantile_levels=[0.25, 0.5, 0.75])
        assert cfg.quantile_levels == [0.25, 0.5, 0.75]

    def test_custom_freq(self):
        cfg = TimeSeriesAdvancedConfig(freq="H")
        assert cfg.freq == "H"

    def test_covariates_and_static_features(self):
        cfg = TimeSeriesAdvancedConfig(
            known_covariates_names=["holiday", "promo"],
            static_features_names=["store_type"],
        )
        assert cfg.known_covariates_names == ["holiday", "promo"]
        assert cfg.static_features_names == ["store_type"]

    def test_chronos_options(self):
        cfg = TimeSeriesAdvancedConfig(use_chronos=True, chronos_model_size="large")
        assert cfg.use_chronos is True
        assert cfg.chronos_model_size == "large"

    def test_empty_quantile_levels(self):
        """Empty list should be accepted by schema."""
        cfg = TimeSeriesAdvancedConfig(quantile_levels=[])
        assert cfg.quantile_levels == []
