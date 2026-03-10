#!/usr/bin/env python3
"""Diagnose Domino API routing: proxy vs direct host.

Run this in a Domino workspace or job to determine:
1. Which env vars are set (DOMINO_API_PROXY, DOMINO_API_HOST, etc.)
2. Whether the proxy and direct host return the same results
3. Whether cross-project job start respects projectId through each path

Usage:
    python scripts/diagnose_api_routing.py
    python scripts/diagnose_api_routing.py --target-project-id <OTHER_PROJECT_ID>
"""

import argparse
import asyncio
import json
import os
import sys


# ---------------------------------------------------------------------------
# 1. Environment dump
# ---------------------------------------------------------------------------

def dump_env():
    keys = [
        "DOMINO_API_PROXY",
        "DOMINO_API_HOST",
        "DOMINO_PROJECT_ID",
        "DOMINO_PROJECT_NAME",
        "DOMINO_PROJECT_OWNER",
        "DOMINO_RUN_ID",
        "DOMINO_API_KEY",
        "DOMINO_USER_API_KEY",
        "DOMINO_TOKEN_FILE",
    ]
    print("=" * 60)
    print("ENVIRONMENT VARIABLES")
    print("=" * 60)
    for key in keys:
        val = os.environ.get(key)
        if val and "KEY" in key:
            print(f"  {key} = {val[:8]}...  (redacted)")
        elif val and "TOKEN" in key:
            print(f"  {key} = {val}")
        else:
            print(f"  {key} = {val or '(not set)'}")
    print()


# ---------------------------------------------------------------------------
# 2. Auth token acquisition
# ---------------------------------------------------------------------------

async def get_sidecar_token() -> str | None:
    """Try to get a Bearer token from the Domino sidecar."""
    import httpx
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get("http://localhost:8899/access-token")
        if resp.status_code == 200 and resp.text.strip():
            return resp.text.strip()
    except Exception as e:
        print(f"  Sidecar token fetch failed: {e}")
    return None


def get_api_key() -> str | None:
    return (
        os.environ.get("DOMINO_API_KEY")
        or os.environ.get("DOMINO_USER_API_KEY")
    )


async def get_auth_headers() -> dict[str, str]:
    token = await get_sidecar_token()
    if token:
        print(f"  Auth method: Bearer token from sidecar ({token[:12]}...)")
        return {"Authorization": f"Bearer {token}"}
    api_key = get_api_key()
    if api_key:
        print(f"  Auth method: X-Domino-Api-Key ({api_key[:8]}...)")
        return {"X-Domino-Api-Key": api_key}
    print("  Auth method: NONE (no token or key found)")
    return {}


# ---------------------------------------------------------------------------
# 3. API call via proxy vs direct host
# ---------------------------------------------------------------------------

async def call_endpoint(base_url: str, path: str, auth_headers: dict, method: str = "GET", json_body: dict = None) -> dict:
    """Make a request and return {status, body, error}."""
    import httpx
    url = f"{base_url.rstrip('/')}{path}"
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            if method == "GET":
                resp = await client.get(url, headers=auth_headers)
            else:
                resp = await client.request(method, url, headers=auth_headers, json=json_body)
        body = None
        try:
            body = resp.json()
        except Exception:
            body = resp.text[:500]
        return {"status": resp.status_code, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "body": None, "error": str(e)}


async def test_self_project(base_url: str, label: str, auth_headers: dict):
    """Test GET /v4/projects/{self_project_id} to verify basic connectivity."""
    project_id = os.environ.get("DOMINO_PROJECT_ID")
    if not project_id:
        print(f"  [{label}] Skipping self-project test: DOMINO_PROJECT_ID not set")
        return

    print(f"  [{label}] GET /v4/projects/{project_id[:8]}... via {base_url}")
    result = await call_endpoint(base_url, f"/v4/projects/{project_id}", auth_headers)
    if result["error"]:
        print(f"    ERROR: {result['error']}")
    else:
        status = result["status"]
        body = result["body"]
        name = body.get("name", "?") if isinstance(body, dict) else "?"
        print(f"    Status: {status}, Project name: {name}")


async def test_cross_project(base_url: str, label: str, auth_headers: dict, target_project_id: str):
    """Test GET /v4/projects/{target_project_id} to verify cross-project access."""
    print(f"  [{label}] GET /v4/projects/{target_project_id[:8]}... via {base_url}")
    result = await call_endpoint(base_url, f"/v4/projects/{target_project_id}", auth_headers)
    if result["error"]:
        print(f"    ERROR: {result['error']}")
    else:
        status = result["status"]
        body = result["body"]
        name = body.get("name", "?") if isinstance(body, dict) else "?"
        owner = body.get("ownerUsername", "?") if isinstance(body, dict) else "?"
        print(f"    Status: {status}, Project: {owner}/{name}")


async def test_list_datasets(base_url: str, label: str, auth_headers: dict, target_project_id: str):
    """Test GET /api/datasetrw/v2/datasets?projectIdsToInclude={id}."""
    print(f"  [{label}] GET /api/datasetrw/v2/datasets?projectIdsToInclude={target_project_id[:8]}... via {base_url}")
    import httpx
    url = f"{base_url.rstrip('/')}/api/datasetrw/v2/datasets"
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get(url, headers=auth_headers, params={
                "projectIdsToInclude": target_project_id,
                "limit": 5,
            })
        if resp.status_code >= 400:
            print(f"    Status: {resp.status_code}, Body: {resp.text[:300]}")
        else:
            body = resp.json()
            items = body if isinstance(body, list) else body.get("items", body.get("datasets", []))
            print(f"    Status: {resp.status_code}, Datasets returned: {len(items)}")
            for item in items[:3]:
                ds_name = item.get("datasetName") or item.get("name", "?")
                ds_id = item.get("datasetId") or item.get("id", "?")
                print(f"      - {ds_name} (id={ds_id[:12]}...)")
    except Exception as e:
        print(f"    ERROR: {e}")


async def test_hardware_tiers(base_url: str, label: str, auth_headers: dict, project_id: str):
    """Test GET /v4/projects/{id}/hardwareTiers — proxy may scope this."""
    print(f"  [{label}] GET /v4/projects/{project_id[:8]}../hardwareTiers via {base_url}")
    result = await call_endpoint(base_url, f"/v4/projects/{project_id}/hardwareTiers", auth_headers)
    if result["error"]:
        print(f"    ERROR: {result['error']}")
    elif result["status"] >= 400:
        print(f"    Status: {result['status']}, Body: {str(result['body'])[:200]}")
    else:
        tiers = result["body"] if isinstance(result["body"], list) else []
        print(f"    Status: {result['status']}, Tiers: {len(tiers)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    parser = argparse.ArgumentParser(description="Diagnose Domino API routing")
    parser.add_argument(
        "--target-project-id",
        help="A DIFFERENT project ID to test cross-project operations against",
    )
    args = parser.parse_args()

    dump_env()

    proxy_url = os.environ.get("DOMINO_API_PROXY")
    direct_url = os.environ.get("DOMINO_API_HOST")
    self_project_id = os.environ.get("DOMINO_PROJECT_ID")
    target_project_id = args.target_project_id

    print("=" * 60)
    print("AUTH")
    print("=" * 60)
    auth_headers = await get_auth_headers()
    print()

    hosts_to_test: list[tuple[str, str]] = []
    if proxy_url:
        hosts_to_test.append((proxy_url, "PROXY"))
    if direct_url:
        hosts_to_test.append((direct_url, "DIRECT"))

    if not hosts_to_test:
        print("ERROR: Neither DOMINO_API_PROXY nor DOMINO_API_HOST is set. Cannot test.")
        sys.exit(1)

    # -- Self-project connectivity --
    print("=" * 60)
    print("TEST 1: Self-project connectivity")
    print("=" * 60)
    for url, label in hosts_to_test:
        await test_self_project(url, label, auth_headers)
    print()

    # -- Cross-project access --
    if target_project_id:
        print("=" * 60)
        print("TEST 2: Cross-project access")
        print("=" * 60)
        for url, label in hosts_to_test:
            await test_cross_project(url, label, auth_headers, target_project_id)
        print()

        print("=" * 60)
        print("TEST 3: List datasets for target project")
        print("=" * 60)
        for url, label in hosts_to_test:
            await test_list_datasets(url, label, auth_headers, target_project_id)
        print()

        print("=" * 60)
        print("TEST 4: Hardware tiers for target project")
        print("=" * 60)
        for url, label in hosts_to_test:
            await test_hardware_tiers(url, label, auth_headers, target_project_id)
        print()
    else:
        print("=" * 60)
        print("TEST 2: List datasets for self project")
        print("=" * 60)
        if self_project_id:
            for url, label in hosts_to_test:
                await test_list_datasets(url, label, auth_headers, self_project_id)
        else:
            print("  Skipping: no DOMINO_PROJECT_ID set")
        print()

        print("-" * 60)
        print("TIP: Re-run with --target-project-id <ID> to test cross-project behavior")
        print("-" * 60)

    # -- Summary --
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  DOMINO_API_PROXY  = {proxy_url or '(not set)'}")
    print(f"  DOMINO_API_HOST   = {direct_url or '(not set)'}")
    print(f"  Self project      = {self_project_id or '(not set)'}")
    print(f"  Target project    = {target_project_id or '(not provided)'}")
    print()
    if proxy_url and direct_url:
        print("  Both PROXY and DIRECT hosts are available.")
        print("  Compare results above to see if the proxy restricts cross-project ops.")
    elif proxy_url:
        print("  Only PROXY is available. Cannot compare proxy vs direct.")
        print("  If cross-project fails, try setting DOMINO_API_HOST explicitly.")
    elif direct_url:
        print("  Only DIRECT host is available (no proxy). This should work for cross-project.")


if __name__ == "__main__":
    asyncio.run(main())
