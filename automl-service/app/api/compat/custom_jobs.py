"""Custom compatibility job routes."""

from fastapi import Body, FastAPI, Request

from app.api.schemas.job import (
    JobCreateRequest,
    JobListItemResponse,
    JobListRequest,
    JobListResponse,
    JobResponse,
    RegisterModelRequest,
)
from app.dependencies import get_db_session
from app.api.schemas.job import JobLogResponse
from app.services.job_service import (
    get_request_project_id,
    create_job_with_context,
    find_orphans_checked,
    delete_orphans as delete_orphans_service,
    build_job_list_item_response,
    get_job_logs as get_job_logs_service,
    get_request_owner,
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
        jobs=[JobListItemResponse.model_validate(build_job_list_item_response(j)) for j in jobs],
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
        owner = get_request_owner(request)
        async with get_db_session() as db:
            return await preview_cleanup_service(
                db=db,
                statuses=body.get("statuses", "failed,cancelled"),
                older_than_days=body.get("older_than_days"),
                project_id=project_id,
                owner=owner,
            )

    @app.post("/svcjoborphans")
    async def svc_job_orphans(request: Request):
        """Preview orphaned artifacts (no deletion)."""
        project_id = get_request_project_id(request)
        async with get_db_session() as db:
            return await find_orphans_checked(db, project_id=project_id)

    @app.post("/svcjobcleanup")
    async def svc_job_cleanup(request: Request, body: dict = Body(default={})):
        from app.services.job_service import bulk_cleanup as bulk_cleanup_service, get_request_project_id
        from app.api.schemas.job import CleanupRequest as CleanupReq
        cleanup_req = CleanupReq(**body)
        project_id = get_request_project_id(request)
        owner = get_request_owner(request)
        async with get_db_session() as db:
            return await bulk_cleanup_service(
                db=db,
                statuses=cleanup_req.statuses,
                older_than_days=cleanup_req.older_than_days,
                include_orphans=cleanup_req.include_orphans,
                project_id=project_id,
                owner=owner,
            )

    @app.post("/svcjoblogs")
    async def svc_job_logs(request: Request, body: dict = Body(default={})):
        job_id = body.get("job_id")
        limit = body.get("limit", 100)
        async with get_db_session() as db:
            logs = await get_job_logs_service(db=db, job_id=job_id, limit=limit, request=request)
        return [JobLogResponse.model_validate(log) for log in logs]

    @app.post("/svcjobcleanuporphans")
    async def svc_job_cleanup_orphans(request: Request):
        project_id = get_request_project_id(request)
        async with get_db_session() as db:
            return await delete_orphans_service(db=db, project_id=project_id)
