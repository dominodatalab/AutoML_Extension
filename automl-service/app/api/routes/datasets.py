"""Dataset management endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query

from app.api.error_handler import handle_errors

from app.api.schemas.dataset import (
    DatasetFilePreviewRequest,
    DatasetResponse,
    DatasetListResponse,
    DatasetPreviewResponse,
    DatasetSchemaResponse,
    FileUploadResponse,
)
from app.services.dataset_service import (
    get_dataset_manager,
    get_dataset_or_404,
    get_dataset_schema_response,
    list_dataset_files_response,
    list_datasets_response,
    preview_dataset_response,
    preview_file_path_response,
    preview_file_response,
    save_uploaded_file,
)

router = APIRouter()


@router.get("", response_model=DatasetListResponse)
@handle_errors("Failed to list datasets", detail_prefix="Failed to list datasets")
async def list_datasets(
    projectId: Optional[str] = Query(None),
):
    """List available datasets in a project."""
    project_id = projectId
    if not project_id:
        raise HTTPException(status_code=400, detail="projectId query parameter is required")
    return await list_datasets_response(project_id=project_id)


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


@router.get("/{dataset_id}/files")
@handle_errors("Failed to list dataset files", detail_prefix="Failed to list dataset files")
async def get_dataset_files(dataset_id: str):
    """List files within a dataset."""
    return await list_dataset_files_response(dataset_id)


@router.post("/preview")
@handle_errors("Failed to preview dataset file", detail_prefix="Failed to preview dataset file")
async def preview_dataset_file(
    body: DatasetFilePreviewRequest,
    dataset_manager=Depends(get_dataset_manager),
):
    """Preview a dataset file by file path or dataset ID."""
    return await preview_file_path_response(dataset_manager=dataset_manager, body=body)


@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(
    file: UploadFile = File(..., description="CSV or Parquet file to upload"),
):
    """Upload a file for training."""
    return await save_uploaded_file(file)
