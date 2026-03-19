from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_endpoint_collaborators_response_400 import GetEndpointCollaboratorsResponse400
from ...models.get_endpoint_collaborators_response_404 import GetEndpointCollaboratorsResponse404
from ...models.get_endpoint_collaborators_response_500 import GetEndpointCollaboratorsResponse500
from ...models.model_endpoint_collaborator_v1 import ModelEndpointCollaboratorV1
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/gen-ai/beta/endpoints/{endpoint_id}/collaborators".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelEndpointCollaboratorV1.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetEndpointCollaboratorsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetEndpointCollaboratorsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetEndpointCollaboratorsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
]:
    """Get the collaborators for a Gen AI Endpoint

     Get the collaborators for a Gen AI Endpoint

    Args:
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointCollaboratorsResponse400 | GetEndpointCollaboratorsResponse404 | GetEndpointCollaboratorsResponse500 | list[ModelEndpointCollaboratorV1]]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
    | None
):
    """Get the collaborators for a Gen AI Endpoint

     Get the collaborators for a Gen AI Endpoint

    Args:
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointCollaboratorsResponse400 | GetEndpointCollaboratorsResponse404 | GetEndpointCollaboratorsResponse500 | list[ModelEndpointCollaboratorV1]
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
]:
    """Get the collaborators for a Gen AI Endpoint

     Get the collaborators for a Gen AI Endpoint

    Args:
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetEndpointCollaboratorsResponse400 | GetEndpointCollaboratorsResponse404 | GetEndpointCollaboratorsResponse500 | list[ModelEndpointCollaboratorV1]]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetEndpointCollaboratorsResponse400
    | GetEndpointCollaboratorsResponse404
    | GetEndpointCollaboratorsResponse500
    | list[ModelEndpointCollaboratorV1]
    | None
):
    """Get the collaborators for a Gen AI Endpoint

     Get the collaborators for a Gen AI Endpoint

    Args:
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetEndpointCollaboratorsResponse400 | GetEndpointCollaboratorsResponse404 | GetEndpointCollaboratorsResponse500 | list[ModelEndpointCollaboratorV1]
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
        )
    ).parsed
