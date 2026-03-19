from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer_template import CustomerTemplate
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_customer_project_template_response_400 import UpdateCustomerProjectTemplateResponse400
from ...models.update_customer_project_template_response_404 import UpdateCustomerProjectTemplateResponse404
from ...models.update_customer_project_template_response_500 import UpdateCustomerProjectTemplateResponse500
from ...models.update_customer_template import UpdateCustomerTemplate
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateCustomerTemplate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/develop/v1/customer-project-templates/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
    | None
):
    if response.status_code == 200:
        response_200 = CustomerTemplate.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateCustomerProjectTemplateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateCustomerProjectTemplateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateCustomerProjectTemplateResponse500.from_dict(response.json())

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
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
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
    body: UpdateCustomerTemplate,
) -> Response[
    CustomerTemplate
    | FailureEnvelopeV1
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
]:
    """Update a customer project template

    Args:
        id (str):
        body (UpdateCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerTemplate | FailureEnvelopeV1 | UpdateCustomerProjectTemplateResponse400 | UpdateCustomerProjectTemplateResponse404 | UpdateCustomerProjectTemplateResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCustomerTemplate,
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
    | None
):
    """Update a customer project template

    Args:
        id (str):
        body (UpdateCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerTemplate | FailureEnvelopeV1 | UpdateCustomerProjectTemplateResponse400 | UpdateCustomerProjectTemplateResponse404 | UpdateCustomerProjectTemplateResponse500
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCustomerTemplate,
) -> Response[
    CustomerTemplate
    | FailureEnvelopeV1
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
]:
    """Update a customer project template

    Args:
        id (str):
        body (UpdateCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomerTemplate | FailureEnvelopeV1 | UpdateCustomerProjectTemplateResponse400 | UpdateCustomerProjectTemplateResponse404 | UpdateCustomerProjectTemplateResponse500]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCustomerTemplate,
) -> (
    CustomerTemplate
    | FailureEnvelopeV1
    | UpdateCustomerProjectTemplateResponse400
    | UpdateCustomerProjectTemplateResponse404
    | UpdateCustomerProjectTemplateResponse500
    | None
):
    """Update a customer project template

    Args:
        id (str):
        body (UpdateCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomerTemplate | FailureEnvelopeV1 | UpdateCustomerProjectTemplateResponse400 | UpdateCustomerProjectTemplateResponse404 | UpdateCustomerProjectTemplateResponse500
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
