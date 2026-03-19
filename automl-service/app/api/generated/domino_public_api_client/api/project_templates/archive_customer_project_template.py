from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_customer_project_template_response_400 import ArchiveCustomerProjectTemplateResponse400
from ...models.archive_customer_project_template_response_404 import ArchiveCustomerProjectTemplateResponse404
from ...models.archive_customer_project_template_response_500 import ArchiveCustomerProjectTemplateResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/develop/v1/customer-project-templates/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ArchiveCustomerProjectTemplateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ArchiveCustomerProjectTemplateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ArchiveCustomerProjectTemplateResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
]:
    """Delete a customer project template by id.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ArchiveCustomerProjectTemplateResponse400 | ArchiveCustomerProjectTemplateResponse404 | ArchiveCustomerProjectTemplateResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete a customer project template by id.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ArchiveCustomerProjectTemplateResponse400 | ArchiveCustomerProjectTemplateResponse404 | ArchiveCustomerProjectTemplateResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
]:
    """Delete a customer project template by id.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ArchiveCustomerProjectTemplateResponse400 | ArchiveCustomerProjectTemplateResponse404 | ArchiveCustomerProjectTemplateResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | ArchiveCustomerProjectTemplateResponse400
    | ArchiveCustomerProjectTemplateResponse404
    | ArchiveCustomerProjectTemplateResponse500
    | FailureEnvelopeV1
    | None
):
    """Delete a customer project template by id.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ArchiveCustomerProjectTemplateResponse400 | ArchiveCustomerProjectTemplateResponse404 | ArchiveCustomerProjectTemplateResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
