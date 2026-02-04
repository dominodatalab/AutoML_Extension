#!/usr/bin/env bash

# Downloads frontend code from the repository into example_domino_frontend_code/
# The .git directory is removed so there's no git continuity with the source repo.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$SCRIPT_DIR/example_domino_frontend_code"
REPO_URL="https://github.com/cerebrotech/frontend-web-ui-service.git"
TEMP_DIR=""

# Cleanup on exit (success, failure, or interrupt)
cleanup() {
    if [[ -n "$TEMP_DIR" && -d "$TEMP_DIR" ]]; then
        rm -rf "$TEMP_DIR"
    fi
}
trap cleanup EXIT

# Check for git
if ! command -v git &> /dev/null; then
    echo "❌ Error: git is not installed or not in PATH" >&2
    exit 1
fi

# Warn if target directory has content
if [[ -d "$TARGET_DIR" ]] && [[ -n "$(ls -A "$TARGET_DIR" 2>/dev/null)" ]]; then
    echo "⚠️  Warning: $TARGET_DIR is not empty and will be overwritten."
    read -r -p "Continue? [y/N] " response
    if [[ ! "$response" =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)

echo "📥 Cloning from $REPO_URL..."
if ! git clone --depth 1 "$REPO_URL" "$TEMP_DIR"; then
    echo "❌ Error: Failed to clone repository" >&2
    exit 1
fi

echo "🧹 Removing git history..."
rm -rf "$TEMP_DIR/.git"

echo "📂 Copying to $TARGET_DIR..."
mkdir -p "$TARGET_DIR"
# Remove existing contents safely
find "$TARGET_DIR" -mindepth 1 -delete 2>/dev/null || rm -rf "$TARGET_DIR" && mkdir -p "$TARGET_DIR"
# Copy all files including hidden ones
cp -r "$TEMP_DIR"/. "$TARGET_DIR/"

echo "✅ Done! Frontend code is in $TARGET_DIR"
