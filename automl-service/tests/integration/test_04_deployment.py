"""Integration tests for deployment endpoints."""

import pytest

from .conftest import has_domino_auth

pytestmark = pytest.mark.integration


class TestDeployments:
    """Model API and deployment lifecycle tests.

    These tests require a live Domino environment with deployment capabilities.
    """

    @pytest.fixture(autouse=True)
    def _require_domino(self):
        if not has_domino_auth():
            pytest.skip("Deployment tests require Domino credentials (checked DOMINO_API_KEY, DOMINO_USER_API_KEY, DOMINO_TOKEN_FILE, DOMINO_API_PROXY)")

    def test_list_model_apis(self, client):
        resp = client.get("/svc/v1/deployments/model-apis")
        assert resp.status_code == 200, f"List model APIs failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        # Endpoint returns {"success": bool, "data": [...]}
        assert body.get("success") is True, f"List model APIs not successful: {body}"
        assert isinstance(body.get("data"), list)

    def test_list_deployments(self, client):
        resp = client.get("/svc/v1/deployments/deployments")
        assert resp.status_code == 200, f"List deployments failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        # Endpoint returns {"success": bool, "data": [...]}
        assert body.get("success") is True, f"List deployments not successful: {body}"
        assert isinstance(body.get("data"), list)

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
            if body.get("success"):
                # deploy_from_job returns model_api_id at top level
                model_api_id = body.get("model_api_id")
                if model_api_id:
                    shared_state["model_api_id"] = model_api_id
                    cleanup_registry["model_apis"].append(model_api_id)
        else:
            pytest.skip(f"Deploy-from-job not available: {resp.status_code} {resp.text}")

    @pytest.mark.slow
    def test_get_model_api_details(self, client, shared_state):
        model_api_id = shared_state.get("model_api_id")
        if not model_api_id:
            pytest.skip("No model API created from deploy-from-job")

        resp = client.get(f"/svc/v1/deployments/model-apis/{model_api_id}")
        assert resp.status_code == 200, (
            f"Get model API failed ({resp.status_code}): {resp.text}"
        )
        body = resp.json()
        assert body.get("success") is True, f"Get model API not successful: {body}"
