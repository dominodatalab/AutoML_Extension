"""Domino dataset management using REST API."""

import asyncio
import logging
import os
import time
from typing import Any, Optional

from app.api.generated.domino_public_api_client.api.dataset_rw import (
    get_dataset as get_dataset_api,
)
from app.api.generated.domino_public_api_client.models.dataset_rw_envelope_v1 import (
    DatasetRwEnvelopeV1,
)
from app.config import get_settings
from app.api.schemas.dataset import (
    DatasetFileResponse,
    DatasetResponse,
    DatasetPreviewResponse,
    DatasetSchemaResponse,
)
from app.core.dataset_mounts import resolve_dataset_mount_paths
from app.core.domino_http import get_domino_public_api_client_sync
from app.core.tabular_data import read_tabular_preview, read_tabular_schema
from app.services.domino_dataset_api import list_project_datasets

logger = logging.getLogger(__name__)
SUPPORTED_DATA_EXTENSIONS = (".csv", ".parquet", ".pq")


class DominoDatasetManager:
    """Manages Domino datasets using the Domino REST API."""

    def __init__(self):
        self.settings = get_settings()

    def _resolve_dataset_mount_paths(self) -> list[str]:
        """Resolve all filesystem paths that may contain mounted datasets."""
        return resolve_dataset_mount_paths(fallback_path=self.settings.datasets_path)

    def _resolve_dataset_mount_path(self) -> str:
        """Resolve a primary mount path for compatibility logging."""
        paths = self._resolve_dataset_mount_paths()
        if paths:
            return paths[0]
        return self.settings.datasets_path

    def _is_supported_file(self, file_name: str) -> bool:
        return file_name.lower().endswith(SUPPORTED_DATA_EXTENSIONS)

    def _first_supported_file(self, path: str) -> Optional[str]:
        for root, _, files in os.walk(path):
            for file_name in files:
                if self._is_supported_file(file_name):
                    return os.path.join(root, file_name)
        return None

    @staticmethod
    def _coerce_int(value: Any, default: int = 0) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def _normalize_dataset_files(
        self,
        files: Any,
        dataset_path: Optional[str] = None,
    ) -> list[DatasetFileResponse]:
        """Normalize file entries from mixed API/local payloads."""
        normalized: list[DatasetFileResponse] = []
        if not isinstance(files, list):
            return normalized

        for entry in files:
            if isinstance(entry, DatasetFileResponse):
                normalized.append(entry)
                continue

            if isinstance(entry, str):
                entry_path = os.path.join(dataset_path, entry) if dataset_path else entry
                normalized.append(DatasetFileResponse(name=entry, path=entry_path, size=0))
                continue

            if isinstance(entry, dict):
                name = str(entry.get("name") or entry.get("fileName") or "").strip()
                path = str(entry.get("path") or "").strip()
                if not name and path:
                    name = os.path.basename(path)
                if not path and dataset_path and name:
                    path = os.path.join(dataset_path, name)
                if not name:
                    continue
                normalized.append(
                    DatasetFileResponse(
                        name=name,
                        path=path,
                        size=self._coerce_int(entry.get("size", entry.get("sizeInBytes", 0))),
                    )
                )
        return normalized

    @staticmethod
    def _fetch_dataset_details(dataset_id: str) -> dict:
        """Fetch a single dataset via the generated Domino API client.

        Returns the inner dataset dict (camelCase keys) on success, or
        an empty dict if the dataset was not found / API returned an error.
        """
        client = get_domino_public_api_client_sync()
        result = get_dataset_api.sync(dataset_id, client=client)
        if isinstance(result, DatasetRwEnvelopeV1):
            return result.dataset.to_dict()
        return {}

    async def list_datasets(
        self,
        project_id: Optional[str] = None,
        include_files: bool = True,
    ) -> list[DatasetResponse]:
        """List datasets, preferring the Domino API when a project ID is available.

        When *project_id* is supplied and the Domino environment is configured,
        the Dataset RW list API is used to retrieve project-scoped datasets,
        trying v2 first and falling back to v1 when the proxy/runtime does not
        serve v2 reliably. The results are then cross-referenced with local
        mount paths so that file listings include real filesystem paths for
        preview/training.

        Falls back to the legacy filesystem-scan approach when the API is
        unavailable or the environment is not configured.
        """
        if project_id and self.settings.is_domino_environment:
            try:
                datasets = await self._list_datasets_via_api(
                    project_id,
                    include_files=include_files,
                )
                if datasets is not None:
                    logger.info(
                        "Listed %s datasets for project %s via Domino API",
                        len(datasets),
                        project_id,
                    )
                    return datasets
            except Exception:
                logger.exception(
                    "Domino Dataset API call failed for project %s",
                    project_id,
                )
                app_project_id = os.environ.get("DOMINO_PROJECT_ID", "")
                if app_project_id and project_id != app_project_id:
                    raise RuntimeError(
                        f"Failed to list datasets for target project {project_id} via Domino API"
                    )
                logger.info(
                    "Falling back to filesystem scan for app project %s after API failure",
                    project_id,
                )

        # Fallback: discover datasets from mounted filesystem paths.
        datasets = await self._list_local_datasets()
        mount_paths = self._resolve_dataset_mount_paths()
        logger.info(
            "Found %s mounted datasets across mount roots: %s",
            len(datasets),
            ", ".join(mount_paths) if mount_paths else "(none)",
        )
        return datasets

    async def _list_datasets_via_api(
        self,
        project_id: str,
        include_files: bool = True,
    ) -> Optional[list[DatasetResponse]]:
        """List datasets for a project using the Domino Dataset RW v2 API.

        Falls back to the v1 Dataset RW API when v2 is unavailable.
        """
        datasets: list[DatasetResponse] = []
        items = await list_project_datasets(project_id)

        for item in items:
            ds = await self._api_item_to_dataset_response(
                item,
                include_files=include_files,
                requested_project_id=project_id,
            )
            if ds is not None:
                datasets.append(ds)

        return datasets

    async def _api_item_to_dataset_response(
        self,
        item: dict,
        include_files: bool = True,
        requested_project_id: Optional[str] = None,
    ) -> Optional[DatasetResponse]:
        """Convert a Domino API dataset object into a DatasetResponse.

        Always lists files via the snapshot API (which reflects the current
        RW snapshot) so that file deletions in Domino are visible immediately.
        The local mount path is used to resolve real file paths when the file
        exists on disk *and* the dataset belongs to the current App project,
        enabling direct reads during training/preview.
        """
        dataset_id = str(item.get("datasetId") or item.get("id", "") or "")
        dataset_name = item.get("datasetName") or item.get("name", "")
        if not dataset_name:
            return None

        # Only resolve local mount paths when the dataset belongs to the
        # same project as this App.  Cross-project datasets with the same
        # name (e.g. "automl-extension" in both App and target projects)
        # would otherwise resolve to the App project's mount, serving the
        # wrong files for preview and training.
        dataset_project_id = item.get("projectId") or item.get("ownerProjectId") or ""
        app_project_id = os.environ.get("DOMINO_PROJECT_ID", "")
        requested_matches_app = bool(
            requested_project_id and app_project_id and requested_project_id == app_project_id
        )
        is_local_dataset = bool(
            requested_matches_app and (not dataset_project_id or dataset_project_id == app_project_id)
        )

        dataset_path: Optional[str] = None
        if include_files and is_local_dataset:
            for mount_root in self._resolve_dataset_mount_paths():
                candidate = os.path.join(mount_root, dataset_name)
                if os.path.exists(candidate):
                    dataset_path = candidate
                    break

        files: list[DatasetFileResponse] = []
        total_size = 0
        rw_snapshot_id = item.get("readWriteSnapshotId")
        if include_files:
            # Always list files from the snapshot API — mounted filesystems use
            # read-only snapshots that go stale when files are deleted in Domino.
            if not rw_snapshot_id and dataset_id:
                from app.services.storage_resolver import get_storage_resolver
                rw_snapshot_id = await get_storage_resolver().get_rw_snapshot_id(dataset_id)
            if rw_snapshot_id:
                api_files, total_size = await self._list_files_via_snapshot_api(
                    rw_snapshot_id, dataset_name, dataset_id=dataset_id,
                )
                # If the dataset is mounted locally (same project), upgrade file
                # paths from synthetic to real mount paths where the file exists.
                for f in api_files:
                    if dataset_path:
                        local_path = os.path.join(dataset_path, f.name)
                        if os.path.exists(local_path):
                            f.path = local_path
                            f.mounted = True
                            try:
                                f.size = os.stat(local_path).st_size
                            except OSError:
                                pass
                    files.append(f)

            # Fall back to mounted filesystem only when the snapshot API returned
            # nothing (e.g. no RW snapshot ID or API unreachable). Warn because
            # mounted datasets use read-only snapshots that can be stale.
            if not files and dataset_path and os.path.isdir(dataset_path):
                logger.warning(
                    "Snapshot API returned no files for dataset %s (%s); "
                    "falling back to mounted filesystem which may be stale",
                    dataset_name,
                    dataset_id,
                )
                for root, _, filenames in os.walk(dataset_path):
                    for filename in filenames:
                        if not self._is_supported_file(filename):
                            continue
                        file_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(file_path, dataset_path)
                        try:
                            file_stat = os.stat(file_path)
                            file_size = file_stat.st_size
                        except OSError:
                            file_size = 0
                        files.append(
                            DatasetFileResponse(name=rel_path, path=file_path, size=file_size)
                        )
                        total_size += file_size

        size_bytes = total_size or self._coerce_int(
            item.get("sizeInBytes", item.get("storageSizeBytes", 0))
        )
        file_count = len(files) if files else self._coerce_int(item.get("fileCount", 0))

        return DatasetResponse(
            id=dataset_id,
            name=dataset_name,
            path=dataset_path,
            description=item.get("description", ""),
            size_bytes=size_bytes,
            created_at=item.get("createdAt"),
            updated_at=item.get("lastUpdatedAt", item.get("updatedAt")),
            file_count=file_count,
            files=files,
        )

    async def _list_files_via_snapshot_api(
        self,
        snapshot_id: str,
        dataset_name: str,
        path: str = "",
        dataset_id: str = "",
    ) -> tuple[list[DatasetFileResponse], int]:
        """List supported files from a snapshot via the Domino API.

        Recursively descends into subdirectories. Returns ``(files, total_size)``.
        """
        from app.services.storage_resolver import get_storage_resolver
        from app.core.domino_project_type import detect_project_type, DominoProjectType

        resolver = get_storage_resolver()
        files: list[DatasetFileResponse] = []
        total_size = 0

        # Use the detected project type so synthetic paths in logs, errors,
        # and CLI args reflect the actual mount layout of the runtime.
        if detect_project_type() == DominoProjectType.GIT:
            synthetic_root = "/mnt/data"
        else:
            synthetic_root = "/domino/datasets/local"

        try:
            entries = await resolver.list_snapshot_files(snapshot_id, path=path)
        except Exception:
            logger.debug(
                "Snapshot file listing failed for %s at path '%s'",
                snapshot_id,
                path,
                exc_info=True,
            )
            return files, total_size

        # The v4 files API may return full paths (e.g. "uploads/file.csv")
        # or just basenames ("file.csv").  Normalise to avoid duplicating
        # the directory prefix when we prepend ``path``.
        prefix_slash = (path + "/") if path else ""

        subdir_tasks: list[asyncio.Task[tuple[list[DatasetFileResponse], int]]] = []

        for entry in entries:
            file_name = entry.get("fileName", "")
            is_dir = entry.get("isDirectory", False)
            size = entry.get("sizeInBytes", 0) or 0

            # Strip the directory prefix if the API already included it.
            if prefix_slash and file_name.startswith(prefix_slash):
                file_name = file_name[len(prefix_slash):]

            if is_dir:
                subpath = f"{path}/{file_name}" if path else file_name
                subdir_tasks.append(
                    asyncio.create_task(
                        self._list_files_via_snapshot_api(
                            snapshot_id,
                            dataset_name,
                            path=subpath,
                            dataset_id=dataset_id,
                        )
                    )
                )
            elif self._is_supported_file(file_name):
                rel_path = f"{path}/{file_name}" if path else file_name
                synthetic_path = f"{synthetic_root}/{dataset_name}/{rel_path}"
                files.append(
                    DatasetFileResponse(
                        name=rel_path,
                        path=synthetic_path,
                        size=size,
                        mounted=False,
                    )
                )
                total_size += size

        if subdir_tasks:
            for sub_files, sub_size in await asyncio.gather(*subdir_tasks):
                files.extend(sub_files)
                total_size += sub_size

        return files, total_size

    def _is_reserved_mount_entry(self, item_name: str, item_path: str) -> bool:
        """Skip known non-dataset mount entries."""
        if item_name.startswith("."):
            return True
        if item_name == "snapshots":
            return True
        project_root = os.path.abspath(self.settings.project_storage_root)
        return os.path.abspath(item_path) == project_root

    def _list_mounted_dataset_entries(self, dataset_mount_path: str) -> list[DatasetResponse]:
        """List mounted datasets from a single mount root."""
        datasets: list[DatasetResponse] = []
        if not os.path.isdir(dataset_mount_path):
            return datasets

        for item in sorted(os.listdir(dataset_mount_path)):
            item_path = os.path.join(dataset_mount_path, item)
            if self._is_reserved_mount_entry(item, item_path):
                continue

            if os.path.isdir(item_path):
                files: list[DatasetFileResponse] = []
                total_size = 0
                for root, _, filenames in os.walk(item_path):
                    for filename in filenames:
                        if not self._is_supported_file(filename):
                            continue
                        file_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(file_path, item_path)
                        file_stat = os.stat(file_path)
                        files.append(
                            DatasetFileResponse(
                                name=rel_path,
                                path=file_path,
                                size=file_stat.st_size,
                            )
                        )
                        total_size += file_stat.st_size

                if files:
                    datasets.append(
                        DatasetResponse(
                            id=f"domino:{item}",
                            name=item,
                            path=item_path,
                            description="Domino dataset",
                            size_bytes=total_size,
                            file_count=len(files),
                            files=files,
                        )
                    )
                continue

            if os.path.isfile(item_path) and self._is_supported_file(item):
                stat = os.stat(item_path)
                datasets.append(
                    DatasetResponse(
                        id=f"domino:{item}",
                        name=item,
                        path=item_path,
                        description="Domino dataset",
                        size_bytes=stat.st_size,
                        file_count=1,
                        files=[DatasetFileResponse(name=item, path=item_path, size=stat.st_size)],
                    )
                )

        logger.info("Found %s mounted datasets in %s", len(datasets), dataset_mount_path)
        return datasets

    def _get_mounted_dataset(self, dataset_name: str) -> Optional[DatasetResponse]:
        """Resolve a mounted dataset by name from the configured mount roots."""
        for dataset_mount_path in self._resolve_dataset_mount_paths():
            for dataset in self._list_mounted_dataset_entries(dataset_mount_path):
                if dataset.id == f"domino:{dataset_name}":
                    return dataset
        return None

    async def _list_local_datasets(self) -> list[DatasetResponse]:
        """List datasets from all mounted dataset roots."""
        merged: dict[str, DatasetResponse] = {}
        for dataset_mount_path in self._resolve_dataset_mount_paths():
            for dataset in self._list_mounted_dataset_entries(dataset_mount_path):
                # Keep first discovered dataset when ids collide across roots.
                merged.setdefault(dataset.id, dataset)
        return list(merged.values())

    async def get_dataset(
        self,
        dataset_id: str,
        include_files: bool = True,
    ) -> Optional[DatasetResponse]:
        """Get dataset details using REST API."""
        started_at = time.perf_counter()
        if dataset_id.startswith("local:"):
            # Local dataset
            file_name = dataset_id.replace("local:", "")
            file_path = os.path.join(self.settings.datasets_path, file_name)

            if os.path.exists(file_path):
                stat = os.stat(file_path)
                return DatasetResponse(
                    id=dataset_id,
                    name=file_name,
                    path=file_path,
                    description="Local dataset",
                    size_bytes=stat.st_size,
                    file_count=1,
                    files=[DatasetFileResponse(name=file_name, path=file_path, size=stat.st_size)],
                )
            return None

        if dataset_id.startswith("domino:"):
            return self._get_mounted_dataset(dataset_id.replace("domino:", ""))

        # Domino dataset - use generated API client
        if self.settings.is_domino_environment:
            try:
                result = self._fetch_dataset_details(dataset_id)
                if not result:
                    return None
                dataset = await self._api_item_to_dataset_response(
                    result,
                    include_files=include_files,
                )
                if dataset is not None:
                    elapsed_ms = (time.perf_counter() - started_at) * 1000
                    logger.debug(
                        "Loaded dataset %s include_files=%s files=%s elapsed=%.1fms",
                        dataset_id,
                        include_files,
                        len(dataset.files),
                        elapsed_ms,
                    )
                    return dataset
            except Exception as e:
                logger.error(f"Failed to get dataset details: {e}")

        return None

    async def get_dataset_file_path(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
    ) -> str:
        """Get the file path for a dataset file."""
        if dataset_id.startswith("local:"):
            file_name = dataset_id.replace("local:", "")
            return os.path.join(self.settings.datasets_path, file_name)

        if dataset_id.startswith("domino:"):
            # Domino dataset from mounted dataset root
            dataset_name = dataset_id.replace("domino:", "")
            for mount_path in self._resolve_dataset_mount_paths():
                dataset_path = os.path.join(mount_path, dataset_name)
                if file_name:
                    candidate = os.path.join(dataset_path, file_name)
                    if os.path.exists(candidate):
                        return candidate
                if os.path.isfile(dataset_path):
                    if not file_name or os.path.basename(dataset_path) == file_name:
                        return dataset_path
                    continue
                if os.path.isdir(dataset_path):
                    if file_name:
                        continue
                    first_supported = self._first_supported_file(dataset_path)
                    if first_supported:
                        return first_supported
            if file_name:
                raise FileNotFoundError(
                    f"File '{file_name}' not found in dataset: {dataset_id} "
                    f"across mount roots {self._resolve_dataset_mount_paths()}"
                )
            raise FileNotFoundError(
                f"No data files found in dataset: {dataset_id} across mount roots {self._resolve_dataset_mount_paths()}"
            )

        # For other Domino datasets, files are mounted under the dataset root
        dataset = await self.get_dataset(dataset_id)
        if dataset:
            candidate_paths: list[str] = []
            if dataset.path:
                candidate_paths.append(dataset.path)
            for mount_path in self._resolve_dataset_mount_paths():
                candidate_paths.append(os.path.join(mount_path, dataset.name))

            # Preserve order and uniqueness.
            deduped_paths: list[str] = []
            seen_paths: set[str] = set()
            for candidate in candidate_paths:
                if not candidate:
                    continue
                normalized = os.path.abspath(candidate)
                if normalized in seen_paths:
                    continue
                deduped_paths.append(normalized)
                seen_paths.add(normalized)

            for dataset_path in deduped_paths:
                if file_name:
                    named_file_path = os.path.join(dataset_path, file_name)
                    if os.path.exists(named_file_path):
                        return named_file_path
                if os.path.isfile(dataset_path) and self._is_supported_file(dataset_path):
                    if not file_name or os.path.basename(dataset_path) == file_name:
                        return dataset_path
                    continue
                if os.path.isdir(dataset_path):
                    if file_name:
                        continue
                    first_supported = self._first_supported_file(dataset_path)
                    if first_supported:
                        return first_supported

            for file_entry in dataset.files:
                if file_name and file_entry.name != file_name:
                    continue
                if file_entry.path and os.path.exists(file_entry.path):
                    return file_entry.path

            if dataset.path and not file_name:
                return dataset.path

        if file_name:
            raise FileNotFoundError(
                f"File '{file_name}' not found in dataset: {dataset_id}"
            )
        raise FileNotFoundError(f"Dataset not found: {dataset_id}")

    async def preview_dataset(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
        rows: int = 100,
    ) -> DatasetPreviewResponse:
        """Preview dataset content."""
        file_path = await self.get_dataset_file_path(dataset_id, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        preview = read_tabular_preview(file_path, limit=rows, offset=0, include_dtypes=False)

        return DatasetPreviewResponse(
            dataset_id=dataset_id,
            file_name=os.path.basename(file_path),
            columns=preview["columns"],
            rows=preview["rows"],
            total_rows=preview["total_rows"],
            preview_rows=preview["preview_rows"],
        )

    async def get_schema(
        self,
        dataset_id: str,
        file_name: Optional[str] = None,
    ) -> DatasetSchemaResponse:
        """Get dataset schema (column names and types)."""
        file_path = await self.get_dataset_file_path(dataset_id, file_name)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        schema = read_tabular_schema(file_path)

        return DatasetSchemaResponse(
            dataset_id=dataset_id,
            file_name=os.path.basename(file_path),
            columns=schema["columns"],
            row_count=schema["row_count"],
        )
