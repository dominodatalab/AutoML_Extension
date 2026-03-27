"""Service helpers for dataset route orchestration."""

import logging
import os
from io import BytesIO
import shutil
import uuid
from functools import lru_cache
from typing import Any, Optional, Sequence

import numpy as np
import pandas as pd
import httpx
from fastapi import HTTPException, UploadFile

import app.core.domino_http as domino_http
from app.api.generated.domino_public_api_client.api.dataset_rw import get_dataset, get_datasets_v2
from app.api.generated.domino_public_api_client.models.dataset_rw_info_dto_v1 import DatasetRwInfoDtoV1
from app.api.generated.domino_public_api_client.models.dataset_rw_permission_v1 import DatasetRwPermissionV1
from app.api.generated_private.domino_data_lab_api_v_4_client.api.dataset import get_snapshot_files_at_root
from app.api.generated_private.domino_data_lab_api_v_4_client.api.dataset_rw import get_files_in_snapshot
from app.api.generated_private.domino_data_lab_api_v_4_client.client import Client as DominoPrivateApiClient
from app.core.domino_http import get_user_auth_headers

from app.api.schemas.dataset import (
    CompatDatasetPreviewRequest,
    DatasetFileResponse,
    DatasetListResponse,
    DatasetPreviewResponse,
    DatasetResponse,
    DatasetSchemaResponse,
    FileUploadResponse,
)
from app.config import get_settings
from app.core.dataset_mounts import resolve_dataset_mount_paths
from app.core.dataset_manager import DominoDatasetManager

ALLOWED_UPLOAD_EXTENSIONS = (".csv", ".parquet", ".pq")
DEFAULT_PREVIEW_LIMIT = 100
MAX_PREVIEW_LIMIT = 1000
MAX_REMOTE_PREVIEW_FILE_BYTES = 500 * 1024 * 1024

logger = logging.getLogger(__name__)


@lru_cache()
def get_dataset_manager() -> DominoDatasetManager:
    """Get dataset manager instance (cached)."""
    return DominoDatasetManager()


def _safe_int(value: Any, field_name: str) -> int:
    """Convert value to int or raise a 400 validation error."""
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise HTTPException(status_code=400, detail=f"{field_name} must be an integer") from exc


def get_dataset_mount_root() -> str:
    """Resolve dataset mount root for current runtime."""
    mount_paths = resolve_dataset_mount_paths(fallback_path=get_settings().datasets_path)
    if mount_paths:
        return mount_paths[0]
    return get_settings().datasets_path


def get_dataset_mount_roots() -> list[str]:
    """Resolve all candidate dataset mount roots for the active runtime."""
    return resolve_dataset_mount_paths(fallback_path=get_settings().datasets_path)


def _extract_file_path(file_entry: Any) -> Optional[str]:
    if isinstance(file_entry, dict):
        path = file_entry.get("path")
        return str(path) if path else None
    if hasattr(file_entry, "path"):
        path = getattr(file_entry, "path")
        return str(path) if path else None
    return None


def filter_local_datasets(
    datasets: Sequence[Any],
    local_path: Optional[str] = None,
    local_paths: Optional[Sequence[str]] = None,
) -> list[Any]:
    """Return only datasets that are mounted in the active dataset path."""
    filtered_datasets: list[Any] = []
    resolved_paths = list(local_paths) if local_paths else []
    if local_path:
        resolved_paths.append(local_path)
    if not resolved_paths:
        resolved_paths = get_dataset_mount_roots()

    for ds in datasets:
        ds_name = getattr(ds, "name", None)
        ds_id = str(getattr(ds, "id", ""))
        ds_files = getattr(ds, "files", []) or []

        if not ds_name or ds_name.startswith("/") or ds_id.startswith("/"):
            continue

        found_on_mount = False
        for root in resolved_paths:
            if os.path.exists(os.path.join(root, ds_name)):
                found_on_mount = True
                break

        if not found_on_mount:
            for file_entry in ds_files:
                file_path = _extract_file_path(file_entry)
                if file_path and os.path.exists(file_path):
                    found_on_mount = True
                    break

        if found_on_mount or ds_id.startswith("domino:"):
            filtered_datasets.append(ds)

    return filtered_datasets


def _is_unset(value: Any) -> bool:
    return value.__class__.__name__ == "Unset"


def _first_defined(*values: Any) -> Any:
    for value in values:
        if value is None or _is_unset(value):
            continue
        return value
    return None


def _coerce_optional_int(*values: Any) -> int:
    for value in values:
        if value is None or _is_unset(value):
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            continue
    return 0


def _build_dataset_file_rows(dataset_id: str, dataset_name: str, rows: Sequence[Any], base_path: str = "") -> list[DatasetFileResponse]:
    normalized_rows: list[DatasetFileResponse] = []
    normalized_base_path = base_path.strip("/")

    for row in rows:
        name_entry = row.name
        size_entry = row.size

        file_name = name_entry.sortable_name or name_entry.file_name or name_entry.label

        if not file_name:
            logger.debug(f"Unable to resolve the file name for row {name_entry.label} in dataset {dataset_name} {dataset_id}")
            continue

        full_path = file_name if not normalized_base_path else f"{normalized_base_path}/{file_name}"
        normalized_rows.append(
            DatasetFileResponse(
                name=file_name,
                path=full_path,
                size=size_entry.size_in_bytes,
            )
        )

    return normalized_rows


def _normalize_dataset_preview_file_path(file_path: str) -> str:
    normalized_path = str(file_path or "").strip().lstrip("/")
    if not normalized_path:
        raise HTTPException(status_code=400, detail="file_path is required")
    return normalized_path


def _snapshot_sort_key(snapshot: dict[str, Any]) -> tuple[int, int]:
    return (
        _coerce_optional_int(snapshot.get("version")),
        _coerce_optional_int(snapshot.get("creationTime")),
    )


async def _fetch_domino_dataset_file_bytes(
    dataset_id: str,
    file_path: str,
) -> bytes:
    normalized_path = _normalize_dataset_preview_file_path(file_path)

    try:
        snapshots_payload = await domino_http.domino_get_dataset_rw_snapshots(dataset_id)
    except httpx.HTTPStatusError as exc:
        status_code = exc.response.status_code
        if status_code == 404:
            raise HTTPException(status_code=404, detail=f"Dataset not found: {dataset_id}") from exc
        raise HTTPException(
            status_code=status_code,
            detail=f"Failed to resolve snapshots for dataset {dataset_id}",
        ) from exc

    if not isinstance(snapshots_payload, list) or not snapshots_payload:
        raise HTTPException(status_code=404, detail=f"No snapshots found for dataset {dataset_id}")

    latest_snapshot = max(snapshots_payload, key=_snapshot_sort_key)
    snapshot_id = latest_snapshot.get("id")
    if not snapshot_id:
        raise HTTPException(status_code=500, detail=f"Failed to resolve a snapshot for dataset {dataset_id}")

    try:
        metadata_payload = await domino_http.domino_get_dataset_snapshot_file_metadata(
            snapshot_id=snapshot_id,
            path=normalized_path,
        )
    except httpx.HTTPStatusError as exc:
        status_code = exc.response.status_code
        if status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"File not found in dataset {dataset_id}: {normalized_path}",
            ) from exc
        raise HTTPException(
            status_code=status_code,
            detail=f"Failed to fetch metadata for dataset file {normalized_path}",
        ) from exc

    file_size = _coerce_optional_int(metadata_payload.get("fileSize"))
    if metadata_payload.get("exceedsSizeLimit") is True or file_size > MAX_REMOTE_PREVIEW_FILE_BYTES:
        raise HTTPException(
            status_code=413,
            detail=(
                f"Dataset file is too large to preview over API: {normalized_path} "
                f"({file_size} bytes, limit {MAX_REMOTE_PREVIEW_FILE_BYTES} bytes)"
            ),
        )

    try:
        file_bytes = await domino_http.domino_get_dataset_snapshot_file_raw(
            snapshot_id=snapshot_id,
            path=normalized_path,
        )
    except httpx.HTTPStatusError as exc:
        status_code = exc.response.status_code
        if status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"File not found in dataset {dataset_id}: {normalized_path}",
            ) from exc
        raise HTTPException(
            status_code=status_code,
            detail=f"Failed to fetch dataset file {normalized_path} for dataset {dataset_id}",
        ) from exc

    logger.info(
        "Fetched dataset file %s for dataset %s from snapshot %s (%s bytes)",
        normalized_path,
        dataset_id,
        snapshot_id,
        len(file_bytes),
    )
    return file_bytes


async def list_dataset_files_response(dataset_id: str):
    public_client = domino_http.get_domino_public_api_client_sync()
    private_client = domino_http.get_domino_private_api_client_sync()

    dataset_result = await get_dataset.asyncio(dataset_id=dataset_id, client=public_client)
    if dataset_result is None:
        raise HTTPException(500, "Empty response when getting root snapshot files for dataset")

    dataset = dataset_result.dataset
    snapshot_ids = dataset.snapshot_ids

    if len(snapshot_ids) == 0:
        logger.debug(f"Found no snapshots for dataset {dataset_id}")
        return DatasetListResponse(datasets=[], total=0)

    root_files_result = await get_files_in_snapshot.asyncio(
        snapshot_id=snapshot_ids[0],
        client=private_client,
        path=""
    )

    if root_files_result is None:
        raise HTTPException(500, "Empty response when getting root snapshot files for dataset")

    file_rows = _build_dataset_file_rows(dataset.id, dataset.name, root_files_result.rows)

    dataset_response = DatasetResponse(
        id=dataset.id,
        name=dataset.name,
        path=None,
        description=_first_defined(dataset.description),
        size_bytes=sum(file.size for file in file_rows),
        created_at=dataset.created_at,
        updated_at=None,
        file_count=len(file_rows),
        files=file_rows,
    )

    logger.debug(
        "Returning %s files for dataset %s",
        dataset_response.file_count,
        dataset_id,
    )
    return DatasetListResponse(datasets=[dataset_response], total=1)

async def list_datasets_response(
    dataset_manager: DominoDatasetManager,
    project_id: str,
) -> DatasetListResponse:
    """List Domino datasets in API response shape."""

    client = domino_http.get_domino_public_api_client_sync()
    response = await get_datasets_v2.asyncio(
        client=client,
        minimum_permission=DatasetRwPermissionV1.READDATASETRWV2,
        project_ids_to_include=[project_id],
        include_project_info=True,
        offset=0,
        limit=100,
    )

    if response is None:
        raise HTTPException(status_code=500, detail="Failed to list datasets from Domino. No response")

    def build_details(d: DatasetRwInfoDtoV1) -> DatasetResponse:
        dataset = d.dataset
        return DatasetResponse(
            id=dataset.id,
            name=dataset.name,
            path=None,
            description=dataset.description,
            size_bytes=0,
            created_at=dataset.created_at,
            updated_at=None,
            file_count=0,
            files=[],
        )

    datasets = [build_details(d) for d in response.datasets]
    total = response.metadata.total_count or len(datasets)

    logger.info("Returning %s Domino datasets for project %s", len(datasets), project_id)
    return DatasetListResponse(datasets=datasets, total=total)


async def get_dataset_or_404(
    dataset_manager: DominoDatasetManager,
    dataset_id: str,
) -> DatasetResponse:
    """Get dataset details or raise a 404."""
    dataset = await dataset_manager.get_dataset(dataset_id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


async def preview_dataset_response(
    dataset_manager: DominoDatasetManager,
    dataset_id: str,
    file_name: Optional[str] = None,
    rows: int = DEFAULT_PREVIEW_LIMIT,
) -> DatasetPreviewResponse:
    """Preview a dataset file via manager."""
    return await dataset_manager.preview_dataset(dataset_id, file_name=file_name, rows=rows)


async def get_dataset_schema_response(
    dataset_manager: DominoDatasetManager,
    dataset_id: str,
    file_name: Optional[str] = None,
) -> DatasetSchemaResponse:
    """Get dataset schema via manager."""
    return await dataset_manager.get_schema(dataset_id, file_name=file_name)


def normalize_preview_pagination(
    limit: Optional[Any] = None,
    rows: Optional[Any] = None,
    offset: Optional[Any] = 0,
) -> tuple[int, int]:
    """Normalize preview pagination params with sensible bounds."""
    # Keep parity with existing route semantics:
    # - falsy `limit` falls back to `rows` then default
    # - negative offsets are clamped to zero
    resolved_limit_raw = limit if limit else rows
    if not resolved_limit_raw:
        resolved_limit_raw = DEFAULT_PREVIEW_LIMIT

    resolved_limit = _safe_int(resolved_limit_raw, "limit")
    if resolved_limit < 1:
        resolved_limit = DEFAULT_PREVIEW_LIMIT

    resolved_offset = _safe_int(offset or 0, "offset")
    if resolved_offset < 0:
        resolved_offset = 0

    return min(resolved_limit, MAX_PREVIEW_LIMIT), resolved_offset


def build_preview_payload(
    file_path: str,
    limit: int = DEFAULT_PREVIEW_LIMIT,
    offset: int = 0,
    include_dtypes: bool = False,
    file_bytes: Optional[bytes] = None,
) -> dict[str, Any]:
    """Read and paginate a local CSV/Parquet file preview."""
    bytes_io_object = None
    if file_bytes is not None:
        bytes_io_object = BytesIO(file_bytes)

    if not file_path:
        raise HTTPException(status_code=400, detail="file_path is required")

    if not os.path.exists(file_path) and not bytes_io_object:
        raise HTTPException(status_code=404, detail=f"Content not provided and file not found: {file_path}")

    file_ext = os.path.splitext(file_path)[1].lower()

    df_content = bytes_io_object or file_path

    if file_ext == ".csv":
        # if df_conetnt is bytes in memory, total_rows is length of dataset

        total_rows = None
        if not bytes_io_object:
            with open(file_path, "r") as f:
                total_rows = max(sum(1 for _ in f) - 1, 0)

        if offset > 0:
            df = pd.read_csv(df_content, skiprows=range(1, offset + 1), nrows=limit)
        else:
            df = pd.read_csv(df_content, nrows=limit)

        if total_rows is None:
            total_rows = len(df)

    elif file_ext in [".parquet", ".pq"]:
        df_full = pd.read_parquet(df_content)
        total_rows = len(df_full)
        df = df_full.iloc[offset : offset + limit]
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    safe_df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
    payload: dict[str, Any] = {
        "dataset_id": file_path,
        "file_path": file_path,
        "file_name": os.path.basename(file_path),
        "columns": list(df.columns),
        "rows": safe_df.to_dict(orient="records"),
        "total_rows": total_rows,
        "preview_rows": len(df),
    }
    if include_dtypes:
        payload["dtypes"] = {col: str(dtype) for col, dtype in df.dtypes.items()}

    return payload


def preview_file_response(
    file_path: str,
    limit: Optional[Any] = None,
    rows: Optional[Any] = None,
    offset: Optional[Any] = 0,
) -> DatasetPreviewResponse:
    """Build typed dataset preview response for a local file path."""
    normalized_limit, normalized_offset = normalize_preview_pagination(
        limit=limit,
        rows=rows,
        offset=offset,
    )
    return DatasetPreviewResponse(
        **build_preview_payload(
            file_path=file_path,
            limit=normalized_limit,
            offset=normalized_offset,
        )
    )


def coerce_preview_response(preview: Any, include_dtypes: bool = False) -> dict[str, Any]:
    """Normalize preview object into a dict payload for compat endpoints."""
    if hasattr(preview, "model_dump"):
        payload = preview.model_dump()
    elif hasattr(preview, "dict"):
        payload = preview.dict()
    elif isinstance(preview, dict):
        payload = dict(preview)
    else:
        payload = dict(preview)

    payload.setdefault("file_path", payload.get("dataset_id"))
    if include_dtypes:
        payload.setdefault("dtypes", {})
    return payload


async def build_compat_dataset_preview_payload(
    dataset_manager: DominoDatasetManager,
    body: CompatDatasetPreviewRequest,
) -> dict[str, Any]:
    """Build compat dataset preview payload from request body."""
    file_path = body.file_path
    dataset_id = body.dataset_id
    limit, offset = normalize_preview_pagination(
        limit=body.limit,
        rows=body.rows,
        offset=body.offset,
    )
    file_bytes = await _fetch_domino_dataset_file_bytes(dataset_id=dataset_id, file_path=file_path)

    return build_preview_payload(
        file_path=file_path,
        limit=limit,
        offset=offset,
        include_dtypes=True,
        file_bytes=file_bytes
    )


async def save_uploaded_file(file: UploadFile) -> FileUploadResponse:
    """Save an uploaded dataset file and return metadata."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type not supported. Allowed: {list(ALLOWED_UPLOAD_EXTENSIONS)}",
        )

    upload_dir = get_settings().uploads_path
    os.makedirs(upload_dir, exist_ok=True)

    unique_id = str(uuid.uuid4())[:8]
    safe_filename = f"{unique_id}_{file.filename}"
    file_path = os.path.join(upload_dir, safe_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {exc}") from exc

    try:
        if file_ext == ".csv":
            header_df = pd.read_csv(file_path, nrows=0)
            with open(file_path, "r") as f:
                row_count = max(sum(1 for _ in f) - 1, 0)
        else:
            header_df = pd.read_parquet(file_path)
            row_count = len(header_df)

        columns = list(header_df.columns)
        file_size = os.path.getsize(file_path)
    except Exception as exc:
        os.remove(file_path)
        raise HTTPException(status_code=400, detail=f"Failed to read file: {exc}") from exc

    return FileUploadResponse(
        success=True,
        file_path=file_path,
        file_name=file.filename,
        file_size=file_size,
        columns=columns,
        row_count=row_count,
    )
