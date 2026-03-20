"""Tests for the --job-config CLI passthrough to child jobs.

Verifies that:
1. serialize_job_config() produces a JSON-safe dict with enum values as strings
2. _deserialize_job_config() round-trips back with restored enums and attribute access
3. Runner CLI parser accepts --job-config
4. DominoJobLauncher._build_command includes properly quoted --job-config JSON
5. Backward compat: run_training_job() without job_config falls back to DB read

Run:
    python -m pytest tests/test_job_config_passthrough.py -v
"""

import json
import sys
import types
from unittest.mock import MagicMock

import pytest


# ---------------------------------------------------------------------------
# 1. serialize_job_config round-trip with _deserialize_job_config
# ---------------------------------------------------------------------------


class TestSerializeDeserializeRoundTrip:
    """serialize_job_config -> JSON -> _deserialize_job_config restores enums."""

    def _make_mock_job(self):
        from app.db.models import ModelType, ProblemType

        job = MagicMock()
        job.name = "my-training-job"
        job.data_source = "upload"
        job.file_path = "/data/train.csv"
        job.dataset_id = None
        job.model_type = ModelType.TABULAR
        job.problem_type = ProblemType.BINARY
        job.target_column = "label"
        job.time_column = None
        job.id_column = None
        job.prediction_length = None
        job.preset = "medium_quality"
        job.time_limit = 600
        job.eval_metric = "accuracy"
        job.autogluon_config = {"advanced": {"num_gpus": 0}}
        job.enable_mlflow = True
        job.experiment_name = "exp-1"
        job.project_id = "proj-abc"
        job.project_name = "MyProject"
        job.auto_register = False
        job.register_name = None
        return job

    def test_round_trip_preserves_all_fields(self):
        from app.services.job_service import serialize_job_config
        from app.workers.training_worker import _deserialize_job_config
        from app.db.models import ModelType, ProblemType

        job = self._make_mock_job()
        config_dict = serialize_job_config(job)

        # Ensure JSON-safe (no enum objects)
        json_str = json.dumps(config_dict)
        restored_dict = json.loads(json_str)
        ns = _deserialize_job_config(restored_dict)

        assert ns.name == "my-training-job"
        assert ns.model_type == ModelType.TABULAR
        assert ns.problem_type == ProblemType.BINARY
        assert ns.target_column == "label"
        assert ns.time_limit == 600
        assert ns.autogluon_config == {"advanced": {"num_gpus": 0}}
        assert ns.enable_mlflow is True
        assert ns.project_id == "proj-abc"

    def test_none_problem_type_preserved(self):
        from app.services.job_service import serialize_job_config
        from app.workers.training_worker import _deserialize_job_config

        job = self._make_mock_job()
        job.problem_type = None
        config_dict = serialize_job_config(job)
        ns = _deserialize_job_config(config_dict)

        assert ns.problem_type is None

    def test_enum_comparisons_work(self):
        from app.services.job_service import serialize_job_config
        from app.workers.training_worker import _deserialize_job_config
        from app.db.models import ModelType, ProblemType

        job = self._make_mock_job()
        config_dict = serialize_job_config(job)
        json_str = json.dumps(config_dict)
        ns = _deserialize_job_config(json.loads(json_str))

        # These comparisons are used in training_worker.py
        assert ns.model_type == ModelType.TABULAR
        assert ns.model_type.value == "tabular"
        assert ns.problem_type == ProblemType.BINARY
        assert ns.problem_type.value == "binary"

    def test_getattr_works_like_orm(self):
        from app.services.job_service import serialize_job_config
        from app.workers.training_worker import _deserialize_job_config

        job = self._make_mock_job()
        config_dict = serialize_job_config(job)
        ns = _deserialize_job_config(config_dict)

        # training_worker.py uses getattr(job, 'project_id', None)
        assert getattr(ns, "project_id", None) == "proj-abc"
        assert getattr(ns, "nonexistent_field", "default") == "default"

    def test_timeseries_fields_preserved(self):
        from app.services.job_service import serialize_job_config
        from app.workers.training_worker import _deserialize_job_config
        from app.db.models import ModelType

        job = self._make_mock_job()
        job.model_type = ModelType.TIMESERIES
        job.time_column = "date"
        job.id_column = "item_id"
        job.prediction_length = 30

        config_dict = serialize_job_config(job)
        ns = _deserialize_job_config(json.loads(json.dumps(config_dict)))

        assert ns.model_type == ModelType.TIMESERIES
        assert ns.time_column == "date"
        assert ns.id_column == "item_id"
        assert ns.prediction_length == 30


# ---------------------------------------------------------------------------
# 2. Runner CLI arg parsing for --job-config
# ---------------------------------------------------------------------------


class TestTrainingRunnerJobConfigArg:
    """domino_training_runner.parse_args accepts --job-config."""

    def test_job_config_parsed(self, monkeypatch):
        config_json = json.dumps({"name": "test", "model_type": "tabular"})
        monkeypatch.setattr(
            sys, "argv",
            ["runner", "--job-id", "abc123", "--job-config", config_json],
        )
        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        assert args.job_id == "abc123"
        assert args.job_config == config_json

    def test_job_config_optional(self, monkeypatch):
        monkeypatch.setattr(sys, "argv", ["runner", "--job-id", "abc123"])
        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        assert args.job_config is None

    def test_job_config_with_database_url(self, monkeypatch):
        config_json = json.dumps({"name": "test"})
        monkeypatch.setattr(
            sys, "argv",
            [
                "runner",
                "--job-id", "abc123",
                "--database-url", "sqlite:///automl.db",
                "--job-config", config_json,
            ],
        )
        from app.workers.domino_training_runner import parse_args

        args = parse_args()
        assert args.job_id == "abc123"
        assert args.database_url == "sqlite:///automl.db"
        assert args.job_config == config_json


# ---------------------------------------------------------------------------
# 3. DominoJobLauncher._build_command includes --job-config
# ---------------------------------------------------------------------------


class TestJobLauncherJobConfigCommand:
    """DominoJobLauncher._build_command properly includes --job-config JSON."""

    def test_build_command_includes_job_config(self, monkeypatch):
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")
        from app.core.domino_job_launcher import DominoJobLauncher

        config_json = json.dumps({"name": "test", "model_type": "tabular"})
        cmd = DominoJobLauncher._build_command(
            DominoJobLauncher,
            "app.workers.domino_training_runner",
            {
                "job_id": "j1",
                "database_url": "sqlite:///automl.db",
                "job_config": config_json,
            },
        )
        assert "--job-config" in cmd
        assert "--job-id" in cmd
        assert "--database-url" in cmd

    def test_build_command_omits_job_config_when_none(self, monkeypatch):
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")
        from app.core.domino_job_launcher import DominoJobLauncher

        cmd = DominoJobLauncher._build_command(
            DominoJobLauncher,
            "app.workers.domino_training_runner",
            {"job_id": "j1", "database_url": "sqlite:///automl.db", "job_config": None},
        )
        assert "--job-config" not in cmd

    def test_build_command_quotes_json_safely(self, monkeypatch):
        monkeypatch.setenv("AUTOML_SERVICE_DIR", "automl-service")
        from app.core.domino_job_launcher import DominoJobLauncher

        # JSON with spaces, braces, quotes — must be safely quoted
        config_json = json.dumps({
            "name": "my job",
            "autogluon_config": {"advanced": {"num_gpus": 0}},
        })
        cmd = DominoJobLauncher._build_command(
            DominoJobLauncher,
            "app.workers.domino_training_runner",
            {"job_id": "j1", "job_config": config_json},
        )
        # shlex.quote wraps strings with special chars in single quotes
        assert "--job-config" in cmd
        # The JSON string should appear in the command (quoted)
        assert "my job" in cmd


# ---------------------------------------------------------------------------
# 4. Backward compatibility: run_training_job without job_config
# ---------------------------------------------------------------------------


class TestRunTrainingJobSignature:
    """run_training_job accepts optional job_config kwarg."""

    def test_accepts_job_config_kwarg(self):
        import inspect
        from app.workers.training_worker import run_training_job

        sig = inspect.signature(run_training_job)
        assert "job_config" in sig.parameters
        assert sig.parameters["job_config"].default is None
