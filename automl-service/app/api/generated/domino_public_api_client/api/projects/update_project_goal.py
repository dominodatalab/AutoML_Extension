from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.project_goal_envelope_v1 import ProjectGoalEnvelopeV1
from ...models.project_goal_for_update_v1 import ProjectGoalForUpdateV1
from ...models.update_project_goal_response_400 import UpdateProjectGoalResponse400
from ...models.update_project_goal_response_404 import UpdateProjectGoalResponse404
from ...models.update_project_goal_response_500 import UpdateProjectGoalResponse500
from ...types import Response


def _get_kwargs(
    project_id: str,
    goal_id: str,
    *,
    body: ProjectGoalForUpdateV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/projects/v1/projects/{project_id}/goals/{goal_id}".format(
            project_id=quote(str(project_id), safe=""),
            goal_id=quote(str(goal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ProjectGoalEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateProjectGoalResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateProjectGoalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateProjectGoalResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectGoalForUpdateV1,
) -> Response[
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
]:
    """Update project goal status

     Update project goal status. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):
        body (ProjectGoalForUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ProjectGoalEnvelopeV1 | UpdateProjectGoalResponse400 | UpdateProjectGoalResponse404 | UpdateProjectGoalResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectGoalForUpdateV1,
) -> (
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
    | None
):
    """Update project goal status

     Update project goal status. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):
        body (ProjectGoalForUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ProjectGoalEnvelopeV1 | UpdateProjectGoalResponse400 | UpdateProjectGoalResponse404 | UpdateProjectGoalResponse500
    """

    return sync_detailed(
        project_id=project_id,
        goal_id=goal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectGoalForUpdateV1,
) -> Response[
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
]:
    """Update project goal status

     Update project goal status. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):
        body (ProjectGoalForUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ProjectGoalEnvelopeV1 | UpdateProjectGoalResponse400 | UpdateProjectGoalResponse404 | UpdateProjectGoalResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectGoalForUpdateV1,
) -> (
    FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | UpdateProjectGoalResponse400
    | UpdateProjectGoalResponse404
    | UpdateProjectGoalResponse500
    | None
):
    """Update project goal status

     Update project goal status. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):
        body (ProjectGoalForUpdateV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ProjectGoalEnvelopeV1 | UpdateProjectGoalResponse400 | UpdateProjectGoalResponse404 | UpdateProjectGoalResponse500
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            goal_id=goal_id,
            client=client,
            body=body,
        )
    ).parsed
