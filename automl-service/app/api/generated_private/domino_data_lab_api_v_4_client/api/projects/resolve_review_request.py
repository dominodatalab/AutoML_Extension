from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_resolve_review_request import DominoProjectsApiResolveReviewRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    review_request_number: int,
    *,
    body: DominoProjectsApiResolveReviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/projects/{project_id}/resolveRequest/{review_request_number}".format(
            project_id=quote(str(project_id), safe=""),
            review_request_number=quote(str(review_request_number), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DominoApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    review_request_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiResolveReviewRequest,
) -> Response[Any | DominoApiErrorResponse]:
    """Resolve a project review request

    Args:
        project_id (str):
        review_request_number (int):
        body (DominoProjectsApiResolveReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        review_request_number=review_request_number,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    review_request_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiResolveReviewRequest,
) -> Any | DominoApiErrorResponse | None:
    """Resolve a project review request

    Args:
        project_id (str):
        review_request_number (int):
        body (DominoProjectsApiResolveReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        project_id=project_id,
        review_request_number=review_request_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    review_request_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiResolveReviewRequest,
) -> Response[Any | DominoApiErrorResponse]:
    """Resolve a project review request

    Args:
        project_id (str):
        review_request_number (int):
        body (DominoProjectsApiResolveReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        review_request_number=review_request_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    review_request_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: DominoProjectsApiResolveReviewRequest,
) -> Any | DominoApiErrorResponse | None:
    """Resolve a project review request

    Args:
        project_id (str):
        review_request_number (int):
        body (DominoProjectsApiResolveReviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            review_request_number=review_request_number,
            client=client,
            body=body,
        )
    ).parsed
