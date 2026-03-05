import os, sys
sys.path.insert(0, "/mnt/automl-service")
print("DOMINO_PROJECT_ID:", os.environ.get("DOMINO_PROJECT_ID"))
try:
    from mlflow.tracking.request_header.registry import _request_header_provider_registry
    print("Registry import: OK")
except Exception as e:
    print("Registry import FAILED:", e); sys.exit(1)
print("Providers before:", len(_request_header_provider_registry._registry))
from app.core.experiment_tracker import _register_domino_project_header_provider
print("Providers after:", len(_request_header_provider_registry._registry))
for i, p in enumerate(_request_header_provider_registry._registry):
    print("  Provider %d: %s, in_context=%s, headers=%s" % (i, type(p).__name__, p.in_context(), p.request_headers()))
