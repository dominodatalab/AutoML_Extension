"""Tests for the profiling API endpoints.

Covers:
- POST /svc/v1/profiling/profile — tabular data profiling
- POST /svc/v1/profiling/profile/timeseries — time series profiling
- POST /svc/v1/profiling/profile/suggest-target — target column suggestions
- GET  /svc/v1/profiling/profile/presets — training presets
- GET  /svc/v1/profiling/profile/metrics — evaluation metrics

.. note:: Requires the ``domino`` package (available in Domino runtime).
"""

import pytest

pytestmark = pytest.mark.domino


# ---------------------------------------------------------------------------
# POST /svc/v1/profiling/profile — tabular profiling
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_profile_tabular_csv(app_client, tabular_csv):
    """POST /svc/v1/profiling/profile returns a full profile for a tabular CSV."""
    response = await app_client.post(
        "/svc/v1/profiling/profile",
        json={"file_path": tabular_csv},
    )

    assert response.status_code == 200
    body = response.json()

    # Verify top-level response shape
    assert "summary" in body
    assert "columns" in body
    assert "correlations" in body
    assert "recommendations" in body
    assert "warnings" in body

    # Verify summary fields
    summary = body["summary"]
    assert summary["total_rows"] == 200
    assert summary["total_columns"] == 8
    assert isinstance(summary["memory_usage_mb"], (int, float))
    assert isinstance(summary["duplicate_rows"], int)
    assert isinstance(summary["duplicate_percentage"], (int, float))
    assert "sampled" in summary
    assert "sample_size" in summary

    # Verify columns list
    columns = body["columns"]
    assert len(columns) == 8
    col_names = [c["name"] for c in columns]
    assert "age" in col_names
    assert "income" in col_names
    assert "target" in col_names
    assert "category" in col_names

    # Verify each column has required fields
    for col in columns:
        assert "name" in col
        assert "dtype" in col
        assert "missing_count" in col
        assert "missing_percentage" in col
        assert "unique_count" in col
        assert "unique_percentage" in col
        assert "semantic_type" in col


@pytest.mark.asyncio
async def test_profile_tabular_csv_with_sampling(app_client, tabular_csv):
    """POST /svc/v1/profiling/profile respects sample_size parameter."""
    response = await app_client.post(
        "/svc/v1/profiling/profile",
        json={
            "file_path": tabular_csv,
            "sample_size": 50,
            "sampling_strategy": "head",
        },
    )

    assert response.status_code == 200
    body = response.json()
    # With only 200 rows and sample_size=50, it should sample
    summary = body["summary"]
    assert summary["sample_size"] <= 200


@pytest.mark.asyncio
async def test_profile_nonexistent_file(app_client):
    """POST /svc/v1/profiling/profile with nonexistent file returns 404."""
    response = await app_client.post(
        "/svc/v1/profiling/profile",
        json={"file_path": "/nonexistent/path/to/data.csv"},
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_profile_missing_file_path(app_client):
    """POST /svc/v1/profiling/profile without file_path returns 422."""
    response = await app_client.post(
        "/svc/v1/profiling/profile",
        json={},
    )

    assert response.status_code == 422


# ---------------------------------------------------------------------------
# POST /svc/v1/profiling/profile/timeseries — time series profiling
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_profile_timeseries_csv(app_client, timeseries_csv):
    """POST /svc/v1/profiling/profile/timeseries returns a time series profile."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/timeseries",
        json={
            "file_path": timeseries_csv,
            "time_column": "timestamp",
            "target_column": "value",
            "id_column": "item_id",
        },
    )

    assert response.status_code == 200
    body = response.json()

    # Verify top-level response shape
    assert "temporal_summary" in body
    assert "gap_analysis" in body
    assert "target_statistics" in body
    assert "recommendations" in body
    assert "warnings" in body

    # Temporal summary should have data about the series
    assert isinstance(body["temporal_summary"], dict)
    assert isinstance(body["target_statistics"], dict)


@pytest.mark.asyncio
async def test_profile_timeseries_without_id_column(app_client, timeseries_csv):
    """POST /svc/v1/profiling/profile/timeseries works without id_column (single series)."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/timeseries",
        json={
            "file_path": timeseries_csv,
            "time_column": "timestamp",
            "target_column": "value",
            # no id_column — treats entire file as one series
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert "temporal_summary" in body


@pytest.mark.asyncio
async def test_profile_timeseries_missing_required_fields(app_client, timeseries_csv):
    """POST /svc/v1/profiling/profile/timeseries without time_column returns 422."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/timeseries",
        json={
            "file_path": timeseries_csv,
            # missing time_column and target_column
        },
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_profile_timeseries_nonexistent_file(app_client):
    """POST /svc/v1/profiling/profile/timeseries with nonexistent file returns 404."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/timeseries",
        json={
            "file_path": "/nonexistent/path/to/ts.csv",
            "time_column": "timestamp",
            "target_column": "value",
        },
    )

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# POST /svc/v1/profiling/profile/suggest-target — target suggestions
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_suggest_target_columns(app_client, tabular_csv):
    """POST /svc/v1/profiling/profile/suggest-target returns target suggestions."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/suggest-target",
        json={"file_path": tabular_csv},
    )

    assert response.status_code == 200
    body = response.json()
    assert "suggestions" in body
    assert isinstance(body["suggestions"], list)

    # The tabular CSV has a 'target' column that should be suggested
    if body["suggestions"]:
        suggestion = body["suggestions"][0]
        assert "column" in suggestion
        assert "score" in suggestion
        assert "reasons" in suggestion
        assert "problem_type" in suggestion
        assert isinstance(suggestion["reasons"], list)


@pytest.mark.asyncio
async def test_suggest_target_nonexistent_file(app_client):
    """POST /svc/v1/profiling/profile/suggest-target with nonexistent file returns 404."""
    response = await app_client.post(
        "/svc/v1/profiling/profile/suggest-target",
        json={"file_path": "/nonexistent/path.csv"},
    )

    assert response.status_code == 404


# ---------------------------------------------------------------------------
# GET /svc/v1/profiling/profile/presets — training presets
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_presets(app_client):
    """GET /svc/v1/profiling/profile/presets returns tabular and timeseries presets."""
    response = await app_client.get("/svc/v1/profiling/profile/presets")

    assert response.status_code == 200
    body = response.json()

    assert "tabular" in body
    assert "timeseries" in body
    assert isinstance(body["tabular"], list)
    assert isinstance(body["timeseries"], list)

    # Each preset should have value, label, description, time_multiplier
    for preset in body["tabular"]:
        assert "value" in preset
        assert "label" in preset
        assert "description" in preset
        assert "time_multiplier" in preset

    for preset in body["timeseries"]:
        assert "value" in preset
        assert "label" in preset
        assert "description" in preset
        assert "time_multiplier" in preset

    # Verify expected preset values are present
    tabular_values = [p["value"] for p in body["tabular"]]
    assert "best_quality" in tabular_values
    assert "medium_quality_faster_train" in tabular_values

    ts_values = [p["value"] for p in body["timeseries"]]
    assert "best_quality" in ts_values
    assert "chronos" in ts_values


# ---------------------------------------------------------------------------
# GET /svc/v1/profiling/profile/metrics — evaluation metrics
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_metrics(app_client):
    """GET /svc/v1/profiling/profile/metrics returns metrics by problem type."""
    response = await app_client.get("/svc/v1/profiling/profile/metrics")

    assert response.status_code == 200
    body = response.json()

    assert "binary" in body
    assert "multiclass" in body
    assert "regression" in body
    assert "timeseries" in body

    # Each problem type contains a list of metric dicts
    for problem_type in ["binary", "multiclass", "regression", "timeseries"]:
        metrics = body[problem_type]
        assert isinstance(metrics, list)
        assert len(metrics) > 0
        for metric in metrics:
            assert "value" in metric
            assert "label" in metric
            assert "description" in metric

    # Spot-check some known metrics
    binary_values = [m["value"] for m in body["binary"]]
    assert "accuracy" in binary_values
    assert "roc_auc" in binary_values
    assert "f1" in binary_values

    regression_values = [m["value"] for m in body["regression"]]
    assert "root_mean_squared_error" in regression_values
    assert "r2" in regression_values

    ts_values = [m["value"] for m in body["timeseries"]]
    assert "MASE" in ts_values
    assert "RMSE" in ts_values
