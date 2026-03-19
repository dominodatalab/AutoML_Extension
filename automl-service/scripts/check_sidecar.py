"""Diagnostic script to test sidecar proxy capabilities from inside an App container.

Usage: python scripts/check_sidecar.py
"""

import os
import json
import urllib.request
import urllib.error


def test_endpoint(label, url, headers=None):
    print(f"\n{'='*60}")
    print(f"TEST: {label}")
    print(f"URL:  {url}")
    if headers:
        print(f"Headers: {headers}")
    print("-" * 60)

    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            body = resp.read().decode("utf-8", errors="replace")
            print(f"STATUS: {status}")
            # Truncate long responses (e.g. JWT tokens)
            if len(body) > 500:
                print(f"BODY (truncated): {body[:500]}...")
            else:
                print(f"BODY: {body}")
            return status
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        print(f"STATUS: {e.code}")
        if body:
            print(f"ERROR BODY: {body[:500]}")
        return e.code
    except Exception as e:
        print(f"EXCEPTION: {type(e).__name__}: {e}")
        return None


def main():
    proxy = os.environ.get("DOMINO_API_PROXY", "http://localhost:8899")
    api_host = os.environ.get("DOMINO_API_HOST", "")
    api_key = os.environ.get("DOMINO_API_KEY") or os.environ.get("DOMINO_USER_API_KEY") or ""
    project_id = os.environ.get("DOMINO_PROJECT_ID", "")

    print("ENVIRONMENT:")
    print(f"  DOMINO_API_PROXY:  {proxy}")
    print(f"  DOMINO_API_HOST:   {api_host}")
    print(f"  DOMINO_API_KEY:    {'set (' + api_key[:8] + '...)' if api_key else 'NOT SET'}")
    print(f"  DOMINO_PROJECT_ID: {project_id}")

    # Test 1: sidecar access-token
    test_endpoint(
        "Sidecar access-token",
        f"{proxy}/access-token",
    )

    # Test 2: users/self through sidecar (no extra auth — sidecar injects it)
    test_endpoint(
        "Users API via sidecar (no auth header)",
        f"{proxy}/api/users/v1/self",
    )

    # Test 3: users/self through sidecar with access token
    token_status = None
    try:
        req = urllib.request.Request(f"{proxy}/access-token")
        with urllib.request.urlopen(req, timeout=5) as resp:
            token = resp.read().decode().strip()
            token_status = test_endpoint(
                "Users API via sidecar (with Bearer token)",
                f"{proxy}/api/users/v1/self",
                headers={"Authorization": f"Bearer {token}"},
            )
    except Exception as e:
        print(f"\nSkipping Bearer token test — could not get access token: {e}")

    # Test 4: users/self through sidecar with API key
    if api_key:
        test_endpoint(
            "Users API via sidecar (with API key)",
            f"{proxy}/api/users/v1/self",
            headers={"X-Domino-Api-Key": api_key},
        )

    # Test 5: users/self direct to nucleus (bypassing sidecar)
    if api_host:
        nucleus_url = api_host.rstrip("/")
        if not nucleus_url.startswith("http"):
            nucleus_url = f"http://{nucleus_url}"
        if api_key:
            test_endpoint(
                "Users API direct to nucleus (API key)",
                f"{nucleus_url}/api/users/v1/self",
                headers={"X-Domino-Api-Key": api_key},
            )
        else:
            test_endpoint(
                "Users API direct to nucleus (no auth)",
                f"{nucleus_url}/api/users/v1/self",
            )

    # Test 6: dataset listing through sidecar (sanity check)
    if project_id:
        test_endpoint(
            "Dataset listing via sidecar",
            f"{proxy}/api/datasetrw/v1/datasets?projectId={project_id}&offset=0&limit=3",
        )

    print(f"\n{'='*60}")
    print("DONE")


if __name__ == "__main__":
    main()
