"""Tests for app.services.job_service helper functions."""

import uuid
from pathlib import Path
from typing import Optional
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio
from fastapi import HTTPException

from app.api.schemas.job import (
    AdvancedAutoGluonConfig,
    JobCreateRequest,
    JobListRequest,
    TimeSeriesAdvancedConfig,
)
from app.db.models import Job, JobStatus, ModelType, ProblemType
from app.services.job_service import (
    _count_active_domino_jobs,
    _is_domino_missing_error,
    _is_domino_terminal_status,
    _normalize_job_name,
    _parse_statuses_csv,
    _terminal_status_from_domino,
    build_autogluon_config,
    build_job_model,
    create_job_with_context,
    extract_metrics_leaderboard,
    get_queue_status,
    get_request_owner,
    normalize_job_leaderboard,
    resolve_execution_target,
    resolve_job_list_filters,
    validate_job_create_request,
    validate_job_name_availability,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_create_request(**overrides) -> JobCreateRequest:
    """Build a minimal JobCreateRequest with sensible defaults."""
    defaults = {
        "name": "test-job",
        "model_type": "tabular",
        "data_source": "upload",
        "target_column": "target",
        "file_path": "/tmp/data.csv",
    }
    defaults.update(overrides)
    return JobCreateRequest(**defaults)


def _make_list_request(**overrides) -> JobListRequest:
    """Build a minimal JobListRequest with sensible defaults."""
    return JobListRequest(**overrides)


def _fake_request(headers: Optional[dict] = None) -> MagicMock:
    """Build a mock FastAPI Request with configurable headers."""
    req = MagicMock()
    req.headers = headers or {}
    return req


# ===========================================================================
# validate_job_create_request
# ===========================================================================


class TestValidateJobCreateRequest:
    """Tests for validate_job_create_request."""

    def test_domino_dataset_requires_dataset_id(self):
        req = _make_create_request(data_source="domino_dataset", dataset_id=None)
        with pytest.raises(HTTPException) as exc_info:
            validate_job_create_request(req)
        assert exc_info.value.status_code == 400
        assert "dataset_id" in exc_info.value.detail

    def test_domino_dataset_ok_with_dataset_id(self):
        req = _make_create_request(data_source="domino_dataset", dataset_id="ds-123")
        validate_job_create_request(req)  # should not raise

    def test_upload_requires_file_path(self):
        req = _make_create_request(data_source="upload", file_path=None)
        with pytest.raises(HTTPException) as exc_info:
            validate_job_create_request(req)
        assert exc_info.value.status_code == 400
        assert "file_path" in exc_info.value.detail

    def test_upload_ok_with_file_path(self):
        req = _make_create_request(data_source="upload", file_path="/data/test.csv")
        validate_job_create_request(req)  # should not raise

    def test_timeseries_requires_time_column(self):
        req = _make_create_request(
            model_type="timeseries",
            time_column=None,
            prediction_length=10,
        )
        with pytest.raises(HTTPException) as exc_info:
            validate_job_create_request(req)
        assert exc_info.value.status_code == 400
        assert "time_column" in exc_info.value.detail

    def test_timeseries_requires_prediction_length(self):
        req = _make_create_request(
            model_type="timeseries",
            time_column="date",
            prediction_length=None,
        )
        with pytest.raises(HTTPException) as exc_info:
            validate_job_create_request(req)
        assert exc_info.value.status_code == 400
        assert "prediction_length" in exc_info.value.detail

    def test_timeseries_ok_with_both(self):
        req = _make_create_request(
            model_type="timeseries",
            time_column="date",
            prediction_length=10,
        )
        validate_job_create_request(req)  # should not raise

    def test_tabular_upload_ok(self):
        req = _make_create_request()
        validate_job_create_request(req)  # should not raise


# ===========================================================================
# validate_job_name_availability
# ===========================================================================


class TestValidateJobNameAvailability:
    """Tests for validate_job_name_availability (async, uses db_session)."""

    @pytest.mark.asyncio
    async def test_empty_name_rejected(self, db_session):
        with pytest.raises(HTTPException) as exc_info:
            await validate_job_name_availability(
                db=db_session,
                name="   ",
                owner="alice",
                project_id=None,
                project_name="proj",
            )
        assert exc_info.value.status_code == 400
        assert "blank" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_unique_name_succeeds(self, db_session):
        result = await validate_job_name_availability(
            db=db_session,
            name="brand-new-job",
            owner="alice",
            project_id=None,
            project_name="proj",
        )
        assert result == "brand-new-job"

    @pytest.mark.asyncio
    async def test_duplicate_name_raises_409(self, db_session, make_job):
        job = make_job(name="duplicate-job", owner="alice", project_name="proj")
        db_session.add(job)
        await db_session.commit()

        with pytest.raises(HTTPException) as exc_info:
            await validate_job_name_availability(
                db=db_session,
                name="duplicate-job",
                owner="alice",
                project_id=None,
                project_name="proj",
            )
        assert exc_info.value.status_code == 409

    @pytest.mark.asyncio
    async def test_strips_whitespace_before_check(self, db_session):
        result = await validate_job_name_availability(
            db=db_session,
            name="  hello-job  ",
            owner="alice",
            project_id=None,
            project_name="proj",
        )
        assert result == "hello-job"


# ===========================================================================
# _normalize_job_name
# ===========================================================================


class TestNormalizeJobName:
    """Tests for _normalize_job_name."""

    def test_strips_leading_whitespace(self):
        assert _normalize_job_name("  hello") == "hello"

    def test_strips_trailing_whitespace(self):
        assert _normalize_job_name("hello  ") == "hello"

    def test_strips_both(self):
        assert _normalize_job_name("  hello  ") == "hello"

    def test_no_op_on_clean_string(self):
        assert _normalize_job_name("hello") == "hello"

    def test_empty_string(self):
        assert _normalize_job_name("") == ""


# ===========================================================================
# build_autogluon_config
# ===========================================================================


class TestBuildAutogluonConfig:
    """Tests for build_autogluon_config."""

    def test_returns_none_when_nothing_set(self):
        req = _make_create_request()
        assert build_autogluon_config(req) is None

    def test_includes_advanced_config(self):
        adv = AdvancedAutoGluonConfig(num_gpus=1, verbosity=3)
        req = _make_create_request(advanced_config=adv)
        result = build_autogluon_config(req)
        assert "advanced" in result
        assert result["advanced"]["num_gpus"] == 1
        assert result["advanced"]["verbosity"] == 3

    def test_includes_timeseries_config(self):
        ts_cfg = TimeSeriesAdvancedConfig(freq="D")
        req = _make_create_request(
            model_type="timeseries",
            time_column="date",
            prediction_length=10,
            timeseries_config=ts_cfg,
        )
        result = build_autogluon_config(req)
        assert "timeseries" in result
        assert result["timeseries"]["freq"] == "D"

    def test_includes_feature_columns(self):
        req = _make_create_request(feature_columns=["age", "income"])
        result = build_autogluon_config(req)
        assert result["feature_columns"] == ["age", "income"]

    def test_combines_all_sections(self):
        adv = AdvancedAutoGluonConfig(num_gpus=2)
        ts_cfg = TimeSeriesAdvancedConfig(freq="H")
        req = _make_create_request(
            model_type="timeseries",
            time_column="date",
            prediction_length=5,
            advanced_config=adv,
            timeseries_config=ts_cfg,
            feature_columns=["col_a"],
        )
        result = build_autogluon_config(req)
        assert "advanced" in result
        assert "timeseries" in result
        assert "feature_columns" in result


# ===========================================================================
# build_job_model
# ===========================================================================


class TestBuildJobModel:
    """Tests for build_job_model."""

    def test_basic_field_mapping(self):
        req = _make_create_request(
            name="my-job",
            description="a training run",
            data_source="upload",
            file_path="/tmp/data.csv",
            target_column="target",
            preset="best_quality",
            time_limit=120,
            eval_metric="accuracy",
            experiment_name="exp-1",
        )
        job = build_job_model(
            job_request=req,
            job_name="my-job",
            owner="bob",
            project_id="pid-1",
            project_name="my-proj",
        )
        assert isinstance(job, Job)
        assert job.name == "my-job"
        assert job.description == "a training run"
        assert job.owner == "bob"
        assert job.project_id == "pid-1"
        assert job.project_name == "my-proj"
        assert job.model_type == ModelType.TABULAR
        assert job.data_source == "upload"
        assert job.file_path == "/tmp/data.csv"
        assert job.target_column == "target"
        assert job.preset == "best_quality"
        assert job.time_limit == 120
        assert job.eval_metric == "accuracy"
        assert job.experiment_name == "exp-1"
        assert job.status == JobStatus.PENDING

    def test_timeseries_fields(self):
        req = _make_create_request(
            model_type="timeseries",
            time_column="ts",
            id_column="item_id",
            prediction_length=14,
        )
        job = build_job_model(req, "ts-job", "alice", None, None)
        assert job.model_type == ModelType.TIMESERIES
        assert job.time_column == "ts"
        assert job.id_column == "item_id"
        assert job.prediction_length == 14

    def test_execution_target_domino_job(self):
        req = _make_create_request(execution_target="domino_job")
        job = build_job_model(req, "job", "user", None, None)
        assert job.execution_target == "domino_job"

    def test_execution_target_defaults_to_local(self):
        req = _make_create_request()
        job = build_job_model(req, "job", "user", None, None)
        assert job.execution_target == "domino_job"

    def test_autogluon_config_stored(self):
        adv = AdvancedAutoGluonConfig(num_gpus=1)
        req = _make_create_request(advanced_config=adv)
        job = build_job_model(req, "job", "user", None, None)
        assert job.autogluon_config is not None
        assert "advanced" in job.autogluon_config


# ===========================================================================
# resolve_execution_target
# ===========================================================================


class TestResolveExecutionTarget:
    """Tests for resolve_execution_target."""

    def test_local_default(self):
        req = _make_create_request()
        assert resolve_execution_target(req) == "local"

    def test_explicit_domino_job(self):
        req = _make_create_request(execution_target="domino_job")
        assert resolve_execution_target(req) == "domino_job"

    def test_legacy_run_as_domino_job_flag(self):
        req = _make_create_request(run_as_domino_job=True)
        assert resolve_execution_target(req) == "domino_job"

    def test_legacy_flag_false_stays_local(self):
        req = _make_create_request(run_as_domino_job=False)
        assert resolve_execution_target(req) == "local"


# ===========================================================================
# resolve_job_list_filters
# ===========================================================================


class TestResolveJobListFilters:
    """Tests for resolve_job_list_filters."""

    def test_all_none_without_request(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request()
        status, model_type, owner, pid, pname = resolve_job_list_filters(lr, None)
        assert status is None
        assert model_type is None
        assert owner is None
        assert pid is None
        assert pname is None

    def test_status_filter_parsed(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(status="completed")
        status, *_ = resolve_job_list_filters(lr, None)
        assert status == JobStatus.COMPLETED

    def test_model_type_filter_parsed(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(model_type="timeseries")
        _, model_type, *_ = resolve_job_list_filters(lr, None)
        assert model_type == ModelType.TIMESERIES

    def test_owner_from_list_request(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(owner="alice")
        _, _, owner, *_ = resolve_job_list_filters(lr, None)
        assert owner == "alice"

    def test_owner_from_http_request_header(self, monkeypatch):
        from app.core.context import user as user_ctx

        def fake_get_viewing_user():
            return user_ctx.User(id="test-id", user_name="bob", roles=["SysAdmin", "Practitioner"])

        import app.services.job_service as job_service
        monkeypatch.setattr(job_service, "get_viewing_user", fake_get_viewing_user, raising=True)

        lr = _make_list_request()
        request = _fake_request(headers={"domino-username": "bob"})
        _, _, owner, *_ = resolve_job_list_filters(lr, request)
        assert owner == "bob"

    def test_owner_explicit_empty_string_gives_none(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(owner="")
        _, _, owner, *_ = resolve_job_list_filters(lr, None)
        assert owner is None

    def test_project_name_filter(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(project_name="my-proj")
        *_, pname = resolve_job_list_filters(lr, None)
        assert pname == "my-proj"

    def test_project_id_filter(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(project_id="pid-42")
        _, _, _, pid, _ = resolve_job_list_filters(lr, None)
        assert pid == "pid-42"


# ===========================================================================
# _terminal_status_from_domino
# ===========================================================================


class TestTerminalStatusFromDomino:
    """Tests for _terminal_status_from_domino."""

    @pytest.mark.parametrize(
        "domino_status,expected",
        [
            ("Succeeded", JobStatus.COMPLETED),
            ("succeeded", JobStatus.COMPLETED),
            ("success", JobStatus.COMPLETED),
            ("completed", JobStatus.COMPLETED),
            ("done", JobStatus.COMPLETED),
            ("finished", JobStatus.COMPLETED),
            ("Failed", JobStatus.FAILED),
            ("error", JobStatus.FAILED),
            ("Stopped", JobStatus.CANCELLED),
            ("cancelled", JobStatus.CANCELLED),
            ("canceled", JobStatus.CANCELLED),
            ("archived", JobStatus.CANCELLED),
        ],
    )
    def test_known_mappings(self, domino_status, expected):
        assert _terminal_status_from_domino(domino_status) == expected

    def test_none_returns_none(self):
        assert _terminal_status_from_domino(None) is None

    def test_empty_returns_none(self):
        assert _terminal_status_from_domino("") is None

    def test_unknown_status_returns_none(self):
        assert _terminal_status_from_domino("in-progress") is None

    def test_whitespace_trimmed(self):
        assert _terminal_status_from_domino("  succeeded  ") == JobStatus.COMPLETED


# ===========================================================================
# _is_domino_terminal_status
# ===========================================================================


class TestIsDominoTerminalStatus:
    """Tests for _is_domino_terminal_status."""

    @pytest.mark.parametrize(
        "status",
        ["succeeded", "failed", "stopped", "cancelled", "error", "done"],
    )
    def test_terminal_statuses(self, status):
        assert _is_domino_terminal_status(status) is True

    @pytest.mark.parametrize(
        "status",
        ["running", "submitted", "queued", "pending", "initializing", None, ""],
    )
    def test_non_terminal_statuses(self, status):
        assert _is_domino_terminal_status(status) is False


# ===========================================================================
# _is_domino_missing_error
# ===========================================================================


class TestIsDominoMissingError:
    """Tests for _is_domino_missing_error."""

    @pytest.mark.parametrize(
        "error",
        [
            "404 Not Found",
            "Run not found",
            "Run does not exist",
            "unknown run id abc",
            "no run with that id",
            "This job was archived",
        ],
    )
    def test_detected_as_missing(self, error):
        assert _is_domino_missing_error(error) is True

    def test_none_returns_false(self):
        assert _is_domino_missing_error(None) is False

    def test_empty_returns_false(self):
        assert _is_domino_missing_error("") is False

    def test_whitespace_only_returns_false(self):
        assert _is_domino_missing_error("   ") is False

    def test_generic_error_returns_false(self):
        assert _is_domino_missing_error("timeout connecting to server") is False


# ===========================================================================
# normalize_job_leaderboard
# ===========================================================================


class TestNormalizeJobLeaderboard:
    """Tests for normalize_job_leaderboard."""

    def test_dict_with_models_key_unwrapped(self, make_job):
        models_list = [{"model": "LightGBM", "score": 0.95}]
        job = make_job(leaderboard={"models": models_list})
        result = normalize_job_leaderboard(job)
        assert result.leaderboard == models_list

    def test_already_list_unchanged(self, make_job):
        models_list = [{"model": "XGBoost", "score": 0.90}]
        job = make_job(leaderboard=models_list)
        result = normalize_job_leaderboard(job)
        assert result.leaderboard == models_list

    def test_none_leaderboard_unchanged(self, make_job):
        job = make_job(leaderboard=None)
        result = normalize_job_leaderboard(job)
        assert result.leaderboard is None

    def test_dict_without_models_key_unchanged(self, make_job):
        payload = {"summary": "no models key"}
        job = make_job(leaderboard=payload)
        result = normalize_job_leaderboard(job)
        assert result.leaderboard == payload


# ===========================================================================
# extract_metrics_leaderboard
# ===========================================================================


class TestExtractMetricsLeaderboard:
    """Tests for extract_metrics_leaderboard."""

    def test_dict_with_models_key(self, make_job):
        models = [{"model": "RF", "score": 0.88}]
        job = make_job(leaderboard={"models": models})
        assert extract_metrics_leaderboard(job) == models

    def test_dict_without_models_key_returns_empty(self, make_job):
        job = make_job(leaderboard={"other": "data"})
        assert extract_metrics_leaderboard(job) == []

    def test_list_returned_directly(self, make_job):
        models = [{"model": "CatBoost"}]
        job = make_job(leaderboard=models)
        assert extract_metrics_leaderboard(job) == models

    def test_none_returns_none(self, make_job):
        job = make_job(leaderboard=None)
        assert extract_metrics_leaderboard(job) is None


# ===========================================================================
# get_request_owner
# ===========================================================================


class TestGetRequestOwner:
    """Tests for get_request_owner."""

    def test_from_header_when_no_viewing_user(self, monkeypatch):
        # Without a viewing user available, header should be used
        monkeypatch.setattr(
            "app.services.job_service.get_viewing_user", lambda: None
        )
        req = _fake_request(headers={"domino-username": "charlie"})
        assert get_request_owner(req) == "charlie"

    def test_missing_header_returns_anonymous_when_no_viewing_user(self, monkeypatch):
        monkeypatch.setattr(
            "app.services.job_service.get_viewing_user", lambda: None
        )
        req = _fake_request(headers={})
        assert get_request_owner(req) == "anonymous"

    def test_none_request_returns_anonymous_when_no_viewing_user(self, monkeypatch):
        monkeypatch.setattr(
            "app.services.job_service.get_viewing_user", lambda: None
        )
        assert get_request_owner(None) == "anonymous"


# ===========================================================================
# _parse_statuses_csv
# ===========================================================================


class TestParseStatusesCsv:
    """Tests for _parse_statuses_csv."""

    def test_single_status(self):
        result = _parse_statuses_csv("failed")
        assert result == [JobStatus.FAILED]

    def test_multiple_statuses(self):
        result = _parse_statuses_csv("failed,cancelled")
        assert result == [JobStatus.FAILED, JobStatus.CANCELLED]

    def test_whitespace_trimmed(self):
        result = _parse_statuses_csv("  failed , completed ")
        assert result == [JobStatus.FAILED, JobStatus.COMPLETED]

    def test_all_statuses(self):
        result = _parse_statuses_csv("pending,running,completed,failed,cancelled")
        assert len(result) == 5
        assert JobStatus.PENDING in result
        assert JobStatus.RUNNING in result

    def test_invalid_status_raises(self):
        with pytest.raises(ValueError):
            _parse_statuses_csv("invalid_status")


# ===========================================================================
# Queue capacity enforcement (429)
# ===========================================================================


class TestQueueCapacity:
    """Tests for rate-limiting in create_job_with_context."""

    def _mock_settings(self, **overrides):
        """Build a settings mock with safe defaults for DB-interacting tests."""
        defaults = dict(
            max_local_queue_size=10,
            max_domino_queue_size=20,
            domino_project_id=None,
            domino_project_name=None,
        )
        defaults.update(overrides)
        return MagicMock(**defaults)

    @pytest.mark.asyncio
    async def test_local_queue_full_returns_429(self, db_session, mock_viewing_user):
        mock_viewing_user
        req = _make_create_request()
        with (
            patch("app.core.job_queue.get_job_queue") as mock_queue,
            patch("app.services.job_service.get_settings") as mock_get_settings,
        ):
            mock_get_settings.return_value = self._mock_settings(max_local_queue_size=5)
            mock_queue.return_value.get_total_tracked.return_value = 5

            with pytest.raises(HTTPException) as exc_info:
                await create_job_with_context(db_session, req)
            assert exc_info.value.status_code == 429
            assert "local" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_domino_queue_full_returns_429(self, db_session, mock_viewing_user):
        mock_viewing_user
        req = _make_create_request(execution_target="domino_job")
        with (
            patch(
                "app.services.job_service._count_active_domino_jobs",
                new_callable=AsyncMock,
                return_value=20,
            ),
            patch("app.services.job_service.get_settings") as mock_get_settings,
        ):
            mock_get_settings.return_value = self._mock_settings(max_domino_queue_size=20)

            with pytest.raises(HTTPException) as exc_info:
                await create_job_with_context(db_session, req)
            assert exc_info.value.status_code == 429
            assert "domino" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_local_queue_under_limit_proceeds(self, db_session, mock_viewing_user):
        """When the local queue is under the limit, the job should be created."""
        mock_viewing_user
        req = _make_create_request()
        with (
            patch("app.core.job_queue.get_job_queue") as mock_queue,
            patch("app.services.job_service.get_settings") as mock_get_settings,
            patch("app.services.job_service.crud") as mock_crud,
        ):
            mock_get_settings.return_value = self._mock_settings()
            mock_queue.return_value.get_total_tracked.return_value = 3
            mock_queue.return_value.enqueue = AsyncMock()

            fake_job = MagicMock()
            fake_job.id = "job-123"
            fake_job.execution_target = "local"
            mock_crud.create_job = AsyncMock(return_value=fake_job)
            mock_crud.get_job_by_scoped_name = AsyncMock(return_value=None)

            result = await create_job_with_context(db_session, req)
            assert result is not None

    @pytest.mark.asyncio
    async def test_bad_input_returns_400_not_429(self, db_session, mock_viewing_user):
        """Validation errors (400) should fire before capacity checks (429)."""
        mock_viewing_user
        req = _make_create_request(data_source="domino_dataset", dataset_id=None)
        # Even if queue is "full", bad input gets 400
        with pytest.raises(HTTPException) as exc_info:
            await create_job_with_context(db_session, req)
        assert exc_info.value.status_code == 400


# ===========================================================================
# get_queue_status includes limits
# ===========================================================================


class TestGetQueueStatusLimits:
    """Tests for queue status response including capacity limits."""

    def test_queue_status_includes_limits(self):
        with (
            patch("app.core.job_queue.get_job_queue") as mock_queue,
            patch("app.services.job_service.get_settings") as mock_get_settings,
        ):
            mock_queue.return_value.get_queue_status.return_value = {
                "max_concurrent_jobs": 2,
                "running_jobs": 1,
                "queued_jobs": 0,
                "total_tracked": 1,
                "shutting_down": False,
            }
            mock_get_settings.return_value = MagicMock(
                max_local_queue_size=10,
                max_domino_queue_size=20,
            )

            status = get_queue_status()
            assert status["max_local_queue_size"] == 10
            assert status["max_domino_queue_size"] == 20
            assert "running_jobs" in status
