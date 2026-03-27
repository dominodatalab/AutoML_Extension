from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    ignore_limit: bool,
    ignore_limits: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ignoreLimit"] = ignore_limit

    params["ignoreLimits"] = ignore_limits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasetrw/datasets/limit/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[DominoApiErrorResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_limit: bool,
    ignore_limits: bool | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Set project-level dataset limit override

    Args:
        project_id (str):
        ignore_limit (bool):
        ignore_limits (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ignore_limit=ignore_limit,
        ignore_limits=ignore_limits,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_limit: bool,
    ignore_limits: bool | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Set project-level dataset limit override

    Args:
        project_id (str):
        ignore_limit (bool):
        ignore_limits (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        ignore_limit=ignore_limit,
        ignore_limits=ignore_limits,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_limit: bool,
    ignore_limits: bool | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Set project-level dataset limit override

    Args:
        project_id (str):
        ignore_limit (bool):
        ignore_limits (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ignore_limit=ignore_limit,
        ignore_limits=ignore_limits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    ignore_limit: bool,
    ignore_limits: bool | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Set project-level dataset limit override

    Args:
        project_id (str):
        ignore_limit (bool):
        ignore_limits (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            ignore_limit=ignore_limit,
            ignore_limits=ignore_limits,
        )
    ).parsed
