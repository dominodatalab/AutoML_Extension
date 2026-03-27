from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_project_portfolio_stats import DominoProjectsApiProjectPortfolioStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include_pm_linked_projects: bool | None | Unset
    if isinstance(include_pm_linked_projects, Unset):
        json_include_pm_linked_projects = UNSET
    else:
        json_include_pm_linked_projects = include_pm_linked_projects
    params["includePmLinkedProjects"] = json_include_pm_linked_projects

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/portfolio/getProjectPortfolioStats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiProjectPortfolioStats.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats]:
    """Get project portfolio stats

    Args:
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats]
    """

    kwargs = _get_kwargs(
        include_pm_linked_projects=include_pm_linked_projects,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats | None:
    """Get project portfolio stats

    Args:
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats
    """

    return sync_detailed(
        client=client,
        include_pm_linked_projects=include_pm_linked_projects,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats]:
    """Get project portfolio stats

    Args:
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats]
    """

    kwargs = _get_kwargs(
        include_pm_linked_projects=include_pm_linked_projects,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_pm_linked_projects: bool | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats | None:
    """Get project portfolio stats

    Args:
        include_pm_linked_projects (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectPortfolioStats
    """

    return (
        await asyncio_detailed(
            client=client,
            include_pm_linked_projects=include_pm_linked_projects,
        )
    ).parsed
