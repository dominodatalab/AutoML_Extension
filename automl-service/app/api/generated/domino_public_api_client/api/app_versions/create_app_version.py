from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_version_creation_request import AppVersionCreationRequest
from ...models.app_version_response import AppVersionResponse
from ...models.create_app_version_response_400 import CreateAppVersionResponse400
from ...models.create_app_version_response_404 import CreateAppVersionResponse404
from ...models.create_app_version_response_500 import CreateAppVersionResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    body: AppVersionCreationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/apps/beta/apps/{app_id}/versions".format(
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
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = AppVersionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateAppVersionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateAppVersionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateAppVersionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
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
    body: AppVersionCreationRequest,
) -> Response[
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
    | FailureEnvelopeV1
]:
    """Create App Version

     Create an App Version

    Args:
        app_id (str):
        body (AppVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | CreateAppVersionResponse400 | CreateAppVersionResponse404 | CreateAppVersionResponse500 | FailureEnvelopeV1]
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
    body: AppVersionCreationRequest,
) -> (
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
    | FailureEnvelopeV1
    | None
):
    """Create App Version

     Create an App Version

    Args:
        app_id (str):
        body (AppVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | CreateAppVersionResponse400 | CreateAppVersionResponse404 | CreateAppVersionResponse500 | FailureEnvelopeV1
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
    body: AppVersionCreationRequest,
) -> Response[
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
    | FailureEnvelopeV1
]:
    """Create App Version

     Create an App Version

    Args:
        app_id (str):
        body (AppVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | CreateAppVersionResponse400 | CreateAppVersionResponse404 | CreateAppVersionResponse500 | FailureEnvelopeV1]
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
    body: AppVersionCreationRequest,
) -> (
    AppVersionResponse
    | CreateAppVersionResponse400
    | CreateAppVersionResponse404
    | CreateAppVersionResponse500
    | FailureEnvelopeV1
    | None
):
    """Create App Version

     Create an App Version

    Args:
        app_id (str):
        body (AppVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | CreateAppVersionResponse400 | CreateAppVersionResponse404 | CreateAppVersionResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
        )
    ).parsed
