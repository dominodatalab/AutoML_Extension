from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_response import AppResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_response_400 import GetAppResponse400
from ...models.get_app_response_404 import GetAppResponse404
from ...models.get_app_response_500 import GetAppResponse500
from ...types import Response


def _get_kwargs(
    app_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/{app_id}".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500 | None:
    if response.status_code == 200:
        response_200 = AppResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500]:
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
) -> Response[AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500]:
    """Get App

     Retrieve an App

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500]
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
) -> AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500 | None:
    """Get App

     Retrieve an App

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500]:
    """Get App

     Retrieve an App

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500]
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
) -> AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500 | None:
    """Get App

     Retrieve an App

    Args:
        app_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | GetAppResponse400 | GetAppResponse404 | GetAppResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
        )
    ).parsed
