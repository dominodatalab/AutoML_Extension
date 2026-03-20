from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_project_goals_response_400 import GetProjectGoalsResponse400
from ...models.get_project_goals_response_404 import GetProjectGoalsResponse404
from ...models.get_project_goals_response_500 import GetProjectGoalsResponse500
from ...models.project_goals_envelope_v1 import ProjectGoalsEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/projects/v1/projects/{project_id}/goals".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectGoalsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectGoalsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProjectGoalsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetProjectGoalsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
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
) -> Response[
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
]:
    """Get goals in this project

     Get goals in this project. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectGoalsResponse400 | GetProjectGoalsResponse404 | GetProjectGoalsResponse500 | ProjectGoalsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
    | None
):
    """Get goals in this project

     Get goals in this project. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectGoalsResponse400 | GetProjectGoalsResponse404 | GetProjectGoalsResponse500 | ProjectGoalsEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
]:
    """Get goals in this project

     Get goals in this project. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectGoalsResponse400 | GetProjectGoalsResponse404 | GetProjectGoalsResponse500 | ProjectGoalsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetProjectGoalsResponse400
    | GetProjectGoalsResponse404
    | GetProjectGoalsResponse500
    | ProjectGoalsEnvelopeV1
    | None
):
    """Get goals in this project

     Get goals in this project. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectGoalsResponse400 | GetProjectGoalsResponse404 | GetProjectGoalsResponse500 | ProjectGoalsEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
