"""Custom compatibility dataset routes."""

from fastapi import Body, FastAPI, File, Query, UploadFile, HTTPException
from typing import Optional
from app.api.schemas.dataset import CompatDatasetPreviewRequest
from app.services.dataset_service import (
    build_compat_dataset_preview_payload,
    get_dataset_manager,
    list_dataset_files_response,
    list_datasets_response,
)


def register_custom_dataset_routes(app: FastAPI) -> None:
    """Register custom /svc* dataset routes."""

    @app.get("/svcdataset/{dataset_id}/files")
    async def svc_list_dataset_files(dataset_id: str):
        return await list_dataset_files_response(dataset_id)

    @app.get("/svcdatasets")
    async def svc_list_datasets(projectId: Optional[str] = Query(None)):
        project_id = projectId
        if not project_id:
            raise HTTPException(status_code=400, detail="Project ID must be provided")

        return await list_datasets_response(get_dataset_manager(), project_id=projectId)

    @app.post("/svcdatasetpreview")
    async def svc_dataset_preview(
        body: CompatDatasetPreviewRequest = Body(...),
    ):
        return await build_compat_dataset_preview_payload(
            get_dataset_manager(),
            body,
        )

    @app.post("/svcupload")
    async def svc_upload_file(file: UploadFile = File(...)):
        raise HTTPException(status_code=501, detail="File upload is disabled")

        #result = await save_uploaded_file(file)
        #return result.model_dump() if hasattr(result, "model_dump") else result
