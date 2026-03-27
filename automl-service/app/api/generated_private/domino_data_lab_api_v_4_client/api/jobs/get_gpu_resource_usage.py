from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_jobs_interface_job_gpu_resource_usage import DominoJobsInterfaceJobGpuResourceUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    node_type: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_node_type: None | str | Unset
    if isinstance(node_type, Unset):
        json_node_type = UNSET
    else:
        json_node_type = node_type
    params["nodeType"] = json_node_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs/jobs/{job_id}/gpuUsage".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoJobsInterfaceJobGpuResourceUsage.from_dict(response_200_item_data)

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
) -> Response[DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    node_type: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]]:
    """Get gpu usage for a Job

    Args:
        job_id (str):
        node_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        node_type=node_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    node_type: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage] | None:
    """Get gpu usage for a Job

    Args:
        job_id (str):
        node_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        node_type=node_type,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    node_type: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]]:
    """Get gpu usage for a Job

    Args:
        job_id (str):
        node_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        node_type=node_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    node_type: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage] | None:
    """Get gpu usage for a Job

    Args:
        job_id (str):
        node_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoJobsInterfaceJobGpuResourceUsage]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            node_type=node_type,
        )
    ).parsed
