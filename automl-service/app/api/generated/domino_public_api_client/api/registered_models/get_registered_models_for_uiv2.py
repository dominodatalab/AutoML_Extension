from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_registered_models_for_uiv2_model_category import GetRegisteredModelsForUIV2ModelCategory
from ...models.get_registered_models_for_uiv2_response_400 import GetRegisteredModelsForUIV2Response400
from ...models.get_registered_models_for_uiv2_response_404 import GetRegisteredModelsForUIV2Response404
from ...models.get_registered_models_for_uiv2_response_500 import GetRegisteredModelsForUIV2Response500
from ...models.paginated_registered_models_for_ui_envelope_v1 import PaginatedRegisteredModelsForUIEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    search_pattern: str | Unset = UNSET,
    globally_discoverable: bool | Unset = UNSET,
    model_category: GetRegisteredModelsForUIV2ModelCategory | Unset = UNSET,
    page_token: str | Unset = UNSET,
    max_results: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["searchPattern"] = search_pattern

    params["globallyDiscoverable"] = globally_discoverable

    json_model_category: str | Unset = UNSET
    if not isinstance(model_category, Unset):
        json_model_category = model_category.value

    params["modelCategory"] = json_model_category

    params["pageToken"] = page_token

    params["maxResults"] = max_results

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v2/ui",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedRegisteredModelsForUIEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRegisteredModelsForUIV2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetRegisteredModelsForUIV2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetRegisteredModelsForUIV2Response500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
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
    search_pattern: str | Unset = UNSET,
    globally_discoverable: bool | Unset = UNSET,
    model_category: GetRegisteredModelsForUIV2ModelCategory | Unset = UNSET,
    page_token: str | Unset = UNSET,
    max_results: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
]:
    """Get Registered Models visible to user (v2)

     Get registered models that a user can see, with support for filtering by model category. Returns all
    models by default.

    Args:
        project_id (str | Unset):
        search_pattern (str | Unset):
        globally_discoverable (bool | Unset):
        model_category (GetRegisteredModelsForUIV2ModelCategory | Unset):
        page_token (str | Unset):
        max_results (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelsForUIV2Response400 | GetRegisteredModelsForUIV2Response404 | GetRegisteredModelsForUIV2Response500 | PaginatedRegisteredModelsForUIEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        search_pattern=search_pattern,
        globally_discoverable=globally_discoverable,
        model_category=model_category,
        page_token=page_token,
        max_results=max_results,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    search_pattern: str | Unset = UNSET,
    globally_discoverable: bool | Unset = UNSET,
    model_category: GetRegisteredModelsForUIV2ModelCategory | Unset = UNSET,
    page_token: str | Unset = UNSET,
    max_results: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
    | None
):
    """Get Registered Models visible to user (v2)

     Get registered models that a user can see, with support for filtering by model category. Returns all
    models by default.

    Args:
        project_id (str | Unset):
        search_pattern (str | Unset):
        globally_discoverable (bool | Unset):
        model_category (GetRegisteredModelsForUIV2ModelCategory | Unset):
        page_token (str | Unset):
        max_results (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelsForUIV2Response400 | GetRegisteredModelsForUIV2Response404 | GetRegisteredModelsForUIV2Response500 | PaginatedRegisteredModelsForUIEnvelopeV1
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        search_pattern=search_pattern,
        globally_discoverable=globally_discoverable,
        model_category=model_category,
        page_token=page_token,
        max_results=max_results,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    search_pattern: str | Unset = UNSET,
    globally_discoverable: bool | Unset = UNSET,
    model_category: GetRegisteredModelsForUIV2ModelCategory | Unset = UNSET,
    page_token: str | Unset = UNSET,
    max_results: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
]:
    """Get Registered Models visible to user (v2)

     Get registered models that a user can see, with support for filtering by model category. Returns all
    models by default.

    Args:
        project_id (str | Unset):
        search_pattern (str | Unset):
        globally_discoverable (bool | Unset):
        model_category (GetRegisteredModelsForUIV2ModelCategory | Unset):
        page_token (str | Unset):
        max_results (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetRegisteredModelsForUIV2Response400 | GetRegisteredModelsForUIV2Response404 | GetRegisteredModelsForUIV2Response500 | PaginatedRegisteredModelsForUIEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        search_pattern=search_pattern,
        globally_discoverable=globally_discoverable,
        model_category=model_category,
        page_token=page_token,
        max_results=max_results,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    search_pattern: str | Unset = UNSET,
    globally_discoverable: bool | Unset = UNSET,
    model_category: GetRegisteredModelsForUIV2ModelCategory | Unset = UNSET,
    page_token: str | Unset = UNSET,
    max_results: int | Unset = 25,
    order_by: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetRegisteredModelsForUIV2Response400
    | GetRegisteredModelsForUIV2Response404
    | GetRegisteredModelsForUIV2Response500
    | PaginatedRegisteredModelsForUIEnvelopeV1
    | None
):
    """Get Registered Models visible to user (v2)

     Get registered models that a user can see, with support for filtering by model category. Returns all
    models by default.

    Args:
        project_id (str | Unset):
        search_pattern (str | Unset):
        globally_discoverable (bool | Unset):
        model_category (GetRegisteredModelsForUIV2ModelCategory | Unset):
        page_token (str | Unset):
        max_results (int | Unset):  Default: 25.
        order_by (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetRegisteredModelsForUIV2Response400 | GetRegisteredModelsForUIV2Response404 | GetRegisteredModelsForUIV2Response500 | PaginatedRegisteredModelsForUIEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            search_pattern=search_pattern,
            globally_discoverable=globally_discoverable,
            model_category=model_category,
            page_token=page_token,
            max_results=max_results,
            order_by=order_by,
        )
    ).parsed
