from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_scheduledjob_api_new_scheduled_job_dto import DominoScheduledjobApiNewScheduledJobDto
from ...models.domino_scheduledjob_api_scheduled_job_dto import DominoScheduledjobApiScheduledJobDto
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: DominoScheduledjobApiNewScheduledJobDto,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/scheduledjobs".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto | None:
    if response.status_code == 200:
        response_200 = DominoScheduledjobApiScheduledJobDto.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = DominoApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoScheduledjobApiNewScheduledJobDto,
) -> Response[DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto]:
    """creates a new scheduled job

    Args:
        project_id (str):
        body (DominoScheduledjobApiNewScheduledJobDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoScheduledjobApiNewScheduledJobDto,
) -> DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto | None:
    """creates a new scheduled job

    Args:
        project_id (str):
        body (DominoScheduledjobApiNewScheduledJobDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoScheduledjobApiNewScheduledJobDto,
) -> Response[DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto]:
    """creates a new scheduled job

    Args:
        project_id (str):
        body (DominoScheduledjobApiNewScheduledJobDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoScheduledjobApiNewScheduledJobDto,
) -> DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto | None:
    """creates a new scheduled job

    Args:
        project_id (str):
        body (DominoScheduledjobApiNewScheduledJobDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoScheduledjobApiScheduledJobDto
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
