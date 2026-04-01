"""Tests for app.workers.training_worker dispatch behaviour."""

import logging
from unittest.mock import AsyncMock, patch

import pytest

from app.workers.training_worker import add_job_log



class TestAddJobLog:
    """Tests for stdout/logger emission when no DB session is available."""

    @pytest.mark.asyncio
    async def test_logs_to_worker_logger_when_db_is_none(self, caplog):
        with (
            caplog.at_level(logging.INFO, logger="app.workers.training_worker"),
            patch("app.workers.training_worker.crud.add_job_log", new_callable=AsyncMock) as mock_add_job_log,
        ):
            await add_job_log("job-123", "Training job started", level="INFO", db=None)
            await add_job_log("job-123", "Training failed", level="ERROR", db=None)

        records = [
            (record.levelname, record.message)
            for record in caplog.records
            if record.name == "app.workers.training_worker"
        ]
        assert ("INFO", "Training job started") in records
        assert ("ERROR", "Training failed") in records
        mock_add_job_log.assert_not_awaited()
