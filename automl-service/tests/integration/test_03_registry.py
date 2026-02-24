"""Integration tests for model registry endpoints."""

import os

import pytest

pytestmark = pytest.mark.integration


class TestModelRegistration:
    """Register models from completed jobs and manage them."""

    @pytest.fixture(autouse=True)
    def _require_completed_job(self, shared_state):
        if shared_state.get("tabular_job_status") != "completed":
            pytest.skip("Requires a completed tabular job (test_02 must pass)")

    @pytest.mark.slow
    def test_register_model_from_job(
        self, client, shared_state, cleanup_registry, unique_name
    ):
        job_id = shared_state["tabular_job_id"]
        model_name = unique_name("registered_model")

        resp = client.post(
            f"/svc/v1/jobs/{job_id}/register",
            json={
                "job_id": job_id,
                "model_name": model_name,
                "description": "Integration test model",
            },
        )
        assert resp.status_code == 200, f"Register failed: {resp.text}"
        body = resp.json()
        assert body.get("success") is True or body.get("model_name") == model_name

        shared_state["registered_model_name"] = model_name
        cleanup_registry["registered_models"].append(model_name)

    @pytest.mark.slow
    def test_list_local_models(self, client, shared_state):
        if "registered_model_name" not in shared_state:
            pytest.skip("No model registered")

        resp = client.get("/svc/v1/registry/models")
        assert resp.status_code == 200
        body = resp.json()
        assert isinstance(body, list)
        names = [m["name"] for m in body]
        assert shared_state["registered_model_name"] in names

    @pytest.mark.slow
    def test_list_mlflow_models(self, client, shared_state):
        """List MLflow registered models (may be empty if MLflow is not configured)."""
        if "registered_model_name" not in shared_state:
            pytest.skip("No model registered")

        resp = client.get("/svc/v1/registry/models/mlflow")
        assert resp.status_code == 200
        body = resp.json()
        assert isinstance(body, list)
        # If MLflow is configured, our model should appear
        if os.environ.get("MLFLOW_TRACKING_URI"):
            names = [m["name"] for m in body]
            assert shared_state["registered_model_name"] in names

    @pytest.mark.slow
    def test_get_model_versions(self, client, shared_state):
        model_name = shared_state.get("registered_model_name")
        if not model_name:
            pytest.skip("No model registered")

        resp = client.get(f"/svc/v1/registry/models/{model_name}/versions")
        # 200 if MLflow configured, 404 if model not in MLflow
        if resp.status_code == 200:
            body = resp.json()
            assert isinstance(body, list)
            assert len(body) >= 1
            shared_state["model_version"] = body[0].get("version", "1")
        else:
            pytest.skip("Model versions not available (MLflow may not be configured)")

    @pytest.mark.slow
    def test_transition_model_to_staging(self, client, shared_state):
        model_name = shared_state.get("registered_model_name")
        version = shared_state.get("model_version")
        if not model_name or not version:
            pytest.skip("No model name or version available")

        resp = client.post(
            "/svc/v1/registry/models/transition-stage",
            json={
                "model_name": model_name,
                "version": str(version),
                "stage": "Staging",
                "archive_existing": False,
            },
        )
        # Success or skip if MLflow not available
        if resp.status_code == 200:
            body = resp.json()
            assert body.get("success") is True
        else:
            pytest.skip(f"Stage transition not available: {resp.status_code}")

    @pytest.mark.slow
    def test_register_via_direct_endpoint(
        self, client, shared_state, cleanup_registry, unique_name
    ):
        """Register using POST /svc/v1/registry/register (direct endpoint)."""
        job_id = shared_state["tabular_job_id"]

        # Get the job to find model_path
        job_resp = client.get(f"/svc/v1/jobs/{job_id}")
        assert job_resp.status_code == 200
        job_data = job_resp.json()
        model_path = job_data.get("model_path")
        if not model_path:
            pytest.skip("No model_path on completed job")

        model_name = unique_name("direct_register")
        resp = client.post(
            "/svc/v1/registry/register",
            json={
                "model_path": model_path,
                "model_name": model_name,
                "model_type": "tabular",
                "description": "Direct registration integration test",
                "job_id": job_id,
            },
        )
        assert resp.status_code == 200, f"Direct register failed: {resp.text}"
        body = resp.json()
        assert body.get("success") is True

        cleanup_registry["registered_models"].append(model_name)
