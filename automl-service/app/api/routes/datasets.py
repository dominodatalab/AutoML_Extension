"""Dataset management endpoints."""

import hashlib
import logging
import mimetypes
import os
import uuid
from io import BytesIO
from typing import Optional

import pandas as pd

logger = logging.getLogger(__name__)

from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File, Query
from fastapi.responses import FileResponse

from app.api.error_handler import handle_errors

from app.api.schemas.dataset import (
    DatasetResponse,
    DatasetListResponse,
    DatasetPreviewResponse,
    DatasetSchemaResponse,
    FilePreviewRequest,
    FileUploadResponse,
)
from app.services.dataset_service import (
    ALLOWED_UPLOAD_EXTENSIONS,
    get_dataset_manager,
    get_dataset_or_404,
    get_dataset_schema_response,
    list_datasets_response,
    preview_dataset_response,
    preview_file_response,
    save_uploaded_file,
)

router = APIRouter()

_VERIFY_BACKOFF = [1, 2, 3, 4, 5]  # ~15s total — keep short to avoid proxy timeouts


async def _verify_snapshot_active(resolver, dataset_id: str) -> bool:
    """Poll dataset snapshot status until it becomes ``active`` (or timeout).

    The Domino Dataset RW API does not expose a file-listing endpoint.
    Instead we check the latest snapshot's ``status`` field — ``active``
    means the upload commit is complete and files are available on the mount.
    """
    import asyncio

    for delay in _VERIFY_BACKOFF:
        await asyncio.sleep(delay)
        try:
            status = await resolver.get_latest_snapshot_status(dataset_id)
            if status == "active":
                logger.info("Snapshot active for dataset %s", dataset_id)
                return True
            logger.debug("Snapshot status for %s: %s", dataset_id, status)
        except Exception:
            logger.debug("Snapshot status poll failed for %s", dataset_id, exc_info=True)
    logger.warning("Snapshot verification timed out for dataset %s", dataset_id)
    return False


def _resolve_project_id(request: Request) -> Optional[str]:
    """Extract project ID from request header with env var fallback."""
    return (
        request.headers.get("X-Project-Id")
        or os.environ.get("DOMINO_PROJECT_ID")
        or None
    )


@router.get("", response_model=DatasetListResponse)
@handle_errors("Failed to list datasets", detail_prefix="Failed to list datasets")
async def list_datasets(
    request: Request,
    dataset_manager=Depends(get_dataset_manager),
):
    """List available datasets scoped to the current project."""
    project_id = _resolve_project_id(request)
    return await list_datasets_response(dataset_manager, project_id=project_id)


@router.get("/verify-snapshot")
async def verify_snapshot(
    dataset_id: str = Query(..., description="Dataset ID to check"),
    file_path: str = Query("", description="Expected file path (unused, kept for compat)"),
):
    """Check whether the dataset's latest snapshot is active.

    The Domino Dataset RW API has no file-listing endpoint, so we check
    the snapshot status instead.  ``active`` means the upload has been
    committed and files are available on the dataset mount.
    """
    from app.services.storage_resolver import get_storage_resolver

    resolver = get_storage_resolver()
    try:
        status = await resolver.get_latest_snapshot_status(dataset_id)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Failed to check snapshot: {exc}") from exc

    verified = status == "active"
    return {
        "verified": verified,
        "dataset_id": dataset_id,
        "file_path": file_path,
        "snapshot_status": status,
    }


@router.get("/{dataset_id}", response_model=DatasetResponse)
@handle_errors("Failed to get dataset", detail_prefix="Failed to get dataset")
async def get_dataset(
    dataset_id: str,
    dataset_manager=Depends(get_dataset_manager),
):
    """Get dataset details."""
    return await get_dataset_or_404(dataset_manager, dataset_id)


@router.get("/{dataset_id}/preview", response_model=DatasetPreviewResponse)
@handle_errors("Failed to preview dataset", detail_prefix="Failed to preview dataset")
async def preview_dataset(
    dataset_id: str,
    file_name: Optional[str] = Query(None, description="Specific file to preview"),
    rows: int = Query(100, ge=1, le=1000, description="Number of rows to preview"),
    dataset_manager=Depends(get_dataset_manager),
):
    """Preview dataset content."""
    return await preview_dataset_response(
        dataset_manager=dataset_manager,
        dataset_id=dataset_id,
        file_name=file_name,
        rows=rows,
    )


@router.get("/{dataset_id}/schema", response_model=DatasetSchemaResponse)
@handle_errors("Failed to get dataset schema", detail_prefix="Failed to get dataset schema")
async def get_dataset_schema(
    dataset_id: str,
    file_name: Optional[str] = Query(None, description="Specific file to get schema for"),
    dataset_manager=Depends(get_dataset_manager),
):
    """Get dataset schema (column names and types)."""
    return await get_dataset_schema_response(
        dataset_manager=dataset_manager,
        dataset_id=dataset_id,
        file_name=file_name,
    )


@router.post("/preview", response_model=DatasetPreviewResponse)
@handle_errors("[PREVIEW] Error reading file", detail_prefix="Failed to read file")
async def preview_file_by_path(request: FilePreviewRequest, http_request: Request):
    """Preview a file by its path with pagination support."""
    from app.core.utils import ensure_local_file

    project_id = http_request.headers.get("X-Project-Id")
    resolved_path = await ensure_local_file(request.file_path, project_id)
    return preview_file_response(
        file_path=resolved_path,
        limit=request.limit,
        rows=request.rows,
        offset=request.offset,
    )


@router.get("/{dataset_id}/files/{file_name:path}/download")
async def download_dataset_file(
    dataset_id: str,
    file_name: str,
    dataset_manager=Depends(get_dataset_manager),
):
    """Download a file from a mounted dataset."""
    try:
        file_path = await dataset_manager.get_dataset_file_path(dataset_id, file_name)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"File '{file_name}' not found in dataset {dataset_id}")

    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"File not found at resolved path: {file_path}")

    media_type, _ = mimetypes.guess_type(file_path)
    return FileResponse(
        path=file_path,
        filename=os.path.basename(file_path),
        media_type=media_type or "application/octet-stream",
    )


@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(
    request: Request,
    file: UploadFile = File(..., description="CSV or Parquet file to upload"),
):
    """Upload a file for training.

    When a target project_id is present (and not standalone), reads the file
    into memory and uploads it directly to the project's automl-extension
    dataset via the v4 chunked API — no local file needed.

    Falls back to local disk via ``save_uploaded_file`` when no project_id
    is available or in standalone mode.
    """
    from app.config import get_settings as _get_settings

    project_id = _resolve_project_id(request)

    if project_id and not _get_settings().standalone_mode:
        # --- Domino dataset upload path (in-memory) ---
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")

        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in ALLOWED_UPLOAD_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"File type not supported. Allowed: {list(ALLOWED_UPLOAD_EXTENSIONS)}",
            )

        content = await file.read()

        safe_filename = f"{str(uuid.uuid4())[:8]}_{file.filename}"

        # Extract metadata from the in-memory buffer
        try:
            if file_ext == ".csv":
                header_df = pd.read_csv(BytesIO(content), nrows=0)
                row_count = max(content.count(b"\n") - 1, 0)
            else:
                pq_df = pd.read_parquet(BytesIO(content))
                header_df = pq_df
                row_count = len(pq_df)
            columns = list(header_df.columns)
        except Exception as exc:
            raise HTTPException(
                status_code=400, detail=f"Failed to read file: {exc}"
            ) from exc

        from app.services.storage_resolver import get_storage_resolver

        resolver = get_storage_resolver()

        dataset_info = await resolver.ensure_dataset_exists(project_id)
        if not dataset_info:
            raise HTTPException(
                status_code=502,
                detail=f"Failed to create/find dataset for project {project_id}",
            )

        dataset_path = f"uploads/{safe_filename}"
        try:
            await resolver.upload_file(
                dataset_info.dataset_id, dataset_path, content
            )
        except Exception as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Failed to upload file to dataset: {exc}",
            ) from exc

        # Canonical mount path the training job will see.
        # Use the probed mount if available; otherwise pick the best guess
        # based on project type (DFS vs git-based).
        mount = dataset_info.mount_path
        if not mount:
            mount = resolver._probe_mount(dataset_info.name)
        if not mount:
            from app.core.domino_project_type import detect_project_type, DominoProjectType
            project_type = detect_project_type()
            if project_type == DominoProjectType.GIT:
                mount = f"/mnt/data/{dataset_info.name}"
            else:
                mount = f"/domino/datasets/local/{dataset_info.name}"
            logger.info("No mount probed; using %s default: %s", project_type.value, mount)
        file_path = f"{mount}/{dataset_path}"

        # Save a local copy so ensure_local_file() can resolve the mount path
        # without needing a download API (which Domino doesn't provide).
        try:
            settings = _get_settings()
            cache_key = hashlib.sha256(
                f"{dataset_info.dataset_id}:{dataset_path}".encode()
            ).hexdigest()[:16]
            local_cache_path = os.path.join(
                settings.temp_path, "dataset_cache", cache_key, dataset_path
            )
            os.makedirs(os.path.dirname(local_cache_path), exist_ok=True)
            with open(local_cache_path, "wb") as fh:
                fh.write(content)
            logger.info("Cached upload locally: %s", local_cache_path)
        except Exception:
            logger.warning("Failed to cache upload locally", exc_info=True)

        # Verify the snapshot is active (upload committed) before returning
        snapshot_verified = await _verify_snapshot_active(
            resolver, dataset_info.dataset_id
        )

        return FileUploadResponse(
            success=True,
            file_path=file_path,
            file_name=file.filename,
            file_size=len(content),
            columns=columns,
            row_count=row_count,
            dataset_id=dataset_info.dataset_id,
            snapshot_file_path=dataset_path,
            snapshot_verified=snapshot_verified,
        )

    # --- Standalone / no project_id: save to local disk ---
    return await save_uploaded_file(file)
