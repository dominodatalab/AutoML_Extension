"""Integration tests for training job lifecycle."""

import pytest

from .conftest import has_domino_auth
from .helpers import poll_job_until_terminal

pytestmark = pytest.mark.integration


class TestLocalTabularTraining:
    """Create and run a tabular training job locally."""

    def test_create_tabular_job(
        self, client, tabular_csv_path, shared_state, cleanup_registry, unique_name
    ):
        job_name = unique_name("tabular_binary")
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": job_name,
                "model_type": "tabular",
                "problem_type": "binary",
                "data_source": "mounted",
                "file_path": tabular_csv_path,
                "target_column": "target",
                "preset": "medium_quality_faster_train",
                "time_limit": 120,
            },
        )
        assert resp.status_code == 200, f"Create job failed: {resp.text}"
        body = resp.json()
        assert "id" in body
        assert body["status"] in ("pending", "running")

        shared_state["tabular_job_id"] = body["id"]
        shared_state["tabular_job_name"] = job_name
        cleanup_registry["job_ids"].append(body["id"])

    @pytest.mark.slow
    def test_tabular_job_completes(self, client, shared_state):
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("tabular_job_id not set (upstream test failed)")

        result = poll_job_until_terminal(
            client, job_id, timeout=600.0, interval=10.0,
        )
        assert result["status"] == "completed", (
            f"Job did not complete successfully: {result}"
        )
        shared_state["tabular_job_status"] = result["status"]

    @pytest.mark.slow
    def test_tabular_job_has_metrics(self, client, shared_state):
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("tabular_job_id not set")
        if shared_state.get("tabular_job_status") != "completed":
            pytest.skip("tabular job did not complete")

        resp = client.get(f"/svc/v1/jobs/{job_id}/metrics")
        assert resp.status_code == 200, f"Get metrics failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert body.get("metrics"), "Metrics should not be empty for a completed job"

    @pytest.mark.slow
    def test_tabular_job_has_leaderboard(self, client, shared_state):
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("tabular_job_id not set")
        if shared_state.get("tabular_job_status") != "completed":
            pytest.skip("tabular job did not complete")

        resp = client.get(f"/svc/v1/jobs/{job_id}")
        assert resp.status_code == 200, f"Get job failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert body.get("leaderboard"), "Leaderboard should not be empty"
        assert len(body["leaderboard"]) >= 1

    @pytest.mark.slow
    def test_tabular_job_in_list(self, client, shared_state):
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("tabular_job_id not set")

        resp = client.get("/svc/v1/jobs")
        assert resp.status_code == 200, f"List jobs failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        job_ids = [j["id"] for j in body["jobs"]]
        assert job_id in job_ids


class TestLocalTimeSeriesTraining:
    """Create and run a time series training job locally."""

    def test_create_ts_job(
        self, client, timeseries_csv_path, shared_state, cleanup_registry, unique_name
    ):
        job_name = unique_name("ts_forecast")
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": job_name,
                "model_type": "timeseries",
                "data_source": "mounted",
                "file_path": timeseries_csv_path,
                "target_column": "value",
                "time_column": "timestamp",
                "id_column": "item_id",
                "prediction_length": 7,
                "preset": "fast_training",
                "time_limit": 120,
            },
        )
        assert resp.status_code == 200, f"Create TS job failed: {resp.text}"
        body = resp.json()
        assert "id" in body

        shared_state["ts_job_id"] = body["id"]
        cleanup_registry["job_ids"].append(body["id"])

    @pytest.mark.slow
    def test_ts_job_completes(self, client, shared_state):
        job_id = shared_state.get("ts_job_id")
        if not job_id:
            pytest.skip("ts_job_id not set")

        result = poll_job_until_terminal(
            client, job_id, timeout=600.0, interval=10.0,
        )
        assert result["status"] == "completed", (
            f"TS job did not complete successfully: {result}"
        )
        shared_state["ts_job_status"] = result["status"]

    @pytest.mark.slow
    def test_ts_job_has_metrics(self, client, shared_state):
        job_id = shared_state.get("ts_job_id")
        if not job_id:
            pytest.skip("ts_job_id not set")
        if shared_state.get("ts_job_status") != "completed":
            pytest.skip("TS job did not complete")

        resp = client.get(f"/svc/v1/jobs/{job_id}/metrics")
        assert resp.status_code == 200, f"Get TS metrics failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert body.get("metrics"), "TS metrics should not be empty"


class TestDominoJobTraining:
    """Training via Domino Job execution target. Skipped if not in Domino."""

    @pytest.fixture(autouse=True)
    def _require_domino(self):
        if not has_domino_auth():
            pytest.skip("No Domino credentials found (checked DOMINO_API_KEY, DOMINO_USER_API_KEY, DOMINO_TOKEN_FILE, DOMINO_API_PROXY)")

    def test_create_domino_job(
        self, client, tabular_csv_path, shared_state, cleanup_registry, unique_name
    ):
        job_name = unique_name("domino_tabular")
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": job_name,
                "model_type": "tabular",
                "problem_type": "binary",
                "data_source": "mounted",
                "file_path": tabular_csv_path,
                "target_column": "target",
                "preset": "medium_quality_faster_train",
                "time_limit": 120,
            },
        )
        assert resp.status_code == 200, f"Create domino job failed: {resp.text}"
        body = resp.json()
        assert "id" in body
        assert body.get("domino_job_id"), "domino_job_id should be set for domino_job target"

        shared_state["domino_job_id"] = body["id"]
        cleanup_registry["job_ids"].append(body["id"])

    @pytest.mark.slow
    def test_domino_job_completes(self, client, shared_state):
        job_id = shared_state.get("domino_job_id")
        if not job_id:
            pytest.skip("domino_job_id not set")

        result = poll_job_until_terminal(
            client, job_id, timeout=900.0, interval=15.0,
        )
        assert result["status"] == "completed", (
            f"Domino job did not complete: {result}"
        )
        shared_state["domino_job_status"] = result["status"]
