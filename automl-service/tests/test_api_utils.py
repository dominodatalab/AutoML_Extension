"""Tests for shared API request helpers."""

from types import SimpleNamespace

import pytest
from starlette.requests import Request

from app.api.utils import get_job_paths, resolve_request_project_id


def _make_request(*, headers=None, query_string: bytes = b"") -> Request:
    encoded_headers = [
        (key.lower().encode("latin-1"), value.encode("latin-1"))
        for key, value in (headers or {}).items()
    ]
    return Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": encoded_headers,
            "query_string": query_string,
        }
    )


def test_resolve_request_project_id_ignores_header(monkeypatch):
    """X-Project-Id header is not used — only query params."""
    monkeypatch.delenv("DOMINO_PROJECT_ID", raising=False)
    request = _make_request(headers={"X-Project-Id": "header-proj"})

    assert resolve_request_project_id(request) is None


def test_resolve_request_project_id_reads_camel_case_query_param(monkeypatch):
    monkeypatch.delenv("DOMINO_PROJECT_ID", raising=False)
    request = _make_request(query_string=b"projectId=query-proj")

    assert resolve_request_project_id(request) == "query-proj"


def test_resolve_request_project_id_reads_snake_case_query_param(monkeypatch):
    monkeypatch.delenv("DOMINO_PROJECT_ID", raising=False)
    request = _make_request(query_string=b"project_id=query-proj")

    assert resolve_request_project_id(request) == "query-proj"


def test_resolve_request_project_id_ignores_environment_variable(monkeypatch):
    """DOMINO_PROJECT_ID is the App's own project — never use it as fallback."""
    monkeypatch.setenv("DOMINO_PROJECT_ID", "env-proj")

    assert resolve_request_project_id(None) is None


def test_resolve_request_project_id_none_without_request():
    assert resolve_request_project_id(None) is None


@pytest.mark.asyncio
async def test_get_job_paths_uses_get_job_or_404(monkeypatch):
    db = object()
    calls: list[tuple[object, str]] = []

    job = SimpleNamespace(
        id="job-123",
        status=SimpleNamespace(value="completed"),
        model_path="runs:/run-123/autogluon_model",
        model_type=SimpleNamespace(value="tabular"),
        file_path="/mnt/data/train.csv",
        problem_type=SimpleNamespace(value="binary"),
    )

    async def fake_get_job_or_404(db_session, job_id: str):
        calls.append((db_session, job_id))
        return job

    monkeypatch.setattr("app.api.utils.get_job_or_404", fake_get_job_or_404)
    monkeypatch.setattr(
        "app.api.utils.download_mlflow_artifact",
        lambda model_path, job_id: f"/tmp/cache/{job_id}",
    )

    result = await get_job_paths(db, "job-123")

    assert calls == [(db, "job-123")]
    assert result == (
        "/tmp/cache/job-123",
        "tabular",
        "/mnt/data/train.csv",
        "binary",
    )
