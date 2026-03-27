from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_templates_api_models_base_templates_collection_dto import (
    DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto,
)
from ...models.get_project_templates_collection_order_by import GetProjectTemplatesCollectionOrderBy
from ...models.get_project_templates_collection_sort_order import GetProjectTemplatesCollectionSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    size: int | Unset = 10,
    hub: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    is_company_official: bool | None | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: None | str | Unset = "",
    custom_template_tag_id: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    json_hub: None | str | Unset
    if isinstance(hub, Unset):
        json_hub = UNSET
    else:
        json_hub = hub
    params["hub"] = json_hub

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_is_company_official: bool | None | Unset
    if isinstance(is_company_official, Unset):
        json_is_company_official = UNSET
    else:
        json_is_company_official = is_company_official
    params["isCompanyOfficial"] = json_is_company_official

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params["customTemplateTagId"] = custom_template_tag_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/develop/v1/project-templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto | None:
    if response.status_code == 200:
        response_200 = DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    hub: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    is_company_official: bool | None | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: None | str | Unset = "",
    custom_template_tag_id: str | Unset = "",
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto]:
    """Get the collection of project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        hub (None | str | Unset):
        category (None | str | Unset):
        owner (None | str | Unset):
        is_company_official (bool | None | Unset):
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (None | str | Unset):  Default: ''.
        custom_template_tag_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        hub=hub,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        custom_template_tag_id=custom_template_tag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    hub: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    is_company_official: bool | None | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: None | str | Unset = "",
    custom_template_tag_id: str | Unset = "",
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto | None:
    """Get the collection of project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        hub (None | str | Unset):
        category (None | str | Unset):
        owner (None | str | Unset):
        is_company_official (bool | None | Unset):
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (None | str | Unset):  Default: ''.
        custom_template_tag_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        hub=hub,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        custom_template_tag_id=custom_template_tag_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    hub: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    is_company_official: bool | None | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: None | str | Unset = "",
    custom_template_tag_id: str | Unset = "",
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto]:
    """Get the collection of project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        hub (None | str | Unset):
        category (None | str | Unset):
        owner (None | str | Unset):
        is_company_official (bool | None | Unset):
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (None | str | Unset):  Default: ''.
        custom_template_tag_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        hub=hub,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        custom_template_tag_id=custom_template_tag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    hub: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    is_company_official: bool | None | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: None | str | Unset = "",
    custom_template_tag_id: str | Unset = "",
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto | None:
    """Get the collection of project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        hub (None | str | Unset):
        category (None | str | Unset):
        owner (None | str | Unset):
        is_company_official (bool | None | Unset):
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (None | str | Unset):  Default: ''.
        custom_template_tag_id (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsTemplatesApiModelsBaseTemplatesCollectionDto
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            hub=hub,
            category=category,
            owner=owner,
            is_company_official=is_company_official,
            order_by=order_by,
            sort_order=sort_order,
            q=q,
            custom_template_tag_id=custom_template_tag_id,
        )
    ).parsed
