"""
Simple FastAPI server that:
1. Serves the React app static files
2. Proxies /api/* requests to the automl-service
"""

import os
import re
import json
import httpx
from urllib.parse import urlencode, quote
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import logging

# Configure logging (configurable via environment)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=getattr(logging, LOG_LEVEL, logging.INFO))
logger = logging.getLogger(__name__)

# Get the API service URL from environment (required in production)
API_SERVICE_URL = os.environ.get("API_SERVICE_URL")
if not API_SERVICE_URL:
    # Fallback for development only
    API_SERVICE_URL = "https://apps.se-demo.domino.tech/apps/9f146ade-e113-46e4-a5ae-1f3c04fb3fa8"
    logger.warning("API_SERVICE_URL not set, using development default")

# Configuration
HTTP_TIMEOUT = float(os.environ.get("HTTP_TIMEOUT", "60.0"))
MAX_FILE_SIZE = int(os.environ.get("MAX_FILE_SIZE", str(100 * 1024 * 1024)))  # 100MB default
MAX_PREVIEW_ROWS = int(os.environ.get("MAX_PREVIEW_ROWS", "10000"))

# Allowed dataset paths (configurable via environment)
# For browsing datasets, only show /domino/datasets/local
# For file validation (uploads, previews), allow additional paths
DATASET_BROWSE_PATHS = os.environ.get("DATASET_BROWSE_PATHS", "/domino/datasets/local").split(":")
DATASET_PATHS = os.environ.get("DATASET_PATHS", "/domino/datasets/local:/domino/datasets:/domino:/mnt:/mnt/automl-uploads:/mnt/automl-ui/uploads:/tmp:/var/tmp").split(":")

logger.info(f"API_SERVICE_URL configured (not logged for security)")

# Create async HTTP client
http_client: httpx.AsyncClient = None


# =============================================================================
# Utility Functions
# =============================================================================

def create_error_response(message: str, status_code: int = 400) -> Response:
    """Create a standardized error response."""
    return Response(
        content=json.dumps({"success": False, "error": message}),
        status_code=status_code,
        media_type="application/json"
    )


def validate_path_safety(file_path: str, allowed_bases: list[str] = None) -> tuple[bool, str]:
    """
    Validate that a file path is safe and within allowed directories.
    Returns (is_valid, error_message).
    """
    if not file_path:
        return False, "File path is required"

    # Normalize the path to prevent traversal attacks
    try:
        real_path = os.path.realpath(file_path)
    except (ValueError, OSError):
        return False, "Invalid file path"

    # Check for path traversal attempts
    if ".." in file_path:
        return False, "Path traversal not allowed"

    # If allowed_bases is provided, verify path is within allowed directories
    if allowed_bases:
        is_allowed = False
        for base in allowed_bases:
            try:
                base_real = os.path.realpath(base)
                if real_path.startswith(base_real + os.sep) or real_path == base_real:
                    is_allowed = True
                    break
            except (ValueError, OSError):
                continue

        if not is_allowed:
            return False, "File path is outside allowed directories"

    return True, ""


def validate_identifier(value: str, name: str, max_length: int = 256) -> tuple[bool, str]:
    """
    Validate an identifier (job_id, model_name, etc.).
    Returns (is_valid, error_message).
    """
    if not value:
        return False, f"{name} is required"

    if not isinstance(value, str):
        return False, f"{name} must be a string"

    if len(value) > max_length:
        return False, f"{name} exceeds maximum length of {max_length}"

    # Allow alphanumeric, hyphens, underscores, dots, and forward slashes (for paths)
    if not re.match(r'^[\w\-./]+$', value):
        return False, f"{name} contains invalid characters"

    return True, ""


async def parse_json_body(request: Request) -> tuple[dict, Response]:
    """
    Safely parse JSON body from request.
    Returns (body_dict, error_response). If successful, error_response is None.
    """
    try:
        body = await request.json()
        if not isinstance(body, dict):
            return None, create_error_response("Request body must be a JSON object", 400)
        return body, None
    except json.JSONDecodeError as e:
        logger.warning(f"Invalid JSON in request: {e}")
        return None, create_error_response("Invalid JSON in request body", 400)
    except Exception as e:
        logger.error(f"Error parsing request body: {e}")
        return None, create_error_response("Failed to parse request body", 400)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage HTTP client lifecycle."""
    global http_client
    http_client = httpx.AsyncClient(timeout=HTTP_TIMEOUT, follow_redirects=True)
    logger.info("HTTP client initialized")
    yield
    await http_client.aclose()
    logger.info("HTTP client closed")


app = FastAPI(lifespan=lifespan)

# Static file paths
dist_path = os.path.join(os.path.dirname(__file__), "dist")
logger.info(f"Dist path: {dist_path}, exists: {os.path.exists(dist_path)}")


# Get Domino access token for inter-app communication
async def get_domino_token() -> str:
    """Fetch access token from Domino's local token endpoint."""
    token_endpoint = os.environ.get("DOMINO_TOKEN_ENDPOINT", "http://localhost:8899/access-token")

    # First, try the local token endpoint (works in Domino Apps)
    try:
        response = await http_client.get(token_endpoint, timeout=5.0)
        if response.status_code == 200 and response.text:
            return response.text
    except httpx.RequestError as e:
        logger.debug(f"Local token endpoint not available: {e}")
    except Exception as e:
        logger.debug(f"Unexpected error fetching token: {e}")

    # Fallback to DOMINO_API_KEY environment variable
    api_key = os.environ.get("DOMINO_API_KEY") or os.environ.get("DOMINO_USER_API_KEY")
    if api_key:
        logger.debug("Using DOMINO_API_KEY for authentication")
        return api_key

    # Try reading from token file (some Domino deployments)
    token_file = os.environ.get("DOMINO_TOKEN_FILE")
    if token_file and os.path.exists(token_file):
        try:
            with open(token_file, 'r') as f:
                return f.read().strip()
        except (IOError, OSError) as e:
            logger.warning(f"Failed to read token file: {e}")

    logger.warning("No Domino authentication token available")
    return ""


# =============================================================================
# Proxy Helpers
# =============================================================================

async def proxy_to_backend_single(request: Request, endpoint: str, body: bytes = None):
    """Proxy a request to a backend single-segment endpoint."""
    target_url = f"{API_SERVICE_URL}/{endpoint}"
    method = request.method

    logger.info(f"Proxy single: {method} -> {endpoint}")

    # Get Domino bearer token
    token = await get_domino_token()

    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = await http_client.request(
            method=method,
            url=target_url,
            headers=headers,
            content=body,
        )
        logger.info(f"Proxy response: {response.status_code}")
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/json",
        )
    except httpx.RequestError as e:
        logger.error(f"Proxy error to {endpoint}: {type(e).__name__}")
        return create_error_response("Service temporarily unavailable", 502)


async def proxy_to_service(request: Request, service_path: str, method_override: str = None, body: bytes = None):
    """Proxy a request to the service."""
    target_url = f"{API_SERVICE_URL}/svc/{service_path}"
    method = method_override or request.method

    logger.info(f"Proxy: {method} -> {service_path}")

    # Get Domino bearer token
    token = await get_domino_token()

    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Forward Domino headers
    for key, value in request.headers.items():
        if key.lower().startswith('domino-'):
            headers[key] = value

    try:
        response = await http_client.request(
            method=method,
            url=target_url,
            headers=headers,
            content=body,
        )
        logger.info(f"Proxy response: {response.status_code}")
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/json",
        )
    except httpx.RequestError as e:
        logger.error(f"Proxy error to {service_path}: {type(e).__name__}")
        return create_error_response("Service temporarily unavailable", 502)


# =============================================================================
# API Endpoints
# =============================================================================

@app.api_route("/svchealth", methods=["GET"])
async def svc_health(request: Request):
    return await proxy_to_service(request, "v1/health")

@app.api_route("/svcuser", methods=["GET"])
async def svc_user(request: Request):
    return await proxy_to_service(request, "v1/health/user")

@app.api_route("/svcjobs", methods=["GET", "POST"])
async def svc_jobs(request: Request):
    """List jobs - GET uses query params, POST uses body for Domino compatibility."""
    if request.method == "POST":
        body = await request.body()
        return await proxy_to_service(request, "v1/jobs/list", body=body)
    else:
        return await proxy_to_service(request, "v1/jobs")


# Individual job operations - use POST with job_id in body
@app.post("/svcjobget")
async def svc_job_get(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}", method_override="GET")

@app.post("/svcjobstatus")
async def svc_job_status(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}/status", method_override="GET")

@app.post("/svcjobmetrics")
async def svc_job_metrics(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}/metrics", method_override="GET")

@app.post("/svcjoblogs")
async def svc_job_logs(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}/logs", method_override="GET")

@app.post("/svcjobprogress")
async def svc_job_progress(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}/progress", method_override="GET")

@app.post("/svcjobcancel")
async def svc_job_cancel(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}/cancel", method_override="POST")

@app.post("/svcjobdelete")
async def svc_job_delete(request: Request):
    body, error = await parse_json_body(request)
    if error:
        return error

    job_id = body.get("job_id")
    valid, msg = validate_identifier(job_id, "job_id")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/jobs/{quote(job_id, safe='')}", method_override="DELETE")

@app.api_route("/svcdatasets", methods=["GET"])
async def svc_datasets(request: Request):
    """List datasets from mounted paths (no API call needed).

    Each base path is treated as a single dataset entry, with all
    data files (CSV, Parquet) within it listed as files.
    """
    datasets = []

    def find_data_files(directory: str, base_dir: str) -> list:
        """Recursively find all data files in a directory."""
        files = []
        try:
            for item in os.listdir(directory):
                # Skip hidden files and snapshots
                if item.startswith('.') or item == "snapshots":
                    continue

                item_path = os.path.join(directory, item)

                try:
                    if os.path.isfile(item_path):
                        # Only include data files (CSV, Parquet)
                        lower_name = item.lower()
                        if lower_name.endswith(('.csv', '.parquet', '.pq')):
                            stat = os.stat(item_path)
                            # Use relative path from base for display
                            rel_path = os.path.relpath(item_path, base_dir)
                            files.append({
                                "name": rel_path,
                                "size": stat.st_size,
                                "path": item_path
                            })
                    elif os.path.isdir(item_path):
                        # Recurse into subdirectories
                        files.extend(find_data_files(item_path, base_dir))
                except (OSError, IOError, PermissionError):
                    continue
        except (PermissionError, OSError):
            pass
        return files

    # Use DATASET_BROWSE_PATHS for listing (only /domino/datasets/local by default)
    for base_path in DATASET_BROWSE_PATHS:
        if not base_path or not os.path.exists(base_path) or not os.path.isdir(base_path):
            continue

        try:
            # Find all data files recursively in this base path
            files = find_data_files(base_path, base_path)
            total_size = sum(f["size"] for f in files)

            # Determine dataset name from path
            dataset_name = os.path.basename(base_path.rstrip('/'))
            if dataset_name == "local":
                dataset_name = "Local Datasets"
            elif dataset_name == "data":
                dataset_name = "Imported Data"

            if files:  # Only add if there are data files
                datasets.append({
                    "id": base_path,
                    "name": dataset_name,
                    "path": base_path,
                    "description": f"Mounted at {base_path}",
                    "size_bytes": total_size,
                    "file_count": len(files),
                    "files": files
                })
        except (PermissionError, OSError) as e:
            logger.warning(f"Error accessing {base_path}: {type(e).__name__}")

    return {"datasets": datasets, "total": len(datasets)}

@app.post("/svcdatasetpreview")
async def svc_dataset_preview(request: Request):
    """Preview dataset file contents - proxy to backend."""
    body = await request.body()
    return await proxy_to_service(request, "v1/datasets/preview", body=body)

@app.post("/svcupload")
async def svc_upload(request: Request):
    """Proxy file upload to backend service."""
    try:
        form = await request.form()
    except Exception as e:
        logger.error(f"Error parsing form data: {e}")
        return create_error_response("Invalid form data", 400)

    file = form.get("file")

    if not file:
        return create_error_response("No file provided", 400)

    logger.info(f"[UPLOAD] Proxying file: {file.filename}")

    # Get auth token
    token = await get_domino_token()

    # Read file content with size limit
    try:
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            return create_error_response(f"File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)}MB", 413)
    except Exception as e:
        logger.error(f"Error reading uploaded file: {e}")
        return create_error_response("Failed to read uploaded file", 400)

    # Proxy to backend service
    target_url = f"{API_SERVICE_URL}/svc/v1/datasets/upload"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        files = {"file": (file.filename, content, file.content_type or "application/octet-stream")}
        response = await http_client.post(
            target_url,
            files=files,
            headers=headers,
        )
        logger.info(f"[UPLOAD] Backend response: {response.status_code}")

        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/json",
        )
    except httpx.RequestError as e:
        logger.error(f"[UPLOAD] Proxy error: {type(e).__name__}")
        return create_error_response("Upload service temporarily unavailable", 502)

@app.api_route("/svcmodels", methods=["GET"])
async def svc_models(request: Request):
    return await proxy_to_service(request, "v1/models")


# Registry endpoints
@app.api_route("/svcregisteredmodels", methods=["GET", "POST"])
async def svc_registered_models(request: Request):
    """List all registered models."""
    return await proxy_to_service(request, "v1/registry/models", method_override="GET")

@app.post("/svcregistermodel")
async def svc_register_model(request: Request):
    """Register a new model."""
    body = await request.body()
    return await proxy_to_service(request, "v1/registry/register", body=body)

@app.post("/svcmodelversions")
async def svc_model_versions(request: Request):
    """Get versions of a registered model."""
    body, error = await parse_json_body(request)
    if error:
        return error

    model_name = body.get("model_name")
    valid, msg = validate_identifier(model_name, "model_name")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/registry/models/{quote(model_name, safe='')}/versions", method_override="GET")

@app.post("/svctransitionstage")
async def svc_transition_stage(request: Request):
    """Transition model version stage."""
    body = await request.body()
    return await proxy_to_service(request, "v1/registry/models/transition-stage", body=body)

@app.post("/svcupdatedescription")
async def svc_update_description(request: Request):
    """Update model description."""
    body = await request.body()
    return await proxy_to_service(request, "v1/registry/models/update-description", body=body)

@app.post("/svcdeleteversion")
async def svc_delete_version(request: Request):
    """Delete a model version."""
    body, error = await parse_json_body(request)
    if error:
        return error

    model_name = body.get("model_name")
    version = body.get("version")

    valid, msg = validate_identifier(model_name, "model_name")
    if not valid:
        return create_error_response(msg)

    if version is None:
        return create_error_response("version is required")

    return await proxy_to_service(request, f"v1/registry/models/{quote(model_name, safe='')}/versions/{version}", method_override="DELETE")

@app.post("/svcdeletemodel")
async def svc_delete_model(request: Request):
    """Delete a registered model."""
    body, error = await parse_json_body(request)
    if error:
        return error

    model_name = body.get("model_name")
    valid, msg = validate_identifier(model_name, "model_name")
    if not valid:
        return create_error_response(msg)

    return await proxy_to_service(request, f"v1/registry/models/{quote(model_name, safe='')}", method_override="DELETE")

@app.post("/svcmodelcard")
async def svc_model_card(request: Request):
    """Generate model card."""
    body = await request.body()
    return await proxy_to_service(request, "v1/registry/models/card", body=body)

@app.post("/svcdownloadmodel")
async def svc_download_model(request: Request):
    """Download model from registry."""
    body, error = await parse_json_body(request)
    if error:
        return error

    model_name = body.get("model_name")
    version = body.get("version")

    valid, msg = validate_identifier(model_name, "model_name")
    if not valid:
        return create_error_response(msg)

    if version is None:
        return create_error_response("version is required")

    return await proxy_to_service(request, f"v1/registry/models/{quote(model_name, safe='')}/versions/{version}/download", body=b'{}')


# Job creation endpoint
@app.post("/svcjobcreate")
async def svc_job_create(request: Request):
    """Create a new training job."""
    body = await request.body()
    return await proxy_to_service(request, "v1/jobs", body=body)

@app.post("/svcjobregister")
async def svc_job_register(request: Request):
    """Register a job's model to registry."""
    body = await request.body()
    return await proxy_to_service(request, "v1/jobs/register", body=body)


# Prediction endpoints
@app.post("/svcpredict")
async def svc_predict(request: Request):
    """Make predictions with a model."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/predict", body=body)

@app.post("/svcpredictbatch")
async def svc_predict_batch(request: Request):
    """Make batch predictions."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/predict/batch", body=body)

@app.post("/svcmodelinfo")
async def svc_model_info(request: Request):
    """Get model information."""
    body, error = await parse_json_body(request)
    if error:
        return error

    model_path = body.get("model_path")
    valid, msg = validate_identifier(model_path, "model_path", max_length=512)
    if not valid:
        return create_error_response(msg)

    # Use proper URL encoding
    params = urlencode({"model_path": model_path})
    return await proxy_to_service(request, f"v1/predictions/model/info?{params}", method_override="GET")

@app.post("/svcfeatureimportance")
async def svc_feature_importance(request: Request):
    """Get feature importance for a model."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/feature-importance", body=body)

@app.post("/svcleaderboard")
async def svc_leaderboard(request: Request):
    """Get model leaderboard."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/leaderboard", body=body)

@app.post("/svcconfusionmatrix")
async def svc_confusion_matrix(request: Request):
    """Get confusion matrix for classification model."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/confusion-matrix", body=body)

@app.post("/svcroccurve")
async def svc_roc_curve(request: Request):
    """Get ROC curve for classification model."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/roc-curve", body=body)

@app.post("/svcprecisionrecall")
async def svc_precision_recall(request: Request):
    """Get precision-recall curve."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/precision-recall", body=body)

@app.post("/svcregressiondiagnostics")
async def svc_regression_diagnostics(request: Request):
    """Get regression diagnostics."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/regression-diagnostics", body=body)

@app.post("/svcunloadmodel")
async def svc_unload_model(request: Request):
    """Unload a model from memory."""
    body = await request.body()
    return await proxy_to_service(request, "v1/predictions/model/unload", body=body)

@app.api_route("/svcloadedmodels", methods=["GET", "POST"])
async def svc_loaded_models(request: Request):
    """List loaded models."""
    return await proxy_to_service(request, "v1/predictions/models/loaded", method_override="GET")


# Profiling endpoints
@app.post("/svcprofile")
async def svc_profile(request: Request):
    """Profile a dataset."""
    body = await request.body()
    return await proxy_to_service(request, "v1/profiling/profile", body=body)

@app.post("/svcprofilequick")
async def svc_profile_quick(request: Request):
    """Quick profile a dataset."""
    body = await request.body()
    return await proxy_to_service(request, "v1/profiling/profile/quick", body=body)

@app.post("/svcsuggesttarget")
async def svc_suggest_target(request: Request):
    """Suggest target column for a dataset."""
    body = await request.body()
    return await proxy_to_service(request, "v1/profiling/suggest-target", body=body)

@app.post("/svcprofilecolumn")
async def svc_profile_column(request: Request):
    """Profile a specific column."""
    body, error = await parse_json_body(request)
    if error:
        return error

    file_path = body.get("file_path")
    column_name = body.get("column_name")

    # Validate inputs
    valid, msg = validate_path_safety(file_path, DATASET_PATHS)
    if not valid:
        return create_error_response(msg)

    valid, msg = validate_identifier(column_name, "column_name")
    if not valid:
        return create_error_response(msg)

    # Use proper URL encoding
    params = urlencode({"file_path": file_path})
    return await proxy_to_service(request, f"v1/profiling/profile/column/{quote(column_name, safe='')}?{params}", method_override="POST", body=b'{}')

@app.api_route("/svcmetrics", methods=["GET", "POST"])
async def svc_metrics(request: Request):
    """Get available metrics."""
    return await proxy_to_service(request, "v1/profiling/metrics", method_override="GET")

@app.api_route("/svcpresets", methods=["GET", "POST"])
async def svc_presets(request: Request):
    """Get available presets."""
    return await proxy_to_service(request, "v1/profiling/presets", method_override="GET")


# Export endpoints - use single-segment endpoints on service
@app.post("/svcexportonnx")
async def svc_export_onnx(request: Request):
    """Export model to ONNX format."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcexportonnx", body=body)

@app.post("/svcexportdeployment")
async def svc_export_deployment(request: Request):
    """Export model for deployment."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcexportdeployment", body=body)

@app.post("/svclearningcurves")
async def svc_learning_curves(request: Request):
    """Get learning curves for a model."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svclearningcurves", body=body)

@app.post("/svccomparemodels")
async def svc_compare_models(request: Request):
    """Compare multiple models."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svccomparemodels", body=body)

@app.api_route("/svcexportformats", methods=["GET", "POST"])
async def svc_export_formats(request: Request):
    """Get available export formats."""
    return await proxy_to_backend_single(request, "svcexportformats")

@app.post("/svcexportnotebook")
async def svc_export_notebook(request: Request):
    """Export job configuration as a Jupyter notebook."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcexportnotebook", body=body)

@app.post("/svcshapanalysis")
async def svc_shap_analysis(request: Request):
    """Run SHAP analysis on a model."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcshapanalysis", body=body)


# Deployment endpoints
@app.get("/svcdeployments")
async def svc_list_deployments(request: Request):
    """List all deployments."""
    target_url = f"{API_SERVICE_URL}/svcdeployments"
    logger.info(f"Proxy: GET -> svcdeployments")
    token = await get_domino_token()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        response = await http_client.get(target_url, headers=headers)
        logger.info(f"Proxy response: {response.status_code}")
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type="application/json",
        )
    except httpx.RequestError as e:
        logger.error(f"Proxy error: {type(e).__name__}")
        # Return proper error status instead of 200 with error message
        return Response(
            content=json.dumps({"success": False, "data": [], "error": "Service unavailable"}),
            status_code=503,
            media_type="application/json",
        )

@app.post("/svcdeploymentcreate")
async def svc_create_deployment(request: Request):
    """Create a new deployment - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentcreate", body=body)

@app.post("/svcdeploymentget")
async def svc_get_deployment(request: Request):
    """Get a deployment - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentget", body=body)

@app.post("/svcdeploymentstart")
async def svc_start_deployment(request: Request):
    """Start a deployment - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentstart", body=body)

@app.post("/svcdeploymentstop")
async def svc_stop_deployment(request: Request):
    """Stop a deployment - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentstop", body=body)

@app.post("/svcdeploymentdelete")
async def svc_delete_deployment(request: Request):
    """Delete a deployment - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentdelete", body=body)

@app.post("/svcdeploymentstatus")
async def svc_deployment_status(request: Request):
    """Get deployment status - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentstatus", body=body)

@app.post("/svcdeploymentlogs")
async def svc_deployment_logs(request: Request):
    """Get deployment logs - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeploymentlogs", body=body)

@app.post("/svcquickdeploy")
async def svc_quick_deploy(request: Request):
    """Quick deploy a model - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcquickdeploy", body=body)

@app.post("/svcdeployfromjob")
async def svc_deploy_from_job(request: Request):
    """Deploy a model from a job - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcdeployfromjob", body=body)

@app.get("/svcmodelapis")
async def svc_list_model_apis(request: Request):
    """List all model APIs - proxy to backend single-segment endpoint."""
    return await proxy_to_backend_single(request, "svcmodelapis")

@app.post("/svcmodelapicreate")
async def svc_create_model_api(request: Request):
    """Create a model API - proxy to backend single-segment endpoint."""
    body = await request.body()
    return await proxy_to_backend_single(request, "svcmodelapicreate", body=body)

@app.get("/svcping")
async def svc_ping():
    """Simple ping for testing."""
    return {"success": True, "message": "pong", "source": "proxy"}


# =============================================================================
# Static File Routes
# =============================================================================

@app.get("/config.js")
async def serve_config():
    return FileResponse(os.path.join(dist_path, "config.js"))


@app.get("/domino-logo.svg")
async def serve_logo():
    logo_path = os.path.join(dist_path, "domino-logo.svg")
    if os.path.exists(logo_path):
        return FileResponse(logo_path)
    return Response(status_code=404)


# Mount static assets
if os.path.exists(os.path.join(dist_path, "assets")):
    app.mount("/assets", StaticFiles(directory=os.path.join(dist_path, "assets")), name="assets")


# Health/debug endpoint to verify proxy is loaded
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "dist_path": dist_path,
        "dist_exists": os.path.exists(dist_path),
    }

# Test endpoints to find what paths Domino allows
@app.get("/test1")
async def test1():
    return {"path": "/test1", "status": "ok"}

@app.get("/ping")
async def ping():
    return {"path": "/ping", "status": "ok"}

@app.get("/status")
async def status():
    return {"path": "/status", "status": "ok"}


# SPA catch-all - MUST be last
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(dist_path, "index.html"))


@app.get("/{path:path}")
async def serve_spa(path: str):
    """Serve the SPA - always return index.html for client-side routing."""
    # Don't serve SPA for API paths (should have been caught above)
    if path.startswith("api/") or path.startswith("svc"):
        logger.warning(f"API path fell through to SPA handler: {path}")
        return create_error_response("Not found", 404)

    # Validate path to prevent traversal attacks
    # Normalize and ensure it stays within dist_path
    try:
        # Clean the path
        clean_path = os.path.normpath(path).lstrip(os.sep)

        # Construct full path
        file_path = os.path.join(dist_path, clean_path)
        real_file_path = os.path.realpath(file_path)
        real_dist_path = os.path.realpath(dist_path)

        # Ensure the resolved path is within dist_path
        if not real_file_path.startswith(real_dist_path + os.sep) and real_file_path != real_dist_path:
            logger.warning(f"Path traversal attempt blocked: {path}")
            return FileResponse(os.path.join(dist_path, "index.html"))

        if os.path.isfile(real_file_path):
            return FileResponse(real_file_path)
    except (ValueError, OSError) as e:
        logger.warning(f"Invalid path: {path}, error: {type(e).__name__}")

    return FileResponse(os.path.join(dist_path, "index.html"))
