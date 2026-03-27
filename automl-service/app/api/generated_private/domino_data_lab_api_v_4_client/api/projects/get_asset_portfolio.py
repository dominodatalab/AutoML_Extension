from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_asset_portfolio_set import DominoProjectsApiAssetPortfolioSet
from ...models.get_asset_portfolio_asset_type import GetAssetPortfolioAssetType
from ...models.get_asset_portfolio_sort_order import GetAssetPortfolioSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_type: GetAssetPortfolioAssetType,
    page_size: int | None | Unset = UNSET,
    sort_order: GetAssetPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_type = asset_type.value
    params["assetType"] = json_asset_type

    json_page_size: int | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_sort_by: None | str | Unset
    if isinstance(sort_by, Unset):
        json_sort_by = UNSET
    else:
        json_sort_by = sort_by
    params["sortBy"] = json_sort_by

    json_page_no: int | None | Unset
    if isinstance(page_no, Unset):
        json_page_no = UNSET
    else:
        json_page_no = page_no
    params["pageNo"] = json_page_no

    json_search_query: None | str | Unset
    if isinstance(search_query, Unset):
        json_search_query = UNSET
    else:
        json_search_query = search_query
    params["searchQuery"] = json_search_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/portfolio/getAssetPortfolio",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiAssetPortfolioSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetAssetPortfolioAssetType,
    page_size: int | None | Unset = UNSET,
    sort_order: GetAssetPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet]:
    """Get assets portfolio

    Args:
        asset_type (GetAssetPortfolioAssetType):
        page_size (int | None | Unset):
        sort_order (GetAssetPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetAssetPortfolioAssetType,
    page_size: int | None | Unset = UNSET,
    sort_order: GetAssetPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet | None:
    """Get assets portfolio

    Args:
        asset_type (GetAssetPortfolioAssetType):
        page_size (int | None | Unset):
        sort_order (GetAssetPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet
    """

    return sync_detailed(
        client=client,
        asset_type=asset_type,
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetAssetPortfolioAssetType,
    page_size: int | None | Unset = UNSET,
    sort_order: GetAssetPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet]:
    """Get assets portfolio

    Args:
        asset_type (GetAssetPortfolioAssetType):
        page_size (int | None | Unset):
        sort_order (GetAssetPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        page_size=page_size,
        sort_order=sort_order,
        sort_by=sort_by,
        page_no=page_no,
        search_query=search_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    asset_type: GetAssetPortfolioAssetType,
    page_size: int | None | Unset = UNSET,
    sort_order: GetAssetPortfolioSortOrder | Unset = UNSET,
    sort_by: None | str | Unset = UNSET,
    page_no: int | None | Unset = UNSET,
    search_query: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet | None:
    """Get assets portfolio

    Args:
        asset_type (GetAssetPortfolioAssetType):
        page_size (int | None | Unset):
        sort_order (GetAssetPortfolioSortOrder | Unset):
        sort_by (None | str | Unset):
        page_no (int | None | Unset):
        search_query (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiAssetPortfolioSet
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type=asset_type,
            page_size=page_size,
            sort_order=sort_order,
            sort_by=sort_by,
            page_no=page_no,
            search_query=search_query,
        )
    ).parsed
