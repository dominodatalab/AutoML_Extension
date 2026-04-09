# AutoML Extension — Design Document

---

## 1. Problem Statement

Data analysts and business users often depend on centralized data science teams to build, evaluate, and deploy ML models. This bottleneck slows decision-making and limits who can leverage ML across the organization.

**AutoML** democratizes machine learning by providing a no-code interface for training, evaluating, and deploying models — directly inside Domino. The target persona is Domino users who need ML capabilities but aren't data scientists: analysts, domain experts, and business stakeholders.

---

## 2. Solution Overview

The AutoML Extension is a full-stack web application that runs as a Domino App. It guides users through the complete ML lifecycle without writing code.

### User Journey

```
  1. Select Data
          │
          ▼
  2. Configure Training
          │
          ▼
  3. Train and Evaluate Models
          │
          ▼
  4. Deploy / Export
  5. Review Data
```

1. **Select data** — browse your Domino Datasets
2. **Train** — configure target column, problem type, and time budget; AutoGluon trains and ensembles models
3. **Evaluate** — leaderboard, feature importance, SHAP explanations, residual plots
4. **Deploy / Export** — three paths to production:
   - **Model API** — create Domino Model APIs with versioning, scaling, and lifecycle management
   - **Model Registry** — push to Domino Model Registry
   - **Export** — download as a reproducible Jupyter notebook
5. **Review Data**
   - Review the data used in the Exploratory Data Exploration view
   - Run EDA job to complete analysis for large datasets
   - Export IPython Notebook to implement cleaning

### Architecture (High-Level)

![Architecture Diagram](architecture-high-level.png)

---

## 3. Architecture & Design

The extension runs a FastAPI backend and a Vite + React frontend. The frontend hits the backend in order to retrieve data
to populate the UI. Only the backend sends requests to Domino APIs for security reasons.

**Training Job**

When you select "New Training job", this launches a model training job. The model training job only runs as a Domino Job.
Users can view the logs and job status as it runs. After the training job finishes, the user can review Autogluon generated
information in the other tabs of the job overview UI.

**Data Exploration View**

This view shows a preview of the selected data, allows EDA job launching, review of an analysis of the data, and Ipython
Notebook export functionality. The exported notebook file contains data transformations selected by the user in the
Transformations tab.

**EDA Job**

The EDA Job may run locally or as a Domino Job. It launches from the Data Exploration view. It computes reports on typical
EDA statistics that a Data Scientist would want to know.

**App File Structure Overview**

```
automl-service/          FastAPI backend (Python, AutoGluon, MLflow, Domino services)
automl-ui/               React frontend (TypeScript, Vite, Tailwind CSS)
docs/                    Documentation and design references
style-guide/             Domino design system reference
app.sh                   Startup script for Domino Apps
Dockerfile               Dockerfile layer the extension's/training job's/EDA job's/Model API Domino Environment
```

### 3.1 Frontend (`automl-ui/`)

| Aspect | Detail |
|--------|--------|
| Framework | React 18 + TypeScript 5.9 |
| Build tool | Vite 5 |
| Styling | Tailwind CSS 3.4 with Domino design tokens (`domino-*`) |
| State | Zustand (client), TanStack React Query (server) |
| Routing | React Router v6 with dynamic `basename` detection |

**File structure** — 

| Layer | Purpose |
|-------|-------|---------|
| `src/pages/` | Dashboard, NewJob wizard, JobDetail, EDA Analysis |
| `src/components/` | Common UI, wizard steps, diagnostics, charts, EDA |
| `src/hooks/` | Data fetching (jobs, datasets, models, diagnostics, profiling, progress) |
| `src/utils/` | Formatters, notebook generator, error handling, path utils |
| `src/api/` | Fetch-based API client with Domino endpoint mapping |
| `src/types/` | TypeScript type definitions |

### 3.2 Backend (`automl-service/`)

| Aspect | Detail |
|--------|--------|
| Framework | FastAPI (async) on Uvicorn |
| Python | 3.10+ |
| Database | SQLite via SQLAlchemy 2.0 + aiosqlite (async) |
| ML engine | AutoGluon 1.1+ (tabular + time series) |
| HTTP client | Generated Domino API clients and httpx for Domino API calls |

**File structure** — 

| Layer | Purpose |
|-------|-------|---------|
| `app/api/routes/` | REST endpoints + WebSocket |
| `app/api/schemas/` | Pydantic request/response models |
| `app/core/` | Predictions, diagnostics, export, profiling, MLflow, Domino integration |
| `app/core/trainers/` | Base, callbacks, tabular, and timeseries training |
| `app/db/` | SQLAlchemy models, async CRUD, migrations |
| `app/workers/` | Background training and EDA orchestration |

---

## 4. Domino Integration Surface

This section details everything the extension requires from the Domino platform.

### 4.1 Environment Variables

> **Criticality levels**:
> - **Required** — App cannot function in Domino without this. Framework must inject it.
> - **Recommended** — Core features degrade without this. Framework should inject it.
> - **Optional** — Enables specific features or overrides defaults. Inject if applicable.

#### Development Configuration

See [Dev Environment Variable File](../.env-dev-example)

#### Production Authentication

Authentication in the training and EDA jobs occurs via infrastructure in Domino.

#### Compute Configuration

| Variable | Source | Criticality | Default | Purpose | When Missing |
|----------|--------|-------------|---------|---------|-------------|
| `DOMINO_ENVIRONMENT_ID` | Extension | Required | `None` | Environment ID for job launching | ... |
| `DOMINO_ENVIRONMENT_REVISION_ID` | Extension | Required | `None` | Environment revision ID job launching | ... |

#### Database

| Variable | Source | Criticality | Default | Purpose | When Missing |
|----------|--------|-------------|---------|---------|-------------|
| `DATABASE_URL` | Extension | Required | File system's local directory | URI for the sqlite database. Required in production | Defaults to file system's local directory |

#### MLflow

| Variable | Source | Criticality | Default | Purpose | When Missing |
|----------|--------|-------------|---------|---------|-------------|
| `MLFLOW_TRACKING_URI` | Extension | Required | `None` | Mlflow tracking URI for mlflow interactions | Uses Domino default. Can be set for local development |
| `MLFLOW_TRACKING_TOKEN` | Extension | Optional | `None` | The access token for authenticating requests to Mlflow | Defaults to the user's access-token |

### 4.2 Authentication Flow

The extension uses the access token found in the Authorization header of requests to the backend.

---

## 5. Deployment Model

The extension runs as a single Docker container serving both frontend and backend:

`app.sh` supports four modes:

| Mode | Flag | Use Case |
|------|------|----------|
| Combined | `--all` (default) | Production: builds frontend, serves everything on one port |
| Backend only | `--backend` | When frontend is served separately |
| Frontend only | `--frontend` | Vite dev server for frontend development |
| Dev | `--dev` | Backend + Vite dev server with HMR |
| Prod | `--prod` | Meant for use when running in Domino. Uses pre-built assets and installation in Domino Environment. Use `app_prod.sh` when deploying the App in Domino |
