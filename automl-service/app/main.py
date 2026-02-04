"""FastAPI application factory and configuration."""

import logging
import os
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, Body, WebSocket, WebSocketDisconnect, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.core.websocket_manager import get_websocket_manager
from app.db.database import create_tables
from app.api.routes import health, jobs, datasets, models, predictions, profiling, registry, export, deployments

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown events."""
    settings = get_settings()

    # Startup
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")

    # Create database tables
    await create_tables()
    logger.info("Database tables created")

    # Create required directories
    os.makedirs(settings.models_path, exist_ok=True)
    os.makedirs(settings.temp_path, exist_ok=True)
    os.makedirs(settings.datasets_path, exist_ok=True)
    os.makedirs(settings.uploads_path, exist_ok=True)  # Persistent uploads directory
    os.makedirs(os.path.join(settings.datasets_path, "uploads"), exist_ok=True)
    logger.info(f"Required directories created (uploads: {settings.uploads_path})")

    yield

    # Shutdown
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

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers - use /svc/ prefix to avoid Domino's /api/ interception
    app.include_router(health.router, prefix="/svc/v1/health", tags=["Health"])
    app.include_router(jobs.router, prefix="/svc/v1/jobs", tags=["Jobs"])
    app.include_router(datasets.router, prefix="/svc/v1/datasets", tags=["Datasets"])
    app.include_router(models.router, prefix="/svc/v1/models", tags=["Models"])
    app.include_router(predictions.router, prefix="/svc/v1/predictions", tags=["Predictions"])
    app.include_router(profiling.router, prefix="/svc/v1/profiling", tags=["Profiling"])
    app.include_router(registry.router, prefix="/svc/v1/registry", tags=["Registry"])
    app.include_router(export.router, prefix="/svc/v1/export", tags=["Export"])
    app.include_router(deployments.router, prefix="/svc/v1/deployments", tags=["Deployments"])

    # Single-segment endpoints for Domino compatibility (nginx doesn't intercept these)
    # Health and User Context
    @app.get("/svchealth")
    async def svc_health():
        return await health.health_check()

    @app.get("/svcuser")
    async def svc_user(request: Request):
        """Get current user and project context from Domino headers/environment."""
        return await health.get_current_user(request)

    # Jobs
    @app.get("/svcjobs")
    async def svc_jobs_list_get(request: Request):
        """List jobs for current user and project (from Domino headers/env)."""
        from app.api.routes.jobs import list_jobs_post, JobListRequest
        from app.dependencies import get_db_session
        list_request = JobListRequest()
        async with get_db_session() as db:
            return await list_jobs_post(list_request, db, request)

    @app.post("/svcjobs")
    async def svc_jobs_list(request: Request, body: dict = Body(default={})):
        """List jobs with optional filtering.

        By default, shows jobs for the current user and project.
        Pass owner="" to see all users' jobs.
        Pass project_id="" to see jobs from all projects.
        Pass a specific project_id to filter by that project.
        """
        from app.api.routes.jobs import list_jobs_post, JobListRequest
        from app.dependencies import get_db_session
        list_request = JobListRequest(**body)
        async with get_db_session() as db:
            return await list_jobs_post(list_request, db, request)

    @app.post("/svcjobcreate")
    async def svc_job_create(request: Request, background_tasks: BackgroundTasks, body: dict = Body(default={})):
        """Create a new training job.

        The job is automatically associated with the current user (from domino-username header)
        and the current project (from DOMINO_PROJECT_ID environment variable).
        """
        from app.api.routes.jobs import create_job, JobCreateRequest
        from app.dependencies import get_db_session
        job_data = JobCreateRequest(**body)
        async with get_db_session() as db:
            return await create_job(job_data, background_tasks, db, request)

    @app.post("/svcjobget")
    async def svc_job_get(body: dict = Body(default={})):
        from app.api.routes.jobs import get_job
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await get_job(body.get("job_id"), db)

    @app.post("/svcjobcancel")
    async def svc_job_cancel(body: dict = Body(default={})):
        from app.api.routes.jobs import cancel_job
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await cancel_job(body.get("job_id"), db)

    @app.post("/svcjobdelete")
    async def svc_job_delete(body: dict = Body(default={})):
        from app.api.routes.jobs import delete_job
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await delete_job(body.get("job_id"), db)

    @app.post("/svcjobstatus")
    async def svc_job_status(body: dict = Body(default={})):
        from app.api.routes.jobs import get_job_status
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await get_job_status(body.get("job_id"), db)

    @app.post("/svcjobmetrics")
    async def svc_job_metrics(body: dict = Body(default={})):
        from app.api.routes.jobs import get_job_metrics
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await get_job_metrics(body.get("job_id"), db)

    @app.post("/svcjoblogs")
    async def svc_job_logs(body: dict = Body(default={})):
        from app.api.routes.jobs import get_job_logs
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await get_job_logs(body.get("job_id"), body.get("limit", 100), db)

    @app.post("/svcjobprogress")
    async def svc_job_progress(body: dict = Body(default={})):
        from app.api.routes.jobs import get_job_progress
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await get_job_progress(body.get("job_id"), db)

    @app.post("/svcjobregister")
    async def svc_job_register(body: dict = Body(default={})):
        from app.api.routes.jobs import register_job_model, RegisterModelRequest
        from app.dependencies import get_db_session
        request = RegisterModelRequest(**body)
        async with get_db_session() as db:
            return await register_job_model(body.get("job_id"), request, db)

    # Datasets
    @app.get("/svcdatasets")
    async def svc_list_datasets():
        from app.api.routes.datasets import list_datasets, get_dataset_manager
        manager = get_dataset_manager()
        return await list_datasets(manager)

    @app.post("/svcdatasetpreview")
    async def svc_dataset_preview(body: dict = Body(default={})):
        """Preview an uploaded file or Domino dataset."""
        import pandas as pd
        import os

        file_path = body.get("file_path")
        dataset_id = body.get("dataset_id")
        rows = body.get("rows", 100)

        # Handle uploaded file preview (file_path provided)
        if file_path:
            if not os.path.exists(file_path):
                raise HTTPException(status_code=404, detail=f"File not found: {file_path}")

            try:
                # Read file based on extension
                ext = os.path.splitext(file_path)[1].lower()
                if ext == ".csv":
                    df = pd.read_csv(file_path, nrows=rows)
                elif ext in [".parquet", ".pq"]:
                    df = pd.read_parquet(file_path)
                    df = df.head(rows)
                else:
                    raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

                # Build response matching DatasetPreview interface
                columns = list(df.columns)
                dtypes = {col: str(df[col].dtype) for col in df.columns}

                return {
                    "file_path": file_path,
                    "columns": columns,
                    "rows": df.to_dict(orient="records"),
                    "total_rows": len(df),
                    "dtypes": dtypes,
                }
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to preview file: {str(e)}")

        # Handle Domino dataset preview (dataset_id provided)
        elif dataset_id:
            from app.api.routes.datasets import get_dataset_manager
            manager = get_dataset_manager()
            return await manager.preview_dataset(dataset_id, rows=rows)

        else:
            raise HTTPException(status_code=400, detail="Either file_path or dataset_id is required")

    @app.post("/svcupload")
    async def svc_upload_file(file: UploadFile = File(...)):
        """Upload a file for training - using persistent storage."""
        import uuid
        import shutil
        import pandas as pd

        logger.info(f"[UPLOAD] Received file upload: {file.filename}")

        # Validate file type
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")

        allowed_extensions = [".csv", ".parquet", ".pq"]
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"File type not supported. Allowed: {allowed_extensions}",
            )

        # CRITICAL: Use persistent path - NOT /tmp/automl
        upload_dir = "/mnt/automl-service/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        logger.info(f"[UPLOAD] Using upload directory: {upload_dir}")

        # Add unique prefix to avoid filename collisions
        unique_id = str(uuid.uuid4())[:8]
        safe_filename = f"{unique_id}_{file.filename}"
        file_path = os.path.join(upload_dir, safe_filename)
        logger.info(f"[UPLOAD] Saving file to: {file_path}")

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            logger.info(f"[UPLOAD] File saved successfully: {file_path}")
        except Exception as e:
            logger.error(f"[UPLOAD] Failed to save file: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

        # Read file to get metadata
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file_path, nrows=0)
                row_count = sum(1 for _ in open(file_path)) - 1  # Subtract header
            else:
                df = pd.read_parquet(file_path)
                row_count = len(df)

            columns = list(df.columns)
            file_size = os.path.getsize(file_path)

        except Exception as e:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail=f"Failed to read file: {str(e)}")

        result = {
            "success": True,
            "file_path": file_path,
            "file_name": file.filename,
            "file_size": file_size,
            "columns": columns,
            "row_count": row_count,
        }
        logger.info(f"[UPLOAD] Returning result with file_path: {file_path}")
        return result

    # Predictions
    @app.post("/svcpredict")
    async def svc_predict(body: dict = Body(default={})):
        from app.api.routes.predictions import predict, PredictRequest
        request = PredictRequest(**body)
        return await predict(request)

    @app.post("/svcpredictbatch")
    async def svc_predict_batch(body: dict = Body(default={})):
        from app.api.routes.predictions import batch_predict, BatchPredictRequest
        request = BatchPredictRequest(**body)
        return await batch_predict(request)

    @app.post("/svcmodelinfo")
    async def svc_model_info(body: dict = Body(default={})):
        from app.api.routes.predictions import get_model_info
        return await get_model_info(body.get("model_id"), body.get("model_type"))

    @app.post("/svcfeatureimportance")
    async def svc_feature_importance(body: dict = Body(default={})):
        from app.api.routes.predictions import get_feature_importance, FeatureImportanceRequest
        from app.dependencies import get_db_session
        request = FeatureImportanceRequest(**body)
        async with get_db_session() as db:
            return await get_feature_importance(request, db)

    @app.post("/svcleaderboard")
    async def svc_leaderboard(body: dict = Body(default={})):
        from app.api.routes.predictions import get_leaderboard, LeaderboardRequest
        from app.dependencies import get_db_session
        request = LeaderboardRequest(**body)
        async with get_db_session() as db:
            return await get_leaderboard(request, db)

    @app.post("/svcconfusionmatrix")
    async def svc_confusion_matrix(body: dict = Body(default={})):
        from app.api.routes.predictions import get_confusion_matrix, DiagnosticsRequest
        from app.dependencies import get_db_session
        request = DiagnosticsRequest(**body)
        async with get_db_session() as db:
            return await get_confusion_matrix(request, db)

    @app.post("/svcroccurve")
    async def svc_roc_curve(body: dict = Body(default={})):
        from app.api.routes.predictions import get_roc_curve, DiagnosticsRequest
        from app.dependencies import get_db_session
        request = DiagnosticsRequest(**body)
        async with get_db_session() as db:
            return await get_roc_curve(request, db)

    @app.post("/svcprecisionrecall")
    async def svc_precision_recall(body: dict = Body(default={})):
        from app.api.routes.predictions import get_precision_recall_curve, DiagnosticsRequest
        from app.dependencies import get_db_session
        request = DiagnosticsRequest(**body)
        async with get_db_session() as db:
            return await get_precision_recall_curve(request, db)

    @app.post("/svcregressiondiagnostics")
    async def svc_regression_diagnostics(body: dict = Body(default={})):
        from app.api.routes.predictions import get_regression_diagnostics, DiagnosticsRequest
        from app.dependencies import get_db_session
        request = DiagnosticsRequest(**body)
        async with get_db_session() as db:
            return await get_regression_diagnostics(request, db)

    @app.post("/svcunloadmodel")
    async def svc_unload_model(body: dict = Body(default={})):
        from app.api.routes.predictions import unload_model
        return await unload_model(body.get("model_id"))

    @app.get("/svcloadedmodels")
    async def svc_loaded_models():
        from app.api.routes.predictions import get_loaded_models
        return await get_loaded_models()

    # Profiling
    @app.post("/svcprofile")
    async def svc_profile(body: dict = Body(default={})):
        from app.api.routes.profiling import profile_data, ProfileRequest
        request = ProfileRequest(**body)
        return await profile_data(request)

    @app.post("/svcprofilequick")
    async def svc_profile_quick(body: dict = Body(default={})):
        from app.api.routes.profiling import quick_profile
        return await quick_profile(body.get("file_path"))

    @app.post("/svcsuggesttarget")
    async def svc_suggest_target(body: dict = Body(default={})):
        from app.api.routes.profiling import suggest_target_column, ProfileRequest
        request = ProfileRequest(**body)
        return await suggest_target_column(request)

    @app.post("/svcprofilecolumn")
    async def svc_profile_column(body: dict = Body(default={})):
        from app.api.routes.profiling import profile_column
        return await profile_column(body.get("file_path"), body.get("column_name"))

    @app.get("/svcmetrics")
    async def svc_metrics():
        from app.api.routes.profiling import get_available_metrics
        return await get_available_metrics()

    @app.get("/svcpresets")
    async def svc_presets():
        from app.api.routes.profiling import get_available_presets
        return await get_available_presets()

    # Registry
    @app.post("/svcregistermodel")
    async def svc_register_model(body: dict = Body(default={})):
        from app.api.routes.registry import register_model, RegisterModelRequest
        request = RegisterModelRequest(**body)
        return await register_model(request)

    @app.get("/svcregisteredmodels")
    async def svc_registered_models():
        from app.api.routes.registry import list_registered_models
        return await list_registered_models()

    @app.post("/svcmodelversions")
    async def svc_model_versions(body: dict = Body(default={})):
        from app.api.routes.registry import get_model_versions
        return await get_model_versions(body.get("model_name"))

    @app.post("/svctransitionstage")
    async def svc_transition_stage(body: dict = Body(default={})):
        from app.api.routes.registry import transition_model_stage, TransitionStageRequest
        request = TransitionStageRequest(**body)
        return await transition_model_stage(request)

    @app.post("/svcupdatedescription")
    async def svc_update_description(body: dict = Body(default={})):
        from app.api.routes.registry import update_model_description, UpdateDescriptionRequest
        request = UpdateDescriptionRequest(**body)
        return await update_model_description(request)

    @app.post("/svcdeleteversion")
    async def svc_delete_version(body: dict = Body(default={})):
        from app.api.routes.registry import delete_model_version
        return await delete_model_version(body.get("model_name"), body.get("version"))

    @app.post("/svcdeletemodel")
    async def svc_delete_model(body: dict = Body(default={})):
        from app.api.routes.registry import delete_registered_model
        return await delete_registered_model(body.get("model_name"))

    @app.post("/svcmodelcard")
    async def svc_model_card(body: dict = Body(default={})):
        from app.api.routes.registry import generate_model_card, ModelCardRequest
        request = ModelCardRequest(**body)
        return await generate_model_card(request)

    @app.post("/svcdownloadmodel")
    async def svc_download_model(body: dict = Body(default={})):
        from app.api.routes.registry import download_model
        return await download_model(body.get("model_name"), body.get("version"))

    # Export
    @app.post("/svcexportonnx")
    async def svc_export_onnx(body: dict = Body(default={})):
        from app.api.routes.export import export_to_onnx, ExportONNXRequest
        from app.dependencies import get_db_session
        request = ExportONNXRequest(**body)
        async with get_db_session() as db:
            return await export_to_onnx(request, db)

    @app.post("/svcexportdeployment")
    async def svc_export_deployment(body: dict = Body(default={})):
        from app.api.routes.export import export_deployment_package, DeploymentPackageRequest
        from app.dependencies import get_db_session
        request = DeploymentPackageRequest(**body)
        async with get_db_session() as db:
            return await export_deployment_package(request, db)

    @app.post("/svclearningcurves")
    async def svc_learning_curves(body: dict = Body(default={})):
        from app.api.routes.export import get_learning_curves, LearningCurvesRequest
        from app.dependencies import get_db_session
        request = LearningCurvesRequest(**body)
        async with get_db_session() as db:
            return await get_learning_curves(request, db)

    @app.post("/svccomparemodels")
    async def svc_compare_models(body: dict = Body(default={})):
        from app.api.routes.export import compare_models, ModelComparisonRequest
        request = ModelComparisonRequest(**body)
        return await compare_models(request)

    @app.get("/svcexportformats")
    async def svc_export_formats():
        from app.api.routes.export import get_supported_formats
        return await get_supported_formats()

    @app.post("/svcexportnotebook")
    async def svc_export_notebook(body: dict = Body(default={})):
        from app.api.routes.export import export_notebook, ExportNotebookRequest
        from app.dependencies import get_db_session
        request = ExportNotebookRequest(**body)
        async with get_db_session() as db:
            return await export_notebook(request, db)

    # Models
    @app.get("/svcmodels")
    async def svc_list_models():
        from app.api.routes.models import list_models
        from app.dependencies import get_db_session
        async with get_db_session() as db:
            return await list_models(db)

    # Deployments
    @app.get("/svcdeployments")
    async def svc_list_deployments():
        """List all Model Deployments - directly calls Domino API."""
        logger.info("[DEPLOYMENTS] GET /svcdeployments called")
        try:
            from app.core.domino_model_api import get_domino_model_api
            api = get_domino_model_api()
            logger.info("[DEPLOYMENTS] Calling list_deployments...")
            result = await api.list_deployments()
            logger.info(f"[DEPLOYMENTS] Result: {result}")
            # Ensure we always return valid JSON
            if not isinstance(result, dict):
                logger.warning("[DEPLOYMENTS] Result is not a dict")
                return {"success": True, "data": [], "error": "Invalid response from Domino API"}
            return result
        except Exception as e:
            import traceback
            logger.error(f"[DEPLOYMENTS] Error: {e}\n{traceback.format_exc()}")
            return {"success": True, "data": [], "error": str(e)}

    @app.post("/svcdeploymentcreate")
    async def svc_create_deployment(body: dict = Body(default={})):
        from app.api.routes.deployments import create_deployment, CreateDeploymentRequest
        request = CreateDeploymentRequest(**body)
        return await create_deployment(request)

    @app.post("/svcdeploymentget")
    async def svc_get_deployment(body: dict = Body(default={})):
        from app.api.routes.deployments import get_deployment
        return await get_deployment(body.get("deployment_id"))

    @app.post("/svcdeploymentstart")
    async def svc_start_deployment(body: dict = Body(default={})):
        from app.api.routes.deployments import start_deployment
        return await start_deployment(body.get("deployment_id"))

    @app.post("/svcdeploymentstop")
    async def svc_stop_deployment(body: dict = Body(default={})):
        from app.api.routes.deployments import stop_deployment
        return await stop_deployment(body.get("deployment_id"))

    @app.post("/svcdeploymentdelete")
    async def svc_delete_deployment(body: dict = Body(default={})):
        from app.api.routes.deployments import delete_deployment
        return await delete_deployment(body.get("deployment_id"))

    @app.post("/svcdeploymentstatus")
    async def svc_deployment_status(body: dict = Body(default={})):
        from app.api.routes.deployments import get_deployment_status
        return await get_deployment_status(body.get("deployment_id"))

    @app.post("/svcdeploymentlogs")
    async def svc_deployment_logs(body: dict = Body(default={})):
        from app.api.routes.deployments import get_deployment_logs
        return await get_deployment_logs(
            body.get("deployment_id"),
            body.get("log_type", "stdout")
        )

    @app.post("/svcquickdeploy")
    async def svc_quick_deploy(body: dict = Body(default={})):
        from app.api.routes.deployments import quick_deploy, QuickDeployRequest
        request = QuickDeployRequest(**body)
        return await quick_deploy(request)

    @app.post("/svcdeployfromjob")
    async def svc_deploy_from_job(body: dict = Body(default={})):
        from app.api.routes.deployments import deploy_from_job
        return await deploy_from_job(
            job_id=body.get("job_id"),
            model_name=body.get("model_name"),
            function_name=body.get("function_name", "predict"),
            min_replicas=body.get("min_replicas", 1),
            max_replicas=body.get("max_replicas", 1),
        )

    @app.get("/svcmodelapis")
    async def svc_list_model_apis():
        """List all Model APIs - directly calls Domino API."""
        try:
            from app.core.domino_model_api import get_domino_model_api
            api = get_domino_model_api()
            result = await api.list_model_apis()
            # Ensure we always return valid JSON
            if not isinstance(result, dict):
                return {"success": True, "data": [], "error": "Invalid response from Domino API"}
            return result
        except Exception as e:
            import traceback
            logger.error(f"Error listing model APIs: {e}\n{traceback.format_exc()}")
            return {"success": True, "data": [], "error": str(e)}

    @app.post("/svcmodelapicreate")
    async def svc_create_model_api(body: dict = Body(default={})):
        from app.api.routes.deployments import create_model_api, CreateModelApiRequest
        request = CreateModelApiRequest(**body)
        return await create_model_api(request)

    # WebSocket endpoint for real-time job progress
    @app.websocket("/ws/jobs/{job_id}")
    async def websocket_job_progress(websocket: WebSocket, job_id: str):
        """WebSocket endpoint for real-time job progress updates."""
        manager = get_websocket_manager()
        await manager.connect(websocket, job_id)
        try:
            # Send initial status
            from app.dependencies import get_db_session
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
                        "type": "error",
                        "job_id": job_id,
                        "message": str(e)
                    })

            # Keep connection alive and receive any client messages
            while True:
                try:
                    data = await websocket.receive_text()
                    # Handle ping/pong for connection keep-alive
                    if data == "ping":
                        await websocket.send_text("pong")
                except WebSocketDisconnect:
                    break
                except Exception:
                    break
        finally:
            await manager.disconnect(websocket, job_id)

    # Debug endpoint to test routing
    @app.get("/svcping")
    async def svc_ping():
        """Simple ping endpoint to verify routing works."""
        return {"success": True, "message": "pong", "timestamp": datetime.now().isoformat()}

    # Root route - returns jobs filtered by owner (always) and project_name (if provided)
    @app.get("/")
    async def root(request: Request, project_name: Optional[str] = None):
        """Main endpoint returning jobs for the current user.

        Jobs are ALWAYS filtered by the current user (from domino-username header).
        If project_name is provided as a query parameter, jobs are also filtered by that project.

        Query Parameters:
            project_name: Optional project name to filter jobs by

        Examples:
            GET /                          -> All jobs for current user (across all projects)
            GET /?project_name=my-project  -> Jobs for current user in 'my-project' only
        """
        from app.api.routes.jobs import JobListRequest, list_jobs_post
        from app.dependencies import get_db_session

        # Get user from Domino header (ALWAYS filter by this)
        # This is the ACCESSING user, not the app deployer
        username = request.headers.get("domino-username", "anonymous")

        # Build list request - always filter by owner, optionally by project_name
        list_request = JobListRequest(
            owner=username,  # Always filter by current user
            project_name=project_name if project_name else "",  # "" = all projects, specific value = filter
            limit=100,
        )

        async with get_db_session() as db:
            jobs_response = await list_jobs_post(list_request, db, request)

        # Get current project context for info
        current_project_name = settings.domino_project_name or os.environ.get("DOMINO_PROJECT_NAME")

        return {
            "service": settings.app_name,
            "version": settings.app_version,
            "status": "running",
            "user": username,
            "current_project_name": current_project_name,
            "filter": {
                "owner": username,
                "project_name": project_name,  # None means all projects
            },
            "jobs": jobs_response.jobs,
            "total_jobs": jobs_response.total,
        }

    return app


# Create application instance
app = create_app()
