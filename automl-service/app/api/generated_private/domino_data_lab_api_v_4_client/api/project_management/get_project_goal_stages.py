from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_project_stage import DominoProjectsApiProjectStage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    include_archived: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_archived: bool | None | Unset
    if isinstance(include_archived, Unset):
        json_include_archived = UNSET
    else:
        json_include_archived = include_archived
    params["includeArchived"] = json_include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projectManagement/{project_id}/projectGoalStages".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoProjectsApiProjectStage] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoProjectsApiProjectStage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[DominoApiErrorResponse | list[DominoProjectsApiProjectStage]]:
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
    include_archived: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoProjectsApiProjectStage]]:
    """Get all project goal stages on a project.

    Args:
        project_id (str):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoProjectsApiProjectStage]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoProjectsApiProjectStage] | None:
    """Get all project goal stages on a project.

    Args:
        project_id (str):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoProjectsApiProjectStage]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoProjectsApiProjectStage]]:
    """Get all project goal stages on a project.

    Args:
        project_id (str):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoProjectsApiProjectStage]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoProjectsApiProjectStage] | None:
    """Get all project goal stages on a project.

    Args:
        project_id (str):
        include_archived (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoProjectsApiProjectStage]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            include_archived=include_archived,
        )
    ).parsed
