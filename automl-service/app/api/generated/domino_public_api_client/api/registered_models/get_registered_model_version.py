from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_registered_model_version_response_400 import GetRegisteredModelVersionResponse400
from ...models.get_registered_model_version_response_404 import GetRegisteredModelVersionResponse404
from ...models.get_registered_model_version_response_500 import GetRegisteredModelVersionResponse500
from ...models.registered_model_version_details_v1 import RegisteredModelVersionDetailsV1
from ...types import Response


def _get_kwargs(
    model_name: str,
    version: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/{model_name}/versions/{version}".format(
            model_name=quote(str(model_name), safe=""),
            version=quote(str(version), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
    | None
):
    if response.status_code == 200:
        response_200 = RegisteredModelVersionDetailsV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRegisteredModelVersionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRegisteredModelVersionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetRegisteredModelVersionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_name: str,
    version: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
]:
    """Get a specific version of a Registered Model

     Get a specific version of a Registered Model

    Args:
        model_name (str):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelVersionResponse400 | GetRegisteredModelVersionResponse404 | GetRegisteredModelVersionResponse500 | RegisteredModelVersionDetailsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_name: str,
    version: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
    | None
):
    """Get a specific version of a Registered Model

     Get a specific version of a Registered Model

    Args:
        model_name (str):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelVersionResponse400 | GetRegisteredModelVersionResponse404 | GetRegisteredModelVersionResponse500 | RegisteredModelVersionDetailsV1
    """

    return sync_detailed(
        model_name=model_name,
        version=version,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_name: str,
    version: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
]:
    """Get a specific version of a Registered Model

     Get a specific version of a Registered Model

    Args:
        model_name (str):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelVersionResponse400 | GetRegisteredModelVersionResponse404 | GetRegisteredModelVersionResponse500 | RegisteredModelVersionDetailsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_name: str,
    version: int,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelVersionResponse400
    | GetRegisteredModelVersionResponse404
    | GetRegisteredModelVersionResponse500
    | RegisteredModelVersionDetailsV1
    | None
):
    """Get a specific version of a Registered Model

     Get a specific version of a Registered Model

    Args:
        model_name (str):
        version (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelVersionResponse400 | GetRegisteredModelVersionResponse404 | GetRegisteredModelVersionResponse500 | RegisteredModelVersionDetailsV1
    """

    return (
        await asyncio_detailed(
            model_name=model_name,
            version=version,
            client=client,
        )
    ).parsed
