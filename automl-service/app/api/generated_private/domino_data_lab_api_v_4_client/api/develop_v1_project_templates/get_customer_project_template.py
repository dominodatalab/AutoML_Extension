from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_projects_templates_api_models_customer_template_dto import (
    DominoProjectsTemplatesApiModelsCustomerTemplateDto,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include_archived: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeArchived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/develop/v1/customer-project-templates/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto | None:
    if response.status_code == 200:
        response_200 = DominoProjectsTemplatesApiModelsCustomerTemplateDto.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = False,
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto]:
    """Get a customer project template by id.

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto]
    """

    kwargs = _get_kwargs(
        id=id,
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = False,
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto | None:
    """Get a customer project template by id.

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto
    """

    return sync_detailed(
        id=id,
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = False,
) -> Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto]:
    """Get a customer project template by id.

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto]
    """

    kwargs = _get_kwargs(
        id=id,
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = False,
) -> DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto | None:
    """Get a customer project template by id.

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectsTemplatesApiModelsCustomerTemplateDto
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_archived=include_archived,
        )
    ).parsed
