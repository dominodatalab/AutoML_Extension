from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_version_response import AppVersionResponse
from ...models.app_version_update_request import AppVersionUpdateRequest
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_app_version_response_400 import UpdateAppVersionResponse400
from ...models.update_app_version_response_404 import UpdateAppVersionResponse404
from ...models.update_app_version_response_500 import UpdateAppVersionResponse500
from ...types import Response


def _get_kwargs(
    app_id: str,
    version_id: str,
    *,
    body: AppVersionUpdateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/apps/beta/apps/{app_id}/versions/{version_id}".format(
            app_id=quote(str(app_id), safe=""),
            version_id=quote(str(version_id), safe=""),
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
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AppVersionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAppVersionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateAppVersionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateAppVersionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppVersionResponse
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppVersionUpdateRequest,
) -> Response[
    AppVersionResponse
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
]:
    """Update App Version

     Update an App Version

    Args:
        app_id (str):
        version_id (str):
        body (AppVersionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | FailureEnvelopeV1 | UpdateAppVersionResponse400 | UpdateAppVersionResponse404 | UpdateAppVersionResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppVersionUpdateRequest,
) -> (
    AppVersionResponse
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
    | None
):
    """Update App Version

     Update an App Version

    Args:
        app_id (str):
        version_id (str):
        body (AppVersionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | FailureEnvelopeV1 | UpdateAppVersionResponse400 | UpdateAppVersionResponse404 | UpdateAppVersionResponse500
    """

    return sync_detailed(
        app_id=app_id,
        version_id=version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppVersionUpdateRequest,
) -> Response[
    AppVersionResponse
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
]:
    """Update App Version

     Update an App Version

    Args:
        app_id (str):
        version_id (str):
        body (AppVersionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | FailureEnvelopeV1 | UpdateAppVersionResponse400 | UpdateAppVersionResponse404 | UpdateAppVersionResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AppVersionUpdateRequest,
) -> (
    AppVersionResponse
    | FailureEnvelopeV1
    | UpdateAppVersionResponse400
    | UpdateAppVersionResponse404
    | UpdateAppVersionResponse500
    | None
):
    """Update App Version

     Update an App Version

    Args:
        app_id (str):
        version_id (str):
        body (AppVersionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | FailureEnvelopeV1 | UpdateAppVersionResponse400 | UpdateAppVersionResponse404 | UpdateAppVersionResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            version_id=version_id,
            client=client,
            body=body,
        )
    ).parsed
