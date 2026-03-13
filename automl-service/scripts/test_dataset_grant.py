#!/usr/bin/env python3
"""Test Domino Dataset grant/share workflow.

Finds the dataset created by test_dataset_api.py and tests granting
access to the App's own project so the mount appears.

Usage:
    python scripts/test_dataset_grant.py <target_project_id>
    python scripts/test_dataset_grant.py <target_project_id> --dataset-name my-dataset
    python scripts/test_dataset_grant.py --dataset-id <dataset_id>
"""

import argparse
import asyncio
import json
import os
import sys
from typing import Any, Optional

import httpx

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DATASET_NAME = "automl-extension"

MOUNT_CANDIDATES = [
    "/domino/datasets/local/{name}",
    "/domino/datasets/{name}",
    "/mnt/data/{name}",
    "/mnt/imported/data/{name}",
]

# ---------------------------------------------------------------------------
# Auth (same standalone pattern as test_dataset_api.py)
# ---------------------------------------------------------------------------


async def get_auth_headers() -> dict[str, str]:
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
    host = os.environ.get("DOMINO_API_PROXY") or os.environ.get("DOMINO_API_HOST")
    if not host:
        print("[env] ERROR: neither DOMINO_API_PROXY nor DOMINO_API_HOST is set")
        sys.exit(1)
    return host.rstrip("/")


# ---------------------------------------------------------------------------
# API helper
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


async def find_dataset_by_name(
    client: httpx.AsyncClient, headers: dict, base_url: str, project_id: str, name: str
) -> Optional[dict]:
    """Find a dataset by name in a project."""
    resp = await api_request(
        client,
        "GET",
        "/api/datasetrw/v2/datasets",
        headers=headers,
        base_url=base_url,
        params={"projectIdsToInclude": project_id},
    )
    if resp.status_code != 200:
        return None

    data = resp.json()
    datasets = data if isinstance(data, list) else (
        data.get("items") or data.get("datasets") or data.get("data") or []
    )
    for ds in datasets:
        ds_name = ds.get("datasetName") or ds.get("name") or ""
        if ds_name == name:
            return ds
    return None


async def get_dataset_details(
    client: httpx.AsyncClient, headers: dict, base_url: str, dataset_id: str
) -> Optional[dict]:
    """GET /api/datasetrw/v2/datasets/{id} for full details."""
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


async def try_grant_endpoints(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    target_project_id: str,
) -> bool:
    """Try various grant/share endpoints to give the App project access."""
    print(f"\n[grant] Attempting to grant project {target_project_id} access to dataset {dataset_id}")

    attempts = [
        # Most likely REST patterns for Domino
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/shares",
            {"projectId": target_project_id},
        ),
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/grants",
            {"projectId": target_project_id},
        ),
        (
            "PUT",
            f"/api/datasetrw/v2/datasets/{dataset_id}/projects/{target_project_id}",
            None,
        ),
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/projects",
            {"projectId": target_project_id},
        ),
        (
            "PATCH",
            f"/api/datasetrw/v2/datasets/{dataset_id}",
            {"sharedProjectIds": [target_project_id]},
        ),
        # v1 variants
        (
            "POST",
            f"/api/datasetrw/v1/datasets/{dataset_id}/shares",
            {"projectId": target_project_id},
        ),
        (
            "POST",
            f"/api/datasetrw/v1/datasets/{dataset_id}/grants",
            {"projectId": target_project_id},
        ),
    ]

    for method, path, body in attempts:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url, json_body=body
        )
        if resp.status_code in (200, 201, 204):
            print(f"\n  -> GRANT SUCCEEDED via {method} {path}")
            return True
        # 409 might mean "already shared"
        if resp.status_code == 409:
            print(f"\n  -> 409 Conflict — may already be shared via {method} {path}")
            return True

    print("\n  -> All grant attempts failed")
    return False


def check_mount_paths(dataset_name: str) -> Optional[str]:
    """Scan known mount roots for the dataset."""
    print(f"\n[mount] Checking mount paths for '{dataset_name}'")
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
        if exists and is_dir:
            return path
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def main(
    target_project_id: Optional[str],
    dataset_id: Optional[str],
    dataset_name: str,
) -> None:
    base_url = resolve_api_host()
    headers = await get_auth_headers()

    app_project_id = os.environ.get("DOMINO_PROJECT_ID")
    if not app_project_id:
        print("[env] ERROR: DOMINO_PROJECT_ID not set — can't determine App project")
        sys.exit(1)

    print(f"\n{'#'*60}")
    print(f"# Domino Dataset Grant/Share Test")
    print(f"# App project:     {app_project_id}")
    print(f"# Target project:  {target_project_id or '(from dataset lookup)'}")
    print(f"# Dataset name:    {dataset_name}")
    print(f"# Dataset ID:      {dataset_id or '(will look up)'}")
    print(f"# API host:        {base_url}")
    print(f"{'#'*60}")

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Resolve dataset ID if not provided
        if not dataset_id:
            if not target_project_id:
                print("\nERROR: Provide either --dataset-id or target_project_id")
                sys.exit(1)

            ds = await find_dataset_by_name(
                client, headers, base_url, target_project_id, dataset_name
            )
            if not ds:
                print(f"\nDataset '{dataset_name}' not found in project {target_project_id}")
                print("Run test_dataset_api.py first to create it.")
                sys.exit(1)
            dataset_id = ds.get("datasetId") or ds.get("id")
            print(f"\n  Found dataset: id={dataset_id}")

        # Get current dataset details (to see current sharing state)
        print("\n[step 1] Current dataset details:")
        details = await get_dataset_details(client, headers, base_url, dataset_id)
        if details:
            # Look for sharing-related fields
            sharing_keys = [
                k for k in details.keys()
                if any(term in k.lower() for term in ("shar", "grant", "project", "access", "mount"))
            ]
            if sharing_keys:
                print(f"\n  Sharing-related fields: {sharing_keys}")
                for k in sharing_keys:
                    print(f"    {k}: {json.dumps(details[k], indent=2)[:500]}")

        # Check if mount already exists (App may already have access)
        mount_before = check_mount_paths(dataset_name)
        if mount_before:
            print(f"\n  Mount already exists at {mount_before} — App may already have access")

        # Try to grant access
        if app_project_id != target_project_id:
            granted = await try_grant_endpoints(
                client, headers, base_url, dataset_id, app_project_id
            )
        else:
            print("\n[grant] Skipped — target and App are the same project")
            granted = True

        # Check mount again after grant attempt
        if not mount_before:
            mount_after = check_mount_paths(dataset_name)
            if mount_after:
                print(f"\n  Mount appeared after grant at {mount_after}!")
            else:
                print("\n  Mount still not found — may require App restart to take effect")

        # Re-check dataset details after grant
        if granted and details:
            print("\n[step final] Dataset details after grant:")
            await get_dataset_details(client, headers, base_url, dataset_id)

    # Summary
    print(f"\n{'#'*60}")
    print("# Summary")
    print(f"#   Dataset ID:       {dataset_id}")
    print(f"#   Mount before:     {mount_before or 'none'}")
    print(f"#   Grant attempted:  {app_project_id != target_project_id}")
    print(f"#   Mount after:      {(mount_before or check_mount_paths(dataset_name)) or 'none'}")
    print(f"{'#'*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Domino Dataset grant/share workflow")
    parser.add_argument("target_project_id", nargs="?", help="Target project ID (optional if --dataset-id given)")
    parser.add_argument("--dataset-id", help="Dataset ID (skip lookup)")
    parser.add_argument("--dataset-name", default=DATASET_NAME, help=f"Dataset name (default: {DATASET_NAME})")
    args = parser.parse_args()

    if not args.target_project_id and not args.dataset_id:
        parser.error("Provide either target_project_id or --dataset-id")

    asyncio.run(main(args.target_project_id, args.dataset_id, args.dataset_name))
