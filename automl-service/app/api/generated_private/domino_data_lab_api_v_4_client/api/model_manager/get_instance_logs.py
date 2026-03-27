from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_model_instance_logs import DominoModelmanagerApiModelInstanceLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_id: str,
    model_version_id: str,
    *,
    pod_name: None | str | Unset = UNSET,
    container_name: None | str | Unset = UNSET,
    since_time_nano: float | None | Unset = UNSET,
    tail: bool | None | Unset = UNSET,
    max_results: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_pod_name: None | str | Unset
    if isinstance(pod_name, Unset):
        json_pod_name = UNSET
    else:
        json_pod_name = pod_name
    params["podName"] = json_pod_name

    json_container_name: None | str | Unset
    if isinstance(container_name, Unset):
        json_container_name = UNSET
    else:
        json_container_name = container_name
    params["containerName"] = json_container_name

    json_since_time_nano: float | None | Unset
    if isinstance(since_time_nano, Unset):
        json_since_time_nano = UNSET
    else:
        json_since_time_nano = since_time_nano
    params["sinceTimeNano"] = json_since_time_nano

    json_tail: bool | None | Unset
    if isinstance(tail, Unset):
        json_tail = UNSET
    else:
        json_tail = tail
    params["tail"] = json_tail

    params["maxResults"] = max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/getInstanceLogs/{model_id}/{model_version_id}".format(
            model_id=quote(str(model_id), safe=""),
            model_version_id=quote(str(model_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoModelmanagerApiModelInstanceLogs.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: None | str | Unset = UNSET,
    container_name: None | str | Unset = UNSET,
    since_time_nano: float | None | Unset = UNSET,
    tail: bool | None | Unset = UNSET,
    max_results: float | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]]:
    """Get model API image instance logs

    Args:
        model_id (str):
        model_version_id (str):
        pod_name (None | str | Unset):
        container_name (None | str | Unset):
        since_time_nano (float | None | Unset):
        tail (bool | None | Unset):
        max_results (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
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
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: None | str | Unset = UNSET,
    container_name: None | str | Unset = UNSET,
    since_time_nano: float | None | Unset = UNSET,
    tail: bool | None | Unset = UNSET,
    max_results: float | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs] | None:
    """Get model API image instance logs

    Args:
        model_id (str):
        model_version_id (str):
        pod_name (None | str | Unset):
        container_name (None | str | Unset):
        since_time_nano (float | None | Unset):
        tail (bool | None | Unset):
        max_results (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]
    """

    return sync_detailed(
        model_id=model_id,
        model_version_id=model_version_id,
        client=client,
        pod_name=pod_name,
        container_name=container_name,
        since_time_nano=since_time_nano,
        tail=tail,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: None | str | Unset = UNSET,
    container_name: None | str | Unset = UNSET,
    since_time_nano: float | None | Unset = UNSET,
    tail: bool | None | Unset = UNSET,
    max_results: float | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]]:
    """Get model API image instance logs

    Args:
        model_id (str):
        model_version_id (str):
        pod_name (None | str | Unset):
        container_name (None | str | Unset):
        since_time_nano (float | None | Unset):
        tail (bool | None | Unset):
        max_results (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
        pod_name=pod_name,
        container_name=container_name,
        since_time_nano=since_time_nano,
        tail=tail,
        max_results=max_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    pod_name: None | str | Unset = UNSET,
    container_name: None | str | Unset = UNSET,
    since_time_nano: float | None | Unset = UNSET,
    tail: bool | None | Unset = UNSET,
    max_results: float | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs] | None:
    """Get model API image instance logs

    Args:
        model_id (str):
        model_version_id (str):
        pod_name (None | str | Unset):
        container_name (None | str | Unset):
        since_time_nano (float | None | Unset):
        tail (bool | None | Unset):
        max_results (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelInstanceLogs]
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            model_version_id=model_version_id,
            client=client,
            pod_name=pod_name,
            container_name=container_name,
            since_time_nano=since_time_nano,
            tail=tail,
            max_results=max_results,
        )
    ).parsed
