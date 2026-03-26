from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.organization_envelope_v1 import OrganizationEnvelopeV1
from ...models.remove_user_from_org_response_400 import RemoveUserFromOrgResponse400
from ...models.remove_user_from_org_response_404 import RemoveUserFromOrgResponse404
from ...models.remove_user_from_org_response_500 import RemoveUserFromOrgResponse500
from ...types import UNSET, Response


def _get_kwargs(
    organization_id: str,
    *,
    member_to_remove_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["memberToRemoveId"] = member_to_remove_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/organizations/v1/organizations/{organization_id}/user".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
    | None
):
    if response.status_code == 200:
        response_200 = OrganizationEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveUserFromOrgResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveUserFromOrgResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveUserFromOrgResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient | Client,
    member_to_remove_id: str,
) -> Response[
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
]:
    """Remove a user from an org

     Remove a user from an Organization. Required permissions: `EditMembers`

    Args:
        organization_id (str):
        member_to_remove_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | OrganizationEnvelopeV1 | RemoveUserFromOrgResponse400 | RemoveUserFromOrgResponse404 | RemoveUserFromOrgResponse500]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        member_to_remove_id=member_to_remove_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient | Client,
    member_to_remove_id: str,
) -> (
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
    | None
):
    """Remove a user from an org

     Remove a user from an Organization. Required permissions: `EditMembers`

    Args:
        organization_id (str):
        member_to_remove_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | OrganizationEnvelopeV1 | RemoveUserFromOrgResponse400 | RemoveUserFromOrgResponse404 | RemoveUserFromOrgResponse500
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        member_to_remove_id=member_to_remove_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient | Client,
    member_to_remove_id: str,
) -> Response[
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
]:
    """Remove a user from an org

     Remove a user from an Organization. Required permissions: `EditMembers`

    Args:
        organization_id (str):
        member_to_remove_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | OrganizationEnvelopeV1 | RemoveUserFromOrgResponse400 | RemoveUserFromOrgResponse404 | RemoveUserFromOrgResponse500]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        member_to_remove_id=member_to_remove_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient | Client,
    member_to_remove_id: str,
) -> (
    FailureEnvelopeV1
    | OrganizationEnvelopeV1
    | RemoveUserFromOrgResponse400
    | RemoveUserFromOrgResponse404
    | RemoveUserFromOrgResponse500
    | None
):
    """Remove a user from an org

     Remove a user from an Organization. Required permissions: `EditMembers`

    Args:
        organization_id (str):
        member_to_remove_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | OrganizationEnvelopeV1 | RemoveUserFromOrgResponse400 | RemoveUserFromOrgResponse404 | RemoveUserFromOrgResponse500
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            member_to_remove_id=member_to_remove_id,
        )
    ).parsed
