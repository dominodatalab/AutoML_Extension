from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_registered_model_names_model_category import GetRegisteredModelNamesModelCategory
from ...models.get_registered_model_names_response_400 import GetRegisteredModelNamesResponse400
from ...models.get_registered_model_names_response_404 import GetRegisteredModelNamesResponse404
from ...models.get_registered_model_names_response_500 import GetRegisteredModelNamesResponse500
from ...models.paginated_registered_model_names_v1 import PaginatedRegisteredModelNamesV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    project_id: str | Unset = UNSET,
    model_category: GetRegisteredModelNamesModelCategory | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    params["offset"] = offset

    params["limit"] = limit

    params["projectId"] = project_id

    json_model_category: str | Unset = UNSET
    if not isinstance(model_category, Unset):
        json_model_category = model_category.value

    params["modelCategory"] = json_model_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/names",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedRegisteredModelNamesV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRegisteredModelNamesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRegisteredModelNamesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetRegisteredModelNamesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
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
    search: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    project_id: str | Unset = UNSET,
    model_category: GetRegisteredModelNamesModelCategory | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
]:
    """Get a list of Registered Models' names visible to user

     Get a list of Registered Models' names visible to user.

    Args:
        search (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        project_id (str | Unset):
        model_category (GetRegisteredModelNamesModelCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelNamesResponse400 | GetRegisteredModelNamesResponse404 | GetRegisteredModelNamesResponse500 | PaginatedRegisteredModelNamesV1]
    """

    kwargs = _get_kwargs(
        search=search,
        offset=offset,
        limit=limit,
        project_id=project_id,
        model_category=model_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    project_id: str | Unset = UNSET,
    model_category: GetRegisteredModelNamesModelCategory | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
    | None
):
    """Get a list of Registered Models' names visible to user

     Get a list of Registered Models' names visible to user.

    Args:
        search (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        project_id (str | Unset):
        model_category (GetRegisteredModelNamesModelCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelNamesResponse400 | GetRegisteredModelNamesResponse404 | GetRegisteredModelNamesResponse500 | PaginatedRegisteredModelNamesV1
    """

    return sync_detailed(
        client=client,
        search=search,
        offset=offset,
        limit=limit,
        project_id=project_id,
        model_category=model_category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    project_id: str | Unset = UNSET,
    model_category: GetRegisteredModelNamesModelCategory | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
]:
    """Get a list of Registered Models' names visible to user

     Get a list of Registered Models' names visible to user.

    Args:
        search (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        project_id (str | Unset):
        model_category (GetRegisteredModelNamesModelCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelNamesResponse400 | GetRegisteredModelNamesResponse404 | GetRegisteredModelNamesResponse500 | PaginatedRegisteredModelNamesV1]
    """

    kwargs = _get_kwargs(
        search=search,
        offset=offset,
        limit=limit,
        project_id=project_id,
        model_category=model_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 10,
    project_id: str | Unset = UNSET,
    model_category: GetRegisteredModelNamesModelCategory | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelNamesResponse400
    | GetRegisteredModelNamesResponse404
    | GetRegisteredModelNamesResponse500
    | PaginatedRegisteredModelNamesV1
    | None
):
    """Get a list of Registered Models' names visible to user

     Get a list of Registered Models' names visible to user.

    Args:
        search (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 10.
        project_id (str | Unset):
        model_category (GetRegisteredModelNamesModelCategory | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelNamesResponse400 | GetRegisteredModelNamesResponse404 | GetRegisteredModelNamesResponse500 | PaginatedRegisteredModelNamesV1
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            offset=offset,
            limit=limit,
            project_id=project_id,
            model_category=model_category,
        )
    ).parsed
