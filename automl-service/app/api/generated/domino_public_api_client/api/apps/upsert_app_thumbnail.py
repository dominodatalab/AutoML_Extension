from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.upsert_app_thumbnail_request import UpsertAppThumbnailRequest
from ...models.upsert_app_thumbnail_response import UpsertAppThumbnailResponse
from ...models.upsert_app_thumbnail_response_400 import UpsertAppThumbnailResponse400
from ...models.upsert_app_thumbnail_response_404 import UpsertAppThumbnailResponse404
from ...models.upsert_app_thumbnail_response_500 import UpsertAppThumbnailResponse500
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: UpsertAppThumbnailRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/apps/beta/apps/{app_id}/thumbnail".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = UpsertAppThumbnailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = UpsertAppThumbnailResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UpsertAppThumbnailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpsertAppThumbnailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpsertAppThumbnailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertAppThumbnailRequest,
) -> Response[
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
]:
    """Upsert App Thumbnail

     Create or replace an App's thumbnail

    Args:
        app_id (str):
        body (UpsertAppThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | UpsertAppThumbnailResponse | UpsertAppThumbnailResponse400 | UpsertAppThumbnailResponse404 | UpsertAppThumbnailResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertAppThumbnailRequest,
) -> (
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
    | None
):
    """Upsert App Thumbnail

     Create or replace an App's thumbnail

    Args:
        app_id (str):
        body (UpsertAppThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | UpsertAppThumbnailResponse | UpsertAppThumbnailResponse400 | UpsertAppThumbnailResponse404 | UpsertAppThumbnailResponse500
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertAppThumbnailRequest,
) -> Response[
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
]:
    """Upsert App Thumbnail

     Create or replace an App's thumbnail

    Args:
        app_id (str):
        body (UpsertAppThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | UpsertAppThumbnailResponse | UpsertAppThumbnailResponse400 | UpsertAppThumbnailResponse404 | UpsertAppThumbnailResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertAppThumbnailRequest,
) -> (
    FailureEnvelopeV1
    | UpsertAppThumbnailResponse
    | UpsertAppThumbnailResponse400
    | UpsertAppThumbnailResponse404
    | UpsertAppThumbnailResponse500
    | None
):
    """Upsert App Thumbnail

     Create or replace an App's thumbnail

    Args:
        app_id (str):
        body (UpsertAppThumbnailRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | UpsertAppThumbnailResponse | UpsertAppThumbnailResponse400 | UpsertAppThumbnailResponse404 | UpsertAppThumbnailResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
