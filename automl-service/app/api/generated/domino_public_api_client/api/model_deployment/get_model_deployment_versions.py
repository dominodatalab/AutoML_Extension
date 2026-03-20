from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_deployment_versions_response_400 import GetModelDeploymentVersionsResponse400
from ...models.get_model_deployment_versions_response_404 import GetModelDeploymentVersionsResponse404
from ...models.get_model_deployment_versions_response_500 import GetModelDeploymentVersionsResponse500
from ...models.model_deployment_paginated_list import ModelDeploymentPaginatedList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_deployment_id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelDeployments/{model_deployment_id}/versions".format(
            model_deployment_id=quote(str(model_deployment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    if response.status_code == 200:
        response_200 = ModelDeploymentPaginatedList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetModelDeploymentVersionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetModelDeploymentVersionsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelDeploymentVersionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
]:
    """Retrieve all versions of a specific Model Deployment

     Retrieves summary information for all historical versions of a Model Deployment.

    Args:
        model_deployment_id (str):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentVersionsResponse400 | GetModelDeploymentVersionsResponse404 | GetModelDeploymentVersionsResponse500 | ModelDeploymentPaginatedList]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    """Retrieve all versions of a specific Model Deployment

     Retrieves summary information for all historical versions of a Model Deployment.

    Args:
        model_deployment_id (str):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentVersionsResponse400 | GetModelDeploymentVersionsResponse404 | GetModelDeploymentVersionsResponse500 | ModelDeploymentPaginatedList
    """

    return sync_detailed(
        model_deployment_id=model_deployment_id,
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
]:
    """Retrieve all versions of a specific Model Deployment

     Retrieves summary information for all historical versions of a Model Deployment.

    Args:
        model_deployment_id (str):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelDeploymentVersionsResponse400 | GetModelDeploymentVersionsResponse404 | GetModelDeploymentVersionsResponse500 | ModelDeploymentPaginatedList]
    """

    kwargs = _get_kwargs(
        model_deployment_id=model_deployment_id,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_deployment_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelDeploymentVersionsResponse400
    | GetModelDeploymentVersionsResponse404
    | GetModelDeploymentVersionsResponse500
    | ModelDeploymentPaginatedList
    | None
):
    """Retrieve all versions of a specific Model Deployment

     Retrieves summary information for all historical versions of a Model Deployment.

    Args:
        model_deployment_id (str):
        limit (int | Unset):
        offset (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelDeploymentVersionsResponse400 | GetModelDeploymentVersionsResponse404 | GetModelDeploymentVersionsResponse500 | ModelDeploymentPaginatedList
    """

    return (
        await asyncio_detailed(
            model_deployment_id=model_deployment_id,
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
