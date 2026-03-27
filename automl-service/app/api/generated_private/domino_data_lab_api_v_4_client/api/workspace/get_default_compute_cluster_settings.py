from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_computecluster_api_default_compute_cluster_settings import (
    DominoComputeclusterApiDefaultComputeClusterSettings,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    cluster_type: Any,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/{project_id}/{cluster_type}/defaultComputeClusterSettings".format(
            project_id=quote(str(project_id), safe=""),
            cluster_type=quote(str(cluster_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings | None:
    if response.status_code == 200:
        response_200 = DominoComputeclusterApiDefaultComputeClusterSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings]:
    """Get the default compute settings for workspaces

    Args:
        project_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cluster_type=cluster_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings | None:
    """Get the default compute settings for workspaces

    Args:
        project_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings
    """

    return sync_detailed(
        project_id=project_id,
        cluster_type=cluster_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings]:
    """Get the default compute settings for workspaces

    Args:
        project_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cluster_type=cluster_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings | None:
    """Get the default compute settings for workspaces

    Args:
        project_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoComputeclusterApiDefaultComputeClusterSettings
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cluster_type=cluster_type,
            client=client,
        )
    ).parsed
