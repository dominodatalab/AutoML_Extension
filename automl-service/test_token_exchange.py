"""Test Keycloak token exchange from the workspace terminal.

Run: PYTHONPATH=/mnt/code/automl-service python3 /mnt/code/automl-service/test_token_exchange.py

This simulates what the app would do:
1. Captures the browser JWT from the request context (here we fake it via the sidecar's access-token as a stand-in)
2. Exchanges it at Keycloak for a properly-scoped token
3. Tests the exchanged token against datasetrw
"""
import json
import sys
import urllib.request
import urllib.parse
import urllib.error
import base64
import os

KEYCLOAK_BASE = os.environ.get("DOMINO_KEYCLOAK_BASE_URI", "http://keycloak-http.domino-platform:80")
TOKEN_ENDPOINT = f"{KEYCLOAK_BASE}/auth/realms/DominoRealm/protocol/openid-connect/token"
DATASETRW_URL = "http://localhost:8899/api/datasetrw/v2/datasets"
PROJECT_ID = os.environ.get("DOMINO_PROJECT_ID", "69b73e50c079b34f9a5b194a")

def decode_jwt_payload(token: str) -> dict:
    """Decode JWT payload without verification."""
    parts = token.split(".")
    if len(parts) < 2:
        return {"error": "not a JWT"}
    padded = parts[1] + "=" * (4 - len(parts[1]) % 4)
    return json.loads(base64.urlsafe_b64decode(padded))

def exchange_token(subject_token: str, client_secret: str = None) -> dict:
    """Exchange a token via Keycloak token exchange grant."""
    params = {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "client_id": "domino-play",
        "subject_token": subject_token,
        "audience": "app-user-token-exchange-client",
        "requested_token_type": "urn:ietf:params:oauth:token-type:access_token",
    }
    if client_secret:
        params["client_secret"] = client_secret

    data = urllib.parse.urlencode(params).encode("utf-8")
    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        resp = urllib.request.urlopen(req)
        return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        try:
            return {"error": json.loads(body), "status": e.code}
        except json.JSONDecodeError:
            return {"error": body[:500], "status": e.code}

def test_datasetrw(token: str) -> dict:
    """Test the token against datasetrw."""
    url = f"{DATASETRW_URL}?projectIdsToInclude={PROJECT_ID}&offset=0&limit=50"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        resp = urllib.request.urlopen(req)
        return {"status": resp.status, "body": json.loads(resp.read().decode())}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "body": e.read().decode()[:200]}

# --- Get the browser JWT ---
# Try to read from stdin/argument, otherwise get sidecar token as fallback
browser_jwt = None
if len(sys.argv) > 1:
    browser_jwt = sys.argv[1]
    if browser_jwt.startswith("Bearer "):
        browser_jwt = browser_jwt[7:]

if not browser_jwt:
    print("Usage: python3 test_token_exchange.py <browser-jwt>")
    print("\nGet the JWT from the DEBUG FULL AUTH log line (without 'Bearer ' prefix)")
    print("\nFalling back to sidecar token for testing...")
    try:
        resp = urllib.request.urlopen("http://localhost:8899/access-token")
        browser_jwt = resp.read().decode().strip()
        print(f"Got sidecar token (this is the app owner's, not a real browser JWT)")
    except Exception as e:
        print(f"Failed to get sidecar token: {e}")
        sys.exit(1)

print(f"\n=== Input token ===")
claims = decode_jwt_payload(browser_jwt)
print(f"sub: {claims.get('sub')}")
print(f"preferred_username: {claims.get('preferred_username')}")
print(f"aud: {claims.get('aud')}")
print(f"azp: {claims.get('azp')}")
print(f"scope: {claims.get('scope')}")

print(f"\n=== Attempting token exchange (no client secret) ===")
result = exchange_token(browser_jwt)

if "access_token" in result:
    exchanged_token = result["access_token"]
    print("SUCCESS!")
    exc_claims = decode_jwt_payload(exchanged_token)
    print(f"sub: {exc_claims.get('sub')}")
    print(f"preferred_username: {exc_claims.get('preferred_username')}")
    print(f"aud: {exc_claims.get('aud')}")
    print(f"azp: {exc_claims.get('azp')}")
    print(f"scope: {exc_claims.get('scope')}")
    print(f"scp: {exc_claims.get('scp')}")

    print(f"\n=== Testing exchanged token against datasetrw ===")
    dr = test_datasetrw(exchanged_token)
    print(f"Status: {dr['status']}")
    if isinstance(dr['body'], dict):
        datasets = dr['body'].get('datasets', [])
        print(f"Datasets returned: {len(datasets)}")
        for ds in datasets:
            d = ds.get('dataset', ds)
            print(f"  - {d.get('name')} ({d.get('id')})")
    else:
        print(f"Body: {dr['body']}")
else:
    print(f"FAILED: {json.dumps(result, indent=2)}")
    if result.get("status") == 401 or "unauthorized" in str(result.get("error", "")).lower():
        print("\ndomino-play requires a client secret. Check with platform team.")
    elif "client_credentials" in str(result.get("error", "")):
        print("\nNeed client_secret — try passing it as second arg:")
        print("  python3 test_token_exchange.py <jwt> <client-secret>")
