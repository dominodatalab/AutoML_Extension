"""FastAPI application factory and configuration."""

import logging
import os
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.compat_routes import register_compat_routes
from app.config import get_settings
from app.core.websocket_manager import get_websocket_manager
from app.db.database import create_tables
from app.api.routes import health, jobs, datasets, predictions, profiling, registry, export, deployments
from app.core.context.auth import set_request_auth_header
from app.core.context.user import clear_viewing_user, resolve_viewing_user

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def _is_truthy(value: Optional[str]) -> bool:
    """Parse common truthy string values from environment variables."""
    if value is None:
        return False
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def validate_local_compute_worker_settings() -> None:
    """Fail fast on unsupported local-queue + multi-worker configuration."""
    local_compute_enabled = _is_truthy(os.environ.get("ENABLE_LOCAL_COMPUTE", "true"))
    if not local_compute_enabled:
        return

    # Uvicorn reload mode runs a single worker process.
    if _is_truthy(os.environ.get("RELOAD", "false")):
        return

    workers_raw = os.environ.get("WORKERS") or os.environ.get("WEB_CONCURRENCY")
    if workers_raw is None:
        return

    try:
        workers = int(workers_raw)
    except ValueError as exc:
        raise RuntimeError(
            f"Invalid worker setting: WORKERS/WEB_CONCURRENCY='{workers_raw}'"
        ) from exc

    if workers > 1:
        raise RuntimeError(
            "Local compute is enabled, but multiple API workers are configured. "
            "Set WORKERS=1 (or WEB_CONCURRENCY=1), or set ENABLE_LOCAL_COMPUTE=false."
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown events."""
    settings = get_settings()
    validate_local_compute_worker_settings()

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

    from app.core.utils import cleanup_dataset_cache
    deleted = cleanup_dataset_cache(os.path.join(settings.temp_path, "dataset_cache"))
    if deleted:
        logger.info("Cleaned up %d stale cached dataset files", deleted)

    from app.dependencies import get_db_session as _get_db_session
    async with _get_db_session() as db:
        from app.db.crud import delete_stale_eda_results
        eda_deleted = await delete_stale_eda_results(db, max_age_hours=72)
        if eda_deleted:
            logger.info("Cleaned up %d stale EDA results", eda_deleted)

    from app.core.job_queue import get_job_queue
    queue = get_job_queue()
    await queue.startup()

    yield

    await queue.shutdown(timeout=30.0)
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

    # Debug request/response logging (AUTOML_DEBUG_LOGGING=true)
    if settings.debug_logging:
        from app.api.middleware import DebugLoggingMiddleware
        app.add_middleware(DebugLoggingMiddleware)
        logging.getLogger("automl.debug").setLevel(logging.DEBUG)
        logger.info("Debug request/response logging ENABLED (AUTOML_DEBUG_LOGGING=true)")

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Only resolve the viewing user (Domino API call) for backend API routes.
    # Static assets, the SPA shell, config.js, health checks etc. skip this
    # to avoid unnecessary sidecar calls on every page load.
    _RESOLVE_USER_PREFIXES = ("/svc/v1/jobs", "/svc/v1/datasets", "/svc/v1/predictions",
                              "/svc/v1/profiling", "/svc/v1/registry", "/svc/v1/export",
                              "/svc/v1/deployments", "/svcjob", "/svcdataset", "/svcprofile",
                              "/svccapabilities", "/svcexport", "/svcpredict", "/svcregistry",
                              "/svcdeployment")

    # Request auth capture: store Authorization header in per-request context
    @app.middleware("http")
    async def capture_auth_header(request: Request, call_next):
        auth_header = request.headers.get("Authorization")
        # Set before handling; ensure cleanup/reset after response
        set_request_auth_header(auth_header)
        # Resolve viewing user only for API routes that need RBAC.
        if any(request.url.path.startswith(p) for p in _RESOLVE_USER_PREFIXES):
            await resolve_viewing_user()
        try:
            response = await call_next(request)
        finally:
            # Clear after request finishes to avoid any cross-request leakage
            set_request_auth_header(None)
            clear_viewing_user()
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

    # Single-segment Domino compat routes (replaces ~550 lines of wrappers)
    register_compat_routes(app)

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
                        **jsonable_encoder(progress)
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
    async def root(request: Request, project_name: Optional[str] = None):
        from app.api.routes.jobs import JobListRequest, list_jobs_post

        username = request.headers.get("domino-username", "anonymous")
        list_request = JobListRequest(
            owner=username,
            project_name=project_name if project_name else "",
            limit=100,
        )

        async with get_db_session() as db:
            jobs_response = await list_jobs_post(list_request, db, request)

        current_project_name = settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")

        return {
            "service": settings.app_name,
            "version": settings.app_version,
            "status": "running",
            "user": username,
            "current_project_name": current_project_name,
            "filter": {"owner": username, "project_name": project_name},
            "jobs": jobs_response.jobs,
            "total_jobs": jobs_response.total,
        }

    return app


app = create_app()
