# Domino AutoML Oil and Gas Demo

An AutoGluon on Domino Data Lab Demo for oil & gas use cases.

## Components

### 1. Notebooks (`notebooks/`)
Jupyter notebooks demonstrating **AutoGluon model types** with comprehensive EDA, visualizations, and advanced features:

| Notebook | Data Type | Model Type | Use Case |
|----------|-----------|------------|----------|
| `01_tabular_predictive_maintenance/` | **Tabular** | TabularPredictor | Equipment failure prediction (multi-class classification) |
| `02_timeseries_production_forecast/` | **Time Series** | TimeSeriesPredictor | Multi-well oil production forecasting |
| `03_multimodal_defect_detection/` | **Images** | MultiModalPredictor | Visual equipment inspection (binary classification) |
| `04_tabular_yield_prediction/` | **Tabular** | TabularPredictor | Chemical process yield prediction (regression) |

Each notebook includes:
- **Synthetic data generation** for realistic use cases
- **Comprehensive EDA** with 10+ visualizations (distributions, correlations, pair plots)
- **Advanced AutoGluon features**: Multi-layer stacking, bagging, custom hyperparameters
- **Model leaderboard** comparing all trained models
- **Feature importance** analysis (permutation-based)
- **Prediction analysis** (residuals, error distribution, actual vs predicted)
- **Domino MLflow tracking** for experiment management
- **Model registry** integration for deployment
- **Containerized deployment** with Dockerfile and FastAPI

### 2. AutoML Service (`automl-service/`)
FastAPI service exposing AutoGluon functionality:

- **Training Jobs**: Create, monitor, and manage AutoGluon training jobs
- **Dataset Management**: Upload files or connect to Domino datasets
- **Model Registry**: Register and deploy trained models
- **Experiment Tracking**: MLflow integration with Domino

### 3. AutoML UI (`automl-ui/`)
React TypeScript application styled like Domino Data Lab:

- **Dashboard**: View and manage training jobs
- **Training Wizard**: 4-step workflow for creating training jobs
- **Job Details**: Monitor training progress, view metrics and logs
- **Model Deployment**: Deploy models to Domino Model API

## Quick Start

### Running the Service

```bash
cd automl-service
pip install -r requirements.txt
python model_api.py
```

The API will be available at `http://localhost:8000`.

### Running the UI

```bash
cd automl-ui
npm install
npm run dev
```

The UI will be available at `http://localhost:3000`.

### Running Notebooks

```bash
cd notebooks
pip install -r requirements.txt
jupyter notebook
```

## API Endpoints

### Jobs
- `POST /api/v1/jobs` - Create training job
- `GET /api/v1/jobs` - List jobs
- `GET /api/v1/jobs/{id}` - Get job details
- `GET /api/v1/jobs/{id}/status` - Get job status
- `GET /api/v1/jobs/{id}/logs` - Get job logs
- `POST /api/v1/jobs/{id}/cancel` - Cancel job

### Datasets
- `GET /api/v1/datasets` - List Domino datasets
- `POST /api/v1/datasets/upload` - Upload file
- `GET /api/v1/datasets/{id}/preview` - Preview data
- `GET /api/v1/datasets/{id}/schema` - Get column schema

### Models
- `GET /api/v1/models` - List registered models
- `POST /api/v1/models/{name}/deploy` - Deploy model

## Training Wizard Steps

1. **Data Source**: Upload CSV/Parquet or select Domino dataset
2. **Model Type**: Choose Tabular, TimeSeries, or Multimodal
3. **Configuration**: Set target column, preset, time limit
4. **Review**: Confirm and start training

## Domino Integration

- **Datasets**: Access via Domino SDK (`dominodatalab` package)
- **Experiments**: MLflow tracking with Domino integration
- **Model Registry**: Register models via MLflow
- **Deployment**: Deploy as Domino Model API

### Environment Variables

```bash
DOMINO_USER_API_KEY     # Domino API key
DOMINO_API_HOST         # Domino API endpoint
DOMINO_PROJECT_ID       # Current project ID
MLFLOW_TRACKING_URI     # MLflow tracking server
```

## Technology Stack

### Backend
- Python 3.10+
- FastAPI
- SQLAlchemy + SQLite
- AutoGluon (Tabular, TimeSeries, Multimodal)
- MLflow
- Domino SDK

### Frontend
- React 18
- TypeScript
- Vite
- Tailwind CSS
- Zustand (state management)
- React Query

## Project Structure

```
domino-automl/
├── notebooks/
│   ├── requirements.txt
│   ├── 01_tabular_predictive_maintenance/
│   │   ├── predictive_maintenance.ipynb
│   │   └── deployment/
│   ├── 02_timeseries_production_forecast/
│   │   ├── production_forecasting.ipynb
│   │   └── deployment/
│   ├── 03_multimodal_defect_detection/
│   │   ├── defect_detection.ipynb
│   │   └── deployment/
│   └── 04_tabular_yield_prediction/
│       ├── yield_prediction.ipynb
│       └── deployment/
├── automl-service/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── core/
│   │   ├── db/
│   │   └── workers/
│   ├── requirements.txt
│   └── Dockerfile
├── automl-ui/
    └── src/
        ├── components/
        ├── pages/
        ├── hooks/
        └── store/

```

## License

MIT License
