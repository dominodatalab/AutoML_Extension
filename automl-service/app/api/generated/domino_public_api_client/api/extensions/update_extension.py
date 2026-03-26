from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extension_patch_request import ExtensionPatchRequest
from ...models.extension_response import ExtensionResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_extension_response_400 import UpdateExtensionResponse400
from ...models.update_extension_response_404 import UpdateExtensionResponse404
from ...models.update_extension_response_500 import UpdateExtensionResponse500
from ...types import Response


def _get_kwargs(
    extension_id: str,
    *,
    body: ExtensionPatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/extensions/beta/extensions/{extension_id}".format(
            extension_id=quote(str(extension_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ExtensionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateExtensionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateExtensionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateExtensionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
]:
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
    body: ExtensionPatchRequest,
) -> Response[
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
]:
    """Update an Extension by id

     Update an Extension by id

    Args:
        extension_id (str):
        body (ExtensionPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionResponse | FailureEnvelopeV1 | UpdateExtensionResponse400 | UpdateExtensionResponse404 | UpdateExtensionResponse500]
    """

    kwargs = _get_kwargs(
        extension_id=extension_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtensionPatchRequest,
) -> (
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
    | None
):
    """Update an Extension by id

     Update an Extension by id

    Args:
        extension_id (str):
        body (ExtensionPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionResponse | FailureEnvelopeV1 | UpdateExtensionResponse400 | UpdateExtensionResponse404 | UpdateExtensionResponse500
    """

    return sync_detailed(
        extension_id=extension_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtensionPatchRequest,
) -> Response[
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
]:
    """Update an Extension by id

     Update an Extension by id

    Args:
        extension_id (str):
        body (ExtensionPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionResponse | FailureEnvelopeV1 | UpdateExtensionResponse400 | UpdateExtensionResponse404 | UpdateExtensionResponse500]
    """

    kwargs = _get_kwargs(
        extension_id=extension_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extension_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExtensionPatchRequest,
) -> (
    ExtensionResponse
    | FailureEnvelopeV1
    | UpdateExtensionResponse400
    | UpdateExtensionResponse404
    | UpdateExtensionResponse500
    | None
):
    """Update an Extension by id

     Update an Extension by id

    Args:
        extension_id (str):
        body (ExtensionPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionResponse | FailureEnvelopeV1 | UpdateExtensionResponse400 | UpdateExtensionResponse404 | UpdateExtensionResponse500
    """

    return (
        await asyncio_detailed(
            extension_id=extension_id,
            client=client,
            body=body,
        )
    ).parsed
