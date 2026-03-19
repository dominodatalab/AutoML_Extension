from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_version_build_logs import ModelApiVersionBuildLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_api_id: str,
    model_api_version_id: str,
    *,
    build_id: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["buildId"] = build_id

    params["sinceTimeNano"] = since_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelApis/{model_api_id}/versions/{model_api_version_id}/buildLogs".format(
            model_api_id=quote(str(model_api_id), safe=""),
            model_api_version_id=quote(str(model_api_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelApiVersionBuildLogs | None:
    if response.status_code == 200:
        response_200 = ModelApiVersionBuildLogs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelApiVersionBuildLogs]:
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
    build_id: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
) -> Response[ModelApiVersionBuildLogs]:
    """Retrieves the build logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        build_id (str | Unset):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionBuildLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        build_id=build_id,
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
    build_id: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
) -> ModelApiVersionBuildLogs | None:
    """Retrieves the build logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        build_id (str | Unset):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionBuildLogs
    """

    return sync_detailed(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        client=client,
        build_id=build_id,
        since_time_nano=since_time_nano,
    ).parsed


async def asyncio_detailed(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    build_id: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
) -> Response[ModelApiVersionBuildLogs]:
    """Retrieves the build logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        build_id (str | Unset):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionBuildLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        build_id=build_id,
        since_time_nano=since_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    build_id: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
) -> ModelApiVersionBuildLogs | None:
    """Retrieves the build logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        build_id (str | Unset):
        since_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionBuildLogs
    """

    return (
        await asyncio_detailed(
            model_api_id=model_api_id,
            model_api_version_id=model_api_version_id,
            client=client,
            build_id=build_id,
            since_time_nano=since_time_nano,
        )
    ).parsed
