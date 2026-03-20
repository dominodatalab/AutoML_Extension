from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_hardware_tier_by_id_response_400 import GetHardwareTierByIdResponse400
from ...models.get_hardware_tier_by_id_response_404 import GetHardwareTierByIdResponse404
from ...models.get_hardware_tier_by_id_response_500 import GetHardwareTierByIdResponse500
from ...models.hardware_tier_envelope_v1 import HardwareTierEnvelopeV1
from ...types import Response


def _get_kwargs(
    hardware_tier_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/hardwaretiers/v1/hardwaretiers/{hardware_tier_id}".format(
            hardware_tier_id=quote(str(hardware_tier_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = HardwareTierEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetHardwareTierByIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetHardwareTierByIdResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetHardwareTierByIdResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
]:
    """Get a hardware tier by Id

     Get a hardware tier by Id. Required permissions: `ViewHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetHardwareTierByIdResponse400 | GetHardwareTierByIdResponse404 | GetHardwareTierByIdResponse500 | HardwareTierEnvelopeV1]
    """

    kwargs = _get_kwargs(
        hardware_tier_id=hardware_tier_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
    | None
):
    """Get a hardware tier by Id

     Get a hardware tier by Id. Required permissions: `ViewHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetHardwareTierByIdResponse400 | GetHardwareTierByIdResponse404 | GetHardwareTierByIdResponse500 | HardwareTierEnvelopeV1
    """

    return sync_detailed(
        hardware_tier_id=hardware_tier_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
]:
    """Get a hardware tier by Id

     Get a hardware tier by Id. Required permissions: `ViewHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetHardwareTierByIdResponse400 | GetHardwareTierByIdResponse404 | GetHardwareTierByIdResponse500 | HardwareTierEnvelopeV1]
    """

    kwargs = _get_kwargs(
        hardware_tier_id=hardware_tier_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hardware_tier_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetHardwareTierByIdResponse400
    | GetHardwareTierByIdResponse404
    | GetHardwareTierByIdResponse500
    | HardwareTierEnvelopeV1
    | None
):
    """Get a hardware tier by Id

     Get a hardware tier by Id. Required permissions: `ViewHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetHardwareTierByIdResponse400 | GetHardwareTierByIdResponse404 | GetHardwareTierByIdResponse500 | HardwareTierEnvelopeV1
    """

    return (
        await asyncio_detailed(
            hardware_tier_id=hardware_tier_id,
            client=client,
        )
    ).parsed
