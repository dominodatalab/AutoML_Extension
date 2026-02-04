#!/bin/bash
# Setup script for running the AutoML UI in a Domino workspace
# This script configures the environment for the Vite dev server to work with Domino's proxy

set -e

echo "=========================================="
echo "AutoML UI - Domino Workspace Setup"
echo "=========================================="

# Check if we're in a Domino environment
if [ -z "$DOMINO_RUN_ID" ]; then
    echo "Warning: DOMINO_RUN_ID not set. Running in local mode."
    export VITE_BASE_PATH="/"
else
    echo "Detected Domino environment: $DOMINO_RUN_ID"

    # Construct the Jupyter proxy URL for the Vite dev server (port 3000)
    # Domino workspace proxy format: /notebookSession/{run_id}/proxy/{port}/
    export VITE_BASE_PATH="/notebookSession/${DOMINO_RUN_ID}/proxy/3000/"
    echo "Setting base path: $VITE_BASE_PATH"
fi

# Set API URL - in Domino workspace, the FastAPI backend runs on port 8000
# which is also proxied through Domino
if [ -z "$VITE_API_URL" ]; then
    if [ -n "$DOMINO_RUN_ID" ]; then
        # In Domino, use the proxy path for API as well
        export VITE_API_URL="/notebookSession/${DOMINO_RUN_ID}/proxy/8000"
        echo "Setting API URL: $VITE_API_URL"
    else
        export VITE_API_URL="http://localhost:8000"
    fi
fi

# Navigate to the UI directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "Installing dependencies..."
npm install

echo ""
echo "Starting Vite development server..."
echo "=========================================="
echo ""

if [ -n "$DOMINO_RUN_ID" ]; then
    echo "Access the UI at:"
    echo "  https://<your-domino-instance>/notebookSession/${DOMINO_RUN_ID}/proxy/3000/"
    echo ""
fi

# Start Vite with host binding for Domino access
npm run dev -- --host 0.0.0.0
