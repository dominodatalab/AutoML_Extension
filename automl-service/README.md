# AutoML Service

Backend service for the AutoML Extension, powered by [AutoGluon](https://auto.gluon.ai/) with [Domino Data Lab](https://www.dominodatalab.com/) integration. Provides automated machine learning for tabular data (binary classification, multiclass classification, regression) and time series forecasting.

## Setup

See the [main README](../README.md) for the top-level quick start. Frontend-specific instructions live in [../automl-ui/README.md](../automl-ui/README.md).

### Install dependencies

From `automl-service/`:

```bash
# Recommended: uv for Python dependencies
pip install uv
uv venv ../.venv
VIRTUAL_ENV=../.venv uv pip install -r requirements-dev.txt -r requirements.txt

# Alternative: pip only
pip install -r requirements-dev.txt -r requirements.txt
```

### Development configuration

From the repository root, create a local env file and populate the Domino values needed for local development:

```bash
cp .env-dev-example .env-dev
source .env-dev
```

The local development flow typically requires these values:

- `DOMINO_API_HOST`
- `DEV_ACCESS_TOKEN`
- `DOMINO_ENVIRONMENT_ID`
- `DOMINO_ENVIRONMENT_REVISION_ID`
- `MLFLOW_TRACKING_URI`
- `MLFLOW_TRACKING_TOKEN`

`DOMINO_ENVIRONMENT_ID` and `DOMINO_ENVIRONMENT_REVISION_ID` are required when local development needs to launch remote Domino Jobs for training or async Exploratory Data Analysis.

### Running the backend

Backend only, from the repository root:

```bash
source .env-dev
PORT=8000 ./app.sh --backend
```

Full-stack development, from the repository root:

```bash
source .env-dev
./app.sh --dev
```

### Production / Domino runtime

For manual production installation as a Domino Extension, see [../INSTALL.md](../INSTALL.md).

From the repository root:

```bash
./app_prod.sh
```

This starts the backend and serves the built frontend assets using the dependencies already installed in the Domino environment.

### Build Generated Domino Clients

```bash
# Download swagger specs
(cd automl-service && export OUT_PATH=./app/api/downloaded_openapi_specs/ && mkdir -p "$OUT_PATH" && ./scripts/download_api_specs.sh)

echo "then pick what you want and put into automl-service/app/api/domino_public_spec.json and automl-service/app/api/domino_private_spec.json"

# Generate public API client
(cd automl-service && OUT_PATH=./app/api/generated IN_PATH=./app/api/domino_public_spec.json ./scripts/generate_api_client.sh)

# Generate private API client
(cd automl-service && OUT_PATH=./app/api/generated_private IN_PATH=./app/api/domino_private_spec.json ./scripts/generate_api_client.sh)
```

### Retrieving `DEV_ACCESS_TOKEN`

Retrieve it from your Account Settings in Domino, or from a Domino Workspace/App terminal:

```bash
curl localhost:8899/access-token
```

## Synthetic Test Data

Generate synthetic datasets for manual testing:

```bash
python scripts/generate_synthetic_test_datasets.py
```

This creates 10 datasets under `local_data/datasets/synthetic_generated_suite/` covering binary classification, multiclass classification, regression, and time series forecasting in both small and large sizes.

---

## Testing

The test suite covers the entire backend with **663 unit tests** and **35 integration tests**.

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

When running as a Domino Job, all environment variables and the `domino` package are available, so all 663 unit tests will execute. The HTML report is written to `/mnt/artifacts/results/test_report_xxx.html` and visible in the Domino Job results tab.

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
