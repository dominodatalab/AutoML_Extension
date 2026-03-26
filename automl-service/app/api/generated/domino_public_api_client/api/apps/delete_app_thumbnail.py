from __future__ import annotations
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_app_thumbnail_response_400 import DeleteAppThumbnailResponse400
from ...models.delete_app_thumbnail_response_404 import DeleteAppThumbnailResponse404
from ...models.delete_app_thumbnail_response_500 import DeleteAppThumbnailResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    app_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/apps/beta/apps/{app_id}/thumbnail".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteAppThumbnailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteAppThumbnailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeleteAppThumbnailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
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
) -> Response[
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
]:
    """Delete App Thumbnail

     Delete an App's thumbnail

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppThumbnailResponse400 | DeleteAppThumbnailResponse404 | DeleteAppThumbnailResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete App Thumbnail

     Delete an App's thumbnail

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppThumbnailResponse400 | DeleteAppThumbnailResponse404 | DeleteAppThumbnailResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
]:
    """Delete App Thumbnail

     Delete an App's thumbnail

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAppThumbnailResponse400 | DeleteAppThumbnailResponse404 | DeleteAppThumbnailResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteAppThumbnailResponse400
    | DeleteAppThumbnailResponse404
    | DeleteAppThumbnailResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete App Thumbnail

     Delete an App's thumbnail

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAppThumbnailResponse400 | DeleteAppThumbnailResponse404 | DeleteAppThumbnailResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
        )
    ).parsed
