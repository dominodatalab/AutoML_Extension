"""Custom compatibility dataset routes."""

from fastapi import Body, FastAPI, File, Query, Request, UploadFile
from app.api.utils import resolve_request_project_id
from app.services.dataset_service import (
    build_compat_dataset_preview_payload,
    get_dataset_or_404,
    get_dataset_manager,
    list_datasets_response,
    save_uploaded_file,
)


def register_custom_dataset_routes(app: FastAPI) -> None:
    """Register custom /svc* dataset routes."""

    @app.get("/svcdatasets")
    async def svc_list_datasets(
        request: Request,
        include_files: bool = Query(True, description="Include file entries for each dataset"),
    ):
        project_id = resolve_request_project_id(request)
        return await list_datasets_response(
            get_dataset_manager(),
            project_id=project_id,
            include_files=include_files,
        )

    @app.post("/svcdatasetpreview")
    async def svc_dataset_preview(request: Request, body: dict = Body(default={})):
        # Resolve file path through cache for cross-project uploads
        file_path = body.get("file_path")
        if file_path:
            from app.core.utils import ensure_local_file

            project_id = resolve_request_project_id(request)
            body = {**body, "file_path": await ensure_local_file(file_path, project_id)}
        return await build_compat_dataset_preview_payload(get_dataset_manager(), body)

    @app.get("/svcdataset")
    async def svc_get_dataset(dataset_id: str):
        dataset = await get_dataset_or_404(
            get_dataset_manager(),
            dataset_id,
            include_files=True,
        )
        return dataset.model_dump() if hasattr(dataset, "model_dump") else dataset

    @app.post("/svcupload")
    async def svc_upload_file(request: Request, file: UploadFile = File(...)):
        from app.api.routes.datasets import upload_file as _upload_file

        result = await _upload_file(request, file)
        return result.model_dump() if hasattr(result, "model_dump") else result

    @app.get("/svcverifysnapshot")
    async def svc_verify_snapshot(dataset_id: str, file_path: str):
        from app.api.routes.datasets import verify_snapshot as _verify_snapshot

        return await _verify_snapshot(dataset_id=dataset_id, file_path=file_path)
