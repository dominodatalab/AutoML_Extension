"""Integration tests for model registry endpoints."""

import pytest

from .conftest import has_domino_auth

pytestmark = pytest.mark.integration


# See DOM-75049: https://dominodatalab.atlassian.net/browse/DOM-75049
@pytest.mark.skip(reason="DOM-75049: integration tests disabled in sandbox")
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
        assert body.get("success") is True, f"Registration not successful: {body}"

        # The backend prefixes model_name with "automlapp-" — capture the
        # actual registered name from the response for downstream tests.
        actual_name = body.get("model_name", model_name)
        shared_state["registered_model_name"] = actual_name
        cleanup_registry["registered_models"].append(actual_name)

    @pytest.mark.slow
    def test_list_mlflow_models(self, client, shared_state):
        """Verify the registered model appears in the Domino/MLflow registry."""
        if "registered_model_name" not in shared_state:
            pytest.skip("No model registered")

        resp = client.get("/svc/v1/registry/models/mlflow")
        assert resp.status_code == 200, f"List MLflow models failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert isinstance(body, list)
        names = [m["name"] for m in body]
        assert shared_state["registered_model_name"] in names, (
            f"Registered model '{shared_state['registered_model_name']}' not found in MLflow registry. "
            f"Available models: {names}"
        )

    @pytest.mark.slow
    def test_list_local_models(self, client):
        """Verify the local model listing endpoint returns a valid list.

        Note: models registered via POST /jobs/{id}/register go to the
        Domino/MLflow registry, not the local DB.  This test only checks
        that the local listing endpoint itself works (returns 200 + list).
        """
        resp = client.get("/svc/v1/registry/models")
        assert resp.status_code == 200, f"List local models failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert isinstance(body, list)

    @pytest.mark.slow
    def test_get_model_versions(self, client, shared_state):
        model_name = shared_state.get("registered_model_name")
        if not model_name:
            pytest.skip("No model registered")

        resp = client.get(f"/svc/v1/registry/models/{model_name}/versions")
        assert resp.status_code == 200, (
            f"Get model versions failed ({resp.status_code}): {resp.text}"
        )
        body = resp.json()
        assert isinstance(body, list)
        assert len(body) >= 1, f"Expected at least 1 version, got {body}"
        shared_state["model_version"] = body[0].get("version", "1")

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
        assert resp.status_code == 200, (
            f"Stage transition failed ({resp.status_code}): {resp.text}"
        )
        body = resp.json()
        assert body.get("success") is True

    @pytest.mark.slow
    def test_register_via_direct_endpoint(
        self, client, shared_state, cleanup_registry, unique_name
    ):
        """Register using POST /svc/v1/registry/register (direct endpoint).

        This endpoint writes to both MLflow and the local DB.
        """
        if not has_domino_auth():
            pytest.skip("Direct registration requires Domino credentials")

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
        assert body.get("success") is True, (
            f"Direct registration failed: {body.get('error')}"
        )

        actual_name = body.get("model_name", model_name)
        cleanup_registry["registered_models"].append(actual_name)
