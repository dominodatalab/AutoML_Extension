from __future__ import annotations
from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_project_file_contents_response_400 import GetProjectFileContentsResponse400
from ...models.get_project_file_contents_response_404 import GetProjectFileContentsResponse404
from ...models.get_project_file_contents_response_500 import GetProjectFileContentsResponse500
from ...types import File, Response


def _get_kwargs(
    project_id: str,
    commit_id: str,
    path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/projects/v1/projects/{project_id}/files/{commit_id}/{path}/content".format(
            project_id=quote(str(project_id), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            path=quote(str(path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectFileContentsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProjectFileContentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetProjectFileContentsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
]:
    """Returns the contents of a file

     Return the raw contents of a file in a project at given commit.

    Args:
        project_id (str):
        commit_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | File | GetProjectFileContentsResponse400 | GetProjectFileContentsResponse404 | GetProjectFileContentsResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        commit_id=commit_id,
        path=path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
    | None
):
    """Returns the contents of a file

     Return the raw contents of a file in a project at given commit.

    Args:
        project_id (str):
        commit_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | File | GetProjectFileContentsResponse400 | GetProjectFileContentsResponse404 | GetProjectFileContentsResponse500
    """

    return sync_detailed(
        project_id=project_id,
        commit_id=commit_id,
        path=path,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
]:
    """Returns the contents of a file

     Return the raw contents of a file in a project at given commit.

    Args:
        project_id (str):
        commit_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | File | GetProjectFileContentsResponse400 | GetProjectFileContentsResponse404 | GetProjectFileContentsResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        commit_id=commit_id,
        path=path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    commit_id: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | File
    | GetProjectFileContentsResponse400
    | GetProjectFileContentsResponse404
    | GetProjectFileContentsResponse500
    | None
):
    """Returns the contents of a file

     Return the raw contents of a file in a project at given commit.

    Args:
        project_id (str):
        commit_id (str):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | File | GetProjectFileContentsResponse400 | GetProjectFileContentsResponse404 | GetProjectFileContentsResponse500
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            commit_id=commit_id,
            path=path,
            client=client,
        )
    ).parsed
