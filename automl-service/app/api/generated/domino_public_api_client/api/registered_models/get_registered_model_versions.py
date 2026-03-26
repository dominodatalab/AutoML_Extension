from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_registered_model_versions_response_400 import GetRegisteredModelVersionsResponse400
from ...models.get_registered_model_versions_response_404 import GetRegisteredModelVersionsResponse404
from ...models.get_registered_model_versions_response_500 import GetRegisteredModelVersionsResponse500
from ...models.paginated_registered_model_version_overview_envelope_v1 import (
    PaginatedRegisteredModelVersionOverviewEnvelopeV1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_name: str,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/{model_name}/versions".format(
            model_name=quote(str(model_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedRegisteredModelVersionOverviewEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRegisteredModelVersionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRegisteredModelVersionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetRegisteredModelVersionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
]:
    """Get all versions of a Registered Model

     Get all versions of a Registered Model

    Args:
        model_name (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelVersionsResponse400 | GetRegisteredModelVersionsResponse404 | GetRegisteredModelVersionsResponse500 | PaginatedRegisteredModelVersionOverviewEnvelopeV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
    | None
):
    """Get all versions of a Registered Model

     Get all versions of a Registered Model

    Args:
        model_name (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelVersionsResponse400 | GetRegisteredModelVersionsResponse404 | GetRegisteredModelVersionsResponse500 | PaginatedRegisteredModelVersionOverviewEnvelopeV1
    """

    return sync_detailed(
        model_name=model_name,
        client=client,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
]:
    """Get all versions of a Registered Model

     Get all versions of a Registered Model

    Args:
        model_name (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelVersionsResponse400 | GetRegisteredModelVersionsResponse404 | GetRegisteredModelVersionsResponse500 | PaginatedRegisteredModelVersionOverviewEnvelopeV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionsResponse400
    | GetRegisteredModelVersionsResponse404
    | GetRegisteredModelVersionsResponse500
    | PaginatedRegisteredModelVersionOverviewEnvelopeV1
    | None
):
    """Get all versions of a Registered Model

     Get all versions of a Registered Model

    Args:
        model_name (str):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelVersionsResponse400 | GetRegisteredModelVersionsResponse404 | GetRegisteredModelVersionsResponse500 | PaginatedRegisteredModelVersionOverviewEnvelopeV1
    """

    return (
        await asyncio_detailed(
            model_name=model_name,
            client=client,
            offset=offset,
            limit=limit,
        )
    ).parsed
