from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_project_management_web_error_response import DominoProjectManagementWebErrorResponse
from ...models.domino_projects_api_project_goal import DominoProjectsApiProjectGoal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    goal_id: str,
    *,
    assignee_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["assigneeId"] = assignee_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projectManagement/goal/{goal_id}/assign".format(
            goal_id=quote(str(goal_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal | None:
    if response.status_code == 200:
        response_200 = DominoProjectsApiProjectGoal.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    assignee_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal]:
    """Assign a user to a goal

    Args:
        goal_id (str):
        assignee_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        assignee_id=assignee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    assignee_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal | None:
    """Assign a user to a goal

    Args:
        goal_id (str):
        assignee_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal
    """

    return sync_detailed(
        goal_id=goal_id,
        client=client,
        assignee_id=assignee_id,
    ).parsed


async def asyncio_detailed(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    assignee_id: str | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal]:
    """Assign a user to a goal

    Args:
        goal_id (str):
        assignee_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        assignee_id=assignee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    assignee_id: str | Unset = UNSET,
) -> DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal | None:
    """Assign a user to a goal

    Args:
        goal_id (str):
        assignee_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoProjectManagementWebErrorResponse | DominoProjectsApiProjectGoal
    """

    return (
        await asyncio_detailed(
            goal_id=goal_id,
            client=client,
            assignee_id=assignee_id,
        )
    ).parsed
