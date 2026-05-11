# AutoML UI

React frontend for the AutoML Extension. Built with Vite, TypeScript, Tailwind CSS, React Query, and Zustand.

## Setup

### Install dependencies

```bash
cd automl-ui
npm install
```

## Development

### Frontend only

From the repository root:

```bash
FRONTEND_PORT=3000 BACKEND_PORT=8000 ./app.sh --frontend
```

This starts the Vite dev server and points it at the backend on `BACKEND_PORT`.

### Full-stack development

From the repository root:

```bash
./app.sh --dev
```

This starts the backend and frontend together.

## Production Build

```bash
cd automl-ui
npm run build
```

For manual production installation as a Domino Extension, see [../INSTALL.md](../INSTALL.md). For Domino runtime, use `./app_prod.sh` or `./app.sh --prod` from the repository root so the backend can serve the built frontend assets.
