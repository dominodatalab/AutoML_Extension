#!/usr/bin/env python3
"""Test whether Domino dataset mounts appear without an app restart.

Creates a new dataset, grants access, then polls mount paths every N seconds
to determine if/when the mount becomes available. This answers the key
architectural question: can we create-and-use a dataset in a single request,
or must the app restart first?

Usage:
    python scripts/test_mount_timing.py <project_id>
    python scripts/test_mount_timing.py <project_id> --poll-interval 5 --max-wait 120
    python scripts/test_mount_timing.py <project_id> --skip-cleanup
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Optional

import httpx

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TEST_DATASET_PREFIX = "automl-mount-test"

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
# Mount probing
# ---------------------------------------------------------------------------


def probe_all_mounts(dataset_name: str) -> Optional[str]:
    """Check all known mount locations. Returns the first existing path or None."""
    for template in MOUNT_CANDIDATES:
        path = template.format(name=dataset_name)
        if os.path.exists(path):
            is_dir = os.path.isdir(path)
            writable = os.access(path, os.W_OK) if is_dir else False
            status = "EXISTS"
            if is_dir:
                status += " (dir)"
            if writable:
                status += " (writable)"
            print(f"  {path}: {status}")
            return path

    # Also check env-provided mount paths
    for env_key in ("DOMINO_DATASET_MOUNT_PATH", "DOMINO_MOUNT_PATHS"):
        val = os.environ.get(env_key)
        if not val:
            continue
        for part in val.replace(",", ":").replace(";", ":").split(":"):
            part = part.strip()
            if not part:
                continue
            ds_path = os.path.join(part, dataset_name)
            if os.path.exists(ds_path):
                print(f"  {ds_path}: EXISTS (env: {env_key})")
                return ds_path

    return None


def report_all_candidates(dataset_name: str) -> None:
    """Print status of every candidate path (for diagnostics)."""
    for template in MOUNT_CANDIDATES:
        path = template.format(name=dataset_name)
        exists = os.path.exists(path)
        print(f"    {path}: {'EXISTS' if exists else 'missing'}")

    for env_key in ("DOMINO_DATASET_MOUNT_PATH", "DOMINO_MOUNT_PATHS"):
        val = os.environ.get(env_key)
        if val:
            for part in val.replace(",", ":").replace(";", ":").split(":"):
                part = part.strip()
                if not part:
                    continue
                ds_path = os.path.join(part, dataset_name)
                exists = os.path.exists(ds_path)
                print(f"    {ds_path}: {'EXISTS' if exists else 'missing'} (env: {env_key})")


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------


async def create_test_dataset(
    client: httpx.AsyncClient,
    headers: dict[str, str],
    base_url: str,
    project_id: str,
    dataset_name: str,
) -> Optional[dict]:
    """Create a dataset via POST /api/datasetrw/v1/datasets (known working endpoint)."""
    print(f"\n[step 1] Creating dataset '{dataset_name}' in project {project_id}")
    payload = {
        "name": dataset_name,
        "projectId": project_id,
        "description": f"Mount timing test — safe to delete",
    }
    resp = await api_request(
        client,
        "POST",
        "/api/datasetrw/v1/datasets",
        headers=headers,
        base_url=base_url,
        json_body=payload,
    )
    if resp.status_code in (200, 201):
        data = resp.json()
        # v1 may wrap as {"dataset": {...}}
        return data.get("dataset", data)

    print(f"  -> FAILED to create dataset (HTTP {resp.status_code})")
    return None


async def grant_project_access(
    client: httpx.AsyncClient,
    headers: dict[str, str],
    base_url: str,
    dataset_id: str,
    project_id: str,
) -> bool:
    """Grant DatasetRwEditor to the current app project."""
    print(f"\n[step 2] Granting DatasetRwEditor on dataset {dataset_id} to project {project_id}")
    resp = await api_request(
        client,
        "POST",
        f"/api/datasetrw/v1/datasets/{dataset_id}/grants",
        headers=headers,
        base_url=base_url,
        json_body={
            "targetId": project_id,
            "targetRole": "DatasetRwEditor",
        },
    )
    if resp.status_code in (200, 201, 204):
        print("  -> Grant succeeded")
        return True
    print(f"  -> Grant failed (HTTP {resp.status_code})")
    return False


async def poll_for_mount(
    dataset_name: str,
    poll_interval: float,
    max_wait: float,
    start_time: float,
) -> Optional[str]:
    """Poll mount paths until one appears or timeout is reached."""
    print(f"\n[step 3] Polling for mount every {poll_interval}s (max {max_wait}s)")
    print(f"  Candidates:")
    report_all_candidates(dataset_name)

    deadline = start_time + max_wait
    poll_count = 0

    while time.monotonic() < deadline:
        poll_count += 1
        elapsed = time.monotonic() - start_time
        mount = probe_all_mounts(dataset_name)

        if mount:
            print(f"\n  >>> MOUNT APPEARED after {elapsed:.1f}s (poll #{poll_count})")
            print(f"  >>> Path: {mount}")
            return mount

        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break

        wait = min(poll_interval, remaining)
        print(f"  [{elapsed:6.1f}s] poll #{poll_count}: not found, waiting {wait:.0f}s...")
        await asyncio.sleep(wait)

    elapsed = time.monotonic() - start_time
    print(f"\n  >>> TIMEOUT after {elapsed:.1f}s ({poll_count} polls) — mount never appeared")
    return None


def test_write_access(mount_path: str) -> bool:
    """Attempt to write and read back a test file."""
    print(f"\n[step 4] Testing write access at {mount_path}")
    test_file = os.path.join(mount_path, ".mount-timing-test")
    try:
        Path(test_file).write_text("mount timing test\n")
        content = Path(test_file).read_text()
        print(f"  -> Write succeeded, read back: {content.strip()!r}")
        os.remove(test_file)
        print("  -> Cleanup succeeded")
        return True
    except PermissionError as e:
        print(f"  -> PermissionError: {e}")
        return False
    except Exception as e:
        print(f"  -> Error: {type(e).__name__}: {e}")
        return False


async def delete_dataset(
    client: httpx.AsyncClient,
    headers: dict[str, str],
    base_url: str,
    dataset_id: str,
) -> bool:
    """Delete the test dataset."""
    print(f"\n[cleanup] Deleting dataset {dataset_id}")
    resp = await api_request(
        client,
        "DELETE",
        f"/api/datasetrw/v1/datasets/{dataset_id}",
        headers=headers,
        base_url=base_url,
    )
    if resp.status_code in (200, 204):
        print("  -> Deleted")
        return True
    print(f"  -> Delete failed (HTTP {resp.status_code})")
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


async def main(
    project_id: str,
    poll_interval: float,
    max_wait: float,
    skip_cleanup: bool,
) -> None:
    base_url = resolve_api_host()
    headers = await get_auth_headers()
    app_project_id = os.environ.get("DOMINO_PROJECT_ID")

    # Generate a unique dataset name for this test run
    dataset_name = f"{TEST_DATASET_PREFIX}-{int(time.time()) % 100000}"

    print(f"\n{'#'*60}")
    print(f"# Dataset Mount Timing Test")
    print(f"# Target project:  {project_id}")
    print(f"# App project:     {app_project_id or '(not set)'}")
    print(f"# Dataset name:    {dataset_name}")
    print(f"# API host:        {base_url}")
    print(f"# Poll interval:   {poll_interval}s")
    print(f"# Max wait:        {max_wait}s")
    print(f"# Skip cleanup:    {skip_cleanup}")
    print(f"{'#'*60}")

    dataset_id: Optional[str] = None
    mount_path: Optional[str] = None
    writable = False

    async with httpx.AsyncClient(timeout=30.0) as client:
        # Step 1: Create dataset
        created = await create_test_dataset(client, headers, base_url, project_id, dataset_name)
        if not created:
            print("\nFATAL: Could not create test dataset. Exiting.")
            return

        dataset_id = str(created.get("datasetId") or created.get("id") or "")
        if not dataset_id:
            print(f"\nFATAL: No dataset ID in create response: {created}")
            return

        print(f"\n  Dataset created: id={dataset_id}")
        start_time = time.monotonic()

        # Step 2: Grant access to app project (if different from target)
        if app_project_id and app_project_id != project_id:
            await grant_project_access(client, headers, base_url, dataset_id, app_project_id)
        elif app_project_id == project_id:
            print("\n[step 2] Skipped — app project IS the target project")
        else:
            print("\n[step 2] Skipped — DOMINO_PROJECT_ID not set")

        # Step 3: Poll for mount
        mount_path = await poll_for_mount(dataset_name, poll_interval, max_wait, start_time)

        # Step 4: Test write access
        if mount_path:
            writable = test_write_access(mount_path)

        # Cleanup
        if dataset_id and not skip_cleanup:
            await delete_dataset(client, headers, base_url, dataset_id)
        elif skip_cleanup:
            print(f"\n[cleanup] Skipped (--skip-cleanup). Dataset '{dataset_name}' (id={dataset_id}) kept.")

    # Final report
    elapsed = time.monotonic() - start_time
    print(f"\n{'#'*60}")
    print(f"# RESULTS")
    print(f"#")
    if mount_path:
        print(f"#   Mount appeared:  YES")
        print(f"#   Time to mount:   {elapsed:.1f}s")
        print(f"#   Mount path:      {mount_path}")
        print(f"#   Writable:        {'YES' if writable else 'NO'}")
        print(f"#")
        print(f"#   CONCLUSION: Mounts appear dynamically without restart.")
        print(f"#   The 503-restart logic in storage_resolver.py can be")
        print(f"#   replaced with a polling/retry approach.")
    else:
        print(f"#   Mount appeared:  NO (after {max_wait}s)")
        print(f"#   Mount path:      none")
        print(f"#   Writable:        n/a")
        print(f"#")
        print(f"#   CONCLUSION: Mounts do NOT appear dynamically.")
        print(f"#   The app MUST restart to pick up new dataset mounts.")
        print(f"#   The current 503 approach in storage_resolver.py is correct.")
    print(f"{'#'*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Test whether Domino dataset mounts appear without app restart"
    )
    parser.add_argument("project_id", help="Domino project ID to create test dataset in")
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=5.0,
        help="Seconds between mount checks (default: 5)",
    )
    parser.add_argument(
        "--max-wait",
        type=float,
        default=120.0,
        help="Maximum seconds to wait for mount (default: 120)",
    )
    parser.add_argument(
        "--skip-cleanup",
        action="store_true",
        help="Keep the test dataset after the test (don't delete it)",
    )
    args = parser.parse_args()
    asyncio.run(main(args.project_id, args.poll_interval, args.max_wait, args.skip_cleanup))
