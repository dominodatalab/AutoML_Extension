from __future__ import annotations
from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_thumbnail_response_400 import GetAppThumbnailResponse400
from ...models.get_app_thumbnail_response_404 import GetAppThumbnailResponse404
from ...models.get_app_thumbnail_response_500 import GetAppThumbnailResponse500
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/{app_id}/thumbnail".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | File
    | GetAppThumbnailResponse400
    | GetAppThumbnailResponse404
    | GetAppThumbnailResponse500
    | None
):
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 400:
        response_400 = GetAppThumbnailResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppThumbnailResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppThumbnailResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500
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
    if_none_match: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500
]:
    """Get App Thumbnail

     Retrieve an App's thumbnail image

    Args:
        app_id (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | File
    | GetAppThumbnailResponse400
    | GetAppThumbnailResponse404
    | GetAppThumbnailResponse500
    | None
):
    """Get App Thumbnail

     Retrieve an App's thumbnail image

    Args:
        app_id (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500
]:
    """Get App Thumbnail

     Retrieve an App's thumbnail image

    Args:
        app_id (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    if_none_match: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | File
    | GetAppThumbnailResponse400
    | GetAppThumbnailResponse404
    | GetAppThumbnailResponse500
    | None
):
    """Get App Thumbnail

     Retrieve an App's thumbnail image

    Args:
        app_id (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | File | GetAppThumbnailResponse400 | GetAppThumbnailResponse404 | GetAppThumbnailResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
