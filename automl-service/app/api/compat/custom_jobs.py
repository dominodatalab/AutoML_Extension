"""Custom compatibility job routes."""

from fastapi import Body, Depends, FastAPI

from app.api.schemas.job import (
    JobCreateRequest,
    JobListRequest,
    JobListResponse,
    JobResponse,
    RegisterModelRequest,
)
from app.dependencies import get_db_session, get_project_context, get_request_project_id
from app.services.job_service import (
    create_job_with_context,
    find_orphans_checked,
    delete_orphans as delete_orphans_service,
    list_jobs_filtered,
    preview_cleanup as preview_cleanup_service,
    register_model_for_job,
)


async def _list_jobs_response(
    list_request: JobListRequest,
) -> JobListResponse:
    """Build list-jobs response for compat endpoints."""
    async with get_db_session() as db:
        jobs = await list_jobs_filtered(db=db, list_request=list_request)
    return JobListResponse(
        jobs=[JobResponse.model_validate(j) for j in jobs],
        total=len(jobs),
        skip=list_request.skip,
        limit=list_request.limit,
    )


def register_custom_job_routes(app: FastAPI) -> None:
    """Register custom /svc* job routes."""

    @app.get("/svcjobs")
    async def svc_jobs_get(project_id: str = Depends(get_request_project_id)):
        return await _list_jobs_response(list_request=JobListRequest(project_id=project_id))

    @app.post("/svcjobs")
    async def svc_jobs_post(body: dict = Body(default={})):
        return await _list_jobs_response(
            list_request=JobListRequest(**body),
        )

    @app.post("/svcjobcreate")
    async def svc_job_create(
        body: dict = Body(default={}),
        project_context: tuple = Depends(get_project_context),
    ):
        project_id, project_name, project_owner = project_context
        async with get_db_session() as db:
            job = await create_job_with_context(
                db=db,
                job_request=JobCreateRequest(**body),
                project_id=project_id,
                project_name=project_name,
                project_owner=project_owner,
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
    async def svc_job_cleanup_preview(
        body: dict = Body(default={}),
        project_id: str = Depends(get_request_project_id),
    ):
        async with get_db_session() as db:
            return await preview_cleanup_service(
                db=db,
                statuses=body.get("statuses", "failed,cancelled"),
                older_than_days=body.get("older_than_days"),
                project_id=project_id,
            )

    @app.post("/svcjoborphans")
    async def svc_job_orphans(project_id: str = Depends(get_request_project_id)):
        """Preview orphaned artifacts (no deletion)."""
        async with get_db_session() as db:
            return await find_orphans_checked(db, project_id=project_id)

    @app.post("/svcjobcleanuporphans")
    async def svc_job_cleanup_orphans(project_id: str = Depends(get_request_project_id)):
        async with get_db_session() as db:
            return await delete_orphans_service(db=db, project_id=project_id)
