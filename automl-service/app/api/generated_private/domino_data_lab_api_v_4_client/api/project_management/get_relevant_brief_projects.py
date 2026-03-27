from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_project_management_api_pm_project_summary import DominoProjectManagementApiPmProjectSummary
from ...models.domino_project_management_web_error_response import DominoProjectManagementWebErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_name: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_project_name: None | str | Unset
    if isinstance(project_name, Unset):
        json_project_name = UNSET
    else:
        json_project_name = project_name
    params["projectName"] = json_project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projectManagement/getProjectsFromPMT",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | list[DominoProjectManagementApiPmProjectSummary]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoProjectManagementApiPmProjectSummary.from_dict(response_200_item_data)

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

    if response.status_code == 409:
        response_409 = DominoProjectManagementWebErrorResponse.from_dict(response.json())

        return response_409

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
    DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]
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
    project_name: None | str | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]
]:
    """Gets List of Relevant Project Management Projects from Project Management Tool

    Args:
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_name: None | str | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | list[DominoProjectManagementApiPmProjectSummary]
    | None
):
    """Gets List of Relevant Project Management Projects from Project Management Tool

    Args:
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]
    """

    return sync_detailed(
        client=client,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_name: None | str | Unset = UNSET,
) -> Response[
    DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]
]:
    """Gets List of Relevant Project Management Projects from Project Management Tool

    Args:
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_name: None | str | Unset = UNSET,
) -> (
    DominoApiErrorResponse
    | DominoProjectManagementWebErrorResponse
    | list[DominoProjectManagementApiPmProjectSummary]
    | None
):
    """Gets List of Relevant Project Management Projects from Project Management Tool

    Args:
        project_name (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | list[DominoProjectManagementApiPmProjectSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_name=project_name,
        )
    ).parsed
