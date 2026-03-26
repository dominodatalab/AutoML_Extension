"""Tests for app.services.storage_resolver (viewing layer).

Covers:
- _find_existing() — dataset listing and matching
- get_rw_snapshot_id() — RW snapshot resolution
- list_snapshot_files() — snapshot file browsing
- _extract_dataset_list() — v2 response unwrapping
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.services.storage_resolver import (
    ProjectStorageResolver,
    DatasetInfo,
    _extract_dataset_list,
)


# ---------------------------------------------------------------------------
# _extract_dataset_list
# ---------------------------------------------------------------------------


class TestExtractDatasetList:

    def test_plain_list(self):
        data = [{"datasetName": "ds1"}, {"datasetName": "ds2"}]
        result = _extract_dataset_list(data)
        assert len(result) == 2
        assert result[0]["datasetName"] == "ds1"

    def test_v2_wrapped_items(self):
        data = {
            "items": [
                {"dataset": {"datasetName": "wrapped", "datasetId": "123"}},
            ]
        }
        result = _extract_dataset_list(data)
        assert len(result) == 1
        assert result[0]["datasetName"] == "wrapped"
        assert result[0]["datasetId"] == "123"

    def test_datasets_key(self):
        data = {"datasets": [{"name": "a"}, {"name": "b"}]}
        result = _extract_dataset_list(data)
        assert len(result) == 2

    def test_empty_dict(self):
        assert _extract_dataset_list({}) == []

    def test_non_dict_non_list(self):
        assert _extract_dataset_list("unexpected") == []


# ---------------------------------------------------------------------------
# _find_existing
# ---------------------------------------------------------------------------


class TestFindExisting:

    @pytest.mark.asyncio
    async def test_finds_matching_dataset(self):
        resolver = ProjectStorageResolver()
        with patch(
            "app.services.storage_resolver.list_project_datasets",
            new_callable=AsyncMock,
            return_value=[
                {"datasetName": "automl-extension", "datasetId": "ds-abc"},
                {"datasetName": "other-dataset", "datasetId": "ds-xyz"},
            ],
        ):
            info = await resolver._find_existing("proj-1")

        assert info is not None
        assert info.dataset_id == "ds-abc"
        assert info.name == "automl-extension"

    @pytest.mark.asyncio
    async def test_returns_none_when_not_found(self):
        resolver = ProjectStorageResolver()
        with patch(
            "app.services.storage_resolver.list_project_datasets",
            new_callable=AsyncMock,
            return_value=[
                {"datasetName": "something-else", "datasetId": "ds-xyz"},
            ],
        ):
            info = await resolver._find_existing("proj-1")

        assert info is None

    @pytest.mark.asyncio
    async def test_returns_none_on_api_error(self):
        resolver = ProjectStorageResolver()

        with patch(
            "app.services.storage_resolver.list_project_datasets",
            side_effect=httpx.HTTPStatusError("err", request=MagicMock(), response=MagicMock()),
        ):
            info = await resolver._find_existing("proj-1")

        assert info is None


# ---------------------------------------------------------------------------
# get_rw_snapshot_id
# ---------------------------------------------------------------------------


class TestGetRwSnapshotId:

    @pytest.mark.asyncio
    async def test_prefers_v1_snapshot_lookup_before_legacy_detail_endpoint(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver,
            "_resolve_rw_snapshot_v1",
            new_callable=AsyncMock,
            return_value="rw-snap-123",
        ) as resolve_v1, patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
        ) as domino_request_mock:
            rw_sid = await resolver.get_rw_snapshot_id("ds-123")

        assert rw_sid == "rw-snap-123"
        resolve_v1.assert_awaited_once_with("ds-123")
        domino_request_mock.assert_not_called()


# ---------------------------------------------------------------------------
# list_snapshot_files
# ---------------------------------------------------------------------------


class TestListSnapshotFiles:

    @pytest.mark.asyncio
    async def test_snapshot_browsing_uses_proxy(self):
        resolver = ProjectStorageResolver()
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"rows": []}

        with patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
            return_value=mock_resp,
        ) as domino_request_mock:
            rows = await resolver.list_snapshot_files("snap-123", path="uploads")

        assert rows == []
        domino_request_mock.assert_awaited_once_with(
            "GET",
            "/v4/datasetrw/files/snap-123",
            params={"path": "uploads"},
        )
