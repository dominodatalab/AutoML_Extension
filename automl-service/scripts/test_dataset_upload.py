#!/usr/bin/env python3
"""Test Domino Dataset RW API — file upload to dataset.

Discovers how to upload files to a Domino Dataset via the RW API.
Domino Datasets may use snapshots, blobs, presigned URLs, or direct
multipart upload — this script probes all known patterns.

Usage:
    python scripts/test_dataset_upload.py <target_project_id>
    python scripts/test_dataset_upload.py <target_project_id> --dataset-name my-dataset
    python scripts/test_dataset_upload.py --dataset-id <dataset_id>
"""

import argparse
import asyncio
import hashlib
import io
import json
import os
import sys
from typing import Any, Optional

import httpx

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

DATASET_NAME = "automl-extension"
TEST_FILE_NAME = "automl-upload-test.csv"
TEST_FILE_CONTENT = "col_a,col_b,col_c\n1,hello,true\n2,world,false\n3,test,true\n"

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
    content: Optional[bytes] = None,
    files: Optional[dict] = None,
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
    if content:
        print(f"    content: {len(content)} bytes")
    if files:
        print(f"    files: {list(files.keys())}")
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
        content=content,
        files=files,
    )

    print(f"<<< {resp.status_code} {resp.reason_phrase}")
    content_type = resp.headers.get("content-type", "")
    if "json" in content_type:
        try:
            body = resp.json()
            print(f"    response: {json.dumps(body, indent=2)[:3000]}")
        except Exception:
            print(f"    response (text): {resp.text[:1000]}")
    else:
        print(f"    content-type: {content_type}")
        print(f"    response (text): {resp.text[:1000]}")
    print(f"{'='*60}")
    return resp


# ---------------------------------------------------------------------------
# Dataset lookup
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
    # v2 wraps each item as {"dataset": {...}} — unwrap
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
    """GET full dataset details."""
    # v1 is the working endpoint for single-dataset GET
    for version in ("v1", "v2"):
        resp = await api_request(
            client,
            "GET",
            f"/api/datasetrw/{version}/datasets/{dataset_id}",
            headers=headers,
            base_url=base_url,
        )
        if resp.status_code == 200:
            return resp.json()
    return None


# ---------------------------------------------------------------------------
# Upload discovery: try every known pattern
# ---------------------------------------------------------------------------


async def probe_v4_chunked_upload(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> bool:
    """Domino's actual upload workflow via /v4/datasetrw/ chunked upload API.

    This is the same flow used by the python-domino SDK:
      1. POST .../snapshot/file/start → get upload_key
      2. POST .../snapshot/file?key=...&chunk params → upload chunk(s)
      3. GET  .../snapshot/file/end/{upload_key} → finalize
    """
    print(f"\n[probe] v4 chunked upload workflow for dataset {dataset_id}")

    file_bytes = TEST_FILE_CONTENT.encode()
    file_checksum = hashlib.md5(file_bytes).hexdigest()
    # Use filename as identifier (same as python-domino)
    identifier = TEST_FILE_NAME.replace(".", "-").replace("/", "-")

    # Step 1: Start upload session
    start_body = {
        "filePaths": [TEST_FILE_NAME],
        "fileCollisionSetting": "Overwrite",
    }
    resp = await api_request(
        client,
        "POST",
        f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/start",
        headers=headers,
        base_url=base_url,
        json_body=start_body,
    )
    if resp.status_code not in (200, 201):
        print(f"  -> Start upload failed ({resp.status_code})")
        return False

    data = resp.json()
    # Response may be a plain string (the key itself) or a dict
    if isinstance(data, str):
        upload_key = data
    elif isinstance(data, dict):
        upload_key = data.get("upload_key") or data.get("uploadKey") or data.get("key")
    else:
        upload_key = None
    if not upload_key:
        print(f"  -> No upload key in response: {data!r}")
        return False
    print(f"  -> Upload key: {upload_key}")

    # Step 2: Upload single chunk as multipart form data (matching python-domino SDK)
    chunk_params = {
        "key": upload_key,
        "resumableChunkNumber": 1,
        "resumableChunkSize": len(file_bytes),
        "resumableCurrentChunkSize": len(file_bytes),
        "resumableTotalChunks": 1,
        "resumableIdentifier": identifier,
        "resumableRelativePath": TEST_FILE_NAME,
        "checksum": file_checksum,
    }
    resp = await api_request(
        client,
        "POST",
        f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file",
        headers=headers,
        base_url=base_url,
        params=chunk_params,
        files={TEST_FILE_NAME: (TEST_FILE_NAME, io.BytesIO(file_bytes), "application/octet-stream")},
        extra_headers={"Csrf-Token": "nocheck"},
    )
    if resp.status_code not in (200, 201, 204):
        print(f"  -> Chunk upload failed ({resp.status_code})")
        # Try to cancel
        await api_request(
            client, "GET",
            f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/cancel/{upload_key}",
            headers=headers, base_url=base_url,
        )
        return False
    print(f"  -> Chunk uploaded successfully")

    # Step 3: End upload session
    resp = await api_request(
        client,
        "GET",
        f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/end/{upload_key}",
        headers=headers,
        base_url=base_url,
    )
    if resp.status_code in (200, 201, 204):
        print(f"  -> Upload finalized successfully!")
        return True
    else:
        print(f"  -> End upload failed ({resp.status_code})")
        return False


async def probe_snapshot_workflow(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[dict]:
    """Domino Datasets use snapshots — try to create one and upload into it.

    Typical flow:
      1. POST .../snapshots → get snapshot ID
      2. Upload file(s) into the snapshot
      3. Commit the snapshot
    """
    print(f"\n[probe] Snapshot-based upload workflow for dataset {dataset_id}")

    # Step 1: Try to create a snapshot
    snapshot_endpoints = [
        ("/api/datasetrw/v2/datasets/{id}/snapshots", {"description": "automl test upload"}),
        ("/api/datasetrw/v2/datasets/{id}/snapshot", {"description": "automl test upload"}),
        ("/api/datasetrw/v1/datasets/{id}/snapshots", {"description": "automl test upload"}),
    ]

    snapshot_id = None
    for path_tpl, body in snapshot_endpoints:
        path = path_tpl.format(id=dataset_id)
        resp = await api_request(
            client, "POST", path, headers=headers, base_url=base_url, json_body=body
        )
        if resp.status_code in (200, 201):
            data = resp.json()
            snapshot_id = (
                data.get("snapshotId")
                or data.get("id")
                or data.get("snapshot", {}).get("id")
            )
            print(f"  -> Snapshot created: {snapshot_id}")
            break

    if not snapshot_id:
        print("  -> No snapshot endpoint worked")
        return None

    # Step 2: Upload file into the snapshot
    file_bytes = TEST_FILE_CONTENT.encode()
    upload_attempts = [
        # Multipart form upload
        (
            "PUT",
            f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{TEST_FILE_NAME}",
            {"content": file_bytes, "extra_headers": {"Content-Type": "application/octet-stream"}},
        ),
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/files",
            {"files": {"file": (TEST_FILE_NAME, io.BytesIO(file_bytes), "text/csv")}},
        ),
        (
            "PUT",
            f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/{TEST_FILE_NAME}",
            {"content": file_bytes, "extra_headers": {"Content-Type": "application/octet-stream"}},
        ),
        # v1 variants
        (
            "PUT",
            f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{TEST_FILE_NAME}",
            {"content": file_bytes, "extra_headers": {"Content-Type": "application/octet-stream"}},
        ),
        (
            "POST",
            f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files",
            {"files": {"file": (TEST_FILE_NAME, io.BytesIO(file_bytes), "text/csv")}},
        ),
    ]

    upload_ok = False
    for method, path, kwargs in upload_attempts:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url, **kwargs
        )
        if resp.status_code in (200, 201, 204):
            print(f"  -> File uploaded via {method} {path}")
            upload_ok = True
            break

    # Step 3: Commit the snapshot (even if upload failed — to see the API shape)
    commit_endpoints = [
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/commit"),
        ("PUT", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/status",
         {"status": "committed"}),
        ("PATCH", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}",
         {"status": "committed"}),
    ]

    for item in commit_endpoints:
        method = item[0]
        path = item[1]
        body = item[2] if len(item) > 2 else None
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url, json_body=body
        )
        if resp.status_code in (200, 201, 204):
            print(f"  -> Snapshot committed via {method} {path}")
            break

    return {"snapshot_id": snapshot_id, "upload_ok": upload_ok}


async def probe_direct_file_upload(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> bool:
    """Try direct file upload (no snapshot) — some Domino versions support this."""
    print(f"\n[probe] Direct file upload (no snapshot) for dataset {dataset_id}")

    file_bytes = TEST_FILE_CONTENT.encode()

    attempts = [
        # PUT raw bytes to a file path
        (
            "PUT",
            f"/api/datasetrw/v2/datasets/{dataset_id}/files/{TEST_FILE_NAME}",
            {"content": file_bytes, "extra_headers": {"Content-Type": "application/octet-stream"}},
        ),
        # POST multipart
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/files",
            {"files": {"file": (TEST_FILE_NAME, io.BytesIO(file_bytes), "text/csv")}},
        ),
        # POST multipart to upload path
        (
            "POST",
            f"/api/datasetrw/v2/datasets/{dataset_id}/upload",
            {"files": {"file": (TEST_FILE_NAME, io.BytesIO(file_bytes), "text/csv")}},
        ),
        # v1 variants
        (
            "PUT",
            f"/api/datasetrw/v1/datasets/{dataset_id}/files/{TEST_FILE_NAME}",
            {"content": file_bytes, "extra_headers": {"Content-Type": "application/octet-stream"}},
        ),
        (
            "POST",
            f"/api/datasetrw/v1/datasets/{dataset_id}/files",
            {"files": {"file": (TEST_FILE_NAME, io.BytesIO(file_bytes), "text/csv")}},
        ),
    ]

    for method, path, kwargs in attempts:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url, **kwargs
        )
        if resp.status_code in (200, 201, 204):
            print(f"  -> Direct upload succeeded via {method} {path}")
            return True

    print("  -> No direct upload endpoint worked")
    return False


async def probe_presigned_upload(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> bool:
    """Try presigned URL workflow: request a presigned URL, then upload to it."""
    print(f"\n[probe] Presigned URL upload workflow for dataset {dataset_id}")

    presign_endpoints = [
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/upload-url",
         {"fileName": TEST_FILE_NAME}),
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/presigned-url",
         {"fileName": TEST_FILE_NAME, "contentType": "text/csv"}),
        ("GET", f"/api/datasetrw/v2/datasets/{dataset_id}/upload-url",
         None),  # params variant
        ("POST", f"/api/datasetrw/v2/datasets/{dataset_id}/files/upload-url",
         {"fileName": TEST_FILE_NAME}),
        ("POST", f"/api/datasetrw/v1/datasets/{dataset_id}/upload-url",
         {"fileName": TEST_FILE_NAME}),
    ]

    for method, path, body in presign_endpoints:
        params = {"fileName": TEST_FILE_NAME} if method == "GET" and body is None else None
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url,
            json_body=body, params=params
        )
        if resp.status_code in (200, 201):
            data = resp.json()
            upload_url = (
                data.get("url")
                or data.get("uploadUrl")
                or data.get("presignedUrl")
                or data.get("signedUrl")
            )
            if upload_url:
                print(f"  -> Got presigned URL: {upload_url[:100]}...")
                # Try uploading to the presigned URL
                file_bytes = TEST_FILE_CONTENT.encode()
                try:
                    put_resp = await client.put(
                        upload_url,
                        content=file_bytes,
                        headers={"Content-Type": "text/csv"},
                    )
                    print(f"  -> PUT to presigned URL: {put_resp.status_code}")
                    if put_resp.status_code in (200, 201, 204):
                        print("  -> Presigned upload SUCCEEDED")
                        return True
                except Exception as e:
                    print(f"  -> PUT to presigned URL failed: {e}")
            else:
                print(f"  -> Response had no recognizable URL field. Keys: {list(data.keys())}")

    print("  -> No presigned upload endpoint worked")
    return False


async def probe_mount_write(dataset_name: str) -> bool:
    """Bypass the API entirely — write directly to the mounted dataset path."""
    print(f"\n[probe] Direct mount write for dataset '{dataset_name}'")

    mount_candidates = [
        f"/domino/datasets/local/{dataset_name}",
        f"/domino/datasets/{dataset_name}",
        f"/mnt/data/{dataset_name}",
        f"/mnt/imported/data/{dataset_name}",
    ]

    for mount in mount_candidates:
        if not os.path.isdir(mount):
            continue
        if not os.access(mount, os.W_OK):
            print(f"  {mount}: exists but NOT writable")
            continue

        test_path = os.path.join(mount, TEST_FILE_NAME)
        try:
            with open(test_path, "w") as f:
                f.write(TEST_FILE_CONTENT)
            # Verify
            with open(test_path, "r") as f:
                readback = f.read()
            if readback == TEST_FILE_CONTENT:
                print(f"  -> Mount write SUCCEEDED at {test_path}")
                print(f"     File size: {os.path.getsize(test_path)} bytes")
                # Leave the file for inspection (don't clean up)
                return True
            else:
                print(f"  -> Write/readback mismatch at {test_path}")
        except Exception as e:
            print(f"  -> Write failed at {test_path}: {e}")

    print("  -> No writable mount found")
    return False


async def list_dataset_files(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[list]:
    """Try to list files in the dataset to verify upload."""
    print(f"\n[verify] Listing files in dataset {dataset_id}")

    file_list_endpoints = [
        ("GET", f"/api/datasetrw/v2/datasets/{dataset_id}/files"),
        ("GET", f"/api/datasetrw/v2/datasets/{dataset_id}/contents"),
        ("GET", f"/api/datasetrw/v1/datasets/{dataset_id}/files"),
    ]

    for method, path in file_list_endpoints:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url
        )
        if resp.status_code == 200:
            data = resp.json()
            files = data if isinstance(data, list) else (
                data.get("files") or data.get("items") or data.get("contents") or []
            )
            print(f"  -> Found {len(files)} file(s)")
            for f in files[:20]:
                if isinstance(f, dict):
                    print(f"     - {f.get('fileName') or f.get('name') or f.get('path', '?')}"
                          f"  ({f.get('size', f.get('sizeBytes', '?'))} bytes)")
                else:
                    print(f"     - {f}")
            return files

    print("  -> No file listing endpoint worked")
    return None


async def list_snapshots(
    client: httpx.AsyncClient,
    headers: dict,
    base_url: str,
    dataset_id: str,
) -> Optional[list]:
    """List snapshots for a dataset to understand the data model."""
    print(f"\n[discover] Listing snapshots for dataset {dataset_id}")

    endpoints = [
        ("GET", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots"),
        ("GET", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots"),
    ]

    for method, path in endpoints:
        resp = await api_request(
            client, method, path, headers=headers, base_url=base_url
        )
        if resp.status_code == 200:
            data = resp.json()
            snapshots = data if isinstance(data, list) else (
                data.get("snapshots") or data.get("items") or []
            )
            print(f"  -> Found {len(snapshots)} snapshot(s)")
            for s in snapshots[:10]:
                if isinstance(s, dict):
                    print(f"     - id={s.get('id', s.get('snapshotId', '?'))}"
                          f"  status={s.get('status', '?')}"
                          f"  created={s.get('createdAt', s.get('created', '?'))}")
            return snapshots

    print("  -> No snapshot listing endpoint worked")
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

    print(f"\n{'#'*60}")
    print(f"# Domino Dataset File Upload Test")
    print(f"# Target project:  {target_project_id or '(from dataset lookup)'}")
    print(f"# Dataset name:    {dataset_name}")
    print(f"# Dataset ID:      {dataset_id or '(will look up)'}")
    print(f"# Test file:       {TEST_FILE_NAME} ({len(TEST_FILE_CONTENT)} bytes)")
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
                print("Run test_dataset_api.py first to create it.")
                sys.exit(1)
            dataset_id = ds.get("datasetId") or ds.get("id")
            print(f"\n  Found dataset: id={dataset_id}")

        # Get dataset details for context
        details = await get_dataset_details(client, headers, base_url, dataset_id)

        # List existing snapshots
        snapshots = await list_snapshots(client, headers, base_url, dataset_id)

        # List existing files
        files_before = await list_dataset_files(client, headers, base_url, dataset_id)

        # --- Upload probes ---
        results = {}

        # Probe 0: v4 chunked upload (actual Domino SDK workflow)
        results["v4_chunked"] = await probe_v4_chunked_upload(
            client, headers, base_url, dataset_id
        )

        # Probe 1: Snapshot-based workflow (v1 API)
        snapshot_result = await probe_snapshot_workflow(
            client, headers, base_url, dataset_id
        )
        results["snapshot"] = bool(snapshot_result and snapshot_result.get("upload_ok"))

        # Probe 2: Direct file upload (no snapshot)
        results["direct"] = await probe_direct_file_upload(
            client, headers, base_url, dataset_id
        )

        # Probe 3: Presigned URL workflow
        results["presigned"] = await probe_presigned_upload(
            client, headers, base_url, dataset_id
        )

        # Probe 4: Direct mount write (bypass API)
        results["mount_write"] = await probe_mount_write(dataset_name)

        # Verify: list files again to see if anything appeared
        files_after = await list_dataset_files(client, headers, base_url, dataset_id)

    # Summary
    print(f"\n{'#'*60}")
    print("# Upload Test Summary")
    print(f"#   Dataset ID:        {dataset_id}")
    print(f"#")
    print(f"#   v4 chunked upload: {'WORKED' if results['v4_chunked'] else 'FAILED'}")
    print(f"#   Snapshot workflow: {'WORKED' if results['snapshot'] else 'FAILED'}")
    print(f"#   Direct upload:     {'WORKED' if results['direct'] else 'FAILED'}")
    print(f"#   Presigned URL:     {'WORKED' if results['presigned'] else 'FAILED'}")
    print(f"#   Mount write:       {'WORKED' if results['mount_write'] else 'FAILED'}")
    print(f"#")
    any_worked = any(results.values())
    if any_worked:
        working = [k for k, v in results.items() if v]
        print(f"#   RESULT: Upload possible via: {', '.join(working)}")
    else:
        print(f"#   RESULT: No upload method worked — check responses above")
    print(f"{'#'*60}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test Domino Dataset file upload")
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
