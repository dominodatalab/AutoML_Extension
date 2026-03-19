from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_kubecost_license_key_response_400 import AddKubecostLicenseKeyResponse400
from ...models.add_kubecost_license_key_response_404 import AddKubecostLicenseKeyResponse404
from ...models.add_kubecost_license_key_response_500 import AddKubecostLicenseKeyResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.kubecost_license_response_v1 import KubecostLicenseResponseV1
from ...models.kubecost_license_v1 import KubecostLicenseV1
from ...types import Response


def _get_kwargs(
    *,
    body: KubecostLicenseV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/cost/v1/licenseKey",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
    | None
):
    if response.status_code == 200:
        response_200 = KubecostLicenseResponseV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddKubecostLicenseKeyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddKubecostLicenseKeyResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AddKubecostLicenseKeyResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
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
    body: KubecostLicenseV1,
) -> Response[
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
]:
    """Add kubecost license key

     Add kubecost license key

    Args:
        body (KubecostLicenseV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddKubecostLicenseKeyResponse400 | AddKubecostLicenseKeyResponse404 | AddKubecostLicenseKeyResponse500 | FailureEnvelopeV1 | KubecostLicenseResponseV1]
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
    body: KubecostLicenseV1,
) -> (
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
    | None
):
    """Add kubecost license key

     Add kubecost license key

    Args:
        body (KubecostLicenseV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddKubecostLicenseKeyResponse400 | AddKubecostLicenseKeyResponse404 | AddKubecostLicenseKeyResponse500 | FailureEnvelopeV1 | KubecostLicenseResponseV1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KubecostLicenseV1,
) -> Response[
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
]:
    """Add kubecost license key

     Add kubecost license key

    Args:
        body (KubecostLicenseV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddKubecostLicenseKeyResponse400 | AddKubecostLicenseKeyResponse404 | AddKubecostLicenseKeyResponse500 | FailureEnvelopeV1 | KubecostLicenseResponseV1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KubecostLicenseV1,
) -> (
    AddKubecostLicenseKeyResponse400
    | AddKubecostLicenseKeyResponse404
    | AddKubecostLicenseKeyResponse500
    | FailureEnvelopeV1
    | KubecostLicenseResponseV1
    | None
):
    """Add kubecost license key

     Add kubecost license key

    Args:
        body (KubecostLicenseV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddKubecostLicenseKeyResponse400 | AddKubecostLicenseKeyResponse404 | AddKubecostLicenseKeyResponse500 | FailureEnvelopeV1 | KubecostLicenseResponseV1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
