from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_endpoints_response_400 import GetEndpointsResponse400
from ...models.get_endpoints_response_404 import GetEndpointsResponse404
from ...models.get_endpoints_response_500 import GetEndpointsResponse500
from ...models.model_endpoints_listing_v1 import ModelEndpointsListingV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["registeredModelName"] = registered_model_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gen-ai/beta/endpoints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
    | None
):
    if response.status_code == 200:
        response_200 = ModelEndpointsListingV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEndpointsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEndpointsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetEndpointsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
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
    project_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
]:
    """Get all Gen AI endpoints accessible by the user

     Get all Gen AI endpoints accessible by the user

    Args:
        project_id (str | Unset):
        registered_model_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointsResponse400 | GetEndpointsResponse404 | GetEndpointsResponse500 | ModelEndpointsListingV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        registered_model_name=registered_model_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
    | None
):
    """Get all Gen AI endpoints accessible by the user

     Get all Gen AI endpoints accessible by the user

    Args:
        project_id (str | Unset):
        registered_model_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointsResponse400 | GetEndpointsResponse404 | GetEndpointsResponse500 | ModelEndpointsListingV1
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        registered_model_name=registered_model_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
]:
    """Get all Gen AI endpoints accessible by the user

     Get all Gen AI endpoints accessible by the user

    Args:
        project_id (str | Unset):
        registered_model_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointsResponse400 | GetEndpointsResponse404 | GetEndpointsResponse500 | ModelEndpointsListingV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        registered_model_name=registered_model_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    registered_model_name: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetEndpointsResponse400
    | GetEndpointsResponse404
    | GetEndpointsResponse500
    | ModelEndpointsListingV1
    | None
):
    """Get all Gen AI endpoints accessible by the user

     Get all Gen AI endpoints accessible by the user

    Args:
        project_id (str | Unset):
        registered_model_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointsResponse400 | GetEndpointsResponse404 | GetEndpointsResponse500 | ModelEndpointsListingV1
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            registered_model_name=registered_model_name,
        )
    ).parsed
