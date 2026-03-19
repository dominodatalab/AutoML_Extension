from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_template_response_400 import CreateProjectTemplateResponse400
from ...models.create_project_template_response_404 import CreateProjectTemplateResponse404
from ...models.create_project_template_response_500 import CreateProjectTemplateResponse500
from ...models.customer_template import CustomerTemplate
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_customer_template import NewCustomerTemplate
from ...types import Response


def _get_kwargs(
    *,
    body: NewCustomerTemplate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/develop/v1/customer-project-templates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = CustomerTemplate.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateProjectTemplateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProjectTemplateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateProjectTemplateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewCustomerTemplate,
) -> Response[
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
]:
    """Create project template

    Args:
        body (NewCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectTemplateResponse400 | CreateProjectTemplateResponse404 | CreateProjectTemplateResponse500 | CustomerTemplate | FailureEnvelopeV1]
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
    body: NewCustomerTemplate,
) -> (
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
    | None
):
    """Create project template

    Args:
        body (NewCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectTemplateResponse400 | CreateProjectTemplateResponse404 | CreateProjectTemplateResponse500 | CustomerTemplate | FailureEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewCustomerTemplate,
) -> Response[
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
]:
    """Create project template

    Args:
        body (NewCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectTemplateResponse400 | CreateProjectTemplateResponse404 | CreateProjectTemplateResponse500 | CustomerTemplate | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewCustomerTemplate,
) -> (
    CreateProjectTemplateResponse400
    | CreateProjectTemplateResponse404
    | CreateProjectTemplateResponse500
    | CustomerTemplate
    | FailureEnvelopeV1
    | None
):
    """Create project template

    Args:
        body (NewCustomerTemplate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectTemplateResponse400 | CreateProjectTemplateResponse404 | CreateProjectTemplateResponse500 | CustomerTemplate | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
