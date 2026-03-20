from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_selectable_deployment_targets_response_400 import GetSelectableDeploymentTargetsResponse400
from ...models.get_selectable_deployment_targets_response_404 import GetSelectableDeploymentTargetsResponse404
from ...models.get_selectable_deployment_targets_response_500 import GetSelectableDeploymentTargetsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    deployment_type: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["deploymentType"] = deployment_type

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/v1/deploymentTargets/selectable",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
    | None
):
    if response.status_code == 400:
        response_400 = GetSelectableDeploymentTargetsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetSelectableDeploymentTargetsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetSelectableDeploymentTargetsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
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
    name: str | Unset = UNSET,
    deployment_type: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
]:
    """Gets all selectable non-archived Deployment Targets based on the provided filters

     Gets all selectable non-archived Deployment Targets based on the provided filters.

    Args:
        name (str | Unset):
        deployment_type (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetSelectableDeploymentTargetsResponse400 | GetSelectableDeploymentTargetsResponse404 | GetSelectableDeploymentTargetsResponse500]
    """

    kwargs = _get_kwargs(
        name=name,
        deployment_type=deployment_type,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    deployment_type: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
    | None
):
    """Gets all selectable non-archived Deployment Targets based on the provided filters

     Gets all selectable non-archived Deployment Targets based on the provided filters.

    Args:
        name (str | Unset):
        deployment_type (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetSelectableDeploymentTargetsResponse400 | GetSelectableDeploymentTargetsResponse404 | GetSelectableDeploymentTargetsResponse500
    """

    return sync_detailed(
        client=client,
        name=name,
        deployment_type=deployment_type,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    deployment_type: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
]:
    """Gets all selectable non-archived Deployment Targets based on the provided filters

     Gets all selectable non-archived Deployment Targets based on the provided filters.

    Args:
        name (str | Unset):
        deployment_type (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetSelectableDeploymentTargetsResponse400 | GetSelectableDeploymentTargetsResponse404 | GetSelectableDeploymentTargetsResponse500]
    """

    kwargs = _get_kwargs(
        name=name,
        deployment_type=deployment_type,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    deployment_type: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetSelectableDeploymentTargetsResponse400
    | GetSelectableDeploymentTargetsResponse404
    | GetSelectableDeploymentTargetsResponse500
    | None
):
    """Gets all selectable non-archived Deployment Targets based on the provided filters

     Gets all selectable non-archived Deployment Targets based on the provided filters.

    Args:
        name (str | Unset):
        deployment_type (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetSelectableDeploymentTargetsResponse400 | GetSelectableDeploymentTargetsResponse404 | GetSelectableDeploymentTargetsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            deployment_type=deployment_type,
            offset=offset,
            limit=limit,
        )
    ).parsed
