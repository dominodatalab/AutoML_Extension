from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_model_resource_usage import DominoModelmanagerApiModelResourceUsage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_id: str,
    model_version_id: str,
    *,
    limit: int | None | Unset = 256,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/{model_id}/{model_version_id}/usage".format(
            model_id=quote(str(model_id), safe=""),
            model_version_id=quote(str(model_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage | None:
    if response.status_code == 200:
        response_200 = DominoModelmanagerApiModelResourceUsage.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage]:
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
    limit: int | None | Unset = 256,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage]:
    """Get resource usage for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
        limit=limit,
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
    limit: int | None | Unset = 256,
) -> DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage | None:
    """Get resource usage for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage
    """

    return sync_detailed(
        model_id=model_id,
        model_version_id=model_version_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 256,
) -> Response[DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage]:
    """Get resource usage for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
        model_version_id=model_version_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_id: str,
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | None | Unset = 256,
) -> DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage | None:
    """Get resource usage for a model API

    Args:
        model_id (str):
        model_version_id (str):
        limit (int | None | Unset):  Default: 256.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoModelmanagerApiModelResourceUsage
    """

    return (
        await asyncio_detailed(
            model_id=model_id,
            model_version_id=model_version_id,
            client=client,
            limit=limit,
        )
    ).parsed
