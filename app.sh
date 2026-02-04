#!/bin/bash
# Combined Domino App startup script for AutoML
# Runs both backend (FastAPI) and frontend (React) as a single app

set -e

echo "=========================================="
echo "AutoML Studio - Combined App Startup"
echo "=========================================="

# Set default environment variables
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8888}
export BACKEND_PORT=${BACKEND_PORT:-8000}

echo "Frontend Port: $PORT"
echo "Backend Port: $BACKEND_PORT"
echo ""

# Ensure required directories exist
mkdir -p /mnt/data/models
mkdir -p /mnt/data/datasets
mkdir -p /mnt/data/temp
mkdir -p /mnt/automl-service/uploads

# Debug: Print Domino environment variables
echo "Domino Environment:"
echo "  DOMINO_API_HOST: ${DOMINO_API_HOST:-NOT SET}"
echo "  DOMINO_API_KEY: ${DOMINO_API_KEY:+SET (hidden)}"
echo "  DOMINO_USER_API_KEY: ${DOMINO_USER_API_KEY:+SET (hidden)}"
echo "  DOMINO_PROJECT_NAME: ${DOMINO_PROJECT_NAME:-NOT SET}"
echo "  DOMINO_PROJECT_OWNER: ${DOMINO_PROJECT_OWNER:-NOT SET}"
echo ""

# ==========================================
# Start Backend Service
# ==========================================
echo "Starting backend service on port $BACKEND_PORT..."

cd /mnt/automl-service

# Install lightweight dependencies if needed
pip install -q --no-deps aiosqlite aiofiles pydantic-settings python-multipart httpx 2>/dev/null || true

# Start backend in background
uvicorn app.main:app \
    --host 127.0.0.1 \
    --port "$BACKEND_PORT" \
    --log-level warning &

BACKEND_PID=$!
echo "Backend started with PID: $BACKEND_PID"

# Wait for backend to be ready
echo "Waiting for backend to be ready..."
MAX_RETRIES=30
RETRY_COUNT=0
while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if curl -s "http://127.0.0.1:$BACKEND_PORT/svc/v1/health" > /dev/null 2>&1; then
        echo "Backend is ready!"
        break
    fi
    RETRY_COUNT=$((RETRY_COUNT + 1))
    sleep 1
done

if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
    echo "ERROR: Backend failed to start within $MAX_RETRIES seconds"
    exit 1
fi

# ==========================================
# Start Frontend Service
# ==========================================
echo ""
echo "Starting frontend service on port $PORT..."

cd /mnt/automl-ui

# Set API URL to local backend
export API_SERVICE_URL="http://127.0.0.1:$BACKEND_PORT"

# Ensure Node.js/npm is available
if ! command -v npm &> /dev/null; then
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
fi

echo "Node.js version: $(node --version)"
echo "npm version: $(npm --version)"

# Install npm dependencies and build
echo "Installing npm dependencies..."
npm install --silent

echo "Building UI..."
npm run build

# Generate runtime config - API calls go through local proxy
echo "Generating runtime config..."
cat > dist/config.js << 'EOF'
// Runtime configuration
// API calls go through this server's proxy to the backend service
window.APP_CONFIG = {
  API_URL: ""
};
EOF

# Install Python dependencies for proxy server
pip install -q fastapi uvicorn httpx 2>/dev/null || true

echo ""
echo "=========================================="
echo "Starting AutoML Studio on http://0.0.0.0:$PORT"
echo "Backend API: http://127.0.0.1:$BACKEND_PORT"
echo "=========================================="

# Trap to clean up backend on exit
cleanup() {
    echo "Shutting down..."
    kill $BACKEND_PID 2>/dev/null || true
    exit 0
}
trap cleanup SIGTERM SIGINT

# Start the frontend FastAPI server (includes proxy to backend)
exec uvicorn server:app --host "$HOST" --port "$PORT" --log-level info
