"""Tests for app.services.model_service."""

import uuid
from pathlib import Path
import sys

import pytest
import pytest_asyncio

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.utils import utc_now
from app.db.models import RegisteredModel
from app.services.model_service import list_registered_models_response


# ---------------------------------------------------------------------------
# list_registered_models_response
# ---------------------------------------------------------------------------


class TestListRegisteredModelsResponse:
    """Tests for list_registered_models_response."""

    @pytest.mark.asyncio
    async def test_empty_table_returns_empty_list(self, db_session) -> None:
        result = await list_registered_models_response(db_session)
        assert result == []

    @pytest.mark.asyncio
    async def test_single_model_returned(self, db_session, make_job) -> None:
        job = make_job(name="train-1")
        db_session.add(job)
        await db_session.flush()

        model = RegisteredModel(
            id=str(uuid.uuid4()),
            name="my-model",
            description="A test model",
            job_id=job.id,
            version=1,
            mlflow_model_uri="models:/my-model/1",
            domino_model_id=None,
            deployed=False,
            created_at=utc_now(),
        )
        db_session.add(model)
        await db_session.flush()

        result = await list_registered_models_response(db_session)

        assert len(result) == 1
        resp = result[0]
        assert resp.id == model.id
        assert resp.name == "my-model"
        assert resp.description == "A test model"
        assert resp.job_id == job.id
        assert resp.version == 1
        assert resp.mlflow_model_uri == "models:/my-model/1"
        assert resp.domino_model_id is None
        assert resp.deployed is False
        assert resp.created_at == model.created_at

    @pytest.mark.asyncio
    async def test_multiple_models_returned(self, db_session, make_job) -> None:
        job = make_job(name="train-multi")
        db_session.add(job)
        await db_session.flush()

        now = utc_now()
        model_a = RegisteredModel(
            id=str(uuid.uuid4()),
            name="model-alpha",
            job_id=job.id,
            version=1,
            deployed=False,
            created_at=now,
        )
        model_b = RegisteredModel(
            id=str(uuid.uuid4()),
            name="model-beta",
            description="Beta variant",
            job_id=job.id,
            version=2,
            deployed=True,
            domino_model_id="domino-xyz",
            created_at=now,
        )
        db_session.add_all([model_a, model_b])
        await db_session.flush()

        result = await list_registered_models_response(db_session)

        assert len(result) == 2
        names = {r.name for r in result}
        assert names == {"model-alpha", "model-beta"}

    @pytest.mark.asyncio
    async def test_response_objects_are_pydantic_models(self, db_session, make_job) -> None:
        """Verify that each item is a RegisteredModelResponse Pydantic instance."""
        from app.api.schemas.model import RegisteredModelResponse

        job = make_job(name="train-pydantic")
        db_session.add(job)
        await db_session.flush()

        model = RegisteredModel(
            id=str(uuid.uuid4()),
            name="pydantic-check",
            job_id=job.id,
            version=1,
            deployed=False,
            created_at=utc_now(),
        )
        db_session.add(model)
        await db_session.flush()

        result = await list_registered_models_response(db_session)

        assert len(result) == 1
        assert isinstance(result[0], RegisteredModelResponse)

    @pytest.mark.asyncio
    async def test_optional_fields_default_to_none(self, db_session, make_job) -> None:
        """Models with no description, mlflow_model_uri, or domino_model_id
        should still serialize correctly with None defaults."""
        job = make_job(name="train-defaults")
        db_session.add(job)
        await db_session.flush()

        model = RegisteredModel(
            id=str(uuid.uuid4()),
            name="bare-minimum",
            job_id=job.id,
            version=1,
            deployed=False,
            created_at=utc_now(),
        )
        db_session.add(model)
        await db_session.flush()

        result = await list_registered_models_response(db_session)

        assert len(result) == 1
        resp = result[0]
        assert resp.description is None
        assert resp.mlflow_model_uri is None
        assert resp.domino_model_id is None
