"""Tests for database CRUD operations (app/db/crud.py).

All tests use the async in-memory SQLite database provided by the
``db_session`` and ``make_job`` fixtures defined in conftest.py.
"""

from datetime import timedelta
from pathlib import Path
import sys
import uuid

import pytest
import pytest_asyncio

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.utils import utc_now
from app.db.models import Job, JobLog, JobStatus, ModelType, RegisteredModel
from app.db import crud


# ---------------------------------------------------------------------------
# create_job / get_job / get_jobs round-trip
# ---------------------------------------------------------------------------


class TestJobRoundTrip:
    """Verify basic create, fetch-by-id, and list operations."""

    @pytest.mark.asyncio
    async def test_create_and_get_job(self, db_session, make_job):
        job = make_job(name="round-trip")
        created = await crud.create_job(db_session, job)

        assert created.id == job.id
        assert created.name == "round-trip"

        fetched = await crud.get_job(db_session, job.id)
        assert fetched is not None
        assert fetched.id == job.id
        assert fetched.name == "round-trip"

    @pytest.mark.asyncio
    async def test_get_job_returns_none_for_missing_id(self, db_session):
        result = await crud.get_job(db_session, "nonexistent-id")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_jobs_returns_all(self, db_session, make_job):
        job_a = make_job(name="job-a")
        job_b = make_job(name="job-b")
        await crud.create_job(db_session, job_a)
        await crud.create_job(db_session, job_b)

        jobs = await crud.get_jobs(db_session)
        names = {j.name for j in jobs}
        assert "job-a" in names
        assert "job-b" in names

    @pytest.mark.asyncio
    async def test_get_jobs_filters_by_status(self, db_session, make_job):
        pending = make_job(name="pending-job", status=JobStatus.PENDING)
        running = make_job(name="running-job", status=JobStatus.RUNNING)
        await crud.create_job(db_session, pending)
        await crud.create_job(db_session, running)

        results = await crud.get_jobs(db_session, status=JobStatus.RUNNING)
        assert all(j.status == JobStatus.RUNNING for j in results)
        assert any(j.name == "running-job" for j in results)

    @pytest.mark.asyncio
    async def test_get_jobs_filters_by_owner(self, db_session, make_job):
        job = make_job(name="owned", owner="alice")
        await crud.create_job(db_session, job)

        results = await crud.get_jobs(db_session, owner="alice")
        assert any(j.name == "owned" for j in results)

        results = await crud.get_jobs(db_session, owner="bob")
        assert not any(j.name == "owned" for j in results)

    @pytest.mark.asyncio
    async def test_get_jobs_skip_and_limit(self, db_session, make_job):
        for i in range(5):
            await crud.create_job(db_session, make_job(name=f"paged-{i}"))

        page = await crud.get_jobs(db_session, skip=0, limit=2)
        assert len(page) == 2


# ---------------------------------------------------------------------------
# get_job_by_scoped_name
# ---------------------------------------------------------------------------


class TestGetJobByScopedName:
    """Verify case-insensitive and owner+project scoping."""

    @pytest.mark.asyncio
    async def test_case_insensitive_match(self, db_session, make_job):
        job = make_job(name="My Job", owner="alice", project_name="proj")
        await crud.create_job(db_session, job)

        found = await crud.get_job_by_scoped_name(
            db_session, name="  my job  ", owner="alice", project_name="proj"
        )
        assert found is not None
        assert found.id == job.id

    @pytest.mark.asyncio
    async def test_scoped_by_owner(self, db_session, make_job):
        job_alice = make_job(name="shared", owner="alice", project_name="proj")
        job_bob = make_job(name="shared", owner="bob", project_name="proj")
        await crud.create_job(db_session, job_alice)
        await crud.create_job(db_session, job_bob)

        found = await crud.get_job_by_scoped_name(
            db_session, name="shared", owner="bob", project_name="proj"
        )
        assert found is not None
        assert found.id == job_bob.id

    @pytest.mark.asyncio
    async def test_scoped_by_project(self, db_session, make_job):
        job_p1 = make_job(name="dup", owner="alice", project_name="proj-1")
        job_p2 = make_job(name="dup", owner="alice", project_name="proj-2")
        await crud.create_job(db_session, job_p1)
        await crud.create_job(db_session, job_p2)

        found = await crud.get_job_by_scoped_name(
            db_session, name="dup", owner="alice", project_name="proj-1"
        )
        assert found is not None
        assert found.id == job_p1.id

    @pytest.mark.asyncio
    async def test_returns_none_when_not_found(self, db_session, make_job):
        job = make_job(name="exists", owner="alice", project_name="proj")
        await crud.create_job(db_session, job)

        found = await crud.get_job_by_scoped_name(
            db_session, name="does-not-exist", owner="alice", project_name="proj"
        )
        assert found is None


# ---------------------------------------------------------------------------
# update_job_status
# ---------------------------------------------------------------------------


class TestUpdateJobStatus:
    """Verify status transitions, error messages, and timestamps."""

    @pytest.mark.asyncio
    async def test_status_transition(self, db_session, make_job):
        job = make_job(status=JobStatus.PENDING)
        await crud.create_job(db_session, job)

        updated = await crud.update_job_status(
            db_session, job.id, JobStatus.RUNNING
        )
        assert updated.status == JobStatus.RUNNING

    @pytest.mark.asyncio
    async def test_status_with_error_message(self, db_session, make_job):
        job = make_job(status=JobStatus.RUNNING)
        await crud.create_job(db_session, job)

        updated = await crud.update_job_status(
            db_session, job.id, JobStatus.FAILED, error_message="OOM"
        )
        assert updated.status == JobStatus.FAILED
        assert updated.error_message == "OOM"

    @pytest.mark.asyncio
    async def test_status_with_timestamps(self, db_session, make_job):
        job = make_job(status=JobStatus.PENDING)
        await crud.create_job(db_session, job)

        now = utc_now()
        updated = await crud.update_job_status(
            db_session, job.id, JobStatus.RUNNING, started_at=now
        )
        assert updated.started_at == now

        later = utc_now()
        updated = await crud.update_job_status(
            db_session, job.id, JobStatus.COMPLETED, completed_at=later
        )
        assert updated.completed_at == later

    @pytest.mark.asyncio
    async def test_update_nonexistent_job_returns_none(self, db_session):
        result = await crud.update_job_status(
            db_session, "no-such-id", JobStatus.RUNNING
        )
        assert result is None


# ---------------------------------------------------------------------------
# update_job_results
# ---------------------------------------------------------------------------


class TestUpdateJobResults:
    """Verify that results set metrics, leaderboard, model_path, status, progress."""

    @pytest.mark.asyncio
    async def test_sets_all_result_fields(self, db_session, make_job):
        job = make_job(status=JobStatus.RUNNING)
        await crud.create_job(db_session, job)

        metrics = {"accuracy": 0.95, "f1": 0.93}
        leaderboard = {"models": [{"name": "LightGBM", "score": 0.95}]}
        model_path = "/models/best"

        updated = await crud.update_job_results(
            db_session, job.id, metrics, leaderboard, model_path
        )

        assert updated.status == JobStatus.COMPLETED
        assert updated.progress == 100
        assert updated.current_step == "Complete"
        assert updated.metrics == metrics
        assert updated.leaderboard == leaderboard
        assert updated.model_path == model_path
        assert updated.completed_at is not None

    @pytest.mark.asyncio
    async def test_sets_experiment_fields(self, db_session, make_job):
        job = make_job(status=JobStatus.RUNNING)
        await crud.create_job(db_session, job)

        updated = await crud.update_job_results(
            db_session,
            job.id,
            metrics={"r2": 0.88},
            leaderboard={},
            model_path="/m",
            experiment_run_id="run-123",
            experiment_name="exp-1",
        )
        assert updated.experiment_run_id == "run-123"
        assert updated.experiment_name == "exp-1"


# ---------------------------------------------------------------------------
# update_job_progress
# ---------------------------------------------------------------------------


class TestUpdateJobProgress:
    """Verify progress, current_step, and models_trained updates."""

    @pytest.mark.asyncio
    async def test_update_progress(self, db_session, make_job):
        job = make_job(status=JobStatus.RUNNING)
        await crud.create_job(db_session, job)

        updated = await crud.update_job_progress(
            db_session,
            job.id,
            progress=42,
            current_step="Feature engineering",
            models_trained=3,
        )
        assert updated.progress == 42
        assert updated.current_step == "Feature engineering"
        assert updated.models_trained == 3

    @pytest.mark.asyncio
    async def test_update_progress_minimal(self, db_session, make_job):
        """Only progress is required; optional fields stay unchanged."""
        job = make_job(status=JobStatus.RUNNING)
        await crud.create_job(db_session, job)

        updated = await crud.update_job_progress(db_session, job.id, progress=10)
        assert updated.progress == 10
        assert updated.current_step is None  # not set


# ---------------------------------------------------------------------------
# delete_job
# ---------------------------------------------------------------------------


class TestDeleteJob:
    """Verify delete returns True/False and actually removes the record."""

    @pytest.mark.asyncio
    async def test_delete_existing_job(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        result = await crud.delete_job(db_session, job.id)
        assert result is True

        gone = await crud.get_job(db_session, job.id)
        assert gone is None

    @pytest.mark.asyncio
    async def test_delete_nonexistent_job(self, db_session):
        result = await crud.delete_job(db_session, "nonexistent")
        assert result is False


# ---------------------------------------------------------------------------
# add_job_log / get_job_logs
# ---------------------------------------------------------------------------


class TestJobLogs:
    """Verify log creation and retrieval."""

    @pytest.mark.asyncio
    async def test_add_and_get_logs(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        log1 = await crud.add_job_log(db_session, job.id, "Starting training")
        log2 = await crud.add_job_log(
            db_session, job.id, "OOM error", level="ERROR"
        )

        assert log1.id is not None
        assert log1.level == "INFO"
        assert log2.level == "ERROR"

        logs = await crud.get_job_logs(db_session, job.id)
        assert len(logs) == 2
        messages = [log.message for log in logs]
        assert "Starting training" in messages
        assert "OOM error" in messages

    @pytest.mark.asyncio
    async def test_get_logs_respects_limit(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        for i in range(10):
            await crud.add_job_log(db_session, job.id, f"msg-{i}")

        logs = await crud.get_job_logs(db_session, job.id, limit=3)
        assert len(logs) == 3

    @pytest.mark.asyncio
    async def test_get_logs_for_job_with_no_logs(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        logs = await crud.get_job_logs(db_session, job.id)
        assert len(logs) == 0


# ---------------------------------------------------------------------------
# create_registered_model / get_registered_models
# ---------------------------------------------------------------------------


class TestRegisteredModels:
    """Verify model registration CRUD."""

    @pytest.mark.asyncio
    async def test_create_and_list_models(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        model = RegisteredModel(
            id=str(uuid.uuid4()),
            name="my-model",
            job_id=job.id,
            version=1,
            created_at=utc_now(),
        )
        created = await crud.create_registered_model(db_session, model)
        assert created.name == "my-model"

        models = await crud.get_registered_models(db_session)
        assert len(models) >= 1
        assert any(m.name == "my-model" for m in models)

    @pytest.mark.asyncio
    async def test_get_registered_model_by_name(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        model = RegisteredModel(
            id=str(uuid.uuid4()),
            name="unique-model",
            job_id=job.id,
            version=1,
            created_at=utc_now(),
        )
        await crud.create_registered_model(db_session, model)

        found = await crud.get_registered_model(db_session, "unique-model")
        assert found is not None
        assert found.job_id == job.id


# ---------------------------------------------------------------------------
# get_jobs_for_cleanup
# ---------------------------------------------------------------------------


class TestGetJobsForCleanup:
    """Verify status + age filtering for cleanup queries."""

    @pytest.mark.asyncio
    async def test_filters_by_status(self, db_session, make_job):
        completed = make_job(name="done", status=JobStatus.COMPLETED)
        failed = make_job(name="bad", status=JobStatus.FAILED)
        pending = make_job(name="wait", status=JobStatus.PENDING)
        await crud.create_job(db_session, completed)
        await crud.create_job(db_session, failed)
        await crud.create_job(db_session, pending)

        jobs = await crud.get_jobs_for_cleanup(
            db_session, statuses=[JobStatus.COMPLETED, JobStatus.FAILED]
        )
        statuses = {j.status for j in jobs}
        assert JobStatus.PENDING not in statuses
        names = {j.name for j in jobs}
        assert "done" in names
        assert "bad" in names

    @pytest.mark.asyncio
    async def test_filters_by_age(self, db_session, make_job):
        old_job = make_job(name="old")
        old_job.created_at = utc_now() - timedelta(days=10)
        new_job = make_job(name="new")
        new_job.created_at = utc_now()
        # Both must be in a qualifying status
        old_job.status = JobStatus.COMPLETED
        new_job.status = JobStatus.COMPLETED
        await crud.create_job(db_session, old_job)
        await crud.create_job(db_session, new_job)

        jobs = await crud.get_jobs_for_cleanup(
            db_session,
            statuses=[JobStatus.COMPLETED],
            older_than_days=5,
        )
        names = {j.name for j in jobs}
        assert "old" in names
        assert "new" not in names

    @pytest.mark.asyncio
    async def test_returns_empty_when_nothing_matches(self, db_session, make_job):
        job = make_job(status=JobStatus.PENDING)
        await crud.create_job(db_session, job)

        jobs = await crud.get_jobs_for_cleanup(
            db_session, statuses=[JobStatus.COMPLETED]
        )
        assert len(jobs) == 0


# ---------------------------------------------------------------------------
# count_jobs_with_file_path
# ---------------------------------------------------------------------------


class TestCountJobsWithFilePath:
    """Verify reference counting by file_path."""

    @pytest.mark.asyncio
    async def test_counts_matching_file_paths(self, db_session, make_job):
        path = "/data/shared.csv"
        await crud.create_job(db_session, make_job(name="j1", file_path=path))
        await crud.create_job(db_session, make_job(name="j2", file_path=path))
        await crud.create_job(
            db_session, make_job(name="j3", file_path="/data/other.csv")
        )

        count = await crud.count_jobs_with_file_path(db_session, path)
        assert count == 2

    @pytest.mark.asyncio
    async def test_returns_zero_when_no_match(self, db_session):
        count = await crud.count_jobs_with_file_path(db_session, "/no/match.csv")
        assert count == 0


# ---------------------------------------------------------------------------
# delete_job_logs
# ---------------------------------------------------------------------------


class TestDeleteJobLogs:
    """Verify bulk log deletion and row count."""

    @pytest.mark.asyncio
    async def test_deletes_logs_and_returns_count(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        for i in range(4):
            await crud.add_job_log(db_session, job.id, f"log-{i}")

        deleted = await crud.delete_job_logs(db_session, job.id)
        assert deleted == 4

        remaining = await crud.get_job_logs(db_session, job.id)
        assert len(remaining) == 0

    @pytest.mark.asyncio
    async def test_returns_zero_when_no_logs(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        deleted = await crud.delete_job_logs(db_session, job.id)
        assert deleted == 0


# ---------------------------------------------------------------------------
# delete_registered_models_for_job
# ---------------------------------------------------------------------------


class TestDeleteRegisteredModelsForJob:
    """Verify cascade deletion of registered models by job_id."""

    @pytest.mark.asyncio
    async def test_deletes_models_and_returns_count(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        for i in range(3):
            model = RegisteredModel(
                id=str(uuid.uuid4()),
                name=f"model-{job.id[:8]}-{i}",
                job_id=job.id,
                version=1,
                created_at=utc_now(),
            )
            await crud.create_registered_model(db_session, model)

        deleted = await crud.delete_registered_models_for_job(db_session, job.id)
        assert deleted == 3

        models = await crud.get_registered_models(db_session)
        assert not any(m.job_id == job.id for m in models)

    @pytest.mark.asyncio
    async def test_returns_zero_when_no_models(self, db_session, make_job):
        job = make_job()
        await crud.create_job(db_session, job)

        deleted = await crud.delete_registered_models_for_job(db_session, job.id)
        assert deleted == 0
