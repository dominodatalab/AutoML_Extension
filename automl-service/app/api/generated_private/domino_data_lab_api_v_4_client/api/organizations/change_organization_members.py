from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_organizations_api_organization_members_dto import DominoOrganizationsApiOrganizationMembersDTO
from ...models.organization import Organization
from ...types import Response


def _get_kwargs(
    organization_user_id: str,
    *,
    body: DominoOrganizationsApiOrganizationMembersDTO,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/organizations/{organization_user_id}/members".format(
            organization_user_id=quote(str(organization_user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | Organization | None:
    if response.status_code == 200:
        response_200 = Organization.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | Organization]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoOrganizationsApiOrganizationMembersDTO,
) -> Response[DominoApiErrorResponse | Organization]:
    """add/remove members from an Organization

    Args:
        organization_user_id (str):
        body (DominoOrganizationsApiOrganizationMembersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | Organization]
    """

    kwargs = _get_kwargs(
        organization_user_id=organization_user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoOrganizationsApiOrganizationMembersDTO,
) -> DominoApiErrorResponse | Organization | None:
    """add/remove members from an Organization

    Args:
        organization_user_id (str):
        body (DominoOrganizationsApiOrganizationMembersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | Organization
    """

    return sync_detailed(
        organization_user_id=organization_user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoOrganizationsApiOrganizationMembersDTO,
) -> Response[DominoApiErrorResponse | Organization]:
    """add/remove members from an Organization

    Args:
        organization_user_id (str):
        body (DominoOrganizationsApiOrganizationMembersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | Organization]
    """

    kwargs = _get_kwargs(
        organization_user_id=organization_user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoOrganizationsApiOrganizationMembersDTO,
) -> DominoApiErrorResponse | Organization | None:
    """add/remove members from an Organization

    Args:
        organization_user_id (str):
        body (DominoOrganizationsApiOrganizationMembersDTO):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | Organization
    """

    return (
        await asyncio_detailed(
            organization_user_id=organization_user_id,
            client=client,
            body=body,
        )
    ).parsed
