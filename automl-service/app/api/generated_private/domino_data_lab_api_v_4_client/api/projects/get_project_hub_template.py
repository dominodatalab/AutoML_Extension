from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_api_project_hub_template_result import DominoProjectsApiProjectHubTemplateResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: str,
    *,
    revision_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_revision_id: None | str | Unset
    if isinstance(revision_id, Unset):
        json_revision_id = UNSET
    else:
        json_revision_id = revision_id
    params["revisionId"] = json_revision_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/templates/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiProjectHubTemplateResult.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult]:
    """Get a single project hub template for a deployment

    Args:
        template_id (str):
        revision_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        revision_id=revision_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult | None:
    """Get a single project hub template for a deployment

    Args:
        template_id (str):
        revision_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        revision_id=revision_id,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult]:
    """Get a single project hub template for a deployment

    Args:
        template_id (str):
        revision_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        revision_id=revision_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    revision_id: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult | None:
    """Get a single project hub template for a deployment

    Args:
        template_id (str):
        revision_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsApiProjectHubTemplateResult
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            revision_id=revision_id,
        )
    ).parsed
