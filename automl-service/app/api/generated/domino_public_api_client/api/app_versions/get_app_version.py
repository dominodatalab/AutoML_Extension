from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_version_response import AppVersionResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_version_response_400 import GetAppVersionResponse400
from ...models.get_app_version_response_404 import GetAppVersionResponse404
from ...models.get_app_version_response_500 import GetAppVersionResponse500
from ...types import Response


def _get_kwargs(
    app_id: str,
    version_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/{app_id}/versions/{version_id}".format(
            app_id=quote(str(app_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppVersionResponse
    | FailureEnvelopeV1
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AppVersionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppVersionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppVersionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppVersionResponse500.from_dict(response.json())

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
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
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
) -> Response[
    AppVersionResponse
    | FailureEnvelopeV1
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
]:
    """Get App Version

     Retrieve an App Version

    Args:
        app_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | FailureEnvelopeV1 | GetAppVersionResponse400 | GetAppVersionResponse404 | GetAppVersionResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
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
) -> (
    AppVersionResponse
    | FailureEnvelopeV1
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
    | None
):
    """Get App Version

     Retrieve an App Version

    Args:
        app_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | FailureEnvelopeV1 | GetAppVersionResponse400 | GetAppVersionResponse404 | GetAppVersionResponse500
    """

    return sync_detailed(
        app_id=app_id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AppVersionResponse
    | FailureEnvelopeV1
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
]:
    """Get App Version

     Retrieve an App Version

    Args:
        app_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppVersionResponse | FailureEnvelopeV1 | GetAppVersionResponse400 | GetAppVersionResponse404 | GetAppVersionResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AppVersionResponse
    | FailureEnvelopeV1
    | GetAppVersionResponse400
    | GetAppVersionResponse404
    | GetAppVersionResponse500
    | None
):
    """Get App Version

     Retrieve an App Version

    Args:
        app_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppVersionResponse | FailureEnvelopeV1 | GetAppVersionResponse400 | GetAppVersionResponse404 | GetAppVersionResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            version_id=version_id,
            client=client,
        )
    ).parsed
