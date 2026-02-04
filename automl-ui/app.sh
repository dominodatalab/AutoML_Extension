#!/bin/bash
# Domino App startup script for AutoML UI
# Serves React app and proxies API requests to automl-service

set -e

echo "=========================================="
echo "AutoML UI - Starting Frontend Server"
echo "=========================================="

cd /mnt/automl-ui

# Set environment variables
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8888}

# API Service URL - the backend automl-service
export API_SERVICE_URL=${API_SERVICE_URL:-"https://apps.se-demo.domino.tech/apps/9f146ade-e113-46e4-a5ae-1f3c04fb3fa8"}

echo "API Service URL: $API_SERVICE_URL"
echo "Port: $PORT"

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
npm install

echo "Building UI..."
npm run build

echo "Build complete"

# Generate runtime config - use relative API path since we proxy through this server
echo "Generating runtime config..."
cat > dist/config.js << 'EOF'
// Runtime configuration
// API calls go through this server's proxy to the backend service
window.APP_CONFIG = {
  API_URL: ""
};
EOF

echo "Config generated (using local proxy)"

# Install dependencies if needed
echo "Checking dependencies..."
pip install -q fastapi uvicorn httpx 2>/dev/null || true

echo ""
echo "=========================================="
echo "Verifying server.py routes..."
echo "=========================================="

# Debug: Print registered routes
python3 -c "
from server import app
print('Registered routes:')
for route in app.routes:
    if hasattr(route, 'path'):
        methods = getattr(route, 'methods', ['*'])
        print(f'  {methods} {route.path}')
" 2>&1 || echo "Failed to verify routes"

echo ""
echo "=========================================="
echo "Starting server on http://0.0.0.0:$PORT"
echo "=========================================="

# Start the FastAPI server
exec uvicorn server:app --host "$HOST" --port "$PORT" --log-level info
