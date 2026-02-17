# AutoML Studio

A full-stack AutoML platform built on [AutoGluon](https://auto.gluon.ai/) and [Domino Data Lab](https://www.dominodatalab.com/). Provides a web UI for training, evaluating, and deploying ML models across tabular and time series data types.

## Architecture

```
automl-service/          FastAPI backend (Python 3.11, AutoGluon 1.5, MLflow)
automl-ui/               React frontend (TypeScript, Vite, Tailwind CSS)
sample_projects/         Example datasets (customer churn)
app.sh                   Combined startup script for Domino Apps
Dockerfile               Container build for Domino deployment
```

### Backend (`automl-service/`)

**~11,400 LOC** across 43 Python files. Async FastAPI with SQLAlchemy ORM, AutoGluon ML, and MLflow tracking.

| Layer | Files | Purpose |
|-------|-------|---------|
| `app/api/routes/` | 9 routers | REST endpoints (50+ routes) + WebSocket |
| `app/api/schemas/` | 3 files | Pydantic request/response models |
| `app/core/` | 12 services | Predictions, diagnostics, export, MLflow, Domino integration |
| `app/core/trainers/` | 3 trainers | Tabular and timeseries training (split from monolithic runner) |
| `app/db/` | 3 files | SQLAlchemy models, async CRUD, migrations |
| `app/workers/` | 1 file | Background training orchestration |

### Frontend (`automl-ui/`)

**~13,500 LOC** across 70 TypeScript files. React 18 with React Query for server state and Zustand for UI state.

| Layer | Files | Purpose |
|-------|-------|---------|
| `src/pages/` | 4 pages | Dashboard, NewJob wizard, JobDetail, EDA Analysis |
| `src/components/` | 37 components | Common UI, wizard steps, diagnostics, charts, EDA |
| `src/hooks/` | 10 hooks | Data fetching (jobs, datasets, models, diagnostics, progress) |
| `src/utils/` | 3 files | Shared formatters, notebook generator, error handling |
| `src/api/` | 4 files | Fetch-based API client with Domino endpoint mapping |
| `src/types/` | 8 files | TypeScript type definitions |

## Features

- **Training Wizard**: 4-step workflow (data source, model type, configuration, review) with advanced AutoGluon config (bagging, stacking, HPO, pseudo-labeling, distillation)
- **Dual Training Execution**: Run training in the in-app queue (`local`) or as an external Domino Job (`domino_job`)
- **Model Diagnostics**: Feature importance, leaderboard, confusion matrix, ROC/PR curves, SHAP explanations, learning curves
- **Exploratory Data Analysis**: Interactive data profiling, column explorer, correlation matrix, data quality checks, notebook export, optional async Domino Job execution
- **Dataset Management**: Upload CSV/Parquet or connect to Domino Datasets
- **Model Registry**: MLflow integration for versioning and stage transitions
- **Model Export**: ONNX, PMML, and pickle formats
- **Deployment**: Deploy trained models to Domino Model APIs
- **Experiment Tracking**: MLflow logging of per-model hyperparameters, metrics, and artifacts
- **Real-time Progress**: WebSocket-based training progress updates

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

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/jobs` | Create training job |
| GET | `/svc/v1/jobs` | List jobs (filter by status, owner, project) |
| GET | `/svc/v1/jobs/{id}` | Get job details |
| DELETE | `/svc/v1/jobs/{id}` | Delete job |
| POST | `/svc/v1/jobs/{id}/cancel` | Cancel running job |
| GET | `/svc/v1/jobs/{id}/progress` | Get training progress |
| GET | `/svc/v1/jobs/{id}/logs` | Get job logs |
| POST | `/svc/v1/jobs/{id}/register` | Register model to MLflow |
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
| GET | `/svcdatasets` | Domino-compatible single-segment dataset list route |

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
| GET | `/svc/v1/predictions/model/{model_id}/info` | Get loaded model info |
| DELETE | `/svc/v1/predictions/model/{model_id}/unload` | Unload model from memory |
| GET | `/svc/v1/predictions/models/loaded` | List loaded models |

### Registry & Export
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/svc/v1/registry/register` | Register model to MLflow |
| GET | `/svc/v1/registry/models` | List registered models |
| POST | `/svc/v1/export/export/onnx` | Export to ONNX |
| POST | `/svc/v1/export/export/deployment` | Export deployment bundle |
| POST | `/svc/v1/export/export/notebook` | Export notebook |
| GET | `/svc/v1/export/export/formats` | List export formats |

### Deployments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/svc/v1/deployments/model-apis` | List model APIs |
| POST | `/svc/v1/deployments/model-apis` | Create model API |
| GET | `/svc/v1/deployments/deployments` | List deployments |
| POST | `/svc/v1/deployments/deployments` | Create deployment |
| POST | `/svc/v1/deployments/quick-deploy` | Create API + version + deployment in one call |
| POST | `/svc/v1/deployments/deploy-from-job/{job_id}` | Deploy from completed AutoML job |

### Domino Compatibility Routes

For Domino proxy constraints, the backend also exposes single-segment `/svc*` routes (examples):

- `POST /svcjobcreate`
- `POST /svcjobprogress`
- `POST /svcprofileasyncstart`
- `POST /svcprofileasyncstatus`
- `GET /svcdeployments`

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
`<safe_project_name>` resolves in this order: `DOMINO_PROJECT_NAME` -> `DOMINO_PROJECT_ID` -> `default_project`,
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
- **Tailwind CSS 3.4** (utility-first styling)
- **TanStack React Query 5** (server state)
- **Zustand 4** (UI state)
- **Recharts 2** (charting)
- **Headless UI** + **Heroicons** (accessible components)

## License

MIT License
