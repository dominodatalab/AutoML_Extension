#!/bin/bash
# AutoML Studio - Unified startup script
# Replaces: app.sh, automl-service/app.sh, automl-ui/app.sh, automl-ui/setup_app_preview.sh
#
# Usage:
#   ./app.sh              # Combined mode: build frontend + start backend serving everything
#   ./app.sh --backend    # Backend only (API server)
#   ./app.sh --frontend   # Frontend only (Vite dev server for development)
#   ./app.sh --dev        # Dev mode: backend + Vite dev server with HMR

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE="${1:---all}"

# Defaults
export HOST=${HOST:-0.0.0.0}
export BACKEND_PORT=${BACKEND_PORT:-8000}
export FRONTEND_PORT=${FRONTEND_PORT:-3000}
export PORT=${PORT:-8888}
export WORKERS=${WORKERS:-1}
export ENABLE_LOCAL_COMPUTE=${ENABLE_LOCAL_COMPUTE:-true}

# Detect Domino environment
IS_DOMINO=false
if [ -n "$DOMINO_RUN_ID" ]; then
    IS_DOMINO=true
fi

# ── Helpers ──────────────────────────────────────────────────────────

print_header() {
    echo "=========================================="
    echo "AutoML Studio - $1"
    echo "=========================================="
}

print_env() {
    echo "Domino Environment:"
    echo "  DOMINO_API_HOST: ${DOMINO_API_HOST:-NOT SET}"
    echo "  DOMINO_API_KEY: ${DOMINO_API_KEY:+SET (hidden)}"
    echo "  DOMINO_USER_API_KEY: ${DOMINO_USER_API_KEY:+SET (hidden)}"
    echo "  DOMINO_PROJECT_NAME: ${DOMINO_PROJECT_NAME:-NOT SET}"
    echo "  DOMINO_PROJECT_OWNER: ${DOMINO_PROJECT_OWNER:-NOT SET}"
    echo ""
}

is_truthy() {
    case "${1,,}" in
        1|true|yes|y|on) return 0 ;;
        *) return 1 ;;
    esac
}

validate_worker_config() {
    local workers="${WORKERS:-1}"
    local local_compute="${ENABLE_LOCAL_COMPUTE:-true}"

    if ! [[ "$workers" =~ ^[0-9]+$ ]] || [ "$workers" -lt 1 ]; then
        echo "ERROR: WORKERS must be a positive integer (received '$workers')."
        exit 1
    fi

    if is_truthy "$local_compute" && [ "$workers" -gt 1 ]; then
        echo "ERROR: Local compute is enabled but WORKERS=$workers."
        echo "Local queue state is process-local and unsafe with multiple API workers."
        echo "Set WORKERS=1, or set ENABLE_LOCAL_COMPUTE=false to force external execution only."
        exit 1
    fi
}

ensure_dirs() {
    mkdir -p /mnt/data/models 2>/dev/null || mkdir -p "${SCRIPT_DIR}/local_data/models"
    mkdir -p /mnt/data/datasets 2>/dev/null || mkdir -p "${SCRIPT_DIR}/local_data/datasets"
    mkdir -p /mnt/data/temp 2>/dev/null || mkdir -p "${SCRIPT_DIR}/local_data/temp"
    mkdir -p /mnt/automl-service/uploads 2>/dev/null || mkdir -p "${SCRIPT_DIR}/local_data/uploads"
}

ensure_node() {
    if command -v npm &> /dev/null; then
        return
    fi
    echo "npm not found, installing Node.js 20..."
    NODE_VERSION="v20.18.1"
    NODE_DIR="/tmp/node-${NODE_VERSION}-linux-x64"
    CURL=$(command -v curl || echo /opt/domino/bin/curl)
    if [ ! -d "$NODE_DIR" ]; then
        $CURL -sSL "https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz" -o /tmp/node.tar.xz
        tar -xf /tmp/node.tar.xz -C /tmp
        rm /tmp/node.tar.xz
    fi
    export PATH="${NODE_DIR}/bin:$PATH"
}

install_lightweight_deps() {
    pip install -q --no-deps aiosqlite aiofiles pydantic-settings python-multipart httpx 2>/dev/null || true
}

build_frontend() {
    echo "Building frontend..."
    cd "${SCRIPT_DIR}/automl-ui"
    ensure_node
    echo "Node.js: $(node --version), npm: $(npm --version)"
    npm install --silent
    npm run build

    # Generate runtime config (empty API_URL = same origin)
    cat > dist/config.js << 'JSEOF'
window.APP_CONFIG = { API_URL: "" };
JSEOF
    echo "Frontend built successfully"
    cd "$SCRIPT_DIR"
}

start_backend() {
    local port="${1:-$PORT}"
    local service_dir="${SCRIPT_DIR}/automl-service"

    # Use /mnt/code path if in Domino, otherwise local
    if [ -d "/mnt/code/automl-service" ]; then
        service_dir="/mnt/code/automl-service"
    fi

    cd "$service_dir"
    install_lightweight_deps

    if [ "${RELOAD:-false}" = "true" ]; then
        echo "Starting backend (dev mode with reload) on port $port..."
        exec uvicorn app.main:app --host "$HOST" --port "$port" --reload --log-level info
    else
        validate_worker_config
        echo "Starting backend on port $port..."
        exec uvicorn app.main:app --host "$HOST" --port "$port" --workers "$WORKERS" --log-level info
    fi
}

start_backend_background() {
    local port="${1:-$BACKEND_PORT}"
    local service_dir="${SCRIPT_DIR}/automl-service"

    if [ -d "/mnt/code/automl-service" ]; then
        service_dir="/mnt/code/automl-service"
    fi

    cd "$service_dir"
    install_lightweight_deps

    uvicorn app.main:app --host 127.0.0.1 --port "$port" --log-level warning &
    BACKEND_PID=$!
    echo "Backend started (PID: $BACKEND_PID) on port $port"

    # Wait for backend to be ready
    echo "Waiting for backend..."
    for i in $(seq 1 30); do
        if curl -s "http://127.0.0.1:$port/svc/v1/health" > /dev/null 2>&1; then
            echo "Backend ready!"
            return 0
        fi
        sleep 1
    done
    echo "ERROR: Backend failed to start within 30 seconds"
    exit 1
}

# ── Modes ────────────────────────────────────────────────────────────

case "$MODE" in
    --backend)
        print_header "Backend Only"
        print_env
        ensure_dirs
        start_backend "$PORT"
        ;;

    --frontend)
        print_header "Frontend Dev Server"
        cd "${SCRIPT_DIR}/automl-ui"
        ensure_node

        # Set base path for Domino workspace proxy
        if [ "$IS_DOMINO" = true ]; then
            export VITE_BASE_PATH="/notebookSession/${DOMINO_RUN_ID}/proxy/${FRONTEND_PORT}/"
            export VITE_API_URL="/notebookSession/${DOMINO_RUN_ID}/proxy/${BACKEND_PORT}"
            echo "Domino workspace mode: $VITE_BASE_PATH"
        else
            export VITE_API_URL="http://localhost:${BACKEND_PORT}"
        fi

        npm install
        echo "Starting Vite dev server on port $FRONTEND_PORT..."
        exec npm run dev -- --host 0.0.0.0 --port "$FRONTEND_PORT"
        ;;

    --dev)
        print_header "Development Mode"
        print_env
        ensure_dirs

        # Start backend in background
        start_backend_background "$BACKEND_PORT"
        cd "$SCRIPT_DIR"

        # Start frontend dev server in foreground
        cd "${SCRIPT_DIR}/automl-ui"
        ensure_node
        export VITE_API_URL="http://localhost:${BACKEND_PORT}"
        npm install
        echo ""
        echo "Backend:  http://127.0.0.1:$BACKEND_PORT"
        echo "Frontend: http://localhost:$FRONTEND_PORT"
        echo ""

        trap "kill $BACKEND_PID 2>/dev/null; exit 0" SIGTERM SIGINT
        npm run dev -- --host 0.0.0.0 --port "$FRONTEND_PORT"
        ;;

    --all|*)
        print_header "Combined Mode"
        print_env
        ensure_dirs

        # Build frontend
        build_frontend

        # Start backend serving both API and static files
        export STATIC_DIR="${SCRIPT_DIR}/automl-ui/dist"
        if [ -d "/mnt/code/automl-ui/dist" ]; then
            export STATIC_DIR="/mnt/code/automl-ui/dist"
        fi

        echo ""
        echo "Starting AutoML Studio on http://0.0.0.0:$PORT"
        echo "  API:      /svc/v1/*"
        echo "  Frontend: / (served from $STATIC_DIR)"
        echo ""

        start_backend "$PORT"
        ;;
esac
