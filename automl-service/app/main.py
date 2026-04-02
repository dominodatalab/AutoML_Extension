"""FastAPI application factory and configuration."""

import logging
import os
from contextlib import asynccontextmanager
import re
from typing import Optional

from fastapi import FastAPI, Query, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import get_settings
from app.core.websocket_manager import get_websocket_manager
from app.db.database import create_tables
from app.api.routes import health, jobs, datasets, predictions, profiling, registry, export, deployments
from app.core.context.auth import set_request_auth_header

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL") or logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def is_auth_header(header_key) -> bool:
    return re.search(r'(cookie|api|key|auth)', header_key, flags=re.I) is not None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown events."""
    settings = get_settings()

    logger.info(f"Starting {settings.app_name} v{settings.app_version}")

    await create_tables()
    logger.info("Database tables created")

    os.makedirs(settings.models_path, exist_ok=True)
    os.makedirs(settings.temp_path, exist_ok=True)
    os.makedirs(settings.datasets_path, exist_ok=True)
    os.makedirs(settings.uploads_path, exist_ok=True)
    os.makedirs(settings.eda_results_path, exist_ok=True)
    os.makedirs(os.path.join(settings.datasets_path, "uploads"), exist_ok=True)
    logger.info(f"Required directories created (uploads: {settings.uploads_path})")

    yield

    logger.info("Shutting down application")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="AutoML service powered by AutoGluon with Domino Data Lab integration",
        lifespan=lifespan,
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request context capture: store the forwarded auth header in a request-scoped ContextVar.
    @app.middleware("http")
    async def capture_request_context(request: Request, call_next):
        headers = request.headers
        redacted_headers = [(key, "<REDACTED>") for key, val in headers.items() if is_auth_header(key)]
        safe_headers = [(key, val) for key, val in headers.items() if not is_auth_header(key)]

        logger.debug(f"Capture request metadata: {request.method} {request.url.path} {redacted_headers + safe_headers}")

        auth_header = request.headers.get("authorization")
        set_request_auth_header(auth_header)
        try:
            response = await call_next(request)
        finally:
            set_request_auth_header(None)
        return response

    # Exception handlers
    @app.exception_handler(FileNotFoundError)
    async def file_not_found_handler(request: Request, exc: FileNotFoundError):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        return JSONResponse(status_code=400, content={"detail": str(exc)})

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception on {request.url}: {exc}", exc_info=True)
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})

    # RESTful routers
    app.include_router(health.router, prefix="/svc/v1/health", tags=["Health"])
    app.include_router(jobs.router, prefix="/svc/v1/jobs", tags=["Jobs"])
    app.include_router(datasets.router, prefix="/svc/v1/datasets", tags=["Datasets"])
    app.include_router(predictions.router, prefix="/svc/v1/predictions", tags=["Predictions"])
    app.include_router(profiling.router, prefix="/svc/v1/profiling", tags=["Profiling"])
    app.include_router(registry.router, prefix="/svc/v1/registry", tags=["Registry"])
    app.include_router(export.router, prefix="/svc/v1/export", tags=["Export"])
    app.include_router(deployments.router, prefix="/svc/v1/deployments", tags=["Deployments"])

    # Optional static file serving for combined frontend+backend mode
    static_dir = os.environ.get("STATIC_DIR")
    if static_dir and os.path.isdir(static_dir):
        from fastapi.staticfiles import StaticFiles
        from fastapi.responses import FileResponse

        assets_dir = os.path.join(static_dir, "assets")
        if os.path.isdir(assets_dir):
            app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

        config_js = os.path.join(static_dir, "config.js")

        @app.get("/config.js")
        async def serve_config():
            return FileResponse(config_js)

        @app.get("/{path:path}")
        async def serve_spa(path: str):
            if path.startswith(("svc", "api", "ws")):
                return JSONResponse(status_code=404, content={"detail": "Not found"})
            file_path = os.path.join(static_dir, path)
            if os.path.isfile(file_path):
                real_path = os.path.realpath(file_path)
                if real_path.startswith(os.path.realpath(static_dir)):
                    return FileResponse(real_path)
            return FileResponse(os.path.join(static_dir, "index.html"))

    # WebSocket for real-time job progress
    @app.websocket("/ws/jobs/{job_id}")
    async def websocket_job_progress(websocket: WebSocket, job_id: str):
        manager = get_websocket_manager()
        await manager.connect(websocket, job_id)
        try:
            async with get_db_session() as db:
                from app.api.routes.jobs import get_job_progress
                try:
                    progress = await get_job_progress(job_id, db)
                    await websocket.send_json({
                        "type": "initial",
                        "job_id": job_id,
                        **(progress.dict() if hasattr(progress, 'dict') else progress)
                    })
                except Exception as e:
                    await websocket.send_json({
                        "type": "error", "job_id": job_id, "message": str(e)
                    })

            while True:
                try:
                    data = await websocket.receive_text()
                    if data == "ping":
                        await websocket.send_text("pong")
                except WebSocketDisconnect:
                    break
                except Exception:
                    break
        finally:
            await manager.disconnect(websocket, job_id)

    # Need to import get_db_session here for WebSocket and root endpoints
    from app.dependencies import get_db_session

    # Root endpoint
    @app.get("/")
    async def root(
        request: Request,
        projectId: Optional[str] = Query(None),
        project_name: Optional[str] = Query(None),
    ):
        from app.api.schemas.job import JobListRequest, JobResponse
        from app.services.job_service import list_jobs_filtered

        username = request.headers.get("domino-username", "anonymous")

        jobs_list = []
        if projectId:
            list_request = JobListRequest(
                owner=username,
                project_id=projectId,
                project_name=project_name or None,
                limit=100,
            )
            async with get_db_session() as db:
                jobs = await list_jobs_filtered(db=db, list_request=list_request)
            jobs_list = [JobResponse.model_validate(j) for j in jobs]

        return {
            "service": settings.app_name,
            "version": settings.app_version,
            "status": "running",
            "user": username,
            "filter": {"owner": username, "project_name": project_name, "project_id": projectId},
            "jobs": jobs_list,
            "total_jobs": len(jobs_list),
        }

    return app


app = create_app()
