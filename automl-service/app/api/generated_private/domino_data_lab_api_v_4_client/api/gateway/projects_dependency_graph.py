from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_gateway_users_models_projects_dependency_graph import (
    DominoNucleusGatewayUsersModelsProjectsDependencyGraph,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    owner_username: None | str | Unset = UNSET,
    project_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_owner_username: None | str | Unset
    if isinstance(owner_username, Unset):
        json_owner_username = UNSET
    else:
        json_owner_username = owner_username
    params["ownerUsername"] = json_owner_username

    json_project_name: None | str | Unset
    if isinstance(project_name, Unset):
        json_project_name = UNSET
    else:
        json_project_name = project_name
    params["projectName"] = json_project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateway/users/projectsDependencyGraph",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph | None:
    if response.status_code == 200:
        response_200 = DominoNucleusGatewayUsersModelsProjectsDependencyGraph.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: None | str | Unset = UNSET,
    project_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph]:
    """Retrieves projects dependency graph for a user, and optionally for a specific project

    Args:
        owner_username (None | str | Unset):
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    owner_username: None | str | Unset = UNSET,
    project_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph | None:
    """Retrieves projects dependency graph for a user, and optionally for a specific project

    Args:
        owner_username (None | str | Unset):
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph
    """

    return sync_detailed(
        client=client,
        owner_username=owner_username,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_username: None | str | Unset = UNSET,
    project_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph]:
    """Retrieves projects dependency graph for a user, and optionally for a specific project

    Args:
        owner_username (None | str | Unset):
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph]
    """

    kwargs = _get_kwargs(
        owner_username=owner_username,
        project_name=project_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_username: None | str | Unset = UNSET,
    project_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph | None:
    """Retrieves projects dependency graph for a user, and optionally for a specific project

    Args:
        owner_username (None | str | Unset):
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusGatewayUsersModelsProjectsDependencyGraph
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_username=owner_username,
            project_name=project_name,
        )
    ).parsed
