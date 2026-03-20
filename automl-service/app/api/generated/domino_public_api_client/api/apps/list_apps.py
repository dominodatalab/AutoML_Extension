from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.list_apps_response import ListAppsResponse
from ...models.list_apps_response_400 import ListAppsResponse400
from ...models.list_apps_response_404 import ListAppsResponse404
from ...models.list_apps_response_500 import ListAppsResponse500
from ...models.list_apps_sort_field import ListAppsSortField
from ...models.list_apps_sort_order import ListAppsSortOrder
from ...models.list_apps_status import ListAppsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    include_template_apps: bool | Unset = False,
    sort_field: ListAppsSortField | Unset = ListAppsSortField.LASTVIEWED,
    sort_order: ListAppsSortOrder | Unset = ListAppsSortOrder.ASC,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,
    owner_id: str | Unset = UNSET,
    status: ListAppsStatus | Unset = UNSET,
    publisher_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["name"] = name

    params["includeTemplateApps"] = include_template_apps

    json_sort_field: str | Unset = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sortField"] = json_sort_field

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["limit"] = limit

    params["offset"] = offset

    params["ownerId"] = owner_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["publisherId"] = publisher_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500 | None:
    if response.status_code == 200:
        response_200 = ListAppsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ListAppsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ListAppsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ListAppsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    include_template_apps: bool | Unset = False,
    sort_field: ListAppsSortField | Unset = ListAppsSortField.LASTVIEWED,
    sort_order: ListAppsSortOrder | Unset = ListAppsSortOrder.ASC,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,
    owner_id: str | Unset = UNSET,
    status: ListAppsStatus | Unset = UNSET,
    publisher_id: str | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500]:
    """List Apps

     List all Apps

    Args:
        project_id (str | Unset):
        name (str | Unset):
        include_template_apps (bool | Unset):  Default: False.
        sort_field (ListAppsSortField | Unset):  Default: ListAppsSortField.LASTVIEWED.
        sort_order (ListAppsSortOrder | Unset):  Default: ListAppsSortOrder.ASC.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.
        owner_id (str | Unset):
        status (ListAppsStatus | Unset):
        publisher_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        name=name,
        include_template_apps=include_template_apps,
        sort_field=sort_field,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
        owner_id=owner_id,
        status=status,
        publisher_id=publisher_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    include_template_apps: bool | Unset = False,
    sort_field: ListAppsSortField | Unset = ListAppsSortField.LASTVIEWED,
    sort_order: ListAppsSortOrder | Unset = ListAppsSortOrder.ASC,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,
    owner_id: str | Unset = UNSET,
    status: ListAppsStatus | Unset = UNSET,
    publisher_id: str | Unset = UNSET,
) -> FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500 | None:
    """List Apps

     List all Apps

    Args:
        project_id (str | Unset):
        name (str | Unset):
        include_template_apps (bool | Unset):  Default: False.
        sort_field (ListAppsSortField | Unset):  Default: ListAppsSortField.LASTVIEWED.
        sort_order (ListAppsSortOrder | Unset):  Default: ListAppsSortOrder.ASC.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.
        owner_id (str | Unset):
        status (ListAppsStatus | Unset):
        publisher_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        name=name,
        include_template_apps=include_template_apps,
        sort_field=sort_field,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
        owner_id=owner_id,
        status=status,
        publisher_id=publisher_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    include_template_apps: bool | Unset = False,
    sort_field: ListAppsSortField | Unset = ListAppsSortField.LASTVIEWED,
    sort_order: ListAppsSortOrder | Unset = ListAppsSortOrder.ASC,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,
    owner_id: str | Unset = UNSET,
    status: ListAppsStatus | Unset = UNSET,
    publisher_id: str | Unset = UNSET,
) -> Response[FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500]:
    """List Apps

     List all Apps

    Args:
        project_id (str | Unset):
        name (str | Unset):
        include_template_apps (bool | Unset):  Default: False.
        sort_field (ListAppsSortField | Unset):  Default: ListAppsSortField.LASTVIEWED.
        sort_order (ListAppsSortOrder | Unset):  Default: ListAppsSortOrder.ASC.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.
        owner_id (str | Unset):
        status (ListAppsStatus | Unset):
        publisher_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        name=name,
        include_template_apps=include_template_apps,
        sort_field=sort_field,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
        owner_id=owner_id,
        status=status,
        publisher_id=publisher_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    include_template_apps: bool | Unset = False,
    sort_field: ListAppsSortField | Unset = ListAppsSortField.LASTVIEWED,
    sort_order: ListAppsSortOrder | Unset = ListAppsSortOrder.ASC,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,
    owner_id: str | Unset = UNSET,
    status: ListAppsStatus | Unset = UNSET,
    publisher_id: str | Unset = UNSET,
) -> FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500 | None:
    """List Apps

     List all Apps

    Args:
        project_id (str | Unset):
        name (str | Unset):
        include_template_apps (bool | Unset):  Default: False.
        sort_field (ListAppsSortField | Unset):  Default: ListAppsSortField.LASTVIEWED.
        sort_order (ListAppsSortOrder | Unset):  Default: ListAppsSortOrder.ASC.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.
        owner_id (str | Unset):
        status (ListAppsStatus | Unset):
        publisher_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ListAppsResponse | ListAppsResponse400 | ListAppsResponse404 | ListAppsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            name=name,
            include_template_apps=include_template_apps,
            sort_field=sort_field,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            owner_id=owner_id,
            status=status,
            publisher_id=publisher_id,
        )
    ).parsed
