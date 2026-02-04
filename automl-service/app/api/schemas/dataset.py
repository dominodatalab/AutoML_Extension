"""Dataset-related Pydantic schemas."""

from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, Field


class DatasetResponse(BaseModel):
    """Response schema for a dataset."""

    id: str
    name: str
    description: Optional[str] = None
    size_bytes: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    file_count: int = 0
    files: list[str] = []


class DatasetListResponse(BaseModel):
    """Response schema for dataset list."""

    datasets: list[DatasetResponse]
    total: int


class DatasetPreviewResponse(BaseModel):
    """Response schema for dataset preview."""

    dataset_id: str
    file_name: str
    columns: list[str]
    rows: list[dict[str, Any]]
    total_rows: int
    preview_rows: int


class DatasetSchemaResponse(BaseModel):
    """Response schema for dataset schema."""

    dataset_id: str
    file_name: str
    columns: list[dict[str, str]]  # {"name": str, "dtype": str}
    row_count: int


class FileUploadResponse(BaseModel):
    """Response schema for file upload."""

    success: bool
    file_path: str
    file_name: str
    file_size: int
    columns: list[str]
    row_count: int
