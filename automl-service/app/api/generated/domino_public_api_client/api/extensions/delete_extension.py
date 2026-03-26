from __future__ import annotations
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_extension_response_404 import DeleteExtensionResponse404
from ...models.delete_extension_response_500 import DeleteExtensionResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    extension_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/extensions/beta/extensions/{extension_id}".format(
            extension_id=quote(str(extension_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteExtensionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteExtensionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1]:
    """Soft delete an Extension by id

     Soft delete an Extension by id

    Args:
        extension_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        extension_id=extension_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1 | None:
    """Soft delete an Extension by id

     Soft delete an Extension by id

    Args:
        extension_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        extension_id=extension_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1]:
    """Soft delete an Extension by id

     Soft delete an Extension by id

    Args:
        extension_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        extension_id=extension_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1 | None:
    """Soft delete an Extension by id

     Soft delete an Extension by id

    Args:
        extension_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteExtensionResponse404 | DeleteExtensionResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            extension_id=extension_id,
            client=client,
        )
    ).parsed
