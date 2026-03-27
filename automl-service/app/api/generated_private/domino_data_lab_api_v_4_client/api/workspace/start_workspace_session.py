from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_workspace_api_workspace_session_dto import DominoWorkspaceApiWorkspaceSessionDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    workspace_id: str,
    *,
    external_volume_mounts: list[str],
    net_app_volume_ids: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_external_volume_mounts = external_volume_mounts

    params["externalVolumeMounts"] = json_external_volume_mounts

    json_net_app_volume_ids: list[str] | None | Unset
    if isinstance(net_app_volume_ids, Unset):
        json_net_app_volume_ids = UNSET
    elif isinstance(net_app_volume_ids, list):
        json_net_app_volume_ids = net_app_volume_ids

    else:
        json_net_app_volume_ids = net_app_volume_ids
    params["netAppVolumeIds"] = json_net_app_volume_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspace/project/{project_id}/workspace/{workspace_id}/sessions".format(
            project_id=quote(str(project_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto | None:
    if response.status_code == 200:
        response_200 = DominoWorkspaceApiWorkspaceSessionDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    external_volume_mounts: list[str],
    net_app_volume_ids: list[str] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto]:
    """Start workspace session

    Args:
        project_id (str):
        workspace_id (str):
        external_volume_mounts (list[str]):
        net_app_volume_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        external_volume_mounts=external_volume_mounts,
        net_app_volume_ids=net_app_volume_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    external_volume_mounts: list[str],
    net_app_volume_ids: list[str] | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto | None:
    """Start workspace session

    Args:
        project_id (str):
        workspace_id (str):
        external_volume_mounts (list[str]):
        net_app_volume_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto
    """

    return sync_detailed(
        project_id=project_id,
        workspace_id=workspace_id,
        client=client,
        external_volume_mounts=external_volume_mounts,
        net_app_volume_ids=net_app_volume_ids,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    external_volume_mounts: list[str],
    net_app_volume_ids: list[str] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto]:
    """Start workspace session

    Args:
        project_id (str):
        workspace_id (str):
        external_volume_mounts (list[str]):
        net_app_volume_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        workspace_id=workspace_id,
        external_volume_mounts=external_volume_mounts,
        net_app_volume_ids=net_app_volume_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    external_volume_mounts: list[str],
    net_app_volume_ids: list[str] | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto | None:
    """Start workspace session

    Args:
        project_id (str):
        workspace_id (str):
        external_volume_mounts (list[str]):
        net_app_volume_ids (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoWorkspaceApiWorkspaceSessionDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            workspace_id=workspace_id,
            client=client,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_ids=net_app_volume_ids,
        )
    ).parsed
