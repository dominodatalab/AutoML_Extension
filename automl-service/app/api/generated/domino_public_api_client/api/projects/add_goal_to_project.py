from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_goal_to_project_response_400 import AddGoalToProjectResponse400
from ...models.add_goal_to_project_response_404 import AddGoalToProjectResponse404
from ...models.add_goal_to_project_response_500 import AddGoalToProjectResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_project_goal_v1 import NewProjectGoalV1
from ...models.project_goal_envelope_v1 import ProjectGoalEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: NewProjectGoalV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v1/projects/{project_id}/goals".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectGoalEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddGoalToProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddGoalToProjectResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AddGoalToProjectResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGoalV1,
) -> Response[
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
]:
    """Add a goal to this project

     Add a goal to this project. Required permissions: `Edit`

    Args:
        project_id (str):
        body (NewProjectGoalV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddGoalToProjectResponse400 | AddGoalToProjectResponse404 | AddGoalToProjectResponse500 | FailureEnvelopeV1 | ProjectGoalEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGoalV1,
) -> (
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | None
):
    """Add a goal to this project

     Add a goal to this project. Required permissions: `Edit`

    Args:
        project_id (str):
        body (NewProjectGoalV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddGoalToProjectResponse400 | AddGoalToProjectResponse404 | AddGoalToProjectResponse500 | FailureEnvelopeV1 | ProjectGoalEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGoalV1,
) -> Response[
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
]:
    """Add a goal to this project

     Add a goal to this project. Required permissions: `Edit`

    Args:
        project_id (str):
        body (NewProjectGoalV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddGoalToProjectResponse400 | AddGoalToProjectResponse404 | AddGoalToProjectResponse500 | FailureEnvelopeV1 | ProjectGoalEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGoalV1,
) -> (
    AddGoalToProjectResponse400
    | AddGoalToProjectResponse404
    | AddGoalToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGoalEnvelopeV1
    | None
):
    """Add a goal to this project

     Add a goal to this project. Required permissions: `Edit`

    Args:
        project_id (str):
        body (NewProjectGoalV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddGoalToProjectResponse400 | AddGoalToProjectResponse404 | AddGoalToProjectResponse500 | FailureEnvelopeV1 | ProjectGoalEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
