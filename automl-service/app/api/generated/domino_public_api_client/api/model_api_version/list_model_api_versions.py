from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_version import ModelApiVersion
from ...types import Response


def _get_kwargs(
    model_api_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/modelServing/v1/modelApis/{model_api_id}/versions".format(
            model_api_id=quote(str(model_api_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[ModelApiVersion] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelApiVersion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[ModelApiVersion]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[ModelApiVersion]]:
    """Lists the Model API Versions for a Model API.

    Args:
        model_api_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ModelApiVersion]]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[ModelApiVersion] | None:
    """Lists the Model API Versions for a Model API.

    Args:
        model_api_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ModelApiVersion]
    """

    return sync_detailed(
        model_api_id=model_api_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[ModelApiVersion]]:
    """Lists the Model API Versions for a Model API.

    Args:
        model_api_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ModelApiVersion]]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> list[ModelApiVersion] | None:
    """Lists the Model API Versions for a Model API.

    Args:
        model_api_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ModelApiVersion]
    """

    return (
        await asyncio_detailed(
            model_api_id=model_api_id,
            client=client,
        )
    ).parsed
