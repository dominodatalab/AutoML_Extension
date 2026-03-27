"""Tests for app.services.job_links URL builder helpers."""

from types import SimpleNamespace
from typing import Optional
from unittest.mock import MagicMock

import pytest

from app.db.models import Job, JobStatus, ModelType
from app.services.job_links import (
    _build_domino_job_url,
    _build_experiment_run_url,
    _build_model_registry_url,
    _normalize_domino_ui_host,
    _resolve_project_name,
    attach_external_links,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_MOCK_LOGGER = MagicMock()


def _stub_job(**overrides) -> Job:
    """Build a lightweight Job instance for link tests."""
    defaults = dict(
        id="job-001",
        name="test-job",
        status=JobStatus.COMPLETED,
        model_type=ModelType.TABULAR,
        data_source="upload",
        target_column="target",
        owner="test-user",
        project_name="test-project",
        project_id="project-001",
        execution_target="domino_job",
        domino_job_id="run-abc-123",
        experiment_run_id=None,
        experiment_name=None,
        registered_model_name=None,
        registered_model_version=None,
    )
    defaults.update(overrides)
    job = MagicMock(spec=Job)
    for k, v in defaults.items():
        setattr(job, k, v)
    return job


def _clear_env(monkeypatch, keys):
    """Remove environment variables that could leak into tests."""
    for key in keys:
        monkeypatch.delenv(key, raising=False)


_DOMINO_ENV_KEYS = [
    "DOMINO_USER_HOST",
    "DOMINO_EXTERNAL_HOST",
    "DOMINO_LINK_HOST",
    "DOMINO_API_HOST",
    "DOMINO_PROJECT_OWNER",
    "DOMINO_PROJECT_NAME",
]


@pytest.fixture
def mock_project_details(monkeypatch):
    """Stub Domino project lookup used by link builders."""
    state = SimpleNamespace(project_id=None, owner_username="alice", name="my-proj")

    def configure(*, project_id=None, owner_username="alice", name="my-proj"):
        state.project_id = project_id
        state.owner_username = owner_username
        state.name = name

    def fake_resolve(project_id: str):
        state.project_id = project_id
        return SimpleNamespace(owner_username=state.owner_username, name=state.name)

    monkeypatch.setattr("app.services.job_links._resolve_project_details", fake_resolve)
    return SimpleNamespace(configure=configure, state=state)


@pytest.fixture(autouse=True)
def mock_job_links_settings(monkeypatch):
    """Isolate job-link tests from repo-local .env settings."""
    monkeypatch.setattr(
        "app.services.job_links.get_settings",
        lambda: SimpleNamespace(
            domino_api_host=None,
            domino_project_owner=None,
            domino_project_name=None,
            mlflow_tracking_uri=None,
        ),
    )


# ===========================================================================
# _normalize_domino_ui_host
# ===========================================================================


class TestNormalizeDominoUiHost:
    """Parametrized tests for URL normalization — kept from the original file."""

    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("https://apps.example.domino.tech", "https://example.domino.tech"),
            ("apps.example.domino.tech", "https://example.domino.tech"),
            ("https://apps.example.domino.tech:8443", "https://example.domino.tech:8443"),
            ("https://example.domino.tech", "https://example.domino.tech"),
            ("http://example.domino.tech", "http://example.domino.tech"),
            ("invalid://host", None),
            ("", None),
            (None, None),
        ],
    )
    def test_normalize_domino_ui_host(self, raw: Optional[str], expected: Optional[str]) -> None:
        assert _normalize_domino_ui_host(raw) == expected

    def test_whitespace_only_returns_none(self):
        assert _normalize_domino_ui_host("   ") is None

    def test_scheme_without_host_returns_none(self):
        assert _normalize_domino_ui_host("https://") is None

    def test_preserves_http_scheme(self):
        result = _normalize_domino_ui_host("http://my-domino.internal")
        assert result == "http://my-domino.internal"

    def test_strips_apps_prefix_with_port(self):
        result = _normalize_domino_ui_host("https://apps.company.domino.tech:9443")
        assert result == "https://company.domino.tech:9443"

    def test_bare_hostname_gets_https(self):
        result = _normalize_domino_ui_host("domino.example.com")
        assert result == "https://domino.example.com"


# ===========================================================================
# _build_domino_job_url
# ===========================================================================


class TestBuildDominoJobUrl:
    """Tests for _build_domino_job_url."""

    def test_returns_none_without_domino_job_id(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        job = _stub_job(domino_job_id=None)
        assert _build_domino_job_url(job) is None

    def test_returns_path_without_host(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")
        job = _stub_job(project_id="project-123")
        result = _build_domino_job_url(job)
        assert result == "/jobs/alice/my-proj/run-abc-123/logs?status=all"
        assert mock_project_details.state.project_id == "project-123"
        config_module._settings_instance = None

    def test_full_url_with_owner_and_project(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")
        job = _stub_job(domino_job_id="run-xyz", project_name="job-proj", project_id="project-456")
        result = _build_domino_job_url(job)
        assert result is not None
        assert "domino.example.com" in result
        assert "/jobs/alice/my-proj/run-xyz" in result
        assert "status=all" in result
        assert mock_project_details.state.project_id == "project-456"
        config_module._settings_instance = None

    def test_url_uses_project_name_from_domino_lookup(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="bob", name="from-domino")
        job = _stub_job(domino_job_id="run-1", project_name="from-job", project_id="project-789")
        result = _build_domino_job_url(job)
        assert "/jobs/bob/from-domino/run-1" in result
        assert "/from-job/" not in result
        assert mock_project_details.state.project_id == "project-789"
        config_module._settings_instance = None


# ===========================================================================
# _build_experiment_run_url
# ===========================================================================


class TestBuildExperimentRunUrl:
    """Tests for _build_experiment_run_url."""

    def test_returns_none_without_experiment_id(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        job = _stub_job()
        assert _build_experiment_run_url(job, experiment_id=None) is None

    def test_returns_none_without_project_id(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(project_id=None)
        result = _build_experiment_run_url(job, experiment_id="exp-100")
        assert result is None
        config_module._settings_instance = None

    def test_full_url_with_experiment_id(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")
        job = _stub_job(project_name="job-proj", project_id="project-321")
        result = _build_experiment_run_url(job, experiment_id="exp-42")
        assert result is not None
        assert "/experiments/alice/my-proj/exp-42" in result
        assert mock_project_details.state.project_id == "project-321"
        config_module._settings_instance = None


# ===========================================================================
# _build_model_registry_url
# ===========================================================================


class TestBuildModelRegistryUrl:
    """Tests for _build_model_registry_url."""

    def test_returns_none_without_registered_model_name(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        job = _stub_job(registered_model_name=None)
        assert _build_model_registry_url(job) is None

    def test_returns_none_without_project_id(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(registered_model_name="automlapp-model-1", project_id=None)
        result = _build_model_registry_url(job)
        assert result is None
        config_module._settings_instance = None

    def test_full_url_without_version(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")
        job = _stub_job(
            project_name="job-proj",
            project_id="project-654",
            registered_model_name="automlapp-model-1",
            registered_model_version=None,
        )
        result = _build_model_registry_url(job)
        assert result is not None
        assert "/model-registry/automlapp-model-1/model-card" in result
        assert "version=" not in result
        assert mock_project_details.state.project_id == "project-654"
        config_module._settings_instance = None

    def test_full_url_with_version(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")
        job = _stub_job(
            project_name="job-proj",
            project_id="project-987",
            registered_model_name="automlapp-model-1",
            registered_model_version="3",
        )
        result = _build_model_registry_url(job)
        assert result is not None
        assert "version=3" in result
        assert mock_project_details.state.project_id == "project-987"
        config_module._settings_instance = None


# ===========================================================================
# _resolve_project_name
# ===========================================================================


class TestResolveProjectName:
    """Tests for _resolve_project_name."""

    def test_prefers_job_project_name(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(project_name="from-job")
        assert _resolve_project_name(job) == "from-job"
        config_module._settings_instance = None

    def test_falls_back_to_env(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "from-env")
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(project_name=None)
        assert _resolve_project_name(job) == "from-env"
        config_module._settings_instance = None

    def test_returns_none_when_nothing_set(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(project_name=None)
        assert _resolve_project_name(job) is None
        config_module._settings_instance = None

    def test_blank_job_name_falls_back(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_PROJECT_NAME", "fallback")
        import app.config as config_module
        config_module._settings_instance = None
        job = _stub_job(project_name="   ")
        assert _resolve_project_name(job) == "fallback"
        config_module._settings_instance = None


# ===========================================================================
# attach_external_links
# ===========================================================================


class TestAttachExternalLinks:
    """Tests for attach_external_links — the top-level orchestrator."""

    def test_sets_all_four_attributes(self, monkeypatch, mock_project_details):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        monkeypatch.setenv("DOMINO_USER_HOST", "https://domino.example.com")
        import app.config as config_module
        config_module._settings_instance = None
        mock_project_details.configure(owner_username="alice", name="my-proj")

        job = _stub_job(
            project_name="job-proj",
            project_id="project-111",
            domino_job_id="run-1",
            registered_model_name="automlapp-my-model",
            registered_model_version="2",
            experiment_run_id=None,
            experiment_name=None,
        )

        logger = MagicMock()
        result = attach_external_links(job, logger)

        # domino_job_url
        assert hasattr(result, "domino_job_url")
        domino_url = getattr(result, "domino_job_url")
        assert domino_url is not None
        assert "/jobs/alice/my-proj/run-1" in domino_url

        # experiment_id (None since no MLflow run/name)
        assert hasattr(result, "experiment_id")

        # experiment_run_url (None since experiment_id is None)
        assert hasattr(result, "experiment_run_url")

        # model_registry_url
        assert hasattr(result, "model_registry_url")
        registry_url = getattr(result, "model_registry_url")
        assert registry_url is not None
        assert "/model-registry/automlapp-my-model/model-card" in registry_url
        assert "version=2" in registry_url
        assert mock_project_details.state.project_id == "project-111"

        config_module._settings_instance = None

    def test_all_links_none_when_no_context(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        import app.config as config_module
        config_module._settings_instance = None

        job = _stub_job(
            domino_job_id=None,
            registered_model_name=None,
            experiment_run_id=None,
            experiment_name=None,
            project_name=None,
        )

        logger = MagicMock()
        result = attach_external_links(job, logger)
        assert getattr(result, "domino_job_url") is None
        assert getattr(result, "experiment_run_url") is None
        assert getattr(result, "model_registry_url") is None

        config_module._settings_instance = None

    def test_returns_same_job_object(self, monkeypatch):
        _clear_env(monkeypatch, _DOMINO_ENV_KEYS)
        import app.config as config_module
        config_module._settings_instance = None

        job = _stub_job(domino_job_id=None, registered_model_name=None)
        logger = MagicMock()
        result = attach_external_links(job, logger)
        assert result is job

        config_module._settings_instance = None
