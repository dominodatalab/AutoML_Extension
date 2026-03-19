from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.athena_billing_configs_v1 import AthenaBillingConfigsV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.set_athena_configs_response_400 import SetAthenaConfigsResponse400
from ...models.set_athena_configs_response_404 import SetAthenaConfigsResponse404
from ...models.set_athena_configs_response_500 import SetAthenaConfigsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: AthenaBillingConfigsV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/cost/v1/athenaConfigs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = AthenaBillingConfigsV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetAthenaConfigsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SetAthenaConfigsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = SetAthenaConfigsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
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
    body: AthenaBillingConfigsV1,
) -> Response[
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
]:
    """Set AWS Billing API Configuration

     Set AWS Billing API Configuration

    Args:
        body (AthenaBillingConfigsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AthenaBillingConfigsV1 | FailureEnvelopeV1 | SetAthenaConfigsResponse400 | SetAthenaConfigsResponse404 | SetAthenaConfigsResponse500]
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
    body: AthenaBillingConfigsV1,
) -> (
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
    | None
):
    """Set AWS Billing API Configuration

     Set AWS Billing API Configuration

    Args:
        body (AthenaBillingConfigsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AthenaBillingConfigsV1 | FailureEnvelopeV1 | SetAthenaConfigsResponse400 | SetAthenaConfigsResponse404 | SetAthenaConfigsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AthenaBillingConfigsV1,
) -> Response[
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
]:
    """Set AWS Billing API Configuration

     Set AWS Billing API Configuration

    Args:
        body (AthenaBillingConfigsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AthenaBillingConfigsV1 | FailureEnvelopeV1 | SetAthenaConfigsResponse400 | SetAthenaConfigsResponse404 | SetAthenaConfigsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AthenaBillingConfigsV1,
) -> (
    AthenaBillingConfigsV1
    | FailureEnvelopeV1
    | SetAthenaConfigsResponse400
    | SetAthenaConfigsResponse404
    | SetAthenaConfigsResponse500
    | None
):
    """Set AWS Billing API Configuration

     Set AWS Billing API Configuration

    Args:
        body (AthenaBillingConfigsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AthenaBillingConfigsV1 | FailureEnvelopeV1 | SetAthenaConfigsResponse400 | SetAthenaConfigsResponse404 | SetAthenaConfigsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
