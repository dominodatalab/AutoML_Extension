"""Custom compatibility job routes."""

from fastapi import Body, FastAPI, Request

from app.api.schemas.job import (
    JobCreateRequest,
    JobListRequest,
    JobListResponse,
    JobResponse,
    RegisterModelRequest,
)
from app.dependencies import get_db_session
from app.services.job_service import (
    get_request_project_id,
    create_job_with_context,
    find_orphans_checked,
    delete_orphans as delete_orphans_service,
    list_jobs_filtered,
    preview_cleanup as preview_cleanup_service,
    register_model_for_job,
)


async def _list_jobs_response(
    request: Request,
    list_request: JobListRequest,
) -> JobListResponse:
    """Build list-jobs response for compat endpoints."""
    async with get_db_session() as db:
        jobs = await list_jobs_filtered(db=db, list_request=list_request, request=request)
    return JobListResponse(
        jobs=[JobResponse.model_validate(j) for j in jobs],
        total=len(jobs),
        skip=list_request.skip,
        limit=list_request.limit,
    )


def register_custom_job_routes(app: FastAPI) -> None:
    """Register custom /svc* job routes."""

    @app.get("/svcjobs")
    async def svc_jobs_get(request: Request):
        return await _list_jobs_response(request=request, list_request=JobListRequest())

    @app.post("/svcjobs")
    async def svc_jobs_post(request: Request, body: dict = Body(default={})):
        return await _list_jobs_response(
            request=request,
            list_request=JobListRequest(**body),
        )

    @app.post("/svcjobcreate")
    async def svc_job_create(
        request: Request,
        body: dict = Body(default={}),
    ):
        async with get_db_session() as db:
            job = await create_job_with_context(
                db=db,
                job_request=JobCreateRequest(**body),
                request=request,
            )
        return JobResponse.model_validate(job)

    @app.post("/svcjobregister")
    async def svc_job_register(body: dict = Body(default={})):
        register_request = RegisterModelRequest(**body)
        async with get_db_session() as db:
            return await register_model_for_job(
                db=db,
                job_id=register_request.job_id,
                request=register_request,
            )

    @app.post("/svcjobcleanuppreview")
    async def svc_job_cleanup_preview(request: Request, body: dict = Body(default={})):
        project_id = get_request_project_id(request)
        async with get_db_session() as db:
            return await preview_cleanup_service(
                db=db,
                statuses=body.get("statuses", "failed,cancelled"),
                older_than_days=body.get("older_than_days"),
                project_id=project_id,
            )

    @app.post("/svcjoborphans")
    async def svc_job_orphans(request: Request):
        """Preview orphaned artifacts (no deletion)."""
        project_id = get_request_project_id(request)
        async with get_db_session() as db:
            return await find_orphans_checked(db, project_id=project_id)

    @app.post("/svcjobcleanuporphans")
    async def svc_job_cleanup_orphans(request: Request):
        project_id = get_request_project_id(request)
        async with get_db_session() as db:
            return await delete_orphans_service(db=db, project_id=project_id)
