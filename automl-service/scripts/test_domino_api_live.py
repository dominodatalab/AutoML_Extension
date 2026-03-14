#!/usr/bin/env python3
"""Live integration test for Domino Dataset RW API operations.

Run inside a Domino workspace/app where auth credentials are available.
Tests the full dataset lifecycle: auth → create → grant → upload →
list files → snapshot → download → cleanup.

Usage:
    python scripts/test_domino_api_live.py
    python scripts/test_domino_api_live.py --keep    # don't delete test dataset
    python scripts/test_domino_api_live.py --project-id <OTHER_PROJECT_ID>

Environment:
    DOMINO_API_PROXY or DOMINO_API_HOST  — Domino API base URL
    DOMINO_PROJECT_ID                    — current project ID (auto-detected)
    Auth via sidecar token (localhost:8899) or DOMINO_API_KEY
"""

import argparse
import asyncio
import hashlib
import io
import os
import sys
import tempfile
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Ensure the app package is importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


# ──────────────────────────────────────────────────────────────────────────
# Result tracking
# ──────────────────────────────────────────────────────────────────────────

@dataclass
class TestResult:
    name: str
    passed: bool
    message: str = ""
    duration_ms: float = 0.0


@dataclass
class TestRunner:
    results: list = field(default_factory=list)
    dataset_id: Optional[str] = None  # for cleanup

    def record(self, name: str, passed: bool, message: str = "", duration_ms: float = 0.0):
        self.results.append(TestResult(name, passed, message, duration_ms))
        status = "PASS ✓" if passed else "FAIL ✗"
        timing = f" ({duration_ms:.0f}ms)" if duration_ms else ""
        print(f"  {status}  {name}{timing}")
        if message and not passed:
            for line in message.split("\n"):
                print(f"         {line}")

    def summary(self):
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed
        print("\n" + "=" * 60)
        print(f"RESULTS: {passed}/{total} passed, {failed} failed")
        print("=" * 60)
        if failed:
            print("\nFailed tests:")
            for r in self.results:
                if not r.passed:
                    print(f"  - {r.name}: {r.message}")
        return failed == 0


# ──────────────────────────────────────────────────────────────────────────
# Tests
# ──────────────────────────────────────────────────────────────────────────

async def test_auth(runner: TestRunner):
    """Verify we can acquire Domino auth headers."""
    from app.core.domino_http import get_domino_auth_headers

    t0 = time.monotonic()
    headers = await get_domino_auth_headers()
    dt = (time.monotonic() - t0) * 1000

    has_auth = bool(
        headers.get("Authorization") or headers.get("X-Domino-Api-Key")
    )
    if has_auth:
        method = "Bearer token" if "Authorization" in headers else "API key"
        runner.record("Auth: acquire credentials", True, f"Using {method}", dt)
    else:
        runner.record("Auth: acquire credentials", False, "No auth headers obtained", dt)

    return has_auth


async def test_resolve_host(runner: TestRunner):
    """Verify Domino API host resolution."""
    from app.core.domino_http import resolve_domino_api_host

    t0 = time.monotonic()
    try:
        host = resolve_domino_api_host()
        dt = (time.monotonic() - t0) * 1000
        runner.record("Host: resolve API base URL", True, host, dt)
        return host
    except ValueError as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Host: resolve API base URL", False, str(e), dt)
        return None


async def test_list_datasets(runner: TestRunner, project_id: str):
    """List datasets for a project via v2 API."""
    from app.core.domino_http import domino_request

    t0 = time.monotonic()
    try:
        resp = await domino_request(
            "GET",
            "/api/datasetrw/v2/datasets",
            params={"projectIdsToInclude": project_id},
        )
        dt = (time.monotonic() - t0) * 1000
        data = resp.json()

        # Count datasets
        if isinstance(data, list):
            count = len(data)
        elif isinstance(data, dict):
            items = data.get("items") or data.get("datasets") or data.get("data") or []
            count = len(items)
        else:
            count = 0

        runner.record(
            "List: GET /api/datasetrw/v2/datasets",
            True,
            f"Found {count} dataset(s) in project {project_id[:12]}...",
            dt,
        )
        return data
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("List: GET /api/datasetrw/v2/datasets", False, str(e), dt)
        return None


async def test_create_dataset(runner: TestRunner, project_id: str) -> Optional[str]:
    """Create a test dataset via v1 API."""
    from app.core.domino_http import domino_request

    dataset_name = f"automl-test-{int(time.time())}"
    t0 = time.monotonic()
    try:
        resp = await domino_request(
            "POST",
            "/api/datasetrw/v1/datasets",
            json={
                "name": dataset_name,
                "projectId": project_id,
                "description": "Temporary test dataset — safe to delete",
            },
        )
        dt = (time.monotonic() - t0) * 1000
        body = resp.json()

        # Extract dataset ID from various response shapes
        ds_id = str(
            body.get("datasetId")
            or body.get("id")
            or (body.get("dataset") or {}).get("id")
            or ""
        )

        if ds_id:
            runner.record(
                "Create: POST /api/datasetrw/v1/datasets",
                True,
                f"Created '{dataset_name}' (id={ds_id})",
                dt,
            )
            return ds_id
        else:
            runner.record(
                "Create: POST /api/datasetrw/v1/datasets",
                False,
                f"No dataset ID in response: {body}",
                dt,
            )
            return None
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Create: POST /api/datasetrw/v1/datasets", False, str(e), dt)
        return None


async def test_get_dataset(runner: TestRunner, dataset_id: str):
    """Get dataset by ID via v1 API."""
    from app.core.domino_http import domino_request

    t0 = time.monotonic()
    try:
        resp = await domino_request(
            "GET", f"/api/datasetrw/v1/datasets/{dataset_id}"
        )
        dt = (time.monotonic() - t0) * 1000
        body = resp.json()
        name = (
            body.get("datasetName")
            or body.get("name")
            or (body.get("dataset") or {}).get("name")
            or "?"
        )
        runner.record(
            "Get: GET /api/datasetrw/v1/datasets/{id}",
            True,
            f"Retrieved '{name}'",
            dt,
        )
        return body
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Get: GET /api/datasetrw/v1/datasets/{id}", False, str(e), dt)
        return None


async def test_grant_access(runner: TestRunner, dataset_id: str, project_id: str):
    """Grant project access via v1 grants API."""
    from app.core.domino_http import domino_request

    # Grant to our own project (idempotent)
    t0 = time.monotonic()
    try:
        resp = await domino_request(
            "POST",
            f"/api/datasetrw/v1/datasets/{dataset_id}/grants",
            json={
                "targetId": project_id,
                "targetRole": "DatasetRwEditor",
            },
        )
        dt = (time.monotonic() - t0) * 1000
        runner.record(
            "Grant: POST .../grants (DatasetRwEditor)",
            True,
            f"Granted to project {project_id[:12]}...",
            dt,
        )
        return True
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        # 409 Conflict means already granted — still a pass
        if "409" in str(e) or "Conflict" in str(e):
            runner.record(
                "Grant: POST .../grants (DatasetRwEditor)",
                True,
                f"Already granted (409 — OK)",
                dt,
            )
            return True
        runner.record("Grant: POST .../grants (DatasetRwEditor)", False, str(e), dt)
        return False


async def test_list_grants(runner: TestRunner, dataset_id: str):
    """List grants for a dataset."""
    from app.core.domino_http import domino_request

    t0 = time.monotonic()
    try:
        resp = await domino_request(
            "GET", f"/api/datasetrw/v1/datasets/{dataset_id}/grants"
        )
        dt = (time.monotonic() - t0) * 1000
        body = resp.json()
        grants = body if isinstance(body, list) else (
            body.get("grants") or body.get("items") or []
        )
        runner.record(
            "Grants: GET .../grants",
            True,
            f"Found {len(grants)} grant(s)",
            dt,
        )
        return grants
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Grants: GET .../grants", False, str(e), dt)
        return None


async def test_upload_file(runner: TestRunner, dataset_id: str) -> bool:
    """Upload a test file via the StorageResolver.upload_file (v4 chunked API)."""
    from app.services.storage_resolver import ProjectStorageResolver

    resolver = ProjectStorageResolver()
    test_content = b"id,name,value\n1,alpha,10.5\n2,beta,20.3\n3,gamma,30.1\n"
    file_path = "uploads/test_upload.csv"

    t0 = time.monotonic()
    try:
        await resolver.upload_file(
            dataset_id=dataset_id,
            file_path=file_path,
            file_content=test_content,
        )
        dt = (time.monotonic() - t0) * 1000
        runner.record(
            "Upload: v4 chunked upload",
            True,
            f"Uploaded '{file_path}' ({len(test_content)} bytes)",
            dt,
        )
        return True
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Upload: v4 chunked upload", False, str(e), dt)
        return False


async def test_list_snapshots(runner: TestRunner, dataset_id: str) -> Optional[str]:
    """List snapshots and return the latest snapshot ID."""
    from app.services.storage_resolver import ProjectStorageResolver

    resolver = ProjectStorageResolver()
    t0 = time.monotonic()
    try:
        snapshot_id = await resolver._get_latest_snapshot_id(dataset_id)
        dt = (time.monotonic() - t0) * 1000
        if snapshot_id:
            runner.record(
                "Snapshots: get latest snapshot ID",
                True,
                f"Latest snapshot: {snapshot_id}",
                dt,
            )
        else:
            runner.record(
                "Snapshots: get latest snapshot ID",
                True,
                "No snapshots found (may be normal for new dataset)",
                dt,
            )
        return snapshot_id
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Snapshots: get latest snapshot ID", False, str(e), dt)
        return None


async def test_list_files(runner: TestRunner, dataset_id: str):
    """List files in the dataset."""
    from app.services.storage_resolver import ProjectStorageResolver

    resolver = ProjectStorageResolver()
    t0 = time.monotonic()
    try:
        files = await resolver.list_files(dataset_id)
        dt = (time.monotonic() - t0) * 1000
        file_names = [
            f.get("path") or f.get("fileName") or f.get("name") or str(f)
            for f in files[:5]
        ]
        runner.record(
            "Files: list dataset files",
            True,
            f"Found {len(files)} file(s): {file_names}" if files else "No files listed (endpoint may not support listing)",
            dt,
        )
        return files
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Files: list dataset files", False, str(e), dt)
        return []


async def test_download_file(runner: TestRunner, dataset_id: str) -> bool:
    """Try to download a file via the API (may not be supported).

    This probes the download endpoints added in StorageResolver.download_file().
    Based on prior testing (2026-03-13), file download via API may return 404
    on all endpoints — files are only accessible via mount paths.
    """
    from app.services.storage_resolver import ProjectStorageResolver

    resolver = ProjectStorageResolver()
    file_path = "uploads/test_upload.csv"

    with tempfile.TemporaryDirectory() as tmpdir:
        dest = os.path.join(tmpdir, "downloaded.csv")
        t0 = time.monotonic()
        try:
            await resolver.download_file(dataset_id, file_path, dest)
            dt = (time.monotonic() - t0) * 1000

            if os.path.exists(dest):
                size = os.path.getsize(dest)
                with open(dest, "r") as f:
                    preview = f.read(200)
                runner.record(
                    "Download: file via API",
                    True,
                    f"Downloaded {size} bytes. Preview: {preview[:80]}...",
                    dt,
                )
                return True
            else:
                runner.record(
                    "Download: file via API",
                    False,
                    "download_file() returned but no file on disk",
                    dt,
                )
                return False
        except Exception as e:
            dt = (time.monotonic() - t0) * 1000
            runner.record(
                "Download: file via API",
                False,
                f"Download not supported or failed: {e}\n"
                f"(This is expected — Domino may not expose file download endpoints.\n"
                f" Files are only accessible via mount paths in Domino Jobs.)",
                dt,
            )
            return False


async def test_ensure_local_file(runner: TestRunner, dataset_id: str, project_id: str) -> bool:
    """Test the ensure_local_file() utility end-to-end.

    Simulates calling ensure_local_file() with a dataset mount path that
    doesn't exist locally, to verify it attempts the download path.
    """
    from app.core.utils import ensure_local_file
    from app.services.storage_resolver import get_storage_resolver, DatasetInfo

    # Pre-populate the resolver cache so ensure_local_file can find the dataset
    resolver = get_storage_resolver()
    resolver._cache[project_id] = DatasetInfo(
        dataset_id=dataset_id,
        name="automl-test",
        project_id=project_id,
    )

    fake_path = "/domino/datasets/local/automl-test/uploads/test_upload.csv"

    t0 = time.monotonic()
    try:
        result = await ensure_local_file(fake_path, project_id)
        dt = (time.monotonic() - t0) * 1000

        if os.path.exists(result) and result != fake_path:
            size = os.path.getsize(result)
            runner.record(
                "ensure_local_file: download-on-demand",
                True,
                f"Downloaded to {result} ({size} bytes)",
                dt,
            )
            return True
        elif result == fake_path:
            runner.record(
                "ensure_local_file: download-on-demand",
                False,
                "Returned original path (download failed or not attempted)",
                dt,
            )
            return False
        else:
            runner.record(
                "ensure_local_file: download-on-demand",
                False,
                f"Returned {result} but file doesn't exist on disk",
                dt,
            )
            return False
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record(
            "ensure_local_file: download-on-demand",
            False,
            f"Exception: {e}\n(Expected if download endpoints don't exist.)",
            dt,
        )
        return False
    finally:
        # Clean up cache
        resolver._cache.pop(project_id, None)


async def test_delete_dataset(runner: TestRunner, dataset_id: str):
    """Delete the test dataset to clean up."""
    from app.core.domino_http import domino_request

    t0 = time.monotonic()
    try:
        await domino_request("DELETE", f"/api/datasetrw/v1/datasets/{dataset_id}")
        dt = (time.monotonic() - t0) * 1000
        runner.record("Cleanup: DELETE dataset", True, f"Deleted {dataset_id}", dt)
        return True
    except Exception as e:
        dt = (time.monotonic() - t0) * 1000
        runner.record("Cleanup: DELETE dataset", False, str(e), dt)
        return False


# ──────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────

async def main():
    parser = argparse.ArgumentParser(description="Live Domino Dataset RW API tests")
    parser.add_argument(
        "--project-id",
        default=os.environ.get("DOMINO_PROJECT_ID"),
        help="Target project ID (default: DOMINO_PROJECT_ID env var)",
    )
    parser.add_argument(
        "--keep",
        action="store_true",
        help="Don't delete the test dataset after running",
    )
    args = parser.parse_args()

    if not args.project_id:
        print("ERROR: No project ID. Set DOMINO_PROJECT_ID or pass --project-id.")
        sys.exit(1)

    runner = TestRunner()

    print("=" * 60)
    print("Domino Dataset RW API — Live Integration Tests")
    print("=" * 60)
    print(f"Project ID: {args.project_id}")
    print(f"Cleanup:    {'disabled (--keep)' if args.keep else 'enabled'}")
    print("-" * 60)

    # ── Phase 1: Auth & connectivity ──
    print("\n[Phase 1] Auth & Connectivity")
    has_auth = await test_auth(runner)
    if not has_auth:
        print("\nAborting: no auth credentials available.")
        runner.summary()
        sys.exit(1)

    host = await test_resolve_host(runner)
    if not host:
        print("\nAborting: cannot resolve Domino API host.")
        runner.summary()
        sys.exit(1)

    # ── Phase 2: Dataset listing ──
    print("\n[Phase 2] Dataset Listing")
    await test_list_datasets(runner, args.project_id)

    # ── Phase 3: Dataset lifecycle ──
    print("\n[Phase 3] Dataset Lifecycle (create → grant → get)")
    dataset_id = await test_create_dataset(runner, args.project_id)
    if not dataset_id:
        print("\nAborting: could not create test dataset.")
        runner.summary()
        sys.exit(1)
    runner.dataset_id = dataset_id

    await test_get_dataset(runner, dataset_id)
    await test_grant_access(runner, dataset_id, args.project_id)
    await test_list_grants(runner, dataset_id)

    # ── Phase 4: File operations ──
    print("\n[Phase 4] File Operations (upload → snapshots → list → download)")
    uploaded = await test_upload_file(runner, dataset_id)

    # Wait a moment for the snapshot to settle
    if uploaded:
        print("  ... waiting 3s for snapshot to settle")
        await asyncio.sleep(3)

    await test_list_snapshots(runner, dataset_id)
    await test_list_files(runner, dataset_id)

    # ── Phase 5: Download (expected to fail — documents API gap) ──
    print("\n[Phase 5] File Download (probing API — may not be supported)")
    if uploaded:
        await test_download_file(runner, dataset_id)
        await test_ensure_local_file(runner, dataset_id, args.project_id)
    else:
        runner.record("Download: file via API", False, "Skipped — upload failed")
        runner.record("ensure_local_file: download-on-demand", False, "Skipped — upload failed")

    # ── Phase 6: Cleanup ──
    if not args.keep:
        print("\n[Phase 6] Cleanup")
        await test_delete_dataset(runner, dataset_id)
    else:
        print(f"\n[Phase 6] Cleanup SKIPPED (--keep). Dataset ID: {dataset_id}")

    # ── Summary ──
    all_passed = runner.summary()
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    asyncio.run(main())
