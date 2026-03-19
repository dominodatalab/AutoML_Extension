# AutoML Studio

A full-stack AutoML platform built on [AutoGluon](https://auto.gluon.ai/) and [Domino Data Lab](https://www.dominodatalab.com/). Provides a web UI for training, evaluating, and deploying ML models across tabular and time series data types.

## Architecture

```
automl-service/          FastAPI backend (Python 3.11, AutoGluon 1.5, MLflow)
automl-ui/               React frontend (TypeScript, Vite, Tailwind CSS)
docs/                    Documentation and design references
style-guide/             Domino design system reference
app.sh                   Combined startup script for Domino Apps
Dockerfile               Container build for Domino deployment
```

### Backend (`automl-service/`)

**~16,600 LOC** across 73 Python files. Async FastAPI with SQLAlchemy ORM, AutoGluon ML, and MLflow tracking.

| Layer | Files | Purpose |
|-------|-------|---------|
| `app/api/routes/` | 8 routers | REST endpoints (107 routes) + WebSocket |
| `app/api/compat/` | pattern-based | 66 single-segment `/svc*` Domino proxy routes |
| `app/api/schemas/` | 3 files | Pydantic request/response models |
| `app/core/` | 18 services | Predictions, diagnostics, export, profiling, MLflow, Domino integration |
| `app/core/trainers/` | 4 trainers | Base, callbacks, tabular, and timeseries training |
| `app/db/` | 3 files | SQLAlchemy models, async CRUD, migrations |
| `app/workers/` | 3 files | Background training and EDA orchestration |

### Frontend (`automl-ui/`)

**~15,700 LOC** across 98 TypeScript files. React 18 with Zustand for UI state.

| Layer | Files | Purpose |
|-------|-------|---------|
| `src/pages/` | 4 pages | Dashboard, NewJob wizard, JobDetail, EDA Analysis |
| `src/components/` | 58 components | Common UI, wizard steps, diagnostics, charts, EDA |
| `src/hooks/` | 13 hooks | Data fetching (jobs, datasets, models, diagnostics, profiling, progress) |
| `src/utils/` | 6 files | Formatters, notebook generator, error handling, path utils |
| `src/api/` | 3 files | Fetch-based API client with Domino endpoint mapping |
| `src/types/` | 8 files | TypeScript type definitions |

## Features

- **Training Wizard**: 4-step workflow (data source, model type, configuration, review) with advanced AutoGluon config (bagging, stacking, HPO, pseudo-labeling, distillation)
- **Dual Training Execution**: Run training in the in-app queue (`local`) or as an external Domino Job (`domino_job`)
- **Model Diagnostics**: Feature importance, leaderboard, confusion matrix, ROC/PR curves, regression diagnostics, learning curves, model comparison
- **Exploratory Data Analysis**: Interactive data profiling, column explorer, correlation matrix, data quality checks, time series profiling (ACF/PACF, stationarity, decomposition), notebook export, optional async Domino Job execution
- **Dataset Management**: Upload CSV/Parquet or connect to Domino Datasets
- **Model Registry**: MLflow integration for versioning, stage transitions, model cards, and downloads
- **Model Export**: deployment bundle and notebook formats
- **Deployment**: Deploy trained models to Domino Model APIs with full lifecycle management (create, start, stop, delete)
- **Experiment Tracking**: MLflow logging of per-model hyperparameters, metrics, and artifacts
- **Real-time Progress**: WebSocket-based training progress updates
- **Job Management**: Queue status, bulk cleanup, orphan detection

## Quick Start

### Prerequisites

- Python 3.11 (recommended for AutoGluon compatibility)
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) (recommended for Python dependency installation)

### Backend

```bash
cd automl-service

# Option A: Using uv (recommended — handles AutoGluon's 200+ transitive deps)
pip install uv
VIRTUAL_ENV=../.venv uv pip install -r requirements.txt

# Option B: Using pip (may hit resolution-too-deep on complex dep graphs)
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd automl-ui
npm install
npm run dev        # Dev server on http://localhost:5173
npm run build      # Production build
```

### Domino Deployment

The `app.sh` script starts both backend and frontend as a combined Domino App:
```bash
# Runs automatically when deployed as a Domino App
./app.sh
```

### Training Execution Modes

Training requests support two execution targets:

- `local` (default): Runs in the app process using the in-app queue
- `domino_job`: Launches an external Domino Job via `python-domino`

Both modes are available from the UI wizard and API payloads via:

- `execution_target`: `"local"` or `"domino_job"`
- `run_as_domino_job`: legacy boolean alias for external execution

### Async EDA Profiling

EDA supports both synchronous and asynchronous profiling:

- Synchronous: profile in-app and return results immediately
- Asynchronous: launch an external Domino Job, then poll for status/results

Async endpoints:

- `POST /svc/v1/profiling/profile/async/start`
- `POST /svc/v1/profiling/profile/async/status`
- `GET /svc/v1/profiling/profile/async/{request_id}`

## API Reference

### Health
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/svc/v1/health` | Basic health check |
| GET | `/svc/v1/health/ready` | Readiness check with DB validation |
| GET | `/svc/v1/health/user` | Get current user context |

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/jobs` | Create training job |
| GET | `/svc/v1/jobs` | List jobs (filter by status, owner, project) |
| POST | `/svc/v1/jobs/list` | List jobs (POST variant with filters in body) |
| GET | `/svc/v1/jobs/{id}` | Get job details |
| GET | `/svc/v1/jobs/{id}/status` | Get job status |
| GET | `/svc/v1/jobs/{id}/metrics` | Get job metrics |
| GET | `/svc/v1/jobs/{id}/progress` | Get training progress |
| GET | `/svc/v1/jobs/{id}/logs` | Get job logs |
| POST | `/svc/v1/jobs/{id}/cancel` | Cancel running job |
| DELETE | `/svc/v1/jobs/{id}` | Delete job |
| POST | `/svc/v1/jobs/{id}/register` | Register model to MLflow |
| GET | `/svc/v1/jobs/queue/status` | Get queue status |
| GET | `/svc/v1/jobs/cleanup/preview` | Preview cleanup candidates |
| POST | `/svc/v1/jobs/cleanup` | Bulk cleanup jobs |
| POST | `/svc/v1/jobs/cleanup/orphans` | Delete orphaned jobs |
| WS | `/ws/jobs/{id}` | Real-time progress updates |

### Datasets
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/svc/v1/datasets` | List local datasets |
| POST | `/svc/v1/datasets/upload` | Upload CSV/Parquet |
| GET | `/svc/v1/datasets/{id}` | Get dataset metadata |
| GET | `/svc/v1/datasets/{id}/preview` | Preview rows |
| GET | `/svc/v1/datasets/{id}/schema` | Get inferred schema |
| POST | `/svc/v1/datasets/preview` | Preview by direct file path |

### Profiling
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/profiling/profile` | Full data profiling |
| POST | `/svc/v1/profiling/profile/quick` | Quick profile (summary stats only) |
| POST | `/svc/v1/profiling/profile/suggest-target` | Suggest target column |
| POST | `/svc/v1/profiling/profile/column/{name}` | Profile single column |
| POST | `/svc/v1/profiling/profile/timeseries` | Time series profiling (ACF/PACF, stationarity, decomposition) |
| GET | `/svc/v1/profiling/profile/metrics` | List available metrics by problem type |
| GET | `/svc/v1/profiling/profile/presets` | List available presets by model type |
| POST | `/svc/v1/profiling/profile/async/start` | Start async profiling as Domino Job |
| POST | `/svc/v1/profiling/profile/async/status` | Poll async profiling status |
| GET | `/svc/v1/profiling/profile/async/{id}` | Get async profiling result |

### Model Diagnostics
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/predictions/model/feature-importance` | Feature importance |
| POST | `/svc/v1/predictions/model/leaderboard` | Model leaderboard |
| POST | `/svc/v1/predictions/model/confusion-matrix` | Confusion matrix |
| POST | `/svc/v1/predictions/model/roc-curve` | ROC curve |
| POST | `/svc/v1/predictions/model/precision-recall` | PR curve |
| POST | `/svc/v1/predictions/model/regression-diagnostics` | Regression diagnostics |

### Predictions
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/predictions/predict` | Single prediction |
| POST | `/svc/v1/predictions/predict/batch` | Batch prediction |
| GET | `/svc/v1/predictions/model/{id}/info` | Get loaded model info |
| DELETE | `/svc/v1/predictions/model/{id}/unload` | Unload model from memory |
| GET | `/svc/v1/predictions/models/loaded` | List loaded models |

### Registry
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/registry/register` | Register model to MLflow |
| GET | `/svc/v1/registry/models` | List registered models |
| GET | `/svc/v1/registry/models/mlflow` | List MLflow models |
| GET | `/svc/v1/registry/models/{name}/versions` | Get model versions |
| GET | `/svc/v1/registry/models/{name}/stages` | Get model by stage |
| GET | `/svc/v1/registry/models/{name}/versions/{v}/uri` | Get model URI |
| POST | `/svc/v1/registry/models/{name}/versions/{v}/download` | Download model |
| POST | `/svc/v1/registry/models/transition-stage` | Transition model stage |
| POST | `/svc/v1/registry/models/update-description` | Update model description |
| POST | `/svc/v1/registry/models/card` | Generate model card |
| DELETE | `/svc/v1/registry/models/{name}` | Delete model |
| DELETE | `/svc/v1/registry/models/{name}/versions/{v}` | Delete version |

### Export
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/export/export/deployment` | Export deployment bundle |
| POST | `/svc/v1/export/export/notebook` | Export notebook |
| GET | `/svc/v1/export/export/formats` | List export formats |
| POST | `/svc/v1/export/learning-curves` | Get learning curves |
| POST | `/svc/v1/export/compare-models` | Compare models |

### Deployments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/svc/v1/deployments/model-apis` | List model APIs |
| POST | `/svc/v1/deployments/model-apis` | Create model API |
| GET | `/svc/v1/deployments/model-apis/{id}` | Get model API |
| DELETE | `/svc/v1/deployments/model-apis/{id}` | Delete model API |
| GET | `/svc/v1/deployments/model-apis/{id}/versions` | List API versions |
| POST | `/svc/v1/deployments/model-apis/{id}/versions` | Create API version |
| GET | `/svc/v1/deployments/model-apis/{id}/versions/{vid}` | Get API version |
| GET | `/svc/v1/deployments/model-apis/{id}/versions/{vid}/logs` | Get build logs |
| GET | `/svc/v1/deployments/deployments` | List deployments |
| POST | `/svc/v1/deployments/deployments` | Create deployment |
| GET | `/svc/v1/deployments/deployments/{id}` | Get deployment |
| PATCH | `/svc/v1/deployments/deployments/{id}` | Update deployment |
| DELETE | `/svc/v1/deployments/deployments/{id}` | Delete deployment |
| POST | `/svc/v1/deployments/deployments/{id}/start` | Start deployment |
| POST | `/svc/v1/deployments/deployments/{id}/stop` | Stop deployment |
| GET | `/svc/v1/deployments/deployments/{id}/status` | Get deployment status |
| GET | `/svc/v1/deployments/deployments/{id}/logs/{type}` | Get deployment logs |
| GET | `/svc/v1/deployments/deployments/{id}/versions` | Get deployment versions |
| GET | `/svc/v1/deployments/deployments/{id}/credentials` | Get credentials |
| POST | `/svc/v1/deployments/quick-deploy` | Create API + version + deployment in one call |
| POST | `/svc/v1/deployments/deploy-from-job/{job_id}` | Deploy from completed AutoML job |

### Domino Compatibility Routes

For Domino proxy constraints, the backend also exposes 66 single-segment `/svc*` routes that mirror the RESTful API. Examples:

- `POST /svcjobcreate` → create job
- `POST /svcjobget` → get job details
- `POST /svcjobprogress` → get training progress
- `POST /svcprofile` → profile dataset
- `POST /svcprofiletimeseries` → time series profiling
- `POST /svcprofileasyncstart` → start async profiling
- `POST /svcprofileasyncstatus` → poll async status
- `POST /svcfeatureimportance` → feature importance
- `POST /svcleaderboard` → model leaderboard
- `POST /svcregistermodel` → register model to MLflow
- `POST /svcquickdeploy` → quick deploy
- `GET /svcdatasets` → list datasets
- `GET /svcdeployments` → list deployments
- `GET /svcmodelapis` → list model APIs

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | No | SQLite URL (default local: `sqlite:///./automl.db`, Domino: `sqlite:////mnt/data/<safe_project_name>/automl.db`) |
| `MODELS_PATH` | No | Model storage directory |
| `DATASETS_PATH` | No | Dataset storage directory |
| `UPLOADS_PATH` | No | Upload directory |
| `TEMP_PATH` | No | Temp directory |
| `EDA_RESULTS_PATH` | No | Shared EDA async result path |
| `DOMINO_API_PROXY` | Domino app | Domino proxy base URL used by API clients |
| `DOMINO_API_HOST` | Domino only | Domino API host |
| `DOMINO_API_KEY` | Optional | Domino API key (fallback auth) |
| `DOMINO_USER_API_KEY` | Optional | Legacy Domino API key |
| `DOMINO_TOKEN_FILE` | Optional | Token file path for Domino SDK/auth fallback |
| `API_KEY_OVERRIDE` | Optional | Explicit API key override (bypasses localhost token endpoint) |
| `DOMINO_PROJECT_ID` | Domino only | Current project ID |
| `DOMINO_PROJECT_NAME` | Domino only | Current project name |
| `DOMINO_PROJECT_OWNER` | Domino only | Current project owner |
| `DOMINO_TRAINING_HARDWARE_TIER_NAME` | Optional | Default hardware tier for external Domino training jobs |
| `DOMINO_TRAINING_ENVIRONMENT_ID` | Optional | Default environment for external Domino training jobs |
| `DOMINO_EDA_HARDWARE_TIER_NAME` | Optional | Default hardware tier for async EDA jobs |
| `DOMINO_EDA_ENVIRONMENT_ID` | Optional | Default environment for async EDA jobs |
| `MLFLOW_TRACKING_URI` | Domino only | MLflow tracking server |
| `MLFLOW_TRACKING_TOKEN` | Optional | MLflow auth token |
| `ENABLE_LOCAL_COMPUTE` | No | Enable local in-app queue execution (`true`/`false`) |
| `WORKERS` | No | Uvicorn worker count (use `1` for local queue mode) |

In Domino, default writable paths are scoped per project under `/mnt/data/<safe_project_name>/`.
`<safe_project_name>` resolves in this order: `DOMINO_PROJECT_NAME` -> `default_project`,
then non-path-safe characters are replaced with `_`.
Derived defaults:
- `MODELS_PATH`: `/mnt/data/<safe_project_name>/models`
- `DATASETS_PATH`: `/mnt/data/<safe_project_name>/datasets`
- `UPLOADS_PATH`: `/mnt/data/<safe_project_name>/uploads`
- `TEMP_PATH`: `/mnt/data/<safe_project_name>/temp`
- `EDA_RESULTS_PATH`: `/mnt/data/<safe_project_name>/eda_results`

## Technology Stack

### Backend
- **Python 3.11** with async FastAPI
- **AutoGluon 1.5** (Tabular, TimeSeries)
- **SQLAlchemy 2.0** + aiosqlite (async SQLite)
- **MLflow 3.9** for experiment tracking
- **Ray Tune** for hyperparameter optimization
- **PyTorch 2.9** (underlying ML framework)

### Frontend
- **React 18** with TypeScript
- **Vite 5** (build tool)
- **Tailwind CSS 3.4** (utility-first styling with custom Domino design tokens)
- **Zustand 4** (UI state)
- **Recharts 2** (diagnostics charts)
- **Heroicons** (icons)

# Local Development

## installation
See the individual service directories automl-service, automl-ui READMEs for installation instructions.

## development
You can develop this application locally by setting some environment variables, and running scripts and the dev servers.

```sh
source .env-dev # see .env-dev-example
# generate api client
cd automl-service && ./scripts/download_public_api_client.sh &&  ./scripts/generate_public_api_client

# run dev servers, option A
FRONTEND_PORT=3000 BACKEND_PORT=8000 ./app.sh --frontend
PORT=8000 ./app.sh --backend

# run dev servers, option B
./app.sh --dev
```

## Retrieving DEV_ACCESS_TOKEN

- start Domino workspace or App
- open a terminal. In workspace, this would be via vscode or jupyterlab (or many other notebook types)
- `curl localhost:8899/access-token`

## License

MIT License
