"""Tests for previously untested methods of ProjectStorageResolver.

Covers:
- ensure_project_storage() — cache hit, fresh resolve, RuntimeError on missing mount
- resolve_project_paths() — standalone mode paths, Domino mode paths, HTTPException(503)
- check_project_storage() — mounted, not mounted, exception
- ensure_dataset_exists() — success, failure returns None
- download_directory() — recursive download, raises on missing RW snapshot
- delete_snapshot_files() — success, failure, empty paths
- get_latest_snapshot_status() — active, wrapped, no snapshots, error
- _probe_mount() — template match, env var override, no match
"""

import os
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from app.services.storage_resolver import (
    DatasetInfo,
    ProjectPaths,
    ProjectStorageResolver,
)


# ---------------------------------------------------------------------------
# ensure_project_storage
# ---------------------------------------------------------------------------


class TestEnsureProjectStorage:

    @pytest.mark.asyncio
    async def test_returns_cached_mount_path(self):
        resolver = ProjectStorageResolver()
        resolver._cache["proj-1"] = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
            mount_path="/domino/datasets/local/automl-extension",
        )

        result = await resolver.ensure_project_storage("proj-1")
        assert result == "/domino/datasets/local/automl-extension"

    @pytest.mark.asyncio
    async def test_resolves_and_probes_mount(self):
        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ), patch.object(
            resolver, "_probe_mount", return_value="/domino/datasets/local/automl-extension"
        ):
            result = await resolver.ensure_project_storage("proj-1")

        assert result == "/domino/datasets/local/automl-extension"
        assert resolver._cache["proj-1"].mount_path == "/domino/datasets/local/automl-extension"

    @pytest.mark.asyncio
    async def test_raises_runtime_error_when_mount_not_found(self):
        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ), patch.object(
            resolver, "_probe_mount", return_value=None
        ):
            with pytest.raises(RuntimeError, match="no local mount was found"):
                await resolver.ensure_project_storage("proj-1")

    @pytest.mark.asyncio
    async def test_skips_cache_when_mount_path_is_none(self):
        """A cached entry without mount_path should not be returned."""
        resolver = ProjectStorageResolver()
        resolver._cache["proj-1"] = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
            mount_path=None,
        )
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ), patch.object(
            resolver, "_probe_mount", return_value="/mnt/data/automl-extension"
        ):
            result = await resolver.ensure_project_storage("proj-1")

        assert result == "/mnt/data/automl-extension"


# ---------------------------------------------------------------------------
# resolve_project_paths
# ---------------------------------------------------------------------------


class TestResolveProjectPaths:

    @pytest.mark.asyncio
    async def test_standalone_mode_returns_settings_paths(self):
        mock_settings = MagicMock()
        mock_settings.standalone_mode = True
        mock_settings.models_path = "/app/storage/models"
        mock_settings.uploads_path = "/app/storage/uploads"
        mock_settings.eda_results_path = "/app/storage/eda_results"

        resolver = ProjectStorageResolver()

        with patch("app.config.get_settings", return_value=mock_settings):
            paths = await resolver.resolve_project_paths("proj-1")

        assert isinstance(paths, ProjectPaths)
        assert paths.project_id == "proj-1"
        assert paths.mount_path == "/app/storage"
        assert paths.models_path == "/app/storage/models"
        assert paths.uploads_path == "/app/storage/uploads"
        assert paths.eda_results_path == "/app/storage/eda_results"
        assert paths.temp_path == "/app/storage/temp"

    @pytest.mark.asyncio
    async def test_domino_mode_returns_mount_based_paths(self):
        mock_settings = MagicMock()
        mock_settings.standalone_mode = False

        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch("app.config.get_settings", return_value=mock_settings), \
             patch.object(resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info), \
             patch.object(resolver, "_probe_mount", return_value="/domino/datasets/local/automl-extension"):
            paths = await resolver.resolve_project_paths("proj-1")

        assert paths.mount_path == "/domino/datasets/local/automl-extension"
        assert paths.models_path == "/domino/datasets/local/automl-extension/models"
        assert paths.uploads_path == "/domino/datasets/local/automl-extension/uploads"
        assert paths.eda_results_path == "/domino/datasets/local/automl-extension/eda_results"
        assert paths.temp_path == "/domino/datasets/local/automl-extension/temp"

    @pytest.mark.asyncio
    async def test_raises_503_when_dataset_exists_but_not_mounted(self):
        mock_settings = MagicMock()
        mock_settings.standalone_mode = False

        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch("app.config.get_settings", return_value=mock_settings), \
             patch.object(resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info), \
             patch.object(resolver, "_probe_mount", return_value=None):
            with pytest.raises(HTTPException) as exc_info:
                await resolver.resolve_project_paths("proj-1")

        assert exc_info.value.status_code == 503
        assert "not mounted" in exc_info.value.detail


# ---------------------------------------------------------------------------
# check_project_storage
# ---------------------------------------------------------------------------


class TestCheckProjectStorage:

    @pytest.mark.asyncio
    async def test_returns_true_when_mounted(self):
        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ), patch.object(
            resolver, "_probe_mount", return_value="/domino/datasets/local/automl-extension"
        ):
            mounted, path = await resolver.check_project_storage("proj-1")

        assert mounted is True
        assert path == "/domino/datasets/local/automl-extension"

    @pytest.mark.asyncio
    async def test_returns_false_when_not_mounted(self):
        resolver = ProjectStorageResolver()
        info = DatasetInfo(
            dataset_id="ds-1",
            name="automl-extension",
            project_id="proj-1",
        )

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock, return_value=info
        ), patch.object(
            resolver, "_probe_mount", return_value=None
        ):
            mounted, path = await resolver.check_project_storage("proj-1")

        assert mounted is False
        assert path is None

    @pytest.mark.asyncio
    async def test_returns_false_on_resolve_exception(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "_resolve_or_create", new_callable=AsyncMock,
            side_effect=RuntimeError("API failure"),
        ):
            mounted, path = await resolver.check_project_storage("proj-1")

        assert mounted is False
        assert path is None


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
# download_directory
# ---------------------------------------------------------------------------


class TestDownloadDirectory:

    @pytest.mark.asyncio
    async def test_downloads_recursively(self, tmp_path):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value="rw-snap-1"
        ), patch.object(
            resolver, "_download_dir_recursive", new_callable=AsyncMock
        ) as mock_recursive:
            result = await resolver.download_directory(
                "ds-123", "models/job_abc", str(tmp_path / "output")
            )

        assert result == str(tmp_path / "output")
        mock_recursive.assert_awaited_once_with(
            "ds-123", "rw-snap-1", "models/job_abc", str(tmp_path / "output")
        )

    @pytest.mark.asyncio
    async def test_raises_when_no_rw_snapshot(self):
        resolver = ProjectStorageResolver()

        with patch.object(
            resolver, "get_rw_snapshot_id", new_callable=AsyncMock, return_value=None
        ):
            with pytest.raises(RuntimeError, match="No RW snapshot found"):
                await resolver.download_directory(
                    "ds-123", "models/job_abc", "/tmp/output"
                )

    @pytest.mark.asyncio
    async def test_download_dir_recursive_handles_files_and_dirs(self, tmp_path):
        """Integration test for _download_dir_recursive with mixed entries."""
        resolver = ProjectStorageResolver()
        dest = str(tmp_path / "downloaded")

        # list_snapshot_files returns a flat file and a subdirectory
        file_entry = {"fileName": "model.pkl", "isDirectory": False}
        dir_entry = {"fileName": "sub", "isDirectory": True}

        sub_file_entry = {"fileName": "data.csv", "isDirectory": False}

        call_count = {"list": 0}

        async def mock_list_files(snap_id, path=""):
            call_count["list"] += 1
            if path == "models":
                return [file_entry, dir_entry]
            elif path == "models/sub":
                return [sub_file_entry]
            return []

        with patch.object(
            resolver, "list_snapshot_files", side_effect=mock_list_files
        ), patch(
            "app.services.storage_resolver.domino_download", new_callable=AsyncMock
        ):
            await resolver._download_dir_recursive(
                "ds-123", "rw-snap-1", "models", dest
            )

        assert os.path.isdir(dest)
        # Should have called list_snapshot_files for both the root and subdir
        assert call_count["list"] == 2


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
