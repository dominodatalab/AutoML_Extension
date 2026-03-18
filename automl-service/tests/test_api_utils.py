"""Tests for shared API request helpers."""

from starlette.requests import Request

from app.api.utils import resolve_request_project_id


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


def test_resolve_request_project_id_prefers_header(monkeypatch):
    monkeypatch.setenv("DOMINO_PROJECT_ID", "env-proj")
    request = _make_request(
        headers={"X-Project-Id": "header-proj"},
        query_string=b"project_id=query-proj",
    )

    assert resolve_request_project_id(request) == "header-proj"


def test_resolve_request_project_id_reads_camel_case_query_param(monkeypatch):
    monkeypatch.delenv("DOMINO_PROJECT_ID", raising=False)
    request = _make_request(query_string=b"projectId=query-proj")

    assert resolve_request_project_id(request) == "query-proj"


def test_resolve_request_project_id_reads_snake_case_query_param(monkeypatch):
    monkeypatch.delenv("DOMINO_PROJECT_ID", raising=False)
    request = _make_request(query_string=b"project_id=query-proj")

    assert resolve_request_project_id(request) == "query-proj"


def test_resolve_request_project_id_falls_back_to_environment(monkeypatch):
    monkeypatch.setenv("DOMINO_PROJECT_ID", "env-proj")

    assert resolve_request_project_id(None) == "env-proj"
