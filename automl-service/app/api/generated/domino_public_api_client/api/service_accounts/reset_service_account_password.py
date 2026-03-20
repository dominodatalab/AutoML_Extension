from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.reset_service_account_password_response_400 import ResetServiceAccountPasswordResponse400
from ...models.reset_service_account_password_response_404 import ResetServiceAccountPasswordResponse404
from ...types import Response


def _get_kwargs(
    service_account_idp_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/serviceAccounts/v1/serviceAccounts/{service_account_idp_id}/resetpassword".format(
            service_account_idp_id=quote(str(service_account_idp_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ResetServiceAccountPasswordResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ResetServiceAccountPasswordResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404
]:
    """
    Args:
        service_account_idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404 | None:
    """
    Args:
        service_account_idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404
    """

    return sync_detailed(
        service_account_idp_id=service_account_idp_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404
]:
    """
    Args:
        service_account_idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404]
    """

    kwargs = _get_kwargs(
        service_account_idp_id=service_account_idp_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_account_idp_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404 | None:
    """
    Args:
        service_account_idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FailureEnvelopeV1 | ResetServiceAccountPasswordResponse400 | ResetServiceAccountPasswordResponse404
    """

    return (
        await asyncio_detailed(
            service_account_idp_id=service_account_idp_id,
            client=client,
        )
    ).parsed
