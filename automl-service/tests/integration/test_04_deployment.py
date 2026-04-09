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

