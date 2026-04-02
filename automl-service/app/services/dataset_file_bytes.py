from fastapi import HTTPException
import httpx
import logging
from typing import Any

import app.core.domino_http as domino_http

logger = logging.getLogger(__name__)

MAX_REMOTE_PREVIEW_FILE_BYTES = 500 * 1024 * 1024


def _is_unset(value: Any) -> bool:
    return value.__class__.__name__ == "Unset"

def _coerce_optional_int(*values: Any) -> int:
    for value in values:
        if value is None or _is_unset(value):
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            continue
    return 0


def _snapshot_sort_key(snapshot: dict[str, Any]) -> tuple[int, int]:
    return (
        _coerce_optional_int(snapshot.get("version")),
        _coerce_optional_int(snapshot.get("creationTime")),
    )


def _normalize_dataset_preview_file_path(file_path: str) -> str:
    normalized_path = str(file_path or "").strip().lstrip("/")
    if not normalized_path:
        raise HTTPException(status_code=400, detail="file_path is required")
    return normalized_path

async def fetch(
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
    # TODO: why default to latest snapshot? why not provide snapshot / rwSnapshot picker?
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

