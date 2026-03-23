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
    def __init__(self, *, post_payload):
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


def test_fetch_authorized_actions_posts_expected_payload_and_parses_alias():
    from app.core.authorized_actions import (
        AUTHORIZED_ACTIONS_PATH,
        AuthorizedActionRequestItem,
        AuthorizedActionsRequest,
        fetch_authorized_actions,
    )

    fake_httpx = _FakeHttpxClient(
        post_payload={"authorizedActions": [{"isAuthorized": True}]},
    )
    client = _FakeDominoClient(fake_httpx)
    request_body = AuthorizedActionsRequest(
        actions=[
            AuthorizedActionRequestItem(
                id="project.change_project_settings-project-1",
                code="project.change_project_settings",
                context={"projectId": "project-1"},
            )
        ]
    )

    results = fetch_authorized_actions(client, request_body)

    assert len(results) == 1
    assert results[0].is_allowed() is True
    assert fake_httpx.post_calls == [
        {
            "url": AUTHORIZED_ACTIONS_PATH,
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


def test_authorized_action_allowed_accepts_list_response_payload():
    from app.core.authorized_actions import AuthorizedActionRequestItem, authorized_action_allowed

    fake_httpx = _FakeHttpxClient(post_payload=[{"permitted": True}])
    client = _FakeDominoClient(fake_httpx)
    action = AuthorizedActionRequestItem(
        id="project.change_project_settings-project-1",
        code="project.change_project_settings",
        context={"projectId": "project-1"},
    )

    assert authorized_action_allowed(client, action) is True
