#!/bin/bash

set -euo pipefail

# args
IN_PATH=${IN_PATH:-"./app/api/domino_public_spec.json"}
OUT_PATH=${OUT_PATH:-"./app/api/generated"}

openapi-python-client generate \
  --path "$IN_PATH" \
  --output-path "$OUT_PATH" \
  --overwrite
