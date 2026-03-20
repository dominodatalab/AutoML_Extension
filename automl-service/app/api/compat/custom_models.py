"""Custom compatibility model and deployment routes."""

from fastapi import Body, FastAPI, Request

from app.dependencies import get_db_session
from app.services.deployment_service import (
    deploy_from_job as deploy_from_job_service,
    list_deployments_safe,
    list_model_apis_safe,
)
from app.services.model_service import list_registered_models_response


def register_custom_model_routes(app: FastAPI) -> None:
    """Register custom /svc* model and deployment routes."""

    @app.get("/svcmodels")
    async def svc_list_models(request: Request):
        project_id = request.headers.get("X-Project-Id")
        owner = request.headers.get("domino-username")
        async with get_db_session() as db:
            return await list_registered_models_response(db, project_id=project_id, owner=owner)

    @app.get("/svcdeployments")
    async def svc_list_deployments():
        return await list_deployments_safe()

    @app.get("/svcmodelapis")
    async def svc_list_model_apis():
        return await list_model_apis_safe()

    @app.post("/svcdeployfromjob")
    async def svc_deploy_from_job(request: Request, body: dict = Body(default={})):
        project_id = request.headers.get("X-Project-Id") or body.get("project_id")
        return await deploy_from_job_service(
            job_id=body.get("job_id"),
            model_name=body.get("model_name"),
            function_name=body.get("function_name", "predict"),
            min_replicas=body.get("min_replicas", 1),
            max_replicas=body.get("max_replicas", 1),
            project_id=project_id,
        )
