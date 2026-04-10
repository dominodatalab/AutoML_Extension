# AutoML Studio

A full-stack AutoML platform built on [AutoGluon](https://auto.gluon.ai/) and [Domino Data Lab](https://www.dominodatalab.com/). Provides a web UI for training, evaluating, and deploying ML models across tabular and time series data types.

## Architecture & Design

See the [Extension Design document](./docs/extension-design.md).

## Quick Start

### Prerequisites

- Python 3.11 (recommended for AutoGluon compatibility)
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) (recommended for Python dependency installation)

### Install dependencies

```bash
cd automl-service

# Recommended: uv for Python dependencies
pip install uv
uv venv ../.venv
VIRTUAL_ENV=../.venv uv pip install -r requirements-dev.txt -r requirements.txt

cd ../automl-ui
npm install
```

### Run the app in development

From the repository root:

```bash
./app.sh --dev
```

### Domino deployment

Run the `app_prod.sh` script, which starts both backend and frontend as a combined Domino App.

## Service Docs

- Backend setup, local development, generated-client rebuilds, and testing: [automl-service/README.md](./automl-service/README.md)
- Frontend install, development, and production build details: [automl-ui/README.md](./automl-ui/README.md)

## License

MIT License
