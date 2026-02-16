"""Pattern-based compatibility route registration."""

from fastapi import Body, FastAPI

from app.dependencies import get_db_session

from app.api.compat.common import lazy_import


def register_pattern_routes(app: FastAPI) -> None:
    """Register compatibility routes that share common endpoint patterns."""
    # Pattern 1: Simple GET -> async function()
    simple_gets = {
        "/svchealth": ("app.api.routes.health", "health_check"),
        "/svcloadedmodels": ("app.api.routes.predictions", "get_loaded_models"),
        "/svcmetrics": ("app.api.routes.profiling", "get_available_metrics"),
        "/svcpresets": ("app.api.routes.profiling", "get_available_presets"),
        "/svcregisteredmodels": ("app.api.routes.registry", "list_registered_models"),
        "/svcexportformats": ("app.api.routes.export", "get_supported_formats"),
        "/svcqueuestatus": ("app.api.compat.adapters.jobs", "get_queue_status"),
    }

    for path, (mod, fn) in simple_gets.items():
        def _handler(m=mod, f=fn):
            async def endpoint():
                return await lazy_import(m, f)()

            endpoint.__name__ = f"svc_{f}"
            return endpoint

        app.get(path)(_handler())

    # Pattern 2: POST body -> RequestClass -> func(request)
    post_request = [
        ("/svcpredict", "app.api.routes.predictions", "predict", "PredictRequest"),
        ("/svcpredictbatch", "app.api.routes.predictions", "batch_predict", "BatchPredictRequest"),
        ("/svcprofile", "app.api.routes.profiling", "profile_data", "ProfileRequest"),
        ("/svcsuggesttarget", "app.api.routes.profiling", "suggest_target_column", "ProfileRequest"),
        ("/svcprofiletimeseries", "app.api.routes.profiling", "profile_timeseries", "TimeSeriesProfileRequest"),
        ("/svcprofileasyncstart", "app.api.routes.profiling", "start_profile_async", "AsyncProfileStartRequest"),
        ("/svcprofileasyncstatus", "app.api.routes.profiling", "get_profile_async_status", "AsyncProfileStatusRequest"),
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
                func, req_cls = lazy_import(m, f, c)
                return await func(req_cls(**body))

            endpoint.__name__ = f"svc_{f}"
            return endpoint

        app.post(path)(_handler())

    # Pattern 3: POST body.get(keys) -> func(*args)
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
                func = lazy_import(m, f)
                args = [body.get(*key) for key in k]
                return await func(*args)

            endpoint.__name__ = f"svc_{f}"
            return endpoint

        app.post(path)(_handler())

    # Pattern 4: POST body -> RequestClass + DB -> func(req, db)
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
        ("/svcjobcleanup", "app.api.compat.adapters.jobs", "bulk_cleanup", "CleanupRequest"),
    ]

    for path, mod, fn, cls in post_request_db:
        def _handler(m=mod, f=fn, c=cls):
            async def endpoint(body: dict = Body(default={})):
                func, req_cls = lazy_import(m, f, c)
                async with get_db_session() as db:
                    return await func(req_cls(**body), db)

            endpoint.__name__ = f"svc_{f}"
            return endpoint

        app.post(path)(_handler())

    # Pattern 5: POST body.get(keys) + DB -> func(*args, db)
    post_keys_db = [
        ("/svcjobget", "app.api.compat.adapters.jobs", "get_job", [("job_id",)]),
        ("/svcjobcancel", "app.api.compat.adapters.jobs", "cancel_job", [("job_id",)]),
        ("/svcjobdelete", "app.api.compat.adapters.jobs", "delete_job", [("job_id",)]),
        ("/svcjobstatus", "app.api.compat.adapters.jobs", "get_job_status", [("job_id",)]),
        ("/svcjobmetrics", "app.api.compat.adapters.jobs", "get_job_metrics", [("job_id",)]),
        ("/svcjoblogs", "app.api.compat.adapters.jobs", "get_job_logs", [("job_id",), ("limit", 100)]),
        ("/svcjobprogress", "app.api.compat.adapters.jobs", "get_job_progress", [("job_id",)]),
    ]

    for path, mod, fn, keys in post_keys_db:
        def _handler(m=mod, f=fn, k=keys):
            async def endpoint(body: dict = Body(default={})):
                func = lazy_import(m, f)
                args = [body.get(*key) for key in k]
                async with get_db_session() as db:
                    return await func(*args, db)

            endpoint.__name__ = f"svc_{f}"
            return endpoint

        app.post(path)(_handler())
