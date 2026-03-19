from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_tags_settings_envelope_v1 import BillingTagsSettingsEnvelopeV1
from ...models.billing_tags_settings_v1 import BillingTagsSettingsV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.update_billing_tag_settings_response_400 import UpdateBillingTagSettingsResponse400
from ...models.update_billing_tag_settings_response_404 import UpdateBillingTagSettingsResponse404
from ...models.update_billing_tag_settings_response_500 import UpdateBillingTagSettingsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: BillingTagsSettingsV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/cost/v1/billingtagSettings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = BillingTagsSettingsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateBillingTagSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateBillingTagSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateBillingTagSettingsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
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
    body: BillingTagsSettingsV1,
) -> Response[
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
]:
    """Update billing tags setting

     Update billing tags setting

    Args:
        body (BillingTagsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagsSettingsEnvelopeV1 | FailureEnvelopeV1 | UpdateBillingTagSettingsResponse400 | UpdateBillingTagSettingsResponse404 | UpdateBillingTagSettingsResponse500]
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
    body: BillingTagsSettingsV1,
) -> (
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
    | None
):
    """Update billing tags setting

     Update billing tags setting

    Args:
        body (BillingTagsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagsSettingsEnvelopeV1 | FailureEnvelopeV1 | UpdateBillingTagSettingsResponse400 | UpdateBillingTagSettingsResponse404 | UpdateBillingTagSettingsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BillingTagsSettingsV1,
) -> Response[
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
]:
    """Update billing tags setting

     Update billing tags setting

    Args:
        body (BillingTagsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagsSettingsEnvelopeV1 | FailureEnvelopeV1 | UpdateBillingTagSettingsResponse400 | UpdateBillingTagSettingsResponse404 | UpdateBillingTagSettingsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BillingTagsSettingsV1,
) -> (
    BillingTagsSettingsEnvelopeV1
    | FailureEnvelopeV1
    | UpdateBillingTagSettingsResponse400
    | UpdateBillingTagSettingsResponse404
    | UpdateBillingTagSettingsResponse500
    | None
):
    """Update billing tags setting

     Update billing tags setting

    Args:
        body (BillingTagsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagsSettingsEnvelopeV1 | FailureEnvelopeV1 | UpdateBillingTagSettingsResponse400 | UpdateBillingTagSettingsResponse404 | UpdateBillingTagSettingsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
