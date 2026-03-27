from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datamount_api_data_mount_dto import DominoDatamountApiDataMountDto
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    datamount_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["datamountId"] = datamount_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/datamount/projects/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

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
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    datamount_id: str,
) -> Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]:
    """Remove project

    Args:
        project_id (str):
        datamount_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        datamount_id=datamount_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    datamount_id: str,
) -> DominoApiErrorResponse | DominoDatamountApiDataMountDto | None:
    """Remove project

    Args:
        project_id (str):
        datamount_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatamountApiDataMountDto
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        datamount_id=datamount_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    datamount_id: str,
) -> Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]:
    """Remove project

    Args:
        project_id (str):
        datamount_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatamountApiDataMountDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        datamount_id=datamount_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    datamount_id: str,
) -> DominoApiErrorResponse | DominoDatamountApiDataMountDto | None:
    """Remove project

    Args:
        project_id (str):
        datamount_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatamountApiDataMountDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            datamount_id=datamount_id,
        )
    ).parsed
