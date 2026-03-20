from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_registered_model_version_from_run_response_400 import (
    CreateRegisteredModelVersionFromRunResponse400,
)
from ...models.create_registered_model_version_from_run_response_404 import (
    CreateRegisteredModelVersionFromRunResponse404,
)
from ...models.create_registered_model_version_from_run_response_500 import (
    CreateRegisteredModelVersionFromRunResponse500,
)
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_registered_model_version_v1 import NewRegisteredModelVersionV1
from ...models.registered_model_version_details_v1 import RegisteredModelVersionDetailsV1
from ...types import Response


def _get_kwargs(
    model_name: str,
    *,
    body: NewRegisteredModelVersionV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/registeredmodels/v1/{model_name}/versions".format(
            model_name=quote(str(model_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelVersionDetailsV1
    | None
):
    if response.status_code == 200:
        response_200 = RegisteredModelVersionDetailsV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateRegisteredModelVersionFromRunResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateRegisteredModelVersionFromRunResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = CreateRegisteredModelVersionFromRunResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
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
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelVersionV1,
) -> Response[
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelVersionDetailsV1
]:
    """[DEPRECATED] Create a new version of a Registered Model

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        model_name (str):
        body (NewRegisteredModelVersionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRegisteredModelVersionFromRunResponse400 | CreateRegisteredModelVersionFromRunResponse404 | CreateRegisteredModelVersionFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelVersionDetailsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelVersionV1,
) -> (
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelVersionDetailsV1
    | None
):
    """[DEPRECATED] Create a new version of a Registered Model

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        model_name (str):
        body (NewRegisteredModelVersionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRegisteredModelVersionFromRunResponse400 | CreateRegisteredModelVersionFromRunResponse404 | CreateRegisteredModelVersionFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelVersionDetailsV1
    """

    return sync_detailed(
        model_name=model_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelVersionV1,
) -> Response[
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelVersionDetailsV1
]:
    """[DEPRECATED] Create a new version of a Registered Model

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        model_name (str):
        body (NewRegisteredModelVersionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRegisteredModelVersionFromRunResponse400 | CreateRegisteredModelVersionFromRunResponse404 | CreateRegisteredModelVersionFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelVersionDetailsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: NewRegisteredModelVersionV1,
) -> (
    CreateRegisteredModelVersionFromRunResponse400
    | CreateRegisteredModelVersionFromRunResponse404
    | CreateRegisteredModelVersionFromRunResponse500
    | FailureEnvelopeV1
    | RegisteredModelVersionDetailsV1
    | None
):
    """[DEPRECATED] Create a new version of a Registered Model

     **DEPRECATED**: This endpoint is deprecated as of version 6.2.1.
    Please migrate to POST /api/registeredmodels/v2 for enhanced functionality.

    Args:
        model_name (str):
        body (NewRegisteredModelVersionV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRegisteredModelVersionFromRunResponse400 | CreateRegisteredModelVersionFromRunResponse404 | CreateRegisteredModelVersionFromRunResponse500 | FailureEnvelopeV1 | RegisteredModelVersionDetailsV1
    """

    return (
        await asyncio_detailed(
            model_name=model_name,
            client=client,
            body=body,
        )
    ).parsed
