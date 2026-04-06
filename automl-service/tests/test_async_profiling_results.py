"""Tests for async EDA result resolution via MLflow."""

import json
import os
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Optional
from unittest.mock import AsyncMock, MagicMock

import mlflow
import pytest
from fastapi import HTTPException

from app.api.routes.profiling import (
    AsyncProfileStartRequest,
    _build_async_status_response,
    _resolve_eda_job_result,
    start_profile_async,
)
from app.core.eda_job_metadata import EDA_JOB_REQUEST_ID_TAG, EDA_JOB_RESULT_ARTIFACT_PATH
from app.run_monkey_patching import MLFLOW_TRACKING_TOKEN_KEY


class DummyStore:
    def __init__(
        self,
        *,
        initial_state: dict[str, Any],
        initial_result: Optional[dict[str, Any]] = None,
        initial_error: Optional[str] = None,
    ):
        self.metadata = dict(initial_state)
        self.result_payload = dict(initial_result) if initial_result is not None else None
        self.error = initial_error if initial_error is not None else self.metadata.get("error")
        self.writes: list[tuple[str, str, dict[str, Any]]] = []
        self.update_calls: list[dict[str, Any]] = []

    async def get_request(self, incoming_request_id: str) -> dict[str, Any]:
        assert incoming_request_id == self.metadata["request_id"]
        return dict(self.metadata)

    async def get_result(self, incoming_request_id: str) -> Optional[dict[str, Any]]:
        assert incoming_request_id == self.metadata["request_id"]
        if self.result_payload is None:
            return None
        return dict(self.result_payload)

    async def update_request(self, incoming_request_id: str, **updates: Any) -> dict[str, Any]:
        assert incoming_request_id == self.metadata["request_id"]
        self.update_calls.append(dict(updates))
        self.metadata.update(updates)
        if "error" in updates:
            self.error = updates["error"]
        return dict(self.metadata)

    async def write_result(self, incoming_request_id: str, mode: str, result: dict[str, Any]) -> None:
        assert incoming_request_id == self.metadata["request_id"]
        self.writes.append((incoming_request_id, mode, result))
        self.result_payload = {
            "request_id": incoming_request_id,
            "mode": mode,
            "result": result,
        }

    async def get_error(self, incoming_request_id: str) -> Optional[str]:
        assert incoming_request_id == self.metadata["request_id"]
        return self.error


class DummyLauncher:
    def __init__(
        self,
        *,
        job_status_result: Optional[dict[str, Any]] = None,
        expected_domino_job_id: Optional[str] = None,
    ):
        self.job_status_result = dict(job_status_result) if job_status_result is not None else {}
        self.expected_domino_job_id = expected_domino_job_id

    async def get_job_status(self, domino_job_id: str) -> dict[str, Any]:
        if self.expected_domino_job_id is not None:
            assert domino_job_id == self.expected_domino_job_id
        return dict(self.job_status_result)


class DummyMlflowClient:
    def __init__(
        self,
        *,
        experiment: Optional[Any] = None,
        runs: Optional[list[Any]] = None,
        artifacts: Optional[list[Any]] = None,
        list_artifacts_error: Optional[Exception] = None,
    ):
        self.experiment = experiment
        self.runs = list(runs) if runs is not None else []
        self.artifacts = list(artifacts) if artifacts is not None else []
        self.list_artifacts_error = list_artifacts_error

    def get_experiment_by_name(self, experiment_name: str) -> Optional[Any]:
        return self.experiment

    def search_runs(self, **_: Any) -> list[Any]:
        return list(self.runs)

    def list_artifacts(self, run_id: str) -> list[Any]:
        if self.list_artifacts_error is not None:
            raise self.list_artifacts_error
        return list(self.artifacts)


def _patch_mlflow_client(monkeypatch, client: DummyMlflowClient) -> None:
    monkeypatch.setattr(
        "app.api.routes.profiling.mlflow.client.MlflowClient",
        lambda: client,
    )


def test_resolve_eda_job_result_downloads_artifact_by_request_id_tag(tmp_path, monkeypatch):
    tracking_uri = str(tmp_path / "mlruns")
    experiment_name = "eda-results-exp"
    request_id = "req-123"
    expected_result = {
        "summary": {"total_rows": 2},
        "warnings": [],
    }

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
    artifact_dir = tmp_path / "artifact_src"
    artifact_dir.mkdir()
    artifact_path = artifact_dir / EDA_JOB_RESULT_ARTIFACT_PATH
    artifact_path.write_text(json.dumps(expected_result), encoding="utf-8")

    with mlflow.start_run(tags={EDA_JOB_REQUEST_ID_TAG: request_id}):
        mlflow.log_artifact(str(artifact_path))

    assert _resolve_eda_job_result(request_id, experiment_name) == expected_result


def test_resolve_eda_job_result_raises_when_experiment_missing(monkeypatch):
    request_id = "req-missing-exp"
    experiment_name = "missing-exp"

    _patch_mlflow_client(monkeypatch, DummyMlflowClient(experiment=None))

    with pytest.raises(HTTPException) as exc_info:
        _resolve_eda_job_result(request_id, experiment_name)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == (
        f"MLflow experiment {experiment_name} not found while resolving EDA request {request_id}"
    )


def test_resolve_eda_job_result_raises_when_no_runs_found(monkeypatch):
    request_id = "req-no-runs"
    experiment_name = "eda-exp"

    _patch_mlflow_client(
        monkeypatch,
        DummyMlflowClient(
            experiment=SimpleNamespace(experiment_id="exp-1"),
            runs=[],
        ),
    )

    with pytest.raises(HTTPException) as exc_info:
        _resolve_eda_job_result(request_id, experiment_name)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == (
        f"No MLflow runs found for experiment {experiment_name} and EDA request {request_id}"
    )


def test_resolve_eda_job_result_raises_when_listing_artifacts_fails(monkeypatch):
    request_id = "req-artifacts"
    experiment_name = "eda-exp"
    run_id = "run-123"

    _patch_mlflow_client(
        monkeypatch,
        DummyMlflowClient(
            experiment=SimpleNamespace(experiment_id="exp-1"),
            runs=[SimpleNamespace(info=SimpleNamespace(run_id=run_id))],
            list_artifacts_error=RuntimeError("artifact listing failed"),
        ),
    )

    with pytest.raises(HTTPException) as exc_info:
        _resolve_eda_job_result(request_id, experiment_name)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == f"Failed listing MLflow artifacts for run {run_id}"


def test_resolve_eda_job_result_raises_when_artifact_download_fails(monkeypatch):
    request_id = "req-download"
    experiment_name = "eda-exp"
    run_id = "run-456"
    artifact_path = EDA_JOB_RESULT_ARTIFACT_PATH

    _patch_mlflow_client(
        monkeypatch,
        DummyMlflowClient(
            experiment=SimpleNamespace(experiment_id="exp-1"),
            runs=[SimpleNamespace(info=SimpleNamespace(run_id=run_id))],
            artifacts=[SimpleNamespace(path=artifact_path)],
        ),
    )
    monkeypatch.setattr(
        "app.api.routes.profiling.mlflow.artifacts.download_artifacts",
        lambda **_: (_ for _ in ()).throw(RuntimeError("download failed")),
    )

    with pytest.raises(HTTPException) as exc_info:
        _resolve_eda_job_result(request_id, experiment_name)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == (
        f"Failed downloading MLflow artifact {artifact_path} "
        f"for EDA request {request_id} from run {run_id}"
    )


@pytest.mark.asyncio
async def test_build_async_status_response_marks_eda_job_running_when_domino_job_not_completed(monkeypatch):
    request_id = "req-running"
    store = DummyStore(
        initial_state={
            "request_id": request_id,
            "status": "running",
            "mode": "tabular",
            "domino_job_id": "domino-job-1",
            "domino_job_status": "Queued",
            "experiment_name": "eda-exp",
            "error": None,
        },
    )
    launcher = DummyLauncher(
        job_status_result={
            "success": True,
            "domino_job_status": "Pending",
        },
        expected_domino_job_id="domino-job-1",
    )

    def fail_if_called(incoming_request_id, experiment_name):
        raise AssertionError(
            f"_resolve_eda_job_result should not be called while job {incoming_request_id} is still running"
        )

    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr("app.api.routes.profiling.get_domino_job_launcher", lambda: launcher)
    monkeypatch.setattr("app.api.routes.profiling._resolve_eda_job_result", fail_if_called)

    response = await _build_async_status_response(request_id)

    assert response.request_id == request_id
    assert response.status == "running"
    assert response.mode == "tabular"
    assert response.domino_job_status == "Pending"
    assert response.result is None
    assert response.error is None


@pytest.mark.asyncio
async def test_build_async_status_response_marks_eda_job_failed_for_failed_domino_status(monkeypatch):
    request_id = "req-failed"
    store = DummyStore(
        initial_state={
            "request_id": request_id,
            "status": "running",
            "mode": "tabular",
            "domino_job_id": "domino-job-2",
            "domino_job_status": "Running",
            "experiment_name": "eda-exp",
            "error": None,
        },
    )
    launcher = DummyLauncher(
        job_status_result={
            "success": True,
            "domino_job_status": "Failed",
        },
        expected_domino_job_id="domino-job-2",
    )
    expected_error = "Domino profiling job ended with status: Failed"

    def fail_if_called(incoming_request_id, experiment_name):
        raise AssertionError(
            f"_resolve_eda_job_result should not be called for failed job {incoming_request_id}"
        )

    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr("app.api.routes.profiling.get_domino_job_launcher", lambda: launcher)
    monkeypatch.setattr("app.api.routes.profiling._resolve_eda_job_result", fail_if_called)

    response = await _build_async_status_response(request_id)

    assert response.request_id == request_id
    assert response.status == "failed"
    assert response.mode == "tabular"
    assert response.domino_job_status == "Failed"
    assert response.result is None
    assert response.error == expected_error


@pytest.mark.asyncio
async def test_build_async_status_response_marks_eda_job_completed_for_successful_domino_status_and_fetches_results(monkeypatch):
    request_id = "req-completed"
    resolved_result = {"summary": {"total_rows": 10}}
    store = DummyStore(
        initial_state={
            "request_id": request_id,
            "status": "running",
            "mode": "tabular",
            "domino_job_id": "domino-job-3",
            "domino_job_status": "Running",
            "experiment_name": "eda-exp",
            "error": None,
        },
    )
    launcher = DummyLauncher(
        job_status_result={
            "success": True,
            "domino_job_status": "Succeeded",
        },
        expected_domino_job_id="domino-job-3",
    )

    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr("app.api.routes.profiling.get_domino_job_launcher", lambda: launcher)
    monkeypatch.setattr(
        "app.api.routes.profiling._resolve_eda_job_result",
        lambda incoming_request_id, experiment_name: resolved_result
        if experiment_name == "eda-exp" and incoming_request_id == request_id
        else None,
    )

    response = await _build_async_status_response(request_id)

    assert response.request_id == request_id
    assert response.status == "completed"
    assert response.result == resolved_result
    assert response.domino_job_status == "Succeeded"


@pytest.mark.asyncio
async def test_async_status_completion_route_resolves_result_with_request_tracking_token(
    app_client,
    monkeypatch,
):
    request_id = "req-completed-auth"
    resolved_result = {"summary": {"total_rows": 7}}
    store = DummyStore(
        initial_state={
            "request_id": request_id,
            "status": "running",
            "mode": "tabular",
            "domino_job_id": "domino-job-auth",
            "domino_job_status": "Running",
            "experiment_name": "eda-exp-auth",
            "error": None,
        },
    )
    launcher = DummyLauncher(
        job_status_result={
            "success": True,
            "domino_job_status": "Succeeded",
        },
        expected_domino_job_id="domino-job-auth",
    )

    # set a token, which shouldn't be returned, instead the value should resulv to
    # the request-token provided in the authorization request header
    monkeypatch.setenv(MLFLOW_TRACKING_TOKEN_KEY, "fallback-env-token")
    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr("app.api.routes.profiling.get_domino_job_launcher", lambda: launcher)

    # verifies that the requesting user's token is set as the mlflow_tracking_token
    def assert_tracking_token(incoming_request_id: str, experiment_name: str) -> dict[str, Any]:
        assert os.environ[MLFLOW_TRACKING_TOKEN_KEY] == "request-token"
        return resolved_result
    monkeypatch.setattr(
        "app.api.routes.profiling._resolve_eda_job_result",
        assert_tracking_token,
    )

    # send request to async status endpoint
    response = await app_client.post(
        "/svc/v1/profiling/profile/async/status",
        json={"request_id": request_id},
        headers={"authorization": "Bearer request-token"},
    )

    assert response.status_code == 200, response.text
    body = response.json()
    assert body["status"] == "completed"
    assert body["domino_job_status"] == "Succeeded"
    assert body["result"] == resolved_result


@pytest.mark.asyncio
async def test_build_async_status_response_requires_experiment_name(monkeypatch):
    request_id = "req-789"
    store = DummyStore(
        initial_state={
            "request_id": request_id,
            "status": "completed",
            "mode": "tabular",
            "domino_job_id": "domino-job-2",
            "domino_job_status": "Succeeded",
            "experiment_name": None,
            "error": None,
        },
    )
    resolve_called = False

    def fail_if_called(incoming_request_id, experiment_name):
        nonlocal resolve_called
        resolve_called = True
        raise AssertionError("experiment_name is required to resolve EDA results")

    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr(
        "app.api.routes.profiling.get_domino_job_launcher",
        lambda: DummyLauncher(),
    )
    monkeypatch.setattr("app.api.routes.profiling._resolve_eda_job_result", fail_if_called)

    with pytest.raises(HTTPException) as exc_info:
        await _build_async_status_response(request_id)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == (
        f"An experiment name wasn't created for EDA job request {request_id}"
    )
    assert not resolve_called
    assert store.writes == []


# ---------------------------------------------------------------------------
# start_profile_async — idempotency and force_restart behaviour
# ---------------------------------------------------------------------------


class DummyStartStore:
    """Minimal store stub for start_profile_async tests."""

    def __init__(self, existing: Optional[dict[str, Any]] = None):
        self._existing = existing
        self.deleted: list[tuple[str, str]] = []
        self.created: list[dict[str, Any]] = []
        self.update_calls: list[dict[str, Any]] = []

    async def get_by_job(self, job_id: str, mode: str) -> Optional[dict[str, Any]]:
        return dict(self._existing) if self._existing is not None else None

    async def delete_by_job(self, job_id: str, mode: str) -> None:
        self.deleted.append((job_id, mode))

    async def create_request(self, **kwargs: Any) -> dict[str, Any]:
        self.created.append(kwargs)
        return {"request_id": kwargs["request_id"], "status": "pending", **kwargs}

    async def update_request(self, request_id: str, **updates: Any) -> dict[str, Any]:
        self.update_calls.append({"request_id": request_id, **updates})
        return {}


def _patch_start_infra(monkeypatch, store: DummyStartStore, launch_result: Optional[dict] = None) -> None:
    monkeypatch.setattr("app.api.routes.profiling.require_domino_job_start", lambda **_: None)
    monkeypatch.setattr("app.api.routes.profiling.get_eda_job_store", lambda: store)
    monkeypatch.setattr(
        "app.api.routes.profiling.get_dataset_manager",
        lambda: MagicMock(get_dataset_path=AsyncMock(return_value="/domino/datasets/ds-123")),
    )
    if launch_result is not None:
        launcher = MagicMock(start_eda_job=AsyncMock(return_value=launch_result))
        monkeypatch.setattr("app.api.routes.profiling.get_domino_job_launcher", lambda: launcher)


def _tabular_request(**overrides: Any) -> AsyncProfileStartRequest:
    return AsyncProfileStartRequest(
        job_id="job-abc",
        mode="tabular",
        dataset_id="ds-123",
        file_path="train.csv",
        **overrides,
    )


@pytest.mark.asyncio
async def test_start_async_returns_completed_result_without_launching(monkeypatch):
    existing = {
        "request_id": "req-existing",
        "job_id": "job-abc",
        "status": "completed",
        "mode": "tabular",
        "domino_job_id": "dj-1",
        "domino_job_status": "Succeeded",
        "domino_job_url": None,
    }
    store = DummyStartStore(existing=existing)
    _patch_start_infra(monkeypatch, store)

    response = await start_profile_async(_tabular_request())

    assert response.request_id == "req-existing"
    assert response.status == "completed"
    assert store.deleted == []
    assert store.created == []


@pytest.mark.asyncio
async def test_start_async_returns_running_job_without_launching(monkeypatch):
    existing = {
        "request_id": "req-running",
        "job_id": "job-abc",
        "status": "running",
        "mode": "tabular",
        "domino_job_id": "dj-2",
        "domino_job_status": "Running",
        "domino_job_url": "http://domino/job/dj-2",
    }
    store = DummyStartStore(existing=existing)
    _patch_start_infra(monkeypatch, store)

    response = await start_profile_async(_tabular_request())

    assert response.request_id == "req-running"
    assert response.status == "running"
    assert response.domino_job_id == "dj-2"
    assert store.deleted == []
    assert store.created == []


@pytest.mark.asyncio
async def test_start_async_launches_new_job_when_none_exists(monkeypatch):
    store = DummyStartStore(existing=None)
    _patch_start_infra(
        monkeypatch,
        store,
        launch_result={"success": True, "domino_job_id": "dj-new", "domino_job_status": "Submitted"},
    )

    response = await start_profile_async(_tabular_request())

    assert response.status in ("pending", "running")
    assert response.domino_job_id == "dj-new"
    assert store.deleted == [("job-abc", "tabular")]
    assert len(store.created) == 1
    assert store.created[0]["job_id"] == "job-abc"


@pytest.mark.asyncio
async def test_start_async_force_restart_replaces_completed_job(monkeypatch):
    existing = {
        "request_id": "req-old",
        "job_id": "job-abc",
        "status": "completed",
        "mode": "tabular",
        "domino_job_id": "dj-old",
        "domino_job_status": "Succeeded",
        "domino_job_url": None,
    }
    store = DummyStartStore(existing=existing)
    _patch_start_infra(
        monkeypatch,
        store,
        launch_result={"success": True, "domino_job_id": "dj-fresh", "domino_job_status": "Submitted"},
    )

    response = await start_profile_async(_tabular_request(force_restart=True))

    assert response.domino_job_id == "dj-fresh"
    assert store.deleted == [("job-abc", "tabular")]
    assert len(store.created) == 1


@pytest.mark.asyncio
async def test_start_async_relaunches_when_existing_failed(monkeypatch):
    existing = {
        "request_id": "req-failed",
        "job_id": "job-abc",
        "status": "failed",
        "mode": "tabular",
        "domino_job_id": "dj-failed",
        "domino_job_status": "Failed",
        "domino_job_url": None,
    }
    store = DummyStartStore(existing=existing)
    _patch_start_infra(
        monkeypatch,
        store,
        launch_result={"success": True, "domino_job_id": "dj-retry", "domino_job_status": "Submitted"},
    )

    response = await start_profile_async(_tabular_request())

    assert response.domino_job_id == "dj-retry"
    assert store.deleted == [("job-abc", "tabular")]
    assert len(store.created) == 1
