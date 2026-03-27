from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.render_snippet_request import RenderSnippetRequest
from ...models.render_snippet_response import RenderSnippetResponse
from ...models.render_snippet_response_400 import RenderSnippetResponse400
from ...models.render_snippet_response_500 import RenderSnippetResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: RenderSnippetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/ppm/snippet",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500 | None:
    if response.status_code == 200:
        response_200 = RenderSnippetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RenderSnippetResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = RenderSnippetResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RenderSnippetRequest,
) -> Response[RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500]:
    """Render PPM Installation Snippet

     Generate a copyable Rscript command for PPM package installation with automatic biocVersion
    detection when needed

    Args:
        body (RenderSnippetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RenderSnippetRequest,
) -> RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500 | None:
    """Render PPM Installation Snippet

     Generate a copyable Rscript command for PPM package installation with automatic biocVersion
    detection when needed

    Args:
        body (RenderSnippetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RenderSnippetRequest,
) -> Response[RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500]:
    """Render PPM Installation Snippet

     Generate a copyable Rscript command for PPM package installation with automatic biocVersion
    detection when needed

    Args:
        body (RenderSnippetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RenderSnippetRequest,
) -> RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500 | None:
    """Render PPM Installation Snippet

     Generate a copyable Rscript command for PPM package installation with automatic biocVersion
    detection when needed

    Args:
        body (RenderSnippetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RenderSnippetResponse | RenderSnippetResponse400 | RenderSnippetResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
