"""Tests for app.core.domino_job_launcher."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.core.domino_job_launcher import DominoJobLauncher


class TestJobApiRequest:

    @pytest.mark.asyncio
    async def test_prefers_direct_host_then_falls_back_to_default(self):
        launcher = DominoJobLauncher()
        response = MagicMock(spec=httpx.Response)

        with patch(
            "app.core.domino_job_launcher.resolve_domino_nucleus_host",
            return_value="http://nucleus-frontend.domino-platform:80",
        ), patch(
            "app.core.domino_job_launcher.domino_request",
            new_callable=AsyncMock,
            side_effect=[
                httpx.RemoteProtocolError("Server disconnected without sending a response."),
                response,
            ],
        ) as domino_request_mock:
            result = await launcher._job_api_request(
                "POST",
                "/api/jobs/v1/jobs",
                json={"projectId": "target-project"},
            )

        assert result is response
        assert len(domino_request_mock.await_args_list) == 2

        first_call = domino_request_mock.await_args_list[0]
        assert first_call.args == ("POST", "/api/jobs/v1/jobs")
        assert first_call.kwargs["json"] == {"projectId": "target-project"}
        assert first_call.kwargs["base_url"] == "http://nucleus-frontend.domino-platform:80"
        assert first_call.kwargs["max_retries"] == 0

        second_call = domino_request_mock.await_args_list[1]
        assert second_call.args == ("POST", "/api/jobs/v1/jobs")
        assert second_call.kwargs["json"] == {"projectId": "target-project"}
        assert second_call.kwargs["base_url"] is None
        assert "max_retries" not in second_call.kwargs


class TestJobStart:

    @pytest.mark.asyncio
    async def test_job_start_uses_job_api_request(self):
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
        ), patch.object(
            launcher,
            "_job_api_request",
            new_callable=AsyncMock,
            return_value=response,
        ) as job_api_request_mock:
            result = await launcher._job_start(
                command="python automl-service/app/workers/domino_eda_runner.py",
                title="AutoML EDA 12345678",
                hardware_tier_name=None,
                environment_id=None,
                project_id="target-project",
            )

        assert result == {"job": {"id": "job-123"}}
        job_api_request_mock.assert_awaited_once_with(
            "POST",
            "/api/jobs/v1/jobs",
            json={
                "projectId": "target-project",
                "runCommand": "python automl-service/app/workers/domino_eda_runner.py",
                "title": "AutoML EDA 12345678",
            },
        )
