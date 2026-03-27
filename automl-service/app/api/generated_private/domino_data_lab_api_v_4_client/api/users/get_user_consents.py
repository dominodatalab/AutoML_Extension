from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_common_user_user_consent import DominoCommonUserUserConsent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    execution_type: None | str | Unset = UNSET,
    execution_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_execution_type: None | str | Unset
    if isinstance(execution_type, Unset):
        json_execution_type = UNSET
    else:
        json_execution_type = execution_type
    params["executionType"] = json_execution_type

    json_execution_id: None | str | Unset
    if isinstance(execution_id, Unset):
        json_execution_id = UNSET
    else:
        json_execution_id = execution_id
    params["executionId"] = json_execution_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/userConsent",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoCommonUserUserConsent] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoCommonUserUserConsent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[DominoApiErrorResponse | list[DominoCommonUserUserConsent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    execution_type: None | str | Unset = UNSET,
    execution_id: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserUserConsent]]:
    """Get the user's consent of the current user

    Args:
        execution_type (None | str | Unset):
        execution_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserUserConsent]]
    """

    kwargs = _get_kwargs(
        execution_type=execution_type,
        execution_id=execution_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    execution_type: None | str | Unset = UNSET,
    execution_id: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserUserConsent] | None:
    """Get the user's consent of the current user

    Args:
        execution_type (None | str | Unset):
        execution_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserUserConsent]
    """

    return sync_detailed(
        client=client,
        execution_type=execution_type,
        execution_id=execution_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    execution_type: None | str | Unset = UNSET,
    execution_id: None | str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | list[DominoCommonUserUserConsent]]:
    """Get the user's consent of the current user

    Args:
        execution_type (None | str | Unset):
        execution_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoCommonUserUserConsent]]
    """

    kwargs = _get_kwargs(
        execution_type=execution_type,
        execution_id=execution_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    execution_type: None | str | Unset = UNSET,
    execution_id: None | str | Unset = UNSET,
) -> DominoApiErrorResponse | list[DominoCommonUserUserConsent] | None:
    """Get the user's consent of the current user

    Args:
        execution_type (None | str | Unset):
        execution_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoCommonUserUserConsent]
    """

    return (
        await asyncio_detailed(
            client=client,
            execution_type=execution_type,
            execution_id=execution_id,
        )
    ).parsed
