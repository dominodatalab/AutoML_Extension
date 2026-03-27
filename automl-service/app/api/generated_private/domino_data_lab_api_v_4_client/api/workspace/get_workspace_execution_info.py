from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_execution_info_dto import DominoWorkspaceApiWorkspaceExecutionInfoDto
from ...types import UNSET, Response


def _get_kwargs(
    execution_id: str,
    *,
    owner_name: str,
    project_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ownerName"] = owner_name

    params["projectName"] = project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspace/{execution_id}/getSessionByExecutionId".format(
            execution_id=quote(str(execution_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspaceExecutionInfoDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto]:
    """Get workspace execution info

    Args:
        execution_id (str):
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        owner_name=owner_name,
        project_name=project_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto | None:
    """Get workspace execution info

    Args:
        execution_id (str):
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto
    """

    return sync_detailed(
        execution_id=execution_id,
        client=client,
        owner_name=owner_name,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto]:
    """Get workspace execution info

    Args:
        execution_id (str):
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto]
    """

    kwargs = _get_kwargs(
        execution_id=execution_id,
        owner_name=owner_name,
        project_name=project_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    execution_id: str,
    *,
    client: AuthenticatedClient | Client,
    owner_name: str,
    project_name: str,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto | None:
    """Get workspace execution info

    Args:
        execution_id (str):
        owner_name (str):
        project_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceExecutionInfoDto
    """

    return (
        await asyncio_detailed(
            execution_id=execution_id,
            client=client,
            owner_name=owner_name,
            project_name=project_name,
        )
    ).parsed
