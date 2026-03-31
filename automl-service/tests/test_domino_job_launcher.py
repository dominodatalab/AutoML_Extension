import json
from unittest.mock import MagicMock, patch

import pytest

from app.core.domino_job_launcher import DominoJobLauncher


ENV_ID = "env-abc123"
ENV_REV_ID = "env-rev-xyz456"
PROJECT_ID = "project-111"


def _make_launcher(monkeypatch, env_id=ENV_ID, env_rev_id=ENV_REV_ID):
    monkeypatch.setenv("DOMINO_ENVIRONMENT_ID", env_id)
    monkeypatch.setenv("DOMINO_ENVIRONMENT_REVISION_ID", env_rev_id)
    return DominoJobLauncher()


def _domino_job_response(job_id: str = "domino-job-999") -> MagicMock:
    resp = MagicMock()
    resp.json.return_value = {"id": job_id}
    return resp


class TestInit:
    def test_stores_environment_ids_from_env(self, monkeypatch):
        launcher = _make_launcher(monkeypatch, env_id="my-env", env_rev_id="my-rev")
        assert launcher.environment_id == "my-env"
        assert launcher.environment_revision_id == "my-rev"

    def test_raises_when_environment_id_missing(self, monkeypatch):
        monkeypatch.setenv("DOMINO_ENVIRONMENT_REVISION_ID", ENV_REV_ID)
        monkeypatch.delenv("DOMINO_ENVIRONMENT_ID", raising=False)
        with pytest.raises(RuntimeError, match="DOMINO_ENVIRONMENT_ID"):
            DominoJobLauncher()

    def test_raises_when_environment_revision_id_missing(self, monkeypatch):
        monkeypatch.setenv("DOMINO_ENVIRONMENT_ID", ENV_ID)
        monkeypatch.delenv("DOMINO_ENVIRONMENT_REVISION_ID", raising=False)
        with pytest.raises(RuntimeError, match="DOMINO_ENVIRONMENT_REVISION_ID"):
            DominoJobLauncher()


class TestStartTrainingJob:
    @pytest.mark.asyncio
    async def test_returns_failure_when_not_domino_environment(self, monkeypatch):
        launcher = _make_launcher(monkeypatch)
        with patch.object(launcher, "settings") as mock_settings:
            mock_settings.is_domino_environment = False
            result = await launcher.start_training_job(job_id="job-1", file_path="/data/train.csv")
        assert result["success"] is False

    @pytest.mark.asyncio
    async def test_command_and_payload_sent_to_domino(self, monkeypatch):
        launcher = _make_launcher(monkeypatch, env_id="env-TEST", env_rev_id="rev-TEST")
        captured = {}

        async def fake_domino_request(method, path, **kwargs):
            if path == "/v4/jobs/start":
                captured["payload"] = kwargs.get("json", {})
            return _domino_job_response()

        job_config = {"model_type": "tabular"}
        with patch.object(launcher, "settings") as mock_settings, \
             patch("app.core.domino_job_launcher.domino_request", side_effect=fake_domino_request):
            mock_settings.is_domino_environment = True
            result = await launcher.start_training_job(
                job_id="abc-123",
                file_path="/mnt/datasets/train.csv",
                project_id=PROJECT_ID,
                job_config=job_config,
            )

        expected_command = (
            f"python {DominoJobLauncher.TRAINING_RUNNER_PATH}"
            " --job-id abc-123 --job-config"
            ' \'{"model_type": "tabular"}\''
        )
        assert captured["payload"]["commandToRun"] == expected_command
        assert captured["payload"]["environmentId"] == "env-TEST"
        assert captured["payload"]["environmentRevisionId"] == "rev-TEST"
        assert captured["payload"]["projectId"] == PROJECT_ID
        assert result["success"] is True
        assert result["domino_job_id"] == "domino-job-999"


class TestStartEdaJob:
    @pytest.mark.asyncio
    async def test_returns_failure_when_not_domino_environment(self, monkeypatch):
        launcher = _make_launcher(monkeypatch)
        with patch.object(launcher, "settings") as mock_settings:
            mock_settings.is_domino_environment = False
            result = await launcher.start_eda_job(
                request_id="req-1", mode="tabular", file_path="/data/train.csv",
                sample_size=50000, sampling_strategy="random",
            )
        assert result["success"] is False

    @pytest.mark.asyncio
    async def test_command_and_payload_sent_to_domino(self, monkeypatch):
        launcher = _make_launcher(monkeypatch, env_id="env-TEST", env_rev_id="rev-TEST")
        captured = {}

        async def fake_domino_request(method, path, **kwargs):
            if path == "/v4/jobs/start":
                captured["payload"] = kwargs.get("json", {})
            return _domino_job_response()

        with patch.object(launcher, "settings") as mock_settings, \
             patch("app.core.domino_job_launcher.domino_request", side_effect=fake_domino_request):
            mock_settings.is_domino_environment = True
            result = await launcher.start_eda_job(
                request_id="req-1", mode="timeseries", file_path="/mnt/datasets/eda.parquet",
                sample_size=10000, sampling_strategy="random",
                stratify_column=None, time_column=None, target_column=None,
                id_column=None, rolling_window=None,
                project_id=PROJECT_ID,
            )

        expected_command = (
            f"python {DominoJobLauncher.EDA_RUNNER_PATH}"
            " --request-id req-1 --mode timeseries --file-path /mnt/datasets/eda.parquet"
            " --sample-size 10000 --sampling-strategy random"
        )
        assert captured["payload"]["commandToRun"] == expected_command
        assert captured["payload"]["environmentId"] == "env-TEST"
        assert captured["payload"]["environmentRevisionId"] == "rev-TEST"
        assert captured["payload"]["projectId"] == PROJECT_ID
        assert result["success"] is True
        assert result["domino_job_id"] == "domino-job-999"
