import os, sys

print("DOMINO_PROJECT_ID:", os.environ.get("DOMINO_PROJECT_ID"))

from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider
from mlflow.tracking.request_header.registry import _request_header_provider_registry

class DominoProjectHeaderProvider(RequestHeaderProvider):
    def in_context(self):
        return bool(os.environ.get("DOMINO_PROJECT_ID"))
    def request_headers(self):
        pid = os.environ.get("DOMINO_PROJECT_ID", "")
        return {"X-Domino-Project-Id": pid} if pid else {}

_request_header_provider_registry.register(DominoProjectHeaderProvider())
print("Registered. Total providers:", len(_request_header_provider_registry._registry))

for i, p in enumerate(_request_header_provider_registry._registry):
    print("  Provider %d: %s, in_context=%s, headers=%s" % (i, type(p).__name__, p.in_context(), p.request_headers()))

import mlflow, json, urllib.request
mlflow.set_tracking_uri(os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:8768"))
print("\nCreating test experiment...")
exp_id = mlflow.create_experiment("debug_header_provider_test_v2")
print("Created experiment:", exp_id)

url = "%s/api/2.0/mlflow/experiments/get?experiment_id=%s" % (
    os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:8768"), exp_id)
resp = json.loads(urllib.request.urlopen(url).read())
tags = {t["key"]: t["value"] for t in (resp["experiment"].get("tags") or [])}
print("  project_id:", tags.get("mlflow.domino.project_id", "N/A"))
print("  project_name:", tags.get("mlflow.domino.project_name", "N/A"))

expected = os.environ.get("DOMINO_PROJECT_ID")
actual = tags.get("mlflow.domino.project_id")
if actual == expected:
    print("\nSUCCESS: Experiment landed in the correct project!")
else:
    print("\nFAILED: Expected project %s but got %s" % (expected, actual))
