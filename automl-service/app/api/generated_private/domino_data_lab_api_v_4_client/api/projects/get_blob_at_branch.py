from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    repo_id: str,
    branch: str,
    file_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/{repo_id}/uriForBlobAtBranch/{branch}/{file_name}".format(
            project_id=quote(str(project_id), safe=""),
            repo_id=quote(str(repo_id), safe=""),
            branch=quote(str(branch), safe=""),
            file_name=quote(str(file_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | str | None:
    if response.status_code == 200:
        response_200 = response.text
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
    repo_id: str,
    branch: str,
    file_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | str]:
    """get repository uri for blob at a specific branch for a specific file

    Args:
        project_id (str):
        repo_id (str):
        branch (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repo_id=repo_id,
        branch=branch,
        file_name=file_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    repo_id: str,
    branch: str,
    file_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | str | None:
    """get repository uri for blob at a specific branch for a specific file

    Args:
        project_id (str):
        repo_id (str):
        branch (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return sync_detailed(
        project_id=project_id,
        repo_id=repo_id,
        branch=branch,
        file_name=file_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repo_id: str,
    branch: str,
    file_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | str]:
    """get repository uri for blob at a specific branch for a specific file

    Args:
        project_id (str):
        repo_id (str):
        branch (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | str]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repo_id=repo_id,
        branch=branch,
        file_name=file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repo_id: str,
    branch: str,
    file_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | str | None:
    """get repository uri for blob at a specific branch for a specific file

    Args:
        project_id (str):
        repo_id (str):
        branch (str):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | str
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repo_id=repo_id,
            branch=branch,
            file_name=file_name,
            client=client,
        )
    ).parsed
