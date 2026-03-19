from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_template import CustomerTemplate
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_customer_project_template_response_400 import GetCustomerProjectTemplateResponse400
from ...models.get_customer_project_template_response_404 import GetCustomerProjectTemplateResponse404
from ...models.get_customer_project_template_response_500 import GetCustomerProjectTemplateResponse500
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
        "url": "/api/develop/v1/customer-project-templates/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
    | None
):
    if response.status_code == 200:
        response_200 = CustomerTemplate.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCustomerProjectTemplateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCustomerProjectTemplateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetCustomerProjectTemplateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
]:
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
) -> Response[
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
]:
    """Get customer project template by id

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerTemplate | FailureEnvelopeV1 | GetCustomerProjectTemplateResponse400 | GetCustomerProjectTemplateResponse404 | GetCustomerProjectTemplateResponse500]
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
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
    | None
):
    """Get customer project template by id

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerTemplate | FailureEnvelopeV1 | GetCustomerProjectTemplateResponse400 | GetCustomerProjectTemplateResponse404 | GetCustomerProjectTemplateResponse500
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
) -> Response[
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
]:
    """Get customer project template by id

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerTemplate | FailureEnvelopeV1 | GetCustomerProjectTemplateResponse400 | GetCustomerProjectTemplateResponse404 | GetCustomerProjectTemplateResponse500]
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
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | GetCustomerProjectTemplateResponse400
    | GetCustomerProjectTemplateResponse404
    | GetCustomerProjectTemplateResponse500
    | None
):
    """Get customer project template by id

    Args:
        id (str):
        include_archived (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerTemplate | FailureEnvelopeV1 | GetCustomerProjectTemplateResponse400 | GetCustomerProjectTemplateResponse404 | GetCustomerProjectTemplateResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_archived=include_archived,
        )
    ).parsed
