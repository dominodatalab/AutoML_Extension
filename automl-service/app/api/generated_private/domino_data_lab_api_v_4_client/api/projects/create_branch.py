from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_repositories_responses_create_branch_api_response import (
    DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    repository_id: str,
    new_branch_name: str,
    *,
    from_branch_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_branch_name: None | str | Unset
    if isinstance(from_branch_name, Unset):
        json_from_branch_name = UNSET
    else:
        json_from_branch_name = from_branch_name
    params["fromBranchName"] = json_from_branch_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/gitRepositories/{repository_id}/git/branches/{new_branch_name}".format(
            project_id=quote(str(project_id), safe=""),
            repository_id=quote(str(repository_id), safe=""),
            new_branch_name=quote(str(new_branch_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    repository_id: str,
    new_branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    from_branch_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse]:
    """Creates a new branch on the repository

    Args:
        project_id (str):
        repository_id (str):
        new_branch_name (str):
        from_branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        new_branch_name=new_branch_name,
        from_branch_name=from_branch_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    repository_id: str,
    new_branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    from_branch_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse | None:
    """Creates a new branch on the repository

    Args:
        project_id (str):
        repository_id (str):
        new_branch_name (str):
        from_branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse
    """

    return sync_detailed(
        project_id=project_id,
        repository_id=repository_id,
        new_branch_name=new_branch_name,
        client=client,
        from_branch_name=from_branch_name,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    repository_id: str,
    new_branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    from_branch_name: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse]:
    """Creates a new branch on the repository

    Args:
        project_id (str):
        repository_id (str):
        new_branch_name (str):
        from_branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        repository_id=repository_id,
        new_branch_name=new_branch_name,
        from_branch_name=from_branch_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    repository_id: str,
    new_branch_name: str,
    *,
    client: AuthenticatedClient | Client,
    from_branch_name: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse | None:
    """Creates a new branch on the repository

    Args:
        project_id (str):
        repository_id (str):
        new_branch_name (str):
        from_branch_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiRepositoriesResponsesCreateBranchApiResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            repository_id=repository_id,
            new_branch_name=new_branch_name,
            client=client,
            from_branch_name=from_branch_name,
        )
    ).parsed
