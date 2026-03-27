from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_files_interface_project_file import DominoFilesInterfaceProjectFile
from ...models.upload_file_body import UploadFileBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    path: str,
    *,
    body: UploadFileBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/commits/head/files/{path}".format(
            project_id=quote(str(project_id), safe=""),
            path=quote(str(path), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectFile | None:
    if response.status_code == 201:
        response_201 = DominoFilesInterfaceProjectFile.from_dict(response.json())

        return response_201

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
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectFile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectFile]:
    """uploads a file to the head commit of the project's repository

    Args:
        project_id (str):
        path (str):
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectFile]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        path=path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectFile | None:
    """uploads a file to the head commit of the project's repository

    Args:
        project_id (str):
        path (str):
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectFile
    """

    return sync_detailed(
        project_id=project_id,
        path=path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoFilesInterfaceProjectFile]:
    """uploads a file to the head commit of the project's repository

    Args:
        project_id (str):
        path (str):
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoFilesInterfaceProjectFile]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        path=path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadFileBody | Unset = UNSET,
) -> DominoApiErrorResponse | DominoFilesInterfaceProjectFile | None:
    """uploads a file to the head commit of the project's repository

    Args:
        project_id (str):
        path (str):
        body (UploadFileBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoFilesInterfaceProjectFile
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            path=path,
            client=client,
            body=body,
        )
    ).parsed
