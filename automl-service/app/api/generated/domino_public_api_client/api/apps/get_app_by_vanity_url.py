from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_response import AppResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_by_vanity_url_response_400 import GetAppByVanityUrlResponse400
from ...models.get_app_by_vanity_url_response_404 import GetAppByVanityUrlResponse404
from ...models.get_app_by_vanity_url_response_500 import GetAppByVanityUrlResponse500
from ...types import Response


def _get_kwargs(
    vanity_url: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/vanityUrls/{vanity_url}".format(
            vanity_url=quote(str(vanity_url), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AppResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppByVanityUrlResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppByVanityUrlResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppByVanityUrlResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
]:
    """Get App by Vanity URL

     Retrieve an App by Vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | GetAppByVanityUrlResponse400 | GetAppByVanityUrlResponse404 | GetAppByVanityUrlResponse500]
    """

    kwargs = _get_kwargs(
        vanity_url=vanity_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
    | None
):
    """Get App by Vanity URL

     Retrieve an App by Vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | GetAppByVanityUrlResponse400 | GetAppByVanityUrlResponse404 | GetAppByVanityUrlResponse500
    """

    return sync_detailed(
        vanity_url=vanity_url,
        client=client,
    ).parsed


async def asyncio_detailed(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
]:
    """Get App by Vanity URL

     Retrieve an App by Vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | GetAppByVanityUrlResponse400 | GetAppByVanityUrlResponse404 | GetAppByVanityUrlResponse500]
    """

    kwargs = _get_kwargs(
        vanity_url=vanity_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AppResponse
    | FailureEnvelopeV1
    | GetAppByVanityUrlResponse400
    | GetAppByVanityUrlResponse404
    | GetAppByVanityUrlResponse500
    | None
):
    """Get App by Vanity URL

     Retrieve an App by Vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | GetAppByVanityUrlResponse400 | GetAppByVanityUrlResponse404 | GetAppByVanityUrlResponse500
    """

    return (
        await asyncio_detailed(
            vanity_url=vanity_url,
            client=client,
        )
    ).parsed
