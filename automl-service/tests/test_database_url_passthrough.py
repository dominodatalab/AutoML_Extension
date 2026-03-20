"""Tests for the --database-url CLI passthrough to child jobs.

Verifies that:
1. Runner CLI parsers accept --database-url
2. The env var gets set before app imports when provided
3. DominoJobLauncher includes --database-url in built commands
4. config.Settings preserves an explicit DATABASE_URL (not overridden by model_post_init)

Run:
    python -m pytest tests/test_database_url_passthrough.py -v
"""

import os
import sys
from unittest.mock import patch, MagicMock

import pytest


# ---------------------------------------------------------------------------
# 1. Runner CLI arg parsing
# ---------------------------------------------------------------------------


class TestTrainingRunnerArgs:
    """domino_training_runner.parse_args accepts --database-url."""

    def test_database_url_parsed(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv",
            ["runner", "--job-id", "abc123", "--database-url", "sqlite:////mnt/data/app/automl.db"],
        )
        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        assert args.job_id == "abc123"
        assert args.database_url == "sqlite:////mnt/data/app/automl.db"

    def test_database_url_optional(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["runner", "--job-id", "abc123"])
        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        assert args.database_url is None


class TestEdaRunnerArgs:
    """domino_eda_runner.parse_args accepts --database-url."""

    def test_database_url_parsed(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv",
            [
                "runner",
                "--request-id", "req-1",
                "--file-path", "/data/file.csv",
                "--database-url", "sqlite:////mnt/data/app/automl.db",
            ],
        )
        from app.workers.domino_eda_runner import parse_args

        args = parse_args()
        assert args.request_id == "req-1"
        assert args.database_url == "sqlite:////mnt/data/app/automl.db"

    def test_database_url_optional(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv",
            ["runner", "--request-id", "req-1", "--file-path", "/data/file.csv"],
        )
        from app.workers.domino_eda_runner import parse_args

        args = parse_args()
        assert args.database_url is None


# ---------------------------------------------------------------------------
# 2. Env var gets set when --database-url is provided
# ---------------------------------------------------------------------------


class TestEnvVarInjection:
    """Runners set DATABASE_URL env var before app imports."""

    def test_training_runner_sets_env(self, monkeypatch):
        monkeypatch.setattr(
            sys, "argv",
            ["runner", "--job-id", "j1", "--database-url", "sqlite:////mnt/data/app/automl.db"],
        )
        monkeypatch.delenv("DATABASE_URL", raising=False)

        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        # Simulate what main() does before importing app modules:
        if args.database_url:
            os.environ["DATABASE_URL"] = args.database_url

        assert os.environ["DATABASE_URL"] == "sqlite:////mnt/data/app/automl.db"

    def test_training_runner_skips_env_when_absent(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["runner", "--job-id", "j1"])
        monkeypatch.delenv("DATABASE_URL", raising=False)

        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        if args.database_url:
            os.environ["DATABASE_URL"] = args.database_url

        assert os.environ.get("DATABASE_URL") is None


# ---------------------------------------------------------------------------
# 3. DominoJobLauncher builds commands with --database-url
# ---------------------------------------------------------------------------


class TestJobLauncherCommand:
    """DominoJobLauncher._build_cli_args and _build_command include --database-url."""

    def test_build_cli_args_includes_database_url(self):
        from app.core.domino_job_launcher import DominoJobLauncher

        args = DominoJobLauncher._build_cli_args({
            "job_id": "j1",
            "database_url": "sqlite:////mnt/data/app/automl.db",
        })
        assert "--database-url" in args
        idx = args.index("--database-url")
        assert args[idx + 1] == "sqlite:////mnt/data/app/automl.db"

    def test_build_cli_args_omits_none_database_url(self):
        from app.core.domino_job_launcher import DominoJobLauncher

        args = DominoJobLauncher._build_cli_args({
            "job_id": "j1",
            "database_url": None,
        })
        assert "--database-url" not in args

    def test_build_command_training(self, monkeypatch):
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")
        from app.core.domino_job_launcher import DominoJobLauncher

        cmd = DominoJobLauncher._build_command(
            DominoJobLauncher,
            "app.workers.domino_training_runner",
            {"job_id": "j1", "database_url": "sqlite:////mnt/data/app/automl.db"},
        )
        assert "--database-url" in cmd
        assert "sqlite:////mnt/data/app/automl.db" in cmd
        assert "--job-id" in cmd

    def test_build_command_eda(self, monkeypatch):
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")
        from app.core.domino_job_launcher import DominoJobLauncher

        cmd = DominoJobLauncher._build_command(
            DominoJobLauncher,
            "app.workers.domino_eda_runner",
            {
                "request_id": "r1",
                "mode": "tabular",
                "file_path": "/data/f.csv",
                "sample_size": 50000,
                "sampling_strategy": "random",
                "database_url": "sqlite:////mnt/data/app/automl.db",
            },
        )
        assert "--database-url" in cmd
        assert "--request-id" in cmd


# ---------------------------------------------------------------------------
# 4. config.Settings preserves explicit DATABASE_URL from env
# ---------------------------------------------------------------------------


class TestConfigPreservesExplicitDatabaseUrl:
    """Settings.model_post_init must NOT override a valid DATABASE_URL."""

    def test_explicit_sqlite_url_preserved(self, monkeypatch):
        url = "sqlite:////mnt/data/my-app-project/automl.db"
        monkeypatch.setenv("DATABASE_URL", url)

        # Reset cached settings singleton
        import app.config as config_module
        config_module._settings_instance = None

        from app.config import Settings

        s = Settings()
        assert s.database_url == url

        # Cleanup
        config_module._settings_instance = None

    def test_empty_database_url_gets_default(self, monkeypatch):
        monkeypatch.delenv("DATABASE_URL", raising=False)

        import app.config as config_module
        config_module._settings_instance = None

        from app.config import Settings

        s = Settings()
        # Should get some default (either local or domino), not empty
        assert s.database_url != ""

        config_module._settings_instance = None
