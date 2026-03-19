#!/bin/bash

set -euo pipefail

# args
BASE_URL=${BASE_URL:-"https://cloud-dogfood.domino.tech"}
OUT_PATH=${OUT_PATH:-"./app/api/domino_public_spec.json"}
# set to non-empty to activate
IGNORE_VERSION_CHECKS=${IGNORE_VERSION_CHECKS:-}
SUPPORTED_DOMINO_VERSION=${SUPPORTED_DOMINO_VERSION:-}

URL="$BASE_URL/assets/public-api.json"
VERSION_URL="$BASE_URL/version"

if [[ -z "$IGNORE_VERSION_CHECKS" ]]; then

  if [[ -z "$SUPPORTED_DOMINO_VERSION" ]]; then
    echo "SUPPORTED_DOMINO_VERSION is not set" >&2
    exit 1
  fi


  echo "Getting Domino version at $VERSION_URL" >&2

  REMOTE_VERSION_RAW=$(curl $VERSION_URL)

  if [[ -z "$REMOTE_VERSION_RAW" ]]; then
    echo "Version info from $VERSION_URL is empty" >&2
    exit 1
  fi

  echo found version info $REMOTE_VERSION_RAW

  REMOTE_VERSION=$(echo $REMOTE_VERSION_RAW | jq -r '.version | match("^([0-9]+\\.[0-9]+\\.[0-9]+)") | .string')

  if [[ "$REMOTE_VERSION" != "$SUPPORTED_DOMINO_VERSION" ]]; then
    echo "Domino version mismatch. Remote=$REMOTE_VERSION, Expected=$SUPPORTED_DOMINO_VERSION" >&2
    exit 1
  fi

  echo "Domino version OK: $REMOTE_VERSION" >&2
fi

curl $URL >> $OUT_PATH
# openapi-python-client generate --url "$URL" --output-path "$OUT_PATH" --overwrite
