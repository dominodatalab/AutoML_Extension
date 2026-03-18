"""Tests for app.core.domino_job_launcher."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.core.domino_job_launcher import DominoJobLauncher


class TestJobStart:

    @pytest.mark.asyncio
    async def test_job_start_uses_proxy(self):
        """Job launch goes through domino_request (proxy) directly."""
        launcher = DominoJobLauncher()
        response = MagicMock(spec=httpx.Response)
        response.json.return_value = {"job": {"id": "job-123"}}

        with patch(
            "app.core.domino_job_launcher.resolve_domino_project_id",
            return_value="app-project",
        ), patch.object(
            launcher,
            "_resolve_launch_commit_id",
            return_value=(None, None),
        ), patch(
            "app.core.domino_job_launcher.domino_request",
            new_callable=AsyncMock,
            return_value=response,
        ) as mock_request:
            result = await launcher._job_start(
                command="python automl-service/app/workers/domino_eda_runner.py",
                title="AutoML EDA 12345678",
                hardware_tier_name=None,
                environment_id=None,
                project_id="target-project",
            )

        assert result == {"job": {"id": "job-123"}}
        mock_request.assert_awaited_once_with(
            "POST",
            "/api/jobs/v1/jobs",
            json={
                "projectId": "target-project",
                "runCommand": "python automl-service/app/workers/domino_eda_runner.py",
                "title": "AutoML EDA 12345678",
            },
        )
