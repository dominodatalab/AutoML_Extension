from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_hardware_tier_response_400 import ArchiveHardwareTierResponse400
from ...models.archive_hardware_tier_response_404 import ArchiveHardwareTierResponse404
from ...models.archive_hardware_tier_response_500 import ArchiveHardwareTierResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.hardware_tier_envelope_v1 import HardwareTierEnvelopeV1
from ...types import Response


def _get_kwargs(
    hardware_tier_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/hardwaretiers/v1/hardwaretiers/{hardware_tier_id}".format(
            hardware_tier_id=quote(str(hardware_tier_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
    | HardwareTierEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = HardwareTierEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ArchiveHardwareTierResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ArchiveHardwareTierResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ArchiveHardwareTierResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
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
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
    | HardwareTierEnvelopeV1
]:
    """Archive a hardware tier

     Archive a hardware tier by Id. Required permissions: `ManageHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveHardwareTierResponse400 | ArchiveHardwareTierResponse404 | ArchiveHardwareTierResponse500 | FailureEnvelopeV1 | HardwareTierEnvelopeV1]
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
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
    | HardwareTierEnvelopeV1
    | None
):
    """Archive a hardware tier

     Archive a hardware tier by Id. Required permissions: `ManageHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveHardwareTierResponse400 | ArchiveHardwareTierResponse404 | ArchiveHardwareTierResponse500 | FailureEnvelopeV1 | HardwareTierEnvelopeV1
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
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
    | HardwareTierEnvelopeV1
]:
    """Archive a hardware tier

     Archive a hardware tier by Id. Required permissions: `ManageHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveHardwareTierResponse400 | ArchiveHardwareTierResponse404 | ArchiveHardwareTierResponse500 | FailureEnvelopeV1 | HardwareTierEnvelopeV1]
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
    ArchiveHardwareTierResponse400
    | ArchiveHardwareTierResponse404
    | ArchiveHardwareTierResponse500
    | FailureEnvelopeV1
    | HardwareTierEnvelopeV1
    | None
):
    """Archive a hardware tier

     Archive a hardware tier by Id. Required permissions: `ManageHardwareTiers`

    Args:
        hardware_tier_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveHardwareTierResponse400 | ArchiveHardwareTierResponse404 | ArchiveHardwareTierResponse500 | FailureEnvelopeV1 | HardwareTierEnvelopeV1
    """

    return (
        await asyncio_detailed(
            hardware_tier_id=hardware_tier_id,
            client=client,
        )
    ).parsed
