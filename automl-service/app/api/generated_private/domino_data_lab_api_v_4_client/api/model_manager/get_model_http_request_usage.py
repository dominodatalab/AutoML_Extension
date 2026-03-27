from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_model_http_request_usage import DominoModelmanagerApiModelHttpRequestUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_id: str,
    model_version_id: str,
    *,
    limit: int | None | Unset = UNSET,
    time_range_minutes: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_time_range_minutes: int | None | Unset
    if isinstance(time_range_minutes, Unset):
        json_time_range_minutes = UNSET
    else:
        json_time_range_minutes = time_range_minutes
    params["timeRangeMinutes"] = json_time_range_minutes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/{model_id}/{model_version_id}/httpRequests".format(
            model_id=quote(str(model_id), safe=""),
            model_version_id=quote(str(model_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage | None:
    if response.status_code == 200:
        response_200 = DominoModelmanagerApiModelHttpRequestUsage.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage]:
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
    limit: int | None | Unset = UNSET,
    time_range_minutes: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage]:
    """Get HTTP request usage by status code for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):
        time_range_minutes (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
        limit=limit,
        time_range_minutes=time_range_minutes,
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
    limit: int | None | Unset = UNSET,
    time_range_minutes: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage | None:
    """Get HTTP request usage by status code for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):
        time_range_minutes (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage
    """

    return sync_detailed(
        model_id=model_id,
        model_version_id=model_version_id,
        client=client,
        limit=limit,
        time_range_minutes=time_range_minutes,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = UNSET,
    time_range_minutes: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage]:
    """Get HTTP request usage by status code for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):
        time_range_minutes (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
        limit=limit,
        time_range_minutes=time_range_minutes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = UNSET,
    time_range_minutes: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage | None:
    """Get HTTP request usage by status code for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):
        time_range_minutes (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiModelHttpRequestUsage
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            model_version_id=model_version_id,
            client=client,
            limit=limit,
            time_range_minutes=time_range_minutes,
        )
    ).parsed
