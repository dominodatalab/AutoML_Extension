from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_org_response_400 import CreateOrgResponse400
from ...models.create_org_response_404 import CreateOrgResponse404
from ...models.create_org_response_500 import CreateOrgResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_organization_v1 import NewOrganizationV1
from ...models.organization_envelope_v1 import OrganizationEnvelopeV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewOrganizationV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/organizations/v1/organizations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateOrgResponse400
    | CreateOrgResponse404
    | CreateOrgResponse500
    | FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = OrganizationEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateOrgResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateOrgResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateOrgResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1
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
    body: NewOrganizationV1,
) -> Response[
    CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1
]:
    """Create an organization

     Create a new Organization. Required permissions: `Must be logged in user`

    Args:
        body (NewOrganizationV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1]
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
    body: NewOrganizationV1,
) -> (
    CreateOrgResponse400
    | CreateOrgResponse404
    | CreateOrgResponse500
    | FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | None
):
    """Create an organization

     Create a new Organization. Required permissions: `Must be logged in user`

    Args:
        body (NewOrganizationV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewOrganizationV1,
) -> Response[
    CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1
]:
    """Create an organization

     Create a new Organization. Required permissions: `Must be logged in user`

    Args:
        body (NewOrganizationV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewOrganizationV1,
) -> (
    CreateOrgResponse400
    | CreateOrgResponse404
    | CreateOrgResponse500
    | FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | None
):
    """Create an organization

     Create a new Organization. Required permissions: `Must be logged in user`

    Args:
        body (NewOrganizationV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateOrgResponse400 | CreateOrgResponse404 | CreateOrgResponse500 | FailureEnvelopeV1 | OrganizationEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
