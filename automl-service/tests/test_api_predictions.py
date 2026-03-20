"""Tests for prediction/diagnostics API endpoints."""

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from app.db.models import JobStatus


class TestFeatureImportanceEndpoint:
    """Feature-importance endpoint behavior for stored diagnostics fallbacks."""

    @pytest.mark.asyncio
    async def test_recomputes_when_stored_feature_importance_has_error(
        self,
        app_client,
        db_session,
        make_job,
        monkeypatch,
    ):
        job = make_job(
            status=JobStatus.COMPLETED,
            model_path="/tmp/model",
            file_path="/tmp/data.csv",
            project_id="proj-1",
            diagnostics_data={
                "get_feature_importance": {
                    "model_type": "tabular",
                    "method": "auto",
                    "features": [],
                    "error": "stored failure",
                }
            },
        )
        db_session.add(job)
        await db_session.commit()

        monkeypatch.setattr(
            "app.api.routes.predictions.get_job_paths",
            AsyncMock(return_value=("/tmp/model", "tabular", "/tmp/data.csv", None)),
        )
        monkeypatch.setattr(
            "app.api.routes.predictions.ensure_local_file",
            AsyncMock(return_value="/tmp/data.csv"),
        )
        monkeypatch.setattr(
            "app.api.routes.predictions.get_model_diagnostics",
            lambda: SimpleNamespace(
                get_feature_importance=lambda **_: {
                    "model_path": "/tmp/model",
                    "model_type": "tabular",
                    "method": "live",
                    "features": [{"feature": "age", "importance": 0.42}],
                }
            ),
        )

        response = await app_client.post(
            "/svc/v1/predictions/model/feature-importance",
            json={"job_id": job.id, "model_type": "tabular"},
        )

        assert response.status_code == 200, response.text
        body = response.json()
        assert body["job_id"] == job.id
        assert body["method"] == "live"
        assert body["features"] == [{"feature": "age", "importance": 0.42}]

    @pytest.mark.asyncio
    async def test_recomputes_when_stored_feature_importance_is_empty(
        self,
        app_client,
        db_session,
        make_job,
        monkeypatch,
    ):
        job = make_job(
            status=JobStatus.COMPLETED,
            model_path="/tmp/model",
            file_path="/tmp/data.csv",
            project_id="proj-1",
            diagnostics_data={
                "get_feature_importance": {
                    "model_type": "timeseries",
                    "method": "auto",
                    "features": [],
                    "error": None,
                }
            },
        )
        db_session.add(job)
        await db_session.commit()

        monkeypatch.setattr(
            "app.api.routes.predictions.get_job_paths",
            AsyncMock(return_value=("/tmp/model", "timeseries", "/tmp/data.csv", None)),
        )
        monkeypatch.setattr(
            "app.api.routes.predictions.ensure_local_file",
            AsyncMock(return_value="/tmp/data.csv"),
        )
        monkeypatch.setattr(
            "app.api.routes.predictions.get_model_diagnostics",
            lambda: SimpleNamespace(
                get_feature_importance=lambda **_: {
                    "model_path": "/tmp/model",
                    "model_type": "timeseries",
                    "method": "live",
                    "features": [{"feature": "promo", "importance": 0.51}],
                }
            ),
        )

        response = await app_client.post(
            "/svc/v1/predictions/model/feature-importance",
            json={"job_id": job.id, "model_type": "timeseries"},
        )

        assert response.status_code == 200, response.text
        body = response.json()
        assert body["job_id"] == job.id
        assert body["method"] == "live"
        assert body["features"] == [{"feature": "promo", "importance": 0.51}]
