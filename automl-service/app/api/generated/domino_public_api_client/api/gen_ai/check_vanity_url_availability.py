from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_vanity_url_availability_response_400 import CheckVanityUrlAvailabilityResponse400
from ...models.check_vanity_url_availability_response_404 import CheckVanityUrlAvailabilityResponse404
from ...models.check_vanity_url_availability_response_500 import CheckVanityUrlAvailabilityResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.vanity_url_availability_v1 import VanityUrlAvailabilityV1
from ...types import Response


def _get_kwargs(
    vanity_url: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gen-ai/beta/vanity-url-availability/{vanity_url}".format(
            vanity_url=quote(str(vanity_url), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
    | None
):
    if response.status_code == 200:
        response_200 = VanityUrlAvailabilityV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CheckVanityUrlAvailabilityResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CheckVanityUrlAvailabilityResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CheckVanityUrlAvailabilityResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
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
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
]:
    """Check if a vanity URL is available

     Check if a vanity URL is available

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckVanityUrlAvailabilityResponse400 | CheckVanityUrlAvailabilityResponse404 | CheckVanityUrlAvailabilityResponse500 | FailureEnvelopeV1 | VanityUrlAvailabilityV1]
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
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
    | None
):
    """Check if a vanity URL is available

     Check if a vanity URL is available

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckVanityUrlAvailabilityResponse400 | CheckVanityUrlAvailabilityResponse404 | CheckVanityUrlAvailabilityResponse500 | FailureEnvelopeV1 | VanityUrlAvailabilityV1
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
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
]:
    """Check if a vanity URL is available

     Check if a vanity URL is available

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckVanityUrlAvailabilityResponse400 | CheckVanityUrlAvailabilityResponse404 | CheckVanityUrlAvailabilityResponse500 | FailureEnvelopeV1 | VanityUrlAvailabilityV1]
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
    CheckVanityUrlAvailabilityResponse400
    | CheckVanityUrlAvailabilityResponse404
    | CheckVanityUrlAvailabilityResponse500
    | FailureEnvelopeV1
    | VanityUrlAvailabilityV1
    | None
):
    """Check if a vanity URL is available

     Check if a vanity URL is available

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckVanityUrlAvailabilityResponse400 | CheckVanityUrlAvailabilityResponse404 | CheckVanityUrlAvailabilityResponse500 | FailureEnvelopeV1 | VanityUrlAvailabilityV1
    """

    return (
        await asyncio_detailed(
            vanity_url=vanity_url,
            client=client,
        )
    ).parsed
