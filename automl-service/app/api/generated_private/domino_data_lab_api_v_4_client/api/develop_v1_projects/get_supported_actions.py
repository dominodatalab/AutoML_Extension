from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_supported_actions_response import DominoProjectsApiSupportedActionsResponse
from ...models.get_supported_actions_q_type_0_item import GetSupportedActionsQType0Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    q: list[GetSupportedActionsQType0Item] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: list[str] | None | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    elif isinstance(q, list):
        json_q = []
        for q_type_0_item_data in q:
            q_type_0_item = q_type_0_item_data.value
            json_q.append(q_type_0_item)

    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/develop/v1/projects/{project_id}/supported-actions".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiSupportedActionsResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse]:
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
    q: list[GetSupportedActionsQType0Item] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse]:
    """Get copy support status for this project

    Args:
        project_id (str):
        q (list[GetSupportedActionsQType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: list[GetSupportedActionsQType0Item] | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse | None:
    """Get copy support status for this project

    Args:
        project_id (str):
        q (list[GetSupportedActionsQType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        q=q,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: list[GetSupportedActionsQType0Item] | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse]:
    """Get copy support status for this project

    Args:
        project_id (str):
        q (list[GetSupportedActionsQType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: list[GetSupportedActionsQType0Item] | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse | None:
    """Get copy support status for this project

    Args:
        project_id (str):
        q (list[GetSupportedActionsQType0Item] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiSupportedActionsResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            q=q,
        )
    ).parsed
