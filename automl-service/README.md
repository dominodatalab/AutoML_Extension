# AutoML Service

Backend service for the AutoML Extension, powered by [AutoGluon](https://auto.gluon.ai/) with [Domino Data Lab](https://www.dominodatalab.com/) integration. Provides automated machine learning for tabular data (binary classification, multiclass classification, regression) and time series forecasting.

## Architecture

```
automl-service/
├── app/
│   ├── main.py                  # FastAPI app factory, lifespan, CORS, WebSocket
│   ├── config.py                # Settings (env-aware: Domino vs local)
│   ├── dependencies.py          # Dependency injection (DB sessions)
│   ├── api/
│   │   ├── error_handler.py     # @handle_errors() decorator
│   │   ├── compat_routes.py     # Single-segment /svc* routes for Domino proxy
│   │   ├── routes/
│   │   │   ├── health.py        # /svc/v1/health — service health, readiness, user info
│   │   │   ├── jobs.py          # /svc/v1/jobs — training job CRUD, progress, logs
│   │   │   ├── datasets.py      # /svc/v1/datasets — dataset management, uploads
│   │   │   ├── profiling.py     # /svc/v1/profiling — data profiling, target suggestions
│   │   │   ├── predictions.py   # /svc/v1/predictions — model inference
│   │   │   ├── registry.py      # /svc/v1/registry — Domino Model Registry
│   │   │   ├── export.py        # /svc/v1/export — model/notebook export
│   │   │   └── deployments.py   # /svc/v1/deployments — Model API deployments
│   │   └── schemas/
│   │       ├── job.py           # Job request/response Pydantic models
│   │       ├── dataset.py       # Dataset schemas
│   │       └── model.py         # Model registry schemas
│   ├── core/
│   │   ├── data_profiler.py     # Tabular EDA (stats, outliers, correlations)
│   │   ├── ts_profiler.py       # Time series EDA (ADF, ACF/PACF, decomposition)
│   │   ├── job_queue.py         # In-process async job queue with semaphore
│   │   ├── cleanup_service.py   # Bulk cleanup, orphan detection
│   │   ├── dataset_mounts.py    # Domino dataset mount resolution
│   │   ├── notebook_generator.py # Jupyter notebook generation
│   │   ├── experiment_tracker.py # MLflow integration
│   │   ├── domino_job_launcher.py # Launch training as Domino Jobs
│   │   ├── domino_model_api.py  # Domino Model API deployment
│   │   ├── domino_registry.py   # Domino Model Registry API
│   │   ├── prediction_service.py # Load and run inference
│   │   ├── model_diagnostics.py # SHAP, feature importance
│   │   ├── model_export.py      # Export trained models
│   │   ├── model_loader.py      # Model deserialization
│   │   ├── trainers/
│   │   │   ├── tabular.py       # AutoGluon TabularPredictor training
│   │   │   └── timeseries.py    # AutoGluon TimeSeriesPredictor training
│   │   └── websocket_manager.py # Real-time job progress via WebSocket
│   ├── db/
│   │   ├── models.py            # SQLAlchemy ORM (Job, JobLog, RegisteredModel)
│   │   ├── database.py          # Async engine, session factory, migrations
│   │   └── crud.py              # Data access layer
│   ├── services/
│   │   ├── job_service.py       # Job lifecycle, validation, status mapping
│   │   ├── job_links.py         # Deep links to Domino UI
│   │   ├── dataset_service.py   # Dataset preview, upload handling
│   │   ├── deployment_service.py # Model API deployment orchestration
│   │   └── model_service.py     # Registered model queries
│   └── workers/
│       ├── training_worker.py   # Async training execution loop
│       ├── domino_training_runner.py
│       └── domino_eda_runner.py
├── tests/                       # 654 unit + 44 integration tests (see Testing section)
│   ├── integration/             # End-to-end tests against live service
│   │   ├── conftest.py          # Service startup, HTTP client, test data, cleanup
│   │   ├── helpers.py           # Polling utilities (wait for job, deployment)
│   │   ├── test_00_health.py    # Health, readiness, user context
│   │   ├── test_01_profiling.py # Tabular + time series profiling
│   │   ├── test_02_training.py  # Local + Domino Job training lifecycle
│   │   ├── test_03_registry.py  # Model registration, versions, stages
│   │   ├── test_04_deployment.py # Model API and deployment lifecycle
│   │   └── test_05_errors.py    # Error paths and edge cases
│   ├── test_*.py                # Unit tests (mocked DB, no live services)
│   └── conftest.py              # Unit test fixtures
├── scripts/
│   └── generate_synthetic_test_datasets.py
├── Dockerfile
├── requirements.txt
└── pytest.ini
```

## Tech Stack

| Component | Technology |
|---|---|
| Web framework | FastAPI + Uvicorn |
| Database | SQLAlchemy 2.0 (async) + aiosqlite |
| AutoML engine | AutoGluon (tabular + timeseries) |
| Experiment tracking | MLflow |
| Validation | Pydantic v2 |
| Platform integration | Domino Data Lab SDK |
| Statistical analysis | statsmodels |

## Setup

### Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The service detects whether it's running inside Domino or locally and adjusts storage paths accordingly:

| Setting | Domino | Local |
|---|---|---|
| Database | `/mnt/data/{project}/automl.db` | `./automl.db` |
| Models | `/mnt/data/{project}/models/` | `./local_data/models/` |
| Uploads | `/mnt/data/{project}/uploads/` | `./local_data/uploads/` |
| Datasets | `/mnt/data/{project}/datasets/` | `./local_data/datasets/` |

### Docker

```bash
docker build -t automl-service .
docker run -p 8000:8000 automl-service
```

## Configuration

All settings are loaded from environment variables. Key variables:

| Variable | Description |
|---|---|
| `DOMINO_API_HOST` | Domino API host URL |
| `DOMINO_API_KEY` | Domino API key (primary) |
| `DOMINO_USER_API_KEY` | Domino user API key (legacy fallback) |
| `DOMINO_PROJECT_NAME` | Current Domino project name |
| `DOMINO_PROJECT_OWNER` | Domino project owner |
| `DOMINO_PROJECT_ID` | Domino project UUID |
| `DOMINO_USER_HOST` | Domino tenant URL for UI links |
| `DOMINO_TRAINING_HARDWARE_TIER_NAME` | Hardware tier for training jobs |
| `DOMINO_TRAINING_ENVIRONMENT_ID` | Environment ID for training jobs |
| `MLFLOW_TRACKING_URI` | MLflow tracking server URL |
| `DATABASE_URL` | SQLite connection string override |
| `MODELS_PATH` | Override models storage path |
| `UPLOADS_PATH` | Override uploads storage path |
| `DATASETS_PATH` | Override datasets storage path |

See `app/config.py` for the full `Settings` class.

## API Endpoints

All endpoints are prefixed with `/svc/v1/`. Compatibility routes (single-segment `/svc*` paths) are also available for Domino nginx proxy routing.

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Service health check |
| GET | `/health/ready` | Readiness check (DB + Domino) |
| GET | `/health/user` | Current user info |
| POST | `/jobs` | Create a training job |
| POST | `/jobs/list` | List jobs with filters |
| GET | `/jobs/{id}` | Get job details |
| GET | `/jobs/{id}/status` | Get job status |
| GET | `/jobs/{id}/metrics` | Get job metrics |
| POST | `/jobs/{id}/cancel` | Cancel a job |
| DELETE | `/jobs/{id}` | Delete a job |
| POST | `/profiling/profile` | Profile tabular data |
| POST | `/profiling/profile/timeseries` | Profile time series data |
| POST | `/profiling/profile/suggest-target` | Suggest target columns |
| GET | `/profiling/profile/presets` | List training presets |
| GET | `/profiling/profile/metrics` | List evaluation metrics |
| WS | `/ws/jobs/{id}` | Real-time job progress |

## Synthetic Test Data

Generate synthetic datasets for manual testing:

```bash
python scripts/generate_synthetic_test_datasets.py
```

This creates 10 datasets under `local_data/datasets/synthetic_generated_suite/` covering binary classification, multiclass classification, regression, and time series forecasting in both small and large sizes.

---

## Testing

The test suite covers the entire backend with **654 unit tests** and **44 integration tests** across 24 test files.

### Test dependencies

Install requirements files

```bash
pip install -r requirements-dev.txt -r requirements.txt
```

> **Note:** `aiosqlite` and `httpx` are already in `requirements.txt`. The additional packages are `pytest`, `pytest-asyncio`, and `pytest-html`.

### Running tests locally

Tests are configured in `pytest.ini`. The default `addopts` writes an HTML report to `/mnt/results/test_report.html` (a Domino-specific path), so override it when running locally:

```bash
# Run unit tests only (skips integration tests and tests requiring the domino package)
python -m pytest tests/ --ignore=tests/integration/

# Run with HTML report to a local path
python -m pytest tests/ --ignore=tests/integration/ --html=test_report.html --self-contained-html

# Run a specific test file
python -m pytest tests/test_crud.py

# Run tests matching a keyword
python -m pytest tests/ --ignore=tests/integration/ -k "profiler"
```

### Running tests in Domino

When running as a Domino Job, all environment variables and the `domino` package are available, so all 654 unit tests will execute. The HTML report is written to `/mnt/artifacts/results/test_report_xxx.html` and visible in the Domino Job results tab.

```bash
# Run unit tests as a Domino Job command (uses pytest.ini defaults)
python -m pytest tests/ --ignore=tests/integration/
```

To skip slow tests (AutoGluon training):

```bash
python -m pytest tests/ --ignore=tests/integration/ -m "not slow"
```

### Test markers

| Marker | Description |
|---|---|
| `@pytest.mark.slow` | Tests involving AutoGluon training (may take minutes) |
| `@pytest.mark.domino` | Tests requiring the `domino` package and Domino environment |
| `@pytest.mark.mlflow` | Tests requiring an MLflow tracking server |
| `@pytest.mark.integration` | End-to-end integration tests against a live service |

Tests marked `@pytest.mark.domino` are automatically skipped when the `domino` package is not installed.

### Unit test file inventory

| File | Tests | What it covers |
|---|---|---|
| `test_deployment_service.py` | 111 | `_is_valid_python_identifier`, `_safe_deployment_result` |
| `test_job_service.py` | 94 | Job validation, name normalization, config building, Domino status mapping |
| `test_schemas.py` | 54 | Pydantic request/response models, boundary validation |
| `test_config.py` | 53 | Settings resolution, `_is_truthy`, project name sanitization, API key priority |
| `test_data_profiler.py` | 44 | Column profiling, sampling strategies, semantic type inference |
| `test_ts_profiler.py` | 43 | Gap analysis, ADF stationarity, STL decomposition, ACF/PACF |
| `test_dataset_service.py` | 42 | Preview pagination, file handling, NaN/Inf coercion |
| `test_crud.py` | 34 | All DB CRUD operations (Job, JobLog, RegisteredModel) |
| `test_job_links.py` | 32 | Domino URL building, host normalization, experiment/registry links |
| `test_notebook_generator.py` | 27 | Tabular/timeseries/binary notebooks, preset normalization |
| `test_dataset_mounts.py` | 24 | Mount path parsing, deduplication, env var resolution |
| `test_error_handler.py` | 21 | `@handle_errors` decorator (HTTPException, 404, 400, 500 mapping) |
| `test_cleanup_service.py` | 21 | Orphan detection, artifact deletion, bulk cleanup |
| `test_api_jobs.py` | 21 | Job CRUD API endpoints (requires `domino`) |
| `test_api_profiling.py` | 12 | Profiling API endpoints (requires `domino`) |
| `test_api_health.py` | 9 | Health/readiness/user endpoints (requires `domino`) |
| `test_job_queue.py` | 7 | Queue status, enqueue, cancel, cancellation detection |
| `test_model_service.py` | 5 | `list_registered_models_response` with DB fixtures |

### Test report

The HTML report (`/mnt/artifacts/results/test_report_xxx.html` in Domino) is customized for fast triage:

- **Module summary table** at the top — one row per test file showing pass/fail/skip/error counts and duration, color-coded (green = all pass, red = failures, orange = all skipped)
- **Passing tests hidden by default** — the results table only shows failures, errors, and skips. Click the "Passed" checkbox to expand if needed.
- **Environment table removed** — no Python version / platform noise

When all tests pass, the report is a single screen: summary table + "0 Failed" banner.

### Unit test infrastructure

- **Database:** Each test gets a fresh async in-memory SQLite instance via the `async_engine` and `db_session` fixtures.
- **Synthetic data:** `conftest.py` provides fixtures for tabular (200 rows, mixed types, injected NaN), multiclass (300 rows), regression (250 rows), time series (multi-series and single-series), and Parquet files.
- **API client:** The `app_client` fixture provides an `httpx.AsyncClient` with `ASGITransport` against the FastAPI app, with DB dependency overrides for isolated testing.
- **Job factory:** The `make_job` fixture creates `Job` ORM instances with sensible defaults.
- **Auto-skip:** Tests marked `@pytest.mark.domino` are automatically skipped when the `domino` package is unavailable.

---

### Integration tests

The integration test suite (**44 tests**) runs against a live FastAPI service to validate the full lifecycle: profiling, training, metrics, model registration, and deployment. Tests run as a Domino Job; fixtures start the service as a subprocess and hit it over HTTP.

#### Running integration tests

```bash
# Full integration suite (runs as a Domino Job)
python -m pytest tests/integration/ -v --tb=long -x

# Locally (error path tests work without full Domino)
python -m pytest tests/integration/test_05_errors.py -v
```

| Flag | What it does |
|---|---|
| `-v` | Verbose output — prints each test name and result instead of just dots |
| `--tb=long` | On failure, shows the full Python traceback (default is `short`) |
| `-x` | Stop on first failure — useful for ordered integration tests where later tests depend on earlier ones |

#### Integration test file inventory

| File | Tests | What it covers |
|---|---|---|
| `test_00_health.py` | 4 | Health, readiness, user context, root endpoint |
| `test_01_profiling.py` | 8 | Tabular + TS profiling, suggest-target, presets, metrics, error paths |
| `test_02_training.py` | 10 | Local tabular + TS training, Domino Job training, metrics, leaderboard |
| `test_03_registry.py` | 6 | Register from job, list models, versions, stage transitions, direct register |
| `test_04_deployment.py` | 4 | List Model APIs, list deployments, deploy-from-job, deployment details |
| `test_05_errors.py` | 12 | Bad files, missing fields, 404s, cancel completed, invalid formats, duplicates |

Numeric prefixes enforce collection order — later tests depend on earlier ones via a session-scoped `shared_state` dict.

#### Integration test design

- **Service startup:** Session-scoped fixture starts `uvicorn app.main:app` as a subprocess on port 9876 (configurable via `INTTEST_SERVICE_PORT`), polls `GET /svc/v1/health` until ready (120s timeout). Teardown sends SIGTERM. Port 9876 is used by default to avoid conflicts with the main app on port 8000.
- **HTTP client:** Synchronous `httpx.Client` pointing at `localhost:{INTTEST_SERVICE_PORT}` with a `domino-username` header from `DOMINO_STARTING_USERNAME`.
- **Test data:** Session-scoped fixtures generate small synthetic CSVs (500-row tabular, 2-series x 180-day time series) written to `/mnt/data/{project}/datasets/integration_test/` (Domino) or `local_data/datasets/integration_test/` (local).
- **Shared state:** Session-scoped mutable dict passes resource IDs between ordered test files (e.g., `tabular_job_id` from test_02 feeds test_03). Downstream tests skip if required keys are missing.
- **Unique names:** All resources use `inttest_{YYYYMMDD_HHMMSS}_{label}` to avoid collisions between runs.
- **Cleanup:** Session teardown deletes resources in reverse dependency order (deployments, Model APIs, registered models, jobs, data files). All cleanup is best-effort.
- **Conditional skips:** Domino-only tests skip when `DOMINO_API_KEY` is not set. Registry/deployment tests skip when upstream training didn't complete.

#### Polling timeouts

| Operation | Timeout | Interval |
|---|---|---|
| Service startup | 120s | 5s |
| Local tabular training (500 rows) | 600s | 10s |
| Local TS training (360 rows) | 600s | 10s |
| Domino Job training | 900s | 15s |
| Deployment startup | 600s | 15s |
