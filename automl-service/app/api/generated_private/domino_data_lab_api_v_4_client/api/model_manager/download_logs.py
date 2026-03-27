from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response


def _get_kwargs(
    model_version_id: str,
    *,
    start_millis: int,
    end_millis: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startMillis"] = start_millis

    params["endMillis"] = end_millis

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/{model_version_id}/logs".format(
            model_version_id=quote(str(model_version_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DominoApiErrorResponse | None:
    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_millis: int,
    end_millis: int,
) -> Response[DominoApiErrorResponse]:
    """download logs for a model for a given time range

    Args:
        model_version_id (str):
        start_millis (int):
        end_millis (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        start_millis=start_millis,
        end_millis=end_millis,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_millis: int,
    end_millis: int,
) -> DominoApiErrorResponse | None:
    """download logs for a model for a given time range

    Args:
        model_version_id (str):
        start_millis (int):
        end_millis (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse
    """

    return sync_detailed(
        model_version_id=model_version_id,
        client=client,
        start_millis=start_millis,
        end_millis=end_millis,
    ).parsed


async def asyncio_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_millis: int,
    end_millis: int,
) -> Response[DominoApiErrorResponse]:
    """download logs for a model for a given time range

    Args:
        model_version_id (str):
        start_millis (int):
        end_millis (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        start_millis=start_millis,
        end_millis=end_millis,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_millis: int,
    end_millis: int,
) -> DominoApiErrorResponse | None:
    """download logs for a model for a given time range

    Args:
        model_version_id (str):
        start_millis (int):
        end_millis (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            model_version_id=model_version_id,
            client=client,
            start_millis=start_millis,
            end_millis=end_millis,
        )
    ).parsed
