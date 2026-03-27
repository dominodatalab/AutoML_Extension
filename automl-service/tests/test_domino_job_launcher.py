"""Tests for app.core.domino_job_launcher."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.core.domino_job_launcher import DominoJobLauncher


class TestJobStart:

    @pytest.mark.asyncio
    async def test_job_start_uses_generated_client(self):
        """Job launch uses the generated Domino public API client."""
        launcher = DominoJobLauncher()

        # Mock the generated client response
        mock_parsed = MagicMock()
        mock_parsed.to_dict.return_value = {"job": {"id": "job-123"}}
        mock_response = MagicMock()
        mock_response.parsed = mock_parsed
        mock_response.status_code = 200

        with patch(
            "app.core.domino_job_launcher.resolve_domino_project_id",
            return_value="app-project",
        ), patch.object(
            launcher,
            "_resolve_launch_commit_id",
            return_value=(None, None),
        ), patch(
            "app.core.domino_job_launcher.get_domino_public_api_client_sync",
        ) as mock_get_client, patch(
            "app.api.generated.domino_public_api_client.api.jobs.start_job.asyncio_detailed",
            new_callable=AsyncMock,
            return_value=mock_response,
        ) as mock_start:
            result = await launcher._job_start(
                command="python automl-service/app/workers/domino_eda_runner.py",
                title="AutoML EDA 12345678",
                hardware_tier_name=None,
                project_id="target-project",
            )

        assert result == {"job": {"id": "job-123"}}
        mock_start.assert_awaited_once()
        # Verify the body was constructed with correct project_id and command
        call_kwargs = mock_start.call_args
        body = call_kwargs.kwargs.get("body") or call_kwargs[1].get("body")
        assert body.project_id == "target-project"
        assert body.run_command == "python automl-service/app/workers/domino_eda_runner.py"
