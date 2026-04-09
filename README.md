# AutoML Studio

A full-stack AutoML platform built on [AutoGluon](https://auto.gluon.ai/) and [Domino Data Lab](https://www.dominodatalab.com/). Provides a web UI for training, evaluating, and deploying ML models across tabular and time series data types.

## Architecture & Design

See the [Extension Design document](./docs/extension-design.md).

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
export VIRTUAL_ENV=../.venv uv pip install -r requirements-dev.txt -r requirements.txt
export UV_ENV_FILE=../.env-dev

# Option B: Using pip (may hit resolution-too-deep on complex dep graphs)
pip install -r requirements-dev.txt -r requirements.txt
source ../.env-dev

# Run the server
PORT=8000 ./app.sh --backend
```

### Frontend

```bash
cd automl-ui

npm install

# Run  dev server
FRONTEND_PORT=3000 BACKEND_PORT=8000 ./app.sh --frontend

npm run build      # Production build
```

### Run all dev servers

`./app.sh --dev`

### Domino Deployment

Run the `app_prod.sh` script,which starts both backend and frontend as a combined Domino App

### Build Generated Domino Clients

```sh
# download swagger specs
(cd automl-service && export OUT_PATH=./app/api/downloaded_openapi_specs/ && mkdir -p $OUT_PATH && ./scripts/download_api_specs.sh)

echo "then pick what you want and put into automl-service/app/api/domino_public_spec.json and automl-service/app/api/domino_private_spec.json"

# generate public api client
(cd automl-service && OUT_PATH=./app/api/generated IN_PATH=./app/api/domino_public_spec.json ./scripts/generate_api_client.sh)

# generate private api client
(cd automl-service && OUT_PATH=./app/api/generated_private IN_PATH=./app/api/domino_private_spec.json ./scripts/generate_api_client.sh)
```

### Retrieving DEV_ACCESS_TOKEN

Retrieve from you Account Settings in Domino.

Or

- start Domino workspace or App
- open a terminal. In workspace, this would be via vscode or jupyterlab (or many other notebook types)
- `curl localhost:8899/access-token`

## License

MIT License
