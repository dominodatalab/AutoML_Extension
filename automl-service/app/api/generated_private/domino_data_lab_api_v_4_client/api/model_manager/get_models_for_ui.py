from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.get_models_for_ui_sort_by import GetModelsForUISortBy
from ...models.get_models_for_ui_sort_direction import GetModelsForUISortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    sort_by: GetModelsForUISortBy | Unset = UNSET,
    sort_direction: GetModelsForUISortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    registered_model_name: None | str | Unset = UNSET,
    registered_model_version: float | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["environmentId"] = environment_id

    json_page_number: float | None | Unset
    if isinstance(page_number, Unset):
        json_page_number = UNSET
    else:
        json_page_number = page_number
    params["pageNumber"] = json_page_number

    json_page_size: float | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_search_pattern: None | str | Unset
    if isinstance(search_pattern, Unset):
        json_search_pattern = UNSET
    else:
        json_search_pattern = search_pattern
    params["searchPattern"] = json_search_pattern

    json_registered_model_name: None | str | Unset
    if isinstance(registered_model_name, Unset):
        json_registered_model_name = UNSET
    else:
        json_registered_model_name = registered_model_name
    params["registeredModelName"] = json_registered_model_name

    json_registered_model_version: float | None | Unset
    if isinstance(registered_model_version, Unset):
        json_registered_model_version = UNSET
    else:
        json_registered_model_version = registered_model_version
    params["registeredModelVersion"] = json_registered_model_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modelManager/ui/models",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DominoApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | DominoApiErrorResponse]:
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
    environment_id: str | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    sort_by: GetModelsForUISortBy | Unset = UNSET,
    sort_direction: GetModelsForUISortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    registered_model_name: None | str | Unset = UNSET,
    registered_model_version: float | None | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """Get model APIs for display in the UI

    Args:
        project_id (str | Unset):
        environment_id (str | Unset):
        page_number (float | None | Unset):
        page_size (float | None | Unset):
        sort_by (GetModelsForUISortBy | Unset):
        sort_direction (GetModelsForUISortDirection | Unset):
        search_pattern (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
        sort_by=sort_by,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    sort_by: GetModelsForUISortBy | Unset = UNSET,
    sort_direction: GetModelsForUISortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    registered_model_name: None | str | Unset = UNSET,
    registered_model_version: float | None | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """Get model APIs for display in the UI

    Args:
        project_id (str | Unset):
        environment_id (str | Unset):
        page_number (float | None | Unset):
        page_size (float | None | Unset):
        sort_by (GetModelsForUISortBy | Unset):
        sort_direction (GetModelsForUISortDirection | Unset):
        search_pattern (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
        sort_by=sort_by,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    sort_by: GetModelsForUISortBy | Unset = UNSET,
    sort_direction: GetModelsForUISortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    registered_model_name: None | str | Unset = UNSET,
    registered_model_version: float | None | Unset = UNSET,
) -> Response[Any | DominoApiErrorResponse]:
    """Get model APIs for display in the UI

    Args:
        project_id (str | Unset):
        environment_id (str | Unset):
        page_number (float | None | Unset):
        page_size (float | None | Unset):
        sort_by (GetModelsForUISortBy | Unset):
        sort_direction (GetModelsForUISortDirection | Unset):
        search_pattern (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DominoApiErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        environment_id=environment_id,
        page_number=page_number,
        page_size=page_size,
        sort_by=sort_by,
        sort_direction=sort_direction,
        search_pattern=search_pattern,
        registered_model_name=registered_model_name,
        registered_model_version=registered_model_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = UNSET,
    environment_id: str | Unset = UNSET,
    page_number: float | None | Unset = UNSET,
    page_size: float | None | Unset = UNSET,
    sort_by: GetModelsForUISortBy | Unset = UNSET,
    sort_direction: GetModelsForUISortDirection | Unset = UNSET,
    search_pattern: None | str | Unset = UNSET,
    registered_model_name: None | str | Unset = UNSET,
    registered_model_version: float | None | Unset = UNSET,
) -> Any | DominoApiErrorResponse | None:
    """Get model APIs for display in the UI

    Args:
        project_id (str | Unset):
        environment_id (str | Unset):
        page_number (float | None | Unset):
        page_size (float | None | Unset):
        sort_by (GetModelsForUISortBy | Unset):
        sort_direction (GetModelsForUISortDirection | Unset):
        search_pattern (None | str | Unset):
        registered_model_name (None | str | Unset):
        registered_model_version (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DominoApiErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            environment_id=environment_id,
            page_number=page_number,
            page_size=page_size,
            sort_by=sort_by,
            sort_direction=sort_direction,
            search_pattern=search_pattern,
            registered_model_name=registered_model_name,
            registered_model_version=registered_model_version,
        )
    ).parsed
