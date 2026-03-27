from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_environments_api_revision_overview import DominoEnvironmentsApiRevisionOverview
from ...types import Response


def _get_kwargs(
    environment_id: str,
    environment_revision_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/environments/{environment_id}/environmentRevision/{environment_revision_id}".format(
            environment_id=quote(str(environment_id), safe=""),
            environment_revision_id=quote(str(environment_revision_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview | None:
    if response.status_code == 200:
        response_200 = DominoEnvironmentsApiRevisionOverview.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    environment_revision_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview]:
    """Get an environment revision's overview

    Args:
        environment_id (str):
        environment_revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        environment_revision_id=environment_revision_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    environment_revision_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview | None:
    """Get an environment revision's overview

    Args:
        environment_id (str):
        environment_revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview
    """

    return sync_detailed(
        environment_id=environment_id,
        environment_revision_id=environment_revision_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    environment_revision_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview]:
    """Get an environment revision's overview

    Args:
        environment_id (str):
        environment_revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview]
    """

    kwargs = _get_kwargs(
        environment_id=environment_id,
        environment_revision_id=environment_revision_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    environment_revision_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview | None:
    """Get an environment revision's overview

    Args:
        environment_id (str):
        environment_revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoEnvironmentsApiRevisionOverview
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            environment_revision_id=environment_revision_id,
            client=client,
        )
    ).parsed
