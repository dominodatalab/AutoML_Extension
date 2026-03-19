from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.model_endpoint_version_patch_result_v1 import ModelEndpointVersionPatchResultV1
from ...models.model_endpoint_version_patch_v1 import ModelEndpointVersionPatchV1
from ...models.patch_endpoint_version_by_number_response_400 import PatchEndpointVersionByNumberResponse400
from ...models.patch_endpoint_version_by_number_response_404 import PatchEndpointVersionByNumberResponse404
from ...models.patch_endpoint_version_by_number_response_500 import PatchEndpointVersionByNumberResponse500
from ...types import Response


def _get_kwargs(
    endpoint_id: str,
    version_number: int,
    *,
    body: ModelEndpointVersionPatchV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/gen-ai/beta/endpoints/{endpoint_id}/versions/{version_number}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ModelEndpointVersionPatchResultV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchEndpointVersionByNumberResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchEndpointVersionByNumberResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = PatchEndpointVersionByNumberResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: ModelEndpointVersionPatchV1,
) -> Response[
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
]:
    """Patch a Gen AI Endpoint version

     Patch a Gen AI Endpoint version

    This can be used to patch the endpoints properties and version label and description in place,
    or to generate a new version based on the given version.
    Changing the value of any of the following properties will stop the current version and start a new
    one
    with the patched values:

    - vanityUrl
    - modelSource
    - environment
    - hardwareTierId
    - configuration

    Args:
        endpoint_id (str):
        version_number (int):
        body (ModelEndpointVersionPatchV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ModelEndpointVersionPatchResultV1 | PatchEndpointVersionByNumberResponse400 | PatchEndpointVersionByNumberResponse404 | PatchEndpointVersionByNumberResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: ModelEndpointVersionPatchV1,
) -> (
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
    | None
):
    """Patch a Gen AI Endpoint version

     Patch a Gen AI Endpoint version

    This can be used to patch the endpoints properties and version label and description in place,
    or to generate a new version based on the given version.
    Changing the value of any of the following properties will stop the current version and start a new
    one
    with the patched values:

    - vanityUrl
    - modelSource
    - environment
    - hardwareTierId
    - configuration

    Args:
        endpoint_id (str):
        version_number (int):
        body (ModelEndpointVersionPatchV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ModelEndpointVersionPatchResultV1 | PatchEndpointVersionByNumberResponse400 | PatchEndpointVersionByNumberResponse404 | PatchEndpointVersionByNumberResponse500
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        version_number=version_number,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: ModelEndpointVersionPatchV1,
) -> Response[
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
]:
    """Patch a Gen AI Endpoint version

     Patch a Gen AI Endpoint version

    This can be used to patch the endpoints properties and version label and description in place,
    or to generate a new version based on the given version.
    Changing the value of any of the following properties will stop the current version and start a new
    one
    with the patched values:

    - vanityUrl
    - modelSource
    - environment
    - hardwareTierId
    - configuration

    Args:
        endpoint_id (str):
        version_number (int):
        body (ModelEndpointVersionPatchV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ModelEndpointVersionPatchResultV1 | PatchEndpointVersionByNumberResponse400 | PatchEndpointVersionByNumberResponse404 | PatchEndpointVersionByNumberResponse500]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        version_number=version_number,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: str,
    version_number: int,
    *,
    client: AuthenticatedClient | Client,
    body: ModelEndpointVersionPatchV1,
) -> (
    FailureEnvelopeV1
    | ModelEndpointVersionPatchResultV1
    | PatchEndpointVersionByNumberResponse400
    | PatchEndpointVersionByNumberResponse404
    | PatchEndpointVersionByNumberResponse500
    | None
):
    """Patch a Gen AI Endpoint version

     Patch a Gen AI Endpoint version

    This can be used to patch the endpoints properties and version label and description in place,
    or to generate a new version based on the given version.
    Changing the value of any of the following properties will stop the current version and start a new
    one
    with the patched values:

    - vanityUrl
    - modelSource
    - environment
    - hardwareTierId
    - configuration

    Args:
        endpoint_id (str):
        version_number (int):
        body (ModelEndpointVersionPatchV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ModelEndpointVersionPatchResultV1 | PatchEndpointVersionByNumberResponse400 | PatchEndpointVersionByNumberResponse404 | PatchEndpointVersionByNumberResponse500
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            version_number=version_number,
            client=client,
            body=body,
        )
    ).parsed
