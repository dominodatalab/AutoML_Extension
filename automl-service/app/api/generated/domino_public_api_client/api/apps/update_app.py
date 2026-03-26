from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_response import AppResponse
from ...models.app_update_request import AppUpdateRequest
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_app_response_400 import UpdateAppResponse400
from ...models.update_app_response_404 import UpdateAppResponse404
from ...models.update_app_response_500 import UpdateAppResponse500
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: AppUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/apps/beta/apps/{app_id}".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500 | None:
    if response.status_code == 200:
        response_200 = AppResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAppResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateAppResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateAppResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500]:
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
    body: AppUpdateRequest,
) -> Response[AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500]:
    """Update App

     Update an App

    Args:
        app_id (str):
        body (AppUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500]
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
    body: AppUpdateRequest,
) -> AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500 | None:
    """Update App

     Update an App

    Args:
        app_id (str):
        body (AppUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500
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
    body: AppUpdateRequest,
) -> Response[AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500]:
    """Update App

     Update an App

    Args:
        app_id (str):
        body (AppUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500]
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
    body: AppUpdateRequest,
) -> AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500 | None:
    """Update App

     Update an App

    Args:
        app_id (str):
        body (AppUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppResponse | FailureEnvelopeV1 | UpdateAppResponse400 | UpdateAppResponse404 | UpdateAppResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
