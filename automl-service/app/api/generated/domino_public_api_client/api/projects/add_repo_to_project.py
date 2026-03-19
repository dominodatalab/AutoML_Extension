from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_repo_to_project_response_400 import AddRepoToProjectResponse400
from ...models.add_repo_to_project_response_404 import AddRepoToProjectResponse404
from ...models.add_repo_to_project_response_500 import AddRepoToProjectResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_project_git_repository_v1 import NewProjectGitRepositoryV1
from ...models.project_git_repository_envelope_v1 import ProjectGitRepositoryEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: NewProjectGitRepositoryV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/v1/projects/{project_id}/repositories".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectGitRepositoryEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddRepoToProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddRepoToProjectResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AddRepoToProjectResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
]:
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
    body: NewProjectGitRepositoryV1,
) -> Response[
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
]:
    """Add an imported git repository to this project

     Add an imported git repository to this project. Required permissions: `ChangeProjectSettings`

    Args:
        project_id (str):
        body (NewProjectGitRepositoryV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddRepoToProjectResponse400 | AddRepoToProjectResponse404 | AddRepoToProjectResponse500 | FailureEnvelopeV1 | ProjectGitRepositoryEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGitRepositoryV1,
) -> (
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
    | None
):
    """Add an imported git repository to this project

     Add an imported git repository to this project. Required permissions: `ChangeProjectSettings`

    Args:
        project_id (str):
        body (NewProjectGitRepositoryV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddRepoToProjectResponse400 | AddRepoToProjectResponse404 | AddRepoToProjectResponse500 | FailureEnvelopeV1 | ProjectGitRepositoryEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGitRepositoryV1,
) -> Response[
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
]:
    """Add an imported git repository to this project

     Add an imported git repository to this project. Required permissions: `ChangeProjectSettings`

    Args:
        project_id (str):
        body (NewProjectGitRepositoryV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddRepoToProjectResponse400 | AddRepoToProjectResponse404 | AddRepoToProjectResponse500 | FailureEnvelopeV1 | ProjectGitRepositoryEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewProjectGitRepositoryV1,
) -> (
    AddRepoToProjectResponse400
    | AddRepoToProjectResponse404
    | AddRepoToProjectResponse500
    | FailureEnvelopeV1
    | ProjectGitRepositoryEnvelopeV1
    | None
):
    """Add an imported git repository to this project

     Add an imported git repository to this project. Required permissions: `ChangeProjectSettings`

    Args:
        project_id (str):
        body (NewProjectGitRepositoryV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddRepoToProjectResponse400 | AddRepoToProjectResponse404 | AddRepoToProjectResponse500 | FailureEnvelopeV1 | ProjectGitRepositoryEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
