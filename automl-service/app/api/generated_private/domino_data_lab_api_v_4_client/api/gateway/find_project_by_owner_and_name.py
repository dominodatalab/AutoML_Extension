from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_server_projects_api_project_gateway_overview import DominoServerProjectsApiProjectGatewayOverview
from ...types import UNSET, Response


def _get_kwargs(
    *,
    owner_name: str,
    project_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerName"] = owner_name

    params["projectName"] = project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateway/projects/findProjectByOwnerAndName",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview | None:
    if response.status_code == 200:
        response_200 = DominoServerProjectsApiProjectGatewayOverview.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> Response[DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview]:
    """Retrieves a project for the Project Overview UI

    Args:
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview]
    """

    kwargs = _get_kwargs(
        owner_name=owner_name,
        project_name=project_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview | None:
    """Retrieves a project for the Project Overview UI

    Args:
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview
    """

    return sync_detailed(
        client=client,
        owner_name=owner_name,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> Response[DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview]:
    """Retrieves a project for the Project Overview UI

    Args:
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview]
    """

    kwargs = _get_kwargs(
        owner_name=owner_name,
        project_name=project_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview | None:
    """Retrieves a project for the Project Overview UI

    Args:
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoServerProjectsApiProjectGatewayOverview
    """

    return (
        await asyncio_detailed(
            client=client,
            owner_name=owner_name,
            project_name=project_name,
        )
    ).parsed
