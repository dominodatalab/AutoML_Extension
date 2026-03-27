from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_project_summary import DominoProjectsApiProjectSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_email: str,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userEmail"] = user_email

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/actionableInsights/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiProjectSummary | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiProjectSummary.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_email: str,
    project_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectSummary]:
    """retrieves the project to be used for Actionable Insights for a Model API

    Args:
        user_email (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectSummary]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_email: str,
    project_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectSummary | None:
    """retrieves the project to be used for Actionable Insights for a Model API

    Args:
        user_email (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectSummary
    """

    return sync_detailed(
        client=client,
        user_email=user_email,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_email: str,
    project_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectSummary]:
    """retrieves the project to be used for Actionable Insights for a Model API

    Args:
        user_email (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectSummary]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_email: str,
    project_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectSummary | None:
    """retrieves the project to be used for Actionable Insights for a Model API

    Args:
        user_email (str):
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            user_email=user_email,
            project_id=project_id,
        )
    ).parsed
