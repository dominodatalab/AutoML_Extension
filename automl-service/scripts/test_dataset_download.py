#!/usr/bin/env python3
"""Test Domino Dataset RW API — file download from dataset.

Discovery script that probes every plausible download endpoint pattern
to find how to read files from a Domino Dataset via the RW API.

Files are normally accessed via mount paths, but mounts require an app
restart.  This script probes for undocumented HTTP download endpoints.

Usage:
    python scripts/test_dataset_download.py <target_project_id>
    python scripts/test_dataset_download.py <target_project_id> --dataset-name my-dataset
    python scripts/test_dataset_download.py --dataset-id <dataset_id>
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
# File uploaded by test_dataset_upload.py
EXPECTED_FILE = "automl-upload-test.csv"
EXPECTED_CONTENT = "col_a,col_b,col_c\n1,hello,true\n2,world,false\n3,test,true\n"

# ---------------------------------------------------------------------------
# Auth (standalone — no app imports)
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
    extra_headers: Optional[dict[str, str]] = None,
) -> httpx.Response:
    """Send a request and log full details."""
    url = f"{base_url}{path}"
    print(f"\n{'='*60}")
    print(f">>> {method} {url}")
    if params:
        print(f"    params: {json.dumps(params)}")
    if json_body:
        print(f"    body:   {json.dumps(json_body, indent=2)}")
    if extra_headers:
        print(f"    extra headers: {list(extra_headers.keys())}")

    merged_headers = {**headers}
    if extra_headers:
        merged_headers.update(extra_headers)

    resp = await client.request(
        method,
        url,
        json=json_body,
        params=params,
        headers=merged_headers,
    )

    print(f"<<< {resp.status_code} {resp.reason_phrase}")
    content_type = resp.headers.get("content-type", "")
    body_bytes = len(resp.content)
    if "json" in content_type:
        try:
            body = resp.json()
            print(f"    response: {json.dumps(body, indent=2)[:3000]}")
        except Exception:
            print(f"    response (text): {resp.text[:1000]}")
    elif body_bytes > 0 and body_bytes < 5000:
        print(f"    content-type: {content_type}")
        print(f"    response ({body_bytes} bytes): {resp.text[:2000]}")
    else:
        print(f"    content-type: {content_type}")
        print(f"    response size: {body_bytes} bytes")
    print(f"{'='*60}")
    return resp


# ---------------------------------------------------------------------------
# Dataset + snapshot lookup
# ---------------------------------------------------------------------------


async def find_dataset(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    project_id: str,
    name: str,
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
    datasets = [ds.get("dataset", ds) if isinstance(ds, dict) and "dataset" in ds else ds for ds in datasets]
    for ds in datasets:
        ds_name = ds.get("datasetName") or ds.get("name") or ""
        if ds_name == name:
            return ds
    return None


async def get_dataset_details(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[dict]:
    """GET full dataset details via v1."""
    resp = await api_request(
        client,
        "GET",
        f"/api/datasetrw/v1/datasets/{dataset_id}",
        headers=headers,
        base_url=base_url,
    )
    if resp.status_code == 200:
        return resp.json()
    return None


async def get_latest_snapshot_id(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[str]:
    """Get the most recent snapshot ID for a dataset."""
    print(f"\n[discover] Looking up snapshots for dataset {dataset_id}")

    for version in ("v2", "v1"):
        resp = await api_request(
            client,
            "GET",
            f"/api/datasetrw/{version}/datasets/{dataset_id}/snapshots",
            headers=headers,
            base_url=base_url,
        )
        if resp.status_code == 200:
            data = resp.json()
            snapshots = data if isinstance(data, list) else (
                data.get("snapshots") or data.get("items") or []
            )
            if snapshots:
                # Pick the latest (usually first or last depending on sort)
                s = snapshots[0]
                sid = s.get("id") or s.get("snapshotId") or ""
                print(f"  -> Latest snapshot: {sid} (status={s.get('status', '?')})")
                return str(sid) if sid else None

    print("  -> No snapshots found")
    return None


# ---------------------------------------------------------------------------
# Download probes
# ---------------------------------------------------------------------------


def check_content(resp: httpx.Response, label: str) -> bool:
    """Check if a response contains the expected file content."""
    if resp.status_code != 200:
        return False
    body = resp.text
    if body.strip() == EXPECTED_CONTENT.strip():
        print(f"  -> {label}: CONTENT MATCHES expected file!")
        return True
    # Partial match check
    if "col_a" in body and "hello" in body:
        print(f"  -> {label}: Response contains expected data (partial match)")
        print(f"     First 200 chars: {body[:200]}")
        return True
    return False


async def probe_v4_snapshot_file_get(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    file_path: str,
) -> bool:
    """GET variant of the v4 chunked upload endpoint."""
    print(f"\n[probe] v4 snapshot file GET (resumable params)")

    resp = await api_request(
        client, "GET",
        f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file",
        headers=headers, base_url=base_url,
        params={"resumableRelativePath": file_path},
    )
    return check_content(resp, "v4 snapshot file GET")


async def probe_v4_snapshot_files_path(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    snapshot_id: Optional[str],
    file_path: str,
) -> bool:
    """GET /v4/datasetrw/datasets/{id}/snapshot/{snapshotId}/files/{path}"""
    print(f"\n[probe] v4 snapshot files with path")

    if snapshot_id:
        resp = await api_request(
            client, "GET",
            f"/v4/datasetrw/datasets/{dataset_id}/snapshot/{snapshot_id}/files/{file_path}",
            headers=headers, base_url=base_url,
        )
        if check_content(resp, "v4 snapshot/{sid}/files/{path}"):
            return True

    # Also try without snapshot ID (use "head" or "latest" as placeholder)
    for placeholder in ("head", "latest", "active"):
        resp = await api_request(
            client, "GET",
            f"/v4/datasetrw/datasets/{dataset_id}/snapshot/{placeholder}/files/{file_path}",
            headers=headers, base_url=base_url,
        )
        if check_content(resp, f"v4 snapshot/{placeholder}/files/{{path}}"):
            return True

    return False


async def probe_v1_files(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    snapshot_id: Optional[str],
    file_path: str,
) -> bool:
    """Probe v1 file download endpoints."""
    print(f"\n[probe] v1 dataset file endpoints")

    endpoints = [
        f"/api/datasetrw/v1/datasets/{dataset_id}/files/{file_path}",
    ]
    if snapshot_id:
        endpoints.extend([
            f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{file_path}",
            f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/content/{file_path}",
        ])

    for path in endpoints:
        resp = await api_request(
            client, "GET", path, headers=headers, base_url=base_url,
        )
        if check_content(resp, path):
            return True

    return False


async def probe_v2_files(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    snapshot_id: Optional[str],
    file_path: str,
) -> bool:
    """Probe v2 file download endpoints."""
    print(f"\n[probe] v2 dataset file endpoints")

    endpoints = [
        f"/api/datasetrw/v2/datasets/{dataset_id}/files/{file_path}",
    ]
    if snapshot_id:
        endpoints.extend([
            f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{file_path}",
            f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/content/{file_path}",
        ])

    for path in endpoints:
        resp = await api_request(
            client, "GET", path, headers=headers, base_url=base_url,
        )
        if check_content(resp, path):
            return True

    return False


async def probe_v4_files_direct(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    file_path: str,
) -> bool:
    """Probe /v4/datasetrw/datasets/{id}/files/{path}"""
    print(f"\n[probe] v4 direct files path")

    resp = await api_request(
        client, "GET",
        f"/v4/datasetrw/datasets/{dataset_id}/files/{file_path}",
        headers=headers, base_url=base_url,
    )
    return check_content(resp, "v4 files/{path}")


async def probe_legacy_blob(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> bool:
    """Probe legacy blob-style endpoint."""
    print(f"\n[probe] Legacy blob-style endpoint")

    resp = await api_request(
        client, "GET",
        f"/dataset/{dataset_id}",
        headers=headers, base_url=base_url,
    )
    if resp.status_code == 200:
        print(f"  -> Legacy endpoint returned 200 ({len(resp.content)} bytes)")
        return check_content(resp, "legacy /dataset/{id}")
    return False


async def probe_presigned_download(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
    snapshot_id: Optional[str],
    file_path: str,
) -> bool:
    """Try getting a presigned download URL."""
    print(f"\n[probe] Presigned download URL")

    endpoints = [
        ("POST", f"/api/datasetrw/v1/datasets/{dataset_id}/download-url",
         {"filePath": file_path}),
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/download-url",
         {"filePath": file_path}),
        ("GET", f"/api/datasetrw/v1/datasets/{dataset_id}/download-url",
         None),
        ("GET", f"/api/datasetrw/v2/datasets/{dataset_id}/download-url",
         None),
    ]
    if snapshot_id:
        endpoints.extend([
            ("POST", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/download-url",
             {"filePath": file_path}),
            ("GET", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/download-url",
             None),
        ])

    for method, path, body in endpoints:
        params = {"filePath": file_path} if method == "GET" else None
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url,
            json_body=body, params=params,
        )
        if resp.status_code in (200, 201):
            data = resp.json() if "json" in resp.headers.get("content-type", "") else {}
            download_url = (
                data.get("url")
                or data.get("downloadUrl")
                or data.get("presignedUrl")
                or data.get("signedUrl")
            )
            if download_url:
                print(f"  -> Got presigned download URL: {download_url[:100]}...")
                try:
                    dl_resp = await client.get(download_url, timeout=30.0)
                    print(f"  -> GET presigned URL: {dl_resp.status_code} ({len(dl_resp.content)} bytes)")
                    if check_content(dl_resp, "presigned download"):
                        return True
                except Exception as e:
                    print(f"  -> GET presigned URL failed: {e}")

    return False


async def probe_mount_read(dataset_name: str, file_path: str) -> bool:
    """Try reading the file directly from mount paths."""
    print(f"\n[probe] Direct mount read for '{dataset_name}/{file_path}'")

    mount_candidates = [
        f"/domino/datasets/local/{dataset_name}",
        f"/domino/datasets/{dataset_name}",
        f"/mnt/data/{dataset_name}",
        f"/mnt/imported/data/{dataset_name}",
    ]

    for mount in mount_candidates:
        full_path = os.path.join(mount, file_path)
        if os.path.isfile(full_path):
            try:
                with open(full_path, "r") as f:
                    content = f.read()
                print(f"  -> Found file at {full_path} ({len(content)} bytes)")
                if content.strip() == EXPECTED_CONTENT.strip():
                    print(f"  -> CONTENT MATCHES!")
                    return True
                else:
                    print(f"  -> Content differs. First 200 chars: {content[:200]}")
                    return True  # Still counts as a working read path
            except Exception as e:
                print(f"  -> Read failed at {full_path}: {e}")
        elif os.path.isdir(mount):
            print(f"  -> Mount exists at {mount} but file not found")
            # List what's actually in the mount
            try:
                entries = os.listdir(mount)
                print(f"     Contents: {entries[:20]}")
            except Exception as e:
                print(f"     Could not list: {e}")

    print("  -> No readable mount found")
    return False


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

    print(f"\n{'#'*60}")
    print(f"# Domino Dataset File Download Test")
    print(f"# Target project:  {target_project_id or '(from dataset lookup)'}")
    print(f"# Dataset name:    {dataset_name}")
    print(f"# Dataset ID:      {dataset_id or '(will look up)'}")
    print(f"# Expected file:   {EXPECTED_FILE}")
    print(f"# API host:        {base_url}")
    print(f"{'#'*60}")

    async with httpx.AsyncClient(timeout=60.0) as client:
        # Resolve dataset ID
        if not dataset_id:
            if not target_project_id:
                print("\nERROR: Provide either --dataset-id or target_project_id")
                sys.exit(1)

            ds = await find_dataset(client, headers, base_url, target_project_id, dataset_name)
            if not ds:
                print(f"\nDataset '{dataset_name}' not found in project {target_project_id}")
                print("Run test_dataset_upload.py first to create and upload a file.")
                sys.exit(1)
            dataset_id = str(ds.get("datasetId") or ds.get("id"))
            print(f"\n  Found dataset: id={dataset_id}")

        # Get dataset details
        details = await get_dataset_details(client, headers, base_url, dataset_id)

        # Get latest snapshot ID (needed for snapshot-scoped endpoints)
        snapshot_id = await get_latest_snapshot_id(client, headers, base_url, dataset_id)

        # --- Download probes ---
        results = {}

        # Probe 1: v4 snapshot file GET (resumable params)
        results["v4_snapshot_file_get"] = await probe_v4_snapshot_file_get(
            client, headers, base_url, dataset_id, EXPECTED_FILE,
        )

        # Probe 2: v4 snapshot/{snapshotId}/files/{path}
        results["v4_snapshot_files_path"] = await probe_v4_snapshot_files_path(
            client, headers, base_url, dataset_id, snapshot_id, EXPECTED_FILE,
        )

        # Probe 3: v1 file endpoints
        results["v1_files"] = await probe_v1_files(
            client, headers, base_url, dataset_id, snapshot_id, EXPECTED_FILE,
        )

        # Probe 4: v2 file endpoints
        results["v2_files"] = await probe_v2_files(
            client, headers, base_url, dataset_id, snapshot_id, EXPECTED_FILE,
        )

        # Probe 5: v4 direct files path
        results["v4_files_direct"] = await probe_v4_files_direct(
            client, headers, base_url, dataset_id, EXPECTED_FILE,
        )

        # Probe 6: Legacy blob endpoint
        results["legacy_blob"] = await probe_legacy_blob(
            client, headers, base_url, dataset_id,
        )

        # Probe 7: Presigned download URL
        results["presigned_download"] = await probe_presigned_download(
            client, headers, base_url, dataset_id, snapshot_id, EXPECTED_FILE,
        )

        # Probe 8: Direct mount read (bypass API)
        results["mount_read"] = await probe_mount_read(dataset_name, EXPECTED_FILE)

    # Summary
    print(f"\n{'#'*60}")
    print("# Download Test Summary")
    print(f"#   Dataset ID:              {dataset_id}")
    print(f"#   Snapshot ID:             {snapshot_id or '(none found)'}")
    print(f"#   Target file:             {EXPECTED_FILE}")
    print(f"#")
    for key, worked in results.items():
        status = "WORKED" if worked else "FAILED"
        print(f"#   {key:30s} {status}")
    print(f"#")
    any_worked = any(results.values())
    if any_worked:
        working = [k for k, v in results.items() if v]
        print(f"#   RESULT: Download possible via: {', '.join(working)}")
    else:
        print(f"#   RESULT: No download method worked — check responses above")
    print(f"{'#'*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Domino Dataset file download")
    parser.add_argument(
        "target_project_id", nargs="?",
        help="Target project ID (optional if --dataset-id given)",
    )
    parser.add_argument("--dataset-id", help="Dataset ID (skip lookup)")
    parser.add_argument(
        "--dataset-name", default=DATASET_NAME,
        help=f"Dataset name (default: {DATASET_NAME})",
    )
    args = parser.parse_args()

    if not args.target_project_id and not args.dataset_id:
        parser.error("Provide either target_project_id or --dataset-id")

    asyncio.run(main(args.target_project_id, args.dataset_id, args.dataset_name))
