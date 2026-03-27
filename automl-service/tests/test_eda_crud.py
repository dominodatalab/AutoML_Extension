"""Tests for EDA CRUD operations (app.db.crud) and EDAJobStore (app.core.eda_job_store)."""

import json
import uuid
from datetime import timedelta

import pytest
import pytest_asyncio
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.eda_job_store import EDAJobStore
from app.core.utils import utc_now
from app.db import crud
from app.db.models import EDAResult


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rid() -> str:
    return str(uuid.uuid4())


SAMPLE_PAYLOAD = {"dataset": "iris.csv", "target": "species"}
SAMPLE_RESULT = {"accuracy": 0.95, "features": ["a", "b"]}


# ===========================================================================
# CRUD function tests
# ===========================================================================


class TestCreateEdaRequest:
    """Tests for crud.create_eda_request."""

    @pytest.mark.asyncio
    async def test_basic_creation(self, db_session: AsyncSession):
        rid = _rid()
        eda = await crud.create_eda_request(db_session, rid, "tabular", SAMPLE_PAYLOAD)
        assert eda.id == rid
        assert eda.status == "pending"
        assert eda.mode == "tabular"
        assert json.loads(eda.request_payload) == SAMPLE_PAYLOAD
        assert eda.owner is None
        assert eda.project_id is None

    @pytest.mark.asyncio
    async def test_creation_with_owner_and_project(self, db_session: AsyncSession):
        rid = _rid()
        eda = await crud.create_eda_request(
            db_session, rid, "timeseries", {"ts": True},
            owner="alice", project_id="proj-123",
        )
        assert eda.owner == "alice"
        assert eda.project_id == "proj-123"
        assert eda.mode == "timeseries"

    @pytest.mark.asyncio
    async def test_created_at_populated(self, db_session: AsyncSession):
        eda = await crud.create_eda_request(db_session, _rid(), "tabular", {})
        assert eda.created_at is not None
        assert eda.updated_at is not None

    @pytest.mark.asyncio
    async def test_result_and_error_initially_none(self, db_session: AsyncSession):
        eda = await crud.create_eda_request(db_session, _rid(), "tabular", {})
        assert eda.result_payload is None
        assert eda.error is None

    @pytest.mark.asyncio
    async def test_domino_fields_initially_none(self, db_session: AsyncSession):
        eda = await crud.create_eda_request(db_session, _rid(), "tabular", {})
        assert eda.domino_job_id is None
        assert eda.domino_job_status is None
        assert eda.domino_job_url is None


class TestGetEdaRequest:
    """Tests for crud.get_eda_request."""

    @pytest.mark.asyncio
    async def test_get_existing(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", SAMPLE_PAYLOAD)
        eda = await crud.get_eda_request(db_session, rid)
        assert eda is not None
        assert eda.id == rid

    @pytest.mark.asyncio
    async def test_get_nonexistent_returns_none(self, db_session: AsyncSession):
        result = await crud.get_eda_request(db_session, "no-such-id")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_with_matching_owner(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {}, owner="bob")
        eda = await crud.get_eda_request(db_session, rid, owner="bob")
        assert eda is not None
        assert eda.owner == "bob"

    @pytest.mark.asyncio
    async def test_get_with_wrong_owner_returns_none(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {}, owner="bob")
        eda = await crud.get_eda_request(db_session, rid, owner="eve")
        assert eda is None

    @pytest.mark.asyncio
    async def test_get_without_owner_filter_returns_any(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {}, owner="charlie")
        eda = await crud.get_eda_request(db_session, rid)
        assert eda is not None


class TestUpdateEdaRequest:
    """Tests for crud.update_eda_request."""

    @pytest.mark.asyncio
    async def test_update_status(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        updated = await crud.update_eda_request(db_session, rid, status="running")
        assert updated is not None
        assert updated.status == "running"

    @pytest.mark.asyncio
    async def test_update_domino_fields(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        updated = await crud.update_eda_request(
            db_session, rid,
            domino_job_id="dj-123",
            domino_job_status="Succeeded",
            domino_job_url="https://domino.example/jobs/dj-123",
        )
        assert updated.domino_job_id == "dj-123"
        assert updated.domino_job_status == "Succeeded"
        assert updated.domino_job_url == "https://domino.example/jobs/dj-123"

    @pytest.mark.asyncio
    async def test_update_sets_updated_at(self, db_session: AsyncSession):
        rid = _rid()
        eda = await crud.create_eda_request(db_session, rid, "tabular", {})
        original_updated = eda.updated_at
        updated = await crud.update_eda_request(db_session, rid, status="running")
        assert updated.updated_at >= original_updated

    @pytest.mark.asyncio
    async def test_update_nonexistent_returns_none(self, db_session: AsyncSession):
        result = await crud.update_eda_request(db_session, "ghost-id", status="running")
        assert result is None

    @pytest.mark.asyncio
    async def test_update_ignores_none_values(self, db_session: AsyncSession):
        """None values in updates are skipped (per the hasattr+not-None check)."""
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {}, owner="alice")
        updated = await crud.update_eda_request(db_session, rid, owner=None)
        # owner should remain unchanged because None values are skipped
        assert updated.owner == "alice"

    @pytest.mark.asyncio
    async def test_update_multiple_fields(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        updated = await crud.update_eda_request(
            db_session, rid, status="completed", error="none",
        )
        assert updated.status == "completed"
        assert updated.error == "none"


class TestWriteEdaResult:
    """Tests for crud.write_eda_result."""

    @pytest.mark.asyncio
    async def test_write_result(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        eda = await crud.write_eda_result(db_session, rid, "tabular", SAMPLE_RESULT)
        assert eda.status == "completed"
        assert json.loads(eda.result_payload) == SAMPLE_RESULT
        assert eda.error is None

    @pytest.mark.asyncio
    async def test_write_result_updates_mode(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        eda = await crud.write_eda_result(db_session, rid, "timeseries", SAMPLE_RESULT)
        assert eda.mode == "timeseries"

    @pytest.mark.asyncio
    async def test_write_result_after_error_sets_completed(self, db_session: AsyncSession):
        """write_eda_result passes error=None, but update_eda_request skips None
        values, so the previous error string is preserved. Status is updated."""
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        await crud.write_eda_error(db_session, rid, "oops")
        eda = await crud.write_eda_result(db_session, rid, "tabular", SAMPLE_RESULT)
        assert eda.status == "completed"
        # error=None is skipped by update_eda_request's `value is not None` guard,
        # so the previous error string persists.
        assert eda.error == "oops"

    @pytest.mark.asyncio
    async def test_write_result_nonexistent_returns_none(self, db_session: AsyncSession):
        result = await crud.write_eda_result(db_session, "nope", "tabular", {})
        assert result is None


class TestWriteEdaError:
    """Tests for crud.write_eda_error."""

    @pytest.mark.asyncio
    async def test_write_error(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        eda = await crud.write_eda_error(db_session, rid, "Something broke")
        assert eda.status == "failed"
        assert eda.error == "Something broke"

    @pytest.mark.asyncio
    async def test_write_error_nonexistent_returns_none(self, db_session: AsyncSession):
        result = await crud.write_eda_error(db_session, "nope", "error msg")
        assert result is None


class TestGetEdaResult:
    """Tests for crud.get_eda_result."""

    @pytest.mark.asyncio
    async def test_get_result_after_write(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        await crud.write_eda_result(db_session, rid, "tabular", SAMPLE_RESULT)
        result = await crud.get_eda_result(db_session, rid)
        assert result == SAMPLE_RESULT

    @pytest.mark.asyncio
    async def test_get_result_pending_returns_none(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        result = await crud.get_eda_result(db_session, rid)
        assert result is None

    @pytest.mark.asyncio
    async def test_get_result_nonexistent_returns_none(self, db_session: AsyncSession):
        result = await crud.get_eda_result(db_session, "no-id")
        assert result is None


class TestDeleteStaleEdaResults:
    """Tests for crud.delete_stale_eda_results."""

    @pytest.mark.asyncio
    async def test_deletes_old_records(self, db_session: AsyncSession):
        # Create a record and manually backdate it
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        old_time = utc_now() - timedelta(hours=100)
        await db_session.execute(
            update(EDAResult).where(EDAResult.id == rid).values(created_at=old_time)
        )
        await db_session.commit()

        deleted = await crud.delete_stale_eda_results(db_session, max_age_hours=72.0)
        assert deleted == 1

        # Confirm it's gone
        assert await crud.get_eda_request(db_session, rid) is None

    @pytest.mark.asyncio
    async def test_keeps_recent_records(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        deleted = await crud.delete_stale_eda_results(db_session, max_age_hours=72.0)
        assert deleted == 0
        assert await crud.get_eda_request(db_session, rid) is not None

    @pytest.mark.asyncio
    async def test_custom_max_age(self, db_session: AsyncSession):
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", {})
        # Backdate by 2 hours
        old_time = utc_now() - timedelta(hours=2)
        await db_session.execute(
            update(EDAResult).where(EDAResult.id == rid).values(created_at=old_time)
        )
        await db_session.commit()

        # 1 hour cutoff should delete it
        deleted = await crud.delete_stale_eda_results(db_session, max_age_hours=1.0)
        assert deleted == 1

    @pytest.mark.asyncio
    async def test_mixed_old_and_new(self, db_session: AsyncSession):
        old_rid = _rid()
        new_rid = _rid()
        await crud.create_eda_request(db_session, old_rid, "tabular", {})
        await crud.create_eda_request(db_session, new_rid, "tabular", {})

        old_time = utc_now() - timedelta(hours=100)
        await db_session.execute(
            update(EDAResult).where(EDAResult.id == old_rid).values(created_at=old_time)
        )
        await db_session.commit()

        deleted = await crud.delete_stale_eda_results(db_session, max_age_hours=72.0)
        assert deleted == 1
        assert await crud.get_eda_request(db_session, old_rid) is None
        assert await crud.get_eda_request(db_session, new_rid) is not None


# ===========================================================================
# EDAJobStore tests
# ===========================================================================


class TestEDAJobStoreCreateRequest:
    """Tests for EDAJobStore.create_request."""

    @pytest.mark.asyncio
    async def test_returns_dict(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        result = await store.create_request(db_session, rid, "tabular", SAMPLE_PAYLOAD)
        assert isinstance(result, dict)
        assert result["request_id"] == rid
        assert result["status"] == "pending"
        assert result["mode"] == "tabular"

    @pytest.mark.asyncio
    async def test_includes_owner_and_project(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        result = await store.create_request(
            db_session, rid, "tabular", {}, owner="dana", project_id="p-1",
        )
        assert result["owner"] == "dana"
        assert result["project_id"] == "p-1"

    @pytest.mark.asyncio
    async def test_dict_has_all_expected_keys(self, db_session: AsyncSession):
        store = EDAJobStore()
        result = await store.create_request(db_session, _rid(), "tabular", {})
        expected_keys = {
            "request_id", "status", "mode", "owner", "project_id",
            "domino_job_id", "domino_job_status", "domino_job_url",
            "error", "created_at", "updated_at",
        }
        assert set(result.keys()) == expected_keys


class TestEDAJobStoreGetRequest:
    """Tests for EDAJobStore.get_request."""

    @pytest.mark.asyncio
    async def test_get_existing(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        result = await store.get_request(db_session, rid)
        assert result is not None
        assert result["request_id"] == rid

    @pytest.mark.asyncio
    async def test_get_nonexistent_returns_none(self, db_session: AsyncSession):
        store = EDAJobStore()
        result = await store.get_request(db_session, "missing")
        assert result is None


class TestEDAJobStoreUpdateRequest:
    """Tests for EDAJobStore.update_request."""

    @pytest.mark.asyncio
    async def test_update_returns_dict(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        result = await store.update_request(db_session, rid, status="running")
        assert result is not None
        assert result["status"] == "running"

    @pytest.mark.asyncio
    async def test_update_nonexistent_returns_none(self, db_session: AsyncSession):
        store = EDAJobStore()
        result = await store.update_request(db_session, "ghost", status="running")
        assert result is None

    @pytest.mark.asyncio
    async def test_update_domino_job_fields(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        result = await store.update_request(
            db_session, rid,
            domino_job_id="dj-456",
            domino_job_status="Running",
        )
        assert result["domino_job_id"] == "dj-456"
        assert result["domino_job_status"] == "Running"


class TestEDAJobStoreWriteResult:
    """Tests for EDAJobStore.write_result."""

    @pytest.mark.asyncio
    async def test_write_and_get_result(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        await store.write_result(db_session, rid, "tabular", SAMPLE_RESULT)

        result = await store.get_result(db_session, rid)
        assert result is not None
        assert result["request_id"] == rid
        assert result["mode"] == "tabular"
        assert result["result"] == SAMPLE_RESULT

    @pytest.mark.asyncio
    async def test_write_result_updates_status(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        await store.write_result(db_session, rid, "tabular", SAMPLE_RESULT)

        req = await store.get_request(db_session, rid)
        assert req["status"] == "completed"


class TestEDAJobStoreGetResult:
    """Tests for EDAJobStore.get_result."""

    @pytest.mark.asyncio
    async def test_get_result_no_result_yet(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        result = await store.get_result(db_session, rid)
        assert result is None

    @pytest.mark.asyncio
    async def test_get_result_nonexistent(self, db_session: AsyncSession):
        store = EDAJobStore()
        result = await store.get_result(db_session, "nope")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_result_shape(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "timeseries", {})
        await store.write_result(db_session, rid, "timeseries", {"decomposition": [1, 2, 3]})

        result = await store.get_result(db_session, rid)
        assert set(result.keys()) == {"request_id", "mode", "result"}
        assert result["mode"] == "timeseries"


class TestEDAJobStoreWriteError:
    """Tests for EDAJobStore.write_error."""

    @pytest.mark.asyncio
    async def test_write_error(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        await store.write_error(db_session, rid, "Column not found")

        req = await store.get_request(db_session, rid)
        assert req["status"] == "failed"
        assert req["error"] == "Column not found"


class TestEDAJobStoreGetError:
    """Tests for EDAJobStore.get_error."""

    @pytest.mark.asyncio
    async def test_get_error_when_present(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        await store.write_error(db_session, rid, "Timeout")
        error = await store.get_error(db_session, rid)
        assert error == "Timeout"

    @pytest.mark.asyncio
    async def test_get_error_when_no_error(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", {})
        error = await store.get_error(db_session, rid)
        assert error is None

    @pytest.mark.asyncio
    async def test_get_error_nonexistent(self, db_session: AsyncSession):
        store = EDAJobStore()
        error = await store.get_error(db_session, "missing")
        assert error is None


class TestEDAJobStoreToDict:
    """Tests for EDAJobStore._to_dict static method."""

    @pytest.mark.asyncio
    async def test_to_dict_timestamps_are_strings(self, db_session: AsyncSession):
        store = EDAJobStore()
        rid = _rid()
        result = await store.create_request(db_session, rid, "tabular", {})
        assert isinstance(result["created_at"], str)
        assert isinstance(result["updated_at"], str)

    @pytest.mark.asyncio
    async def test_to_dict_nullable_fields_default_to_none(self, db_session: AsyncSession):
        store = EDAJobStore()
        result = await store.create_request(db_session, _rid(), "tabular", {})
        assert result["domino_job_id"] is None
        assert result["domino_job_status"] is None
        assert result["domino_job_url"] is None
        assert result["error"] is None
        assert result["owner"] is None
        assert result["project_id"] is None


# ===========================================================================
# Integration / round-trip tests
# ===========================================================================


class TestEdaCrudRoundTrip:
    """End-to-end scenarios combining multiple CRUD operations."""

    @pytest.mark.asyncio
    async def test_full_success_lifecycle(self, db_session: AsyncSession):
        """pending -> running -> completed with result."""
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "tabular", SAMPLE_PAYLOAD, owner="alice")

        # Simulate job dispatched
        await crud.update_eda_request(db_session, rid, status="running", domino_job_id="dj-1")

        # Simulate completion
        await crud.write_eda_result(db_session, rid, "tabular", SAMPLE_RESULT)

        eda = await crud.get_eda_request(db_session, rid)
        assert eda.status == "completed"
        assert eda.domino_job_id == "dj-1"

        result = await crud.get_eda_result(db_session, rid)
        assert result == SAMPLE_RESULT

    @pytest.mark.asyncio
    async def test_full_error_lifecycle(self, db_session: AsyncSession):
        """pending -> running -> failed with error."""
        rid = _rid()
        await crud.create_eda_request(db_session, rid, "timeseries", {})
        await crud.update_eda_request(db_session, rid, status="running")
        await crud.write_eda_error(db_session, rid, "OOM killed")

        eda = await crud.get_eda_request(db_session, rid)
        assert eda.status == "failed"
        assert eda.error == "OOM killed"
        assert await crud.get_eda_result(db_session, rid) is None

    @pytest.mark.asyncio
    async def test_store_lifecycle_mirrors_crud(self, db_session: AsyncSession):
        """EDAJobStore round trip should match underlying CRUD state."""
        store = EDAJobStore()
        rid = _rid()
        await store.create_request(db_session, rid, "tabular", SAMPLE_PAYLOAD, owner="bob")
        await store.update_request(db_session, rid, status="running")
        await store.write_result(db_session, rid, "tabular", SAMPLE_RESULT)

        req = await store.get_request(db_session, rid)
        assert req["status"] == "completed"
        assert req["owner"] == "bob"

        result = await store.get_result(db_session, rid)
        assert result["result"] == SAMPLE_RESULT

        error = await store.get_error(db_session, rid)
        assert error is None
