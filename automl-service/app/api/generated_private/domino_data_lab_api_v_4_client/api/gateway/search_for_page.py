from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_gateway_search_search_page_gateway_dto import DominoCommonGatewaySearchSearchPageGatewayDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: None | str,
    area: None | str | Unset = UNSET,
    page: float | None | Unset = UNSET,
    timestamp_format: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_query: None | str
    json_query = query
    params["query"] = json_query

    json_area: None | str | Unset
    if isinstance(area, Unset):
        json_area = UNSET
    else:
        json_area = area
    params["area"] = json_area

    json_page: float | None | Unset
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    json_timestamp_format: None | str | Unset
    if isinstance(timestamp_format, Unset):
        json_timestamp_format = UNSET
    else:
        json_timestamp_format = timestamp_format
    params["timestampFormat"] = json_timestamp_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gateway/search-page",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO | None:
    if response.status_code == 200:
        response_200 = DominoCommonGatewaySearchSearchPageGatewayDTO.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: None | str,
    area: None | str | Unset = UNSET,
    page: float | None | Unset = UNSET,
    timestamp_format: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO]:
    """provides search results for search page. has the same functionality as /search but returns more
    details for the selected area

    Args:
        query (None | str):
        area (None | str | Unset):
        page (float | None | Unset):
        timestamp_format (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO]
    """

    kwargs = _get_kwargs(
        query=query,
        area=area,
        page=page,
        timestamp_format=timestamp_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: None | str,
    area: None | str | Unset = UNSET,
    page: float | None | Unset = UNSET,
    timestamp_format: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO | None:
    """provides search results for search page. has the same functionality as /search but returns more
    details for the selected area

    Args:
        query (None | str):
        area (None | str | Unset):
        page (float | None | Unset):
        timestamp_format (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO
    """

    return sync_detailed(
        client=client,
        query=query,
        area=area,
        page=page,
        timestamp_format=timestamp_format,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: None | str,
    area: None | str | Unset = UNSET,
    page: float | None | Unset = UNSET,
    timestamp_format: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO]:
    """provides search results for search page. has the same functionality as /search but returns more
    details for the selected area

    Args:
        query (None | str):
        area (None | str | Unset):
        page (float | None | Unset):
        timestamp_format (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO]
    """

    kwargs = _get_kwargs(
        query=query,
        area=area,
        page=page,
        timestamp_format=timestamp_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: None | str,
    area: None | str | Unset = UNSET,
    page: float | None | Unset = UNSET,
    timestamp_format: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO | None:
    """provides search results for search page. has the same functionality as /search but returns more
    details for the selected area

    Args:
        query (None | str):
        area (None | str | Unset):
        page (float | None | Unset):
        timestamp_format (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoCommonGatewaySearchSearchPageGatewayDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            area=area,
            page=page,
            timestamp_format=timestamp_format,
        )
    ).parsed
