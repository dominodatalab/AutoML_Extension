class FakeResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


class FakeHttpxClient:
    def __init__(self, *, post_payload=None):
        self._post_payload = post_payload
        self.post_calls = []

    def post(self, url, json=None):
        self.post_calls.append({"url": url, "json": json})
        return FakeResponse(self._post_payload)


class FakeDominoClient:
    def __init__(self, httpx_client):
        self._httpx_client = httpx_client

    def get_httpx_client(self):
        return self._httpx_client

