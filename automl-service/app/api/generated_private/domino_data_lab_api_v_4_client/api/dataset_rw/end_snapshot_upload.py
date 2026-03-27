from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    upload_key: str,
    *,
    target_relative_path: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_relative_path: None | str | Unset
    if isinstance(target_relative_path, Unset):
        json_target_relative_path = UNSET
    else:
        json_target_relative_path = target_relative_path
    params["targetRelativePath"] = json_target_relative_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/datasets/{dataset_id}/snapshot/file/end/{upload_key}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            upload_key=quote(str(upload_key), safe=""),
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
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    target_relative_path: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Checks for destination consistency and if consistent, moves uploaded files to specified dataset
    directory.

    Args:
        dataset_id (str):
        upload_key (str):
        target_relative_path (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_key=upload_key,
        target_relative_path=target_relative_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    target_relative_path: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Checks for destination consistency and if consistent, moves uploaded files to specified dataset
    directory.

    Args:
        dataset_id (str):
        upload_key (str):
        target_relative_path (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        dataset_id=dataset_id,
        upload_key=upload_key,
        client=client,
        target_relative_path=target_relative_path,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    target_relative_path: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | str]:
    """Checks for destination consistency and if consistent, moves uploaded files to specified dataset
    directory.

    Args:
        dataset_id (str):
        upload_key (str):
        target_relative_path (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        upload_key=upload_key,
        target_relative_path=target_relative_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    upload_key: str,
    *,
    client: AuthenticatedClient | Client,
    target_relative_path: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | str | None:
    """Checks for destination consistency and if consistent, moves uploaded files to specified dataset
    directory.

    Args:
        dataset_id (str):
        upload_key (str):
        target_relative_path (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            upload_key=upload_key,
            client=client,
            target_relative_path=target_relative_path,
        )
    ).parsed
