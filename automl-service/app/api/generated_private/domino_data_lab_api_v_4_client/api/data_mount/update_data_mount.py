from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datamount_api_data_mount_dto import DominoDatamountApiDataMountDto
from ...models.domino_datamount_web_update_data_mount_request import DominoDatamountWebUpdateDataMountRequest
from ...types import Response


def _get_kwargs(
    datamount_id: str,
    *,
    body: DominoDatamountWebUpdateDataMountRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datamount/{datamount_id}".format(
            datamount_id=quote(str(datamount_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatamountApiDataMountDto | None:
    if response.status_code == 200:
        response_200 = DominoDatamountApiDataMountDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datamount_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoDatamountWebUpdateDataMountRequest,
) -> Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]:
    """Update data mount

    Args:
        datamount_id (str):
        body (DominoDatamountWebUpdateDataMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]
    """

    kwargs = _get_kwargs(
        datamount_id=datamount_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datamount_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoDatamountWebUpdateDataMountRequest,
) -> DominoApiErrorResponse | DominoDatamountApiDataMountDto | None:
    """Update data mount

    Args:
        datamount_id (str):
        body (DominoDatamountWebUpdateDataMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatamountApiDataMountDto
    """

    return sync_detailed(
        datamount_id=datamount_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    datamount_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoDatamountWebUpdateDataMountRequest,
) -> Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]:
    """Update data mount

    Args:
        datamount_id (str):
        body (DominoDatamountWebUpdateDataMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]
    """

    kwargs = _get_kwargs(
        datamount_id=datamount_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datamount_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoDatamountWebUpdateDataMountRequest,
) -> DominoApiErrorResponse | DominoDatamountApiDataMountDto | None:
    """Update data mount

    Args:
        datamount_id (str):
        body (DominoDatamountWebUpdateDataMountRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatamountApiDataMountDto
    """

    return (
        await asyncio_detailed(
            datamount_id=datamount_id,
            client=client,
            body=body,
        )
    ).parsed
