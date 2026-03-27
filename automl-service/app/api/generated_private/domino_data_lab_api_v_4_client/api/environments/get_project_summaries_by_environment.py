from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_environment_project_usage_summaries_set import (
    DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet,
)
from ...types import Response


def _get_kwargs(
    environment_id: str,
    page_number: int,
    page_size: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environments/{environment_id}/projectUsageSummaries/page/{page_number}/pageSize/{page_size}".format(
            environment_id=quote(str(environment_id), safe=""),
            page_number=quote(str(page_number), safe=""),
            page_size=quote(str(page_size), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet | None:
    if response.status_code == 200:
        response_200 = DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    page_number: int,
    page_size: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet]:
    """Get project usage summaries for an environment

    Args:
        environment_id (str):
        page_number (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    page_number: int,
    page_size: int,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet | None:
    """Get project usage summaries for an environment

    Args:
        environment_id (str):
        page_number (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet
    """

    return sync_detailed(
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    page_number: int,
    page_size: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet]:
    """Get project usage summaries for an environment

    Args:
        environment_id (str):
        page_number (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    page_number: int,
    page_size: int,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet | None:
    """Get project usage summaries for an environment

    Args:
        environment_id (str):
        page_number (int):
        page_size (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiEnvironmentProjectUsageSummariesSet
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            page_number=page_number,
            page_size=page_size,
            client=client,
        )
    ).parsed
