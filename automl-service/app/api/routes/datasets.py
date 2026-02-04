"""Dataset management endpoints."""

import logging
import os
import shutil
from typing import Optional

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings

logger = logging.getLogger(__name__)

# Log when this module is loaded to verify which version is running
logger.info("[DATASETS MODULE] Loaded - upload_dir will be /mnt/automl-service/uploads")
print("[DATASETS MODULE] Loaded - upload_dir will be /mnt/automl-service/uploads", flush=True)
from app.dependencies import get_db
from app.core.dataset_manager import DominoDatasetManager
from app.api.schemas.dataset import (
    DatasetResponse,
    DatasetListResponse,
    DatasetPreviewResponse,
    DatasetSchemaResponse,
    FileUploadResponse,
)

router = APIRouter()


def get_dataset_manager() -> DominoDatasetManager:
    """Get dataset manager instance."""
    return DominoDatasetManager()


@router.get("", response_model=DatasetListResponse)
async def list_datasets(
    dataset_manager: DominoDatasetManager = Depends(get_dataset_manager),
):
    """List available Domino datasets from /domino/datasets/local/ only."""
    try:
        datasets = await dataset_manager.list_datasets()

        # Only return datasets that exist in /domino/datasets/local/
        # This filters out any datasets from Domino API that aren't mounted locally
        local_path = "/domino/datasets/local"
        filtered_datasets = []

        for ds in datasets:
            # Skip datasets with path-like names
            if not ds.name or ds.name.startswith("/") or ds.id.startswith("/"):
                continue

            # Check if this dataset exists in /domino/datasets/local/
            dataset_path = os.path.join(local_path, ds.name)
            if os.path.exists(dataset_path):
                filtered_datasets.append(ds)
            elif ds.id.startswith("domino:"):
                # Already validated by _list_local_datasets
                filtered_datasets.append(ds)

        logger.info(f"Returning {len(filtered_datasets)} datasets (filtered from {len(datasets)})")

        return DatasetListResponse(
            datasets=filtered_datasets,
            total=len(filtered_datasets),
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list datasets: {str(e)}",
        )


@router.get("/{dataset_id}", response_model=DatasetResponse)
async def get_dataset(
    dataset_id: str,
    dataset_manager: DominoDatasetManager = Depends(get_dataset_manager),
):
    """Get dataset details."""
    try:
        dataset = await dataset_manager.get_dataset(dataset_id)
        if not dataset:
            raise HTTPException(status_code=404, detail="Dataset not found")
        return dataset
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get dataset: {str(e)}",
        )


@router.get("/{dataset_id}/preview", response_model=DatasetPreviewResponse)
async def preview_dataset(
    dataset_id: str,
    file_name: Optional[str] = Query(None, description="Specific file to preview"),
    rows: int = Query(100, ge=1, le=1000, description="Number of rows to preview"),
    dataset_manager: DominoDatasetManager = Depends(get_dataset_manager),
):
    """Preview dataset content."""
    try:
        preview = await dataset_manager.preview_dataset(
            dataset_id, file_name=file_name, rows=rows
        )
        return preview
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to preview dataset: {str(e)}",
        )


@router.get("/{dataset_id}/schema", response_model=DatasetSchemaResponse)
async def get_dataset_schema(
    dataset_id: str,
    file_name: Optional[str] = Query(None, description="Specific file to get schema for"),
    dataset_manager: DominoDatasetManager = Depends(get_dataset_manager),
):
    """Get dataset schema (column names and types)."""
    try:
        schema = await dataset_manager.get_schema(dataset_id, file_name=file_name)
        return schema
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get dataset schema: {str(e)}",
        )


class PreviewRequest(BaseModel):
    """Request body for file preview."""
    file_path: str
    limit: int = 100
    offset: int = 0
    rows: Optional[int] = None  # Legacy support


@router.post("/preview", response_model=DatasetPreviewResponse)
async def preview_file_by_path(request: PreviewRequest):
    """Preview a file by its path with pagination support."""
    file_path = request.file_path
    limit = min(request.limit if request.limit else (request.rows or 100), 1000)
    offset = max(request.offset, 0)

    logger.info(f"[PREVIEW] Request for file: {file_path}, limit: {limit}, offset: {offset}")

    if not file_path:
        raise HTTPException(status_code=400, detail="file_path is required")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File not found: {file_path}")

    try:
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext == ".csv":
            # Count total rows first
            with open(file_path, 'r') as f:
                total_rows = sum(1 for _ in f) - 1
            # Read with skip and limit for pagination
            if offset > 0:
                df = pd.read_csv(file_path, skiprows=range(1, offset + 1), nrows=limit)
            else:
                df = pd.read_csv(file_path, nrows=limit)
        elif file_ext in [".parquet", ".pq"]:
            df_full = pd.read_parquet(file_path)
            total_rows = len(df_full)
            df = df_full.iloc[offset:offset + limit]
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")

        return DatasetPreviewResponse(
            dataset_id=file_path,
            file_name=os.path.basename(file_path),
            columns=list(df.columns),
            rows=df.to_dict(orient="records"),
            total_rows=total_rows,
            preview_rows=len(df),
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"[PREVIEW] Error reading file: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")


@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(
    file: UploadFile = File(..., description="CSV or Parquet file to upload"),
):
    """Upload a file for training."""
    import uuid
    settings = get_settings()

    # Validate file type
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    allowed_extensions = [".csv", ".parquet", ".pq"]
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"File type not supported. Allowed: {allowed_extensions}",
        )

    # Save file to persistent location with unique prefix to avoid collisions
    # HARDCODED to bypass any settings caching issues
    upload_dir = "/mnt/automl-service/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    # DEBUG: Log the upload directory being used
    logger.info(f"[UPLOAD] Using hardcoded upload_dir: {upload_dir}")

    # Add unique prefix to avoid filename collisions
    unique_id = str(uuid.uuid4())[:8]
    safe_filename = f"{unique_id}_{file.filename}"
    file_path = os.path.join(upload_dir, safe_filename)
    logger.info(f"[UPLOAD] Saving file to: {file_path}")

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save file: {str(e)}",
        )

    # Read file to get metadata
    try:
        if file_ext == ".csv":
            df = pd.read_csv(file_path, nrows=0)
        else:
            df = pd.read_parquet(file_path)

        columns = list(df.columns)
        row_count = len(pd.read_csv(file_path)) if file_ext == ".csv" else len(df)
        file_size = os.path.getsize(file_path)

    except Exception as e:
        os.remove(file_path)
        raise HTTPException(
            status_code=400,
            detail=f"Failed to read file: {str(e)}",
        )

    return FileUploadResponse(
        success=True,
        file_path=file_path,
        file_name=file.filename,
        file_size=file_size,
        columns=columns,
        row_count=row_count,
    )
