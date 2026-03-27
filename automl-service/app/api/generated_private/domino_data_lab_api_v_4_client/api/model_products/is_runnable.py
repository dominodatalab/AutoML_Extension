from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_nucleus_modelproduct_models_is_runnable import DominoNucleusModelproductModelsIsRunnable
from ...models.is_runnable_type import IsRunnableType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    project_id: str,
    type_: IsRunnableType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    json_type_ = type_.value
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelProducts/isRunnable",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable | None:
    if response.status_code == 200:
        response_200 = DominoNucleusModelproductModelsIsRunnable.from_dict(response.json())

        return response_200

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
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    type_: IsRunnableType,
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable]:
    """retrieves whether this project can be run as the model product type

    Args:
        project_id (str):
        type_ (IsRunnableType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    type_: IsRunnableType,
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable | None:
    """retrieves whether this project can be run as the model product type

    Args:
        project_id (str):
        type_ (IsRunnableType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    type_: IsRunnableType,
) -> Response[DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable]:
    """retrieves whether this project can be run as the model product type

    Args:
        project_id (str):
        type_ (IsRunnableType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    type_: IsRunnableType,
) -> DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable | None:
    """retrieves whether this project can be run as the model product type

    Args:
        project_id (str):
        type_ (IsRunnableType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoNucleusModelproductModelsIsRunnable
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            type_=type_,
        )
    ).parsed
