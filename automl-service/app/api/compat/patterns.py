"""Pattern-based compatibility route registration."""

from fastapi import Body, FastAPI, Request

from app.dependencies import get_db_session

from app.api.compat.common import lazy_import


def _make_endpoint(mod, fn, cls=None, keys=None, use_db=False, db_first=False, method="post", project_scoped=False):
    """Create a compat endpoint closure for any of the 5 patterns."""
    def _handler(m=mod, f=fn, c=cls, k=keys):
        if c:
            # Pattern 2/4: RequestClass-based
            if project_scoped:
                async def endpoint(request: Request, body: dict = Body(default={})):
                    func, req_cls = lazy_import(m, f, c)
                    project_id = request.headers.get("X-Project-Id")
                    if use_db:
                        async with get_db_session() as db:
                            return await func(req_cls(**body), db, project_id=project_id)
                    return await func(req_cls(**body), project_id=project_id)
            else:
                async def endpoint(body: dict = Body(default={})):
                    func, req_cls = lazy_import(m, f, c)
                    if use_db:
                        async with get_db_session() as db:
                            return await func(req_cls(**body), db)
                    return await func(req_cls(**body))
        elif k is not None:
            # Pattern 3/5: key-extraction
            async def endpoint(body: dict = Body(default={})):
                func = lazy_import(m, f)
                args = [body.get(*key) for key in k]
                if use_db:
                    async with get_db_session() as db:
                        if db_first:
                            return await func(db, *args)
                        return await func(*args, db)
                return await func(*args)
        elif use_db:
            # Pattern 1b: Simple GET + DB
            if project_scoped:
                async def endpoint(request: Request):
                    func = lazy_import(m, f)
                    project_id = request.headers.get("X-Project-Id")
                    async with get_db_session() as db:
                        return await func(db, project_id=project_id)
            else:
                async def endpoint():
                    func = lazy_import(m, f)
                    async with get_db_session() as db:
                        return await func(db)
        else:
            # Pattern 1: Simple GET
            async def endpoint():
                return await lazy_import(m, f)()

        endpoint.__name__ = f"svc_{f}"
        return endpoint
    return _handler()


def register_pattern_routes(app: FastAPI) -> None:
    """Register compatibility routes that share common endpoint patterns."""
    # Pattern 1: Simple GET -> async function()
    simple_gets = {
        "/svchealth": ("app.api.routes.health", "health_check"),
        "/svcloadedmodels": ("app.api.routes.predictions", "get_loaded_models"),
        "/svcmetrics": ("app.api.routes.profiling", "get_available_metrics"),
        "/svcpresets": ("app.api.routes.profiling", "get_available_presets"),
        "/svcexportformats": ("app.api.routes.export", "get_supported_formats"),
        "/svcqueuestatus": ("app.api.compat.adapters.jobs", "get_queue_status"),
    }

    for path, (mod, fn) in simple_gets.items():
        app.get(path)(_make_endpoint(mod, fn, method="get"))

    # Pattern 1b: Simple GET + DB -> async function(db)
    simple_gets_db = [
        ("/svcregisteredmodels", "app.api.routes.registry", "list_registered_models", True),
    ]

    for path, mod, fn, scoped in simple_gets_db:
        app.get(path)(_make_endpoint(mod, fn, use_db=True, method="get", project_scoped=scoped))

    # Pattern 2: POST body -> RequestClass -> func(request)
    post_request = [
        ("/svcpredict", "app.api.routes.predictions", "predict", "PredictRequest"),
        ("/svcpredictbatch", "app.api.routes.predictions", "batch_predict", "BatchPredictRequest"),
        ("/svcprofile", "app.api.routes.profiling", "profile_data", "ProfileRequest"),
        ("/svcsuggesttarget", "app.api.routes.profiling", "suggest_target_column", "ProfileRequest"),
        ("/svcprofiletimeseries", "app.api.routes.profiling", "profile_timeseries", "TimeSeriesProfileRequest"),
        ("/svcprofileasyncstart", "app.api.routes.profiling", "start_profile_async", "AsyncProfileStartRequest"),
        ("/svcprofileasyncstatus", "app.api.routes.profiling", "get_profile_async_status", "AsyncProfileStatusRequest"),
        ("/svctransitionstage", "app.api.routes.registry", "transition_model_stage", "TransitionStageRequest"),
        ("/svcupdatedescription", "app.api.routes.registry", "update_model_description", "UpdateDescriptionRequest"),
        ("/svcmodelcard", "app.api.routes.registry", "generate_model_card", "ModelCardRequest"),
        ("/svccomparemodels", "app.api.routes.export", "compare_models", "ModelComparisonRequest"),
        ("/svcdeploymentcreate", "app.api.routes.deployments", "create_deployment", "CreateDeploymentRequest"),
        ("/svcquickdeploy", "app.api.routes.deployments", "quick_deploy", "QuickDeployRequest"),
        ("/svcmodelapicreate", "app.api.routes.deployments", "create_model_api", "CreateModelApiRequest"),
    ]

    for path, mod, fn, cls in post_request:
        app.post(path)(_make_endpoint(mod, fn, cls=cls))

    # Pattern 3: POST body.get(keys) -> func(*args)
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
        app.post(path)(_make_endpoint(mod, fn, keys=keys))

    # Pattern 4: POST body -> RequestClass + DB -> func(req, db)
    post_request_db = [
        ("/svcfeatureimportance", "app.api.routes.predictions", "get_feature_importance", "FeatureImportanceRequest", False),
        ("/svcleaderboard", "app.api.routes.predictions", "get_leaderboard", "LeaderboardRequest", False),
        ("/svcconfusionmatrix", "app.api.routes.predictions", "get_confusion_matrix", "DiagnosticsRequest", False),
        ("/svcroccurve", "app.api.routes.predictions", "get_roc_curve", "DiagnosticsRequest", False),
        ("/svcprecisionrecall", "app.api.routes.predictions", "get_precision_recall_curve", "DiagnosticsRequest", False),
        ("/svcregressiondiagnostics", "app.api.routes.predictions", "get_regression_diagnostics", "DiagnosticsRequest", False),
        ("/svcexportdeployment", "app.api.routes.export", "export_deployment_package", "DeploymentPackageRequest", False),
        ("/svclearningcurves", "app.api.routes.export", "get_learning_curves", "LearningCurvesRequest", False),
        ("/svcexportnotebook", "app.api.routes.export", "export_notebook", "ExportNotebookRequest", False),
        ("/svcjobcleanup", "app.api.compat.adapters.jobs", "bulk_cleanup", "CleanupRequest", True),
        ("/svcregistermodel", "app.api.routes.registry", "register_model", "RegisterModelRequest", False),
    ]

    for path, mod, fn, cls, scoped in post_request_db:
        app.post(path)(_make_endpoint(mod, fn, cls=cls, use_db=True, project_scoped=scoped))

    # Pattern 5: POST body.get(keys) + DB -> func(db, *args) [service direct]
    post_keys_db_first = [
        ("/svcjobget", "app.services.job_service", "get_job_response", [("job_id",)]),
        ("/svcjobcancel", "app.services.job_service", "cancel_job", [("job_id",)]),
        ("/svcjobdelete", "app.services.job_service", "delete_job", [("job_id",)]),
        ("/svcjobstatus", "app.services.job_service", "get_job_status_response", [("job_id",)]),
        ("/svcjobmetrics", "app.services.job_service", "get_job_metrics_response", [("job_id",)]),
        ("/svcjobprogress", "app.services.job_service", "get_job_progress_response", [("job_id",)]),
        ("/svcjobbulkdelete", "app.services.job_service", "bulk_delete_jobs", [("job_ids",)]),
    ]

    for path, mod, fn, keys in post_keys_db_first:
        app.post(path)(_make_endpoint(mod, fn, keys=keys, use_db=True, db_first=True))

    # Pattern 5b: POST body.get(keys) + DB -> func(*args, db) [adapter with logic]
    post_keys_db = [
        ("/svcjoblogs", "app.api.compat.adapters.jobs", "get_job_logs", [("job_id",), ("limit", 100)]),
    ]

    for path, mod, fn, keys in post_keys_db:
        app.post(path)(_make_endpoint(mod, fn, keys=keys, use_db=True))
