from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.model_api_version import ModelApiVersion
from ...models.model_api_version_creation_request import ModelApiVersionCreationRequest
from ...types import Response


def _get_kwargs(
    model_api_id: str,
    *,
    body: ModelApiVersionCreationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/modelServing/v1/modelApis/{model_api_id}/versions".format(
            model_api_id=quote(str(model_api_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ModelApiVersion | None:
    if response.status_code == 201:
        response_201 = ModelApiVersion.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ModelApiVersion]:
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
    body: ModelApiVersionCreationRequest,
) -> Response[ModelApiVersion]:
    """Creates a Model API Version for a Model API.

    Args:
        model_api_id (str):
        body (ModelApiVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersion]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelApiVersionCreationRequest,
) -> ModelApiVersion | None:
    """Creates a Model API Version for a Model API.

    Args:
        model_api_id (str):
        body (ModelApiVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersion
    """

    return sync_detailed(
        model_api_id=model_api_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelApiVersionCreationRequest,
) -> Response[ModelApiVersion]:
    """Creates a Model API Version for a Model API.

    Args:
        model_api_id (str):
        body (ModelApiVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelApiVersion]
    """

    kwargs = _get_kwargs(
        model_api_id=model_api_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_api_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelApiVersionCreationRequest,
) -> ModelApiVersion | None:
    """Creates a Model API Version for a Model API.

    Args:
        model_api_id (str):
        body (ModelApiVersionCreationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelApiVersion
    """

    return (
        await asyncio_detailed(
            model_api_id=model_api_id,
            client=client,
            body=body,
        )
    ).parsed
