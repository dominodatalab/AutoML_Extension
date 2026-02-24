"""Tests for app.core.job_queue.JobQueueManager."""

import asyncio
from unittest.mock import AsyncMock, patch, MagicMock

import pytest
import pytest_asyncio

from app.core.job_queue import JobQueueManager


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def queue() -> JobQueueManager:
    """Create a fresh JobQueueManager (not the cached singleton)."""
    return JobQueueManager(max_concurrent=2)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

async def _fake_training_job(job_id: str, advanced_config=None):
    """Minimal stand-in for run_training_job that just sleeps briefly."""
    await asyncio.sleep(0.05)


# ---------------------------------------------------------------------------
# get_queue_status
# ---------------------------------------------------------------------------

class TestGetQueueStatus:
    def test_initial_state_has_no_jobs(self, queue: JobQueueManager):
        status = queue.get_queue_status()
        assert status["max_concurrent_jobs"] == 2
        assert status["running_jobs"] == 0
        assert status["queued_jobs"] == 0
        assert status["total_tracked"] == 0
        assert status["shutting_down"] is False


# ---------------------------------------------------------------------------
# enqueue
# ---------------------------------------------------------------------------

class TestEnqueue:
    @pytest.mark.asyncio
    async def test_job_appears_in_tasks(self, queue: JobQueueManager):
        with (
            patch("app.core.job_queue.async_session_maker") as mock_session_maker,
            patch(
                "app.core.job_queue.crud",
                new_callable=MagicMock,
            ) as mock_crud,
            patch(
                "app.workers.training_worker.run_training_job",
                side_effect=_fake_training_job,
            ),
        ):
            # Make the context manager returned by async_session_maker()
            # yield a mock session that has async noop helpers.
            mock_db = AsyncMock()
            mock_ctx = AsyncMock()
            mock_ctx.__aenter__ = AsyncMock(return_value=mock_db)
            mock_ctx.__aexit__ = AsyncMock(return_value=False)
            mock_session_maker.return_value = mock_ctx

            mock_crud.update_job_progress = AsyncMock()

            await queue.enqueue("job-1")

            # The task dict should now have an entry for this job.
            assert "job-1" in queue._tasks
            assert "job-1" in queue._cancel_events

            # Let the task finish so it doesn't leak into other tests.
            await asyncio.sleep(0.2)

    @pytest.mark.asyncio
    async def test_duplicate_enqueue_is_skipped(self, queue: JobQueueManager):
        with (
            patch("app.core.job_queue.async_session_maker") as mock_session_maker,
            patch(
                "app.core.job_queue.crud",
                new_callable=MagicMock,
            ) as mock_crud,
            patch(
                "app.workers.training_worker.run_training_job",
                side_effect=_fake_training_job,
            ),
        ):
            mock_db = AsyncMock()
            mock_ctx = AsyncMock()
            mock_ctx.__aenter__ = AsyncMock(return_value=mock_db)
            mock_ctx.__aexit__ = AsyncMock(return_value=False)
            mock_session_maker.return_value = mock_ctx

            mock_crud.update_job_progress = AsyncMock()

            await queue.enqueue("job-dup")
            await queue.enqueue("job-dup")  # should be silently skipped

            # Still only one task for this job id.
            tasks_for_job = [
                name for name in queue._tasks if name == "job-dup"
            ]
            assert len(tasks_for_job) == 1

            await asyncio.sleep(0.2)


# ---------------------------------------------------------------------------
# cancel
# ---------------------------------------------------------------------------

class TestCancel:
    @pytest.mark.asyncio
    async def test_cancel_queued_job_returns_true(self, queue: JobQueueManager):
        with (
            patch("app.core.job_queue.async_session_maker") as mock_session_maker,
            patch(
                "app.core.job_queue.crud",
                new_callable=MagicMock,
            ) as mock_crud,
            patch(
                "app.workers.training_worker.run_training_job",
                side_effect=_fake_training_job,
            ),
        ):
            mock_db = AsyncMock()
            mock_ctx = AsyncMock()
            mock_ctx.__aenter__ = AsyncMock(return_value=mock_db)
            mock_ctx.__aexit__ = AsyncMock(return_value=False)
            mock_session_maker.return_value = mock_ctx

            mock_crud.update_job_progress = AsyncMock()
            mock_crud.get_job = AsyncMock(return_value=None)
            mock_crud.update_job_status = AsyncMock()

            await queue.enqueue("job-cancel")
            result = await queue.cancel("job-cancel")

            assert result is True

            await asyncio.sleep(0.2)

    @pytest.mark.asyncio
    async def test_cancel_nonexistent_returns_false(self, queue: JobQueueManager):
        result = await queue.cancel("no-such-job")
        assert result is False


# ---------------------------------------------------------------------------
# is_job_cancelled
# ---------------------------------------------------------------------------

class TestIsJobCancelled:
    @pytest.mark.asyncio
    async def test_reflects_cancel_event_state(self, queue: JobQueueManager):
        with (
            patch("app.core.job_queue.async_session_maker") as mock_session_maker,
            patch(
                "app.core.job_queue.crud",
                new_callable=MagicMock,
            ) as mock_crud,
            patch(
                "app.workers.training_worker.run_training_job",
                side_effect=_fake_training_job,
            ),
        ):
            mock_db = AsyncMock()
            mock_ctx = AsyncMock()
            mock_ctx.__aenter__ = AsyncMock(return_value=mock_db)
            mock_ctx.__aexit__ = AsyncMock(return_value=False)
            mock_session_maker.return_value = mock_ctx

            mock_crud.update_job_progress = AsyncMock()
            mock_crud.get_job = AsyncMock(return_value=None)
            mock_crud.update_job_status = AsyncMock()

            await queue.enqueue("job-flag")

            # Before cancel, event should not be set.
            assert queue.is_job_cancelled("job-flag") is False

            await queue.cancel("job-flag")

            # After cancel, event should be set.
            assert queue.is_job_cancelled("job-flag") is True

            await asyncio.sleep(0.2)

    def test_unknown_job_returns_false(self, queue: JobQueueManager):
        assert queue.is_job_cancelled("ghost-job") is False
