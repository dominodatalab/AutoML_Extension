from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_file_matches_dto import DominoFilesInterfaceFileMatchesDto
from ...models.domino_files_interface_file_search_query import DominoFilesInterfaceFileSearchQuery
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: DominoFilesInterfaceFileSearchQuery,
    max_results: int | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_max_results: int | None | Unset
    if isinstance(max_results, Unset):
        json_max_results = UNSET
    else:
        json_max_results = max_results
    params["maxResults"] = json_max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/search/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto | None:
    if response.status_code == 200:
        response_200 = DominoFilesInterfaceFileMatchesDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto]:
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
    body: DominoFilesInterfaceFileSearchQuery,
    max_results: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto]:
    """Search for files in a project by matching on path with string queries

    Args:
        project_id (str):
        max_results (int | None | Unset):
        body (DominoFilesInterfaceFileSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        max_results=max_results,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoFilesInterfaceFileSearchQuery,
    max_results: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto | None:
    """Search for files in a project by matching on path with string queries

    Args:
        project_id (str):
        max_results (int | None | Unset):
        body (DominoFilesInterfaceFileSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        max_results=max_results,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoFilesInterfaceFileSearchQuery,
    max_results: int | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto]:
    """Search for files in a project by matching on path with string queries

    Args:
        project_id (str):
        max_results (int | None | Unset):
        body (DominoFilesInterfaceFileSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        max_results=max_results,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoFilesInterfaceFileSearchQuery,
    max_results: int | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto | None:
    """Search for files in a project by matching on path with string queries

    Args:
        project_id (str):
        max_results (int | None | Unset):
        body (DominoFilesInterfaceFileSearchQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceFileMatchesDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            max_results=max_results,
        )
    ).parsed
