from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_project_models_fork_or_copy_project import DominoNucleusProjectModelsForkOrCopyProject
from ...models.domino_nucleus_project_models_project import DominoNucleusProjectModelsProject
from ...types import Response


def _get_kwargs(
    project_to_copy_id: str,
    *,
    body: DominoNucleusProjectModelsForkOrCopyProject,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_to_copy_id}/copy".format(
            project_to_copy_id=quote(str(project_to_copy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusProjectModelsProject | None:
    if response.status_code == 200:
        response_200 = DominoNucleusProjectModelsProject.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoNucleusProjectModelsProject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_to_copy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoNucleusProjectModelsForkOrCopyProject,
) -> Response[DominoApiErrorResponse | DominoNucleusProjectModelsProject]:
    """copies a project

    Args:
        project_to_copy_id (str):
        body (DominoNucleusProjectModelsForkOrCopyProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusProjectModelsProject]
    """

    kwargs = _get_kwargs(
        project_to_copy_id=project_to_copy_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_to_copy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoNucleusProjectModelsForkOrCopyProject,
) -> DominoApiErrorResponse | DominoNucleusProjectModelsProject | None:
    """copies a project

    Args:
        project_to_copy_id (str):
        body (DominoNucleusProjectModelsForkOrCopyProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusProjectModelsProject
    """

    return sync_detailed(
        project_to_copy_id=project_to_copy_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_to_copy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoNucleusProjectModelsForkOrCopyProject,
) -> Response[DominoApiErrorResponse | DominoNucleusProjectModelsProject]:
    """copies a project

    Args:
        project_to_copy_id (str):
        body (DominoNucleusProjectModelsForkOrCopyProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusProjectModelsProject]
    """

    kwargs = _get_kwargs(
        project_to_copy_id=project_to_copy_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_to_copy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoNucleusProjectModelsForkOrCopyProject,
) -> DominoApiErrorResponse | DominoNucleusProjectModelsProject | None:
    """copies a project

    Args:
        project_to_copy_id (str):
        body (DominoNucleusProjectModelsForkOrCopyProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusProjectModelsProject
    """

    return (
        await asyncio_detailed(
            project_to_copy_id=project_to_copy_id,
            client=client,
            body=body,
        )
    ).parsed
