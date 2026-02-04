#!/bin/bash
# Domino App startup script for AutoML Service
# This script starts the FastAPI backend server

set -e

echo "=========================================="
echo "AutoML Service - Starting FastAPI Backend"
echo "=========================================="

# Set default environment variables - Domino uses PORT env var, default to 8888
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8888}
export WORKERS=${WORKERS:-4}

# Ensure required directories exist
mkdir -p /mnt/data/models
mkdir -p /mnt/data/datasets
mkdir -p /mnt/data/temp
mkdir -p /mnt/automl-service/uploads  # Persistent uploads directory

echo "Host: $HOST"
echo "Port: $PORT"
echo "Workers: $WORKERS"
echo ""

# Debug: Print Domino environment variables (masking sensitive values)
echo "Domino Environment:"
echo "  DOMINO_API_HOST: ${DOMINO_API_HOST:-NOT SET}"
echo "  DOMINO_API_KEY: ${DOMINO_API_KEY:+SET (hidden)}"
echo "  DOMINO_USER_API_KEY: ${DOMINO_USER_API_KEY:+SET (hidden)}"
echo "  DOMINO_PROJECT_NAME: ${DOMINO_PROJECT_NAME:-NOT SET}"
echo "  DOMINO_PROJECT_OWNER: ${DOMINO_PROJECT_OWNER:-NOT SET}"
echo ""

# Change to service directory
cd /mnt/automl-service

# Install missing lightweight dependencies only
# NOTE: Heavy packages like AutoGluon should be pre-installed in the Domino compute environment
echo "Installing lightweight dependencies..."
pip install -q --no-deps aiosqlite pydantic-settings python-multipart httpx 2>/dev/null || true

echo "Dependencies check complete"
echo ""

# Start the FastAPI server with uvicorn
# Use --reload for development (auto-reload on file changes)
# Note: --reload is incompatible with --workers, so we use single worker in dev mode

if [ "${RELOAD:-true}" = "true" ]; then
    echo "Starting with --reload (development mode)"
    exec uvicorn app.main:app \
        --host "$HOST" \
        --port "$PORT" \
        --reload \
        --log-level info
else
    echo "Starting with $WORKERS workers (production mode)"
    exec uvicorn app.main:app \
        --host "$HOST" \
        --port "$PORT" \
        --workers "$WORKERS" \
        --log-level info
fi
