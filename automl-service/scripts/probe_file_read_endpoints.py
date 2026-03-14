#!/usr/bin/env python3
"""Probe Domino API for any file read/download/content endpoint.

Uploads a small test file to a temporary dataset, then systematically
tries every plausible endpoint pattern to read it back. Reports which
endpoints return data vs 404/403/etc.

Usage:
    python scripts/probe_file_read_endpoints.py
    python scripts/probe_file_read_endpoints.py --keep  # don't delete dataset
"""

import argparse
import asyncio
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.domino_http import (
    domino_request,
    get_domino_auth_headers,
    resolve_domino_api_host,
)
from app.services.storage_resolver import ProjectStorageResolver

# Test file to upload
TEST_FILE_PATH = "uploads/probe_test.csv"
TEST_FILE_CONTENT = b"id,name,value\n1,alpha,10.5\n2,beta,20.3\n3,gamma,30.1\n"


async def setup_test_dataset(project_id: str) -> tuple[str, str]:
    """Create a temp dataset and upload a test file. Returns (dataset_id, snapshot_id)."""
    print("[Setup] Creating temporary test dataset...")
    resp = await domino_request(
        "POST",
        "/api/datasetrw/v1/datasets",
        json={
            "name": f"probe-test-{int(time.time())}",
            "projectId": project_id,
            "description": "Temporary probe dataset — safe to delete",
        },
    )
    body = resp.json()
    dataset_id = str(
        body.get("datasetId") or body.get("id")
        or (body.get("dataset") or {}).get("id") or ""
    )
    print(f"[Setup] Created dataset: {dataset_id}")

    print("[Setup] Uploading test file...")
    resolver = ProjectStorageResolver()
    await resolver.upload_file(dataset_id, TEST_FILE_PATH, TEST_FILE_CONTENT)
    print(f"[Setup] Uploaded '{TEST_FILE_PATH}' ({len(TEST_FILE_CONTENT)} bytes)")

    # Wait for snapshot to settle
    print("[Setup] Waiting 3s for snapshot...")
    await asyncio.sleep(3)

    snapshot_id = await resolver._get_latest_snapshot_id(dataset_id)
    print(f"[Setup] Latest snapshot: {snapshot_id or '(none)'}")

    return dataset_id, snapshot_id or ""


async def probe_endpoint(
    method: str, path: str, *, label: str, expect_binary: bool = False,
    params: dict = None, json_body: dict = None,
) -> dict:
    """Try a single endpoint and return result info."""
    try:
        if json_body:
            resp = await domino_request(
                method, path, json=json_body, max_retries=0, timeout=15.0,
            )
        elif params:
            resp = await domino_request(
                method, path, params=params, max_retries=0, timeout=15.0,
            )
        else:
            resp = await domino_request(
                method, path, max_retries=0, timeout=15.0,
            )

        content_type = resp.headers.get("content-type", "")
        content_len = len(resp.content)

        # Check if we got actual file content back
        is_csv = b"id,name,value" in resp.content[:200]
        is_json = "json" in content_type

        result = {
            "status": resp.status_code,
            "content_type": content_type,
            "content_length": content_len,
            "is_csv": is_csv,
            "is_json": is_json,
            "preview": "",
        }

        if is_csv:
            result["preview"] = resp.content[:200].decode("utf-8", errors="replace")
        elif is_json:
            try:
                result["preview"] = str(resp.json())[:300]
            except Exception:
                result["preview"] = resp.text[:300]
        else:
            result["preview"] = resp.content[:200].decode("utf-8", errors="replace")

        return result

    except Exception as e:
        error_str = str(e)
        status = ""
        if "404" in error_str:
            status = "404"
        elif "403" in error_str:
            status = "403"
        elif "405" in error_str:
            status = "405"
        elif "500" in error_str:
            status = "500"
        elif "502" in error_str:
            status = "502"
        else:
            status = "ERR"
        return {"status": status, "error": error_str[:200]}


def print_result(label: str, endpoint: str, result: dict):
    """Print a single probe result."""
    status = result.get("status", "?")
    if result.get("is_csv"):
        icon = "★ FILE CONTENT"
        color = "\033[92m"  # green
    elif result.get("is_json"):
        icon = "● JSON"
        color = "\033[93m"  # yellow
    elif result.get("error"):
        icon = "✗"
        color = "\033[91m"  # red
    else:
        icon = "?"
        color = "\033[90m"  # gray

    reset = "\033[0m"
    print(f"  {color}{icon} [{status}]{reset} {label}")
    print(f"       {endpoint}")

    if result.get("is_csv"):
        print(f"       Content: {result['preview'][:100]}")
    elif result.get("preview") and not result.get("error"):
        print(f"       Response: {result['preview'][:150]}")
    elif result.get("error"):
        # Abbreviate common errors
        err = result["error"]
        if "404" in err:
            print(f"       404 Not Found")
        elif "403" in err:
            print(f"       403 Forbidden")
        elif "405" in err:
            print(f"       405 Method Not Allowed")
        else:
            print(f"       {err[:120]}")


async def run_probes(dataset_id: str, snapshot_id: str):
    """Try every plausible endpoint pattern."""
    file_path = TEST_FILE_PATH  # "uploads/probe_test.csv"
    file_name = "probe_test.csv"
    encoded_path = "uploads%2Fprobe_test.csv"

    print("\n" + "=" * 70)
    print("PROBING FILE READ/DOWNLOAD ENDPOINTS")
    print("=" * 70)

    # ── Group 1: v1 snapshot-based file endpoints ──
    print("\n── v1 snapshot-based ──")

    if snapshot_id:
        endpoints_v1_snap = [
            ("v1 snap /files/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{file_path}"),
            ("v1 snap /files?path=", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files?path={file_path}"),
            ("v1 snap /file/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/file/{file_path}"),
            ("v1 snap /file/content/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/file/content/{file_path}"),
            ("v1 snap /content/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/content/{file_path}"),
            ("v1 snap /download/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/download/{file_path}"),
            ("v1 snap /read/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/read/{file_path}"),
            ("v1 snap /blob/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/blob/{file_path}"),
        ]
        for label, ep in endpoints_v1_snap:
            result = await probe_endpoint("GET", ep, label=label)
            print_result(label, ep, result)

    # ── Group 2: v1 direct (no snapshot) ──
    print("\n── v1 direct (no snapshot) ──")
    endpoints_v1_direct = [
        ("v1 /files/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/files/{file_path}"),
        ("v1 /files?path=", f"/api/datasetrw/v1/datasets/{dataset_id}/files?path={file_path}"),
        ("v1 /file/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/file/{file_path}"),
        ("v1 /file/content/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/file/content/{file_path}"),
        ("v1 /content/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/content/{file_path}"),
        ("v1 /download/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/download/{file_path}"),
        ("v1 /read/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/read/{file_path}"),
        ("v1 /blob/{path}", f"/api/datasetrw/v1/datasets/{dataset_id}/blob/{file_path}"),
    ]
    for label, ep in endpoints_v1_direct:
        result = await probe_endpoint("GET", ep, label=label)
        print_result(label, ep, result)

    # ── Group 3: v2 endpoints ──
    print("\n── v2 endpoints ──")
    endpoints_v2 = [
        ("v2 /files/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/files/{file_path}"),
        ("v2 /file/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/file/{file_path}"),
        ("v2 /content/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/content/{file_path}"),
        ("v2 /download/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/download/{file_path}"),
    ]
    if snapshot_id:
        endpoints_v2.extend([
            ("v2 snap /files/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/files/{file_path}"),
            ("v2 snap /file/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/file/{file_path}"),
            ("v2 snap /content/{path}", f"/api/datasetrw/v2/datasets/{dataset_id}/snapshots/{snapshot_id}/content/{file_path}"),
        ])
    for label, ep in endpoints_v2:
        result = await probe_endpoint("GET", ep, label=label)
        print_result(label, ep, result)

    # ── Group 4: v4 endpoints (same prefix as upload) ──
    print("\n── v4 endpoints (upload API prefix) ──")
    endpoints_v4 = [
        ("v4 /files/{path}", f"/v4/datasetrw/datasets/{dataset_id}/files/{file_path}"),
        ("v4 /file/{path}", f"/v4/datasetrw/datasets/{dataset_id}/file/{file_path}"),
        ("v4 /snapshot/file/{path}", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/{file_path}"),
        ("v4 /snapshot/file?path=", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file?path={file_path}"),
        ("v4 /snapshot/file/read/{path}", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/read/{file_path}"),
        ("v4 /snapshot/file/download/{path}", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/download/{file_path}"),
        ("v4 /snapshot/file/content/{path}", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/content/{file_path}"),
        ("v4 /snapshot/files/{path}", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/files/{file_path}"),
        ("v4 /content/{path}", f"/v4/datasetrw/datasets/{dataset_id}/content/{file_path}"),
        ("v4 /download/{path}", f"/v4/datasetrw/datasets/{dataset_id}/download/{file_path}"),
        ("v4 /read/{path}", f"/v4/datasetrw/datasets/{dataset_id}/read/{file_path}"),
        ("v4 /blob/{path}", f"/v4/datasetrw/datasets/{dataset_id}/blob/{file_path}"),
    ]
    for label, ep in endpoints_v4:
        result = await probe_endpoint("GET", ep, label=label)
        print_result(label, ep, result)

    # ── Group 5: snapshot-level file read (v1 snapshot ID in path) ──
    if snapshot_id:
        print("\n── v1 snapshot top-level ──")
        endpoints_snap_top = [
            ("v1 /snapshots/{snap}/files/{path}", f"/api/datasetrw/v1/snapshots/{snapshot_id}/files/{file_path}"),
            ("v1 /snapshots/{snap}/file/{path}", f"/api/datasetrw/v1/snapshots/{snapshot_id}/file/{file_path}"),
            ("v1 /snapshots/{snap}/content/{path}", f"/api/datasetrw/v1/snapshots/{snapshot_id}/content/{file_path}"),
            ("v1 /snapshots/{snap}/download/{path}", f"/api/datasetrw/v1/snapshots/{snapshot_id}/download/{file_path}"),
        ]
        for label, ep in endpoints_snap_top:
            result = await probe_endpoint("GET", ep, label=label)
            print_result(label, ep, result)

    # ── Group 6: Query-param style ──
    print("\n── Query param style ──")
    endpoints_query = [
        ("v1 ?fileName=", f"/api/datasetrw/v1/datasets/{dataset_id}/files"),
        ("v4 ?filePath=", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file"),
    ]
    query_params_list = [
        {"fileName": file_path},
        {"filePath": file_path},
        {"path": file_path},
        {"file": file_path},
        {"key": file_path},
    ]
    for base_label, ep in endpoints_query:
        for params in query_params_list:
            param_key = list(params.keys())[0]
            label = f"{base_label.split('?')[0]}?{param_key}="
            result = await probe_endpoint("GET", ep, label=label, params=params)
            print_result(label, ep + "?" + "&".join(f"{k}={v}" for k, v in params.items()), result)

    # ── Group 7: POST-based read (some APIs use POST for file retrieval) ──
    print("\n── POST-based file read ──")
    post_endpoints = [
        ("POST v1 /files/read", f"/api/datasetrw/v1/datasets/{dataset_id}/files/read",
         {"filePath": file_path}),
        ("POST v1 /files/download", f"/api/datasetrw/v1/datasets/{dataset_id}/files/download",
         {"filePath": file_path}),
        ("POST v4 /snapshot/file/read", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/read",
         {"filePath": file_path}),
        ("POST v4 /snapshot/file/download", f"/v4/datasetrw/datasets/{dataset_id}/snapshot/file/download",
         {"filePaths": [file_path]}),
        ("POST v1 /files/presigned", f"/api/datasetrw/v1/datasets/{dataset_id}/files/presigned",
         {"filePath": file_path}),
        ("POST v4 /presigned-url", f"/v4/datasetrw/datasets/{dataset_id}/presigned-url",
         {"filePath": file_path}),
        ("POST v1 /snapshots/{snap}/files/download",
         f"/api/datasetrw/v1/datasets/{dataset_id}/snapshots/{snapshot_id}/files/download" if snapshot_id else "",
         {"filePaths": [file_path]}),
    ]
    for label, ep, body in post_endpoints:
        if not ep:
            continue
        result = await probe_endpoint("POST", ep, label=label, json_body=body)
        print_result(label, ep, result)

    # ── Group 8: Object store / data API (non-datasetrw paths) ──
    print("\n── Alternative API paths ──")
    alt_endpoints = [
        ("data-api /datasets/{id}/files/{path}", f"/api/data/v1/datasets/{dataset_id}/files/{file_path}"),
        ("data-api /datasets/{id}/read/{path}", f"/api/data/v1/datasets/{dataset_id}/read/{file_path}"),
        ("/datasets/{id}", f"/dataset/{dataset_id}"),
        ("/datasets/{id}/file/{path}", f"/dataset/{dataset_id}/file/{file_path}"),
        ("objectstore /datasets/{id}/{path}", f"/objectstore/datasets/{dataset_id}/{file_path}"),
        ("v1 files /{path}", f"/v1/files/{dataset_id}/{file_path}"),
        ("nucleus /datasetrw/{id}/files", f"/nucleus/v1/datasetrw/{dataset_id}/files/{file_path}"),
    ]
    for label, ep in alt_endpoints:
        result = await probe_endpoint("GET", ep, label=label)
        print_result(label, ep, result)

    print("\n" + "=" * 70)
    print("PROBE COMPLETE")
    print("=" * 70)
    print("\nLegend: ★ = file content returned, ● = JSON response, ✗ = error/404")


async def cleanup_dataset(dataset_id: str):
    """Delete the test dataset."""
    print(f"\n[Cleanup] Deleting dataset {dataset_id}...")
    try:
        await domino_request("DELETE", f"/api/datasetrw/v1/datasets/{dataset_id}")
        print("[Cleanup] Done.")
    except Exception as e:
        print(f"[Cleanup] Warning: {e}")


async def main():
    parser = argparse.ArgumentParser(description="Probe Domino file read endpoints")
    parser.add_argument(
        "--project-id",
        default=os.environ.get("DOMINO_PROJECT_ID"),
        help="Project ID (default: DOMINO_PROJECT_ID env var)",
    )
    parser.add_argument("--keep", action="store_true", help="Don't delete test dataset")
    parser.add_argument(
        "--dataset-id",
        help="Use existing dataset ID instead of creating a new one",
    )
    parser.add_argument(
        "--snapshot-id",
        help="Use specific snapshot ID (requires --dataset-id)",
    )
    args = parser.parse_args()

    if not args.project_id:
        print("ERROR: No project ID. Set DOMINO_PROJECT_ID or pass --project-id.")
        sys.exit(1)

    host = resolve_domino_api_host()
    print(f"API Host: {host}")
    print(f"Project:  {args.project_id}")

    dataset_id = args.dataset_id
    snapshot_id = args.snapshot_id

    if not dataset_id:
        dataset_id, snapshot_id = await setup_test_dataset(args.project_id)

    try:
        await run_probes(dataset_id, snapshot_id)
    finally:
        if not args.keep and not args.dataset_id:
            await cleanup_dataset(dataset_id)
        elif args.dataset_id:
            print(f"\n[Skip cleanup] Using provided dataset {dataset_id}")
        else:
            print(f"\n[Skip cleanup] --keep flag set. Dataset: {dataset_id}")


if __name__ == "__main__":
    asyncio.run(main())
