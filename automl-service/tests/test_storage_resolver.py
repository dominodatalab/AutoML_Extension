"""Tests for app.services.storage_resolver.

Covers:
- download_file() — endpoint probing and delegation to domino_download
- _find_existing() — dataset listing and matching
- _create_dataset() — creation with payload variants
- _get_latest_snapshot_id() — snapshot lookup
- upload_file() — chunked upload workflow
- extract_dataset_list() — v2 response unwrapping (tested via domino_dataset_api)
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from app.services.storage_resolver import (
    ProjectStorageResolver,
    DatasetInfo,
)
from app.services.domino_dataset_api import extract_dataset_list


# ---------------------------------------------------------------------------
# extract_dataset_list
# ---------------------------------------------------------------------------


class TestExtractDatasetList:

    def test_plain_list(self):
        data = [{"datasetName": "ds1"}, {"datasetName": "ds2"}]
        result = extract_dataset_list(data)
        assert len(result) == 2
        assert result[0]["datasetName"] == "ds1"

    def test_v2_wrapped_items(self):
        data = {
            "items": [
                {"dataset": {"datasetName": "wrapped", "datasetId": "123"}},
            ]
        }
        result = extract_dataset_list(data)
        assert len(result) == 1
        assert result[0]["datasetName"] == "wrapped"
        assert result[0]["datasetId"] == "123"

    def test_datasets_key(self):
        data = {"datasets": [{"name": "a"}, {"name": "b"}]}
        result = extract_dataset_list(data)
        assert len(result) == 2

    def test_empty_dict(self):
        assert extract_dataset_list({}) == []

    def test_non_dict_non_list(self):
        assert extract_dataset_list("unexpected") == []


# ---------------------------------------------------------------------------
# download_file
# ---------------------------------------------------------------------------


class TestDownloadFile:

    @pytest.mark.asyncio
    async def test_download_with_snapshot(self, tmp_path):
        resolver = ProjectStorageResolver()
        dest = str(tmp_path / "output.csv")

        with patch.object(
            resolver, "_get_latest_snapshot_id", new_callable=AsyncMock, return_value="snap-1"
        ), patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value="rw-snap-1"
        ), patch(
            "app.services.storage_resolver.domino_download", new_callable=AsyncMock
        ) as mock_dl:
            result = await resolver.download_file("ds-123", "uploads/file.csv", dest)

        assert result == dest
        # First call should use the v4 raw endpoint with the RW snapshot
        call_path = mock_dl.call_args_list[0][0][0]
        assert "rw-snap-1" in call_path
        assert "/v4/datasetrw/snapshot/" in call_path

    @pytest.mark.asyncio
    async def test_falls_back_when_snapshot_endpoint_fails(self, tmp_path):
        resolver = ProjectStorageResolver()
        dest = str(tmp_path / "output.csv")
        call_count = 0

        async def fake_download(path, dest_path, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise httpx.HTTPStatusError(
                    "Not Found", request=MagicMock(), response=MagicMock(status_code=404)
                )
            # Second call succeeds (Bearer auth fallback on same v4 endpoint)

        with patch.object(
            resolver, "_get_latest_snapshot_id", new_callable=AsyncMock, return_value="snap-1"
        ), patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value="rw-snap-1"
        ), patch(
            "app.services.storage_resolver.domino_download", side_effect=fake_download
        ):
            result = await resolver.download_file("ds-123", "uploads/file.csv", dest)

        assert result == dest
        assert call_count == 2

    @pytest.mark.asyncio
    async def test_download_without_latest_snapshot(self, tmp_path):
        """Even without a latest snapshot, the RW snapshot provides the v4 path."""
        resolver = ProjectStorageResolver()
        dest = str(tmp_path / "output.csv")

        with patch.object(
            resolver, "_get_latest_snapshot_id", new_callable=AsyncMock, return_value=None
        ), patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value="rw-snap-1"
        ), patch(
            "app.services.storage_resolver.domino_download", new_callable=AsyncMock
        ) as mock_dl:
            result = await resolver.download_file("ds-123", "uploads/file.csv", dest)

        assert result == dest
        call_path = mock_dl.call_args_list[0][0][0]
        assert "/v4/datasetrw/snapshot/rw-snap-1/file/raw" in call_path

    @pytest.mark.asyncio
    async def test_raises_when_all_endpoints_fail(self, tmp_path):
        resolver = ProjectStorageResolver()
        dest = str(tmp_path / "output.csv")

        with patch.object(
            resolver, "_get_latest_snapshot_id", new_callable=AsyncMock, return_value=None
        ), patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value="rw-snap-1"
        ), patch(
            "app.services.storage_resolver.domino_download",
            side_effect=RuntimeError("fail"),
        ):
            with pytest.raises(RuntimeError, match="Failed to download"):
                await resolver.download_file("ds-123", "uploads/file.csv", dest)


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
# _create_dataset
# ---------------------------------------------------------------------------


class TestCreateDataset:

    @pytest.mark.asyncio
    async def test_uses_dataset_rw_write_helper(self):
        resolver = ProjectStorageResolver()
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "dataset": {
                "id": "ds-created",
                "name": "automl-extension",
            }
        }

        with patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
            return_value=mock_resp,
        ) as mock_request:
            info = await resolver._create_dataset("proj-1")

        assert info.dataset_id == "ds-created"
        assert info.name == "automl-extension"
        assert mock_request.await_count >= 1
        first_call = mock_request.await_args_list[0]
        assert first_call.args == ("POST", "/api/datasetrw/v1/datasets")
        assert first_call.kwargs["json"]["name"] == "automl-extension"
        assert first_call.kwargs["json"]["projectId"] == "proj-1"

    @pytest.mark.asyncio
    async def test_retries_with_next_payload_on_error(self):
        resolver = ProjectStorageResolver()
        bad_response = MagicMock()
        bad_response.status_code = 400
        bad_response.text = "Bad Request"
        bad_error = httpx.HTTPStatusError(
            "bad request",
            request=MagicMock(),
            response=bad_response,
        )
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "dataset": {
                "id": "ds-created",
                "name": "automl-extension",
            }
        }

        with patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
            side_effect=[bad_error, mock_resp],
        ) as mock_request:
            info = await resolver._create_dataset("proj-1")

        assert info.dataset_id == "ds-created"
        assert mock_request.await_count == 2
        first_call = mock_request.await_args_list[0]
        second_call = mock_request.await_args_list[1]
        assert first_call.args == ("POST", "/api/datasetrw/v1/datasets")
        assert second_call.args == ("POST", "/api/datasetrw/v1/datasets")

    @pytest.mark.asyncio
    async def test_resolve_or_create_falls_back_to_find_existing(self):
        """When create fails, _resolve_or_create falls back to listing."""
        resolver = ProjectStorageResolver()
        existing = DatasetInfo(
            dataset_id="ds-existing",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver,
            "_create_dataset",
            new_callable=AsyncMock,
            side_effect=RuntimeError("all create attempts failed"),
        ), patch.object(
            resolver,
            "_find_existing",
            new_callable=AsyncMock,
            return_value=existing,
        ) as find_existing:
            info = await resolver._resolve_or_create("proj-1")

        assert info is existing
        find_existing.assert_awaited_once_with("proj-1")


class TestDeleteDataset:

    @pytest.mark.asyncio
    async def test_uses_dataset_rw_write_helper(self):
        resolver = ProjectStorageResolver()
        resolver._cache = {
            "proj-1": DatasetInfo(
                dataset_id="ds-123",
                name="automl-extension",
                project_id="proj-1",
            )
        }
        resolver._rw_cache["ds-123"] = "rw-123"

        with patch.object(
            resolver,
            "_dataset_rw_write_request",
            new_callable=AsyncMock,
        ) as write_request:
            await resolver.delete_dataset("ds-123")

        write_request.assert_awaited_once_with(
            "DELETE",
            "/api/datasetrw/v1/datasets/ds-123",
        )
        assert resolver._cache == {}
        assert resolver._rw_cache == {}


# ---------------------------------------------------------------------------
# _get_latest_snapshot_id
# ---------------------------------------------------------------------------


class TestGetLatestSnapshotId:

    @pytest.mark.asyncio
    async def test_returns_snapshot_id(self):
        resolver = ProjectStorageResolver()
        mock_snapshot = MagicMock()
        mock_snapshot.id = "snap-42"

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[mock_snapshot]
        ):
            sid = await resolver._get_latest_snapshot_id("ds-123")

        assert sid == "snap-42"

    @pytest.mark.asyncio
    async def test_returns_none_when_no_snapshots(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[]
        ):
            sid = await resolver._get_latest_snapshot_id("ds-123")

        assert sid is None

    @pytest.mark.asyncio
    async def test_returns_none_on_error(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            ProjectStorageResolver,
            "_list_snapshots_typed",
            side_effect=Exception("network error"),
        ):
            sid = await resolver._get_latest_snapshot_id("ds-123")

        assert sid is None


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
# Dataset RW write requests
# ---------------------------------------------------------------------------


class TestDatasetRwWriteRequest:

    @pytest.mark.asyncio
    async def test_prefers_direct_host_then_falls_back_to_default(self):
        resolver = ProjectStorageResolver()
        response = MagicMock()

        with patch(
            "app.services.storage_resolver.resolve_domino_nucleus_host",
            return_value="http://nucleus-frontend.domino-platform:80",
        ), patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
            side_effect=[
                httpx.RemoteProtocolError("Server disconnected without sending a response."),
                response,
            ],
        ) as domino_request_mock:
            result = await resolver._dataset_rw_write_request(
                "POST",
                "/v4/datasetrw/datasets/ds-123/snapshot/file/start",
                json={"filePaths": ["uploads/file.csv"]},
            )

        assert result is response
        assert len(domino_request_mock.await_args_list) == 2

        first_call = domino_request_mock.await_args_list[0]
        assert first_call.args == ("POST", "/v4/datasetrw/datasets/ds-123/snapshot/file/start")
        assert first_call.kwargs["json"] == {"filePaths": ["uploads/file.csv"]}
        assert first_call.kwargs["base_url"] == "http://nucleus-frontend.domino-platform:80"
        assert first_call.kwargs["max_retries"] == 0

        second_call = domino_request_mock.await_args_list[1]
        assert second_call.args == ("POST", "/v4/datasetrw/datasets/ds-123/snapshot/file/start")
        assert second_call.kwargs["json"] == {"filePaths": ["uploads/file.csv"]}
        assert second_call.kwargs["base_url"] is None
        assert "max_retries" not in second_call.kwargs


class TestUploadFile:

    @pytest.mark.asyncio
    async def test_upload_file_uses_proxy(self):
        """Upload goes through domino_request (proxy) not the nucleus wrapper."""
        resolver = ProjectStorageResolver()
        start_resp = MagicMock()
        start_resp.json.return_value = "upload-key-123"
        end_resp = MagicMock()

        with patch(
            "app.services.storage_resolver.domino_request",
            new_callable=AsyncMock,
            side_effect=[start_resp, end_resp],
        ) as mock_request, patch.object(
            resolver,
            "_upload_chunks",
            new_callable=AsyncMock,
        ) as upload_chunks:
            await resolver.upload_file(
                "ds-123",
                "uploads/file.csv",
                b"hello world",
            )

        assert mock_request.await_args_list[0].args == (
            "POST",
            "/v4/datasetrw/datasets/ds-123/snapshot/file/start",
        )
        upload_chunks.assert_awaited_once_with(
            "ds-123",
            "upload-key-123",
            "uploads/file.csv",
            b"hello world",
            8 * 1024 * 1024,
        )
        assert mock_request.await_args_list[1].args == (
            "GET",
            "/v4/datasetrw/datasets/ds-123/snapshot/file/end/upload-key-123",
        )


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


# ---------------------------------------------------------------------------
# Cache and invalidate
# ---------------------------------------------------------------------------


class TestCacheInvalidation:

    def test_invalidate_single_project(self):
        resolver = ProjectStorageResolver()
        resolver._cache["proj-1"] = DatasetInfo(
            dataset_id="ds-1", name="test", project_id="proj-1"
        )
        resolver._cache["proj-2"] = DatasetInfo(
            dataset_id="ds-2", name="test", project_id="proj-2"
        )

        resolver.invalidate("proj-1")
        assert "proj-1" not in resolver._cache
        assert "proj-2" in resolver._cache

    def test_invalidate_all(self):
        resolver = ProjectStorageResolver()
        resolver._cache["proj-1"] = DatasetInfo(
            dataset_id="ds-1", name="test", project_id="proj-1"
        )
        resolver.invalidate()
        assert len(resolver._cache) == 0
