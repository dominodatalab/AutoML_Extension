from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_user_response import AppUserResponse
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_publisher_filter_options_response_400 import GetPublisherFilterOptionsResponse400
from ...models.get_publisher_filter_options_response_500 import GetPublisherFilterOptionsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/apps/beta/apps/publisherFilterOptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppUserResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = GetPublisherFilterOptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = GetPublisherFilterOptionsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
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
    project_id: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
]:
    """Get Publisher Filter Options

     Returns all app publishers from all the apps the principal can access, optionally filtered by
    project.

    Args:
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetPublisherFilterOptionsResponse400 | GetPublisherFilterOptionsResponse500 | list[AppUserResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
    | None
):
    """Get Publisher Filter Options

     Returns all app publishers from all the apps the principal can access, optionally filtered by
    project.

    Args:
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetPublisherFilterOptionsResponse400 | GetPublisherFilterOptionsResponse500 | list[AppUserResponse]
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
]:
    """Get Publisher Filter Options

     Returns all app publishers from all the apps the principal can access, optionally filtered by
    project.

    Args:
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetPublisherFilterOptionsResponse400 | GetPublisherFilterOptionsResponse500 | list[AppUserResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetPublisherFilterOptionsResponse400
    | GetPublisherFilterOptionsResponse500
    | list[AppUserResponse]
    | None
):
    """Get Publisher Filter Options

     Returns all app publishers from all the apps the principal can access, optionally filtered by
    project.

    Args:
        project_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetPublisherFilterOptionsResponse400 | GetPublisherFilterOptionsResponse500 | list[AppUserResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
        )
    ).parsed
