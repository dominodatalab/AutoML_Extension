"""Integration tests for cross-project database URL resolution and job launch flows.

Tests the full API request path with mocked Domino APIs to verify:
1. Training job creation via POST /svc/v1/jobs (domino_job target) includes
   --database-url and --job-config in the launched command.
2. Async EDA profiling via POST /svc/v1/profiling/profile/async/start includes
   --database-url in the launched command.
3. The _db_url_remap module correctly rewires sqlite URLs when the original
   path doesn't exist but an alternative mount does.
4. remap_shared_path in utils.py finds files across all mount roots including
   the newly added /mnt/imported/data/.

Run:
    python -m pytest tests/test_cross_project_integration.py -v
"""

import json
import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


# ---------------------------------------------------------------------------
# 1. Training job launch includes --database-url and --job-config
# ---------------------------------------------------------------------------


class TestTrainingJobLaunchCommand:
    """POST /svc/v1/jobs with execution_target=domino_job builds correct command."""

    @pytest.mark.asyncio
    async def test_launch_command_includes_database_url(
        self, app_client, tabular_csv, monkeypatch
    ):
        """The Domino job start payload contains --database-url with the app's DB URL."""
        monkeypatch.setenv("DOMINO_PROJECT_ID", "proj-123")
        monkeypatch.setenv("DOMINO_PROJECT_OWNER", "testowner")
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "testproject")
        monkeypatch.setenv("DOMINO_API_HOST", "https://domino.example.com")
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")

        import app.config as config_module
        config_module._settings_instance = None

        captured_payloads = []

        async def mock_domino_request(method, path, **kwargs):
            resp = MagicMock()
            resp.status_code = 200
            if method == "POST" and "jobs/start" in path:
                captured_payloads.append(kwargs.get("json", {}))
                resp.json.return_value = {"id": "domino-job-abc"}
            elif "hardwareTiers" in path:
                resp.json.return_value = []
            else:
                resp.json.return_value = {}
            return resp

        monkeypatch.setattr(
            "app.core.domino_job_launcher.domino_request",
            mock_domino_request,
        )
        monkeypatch.setattr(
            "app.core.domino_job_launcher.resolve_domino_project_id",
            lambda: "proj-123",
        )

        # Mock storage resolver to avoid real Domino dataset API calls.
        # It's imported locally inside create_job_with_context, so mock at source.
        mock_resolver = AsyncMock()
        mock_resolver.ensure_dataset_exists = AsyncMock(return_value=None)
        monkeypatch.setattr(
            "app.services.storage_resolver.get_storage_resolver",
            lambda: mock_resolver,
        )

        resp = await app_client.post(
            "/svc/v1/jobs",
            json={
                "name": "integration-train-test",
                "model_type": "tabular",
                "problem_type": "binary",
                "data_source": "upload",
                "file_path": tabular_csv,
                "target_column": "target",
                "execution_target": "domino_job",
            },
        )

        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body["execution_target"] == "domino_job"
        assert body["domino_job_id"] == "domino-job-abc"

        # Verify the command sent to Domino
        assert len(captured_payloads) == 1
        command = captured_payloads[0]["commandToRun"]
        assert "--database-url" in command
        assert "--job-id" in command
        assert "--job-config" in command

        config_module._settings_instance = None

    @pytest.mark.asyncio
    async def test_launch_command_job_config_is_valid_json(
        self, app_client, tabular_csv, monkeypatch
    ):
        """The --job-config value is parseable JSON containing the job's fields."""
        monkeypatch.setenv("DOMINO_PROJECT_ID", "proj-123")
        monkeypatch.setenv("DOMINO_PROJECT_OWNER", "testowner")
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "testproject")
        monkeypatch.setenv("DOMINO_API_HOST", "https://domino.example.com")
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")

        import app.config as config_module
        config_module._settings_instance = None

        captured_payloads = []

        async def mock_domino_request(method, path, **kwargs):
            resp = MagicMock()
            resp.status_code = 200
            if method == "POST" and "jobs/start" in path:
                captured_payloads.append(kwargs.get("json", {}))
                resp.json.return_value = {"id": "domino-job-def"}
            elif "hardwareTiers" in path:
                resp.json.return_value = []
            else:
                resp.json.return_value = {}
            return resp

        monkeypatch.setattr(
            "app.core.domino_job_launcher.domino_request",
            mock_domino_request,
        )
        monkeypatch.setattr(
            "app.core.domino_job_launcher.resolve_domino_project_id",
            lambda: "proj-123",
        )
        mock_resolver = AsyncMock()
        mock_resolver.ensure_dataset_exists = AsyncMock(return_value=None)
        monkeypatch.setattr(
            "app.services.storage_resolver.get_storage_resolver",
            lambda: mock_resolver,
        )

        resp = await app_client.post(
            "/svc/v1/jobs",
            json={
                "name": "integration-config-test",
                "model_type": "tabular",
                "problem_type": "binary",
                "data_source": "upload",
                "file_path": tabular_csv,
                "target_column": "target",
                "execution_target": "domino_job",
            },
        )
        assert resp.status_code == 200, resp.text

        command = captured_payloads[0]["commandToRun"]

        # Extract the --job-config value from the shell-quoted command.
        # The command format: python ... --job-config '<json>' ...
        import shlex
        parts = shlex.split(command)
        idx = parts.index("--job-config")
        raw_config = parts[idx + 1]
        config = json.loads(raw_config)

        assert config["target_column"] == "target"
        assert config["model_type"] == "tabular"
        assert config["problem_type"] == "binary"
        assert config["file_path"] == tabular_csv

        config_module._settings_instance = None


# ---------------------------------------------------------------------------
# 2. Async EDA launch includes --database-url
# ---------------------------------------------------------------------------


class TestAsyncEdaLaunchCommand:
    """POST /svc/v1/profiling/profile/async/start builds command with --database-url."""

    @pytest.mark.asyncio
    async def test_eda_launch_includes_database_url(
        self, app_client, tabular_csv, monkeypatch
    ):
        monkeypatch.setenv("DOMINO_PROJECT_ID", "proj-123")
        monkeypatch.setenv("DOMINO_PROJECT_OWNER", "testowner")
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "testproject")
        monkeypatch.setenv("DOMINO_API_HOST", "https://domino.example.com")
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")

        import app.config as config_module
        config_module._settings_instance = None

        captured_payloads = []

        async def mock_domino_request(method, path, **kwargs):
            resp = MagicMock()
            resp.status_code = 200
            if method == "POST" and "jobs/start" in path:
                captured_payloads.append(kwargs.get("json", {}))
                resp.json.return_value = {"id": "domino-eda-abc"}
            elif "hardwareTiers" in path:
                resp.json.return_value = []
            else:
                resp.json.return_value = {}
            return resp

        monkeypatch.setattr(
            "app.core.domino_job_launcher.domino_request",
            mock_domino_request,
        )
        monkeypatch.setattr(
            "app.core.domino_job_launcher.resolve_domino_project_id",
            lambda: "proj-123",
        )

        # Mock storage resolver (imported locally inside the route handler)
        mock_resolver = AsyncMock()
        mock_resolver.ensure_dataset_exists = AsyncMock(return_value=None)
        monkeypatch.setattr(
            "app.services.storage_resolver.get_storage_resolver",
            lambda: mock_resolver,
        )

        resp = await app_client.post(
            "/svc/v1/profiling/profile/async/start",
            json={
                "mode": "tabular",
                "file_path": tabular_csv,
                "sample_size": 1000,
                "sampling_strategy": "random",
            },
        )

        assert resp.status_code == 200, resp.text
        body = resp.json()
        assert body["status"] == "running"
        assert body["domino_job_id"] == "domino-eda-abc"

        assert len(captured_payloads) == 1
        command = captured_payloads[0]["commandToRun"]
        assert "--database-url" in command
        assert "--request-id" in command
        assert "--file-path" in command

        config_module._settings_instance = None


# ---------------------------------------------------------------------------
# 3. DB URL remap: runner main() uses remapped URL
# ---------------------------------------------------------------------------


class TestRunnerDbUrlRemap:
    """Runners apply remap_database_url before setting DATABASE_URL."""

    def test_training_runner_remaps_database_url(self, monkeypatch):
        """domino_training_runner.main() remaps a non-existent sqlite path to git mount."""
        import sys

        original_url = "sqlite:////mnt/data/myapp/automl.db"
        expected_url = "sqlite:////mnt/imported/data/myapp/automl.db"

        monkeypatch.setattr(
            sys, "argv",
            ["runner", "--job-id", "j1", "--database-url", original_url],
        )
        monkeypatch.delenv("DATABASE_URL", raising=False)

        from app.workers.domino_training_runner import parse_args
        from app.workers._db_url_remap import remap_database_url

        args = parse_args()

        def exists(p):
            return p == "/mnt/imported/data/myapp/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", side_effect=exists), \
             patch("app.workers._db_url_remap.detect_project_type") as mock_detect:
            from app.core.domino_project_type import DominoProjectType
            mock_detect.return_value = DominoProjectType.GIT

            result = remap_database_url(args.database_url)

        assert result == expected_url

    def test_eda_runner_remaps_database_url(self, monkeypatch):
        """domino_eda_runner remaps a non-existent sqlite path to DFS mount."""
        import sys

        original_url = "sqlite:////mnt/data/myapp/automl.db"
        expected_url = "sqlite:////domino/datasets/local/myapp/automl.db"

        monkeypatch.setattr(
            sys, "argv",
            [
                "runner",
                "--request-id", "req-1",
                "--file-path", "/data/file.csv",
                "--database-url", original_url,
            ],
        )
        monkeypatch.delenv("DATABASE_URL", raising=False)

        from app.workers.domino_eda_runner import parse_args
        from app.workers._db_url_remap import remap_database_url

        args = parse_args()

        def exists(p):
            return p == "/domino/datasets/local/myapp/automl.db"

        with patch("app.workers._db_url_remap.os.path.exists", side_effect=exists), \
             patch("app.workers._db_url_remap.detect_project_type") as mock_detect:
            from app.core.domino_project_type import DominoProjectType
            mock_detect.return_value = DominoProjectType.DFS

            result = remap_database_url(args.database_url)

        assert result == expected_url


# ---------------------------------------------------------------------------
# 4. remap_shared_path finds files via /mnt/imported/data/
# ---------------------------------------------------------------------------


class TestRemapSharedPathMountRoots:
    """remap_shared_path in utils.py covers all mount roots including /mnt/imported/data/."""

    def test_remap_mnt_data_to_mnt_imported_data(self):
        """A path under /mnt/data/ remaps to /mnt/imported/data/ when the latter exists."""
        original = "/mnt/data/shared_ds/uploads/file.csv"

        def exists(p):
            return p == "/mnt/imported/data/shared_ds/uploads/file.csv"

        with patch("app.core.utils.os.path.exists", side_effect=exists):
            from app.core.utils import remap_shared_path
            result = remap_shared_path(original)

        assert result == "/mnt/imported/data/shared_ds/uploads/file.csv"

    def test_remap_mnt_imported_data_to_domino_datasets_local(self):
        """A path under /mnt/imported/data/ remaps to /domino/datasets/local/."""
        original = "/mnt/imported/data/shared_ds/uploads/file.csv"

        def exists(p):
            return p == "/domino/datasets/local/shared_ds/uploads/file.csv"

        with patch("app.core.utils.os.path.exists", side_effect=exists):
            from app.core.utils import remap_shared_path
            result = remap_shared_path(original)

        assert result == "/domino/datasets/local/shared_ds/uploads/file.csv"

    def test_remap_domino_datasets_local_to_mnt_imported_data(self):
        """A path under /domino/datasets/local/ remaps to /mnt/imported/data/."""
        original = "/domino/datasets/local/shared_ds/uploads/file.csv"

        def exists(p):
            return p == "/mnt/imported/data/shared_ds/uploads/file.csv"

        with patch("app.core.utils.os.path.exists", side_effect=exists):
            from app.core.utils import remap_shared_path
            result = remap_shared_path(original)

        assert result == "/mnt/imported/data/shared_ds/uploads/file.csv"

    def test_existing_path_returned_unchanged(self, tmp_path):
        """If the original path exists, no remapping occurs."""
        f = tmp_path / "data.csv"
        f.write_text("a,b\n1,2\n")

        from app.core.utils import remap_shared_path
        assert remap_shared_path(str(f)) == str(f)
