from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_server_projects_api_project_gateway_summary import DominoServerProjectsApiProjectGatewaySummary
from ...models.list_relationship import ListRelationship
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    relationship: ListRelationship,
    show_completed: bool | Unset = True,
    limit: int | None | Unset = UNSET,
    include_searchable_and_public: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_relationship = relationship.value
    params["relationship"] = json_relationship

    params["showCompleted"] = show_completed

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params["includeSearchableAndPublic"] = include_searchable_and_public

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateway/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoServerProjectsApiProjectGatewaySummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

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
) -> Response[DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    relationship: ListRelationship,
    show_completed: bool | Unset = True,
    limit: int | None | Unset = UNSET,
    include_searchable_and_public: bool | Unset = False,
) -> Response[DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]]:
    """Retrieves projects for the Project List UI, ordered from most to least recently updated

    Args:
        relationship (ListRelationship):
        show_completed (bool | Unset):  Default: True.
        limit (int | None | Unset):
        include_searchable_and_public (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]]
    """

    kwargs = _get_kwargs(
        relationship=relationship,
        show_completed=show_completed,
        limit=limit,
        include_searchable_and_public=include_searchable_and_public,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    relationship: ListRelationship,
    show_completed: bool | Unset = True,
    limit: int | None | Unset = UNSET,
    include_searchable_and_public: bool | Unset = False,
) -> DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary] | None:
    """Retrieves projects for the Project List UI, ordered from most to least recently updated

    Args:
        relationship (ListRelationship):
        show_completed (bool | Unset):  Default: True.
        limit (int | None | Unset):
        include_searchable_and_public (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]
    """

    return sync_detailed(
        client=client,
        relationship=relationship,
        show_completed=show_completed,
        limit=limit,
        include_searchable_and_public=include_searchable_and_public,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    relationship: ListRelationship,
    show_completed: bool | Unset = True,
    limit: int | None | Unset = UNSET,
    include_searchable_and_public: bool | Unset = False,
) -> Response[DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]]:
    """Retrieves projects for the Project List UI, ordered from most to least recently updated

    Args:
        relationship (ListRelationship):
        show_completed (bool | Unset):  Default: True.
        limit (int | None | Unset):
        include_searchable_and_public (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]]
    """

    kwargs = _get_kwargs(
        relationship=relationship,
        show_completed=show_completed,
        limit=limit,
        include_searchable_and_public=include_searchable_and_public,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    relationship: ListRelationship,
    show_completed: bool | Unset = True,
    limit: int | None | Unset = UNSET,
    include_searchable_and_public: bool | Unset = False,
) -> DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary] | None:
    """Retrieves projects for the Project List UI, ordered from most to least recently updated

    Args:
        relationship (ListRelationship):
        show_completed (bool | Unset):  Default: True.
        limit (int | None | Unset):
        include_searchable_and_public (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoServerProjectsApiProjectGatewaySummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            relationship=relationship,
            show_completed=show_completed,
            limit=limit,
            include_searchable_and_public=include_searchable_and_public,
        )
    ).parsed
