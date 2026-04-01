"""Helpers for Domino authorized-actions permission checks."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

AUTHORIZED_ACTIONS_PATH = "/account/authz/permissions/authorizedactions"


class AuthorizedActionRequestItem(BaseModel):
    id: str
    code: str
    context: dict[str, object] | None = None


class AuthorizedActionsRequest(BaseModel):
    actions: list[AuthorizedActionRequestItem]


class AuthorizedActionResult(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    code: str
    result: bool | None = None

    def is_allowed(self) -> bool:
        return self.result


class AuthorizedActionsEnvelope(BaseModel):
    model_config = ConfigDict(extra="ignore")

    actions: list[AuthorizedActionResult] | None = None

    def action_results(self) -> list[AuthorizedActionResult]:
        return self.actions or []


def parse_authorized_actions(payload: object) -> list[AuthorizedActionResult]:
    """Parse the authz response while tolerating minor envelope differences."""
    if isinstance(payload, list):
        return [AuthorizedActionResult.model_validate(item) for item in payload]

    envelope = AuthorizedActionsEnvelope.model_validate(payload)
    return envelope.action_results()


def fetch_authorized_actions(client, request_body: AuthorizedActionsRequest) -> list[AuthorizedActionResult]:
    """Post an authorized-actions request and return the parsed action results."""
    response = client.get_httpx_client().post(
        AUTHORIZED_ACTIONS_PATH,
        json=request_body.model_dump(exclude_none=True),
    )
    response.raise_for_status()
    return parse_authorized_actions(response.json())


def authorized_action_allowed(client, action: AuthorizedActionRequestItem) -> bool:
    """Return True when any result for the given action request is allowed."""
    request_body = AuthorizedActionsRequest(actions=[action])
    action_results = fetch_authorized_actions(client, request_body)
    return any(result.is_allowed() for result in action_results)
