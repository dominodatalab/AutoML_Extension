from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_modelproduct_models_consumer_model_product import (
    DominoNucleusModelproductModelsConsumerModelProduct,
)
from ...models.domino_nucleus_modelproduct_models_grant_access_required import (
    DominoNucleusModelproductModelsGrantAccessRequired,
)
from ...models.domino_nucleus_modelproduct_models_login_required import DominoNucleusModelproductModelsLoginRequired
from ...types import Response


def _get_kwargs(
    vanity_url: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelProducts/consumer/vanityUrl/{vanity_url}".format(
            vanity_url=quote(str(vanity_url), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
    | None
):
    if response.status_code == 200:
        response_200 = DominoNucleusModelproductModelsConsumerModelProduct.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoNucleusModelproductModelsGrantAccessRequired.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoNucleusModelproductModelsLoginRequired.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
]:
    """retrieves a Model Product by vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsConsumerModelProduct | DominoNucleusModelproductModelsGrantAccessRequired | DominoNucleusModelproductModelsLoginRequired]
    """

    kwargs = _get_kwargs(
        vanity_url=vanity_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
    | None
):
    """retrieves a Model Product by vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsConsumerModelProduct | DominoNucleusModelproductModelsGrantAccessRequired | DominoNucleusModelproductModelsLoginRequired
    """

    return sync_detailed(
        vanity_url=vanity_url,
        client=client,
    ).parsed


async def asyncio_detailed(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
]:
    """retrieves a Model Product by vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsConsumerModelProduct | DominoNucleusModelproductModelsGrantAccessRequired | DominoNucleusModelproductModelsLoginRequired]
    """

    kwargs = _get_kwargs(
        vanity_url=vanity_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DominoApiErrorResponse
    | DominoNucleusModelproductModelsConsumerModelProduct
    | DominoNucleusModelproductModelsGrantAccessRequired
    | DominoNucleusModelproductModelsLoginRequired
    | None
):
    """retrieves a Model Product by vanity URL

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsConsumerModelProduct | DominoNucleusModelproductModelsGrantAccessRequired | DominoNucleusModelproductModelsLoginRequired
    """

    return (
        await asyncio_detailed(
            vanity_url=vanity_url,
            client=client,
        )
    ).parsed
