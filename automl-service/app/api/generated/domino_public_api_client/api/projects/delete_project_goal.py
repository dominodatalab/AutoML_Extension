from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_envelope_v1 import DeleteEnvelopeV1
from ...models.delete_project_goal_response_400 import DeleteProjectGoalResponse400
from ...models.delete_project_goal_response_404 import DeleteProjectGoalResponse404
from ...models.delete_project_goal_response_500 import DeleteProjectGoalResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    goal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/projects/v1/projects/{project_id}/goals/{goal_id}".format(
            project_id=quote(str(project_id), safe=""),
            goal_id=quote(str(goal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = DeleteEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectGoalResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteProjectGoalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteProjectGoalResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
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
) -> Response[
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
]:
    """Delete a project goal

     Delete a project goal. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | DeleteProjectGoalResponse400 | DeleteProjectGoalResponse404 | DeleteProjectGoalResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
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
) -> (
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete a project goal

     Delete a project goal. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | DeleteProjectGoalResponse400 | DeleteProjectGoalResponse404 | DeleteProjectGoalResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        goal_id=goal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
]:
    """Delete a project goal

     Delete a project goal. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | DeleteProjectGoalResponse400 | DeleteProjectGoalResponse404 | DeleteProjectGoalResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        goal_id=goal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteEnvelopeV1
    | DeleteProjectGoalResponse400
    | DeleteProjectGoalResponse404
    | DeleteProjectGoalResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete a project goal

     Delete a project goal. Required permissions: `Edit`

    Args:
        project_id (str):
        goal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | DeleteProjectGoalResponse400 | DeleteProjectGoalResponse404 | DeleteProjectGoalResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            goal_id=goal_id,
            client=client,
        )
    ).parsed
