from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_guardrails_interface_bundle_comment_thread_dto import (
    DominoGuardrailsInterfaceBundleCommentThreadDto,
)
from ...models.get_comment_threads_thread_status import GetCommentThreadsThreadStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bundle_id: str,
    thread_status: GetCommentThreadsThreadStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["bundleId"] = bundle_id

    json_thread_status: str | Unset = UNSET
    if not isinstance(thread_status, Unset):
        json_thread_status = thread_status.value

    params["threadStatus"] = json_thread_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/guardrails/comments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoGuardrailsInterfaceBundleCommentThreadDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bundle_id: str,
    thread_status: GetCommentThreadsThreadStatus | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]]:
    """get comments threads for a bundle

    Args:
        bundle_id (str):
        thread_status (GetCommentThreadsThreadStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        thread_status=thread_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bundle_id: str,
    thread_status: GetCommentThreadsThreadStatus | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto] | None:
    """get comments threads for a bundle

    Args:
        bundle_id (str):
        thread_status (GetCommentThreadsThreadStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]
    """

    return sync_detailed(
        client=client,
        bundle_id=bundle_id,
        thread_status=thread_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bundle_id: str,
    thread_status: GetCommentThreadsThreadStatus | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]]:
    """get comments threads for a bundle

    Args:
        bundle_id (str):
        thread_status (GetCommentThreadsThreadStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        thread_status=thread_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bundle_id: str,
    thread_status: GetCommentThreadsThreadStatus | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto] | None:
    """get comments threads for a bundle

    Args:
        bundle_id (str):
        thread_status (GetCommentThreadsThreadStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoGuardrailsInterfaceBundleCommentThreadDto]
    """

    return (
        await asyncio_detailed(
            client=client,
            bundle_id=bundle_id,
            thread_status=thread_status,
        )
    ).parsed
