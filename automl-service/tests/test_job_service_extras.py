"""Tests for helper functions in app.services.job_service that lack coverage."""

from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import IntegrityError

from app.db.models import JobStatus, ModelType, ProblemType
from app.services.job_service import (
    _coerce_nonnegative_int,
    _get_local_queue_depth,
    _is_job_name_unique_violation,
    build_job_list_item_response,
    serialize_job_config,
)


# ---------------------------------------------------------------------------
# _coerce_nonnegative_int
# ---------------------------------------------------------------------------
class TestCoerceNonnegativeInt:
    def test_positive_int(self):
        assert _coerce_nonnegative_int(5) == 5

    def test_zero(self):
        assert _coerce_nonnegative_int(0) == 0

    def test_negative_int_clamped(self):
        assert _coerce_nonnegative_int(-3) == 0

    def test_string_number(self):
        assert _coerce_nonnegative_int("7") == 7

    def test_string_negative_clamped(self):
        assert _coerce_nonnegative_int("-10") == 0

    def test_float_truncated(self):
        assert _coerce_nonnegative_int(3.9) == 3

    def test_float_negative_clamped(self):
        assert _coerce_nonnegative_int(-1.5) == 0

    def test_none_returns_none(self):
        assert _coerce_nonnegative_int(None) is None

    def test_bool_true_returns_none(self):
        assert _coerce_nonnegative_int(True) is None

    def test_bool_false_returns_none(self):
        assert _coerce_nonnegative_int(False) is None

    def test_non_numeric_string_returns_none(self):
        assert _coerce_nonnegative_int("abc") is None

    def test_empty_string_returns_none(self):
        assert _coerce_nonnegative_int("") is None

    def test_list_returns_none(self):
        assert _coerce_nonnegative_int([1, 2]) is None

    def test_large_int(self):
        assert _coerce_nonnegative_int(999999) == 999999

    def test_string_float(self):
        # int("3.5") raises ValueError, so this returns None
        assert _coerce_nonnegative_int("3.5") is None


# ---------------------------------------------------------------------------
# _get_local_queue_depth
# ---------------------------------------------------------------------------
class TestGetLocalQueueDepth:
    """Tests for _get_local_queue_depth with various queue manager shapes."""

    def test_get_total_tracked_preferred(self):
        qm = MagicMock()
        qm.get_total_tracked.return_value = 5
        assert _get_local_queue_depth(qm) == 5

    def test_get_total_tracked_zero(self):
        qm = MagicMock()
        qm.get_total_tracked.return_value = 0
        assert _get_local_queue_depth(qm) == 0

    def test_get_total_tracked_returns_none_falls_to_queue_status(self):
        """When get_total_tracked returns a bool, fall through to get_queue_status."""
        qm = MagicMock()
        qm.get_total_tracked.return_value = True  # bool -> None via coerce
        qm.get_queue_status.return_value = {"total_tracked": 3}
        assert _get_local_queue_depth(qm) == 3

    def test_queue_status_total_tracked(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"total_tracked": 4})
        assert _get_local_queue_depth(qm) == 4

    def test_queue_status_active_queued(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"active": 2, "queued": 3})
        assert _get_local_queue_depth(qm) == 5

    def test_queue_status_active_only(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"active": 2})
        assert _get_local_queue_depth(qm) == 2

    def test_queue_status_queued_only(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"queued": 7})
        assert _get_local_queue_depth(qm) == 7

    def test_queue_status_running_queued_jobs(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"running_jobs": 1, "queued_jobs": 2})
        assert _get_local_queue_depth(qm) == 3

    def test_queue_status_running_jobs_only(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={"running_jobs": 4})
        assert _get_local_queue_depth(qm) == 4

    def test_queue_status_empty_dict_returns_zero(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value={})
        assert _get_local_queue_depth(qm) == 0

    def test_queue_status_returns_none_falls_to_zero(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value=None)
        assert _get_local_queue_depth(qm) == 0

    def test_queue_status_returns_non_dict(self):
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(return_value="not a dict")
        assert _get_local_queue_depth(qm) == 0

    def test_no_methods_returns_zero(self):
        qm = object()  # plain object, no relevant attributes
        assert _get_local_queue_depth(qm) == 0

    def test_priority_total_tracked_over_active_queued(self):
        """total_tracked in status dict takes priority over active/queued."""
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(
            return_value={"total_tracked": 10, "active": 2, "queued": 3}
        )
        assert _get_local_queue_depth(qm) == 10

    def test_priority_active_queued_over_running_queued_jobs(self):
        """active/queued takes priority over running_jobs/queued_jobs."""
        qm = MagicMock(spec=[])
        qm.get_queue_status = MagicMock(
            return_value={"active": 1, "queued": 1, "running_jobs": 99, "queued_jobs": 99}
        )
        assert _get_local_queue_depth(qm) == 2

    def test_get_total_tracked_negative_clamped(self):
        qm = MagicMock()
        qm.get_total_tracked.return_value = -5
        assert _get_local_queue_depth(qm) == 0


# ---------------------------------------------------------------------------
# serialize_job_config
# ---------------------------------------------------------------------------
class TestSerializeJobConfig:
    def _make_job_mock(self, **overrides):
        job = MagicMock()
        defaults = {
            "name": "my-job",
            "data_source": "upload",
            "file_path": "/data/train.csv",
            "dataset_id": None,
            "model_type": ModelType.TABULAR,
            "problem_type": ProblemType.BINARY,
            "target_column": "target",
            "time_column": None,
            "id_column": None,
            "prediction_length": None,
            "preset": "medium_quality",
            "time_limit": 600,
            "eval_metric": "accuracy",
            "autogluon_config": None,
            "enable_mlflow": False,
            "experiment_name": None,
            "project_id": "proj-123",
            "project_name": "My Project",
            "auto_register": False,
            "register_name": None,
        }
        defaults.update(overrides)
        for k, v in defaults.items():
            setattr(job, k, v)
        return job

    def test_basic_tabular_job(self):
        job = self._make_job_mock()
        result = serialize_job_config(job)
        assert result["name"] == "my-job"
        assert result["model_type"] == "tabular"
        assert result["problem_type"] == "binary"
        assert result["target_column"] == "target"
        assert result["file_path"] == "/data/train.csv"
        assert result["dataset_id"] is None
        assert result["time_column"] is None

    def test_timeseries_job(self):
        job = self._make_job_mock(
            model_type=ModelType.TIMESERIES,
            problem_type=None,
            time_column="date",
            id_column="item_id",
            prediction_length=12,
        )
        result = serialize_job_config(job)
        assert result["model_type"] == "timeseries"
        assert result["problem_type"] is None
        assert result["time_column"] == "date"
        assert result["id_column"] == "item_id"
        assert result["prediction_length"] == 12

    def test_mlflow_fields(self):
        job = self._make_job_mock(enable_mlflow=True, experiment_name="exp-1")
        result = serialize_job_config(job)
        assert result["enable_mlflow"] is True
        assert result["experiment_name"] == "exp-1"

    def test_auto_register_fields(self):
        job = self._make_job_mock(auto_register=True, register_name="my-model")
        result = serialize_job_config(job)
        assert result["auto_register"] is True
        assert result["register_name"] == "my-model"

    def test_all_keys_present(self):
        job = self._make_job_mock()
        result = serialize_job_config(job)
        expected_keys = {
            "name", "data_source", "file_path", "dataset_id", "model_type",
            "problem_type", "target_column", "time_column", "id_column",
            "prediction_length", "preset", "time_limit", "eval_metric",
            "autogluon_config", "enable_mlflow", "experiment_name",
            "project_id", "project_name", "auto_register", "register_name",
        }
        assert set(result.keys()) == expected_keys


# ---------------------------------------------------------------------------
# build_job_list_item_response
# ---------------------------------------------------------------------------
class TestBuildJobListItemResponse:
    def _make_job_mock(self, **overrides):
        now = datetime(2025, 1, 15, 12, 0, 0, tzinfo=timezone.utc)
        job = MagicMock()
        defaults = {
            "id": "job-1",
            "name": "Test Job",
            "description": "A test job",
            "owner": "alice",
            "project_id": "proj-1",
            "project_name": "My Project",
            "model_type": ModelType.TABULAR,
            "problem_type": ProblemType.REGRESSION,
            "status": JobStatus.RUNNING,
            "execution_target": "local",
            "domino_job_id": None,
            "domino_job_status": None,
            "progress": 50,
            "current_step": "fitting",
            "data_source": "upload",
            "dataset_id": None,
            "file_path": "/data/train.csv",
            "experiment_name": None,
            "error_message": None,
            "is_registered": False,
            "registered_model_name": None,
            "registered_model_version": None,
            "metrics": {"best_model": "LightGBM", "best_score": 0.95},
            "created_at": now,
            "started_at": now,
            "completed_at": None,
        }
        defaults.update(overrides)
        for k, v in defaults.items():
            setattr(job, k, v)
        return job

    def test_basic_fields(self):
        job = self._make_job_mock()
        resp = build_job_list_item_response(job)
        assert resp.id == "job-1"
        assert resp.name == "Test Job"
        assert resp.owner == "alice"
        assert resp.model_type == "tabular"
        assert resp.problem_type == "regression"
        assert resp.status == "running"
        assert resp.data_source == "upload"

    def test_metrics_extraction(self):
        job = self._make_job_mock(metrics={"best_model": "XGBoost", "best_score": 0.88})
        resp = build_job_list_item_response(job)
        assert resp.best_model_name == "XGBoost"
        assert resp.best_model_score == pytest.approx(0.88)

    def test_metrics_none(self):
        job = self._make_job_mock(metrics=None)
        resp = build_job_list_item_response(job)
        assert resp.best_model_name is None
        assert resp.best_model_score is None

    def test_metrics_empty_dict(self):
        job = self._make_job_mock(metrics={})
        resp = build_job_list_item_response(job)
        assert resp.best_model_name is None
        assert resp.best_model_score is None

    def test_metrics_non_dict(self):
        """When metrics is not a dict (e.g. a string), treat as empty."""
        job = self._make_job_mock(metrics="invalid")
        resp = build_job_list_item_response(job)
        assert resp.best_model_name is None
        assert resp.best_model_score is None

    def test_best_score_non_numeric(self):
        job = self._make_job_mock(metrics={"best_model": "RF", "best_score": "not_a_number"})
        resp = build_job_list_item_response(job)
        assert resp.best_model_name == "RF"
        assert resp.best_model_score is None

    def test_best_score_string_number(self):
        job = self._make_job_mock(metrics={"best_model": "RF", "best_score": "0.75"})
        resp = build_job_list_item_response(job)
        assert resp.best_model_score == pytest.approx(0.75)

    def test_execution_target_defaults_to_local(self):
        job = self._make_job_mock()
        del job.execution_target  # make getattr fall back
        resp = build_job_list_item_response(job)
        assert resp.execution_target == "local"

    def test_domino_execution_target(self):
        job = self._make_job_mock(
            execution_target="domino_job",
            domino_job_id="dj-123",
            domino_job_status="running",
        )
        resp = build_job_list_item_response(job)
        assert resp.execution_target == "domino_job"
        assert resp.domino_job_id == "dj-123"
        assert resp.domino_job_status == "running"

    def test_problem_type_none(self):
        job = self._make_job_mock(problem_type=None)
        resp = build_job_list_item_response(job)
        assert resp.problem_type is None

    def test_is_registered_true(self):
        job = self._make_job_mock(
            is_registered=True,
            registered_model_name="my-model",
            registered_model_version="1",
        )
        resp = build_job_list_item_response(job)
        assert resp.is_registered is True
        assert resp.registered_model_name == "my-model"
        assert resp.registered_model_version == "1"

    def test_completed_job(self):
        completed_at = datetime(2025, 1, 15, 13, 0, 0, tzinfo=timezone.utc)
        job = self._make_job_mock(
            status=JobStatus.COMPLETED,
            completed_at=completed_at,
            progress=100,
        )
        resp = build_job_list_item_response(job)
        assert resp.status == "completed"
        assert resp.completed_at == completed_at
        assert resp.progress == 100


# ---------------------------------------------------------------------------
# _is_job_name_unique_violation
# ---------------------------------------------------------------------------
class TestIsJobNameUniqueViolation:
    def _make_exc(self, orig_message: str) -> IntegrityError:
        """Build an IntegrityError with a given orig message."""
        orig = Exception(orig_message)
        exc = IntegrityError(statement="INSERT INTO jobs", params={}, orig=orig)
        return exc

    def test_exact_constraint_name(self):
        exc = self._make_exc("uq_jobs_owner_project_name_ci")
        assert _is_job_name_unique_violation(exc) is True

    def test_generic_unique_constraint_with_jobs_and_name(self):
        exc = self._make_exc("UNIQUE constraint failed: jobs.name")
        assert _is_job_name_unique_violation(exc) is True

    def test_unique_constraint_without_jobs(self):
        exc = self._make_exc("UNIQUE constraint failed: other_table.name")
        assert _is_job_name_unique_violation(exc) is False

    def test_unique_constraint_without_name(self):
        exc = self._make_exc("UNIQUE constraint failed: jobs.email")
        assert _is_job_name_unique_violation(exc) is False

    def test_unrelated_integrity_error(self):
        exc = self._make_exc("NOT NULL constraint failed: jobs.owner")
        assert _is_job_name_unique_violation(exc) is False

    def test_case_insensitive_matching(self):
        exc = self._make_exc("UQ_JOBS_OWNER_PROJECT_NAME_CI")
        assert _is_job_name_unique_violation(exc) is True

    def test_constraint_name_embedded_in_longer_message(self):
        exc = self._make_exc(
            '(psycopg2.errors.UniqueViolation) duplicate key value violates '
            'unique constraint "uq_jobs_owner_project_name_ci"'
        )
        assert _is_job_name_unique_violation(exc) is True
