from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_version_instance_logs import ModelApiVersionInstanceLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_api_id: str,
    model_api_version_id: str,
    *,
    pod_name: str | Unset = UNSET,
    container_name: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
    tail: bool | Unset = UNSET,
    max_results: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["podName"] = pod_name

    params["containerName"] = container_name

    params["sinceTimeNano"] = since_time_nano

    params["tail"] = tail

    params["maxResults"] = max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelApis/{model_api_id}/versions/{model_api_version_id}/instanceLogs".format(
            model_api_id=quote(str(model_api_id), safe=""),
            model_api_version_id=quote(str(model_api_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ModelApiVersionInstanceLogs | None:
    if response.status_code == 200:
        response_200 = ModelApiVersionInstanceLogs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelApiVersionInstanceLogs]:
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
    pod_name: str | Unset = UNSET,
    container_name: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
    tail: bool | Unset = UNSET,
    max_results: int | Unset = UNSET,
) -> Response[ModelApiVersionInstanceLogs]:
    """Retrieves the instance logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        pod_name (str | Unset):
        container_name (str | Unset):
        since_time_nano (str | Unset):
        tail (bool | Unset):
        max_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionInstanceLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        pod_name=pod_name,
        container_name=container_name,
        since_time_nano=since_time_nano,
        tail=tail,
        max_results=max_results,
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
    pod_name: str | Unset = UNSET,
    container_name: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
    tail: bool | Unset = UNSET,
    max_results: int | Unset = UNSET,
) -> ModelApiVersionInstanceLogs | None:
    """Retrieves the instance logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        pod_name (str | Unset):
        container_name (str | Unset):
        since_time_nano (str | Unset):
        tail (bool | Unset):
        max_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionInstanceLogs
    """

    return sync_detailed(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        client=client,
        pod_name=pod_name,
        container_name=container_name,
        since_time_nano=since_time_nano,
        tail=tail,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: str | Unset = UNSET,
    container_name: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
    tail: bool | Unset = UNSET,
    max_results: int | Unset = UNSET,
) -> Response[ModelApiVersionInstanceLogs]:
    """Retrieves the instance logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        pod_name (str | Unset):
        container_name (str | Unset):
        since_time_nano (str | Unset):
        tail (bool | Unset):
        max_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersionInstanceLogs]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        model_api_version_id=model_api_version_id,
        pod_name=pod_name,
        container_name=container_name,
        since_time_nano=since_time_nano,
        tail=tail,
        max_results=max_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_api_id: str,
    model_api_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: str | Unset = UNSET,
    container_name: str | Unset = UNSET,
    since_time_nano: str | Unset = UNSET,
    tail: bool | Unset = UNSET,
    max_results: int | Unset = UNSET,
) -> ModelApiVersionInstanceLogs | None:
    """Retrieves the instance logs for a Model API Version.

    Args:
        model_api_id (str):
        model_api_version_id (str):
        pod_name (str | Unset):
        container_name (str | Unset):
        since_time_nano (str | Unset):
        tail (bool | Unset):
        max_results (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersionInstanceLogs
    """

    return (
        await asyncio_detailed(
            model_api_id=model_api_id,
            model_api_version_id=model_api_version_id,
            client=client,
            pod_name=pod_name,
            container_name=container_name,
            since_time_nano=since_time_nano,
            tail=tail,
            max_results=max_results,
        )
    ).parsed
