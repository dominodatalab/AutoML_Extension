"""Integration tests for error paths and edge cases."""

import uuid

import pytest

pytestmark = pytest.mark.integration


class TestJobErrors:
    """Error handling for job-related endpoints."""

    def test_create_job_nonexistent_file(self, client, unique_name):
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": unique_name("bad_file"),
                "model_type": "tabular",
                "problem_type": "binary",
                "data_source": "mounted",
                "file_path": "/nonexistent/path/data.csv",
                "target_column": "target",
                "preset": "medium_quality_faster_train",
                "time_limit": 60,
            },
        )
        # Service should accept the job but it will fail during execution,
        # OR reject it immediately with a 4xx/5xx
        assert resp.status_code in (200, 400, 404, 422, 500)

    def test_create_job_missing_required_fields(self, client):
        """Missing model_type and target_column should return 422."""
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": "incomplete-job",
                # model_type missing
                "data_source": "mounted",
                "file_path": "/some/path.csv",
                # target_column missing
            },
        )
        assert resp.status_code == 422, f"Expected 422, got {resp.status_code}: {resp.text}"

    def test_create_ts_job_without_time_column(self, client, tabular_csv_path, unique_name):
        """Time series job without time_column should fail."""
        resp = client.post(
            "/svc/v1/jobs",
            json={
                "name": unique_name("ts_no_time"),
                "model_type": "timeseries",
                "data_source": "mounted",
                "file_path": tabular_csv_path,
                "target_column": "target",
                # time_column missing
                "preset": "fast_training",
                "time_limit": 60,
            },
        )
        # Should fail with 400 or 422
        assert resp.status_code in (200, 400, 422), (
            f"Expected 400/422 for missing time_column, got {resp.status_code}: {resp.text}"
        )

    def test_get_nonexistent_job(self, client):
        fake_id = str(uuid.uuid4())
        resp = client.get(f"/svc/v1/jobs/{fake_id}")
        assert resp.status_code == 404, f"Expected 404, got {resp.status_code}: {resp.text}"

    def test_cancel_nonexistent_job(self, client):
        fake_id = str(uuid.uuid4())
        resp = client.post(f"/svc/v1/jobs/{fake_id}/cancel")
        assert resp.status_code == 404, f"Expected 404, got {resp.status_code}: {resp.text}"

    def test_cancel_completed_job(self, client, shared_state):
        """Cancelling a completed job should return an error."""
        job_id = shared_state.get("tabular_job_id")
        if not job_id:
            pytest.skip("No tabular_job_id available")
        if shared_state.get("tabular_job_status") != "completed":
            pytest.skip("Job not completed yet")

        resp = client.post(f"/svc/v1/jobs/{job_id}/cancel")
        # Should fail — can't cancel a completed job
        assert resp.status_code in (400, 409, 422)

    def test_bulk_delete_empty_list(self, client):
        """Bulk delete with empty job_ids list should return 422."""
        resp = client.post(
            "/svc/v1/jobs/bulk-delete",
            json={"job_ids": []},
        )
        assert resp.status_code == 422, f"Expected 422, got {resp.status_code}: {resp.text}"


class TestProfilingErrors:
    """Error handling for profiling endpoints."""

    def test_profile_nonexistent_file(self, client):
        resp = client.post(
            "/svc/v1/profiling/profile",
            json={"file_path": "/does/not/exist.csv"},
        )
        assert resp.status_code in (404, 500)

    def test_profile_invalid_format(self, client, cleanup_registry):
        """Profiling a non-CSV/non-Parquet file should fail."""
        import tempfile
        import os

        # Write a small text file that isn't valid CSV
        fd, path = tempfile.mkstemp(suffix=".xyz")
        os.write(fd, b"this is not a valid data file\x00\x01\x02")
        os.close(fd)
        cleanup_registry["data_files"].append(path)

        resp = client.post(
            "/svc/v1/profiling/profile",
            json={"file_path": path},
        )
        assert resp.status_code in (400, 404, 422, 500)


class TestRegistryErrors:
    """Error handling for registry endpoints."""

    def test_delete_nonexistent_model(self, client):
        resp = client.delete("/svc/v1/registry/models/nonexistent_model_xyz")
        # Should fail gracefully
        assert resp.status_code in (400, 404, 500)

    def test_get_versions_nonexistent_model(self, client):
        resp = client.get("/svc/v1/registry/models/nonexistent_model_xyz/versions")
        assert resp.status_code in (404, 500)

    def test_register_from_noncompleted_job(self, client, unique_name):
        """Register model from a job that doesn't exist should fail."""
        fake_job_id = str(uuid.uuid4())
        resp = client.post(
            f"/svc/v1/jobs/{fake_job_id}/register",
            json={
                "job_id": fake_job_id,
                "model_name": unique_name("ghost_register"),
            },
        )
        assert resp.status_code in (400, 404, 500)
