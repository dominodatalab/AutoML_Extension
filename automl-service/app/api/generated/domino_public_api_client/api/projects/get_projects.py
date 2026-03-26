from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_projects_response_400 import GetProjectsResponse400
from ...models.get_projects_response_404 import GetProjectsResponse404
from ...models.get_projects_response_500 import GetProjectsResponse500
from ...models.paginated_projects_envelope_v1 import PaginatedProjectsEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/projects/beta/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedProjectsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProjectsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetProjectsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
]:
    """Get Projects visible to user

     Get projects that a user can see. Required permissions: `ListProject`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectsResponse400 | GetProjectsResponse404 | GetProjectsResponse500 | PaginatedProjectsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
    | None
):
    """Get Projects visible to user

     Get projects that a user can see. Required permissions: `ListProject`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectsResponse400 | GetProjectsResponse404 | GetProjectsResponse500 | PaginatedProjectsEnvelopeV1
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
]:
    """Get Projects visible to user

     Get projects that a user can see. Required permissions: `ListProject`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectsResponse400 | GetProjectsResponse404 | GetProjectsResponse500 | PaginatedProjectsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetProjectsResponse400
    | GetProjectsResponse404
    | GetProjectsResponse500
    | PaginatedProjectsEnvelopeV1
    | None
):
    """Get Projects visible to user

     Get projects that a user can see. Required permissions: `ListProject`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectsResponse400 | GetProjectsResponse404 | GetProjectsResponse500 | PaginatedProjectsEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
