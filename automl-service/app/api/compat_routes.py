"""Single-segment Domino compatibility routes.

Domino's nginx proxy intercepts multi-segment paths under /api/.
These /svc* endpoints provide single-segment alternatives that bypass interception.

Routes are organized by pattern and registered dynamically to avoid
500+ lines of repetitive endpoint wrappers.
"""

import importlib
import logging
import os
from datetime import datetime

from fastapi import (
    BackgroundTasks,
    Body,
    FastAPI,
    File,
    HTTPException,
    Request,
    UploadFile,
)

from app.dependencies import get_db_session

logger = logging.getLogger(__name__)


def _import(module_path: str, *names: str):
    """Lazy import names from a module."""
    mod = importlib.import_module(module_path)
    if len(names) == 1:
        return getattr(mod, names[0])
    return tuple(getattr(mod, n) for n in names)


def register_compat_routes(app: FastAPI):
    """Register all /svc* single-segment routes for Domino compatibility."""

    # ── Pattern 1: Simple GET → async function() ────────────────────
    simple_gets = {
        "/svchealth": ("app.api.routes.health", "health_check"),
        "/svcloadedmodels": ("app.api.routes.predictions", "get_loaded_models"),
        "/svcmetrics": ("app.api.routes.profiling", "get_available_metrics"),
        "/svcpresets": ("app.api.routes.profiling", "get_available_presets"),
        "/svcregisteredmodels": ("app.api.routes.registry", "list_registered_models"),
        "/svcexportformats": ("app.api.routes.export", "get_supported_formats"),
    }

    for path, (mod, fn) in simple_gets.items():
        def _handler(m=mod, f=fn):
            async def endpoint():
                return await _import(m, f)()
            endpoint.__name__ = f"svc_{f}"
            return endpoint
        app.get(path)(_handler())

    # ── Pattern 2: POST body → RequestClass → func(request) ─────────
    post_request = [
        ("/svcpredict", "app.api.routes.predictions", "predict", "PredictRequest"),
        ("/svcpredictbatch", "app.api.routes.predictions", "batch_predict", "BatchPredictRequest"),
        ("/svcprofile", "app.api.routes.profiling", "profile_data", "ProfileRequest"),
        ("/svcsuggesttarget", "app.api.routes.profiling", "suggest_target_column", "ProfileRequest"),
        ("/svcprofiletimeseries", "app.api.routes.profiling", "profile_timeseries", "TimeSeriesProfileRequest"),
        ("/svcregistermodel", "app.api.routes.registry", "register_model", "RegisterModelRequest"),
        ("/svctransitionstage", "app.api.routes.registry", "transition_model_stage", "TransitionStageRequest"),
        ("/svcupdatedescription", "app.api.routes.registry", "update_model_description", "UpdateDescriptionRequest"),
        ("/svcmodelcard", "app.api.routes.registry", "generate_model_card", "ModelCardRequest"),
        ("/svccomparemodels", "app.api.routes.export", "compare_models", "ModelComparisonRequest"),
        ("/svcdeploymentcreate", "app.api.routes.deployments", "create_deployment", "CreateDeploymentRequest"),
        ("/svcquickdeploy", "app.api.routes.deployments", "quick_deploy", "QuickDeployRequest"),
        ("/svcmodelapicreate", "app.api.routes.deployments", "create_model_api", "CreateModelApiRequest"),
    ]

    for path, mod, fn, cls in post_request:
        def _handler(m=mod, f=fn, c=cls):
            async def endpoint(body: dict = Body(default={})):
                func, req_cls = _import(m, f, c)
                return await func(req_cls(**body))
            endpoint.__name__ = f"svc_{f}"
            return endpoint
        app.post(path)(_handler())

    # ── Pattern 3: POST body.get(keys) → func(*args) ────────────────
    # Each key is (name,) or (name, default)
    post_keys = [
        ("/svcmodelinfo", "app.api.routes.predictions", "get_model_info", [("model_id",), ("model_type",)]),
        ("/svcprofilequick", "app.api.routes.profiling", "quick_profile", [("file_path",)]),
        ("/svcprofilecolumn", "app.api.routes.profiling", "profile_column", [("file_path",), ("column_name",)]),
        ("/svcunloadmodel", "app.api.routes.predictions", "unload_model", [("model_id",)]),
        ("/svcmodelversions", "app.api.routes.registry", "get_model_versions", [("model_name",)]),
        ("/svcdeleteversion", "app.api.routes.registry", "delete_model_version", [("model_name",), ("version",)]),
        ("/svcdeletemodel", "app.api.routes.registry", "delete_registered_model", [("model_name",)]),
        ("/svcdownloadmodel", "app.api.routes.registry", "download_model", [("model_name",), ("version",)]),
        ("/svcdeploymentget", "app.api.routes.deployments", "get_deployment", [("deployment_id",)]),
        ("/svcdeploymentstart", "app.api.routes.deployments", "start_deployment", [("deployment_id",)]),
        ("/svcdeploymentstop", "app.api.routes.deployments", "stop_deployment", [("deployment_id",)]),
        ("/svcdeploymentdelete", "app.api.routes.deployments", "delete_deployment", [("deployment_id",)]),
        ("/svcdeploymentstatus", "app.api.routes.deployments", "get_deployment_status", [("deployment_id",)]),
        ("/svcdeploymentlogs", "app.api.routes.deployments", "get_deployment_logs", [("deployment_id",), ("log_type", "stdout")]),
    ]

    for path, mod, fn, keys in post_keys:
        def _handler(m=mod, f=fn, k=keys):
            async def endpoint(body: dict = Body(default={})):
                func = _import(m, f)
                args = [body.get(*key) for key in k]
                return await func(*args)
            endpoint.__name__ = f"svc_{f}"
            return endpoint
        app.post(path)(_handler())

    # ── Pattern 4: POST body → RequestClass + DB → func(req, db) ────
    post_request_db = [
        ("/svcfeatureimportance", "app.api.routes.predictions", "get_feature_importance", "FeatureImportanceRequest"),
        ("/svcleaderboard", "app.api.routes.predictions", "get_leaderboard", "LeaderboardRequest"),
        ("/svcconfusionmatrix", "app.api.routes.predictions", "get_confusion_matrix", "DiagnosticsRequest"),
        ("/svcroccurve", "app.api.routes.predictions", "get_roc_curve", "DiagnosticsRequest"),
        ("/svcprecisionrecall", "app.api.routes.predictions", "get_precision_recall_curve", "DiagnosticsRequest"),
        ("/svcregressiondiagnostics", "app.api.routes.predictions", "get_regression_diagnostics", "DiagnosticsRequest"),
        ("/svcexportonnx", "app.api.routes.export", "export_to_onnx", "ExportONNXRequest"),
        ("/svcexportdeployment", "app.api.routes.export", "export_deployment_package", "DeploymentPackageRequest"),
        ("/svclearningcurves", "app.api.routes.export", "get_learning_curves", "LearningCurvesRequest"),
        ("/svcexportnotebook", "app.api.routes.export", "export_notebook", "ExportNotebookRequest"),
    ]

    for path, mod, fn, cls in post_request_db:
        def _handler(m=mod, f=fn, c=cls):
            async def endpoint(body: dict = Body(default={})):
                func, req_cls = _import(m, f, c)
                async with get_db_session() as db:
                    return await func(req_cls(**body), db)
            endpoint.__name__ = f"svc_{f}"
            return endpoint
        app.post(path)(_handler())

    # ── Pattern 5: POST body.get(keys) + DB → func(*args, db) ───────
    post_keys_db = [
        ("/svcjobget", "app.api.routes.jobs", "get_job", [("job_id",)]),
        ("/svcjobcancel", "app.api.routes.jobs", "cancel_job", [("job_id",)]),
        ("/svcjobdelete", "app.api.routes.jobs", "delete_job", [("job_id",)]),
        ("/svcjobstatus", "app.api.routes.jobs", "get_job_status", [("job_id",)]),
        ("/svcjobmetrics", "app.api.routes.jobs", "get_job_metrics", [("job_id",)]),
        ("/svcjoblogs", "app.api.routes.jobs", "get_job_logs", [("job_id",), ("limit", 100)]),
        ("/svcjobprogress", "app.api.routes.jobs", "get_job_progress", [("job_id",)]),
    ]

    for path, mod, fn, keys in post_keys_db:
        def _handler(m=mod, f=fn, k=keys):
            async def endpoint(body: dict = Body(default={})):
                func = _import(m, f)
                args = [body.get(*key) for key in k]
                async with get_db_session() as db:
                    return await func(*args, db)
            endpoint.__name__ = f"svc_{f}"
            return endpoint
        app.post(path)(_handler())

    # ── Custom routes (require special handling) ─────────────────────

    @app.get("/svcuser")
    async def svc_user(request: Request):
        return await _import("app.api.routes.health", "get_current_user")(request)

    @app.get("/svcjobs")
    async def svc_jobs_get(request: Request):
        list_jobs_post, JobListRequest = _import(
            "app.api.routes.jobs", "list_jobs_post", "JobListRequest"
        )
        async with get_db_session() as db:
            return await list_jobs_post(JobListRequest(), db, request)

    @app.post("/svcjobs")
    async def svc_jobs_post(request: Request, body: dict = Body(default={})):
        list_jobs_post, JobListRequest = _import(
            "app.api.routes.jobs", "list_jobs_post", "JobListRequest"
        )
        async with get_db_session() as db:
            return await list_jobs_post(JobListRequest(**body), db, request)

    @app.post("/svcjobcreate")
    async def svc_job_create(
        request: Request,
        background_tasks: BackgroundTasks,
        body: dict = Body(default={}),
    ):
        create_job, JobCreateRequest = _import(
            "app.api.routes.jobs", "create_job", "JobCreateRequest"
        )
        async with get_db_session() as db:
            return await create_job(JobCreateRequest(**body), background_tasks, db, request)

    @app.post("/svcjobregister")
    async def svc_job_register(body: dict = Body(default={})):
        register_job_model, RegisterModelRequest = _import(
            "app.api.routes.jobs", "register_job_model", "RegisterModelRequest"
        )
        async with get_db_session() as db:
            return await register_job_model(
                body.get("job_id"), RegisterModelRequest(**body), db
            )

    @app.get("/svcdatasets")
    async def svc_list_datasets():
        list_datasets = _import("app.api.routes.datasets", "list_datasets")
        get_mgr = _import("app.api.routes.datasets", "get_dataset_manager")
        return await list_datasets(get_mgr())

    @app.post("/svcdatasetpreview")
    async def svc_dataset_preview(body: dict = Body(default={})):
        import pandas as pd

        file_path = body.get("file_path")
        dataset_id = body.get("dataset_id")
        rows = body.get("rows", 100)

        if file_path:
            if not os.path.exists(file_path):
                raise HTTPException(status_code=404, detail=f"File not found: {file_path}")
            try:
                ext = os.path.splitext(file_path)[1].lower()
                if ext == ".csv":
                    df = pd.read_csv(file_path, nrows=rows)
                elif ext in [".parquet", ".pq"]:
                    df = pd.read_parquet(file_path)
                    df = df.head(rows)
                else:
                    raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")
                return {
                    "file_path": file_path,
                    "columns": list(df.columns),
                    "rows": df.to_dict(orient="records"),
                    "total_rows": len(df),
                    "dtypes": {col: str(df[col].dtype) for col in df.columns},
                }
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Failed to preview file: {str(e)}")
        elif dataset_id:
            get_mgr = _import("app.api.routes.datasets", "get_dataset_manager")
            return await get_mgr().preview_dataset(dataset_id, rows=rows)
        else:
            raise HTTPException(status_code=400, detail="Either file_path or dataset_id is required")

    @app.post("/svcupload")
    async def svc_upload_file(file: UploadFile = File(...)):
        import shutil
        import uuid

        import pandas as pd

        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")

        allowed_extensions = [".csv", ".parquet", ".pq"]
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in allowed_extensions:
            raise HTTPException(
                status_code=400,
                detail=f"File type not supported. Allowed: {allowed_extensions}",
            )

        from app.config import get_settings
        upload_dir = get_settings().uploads_path
        os.makedirs(upload_dir, exist_ok=True)
        unique_id = str(uuid.uuid4())[:8]
        safe_filename = f"{unique_id}_{file.filename}"
        file_path = os.path.join(upload_dir, safe_filename)

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

        try:
            if file_ext == ".csv":
                df = pd.read_csv(file_path, nrows=0)
                row_count = sum(1 for _ in open(file_path)) - 1
            else:
                df = pd.read_parquet(file_path)
                row_count = len(df)
            columns = list(df.columns)
            file_size = os.path.getsize(file_path)
        except Exception as e:
            os.remove(file_path)
            raise HTTPException(status_code=400, detail=f"Failed to read file: {str(e)}")

        return {
            "success": True,
            "file_path": file_path,
            "file_name": file.filename,
            "file_size": file_size,
            "columns": columns,
            "row_count": row_count,
        }

    @app.get("/svcmodels")
    async def svc_list_models():
        list_models = _import("app.api.routes.models", "list_models")
        async with get_db_session() as db:
            return await list_models(db)

    @app.get("/svcdeployments")
    async def svc_list_deployments():
        try:
            api = _import("app.core.domino_model_api", "get_domino_model_api")()
            result = await api.list_deployments()
            return result if isinstance(result, dict) else {"success": True, "data": [], "error": "Invalid response"}
        except Exception as e:
            logger.error(f"Error listing deployments: {e}")
            return {"success": True, "data": [], "error": str(e)}

    @app.get("/svcmodelapis")
    async def svc_list_model_apis():
        try:
            api = _import("app.core.domino_model_api", "get_domino_model_api")()
            result = await api.list_model_apis()
            return result if isinstance(result, dict) else {"success": True, "data": [], "error": "Invalid response"}
        except Exception as e:
            logger.error(f"Error listing model APIs: {e}")
            return {"success": True, "data": [], "error": str(e)}

    @app.post("/svcdeployfromjob")
    async def svc_deploy_from_job(body: dict = Body(default={})):
        deploy_fn = _import("app.api.routes.deployments", "deploy_from_job")
        return await deploy_fn(
            job_id=body.get("job_id"),
            model_name=body.get("model_name"),
            function_name=body.get("function_name", "predict"),
            min_replicas=body.get("min_replicas", 1),
            max_replicas=body.get("max_replicas", 1),
        )

    @app.get("/svcping")
    async def svc_ping():
        return {"success": True, "message": "pong", "timestamp": datetime.now().isoformat()}
