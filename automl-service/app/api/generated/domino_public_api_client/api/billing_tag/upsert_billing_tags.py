from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_tags_envelope_v1 import BillingTagsEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.new_billing_tags_v1 import NewBillingTagsV1
from ...models.upsert_billing_tags_response_400 import UpsertBillingTagsResponse400
from ...models.upsert_billing_tags_response_404 import UpsertBillingTagsResponse404
from ...models.upsert_billing_tags_response_500 import UpsertBillingTagsResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: NewBillingTagsV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/cost/v1/billingtags",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = BillingTagsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpsertBillingTagsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpsertBillingTagsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpsertBillingTagsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
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
    body: NewBillingTagsV1,
) -> Response[
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
]:
    """Upsert billing codes

     Upsert billing codes.

    Args:
        body (NewBillingTagsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagsEnvelopeV1 | FailureEnvelopeV1 | UpsertBillingTagsResponse400 | UpsertBillingTagsResponse404 | UpsertBillingTagsResponse500]
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
    body: NewBillingTagsV1,
) -> (
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
    | None
):
    """Upsert billing codes

     Upsert billing codes.

    Args:
        body (NewBillingTagsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagsEnvelopeV1 | FailureEnvelopeV1 | UpsertBillingTagsResponse400 | UpsertBillingTagsResponse404 | UpsertBillingTagsResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewBillingTagsV1,
) -> Response[
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
]:
    """Upsert billing codes

     Upsert billing codes.

    Args:
        body (NewBillingTagsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagsEnvelopeV1 | FailureEnvelopeV1 | UpsertBillingTagsResponse400 | UpsertBillingTagsResponse404 | UpsertBillingTagsResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewBillingTagsV1,
) -> (
    BillingTagsEnvelopeV1
    | FailureEnvelopeV1
    | UpsertBillingTagsResponse400
    | UpsertBillingTagsResponse404
    | UpsertBillingTagsResponse500
    | None
):
    """Upsert billing codes

     Upsert billing codes.

    Args:
        body (NewBillingTagsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagsEnvelopeV1 | FailureEnvelopeV1 | UpsertBillingTagsResponse400 | UpsertBillingTagsResponse404 | UpsertBillingTagsResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
