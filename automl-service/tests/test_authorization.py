class _FakeResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


class _FakeHttpxClient:
    def __init__(self, *, post_payload=None):
        self._post_payload = post_payload
        self.post_calls = []

    def post(self, url, json=None):
        self.post_calls.append({"url": url, "json": json})
        return _FakeResponse(self._post_payload)


class _FakeDominoClient:
    def __init__(self, httpx_client):
        self._httpx_client = httpx_client

    def get_httpx_client(self):
        return self._httpx_client


def test_current_user_can_modify_storage_when_authz_allows(monkeypatch):
    from app.core import authorization as auth

    fake_httpx = _FakeHttpxClient(
        post_payload={"actions": [{"id": "project.change_project_settings-project-1", "result": True}]},
    )
    fake_client = _FakeDominoClient(fake_httpx)
    monkeypatch.setattr(
        auth,
        "get_domino_public_api_client_sync",
        lambda: fake_client,
        raising=True,
    )
    monkeypatch.setattr(auth, "resolve_domino_project_id", lambda: "project-1", raising=True)

    assert auth.current_user_can_modify_storage() is True
    assert fake_httpx.post_calls == [
        {
            "url": "/account/authz/permissions/authorizedactions",
            "json": {
                "actions": [
                    {
                        "id": "project.change_project_settings-project-1",
                        "code": "project.change_project_settings",
                        "context": {"projectId": "project-1"},
                    }
                ]
            },
        }
    ]


def test_current_user_can_modify_storage_when_authz_denies(monkeypatch):
    from app.core import authorization as auth

    fake_httpx = _FakeHttpxClient(
        post_payload={"actions": [{"id": "project.change_project_settings-project-1", "result": False}]},
    )
    fake_client = _FakeDominoClient(fake_httpx)
    monkeypatch.setattr(
        auth,
        "get_domino_public_api_client_sync",
        lambda: fake_client,
        raising=True,
    )
    monkeypatch.setattr(auth, "resolve_domino_project_id", lambda: "project-1", raising=True)

    assert auth.current_user_can_modify_storage() is False
    assert len(fake_httpx.post_calls) == 1
