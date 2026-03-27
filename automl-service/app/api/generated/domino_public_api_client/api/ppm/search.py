from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_request import SearchRequest
from ...models.search_response import SearchResponse
from ...models.search_response_400 import SearchResponse400
from ...models.search_response_404 import SearchResponse404
from ...models.search_response_500 import SearchResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: SearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/ppm/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500 | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = SearchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = SearchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
) -> Response[SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500]:
    """Search PPM Snapshots with Workspace Repository Targeting

     Search for ascending snapshot candidates that satisfy the provided package constraints. When
    workspace repositories are provided, the search is targeted to matching server repositories.

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
) -> SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500 | None:
    """Search PPM Snapshots with Workspace Repository Targeting

     Search for ascending snapshot candidates that satisfy the provided package constraints. When
    workspace repositories are provided, the search is targeted to matching server repositories.

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
) -> Response[SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500]:
    """Search PPM Snapshots with Workspace Repository Targeting

     Search for ascending snapshot candidates that satisfy the provided package constraints. When
    workspace repositories are provided, the search is targeted to matching server repositories.

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
) -> SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500 | None:
    """Search PPM Snapshots with Workspace Repository Targeting

     Search for ascending snapshot candidates that satisfy the provided package constraints. When
    workspace repositories are provided, the search is targeted to matching server repositories.

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse | SearchResponse400 | SearchResponse404 | SearchResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
