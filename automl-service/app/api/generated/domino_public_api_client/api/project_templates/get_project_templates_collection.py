from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_project_templates_collection_order_by import GetProjectTemplatesCollectionOrderBy
from ...models.get_project_templates_collection_response_400 import GetProjectTemplatesCollectionResponse400
from ...models.get_project_templates_collection_response_404 import GetProjectTemplatesCollectionResponse404
from ...models.get_project_templates_collection_response_500 import GetProjectTemplatesCollectionResponse500
from ...models.get_project_templates_collection_sort_order import GetProjectTemplatesCollectionSortOrder
from ...models.paginated_base_templates_collection_v1 import PaginatedBaseTemplatesCollectionV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    size: int | Unset = 10,
    view: str | Unset = UNSET,
    category: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    is_company_official: bool | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: str | Unset = "",
    tag_name: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["size"] = size

    params["view"] = view

    params["category"] = category

    params["owner"] = owner

    params["isCompanyOfficial"] = is_company_official

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["q"] = q

    params["tagName"] = tag_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/develop/v1/project-templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedBaseTemplatesCollectionV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectTemplatesCollectionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProjectTemplatesCollectionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetProjectTemplatesCollectionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
]:
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
    view: str | Unset = UNSET,
    category: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    is_company_official: bool | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: str | Unset = "",
    tag_name: str | Unset = "",
) -> Response[
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
]:
    """List project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        view (str | Unset):
        category (str | Unset):
        owner (str | Unset):
        is_company_official (bool | Unset): To filter on company official templates.
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (str | Unset):  Default: ''.
        tag_name (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectTemplatesCollectionResponse400 | GetProjectTemplatesCollectionResponse404 | GetProjectTemplatesCollectionResponse500 | PaginatedBaseTemplatesCollectionV1]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        view=view,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        tag_name=tag_name,
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
    view: str | Unset = UNSET,
    category: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    is_company_official: bool | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: str | Unset = "",
    tag_name: str | Unset = "",
) -> (
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
    | None
):
    """List project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        view (str | Unset):
        category (str | Unset):
        owner (str | Unset):
        is_company_official (bool | Unset): To filter on company official templates.
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (str | Unset):  Default: ''.
        tag_name (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectTemplatesCollectionResponse400 | GetProjectTemplatesCollectionResponse404 | GetProjectTemplatesCollectionResponse500 | PaginatedBaseTemplatesCollectionV1
    """

    return sync_detailed(
        client=client,
        page=page,
        size=size,
        view=view,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        tag_name=tag_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    view: str | Unset = UNSET,
    category: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    is_company_official: bool | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: str | Unset = "",
    tag_name: str | Unset = "",
) -> Response[
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
]:
    """List project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        view (str | Unset):
        category (str | Unset):
        owner (str | Unset):
        is_company_official (bool | Unset): To filter on company official templates.
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (str | Unset):  Default: ''.
        tag_name (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectTemplatesCollectionResponse400 | GetProjectTemplatesCollectionResponse404 | GetProjectTemplatesCollectionResponse500 | PaginatedBaseTemplatesCollectionV1]
    """

    kwargs = _get_kwargs(
        page=page,
        size=size,
        view=view,
        category=category,
        owner=owner,
        is_company_official=is_company_official,
        order_by=order_by,
        sort_order=sort_order,
        q=q,
        tag_name=tag_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    size: int | Unset = 10,
    view: str | Unset = UNSET,
    category: str | Unset = UNSET,
    owner: str | Unset = UNSET,
    is_company_official: bool | Unset = UNSET,
    order_by: GetProjectTemplatesCollectionOrderBy | Unset = GetProjectTemplatesCollectionOrderBy.UPDATED,
    sort_order: GetProjectTemplatesCollectionSortOrder | Unset = GetProjectTemplatesCollectionSortOrder.DESC,
    q: str | Unset = "",
    tag_name: str | Unset = "",
) -> (
    FailureEnvelopeV1
    | GetProjectTemplatesCollectionResponse400
    | GetProjectTemplatesCollectionResponse404
    | GetProjectTemplatesCollectionResponse500
    | PaginatedBaseTemplatesCollectionV1
    | None
):
    """List project templates

    Args:
        page (int | Unset):  Default: 1.
        size (int | Unset):  Default: 10.
        view (str | Unset):
        category (str | Unset):
        owner (str | Unset):
        is_company_official (bool | Unset): To filter on company official templates.
        order_by (GetProjectTemplatesCollectionOrderBy | Unset):  Default:
            GetProjectTemplatesCollectionOrderBy.UPDATED.
        sort_order (GetProjectTemplatesCollectionSortOrder | Unset):  Default:
            GetProjectTemplatesCollectionSortOrder.DESC.
        q (str | Unset):  Default: ''.
        tag_name (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectTemplatesCollectionResponse400 | GetProjectTemplatesCollectionResponse404 | GetProjectTemplatesCollectionResponse500 | PaginatedBaseTemplatesCollectionV1
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            size=size,
            view=view,
            category=category,
            owner=owner,
            is_company_official=is_company_official,
            order_by=order_by,
            sort_order=sort_order,
            q=q,
            tag_name=tag_name,
        )
    ).parsed
