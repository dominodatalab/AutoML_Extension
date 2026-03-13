#!/usr/bin/env python3
"""Test Domino Dataset RW API — create dataset in target project.

Validates that the App can list, create, and write to a dataset in a
target project via the Dataset RW v2 API.

Usage:
    python scripts/test_dataset_api.py <target_project_id>
    python scripts/test_dataset_api.py <target_project_id> --dataset-name my-dataset
    python scripts/test_dataset_api.py <target_project_id> --skip-create
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

import httpx

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DATASET_NAME = "automl-extension"
DESCRIPTION = "AutoML Extension storage — auto-created by the AutoML App"

MOUNT_CANDIDATES = [
    "/domino/datasets/local/{name}",
    "/domino/datasets/{name}",
    "/mnt/data/{name}",
    "/mnt/imported/data/{name}",
]

# ---------------------------------------------------------------------------
# Auth helpers (standalone — no app imports)
# ---------------------------------------------------------------------------


async def get_auth_headers() -> dict[str, str]:
    """Acquire Domino auth headers (sidecar token > env API key)."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get("http://localhost:8899/access-token")
        if resp.status_code == 200 and resp.text.strip():
            print("[auth] Using ephemeral sidecar token")
            return {"Authorization": f"Bearer {resp.text.strip()}"}
    except Exception:
        pass

    api_key = os.environ.get("DOMINO_API_KEY") or os.environ.get("DOMINO_USER_API_KEY")
    if api_key:
        print("[auth] Using static API key from env")
        return {"X-Domino-Api-Key": api_key}

    print("[auth] WARNING: no auth available")
    return {}


def resolve_api_host() -> str:
    """Resolve Domino API base URL from env."""
    host = os.environ.get("DOMINO_API_PROXY") or os.environ.get("DOMINO_API_HOST")
    if not host:
        print("[env] ERROR: neither DOMINO_API_PROXY nor DOMINO_API_HOST is set")
        sys.exit(1)
    return host.rstrip("/")


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------


async def api_request(
    client: httpx.AsyncClient,
    method: str,
    path: str,
    *,
    headers: dict[str, str],
    base_url: str,
    json_body: Any = None,
    params: Optional[dict[str, Any]] = None,
) -> httpx.Response:
    """Send a request and log full details."""
    url = f"{base_url}{path}"
    print(f"\n{'='*60}")
    print(f">>> {method} {url}")
    if params:
        print(f"    params: {json.dumps(params)}")
    if json_body:
        print(f"    body:   {json.dumps(json_body, indent=2)}")

    resp = await client.request(method, url, json=json_body, params=params, headers=headers)

    print(f"<<< {resp.status_code} {resp.reason_phrase}")
    try:
        body = resp.json()
        print(f"    response: {json.dumps(body, indent=2)[:2000]}")
    except Exception:
        print(f"    response (text): {resp.text[:1000]}")
    print(f"{'='*60}")
    return resp


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------


async def resolve_project(
    client: httpx.AsyncClient, headers: dict, base_url: str, project_id: str
) -> Optional[dict]:
    """GET /v4/projects/{id} to resolve project name/owner."""
    print(f"\n[step 0] Resolving project metadata for {project_id}")
    resp = await api_request(
        client, "GET", f"/v4/projects/{project_id}", headers=headers, base_url=base_url
    )
    if resp.status_code == 200:
        data = resp.json()
        print(f"  -> Project: {data.get('ownerUsername')}/{data.get('name')}")
        return data
    return None


async def list_datasets(
    client: httpx.AsyncClient, headers: dict, base_url: str, project_id: str
) -> list[dict]:
    """List datasets for a project, return the full list."""
    print(f"\n[step 1] Listing datasets for project {project_id}")
    resp = await api_request(
        client,
        "GET",
        "/api/datasetrw/v2/datasets",
        headers=headers,
        base_url=base_url,
        params={"projectIdsToInclude": project_id},
    )
    if resp.status_code != 200:
        print(f"  -> Failed to list datasets: HTTP {resp.status_code}")
        return []

    data = resp.json()
    # Response could be a list or a wrapper with .items / .datasets
    if isinstance(data, list):
        datasets = data
    elif isinstance(data, dict):
        datasets = data.get("items") or data.get("datasets") or data.get("data") or []
        if not datasets:
            print(f"  -> Response keys: {list(data.keys())}")
            # Maybe the dict itself is one dataset? Unlikely but log it.
    else:
        datasets = []

    print(f"  -> Found {len(datasets)} dataset(s)")
    for ds in datasets:
        print(f"     - {ds.get('datasetName', ds.get('name', '?'))} (id={ds.get('datasetId', ds.get('id', '?'))})")

    return datasets


def find_dataset(datasets: list[dict], name: str) -> Optional[dict]:
    """Find a dataset by name in the list."""
    for ds in datasets:
        ds_name = ds.get("datasetName") or ds.get("name") or ""
        if ds_name == name:
            return ds
    return None


async def create_dataset(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    project_id: str,
    dataset_name: str,
    description: str,
) -> Optional[dict]:
    """Try to create a dataset via POST /api/datasetrw/v2/datasets.

    Tries multiple payload shapes since the exact API contract is unknown.
    """
    print(f"\n[step 2] Creating dataset '{dataset_name}' in project {project_id}")

    # Attempt 1: camelCase field names (most likely for Domino v2 API)
    payload_v1 = {
        "datasetName": dataset_name,
        "projectId": project_id,
        "description": description,
    }
    resp = await api_request(
        client,
        "POST",
        "/api/datasetrw/v2/datasets",
        headers=headers,
        base_url=base_url,
        json_body=payload_v1,
    )
    if resp.status_code in (200, 201):
        print("  -> Created with payload v1 (camelCase)")
        return resp.json()

    # If 400/422 with validation details, log and try alternate payloads
    print(f"  -> Payload v1 failed ({resp.status_code}), trying alternate shapes...")

    # Attempt 2: snake_case field names
    payload_v2 = {
        "dataset_name": dataset_name,
        "project_id": project_id,
        "description": description,
    }
    resp = await api_request(
        client,
        "POST",
        "/api/datasetrw/v2/datasets",
        headers=headers,
        base_url=base_url,
        json_body=payload_v2,
    )
    if resp.status_code in (200, 201):
        print("  -> Created with payload v2 (snake_case)")
        return resp.json()

    # Attempt 3: with "name" instead of "datasetName"
    payload_v3 = {
        "name": dataset_name,
        "projectId": project_id,
        "description": description,
    }
    resp = await api_request(
        client,
        "POST",
        "/api/datasetrw/v2/datasets",
        headers=headers,
        base_url=base_url,
        json_body=payload_v3,
    )
    if resp.status_code in (200, 201):
        print("  -> Created with payload v3 (name + projectId)")
        return resp.json()

    # Attempt 4: v1 endpoint path
    resp = await api_request(
        client,
        "POST",
        "/api/datasetrw/v1/datasets",
        headers=headers,
        base_url=base_url,
        json_body=payload_v1,
    )
    if resp.status_code in (200, 201):
        print("  -> Created with v1 endpoint path")
        return resp.json()

    print("  -> All create attempts failed. Check responses above for clues.")
    return None


async def verify_creation(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    project_id: str,
    dataset_name: str,
) -> Optional[dict]:
    """Re-list datasets and confirm the new one exists."""
    print(f"\n[step 3] Verifying '{dataset_name}' exists after creation")
    datasets = await list_datasets(client, headers, base_url, project_id)
    ds = find_dataset(datasets, dataset_name)
    if ds:
        print(f"  -> CONFIRMED: '{dataset_name}' exists (id={ds.get('datasetId', ds.get('id'))})")
    else:
        print(f"  -> NOT FOUND: '{dataset_name}' not in dataset list after creation")
    return ds


def check_mount_paths(dataset_name: str) -> Optional[str]:
    """Scan known mount roots for the dataset directory."""
    print(f"\n[step 4] Scanning mount paths for '{dataset_name}'")
    found = None
    for template in MOUNT_CANDIDATES:
        path = template.format(name=dataset_name)
        exists = os.path.exists(path)
        is_dir = os.path.isdir(path) if exists else False
        writable = os.access(path, os.W_OK) if exists else False
        status = "EXISTS" if exists else "missing"
        if is_dir:
            status += " (dir)"
        if writable:
            status += " (writable)"
        print(f"  {path}: {status}")
        if exists and is_dir and found is None:
            found = path

    # Also check env-provided mount paths
    for env_key in ("DOMINO_DATASET_MOUNT_PATH", "DOMINO_MOUNT_PATHS"):
        val = os.environ.get(env_key)
        if val:
            print(f"\n  env {env_key} = {val}")
            for part in val.replace(",", ":").replace(";", ":").split(":"):
                part = part.strip()
                if not part:
                    continue
                ds_path = os.path.join(part, dataset_name)
                exists = os.path.exists(ds_path)
                print(f"  {ds_path}: {'EXISTS' if exists else 'missing'}")
                if exists and found is None:
                    found = ds_path

    if found:
        print(f"\n  -> Mount found at: {found}")
    else:
        print(f"\n  -> No mount found. Dataset may require App restart to appear.")
    return found


def test_write(mount_path: str) -> bool:
    """Attempt to write and read back a test file."""
    print(f"\n[step 5] Testing write to {mount_path}")
    test_file = os.path.join(mount_path, ".automl-test-write")
    try:
        Path(test_file).write_text("automl-extension write test\n")
        content = Path(test_file).read_text()
        print(f"  -> Write succeeded, read back: {content.strip()!r}")
        # Clean up
        os.remove(test_file)
        print("  -> Cleanup succeeded")
        return True
    except PermissionError as e:
        print(f"  -> PermissionError: {e}")
        return False
    except Exception as e:
        print(f"  -> Error: {type(e).__name__}: {e}")
        return False


async def test_share_api(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    app_project_id: str,
) -> None:
    """Discover dataset sharing/grant API endpoints."""
    print(f"\n[step 6] Exploring dataset share/grant API for dataset {dataset_id}")

    # Try various known/guessed share endpoints
    share_endpoints = [
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/shares", {"projectId": app_project_id}),
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/grants", {"projectId": app_project_id}),
        ("PUT", f"/api/datasetrw/v2/datasets/{dataset_id}/projects/{app_project_id}", {}),
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/projects", {"projectId": app_project_id}),
        ("PATCH", f"/api/datasetrw/v2/datasets/{dataset_id}", {"sharedProjectIds": [app_project_id]}),
    ]

    for method, path, body in share_endpoints:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url, json_body=body or None
        )
        if resp.status_code in (200, 201, 204):
            print(f"  -> Share/grant succeeded via {method} {path}")
            return

    print("  -> No share endpoint found. The dataset may auto-share or sharing may not be needed.")


async def get_dataset_details(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[dict]:
    """GET full dataset details to inspect sharing/mount info."""
    print(f"\n[step extra] Getting full dataset details for {dataset_id}")
    resp = await api_request(
        client,
        "GET",
        f"/api/datasetrw/v2/datasets/{dataset_id}",
        headers=headers,
        base_url=base_url,
    )
    if resp.status_code == 200:
        return resp.json()
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def main(target_project_id: str, dataset_name: str, skip_create: bool) -> None:
    base_url = resolve_api_host()
    headers = await get_auth_headers()

    print(f"\n{'#'*60}")
    print(f"# Domino Dataset RW API Test")
    print(f"# Target project: {target_project_id}")
    print(f"# Dataset name:   {dataset_name}")
    print(f"# API host:       {base_url}")
    print(f"# App project:    {os.environ.get('DOMINO_PROJECT_ID', '(not set)')}")
    print(f"{'#'*60}")

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Step 0: Resolve project
        project_info = await resolve_project(client, headers, base_url, target_project_id)

        # Step 1: List existing datasets
        datasets = await list_datasets(client, headers, base_url, target_project_id)
        existing = find_dataset(datasets, dataset_name)

        if existing:
            print(f"\n  Dataset '{dataset_name}' already exists!")
            dataset_id = existing.get("datasetId") or existing.get("id")
        elif skip_create:
            print(f"\n  Dataset '{dataset_name}' not found and --skip-create specified. Exiting.")
            return
        else:
            # Step 2: Create dataset
            created = await create_dataset(
                client, headers, base_url, target_project_id, dataset_name, DESCRIPTION
            )
            if not created:
                print("\n  FAILED to create dataset. Exiting.")
                return
            dataset_id = created.get("datasetId") or created.get("id")

            # Step 3: Verify
            verified = await verify_creation(client, headers, base_url, target_project_id, dataset_name)
            if verified:
                dataset_id = verified.get("datasetId") or verified.get("id")

        # Get full details if we have an ID
        if dataset_id:
            await get_dataset_details(client, headers, base_url, dataset_id)

        # Step 4: Check mount paths
        mount = check_mount_paths(dataset_name)

        # Step 5: Test write
        if mount:
            test_write(mount)
        else:
            print("\n[step 5] Skipped (no mount found)")

        # Step 6: Test sharing
        app_project_id = os.environ.get("DOMINO_PROJECT_ID")
        if dataset_id and app_project_id and app_project_id != target_project_id:
            await test_share_api(client, headers, base_url, dataset_id, app_project_id)
        elif not app_project_id:
            print("\n[step 6] Skipped (DOMINO_PROJECT_ID not set, can't test sharing)")
        elif app_project_id == target_project_id:
            print("\n[step 6] Skipped (target == app project, sharing not needed)")

    # Summary
    print(f"\n{'#'*60}")
    print("# Summary")
    print(f"#   Dataset exists: {bool(existing or dataset_id)}")
    print(f"#   Dataset ID:     {dataset_id or 'unknown'}")
    print(f"#   Mount found:    {mount or 'none'}")
    print(f"#   Writable:       {'yes' if mount and os.access(mount, os.W_OK) else 'unknown/no'}")
    print(f"{'#'*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Domino Dataset RW API")
    parser.add_argument("target_project_id", help="Target Domino project ID")
    parser.add_argument(
        "--dataset-name", default=DATASET_NAME, help=f"Dataset name (default: {DATASET_NAME})"
    )
    parser.add_argument(
        "--skip-create", action="store_true", help="Only list/check, don't create"
    )
    args = parser.parse_args()
    asyncio.run(main(args.target_project_id, args.dataset_name, args.skip_create))
