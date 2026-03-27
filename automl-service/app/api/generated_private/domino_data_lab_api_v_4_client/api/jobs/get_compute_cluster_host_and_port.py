from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import Response


def _get_kwargs(
    job_id: str,
    cluster_type: Any,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs/{job_id}/{cluster_type}/hostAndPort".format(
            job_id=quote(str(job_id), safe=""),
            cluster_type=quote(str(cluster_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[Any | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DominoApiErrorResponse]:
    """Gets host and port for spark web ui reverse proxy

    Args:
        job_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        cluster_type=cluster_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DominoApiErrorResponse | None:
    """Gets host and port for spark web ui reverse proxy

    Args:
        job_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        job_id=job_id,
        cluster_type=cluster_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DominoApiErrorResponse]:
    """Gets host and port for spark web ui reverse proxy

    Args:
        job_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        cluster_type=cluster_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    cluster_type: Any,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DominoApiErrorResponse | None:
    """Gets host and port for spark web ui reverse proxy

    Args:
        job_id (str):
        cluster_type (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            cluster_type=cluster_type,
            client=client,
        )
    ).parsed
