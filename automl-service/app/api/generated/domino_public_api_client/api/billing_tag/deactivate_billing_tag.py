from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_tag_envelope_v1 import BillingTagEnvelopeV1
from ...models.deactivate_billing_tag_response_400 import DeactivateBillingTagResponse400
from ...models.deactivate_billing_tag_response_404 import DeactivateBillingTagResponse404
from ...models.deactivate_billing_tag_response_500 import DeactivateBillingTagResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    tag: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/cost/v1/billingtags/{tag}".format(
            tag=quote(str(tag), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = BillingTagEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeactivateBillingTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeactivateBillingTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DeactivateBillingTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
]:
    """Deactivate billing tag

     Deactivate a  billing tag.

    Args:
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagEnvelopeV1 | DeactivateBillingTagResponse400 | DeactivateBillingTagResponse404 | DeactivateBillingTagResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
    | None
):
    """Deactivate billing tag

     Deactivate a  billing tag.

    Args:
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagEnvelopeV1 | DeactivateBillingTagResponse400 | DeactivateBillingTagResponse404 | DeactivateBillingTagResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        tag=tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    tag: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
]:
    """Deactivate billing tag

     Deactivate a  billing tag.

    Args:
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTagEnvelopeV1 | DeactivateBillingTagResponse400 | DeactivateBillingTagResponse404 | DeactivateBillingTagResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        tag=tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    BillingTagEnvelopeV1
    | DeactivateBillingTagResponse400
    | DeactivateBillingTagResponse404
    | DeactivateBillingTagResponse500
    | FailureEnvelopeV1
    | None
):
    """Deactivate billing tag

     Deactivate a  billing tag.

    Args:
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTagEnvelopeV1 | DeactivateBillingTagResponse400 | DeactivateBillingTagResponse404 | DeactivateBillingTagResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            tag=tag,
            client=client,
        )
    ).parsed
