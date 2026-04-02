"""Tests for app.services.job_service helper functions."""

from datetime import datetime, timezone
from typing import Optional
from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest
from fastapi import HTTPException

from app.api.generated.domino_public_api_client.models.job_logs_v1 import JobLogsV1
from app.api.generated.domino_public_api_client.models.log_content_v1 import LogContentV1
from app.api.generated.domino_public_api_client.models.log_type_v1 import LogTypeV1
from app.api.generated.domino_public_api_client.models.logs_envelope_v1 import LogsEnvelopeV1
from app.api.generated.domino_public_api_client.models.logs_envelope_v1_metadata import LogsEnvelopeV1Metadata
from app.api.generated.domino_public_api_client.models.logs_pagination_v1 import LogsPaginationV1
from app.api.schemas.job import (
    AdvancedAutoGluonConfig,
    JobCreateRequest,
    JobListRequest,
    TimeSeriesAdvancedConfig,
)
from app.db.models import Job, JobLog, JobStatus, ModelType, ProblemType
from app.services.job_service import (
    _build_domino_job_logs,
    _ensure_mlflow_results,
    _is_domino_missing_error,
    _is_domino_terminal_status,
    _normalize_job_name,
    _parse_statuses_csv,
    _terminal_status_from_domino,
    build_autogluon_config,
    build_job_config,
    build_job_model,
    bulk_delete_jobs,
    cancel_job,
    create_job_with_context,
    delete_job,
    extract_metrics_leaderboard,
    get_job_logs,
    get_job_or_404,
    normalize_job_leaderboard,
    resolve_job_list_filters,
    validate_job_create_request,
    validate_job_name_availability,
)
from app.services.models import JobConfig


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

    def test_autogluon_config_stored(self):
        adv = AdvancedAutoGluonConfig(num_gpus=1)
        req = _make_create_request(advanced_config=adv)
        job = build_job_model(req, "job", "user", None, None)
        assert job.autogluon_config is not None
        assert "advanced" in job.autogluon_config


class TestBuildJobConfig:
    """Tests for JobConfig transport model construction."""

    def test_builds_pydantic_model_from_job(self, make_job):
        job = make_job(
            name="transport-job",
            model_type=ModelType.TABULAR,
            problem_type=ProblemType.BINARY,
            dataset_id="dataset-1",
        )

        job_config = build_job_config(job)

        assert isinstance(job_config, JobConfig)
        assert job_config.id == job.id
        assert job_config.name == "transport-job"
        assert job_config.model_type == ModelType.TABULAR
        assert job_config.problem_type == ProblemType.BINARY
        assert job_config.dataset_id == "dataset-1"

        dumped = job_config.model_dump(mode="json")
        assert dumped["model_type"] == "tabular"
        assert dumped["problem_type"] == "binary"

    def test_allows_overriding_file_path(self, make_job):
        job = make_job(file_path="/tmp/original.csv")

        job_config = build_job_config(job, file_path="/mnt/data/train.csv")

        assert job_config.file_path == "/mnt/data/train.csv"


class TestResolveJobListFilters:
    """Tests for resolve_job_list_filters."""

    def test_all_none_without_request(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request()
        status, model_type, owner, pid, pname = resolve_job_list_filters(lr)
        assert status is None
        assert model_type is None
        assert owner == "test-user"
        assert pid is None
        assert pname is None

    def test_status_filter_parsed(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(status="completed")
        status, *_ = resolve_job_list_filters(lr)
        assert status == JobStatus.COMPLETED

    def test_model_type_filter_parsed(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(model_type="timeseries")
        _, model_type, *_ = resolve_job_list_filters(lr)
        assert model_type == ModelType.TIMESERIES

    def test_owner_from_list_request(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(owner="alice")
        _, _, owner, *_ = resolve_job_list_filters(lr)
        assert owner == "alice"

    def test_owner_from_http_request_header(self, monkeypatch):
        from app.core.context import user as user_ctx

        def fake_get_viewing_user():
            return user_ctx.User(id="test-id", user_name="bob", roles=["SysAdmin", "Practitioner"])

        import app.services.job_service as job_service
        monkeypatch.setattr(job_service, "get_viewing_user", fake_get_viewing_user, raising=True)

        lr = _make_list_request()
        _, _, owner, *_ = resolve_job_list_filters(lr)
        assert owner == "bob"

    def test_owner_explicit_empty_string_gives_none(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(owner="")
        _, _, owner, *_ = resolve_job_list_filters(lr)
        assert owner is None

    def test_project_name_filter(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(project_name="my-proj")
        *_, pname = resolve_job_list_filters(lr)
        assert pname == "my-proj"

    def test_project_id_filter(self, mock_viewing_user):
        mock_viewing_user
        lr = _make_list_request(project_id="pid-42")
        _, _, _, pid, _ = resolve_job_list_filters(lr)
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
# create_job_with_context authorization
# ===========================================================================


class TestCreateJobAuthorization:
    """Tests for authorization gates in create_job_with_context."""

    @pytest.mark.asyncio
    async def test_domino_job_launch_requires_start_permission(self, db_session, mock_viewing_user):
        mock_viewing_user
        req = _make_create_request()

        with (
            patch(
                "app.services.job_service.require_domino_job_start",
                side_effect=HTTPException(
                    status_code=403,
                    detail="This operation requires permission to start jobs in the target project",
                ),
            ) as mock_require_start,
            patch("app.services.job_service.get_settings") as mock_get_settings,
            patch(
                "app.services.job_service._count_active_domino_jobs",
                new_callable=AsyncMock,
            ) as mock_count_active_domino_jobs,
            patch(
                "app.services.job_service.crud.create_job",
                new_callable=AsyncMock,
            ) as mock_create_job,
        ):
            mock_get_settings.return_value = MagicMock(
                max_local_queue_size=10,
                max_domino_queue_size=20,
                domino_project_id=None,
                domino_project_name=None,
            )

            with pytest.raises(HTTPException) as exc_info:
                await create_job_with_context(
                    db_session,
                    req,
                    project_id="proj-1",
                    project_name="my-proj",
                    project_owner="owner",
                )

            assert exc_info.value.status_code == 403
            mock_require_start.assert_called_once_with(project_id="proj-1")

            mock_count_active_domino_jobs.assert_not_awaited()
            mock_create_job.assert_not_awaited()


# ===========================================================================
# Queue capacity enforcement (429)
# ===========================================================================


class TestQueueCapacity:
    """Tests for rate-limiting in create_job_with_context."""

    def _mock_settings(self, **overrides):
        """Build a settings mock with safe defaults for DB-interacting tests."""
        defaults = dict(
            max_domino_queue_size=20,
            domino_project_id=None,
            domino_project_name=None,
        )
        defaults.update(overrides)
        return MagicMock(**defaults)

    @pytest.mark.asyncio
    async def test_domino_queue_full_returns_429(self, db_session, mock_viewing_user):
        mock_viewing_user
        req = _make_create_request()
        with (
            patch(
                "app.services.job_service._count_active_domino_jobs",
                new_callable=AsyncMock,
                return_value=20,
            ),
            patch("app.services.job_service.require_domino_job_start"),
            patch("app.services.job_service.get_settings") as mock_get_settings,
        ):
            mock_get_settings.return_value = self._mock_settings(max_domino_queue_size=20)

            with pytest.raises(HTTPException) as exc_info:
                await create_job_with_context(
                    db_session, req,
                    project_id="proj-1", project_name="my-proj", project_owner="owner",
                )
            assert exc_info.value.status_code == 429
            assert "domino" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_bad_input_returns_400_not_429(self, db_session, mock_viewing_user):
        """Validation errors (400) should fire before capacity checks (429)."""
        mock_viewing_user
        req = _make_create_request(data_source="domino_dataset", dataset_id=None)
        with pytest.raises(HTTPException) as exc_info:
            await create_job_with_context(
                db_session, req,
                project_id="proj-1", project_name="my-proj", project_owner="owner",
            )
        assert exc_info.value.status_code == 400


# ===========================================================================
# cancel_job
# ===========================================================================


class TestCancelJob:
    """Tests for cancel_job."""

    @pytest.mark.asyncio
    async def test_domino_job_cancel_calls_stop_authorization(
        self,
        db_session,
        make_job,
        mock_viewing_user,
    ):
        mock_viewing_user
        job = make_job(
            status=JobStatus.PENDING,
            domino_job_id="run-123",
            project_id="proj-1",
        )
        db_session.add(job)
        await db_session.commit()

        fake_launcher = MagicMock()
        fake_launcher.stop_job = AsyncMock(return_value={"success": True})

        with (
            patch("app.services.job_service._fetch_domino_job_or_throw"),
            patch("app.services.job_service.require_domino_job_stop") as mock_require_stop,
            patch("app.services.job_service.get_domino_job_launcher", return_value=fake_launcher),
            patch(
                "app.services.job_service.crud.update_job_domino_fields",
                new_callable=AsyncMock,
            ) as mock_update_domino_fields,
            patch(
                "app.services.job_service.crud.update_job_status",
                new_callable=AsyncMock,
            ) as mock_update_status,
        ):
            result = await cancel_job(db_session, job.id)

        assert result["message"] == "Job cancelled"
        assert result["external_cancelled"] is True
        mock_require_stop.assert_called_once_with("run-123")
        fake_launcher.stop_job.assert_awaited_once_with("run-123", project_id="proj-1")
        mock_update_domino_fields.assert_awaited_once()
        mock_update_status.assert_awaited_once()


# ===========================================================================
# delete_job / bulk_delete_jobs
# ===========================================================================


class TestDeleteJob:
    """Tests for delete_job."""

    @pytest.mark.asyncio
    async def test_delete_job_calls_owner_check(
        self,
        db_session,
        make_job,
        mock_viewing_user,
    ):
        mock_viewing_user
        job = make_job(domino_job_id="run-123")
        cleanup_service = MagicMock()
        cleanup_service.delete_job_artifacts = AsyncMock(return_value={"deleted_files": 1})

        with (
            patch(
                "app.services.job_service.require_user_owns_local_job",
                new_callable=AsyncMock,
            ) as mock_require_owner,
            patch(
                "app.services.job_service.get_job_or_404",
                new_callable=AsyncMock,
                return_value=job,
            ),
            patch(
                "app.core.cleanup_service.get_cleanup_service",
                return_value=cleanup_service,
            ),
            patch(
                "app.services.job_service.crud.delete_job",
                new_callable=AsyncMock,
            ) as mock_delete_job,
        ):
            result = await delete_job(db_session, job.id)

        assert result["message"] == "Job deleted"
        assert result["job_id"] == job.id
        mock_require_owner.assert_awaited_once_with(db_session, job.id)
        cleanup_service.delete_job_artifacts.assert_awaited_once_with(job, db_session)
        mock_delete_job.assert_awaited_once_with(db_session, job.id)


class TestBulkDeleteJobs:
    """Tests for bulk_delete_jobs."""

    @pytest.mark.asyncio
    async def test_bulk_delete_jobs_calls_owner_check_per_job(
        self,
        db_session,
        make_job,
        mock_viewing_user,
    ):
        mock_viewing_user
        job1 = make_job(name="job-1", status=JobStatus.COMPLETED)
        job2 = make_job(name="job-2", status=JobStatus.COMPLETED)
        cleanup_service = MagicMock()
        cleanup_service.delete_job_artifacts = AsyncMock(side_effect=[{"deleted_files": 1}, {"deleted_files": 2}])

        with (
            patch(
                "app.services.job_service.require_user_owns_local_job",
                new_callable=AsyncMock,
            ) as mock_require_owner,
            patch(
                "app.services.job_service.crud.get_job",
                new_callable=AsyncMock,
                side_effect=[job1, job2],
            ),
            patch(
                "app.core.cleanup_service.get_cleanup_service",
                return_value=cleanup_service,
            ),
            patch(
                "app.services.job_service.crud.delete_job",
                new_callable=AsyncMock,
            ) as mock_delete_job,
        ):
            result = await bulk_delete_jobs(db_session, [job1.id, job2.id])

        assert result["deleted_job_ids"] == [job1.id, job2.id]
        assert result["failed"] == []
        assert mock_require_owner.await_args_list == [
            call(db_session, job1.id),
            call(db_session, job2.id),
        ]
        assert cleanup_service.delete_job_artifacts.await_args_list == [
            call(job1, db_session),
            call(job2, db_session),
        ]
        assert mock_delete_job.await_args_list == [
            call(db_session, job1.id),
            call(db_session, job2.id),
        ]


# ===========================================================================
# get_job_or_404
# ===========================================================================


class TestGetJobOr404:
    """Tests for fetching jobs with optional Domino validation."""

    @pytest.mark.asyncio
    async def test_raises_500_when_no_domino_job_id(self, db_session, make_job):
        job = make_job()
        db_session.add(job)
        await db_session.commit()

        with pytest.raises(HTTPException) as exc_info:
            await get_job_or_404(db_session, job.id, "test-user")

        assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_fetches_domino_job_when_domino_job_id_present(self, db_session, make_job):
        job = make_job(domino_job_id="run-123")
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_domino_job_or_throw",
            new_callable=MagicMock,
        ) as mock_fetch:
            result = await get_job_or_404(db_session, job.id, "test-user")

        assert result.id == job.id
        mock_fetch.assert_called_once_with("run-123")

    @pytest.mark.asyncio
    async def test_propagates_domino_fetch_error(self, db_session, make_job):
        job = make_job(domino_job_id="run-123")
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_domino_job_or_throw",
            new_callable=MagicMock,
            side_effect=RuntimeError("Domino failed"),
        ):
            with pytest.raises(RuntimeError, match="Domino failed"):
                await get_job_or_404(db_session, job.id, "test-user")

    @pytest.mark.asyncio
    async def test_raises_404_when_job_missing(self, db_session):
        with pytest.raises(HTTPException) as exc_info:
            await get_job_or_404(db_session, "missing-job-id", "test-user")

        assert exc_info.value.status_code == 404


# ===========================================================================
# Domino log adaptation / branching
# ===========================================================================


class TestDominoJobLogs:
    """Tests for Domino-backed job log fetching."""

    def test_build_domino_job_logs_adapts_to_job_log_shape(self):
        timestamp = datetime(2026, 3, 30, 12, 0, tzinfo=timezone.utc)
        envelope = LogsEnvelopeV1(
            logs=JobLogsV1(
                is_complete=True,
                log_content=[
                    LogContentV1(
                        log="training started",
                        log_type=LogTypeV1.STDOUT,
                        size=16,
                        timestamp=timestamp,
                    ),
                    LogContentV1(
                        log="out of memory",
                        log_type=LogTypeV1.STDERR,
                        size=13,
                        timestamp=timestamp,
                    ),
                ],
            ),
            metadata=LogsEnvelopeV1Metadata(
                notices=[],
                pagination=LogsPaginationV1(limit=2),
                request_id="req-123",
            ),
        )

        logs = _build_domino_job_logs("job-123", envelope)

        assert [log.id for log in logs] == [1, 2]
        assert [log.job_id for log in logs] == ["job-123", "job-123"]
        assert [log.level for log in logs] == ["INFO", "ERROR"]
        assert [log.message for log in logs] == ["training started", "out of memory"]
        assert all(log.timestamp == timestamp for log in logs)

    @pytest.mark.asyncio
    async def test_get_job_logs_uses_domino_http_when_domino_job_id_exists(self, db_session):
        remote_logs = [
            JobLog(
                id=1,
                job_id="job-123",
                level="INFO",
                message="remote line",
                timestamp=datetime(2026, 3, 30, 12, 0, tzinfo=timezone.utc),
            )
        ]
        job = MagicMock(id="job-123", domino_job_id="run-123")

        with (
            patch("app.services.job_service.get_viewing_user_name", return_value="test-user"),
            patch("app.services.job_service.get_job_or_404", new_callable=AsyncMock, return_value=job),
            patch(
                "app.services.job_service._fetch_domino_job_logs",
                new_callable=AsyncMock,
                return_value=remote_logs,
            ) as mock_fetch_domino_logs,
            patch("app.services.job_service.crud.get_job_logs", new_callable=AsyncMock) as mock_get_db_logs,
        ):
            logs = await get_job_logs(db_session, "job-123", limit=25)

        assert logs == remote_logs
        mock_fetch_domino_logs.assert_awaited_once_with(
            job_id="job-123",
            domino_job_id="run-123",
            limit=25,
        )
        mock_get_db_logs.assert_not_awaited()


# ===========================================================================
# _ensure_mlflow_results
# ===========================================================================


class TestEnsureMlflowResults:
    """Tests for the lazy MLflow result fetch on completed jobs."""

    _MLFLOW_RESULTS = {
        "metrics": {"best_model": "LightGBM", "best_score": 0.92},
        "leaderboard": [{"model": "LightGBM", "score": 0.92}],
        "feature_importance": [{"feature": "age", "importance": 0.5}],
        "model_path": "runs:/run-xyz/autogluon_model",
        "experiment_run_id": "run-xyz",
        "experiment_name": "my-experiment",
    }

    @pytest.mark.asyncio
    async def test_fetches_and_persists_when_completed_without_results(self, db_session, make_job):
        job = make_job(status=JobStatus.COMPLETED)
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_mlflow_results",
            new_callable=AsyncMock,
            return_value=self._MLFLOW_RESULTS,
        ):
            result = await _ensure_mlflow_results(db_session, job)

        assert result.model_path == "runs:/run-xyz/autogluon_model"
        assert result.leaderboard == self._MLFLOW_RESULTS["leaderboard"]
        assert result.feature_importance == self._MLFLOW_RESULTS["feature_importance"]

    @pytest.mark.asyncio
    async def test_skips_fetch_when_model_path_already_set(self, db_session, make_job):
        job = make_job(status=JobStatus.COMPLETED, model_path="runs:/existing/model")
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_mlflow_results",
            new_callable=AsyncMock,
        ) as mock_fetch:
            result = await _ensure_mlflow_results(db_session, job)

        mock_fetch.assert_not_awaited()
        assert result.model_path == "runs:/existing/model"

    @pytest.mark.asyncio
    async def test_skips_fetch_when_job_not_completed(self, db_session, make_job):
        for status in (JobStatus.PENDING, JobStatus.RUNNING, JobStatus.FAILED):
            job = make_job(status=status)
            db_session.add(job)
            await db_session.commit()

            with patch(
                "app.services.job_service._fetch_mlflow_results",
                new_callable=AsyncMock,
            ) as mock_fetch:
                result = await _ensure_mlflow_results(db_session, job)

            mock_fetch.assert_not_awaited()
            assert result.model_path is None

    @pytest.mark.asyncio
    async def test_returns_original_job_when_fetch_returns_none(self, db_session, make_job):
        job = make_job(status=JobStatus.COMPLETED)
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_mlflow_results",
            new_callable=AsyncMock,
            return_value=None,
        ):
            result = await _ensure_mlflow_results(db_session, job)

        assert result.model_path is None

    @pytest.mark.asyncio
    async def test_returns_original_job_when_fetch_raises(self, db_session, make_job):
        job = make_job(status=JobStatus.COMPLETED)
        db_session.add(job)
        await db_session.commit()

        with patch(
            "app.services.job_service._fetch_mlflow_results",
            new_callable=AsyncMock,
            side_effect=RuntimeError("MLflow unavailable"),
        ):
            result = await _ensure_mlflow_results(db_session, job)

        assert result.model_path is None


