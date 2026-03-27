from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_guardrails_interface_bundle_comment_thread_dto import (
    DominoGuardrailsInterfaceBundleCommentThreadDto,
)
from ...types import Response


def _get_kwargs(
    bundle_id: str,
    artifact_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/comments/bundle/{bundle_id}/artifact/{artifact_id}".format(
            bundle_id=quote(str(bundle_id), safe=""),
            artifact_id=quote(str(artifact_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto | None:
    if response.status_code == 200:
        response_200 = DominoGuardrailsInterfaceBundleCommentThreadDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bundle_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto]:
    """Get a comment thread by bundle ID and artifact ID

    Args:
        bundle_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        artifact_id=artifact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto | None:
    """Get a comment thread by bundle ID and artifact ID

    Args:
        bundle_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto
    """

    return sync_detailed(
        bundle_id=bundle_id,
        artifact_id=artifact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bundle_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto]:
    """Get a comment thread by bundle ID and artifact ID

    Args:
        bundle_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        artifact_id=artifact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_id: str,
    artifact_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto | None:
    """Get a comment thread by bundle ID and artifact ID

    Args:
        bundle_id (str):
        artifact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoGuardrailsInterfaceBundleCommentThreadDto
    """

    return (
        await asyncio_detailed(
            bundle_id=bundle_id,
            artifact_id=artifact_id,
            client=client,
        )
    ).parsed
