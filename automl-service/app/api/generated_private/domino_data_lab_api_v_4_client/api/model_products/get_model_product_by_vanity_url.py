from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_modelproduct_models_model_product import DominoNucleusModelproductModelsModelProduct
from ...types import Response


def _get_kwargs(
    vanity_url: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelProducts/vanityUrl/{vanity_url}".format(
            vanity_url=quote(str(vanity_url), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct | None:
    if response.status_code == 200:
        response_200 = DominoNucleusModelproductModelsModelProduct.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DominoApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DominoApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DominoApiErrorResponse.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct]:
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
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct]:
    """retrieves a Model Product by vanity URl

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct]
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
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct | None:
    """retrieves a Model Product by vanity URl

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct
    """

    return sync_detailed(
        vanity_url=vanity_url,
        client=client,
    ).parsed


async def asyncio_detailed(
    vanity_url: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct]:
    """retrieves a Model Product by vanity URl

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct]
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
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct | None:
    """retrieves a Model Product by vanity URl

    Args:
        vanity_url (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsModelProduct
    """

    return (
        await asyncio_detailed(
            vanity_url=vanity_url,
            client=client,
        )
    ).parsed
