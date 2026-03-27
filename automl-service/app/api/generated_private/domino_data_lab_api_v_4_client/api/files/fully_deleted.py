from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    file_path: str,
    project_id: str,
    commit_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filePath"] = file_path

    params["projectId"] = project_id

    params["commitId"] = commit_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/files/fullyDeleted",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None | DominoApiErrorResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[Any | None | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    file_path: str,
    project_id: str,
    commit_id: str,
) -> Response[Any | None | DominoApiErrorResponse]:
    """Check permanent deletion status of a file in a project starting at a commit

    Args:
        file_path (str):
        project_id (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        file_path=file_path,
        project_id=project_id,
        commit_id=commit_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    file_path: str,
    project_id: str,
    commit_id: str,
) -> Any | None | DominoApiErrorResponse | None:
    """Check permanent deletion status of a file in a project starting at a commit

    Args:
        file_path (str):
        project_id (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        file_path=file_path,
        project_id=project_id,
        commit_id=commit_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    file_path: str,
    project_id: str,
    commit_id: str,
) -> Response[Any | None | DominoApiErrorResponse]:
    """Check permanent deletion status of a file in a project starting at a commit

    Args:
        file_path (str):
        project_id (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | None | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        file_path=file_path,
        project_id=project_id,
        commit_id=commit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    file_path: str,
    project_id: str,
    commit_id: str,
) -> Any | None | DominoApiErrorResponse | None:
    """Check permanent deletion status of a file in a project starting at a commit

    Args:
        file_path (str):
        project_id (str):
        commit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | None | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            file_path=file_path,
            project_id=project_id,
            commit_id=commit_id,
        )
    ).parsed
