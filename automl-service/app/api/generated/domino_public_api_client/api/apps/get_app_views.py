from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_views_response import AppViewsResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_app_views_response_400 import GetAppViewsResponse400
from ...models.get_app_views_response_404 import GetAppViewsResponse404
from ...models.get_app_views_response_500 import GetAppViewsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    granularity: int | Unset = 86400000,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startTimestamp"] = start_timestamp

    params["endTimestamp"] = end_timestamp

    params["granularity"] = granularity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/{app_id}/views".format(
            app_id=quote(str(app_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppViewsResponse
    | FailureEnvelopeV1
    | GetAppViewsResponse400
    | GetAppViewsResponse404
    | GetAppViewsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AppViewsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAppViewsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAppViewsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAppViewsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500
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
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    granularity: int | Unset = 86400000,
) -> Response[
    AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500
]:
    """Get App Views

     Retrieve an App's Views

    Args:
        app_id (str):
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        granularity (int | Unset):  Default: 86400000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        granularity=granularity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    granularity: int | Unset = 86400000,
) -> (
    AppViewsResponse
    | FailureEnvelopeV1
    | GetAppViewsResponse400
    | GetAppViewsResponse404
    | GetAppViewsResponse500
    | None
):
    """Get App Views

     Retrieve an App's Views

    Args:
        app_id (str):
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        granularity (int | Unset):  Default: 86400000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        granularity=granularity,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    granularity: int | Unset = 86400000,
) -> Response[
    AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500
]:
    """Get App Views

     Retrieve an App's Views

    Args:
        app_id (str):
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        granularity (int | Unset):  Default: 86400000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        granularity=granularity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_timestamp: int | Unset = UNSET,
    end_timestamp: int | Unset = UNSET,
    granularity: int | Unset = 86400000,
) -> (
    AppViewsResponse
    | FailureEnvelopeV1
    | GetAppViewsResponse400
    | GetAppViewsResponse404
    | GetAppViewsResponse500
    | None
):
    """Get App Views

     Retrieve an App's Views

    Args:
        app_id (str):
        start_timestamp (int | Unset):
        end_timestamp (int | Unset):
        granularity (int | Unset):  Default: 86400000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppViewsResponse | FailureEnvelopeV1 | GetAppViewsResponse400 | GetAppViewsResponse404 | GetAppViewsResponse500
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            granularity=granularity,
        )
    ).parsed
