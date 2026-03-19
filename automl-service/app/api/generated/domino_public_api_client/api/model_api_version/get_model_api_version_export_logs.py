from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_version_export_logs import ModelApiVersionExportLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_api_id: str,
    model_api_version_id: str,
    *,
    since_time_nano: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sinceTimeNano"] = since_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelApis/{model_api_id}/versions/{model_api_version_id}/exportLogs".format(
            model_api_id=quote(str(model_api_id), safe=""),
            model_api_version_id=quote(str(model_api_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelApiVersionExportLogs | None:
    if response.status_code == 200:
        response_200 = ModelApiVersionExportLogs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelApiVersionExportLogs]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: str | Unset = UNSET,
) -> Response[ModelApiVersionExportLogs]:
    """Retrieves the export logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionExportLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        since_time_nano=since_time_nano,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: str | Unset = UNSET,
) -> ModelApiVersionExportLogs | None:
    """Retrieves the export logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionExportLogs
    """

    return sync_detailed(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        client=client,
        since_time_nano=since_time_nano,
    ).parsed


async def asyncio_detailed(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: str | Unset = UNSET,
) -> Response[ModelApiVersionExportLogs]:
    """Retrieves the export logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionExportLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        since_time_nano=since_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: str | Unset = UNSET,
) -> ModelApiVersionExportLogs | None:
    """Retrieves the export logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionExportLogs
    """

    return (
        await asyncio_detailed(
            model_api_id=model_api_id,
            model_api_version_id=model_api_version_id,
            client=client,
            since_time_nano=since_time_nano,
        )
    ).parsed
