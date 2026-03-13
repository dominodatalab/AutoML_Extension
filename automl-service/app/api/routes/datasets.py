"""Dataset management endpoints."""

import logging
import mimetypes
import os
from typing import Optional

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
    get_dataset_manager,
    get_dataset_or_404,
    get_dataset_schema_response,
    list_datasets_response,
    preview_dataset_response,
    preview_file_response,
    save_uploaded_file,
)

router = APIRouter()


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
async def preview_file_by_path(request: FilePreviewRequest):
    """Preview a file by its path with pagination support."""
    return preview_file_response(
        file_path=request.file_path,
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
    """Upload a file for training."""
    from app.config import get_settings as _get_settings

    project_id = _resolve_project_id(request)
    upload_dir = None
    if project_id and not _get_settings().standalone_mode:
        from app.services.storage_resolver import get_storage_resolver

        resolver = get_storage_resolver()

        # Pre-create the dataset so future Jobs/restarts will have the mount.
        # Best-effort — upload proceeds regardless.
        await resolver.ensure_dataset_exists(project_id)

        # Use the mount if available; fall back to app-local uploads_path.
        mounted, mount_path = await resolver.check_project_storage(project_id)
        if mounted and mount_path:
            upload_dir = os.path.join(mount_path, "uploads")
        else:
            logger.info(
                "Dataset mount not available for project %s; using local uploads_path",
                project_id,
            )
        if upload_dir:
            os.makedirs(upload_dir, exist_ok=True)
    return await save_uploaded_file(file, upload_dir=upload_dir)
