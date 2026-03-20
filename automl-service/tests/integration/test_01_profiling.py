"""Integration tests for data profiling endpoints."""

import pytest

pytestmark = pytest.mark.integration


class TestTabularProfiling:
    """Tabular data profiling via POST /svc/v1/profiling/profile."""

    def test_profile_tabular_csv(self, client, tabular_csv_path):
        resp = client.post(
            "/svc/v1/profiling/profile",
            json={"file_path": tabular_csv_path},
        )
        assert resp.status_code == 200, f"Profile tabular failed ({resp.status_code}): {resp.text}"
        body = resp.json()

        # Summary
        summary = body["summary"]
        assert summary["total_rows"] == 500
        assert summary["total_columns"] >= 7
        assert isinstance(summary["memory_usage_mb"], (int, float))

        # Columns
        assert len(body["columns"]) >= 7
        col_names = {c["name"] for c in body["columns"]}
        assert "target" in col_names
        assert "income" in col_names

        # Correlations should be present
        assert isinstance(body.get("correlations"), dict)

    def test_profile_with_sampling(self, client, tabular_csv_path):
        resp = client.post(
            "/svc/v1/profiling/profile",
            json={
                "file_path": tabular_csv_path,
                "sample_size": 100,
                "sampling_strategy": "random",
            },
        )
        assert resp.status_code == 200, f"Profile with sampling failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        # With 500-row file and sample_size=100, sampling should engage
        summary = body["summary"]
        assert summary["sample_size"] <= 500

    def test_suggest_target(self, client, tabular_csv_path):
        resp = client.post(
            "/svc/v1/profiling/profile/suggest-target",
            json={"file_path": tabular_csv_path},
        )
        assert resp.status_code == 200, f"Suggest target failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert "suggestions" in body
        assert len(body["suggestions"]) > 0
        # "target" column should appear in suggestions
        suggested_cols = [s["column"] for s in body["suggestions"]]
        assert "target" in suggested_cols

    def test_profile_nonexistent_file(self, client):
        resp = client.post(
            "/svc/v1/profiling/profile",
            json={"file_path": "/nonexistent/path/to/data.csv"},
        )
        assert resp.status_code in (404, 500)


class TestTimeSeriesProfiling:
    """Time series profiling via POST /svc/v1/profiling/profile/timeseries."""

    def test_profile_timeseries(self, client, timeseries_csv_path):
        resp = client.post(
            "/svc/v1/profiling/profile/timeseries",
            json={
                "file_path": timeseries_csv_path,
                "time_column": "timestamp",
                "target_column": "value",
                "id_column": "item_id",
            },
        )
        assert resp.status_code == 200, f"Profile TS failed ({resp.status_code}): {resp.text}"
        body = resp.json()

        # Should have temporal summary
        assert "temporal_summary" in body
        assert body["temporal_summary"]  # non-empty

        # Stationarity and autocorrelation
        assert "stationarity" in body
        assert "autocorrelation" in body

    def test_profile_ts_wrong_time_column(self, client, timeseries_csv_path):
        resp = client.post(
            "/svc/v1/profiling/profile/timeseries",
            json={
                "file_path": timeseries_csv_path,
                "time_column": "nonexistent_col",
                "target_column": "value",
            },
        )
        # Should fail with a client or server error
        assert resp.status_code >= 400


class TestPresetsAndMetrics:
    """Static endpoints for presets and metrics."""

    def test_get_presets(self, client):
        resp = client.get("/svc/v1/profiling/profile/presets")
        assert resp.status_code == 200, f"Get presets failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        assert "tabular" in body
        assert "timeseries" in body
        assert len(body["tabular"]) > 0
        assert len(body["timeseries"]) > 0

    def test_get_metrics(self, client):
        resp = client.get("/svc/v1/profiling/profile/metrics")
        assert resp.status_code == 200, f"Get metrics failed ({resp.status_code}): {resp.text}"
        body = resp.json()
        for problem_type in ("binary", "multiclass", "regression", "timeseries"):
            assert problem_type in body
            assert len(body[problem_type]) > 0
