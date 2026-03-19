from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_endpoint_version_by_number_response_400 import GetEndpointVersionByNumberResponse400
from ...models.get_endpoint_version_by_number_response_404 import GetEndpointVersionByNumberResponse404
from ...models.get_endpoint_version_by_number_response_500 import GetEndpointVersionByNumberResponse500
from ...models.model_endpoint_version_v1 import ModelEndpointVersionV1
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
    version_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gen-ai/beta/endpoints/{endpoint_id}/versions/{version_number}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
    | None
):
    if response.status_code == 200:
        response_200 = ModelEndpointVersionV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEndpointVersionByNumberResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEndpointVersionByNumberResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetEndpointVersionByNumberResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
]:
    """Get a Gen AI Endpoint Version

     Get a Gen AI Endpoint Version

    Args:
        endpoint_id (str):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointVersionByNumberResponse400 | GetEndpointVersionByNumberResponse404 | GetEndpointVersionByNumberResponse500 | ModelEndpointVersionV1]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
    | None
):
    """Get a Gen AI Endpoint Version

     Get a Gen AI Endpoint Version

    Args:
        endpoint_id (str):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointVersionByNumberResponse400 | GetEndpointVersionByNumberResponse404 | GetEndpointVersionByNumberResponse500 | ModelEndpointVersionV1
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        version_number=version_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
]:
    """Get a Gen AI Endpoint Version

     Get a Gen AI Endpoint Version

    Args:
        endpoint_id (str):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointVersionByNumberResponse400 | GetEndpointVersionByNumberResponse404 | GetEndpointVersionByNumberResponse500 | ModelEndpointVersionV1]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetEndpointVersionByNumberResponse400
    | GetEndpointVersionByNumberResponse404
    | GetEndpointVersionByNumberResponse500
    | ModelEndpointVersionV1
    | None
):
    """Get a Gen AI Endpoint Version

     Get a Gen AI Endpoint Version

    Args:
        endpoint_id (str):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointVersionByNumberResponse400 | GetEndpointVersionByNumberResponse404 | GetEndpointVersionByNumberResponse500 | ModelEndpointVersionV1
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            version_number=version_number,
            client=client,
        )
    ).parsed
