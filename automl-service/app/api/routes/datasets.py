"""Dataset viewing endpoints — list, detail, verify-snapshot."""

import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from app.api.error_handler import handle_errors
from app.api.utils import resolve_request_project_id
from app.api.schemas.dataset import (
    DatasetResponse,
    DatasetListResponse,
)
from app.services.dataset_service import (
    get_dataset_manager,
    get_dataset_or_404,
    list_datasets_response,
)

logger = logging.getLogger(__name__)
router = APIRouter()


def _resolve_project_id(request: Request) -> Optional[str]:
    """Extract project ID from request metadata with env var fallback."""
    return resolve_request_project_id(request)


@router.get("", response_model=DatasetListResponse)
@handle_errors("Failed to list datasets", detail_prefix="Failed to list datasets")
async def list_datasets(
    request: Request,
    include_files: bool = Query(True, description="Include file entries for each dataset"),
    dataset_manager=Depends(get_dataset_manager),
):
    """List available datasets scoped to the current project."""
    project_id = _resolve_project_id(request)
    return await list_datasets_response(
        dataset_manager,
        project_id=project_id,
        include_files=include_files,
    )


@router.get("/verify-snapshot")
async def verify_snapshot(
    dataset_id: str = Query(..., description="Dataset ID to check"),
    file_path: str = Query("", description="Relative file path to verify in the snapshot"),
):
    """Check whether the dataset's latest snapshot is active."""
    from app.services.storage_resolver import get_storage_resolver

    resolver = get_storage_resolver()
    try:
        status = await resolver.get_latest_snapshot_status(dataset_id)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Failed to check snapshot: {exc}") from exc

    return {
        "verified": status == "active",
        "dataset_id": dataset_id,
        "file_path": file_path,
        "snapshot_status": status,
    }


@router.get("/{dataset_id}", response_model=DatasetResponse)
@handle_errors("Failed to get dataset", detail_prefix="Failed to get dataset")
async def get_dataset(
    dataset_id: str,
    include_files: bool = Query(True, description="Include file entries for the dataset"),
    dataset_manager=Depends(get_dataset_manager),
):
    """Get dataset details."""
    return await get_dataset_or_404(
        dataset_manager,
        dataset_id,
        include_files=include_files,
    )


