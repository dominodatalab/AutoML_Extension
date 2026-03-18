#!/bin/bash
# Test proxy connectivity from inside the Domino App
echo "=== Environment ==="
echo "DOMINO_API_PROXY: ${DOMINO_API_PROXY:-not set}"
echo "DOMINO_API_HOST: ${DOMINO_API_HOST:-not set}"
echo "DOMINO_PROJECT_ID: ${DOMINO_PROJECT_ID:-not set}"
echo ""

PROXY="${DOMINO_API_PROXY:-http://localhost:8899}"
TOKEN=$(curl -s http://localhost:8899/access-token)
echo "Token length: ${#TOKEN}"
echo ""

echo "=== GET access-token ==="
curl -s -o /dev/null -w "status: %{http_code}, time: %{time_total}s\n" http://localhost:8899/access-token
echo ""

echo "=== GET v1 datasets (proxy) ==="
curl -s -w "\nstatus: %{http_code}, time: %{time_total}s\n" \
  -H "Authorization: Bearer $TOKEN" \
  "${PROXY}/api/datasetrw/v1/datasets?projectId=69b73e50c079b34f9a5b194a&limit=5" \
  --max-time 15 | head -c 300
echo ""
echo ""

echo "=== POST v1 create dataset (proxy) ==="
curl -s -w "\nstatus: %{http_code}, time: %{time_total}s\n" \
  -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"automl-extension","projectId":"69b73e50c079b34f9a5b194a","description":"test"}' \
  "${PROXY}/api/datasetrw/v1/datasets" \
  --max-time 15 | head -c 300
echo ""
echo ""

echo "=== POST /dataset (proxy) ==="
curl -s -w "\nstatus: %{http_code}, time: %{time_total}s\n" \
  -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"datasetName":"automl-extension","projectId":"69b73e50c079b34f9a5b194a","description":"test"}' \
  "${PROXY}/dataset" \
  --max-time 15 | head -c 300
echo ""
echo ""

NUCLEUS="${DOMINO_API_HOST}"
if [ -n "$NUCLEUS" ]; then
  echo "=== GET v1 datasets (nucleus) ==="
  curl -s -w "\nstatus: %{http_code}, time: %{time_total}s\n" \
    -H "Authorization: Bearer $TOKEN" \
    "${NUCLEUS}/api/datasetrw/v1/datasets?projectId=69b73e50c079b34f9a5b194a&limit=5" \
    --max-time 15 | head -c 300
  echo ""
  echo ""

  echo "=== POST v1 create dataset (nucleus) ==="
  curl -s -w "\nstatus: %{http_code}, time: %{time_total}s\n" \
    -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"name":"automl-extension","projectId":"69b73e50c079b34f9a5b194a","description":"test"}' \
    "${NUCLEUS}/api/datasetrw/v1/datasets" \
    --max-time 15 | head -c 300
  echo ""
  echo ""
fi

echo "=== DONE ==="
