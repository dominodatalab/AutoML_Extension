from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_paginated_list import ModelApiPaginatedList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    environment_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["environmentId"] = environment_id

    params["projectId"] = project_id

    params["name"] = name

    params["registeredModelName"] = registered_model_name

    params["registeredModelVersion"] = registered_model_version

    params["limit"] = limit

    params["offset"] = offset

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelApis",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ModelApiPaginatedList | None:
    if response.status_code == 200:
        response_200 = ModelApiPaginatedList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ModelApiPaginatedList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[ModelApiPaginatedList]:
    """Lists Model APIs based on the query filters. Returns only Model APIs visible to the requesting user.

    Args:
        environment_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiPaginatedList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        project_id=project_id,
        name=name,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> ModelApiPaginatedList | None:
    """Lists Model APIs based on the query filters. Returns only Model APIs visible to the requesting user.

    Args:
        environment_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiPaginatedList
    """

    return sync_detailed(
        client=client,
        environment_id=environment_id,
        project_id=project_id,
        name=name,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[ModelApiPaginatedList]:
    """Lists Model APIs based on the query filters. Returns only Model APIs visible to the requesting user.

    Args:
        environment_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiPaginatedList]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        project_id=project_id,
        name=name,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    environment_id: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
    registered_model_version: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> ModelApiPaginatedList | None:
    """Lists Model APIs based on the query filters. Returns only Model APIs visible to the requesting user.

    Args:
        environment_id (str | Unset):
        project_id (str | Unset):
        name (str | Unset):
        registered_model_name (str | Unset):
        registered_model_version (int | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiPaginatedList
    """

    return (
        await asyncio_detailed(
            client=client,
            environment_id=environment_id,
            project_id=project_id,
            name=name,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
