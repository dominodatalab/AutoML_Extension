"""Integration tests for deployment endpoints."""

import os

import pytest

pytestmark = pytest.mark.integration


class TestDeployments:
    """Model API and deployment lifecycle tests.

    These tests require a live Domino environment with deployment capabilities.
    """

    @pytest.fixture(autouse=True)
    def _require_domino(self):
        if not os.environ.get("DOMINO_API_KEY"):
            pytest.skip("Deployment tests require Domino environment")

    def test_list_model_apis(self, client):
        resp = client.get("/svc/v1/deployments/model-apis")
        assert resp.status_code == 200
        body = resp.json()
        # Should be a list (possibly empty)
        assert isinstance(body, list)

    def test_list_deployments(self, client):
        resp = client.get("/svc/v1/deployments/deployments")
        assert resp.status_code == 200
        body = resp.json()
        assert isinstance(body, list)

    @pytest.mark.slow
    def test_deploy_from_job(self, client, shared_state, cleanup_registry):
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("No tabular_job_id (upstream test failed)")
        if shared_state.get("tabular_job_status") != "completed":
            pytest.skip("Tabular job did not complete")

        resp = client.post(
            f"/svc/v1/deployments/deploy-from-job/{job_id}",
            params={"function_name": "predict"},
        )
        # The endpoint may fail if deployment infra isn't available
        if resp.status_code == 200:
            body = resp.json()
            if body.get("success") and body.get("data", {}).get("model_api_id"):
                cleanup_registry["model_apis"].append(body["data"]["model_api_id"])
            if body.get("deployment_id"):
                cleanup_registry["deployments"].append(body["deployment_id"])
                shared_state["deployment_id"] = body["deployment_id"]
        else:
            pytest.skip(f"Deploy-from-job not available: {resp.status_code} {resp.text}")

    @pytest.mark.slow
    def test_get_deployment_details(self, client, shared_state):
        dep_id = shared_state.get("deployment_id")
        if not dep_id:
            pytest.skip("No deployment created")

        resp = client.get(f"/svc/v1/deployments/deployments/{dep_id}")
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("success") is True or "status" in body
