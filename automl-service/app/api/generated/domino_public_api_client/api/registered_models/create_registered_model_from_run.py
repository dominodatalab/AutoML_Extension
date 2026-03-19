from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_registered_model_from_run_response_400 import CreateRegisteredModelFromRunResponse400
from ...models.create_registered_model_from_run_response_404 import CreateRegisteredModelFromRunResponse404
from ...models.create_registered_model_from_run_response_500 import CreateRegisteredModelFromRunResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_registered_model_v1 import NewRegisteredModelV1
from ...models.registered_model_v1 import RegisteredModelV1
from ...types import Response


def _get_kwargs(
    *,
    body: NewRegisteredModelV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/registeredmodels/v1",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
    | None
):
    if response.status_code == 200:
        response_200 = RegisteredModelV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateRegisteredModelFromRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateRegisteredModelFromRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateRegisteredModelFromRunResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
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
    body: NewRegisteredModelV1,
) -> Response[
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
]:
    """[DEPRECATED] Create a new Registered Model from an experiment run

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        body (NewRegisteredModelV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRegisteredModelFromRunResponse400 | CreateRegisteredModelFromRunResponse404 | CreateRegisteredModelFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelV1]
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
    body: NewRegisteredModelV1,
) -> (
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
    | None
):
    """[DEPRECATED] Create a new Registered Model from an experiment run

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        body (NewRegisteredModelV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRegisteredModelFromRunResponse400 | CreateRegisteredModelFromRunResponse404 | CreateRegisteredModelFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelV1,
) -> Response[
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
]:
    """[DEPRECATED] Create a new Registered Model from an experiment run

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        body (NewRegisteredModelV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRegisteredModelFromRunResponse400 | CreateRegisteredModelFromRunResponse404 | CreateRegisteredModelFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelV1,
) -> (
    CreateRegisteredModelFromRunResponse400
    | CreateRegisteredModelFromRunResponse404
    | CreateRegisteredModelFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelV1
    | None
):
    """[DEPRECATED] Create a new Registered Model from an experiment run

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        body (NewRegisteredModelV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRegisteredModelFromRunResponse400 | CreateRegisteredModelFromRunResponse404 | CreateRegisteredModelFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
