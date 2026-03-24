"""Diagnostic script to verify auth behavior inside a Domino App container.

Run this as the App entry script to see what auth the sidecar uses
and whether it returns the viewing user or the App owner.

Usage: python automl-service/scripts/check_app_auth.py
"""

import os
import json
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler


PROXY = os.environ.get("DOMINO_API_PROXY", "http://localhost:8899")


def call(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, body
    except Exception as e:
        return None, str(e)


class DiagHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        results = {}

        # 1. What headers does the Domino proxy send to this App?
        results["incoming_headers"] = {
            "Authorization": self.headers.get("Authorization", "NOT SET"),
            "authorization": self.headers.get("authorization", "NOT SET"),
            "domino-username": self.headers.get("domino-username", "NOT SET"),
            "X-Domino-Api-Key": self.headers.get("X-Domino-Api-Key", "NOT SET"),
        }

        # 2. /api/users/v1/self with NO auth (sidecar injects its own)
        status, body = call(f"{PROXY}/api/users/v1/self")
        try:
            user_no_auth = json.loads(body).get("user", {}).get("userName", "?")
        except Exception:
            user_no_auth = f"status={status}"
        results["users_self_no_auth"] = {"status": status, "userName": user_no_auth}

        # 3. /api/users/v1/self with the FORWARDED browser auth
        forwarded = self.headers.get("Authorization")
        if forwarded:
            status, body = call(f"{PROXY}/api/users/v1/self",
                                headers={"Authorization": forwarded})
            try:
                user_forwarded = json.loads(body).get("user", {}).get("userName", "?")
            except Exception:
                user_forwarded = f"status={status}"
            results["users_self_forwarded_auth"] = {"status": status, "userName": user_forwarded}
        else:
            results["users_self_forwarded_auth"] = "NO Authorization header from proxy"

        # 4. /api/users/v1/self with API key
        api_key = os.environ.get("DOMINO_API_KEY") or os.environ.get("DOMINO_USER_API_KEY")
        if api_key:
            status, body = call(f"{PROXY}/api/users/v1/self",
                                headers={"X-Domino-Api-Key": api_key})
            try:
                user_apikey = json.loads(body).get("user", {}).get("userName", "?")
            except Exception:
                user_apikey = f"status={status}"
            results["users_self_api_key"] = {"status": status, "userName": user_apikey}

        # 5. Dataset listing with no auth (sidecar injects)
        project_id = os.environ.get("DOMINO_PROJECT_ID", "")
        if project_id:
            status, _ = call(f"{PROXY}/api/datasetrw/v1/datasets?projectId={project_id}&offset=0&limit=1")
            results["datasets_no_auth"] = {"status": status}

        # 6. Dataset listing with forwarded auth
        if forwarded and project_id:
            status, _ = call(f"{PROXY}/api/datasetrw/v1/datasets?projectId={project_id}&offset=0&limit=1",
                             headers={"Authorization": forwarded})
            results["datasets_forwarded_auth"] = {"status": status}

        # Summary
        results["conclusion"] = {
            "domino_username_header": self.headers.get("domino-username", "NOT SET"),
            "proxy_injects_auth": forwarded is not None,
            "sidecar_user_no_auth": results.get("users_self_no_auth", {}).get("userName", "?"),
        }

        output = json.dumps(results, indent=2)
        print(output)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(output.encode())

    def log_message(self, format, *args):
        print(f"[diag] {args[0]}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    print(f"Auth diagnostic server on port {port}")
    print(f"Open the App in your browser, then check the App logs for results.")
    print(f"Every request to the App will show the auth diagnostic.")
    HTTPServer(("0.0.0.0", port), DiagHandler).serve_forever()
