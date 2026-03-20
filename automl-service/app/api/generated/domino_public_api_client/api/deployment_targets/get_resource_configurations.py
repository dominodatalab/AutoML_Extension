from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_resource_configurations_response_400 import GetResourceConfigurationsResponse400
from ...models.get_resource_configurations_response_404 import GetResourceConfigurationsResponse404
from ...models.get_resource_configurations_response_500 import GetResourceConfigurationsResponse500
from ...models.paginated_resource_configurations import PaginatedResourceConfigurations
from ...types import UNSET, Response, Unset


def _get_kwargs(
    deployment_target_id: str,
    *,
    name: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/v1/deploymentTargets/{deployment_target_id}/resourceConfigurations".format(
            deployment_target_id=quote(str(deployment_target_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedResourceConfigurations.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetResourceConfigurationsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetResourceConfigurationsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetResourceConfigurationsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
]:
    """Gets all non-archived Resource Configurations based on the provided filters

     Gets all non-archived Resource Configurations based on the provided filters.

    Args:
        deployment_target_id (str):
        name (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetResourceConfigurationsResponse400 | GetResourceConfigurationsResponse404 | GetResourceConfigurationsResponse500 | PaginatedResourceConfigurations]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        name=name,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
    | None
):
    """Gets all non-archived Resource Configurations based on the provided filters

     Gets all non-archived Resource Configurations based on the provided filters.

    Args:
        deployment_target_id (str):
        name (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetResourceConfigurationsResponse400 | GetResourceConfigurationsResponse404 | GetResourceConfigurationsResponse500 | PaginatedResourceConfigurations
    """

    return sync_detailed(
        deployment_target_id=deployment_target_id,
        client=client,
        name=name,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> Response[
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
]:
    """Gets all non-archived Resource Configurations based on the provided filters

     Gets all non-archived Resource Configurations based on the provided filters.

    Args:
        deployment_target_id (str):
        name (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetResourceConfigurationsResponse400 | GetResourceConfigurationsResponse404 | GetResourceConfigurationsResponse500 | PaginatedResourceConfigurations]
    """

    kwargs = _get_kwargs(
        deployment_target_id=deployment_target_id,
        name=name,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deployment_target_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
) -> (
    FailureEnvelopeV1
    | GetResourceConfigurationsResponse400
    | GetResourceConfigurationsResponse404
    | GetResourceConfigurationsResponse500
    | PaginatedResourceConfigurations
    | None
):
    """Gets all non-archived Resource Configurations based on the provided filters

     Gets all non-archived Resource Configurations based on the provided filters.

    Args:
        deployment_target_id (str):
        name (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetResourceConfigurationsResponse400 | GetResourceConfigurationsResponse404 | GetResourceConfigurationsResponse500 | PaginatedResourceConfigurations
    """

    return (
        await asyncio_detailed(
            deployment_target_id=deployment_target_id,
            client=client,
            name=name,
            offset=offset,
            limit=limit,
        )
    ).parsed
