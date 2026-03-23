"""Tests for upload-layer methods of ProjectStorageResolver.

Covers:
- ensure_dataset_exists() — success, failure returns None
- delete_snapshot_files() — success, failure, empty paths
- get_latest_snapshot_status() — active, pending, no snapshots, error
- _probe_mount() — template match, env var override, no match
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.services.storage_resolver import (
    DatasetInfo,
    ProjectStorageResolver,
)


# ---------------------------------------------------------------------------
# ensure_dataset_exists
# ---------------------------------------------------------------------------


class TestEnsureDatasetExists:

    @pytest.mark.asyncio
    async def test_returns_dataset_info_on_success(self):
        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ):
            result = await resolver.ensure_dataset_exists("proj-1")

        assert result is info

    @pytest.mark.asyncio
    async def test_returns_none_on_failure(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock,
            side_effect=RuntimeError("create failed"),
        ):
            result = await resolver.ensure_dataset_exists("proj-1")

        assert result is None

    @pytest.mark.asyncio
    async def test_never_raises(self):
        """Even unexpected exceptions are swallowed."""
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock,
            side_effect=ValueError("unexpected"),
        ):
            result = await resolver.ensure_dataset_exists("proj-1")

        assert result is None


# ---------------------------------------------------------------------------
# delete_snapshot_files
# ---------------------------------------------------------------------------


class TestDeleteSnapshotFiles:

    @pytest.mark.asyncio
    async def test_returns_true_on_success(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_dataset_rw_write_request", new_callable=AsyncMock
        ) as mock_write:
            result = await resolver.delete_snapshot_files(
                "snap-1", ["uploads/file.csv", "uploads/other.csv"]
            )

        assert result is True
        mock_write.assert_awaited_once_with(
            "DELETE",
            "/v4/datasetrw/snapshot/snap-1/files",
            json={"relativePaths": ["uploads/file.csv", "uploads/other.csv"]},
        )

    @pytest.mark.asyncio
    async def test_returns_false_on_failure(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_dataset_rw_write_request", new_callable=AsyncMock,
            side_effect=RuntimeError("delete failed"),
        ):
            result = await resolver.delete_snapshot_files("snap-1", ["file.csv"])

        assert result is False

    @pytest.mark.asyncio
    async def test_empty_paths_returns_true_immediately(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_dataset_rw_write_request", new_callable=AsyncMock
        ) as mock_write:
            result = await resolver.delete_snapshot_files("snap-1", [])

        assert result is True
        mock_write.assert_not_awaited()


# ---------------------------------------------------------------------------
# get_latest_snapshot_status
# ---------------------------------------------------------------------------


class TestGetLatestSnapshotStatus:

    @pytest.mark.asyncio
    async def test_returns_status_string(self):
        from app.api.generated.domino_public_api_client.models.snapshot_details_v1_status import (
            SnapshotDetailsV1Status,
        )

        resolver = ProjectStorageResolver()
        mock_snapshot = MagicMock()
        mock_snapshot.status = SnapshotDetailsV1Status.ACTIVE

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[mock_snapshot]
        ):
            status = await resolver.get_latest_snapshot_status("ds-123")

        assert status == "active"

    @pytest.mark.asyncio
    async def test_returns_pending_status(self):
        from app.api.generated.domino_public_api_client.models.snapshot_details_v1_status import (
            SnapshotDetailsV1Status,
        )

        resolver = ProjectStorageResolver()
        mock_snapshot = MagicMock()
        mock_snapshot.status = SnapshotDetailsV1Status.PENDING

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[mock_snapshot]
        ):
            status = await resolver.get_latest_snapshot_status("ds-123")

        assert status == "pending"

    @pytest.mark.asyncio
    async def test_returns_none_when_no_snapshots(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[]
        ):
            status = await resolver.get_latest_snapshot_status("ds-123")

        assert status is None

    @pytest.mark.asyncio
    async def test_returns_none_on_error(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            ProjectStorageResolver,
            "_list_snapshots_typed",
            side_effect=Exception("network error"),
        ):
            status = await resolver.get_latest_snapshot_status("ds-123")

        assert status is None

    @pytest.mark.asyncio
    async def test_passes_limit_param(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            ProjectStorageResolver, "_list_snapshots_typed", return_value=[]
        ) as mock_list:
            await resolver.get_latest_snapshot_status("ds-123")

        mock_list.assert_called_once_with("ds-123", limit=1)


# ---------------------------------------------------------------------------
# _probe_mount (static method)
# ---------------------------------------------------------------------------


class TestProbeMount:

    def test_finds_writable_template_path(self, tmp_path):
        mount_dir = tmp_path / "domino" / "datasets" / "local" / "automl-extension"
        mount_dir.mkdir(parents=True)

        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES",
            [str(tmp_path / "domino" / "datasets" / "local" / "{name}")],
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result == str(mount_dir)

    def test_returns_none_when_no_path_exists(self):
        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES",
            ["/nonexistent/{name}"],
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result is None

    def test_returns_none_when_path_not_writable(self, tmp_path):
        mount_dir = tmp_path / "readonly" / "automl-extension"
        mount_dir.mkdir(parents=True)
        mount_dir.chmod(0o444)

        try:
            with patch(
                "app.services.storage_resolver._MOUNT_TEMPLATES",
                [str(tmp_path / "readonly" / "{name}")],
            ):
                result = ProjectStorageResolver._probe_mount("automl-extension")

            assert result is None
        finally:
            mount_dir.chmod(0o755)

    def test_checks_env_var_mount_path(self, tmp_path):
        mount_dir = tmp_path / "custom_mount" / "automl-extension"
        mount_dir.mkdir(parents=True)

        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES", []
        ), patch.dict(
            os.environ,
            {"DOMINO_DATASET_MOUNT_PATH": str(tmp_path / "custom_mount")},
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result == str(mount_dir)

    def test_checks_domino_mount_paths_env_var(self, tmp_path):
        mount_dir = tmp_path / "mount_a" / "automl-extension"
        mount_dir.mkdir(parents=True)

        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES", []
        ), patch.dict(
            os.environ,
            {"DOMINO_MOUNT_PATHS": f"/nonexistent:{tmp_path / 'mount_a'}"},
            clear=False,
        ):
            # Clear DOMINO_DATASET_MOUNT_PATH to isolate this test
            env = os.environ.copy()
            env.pop("DOMINO_DATASET_MOUNT_PATH", None)
            with patch.dict(os.environ, env, clear=True):
                with patch.dict(
                    os.environ,
                    {"DOMINO_MOUNT_PATHS": f"/nonexistent:{tmp_path / 'mount_a'}"},
                ):
                    result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result == str(mount_dir)

    def test_handles_colon_separated_env_paths(self, tmp_path):
        mount_dir = tmp_path / "path_b" / "automl-extension"
        mount_dir.mkdir(parents=True)

        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES", []
        ), patch.dict(
            os.environ,
            {
                "DOMINO_DATASET_MOUNT_PATH": f"/bad:{tmp_path / 'path_b'}",
            },
            clear=False,
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result == str(mount_dir)

    def test_handles_comma_separated_env_paths(self, tmp_path):
        mount_dir = tmp_path / "path_c" / "automl-extension"
        mount_dir.mkdir(parents=True)

        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES", []
        ), patch.dict(
            os.environ,
            {
                "DOMINO_DATASET_MOUNT_PATH": f"/bad,{tmp_path / 'path_c'}",
            },
            clear=False,
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result == str(mount_dir)

    def test_env_var_not_set_returns_none(self):
        with patch(
            "app.services.storage_resolver._MOUNT_TEMPLATES", []
        ), patch.dict(
            os.environ,
            {},
            clear=True,
        ):
            result = ProjectStorageResolver._probe_mount("automl-extension")

        assert result is None
