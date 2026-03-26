from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_linked_goals_for_job_response_400 import GetLinkedGoalsForJobResponse400
from ...models.get_linked_goals_for_job_response_404 import GetLinkedGoalsForJobResponse404
from ...models.get_linked_goals_for_job_response_500 import GetLinkedGoalsForJobResponse500
from ...models.paginated_goal_envelope_v1 import PaginatedGoalEnvelopeV1
from ...types import UNSET, Response


def _get_kwargs(
    *,
    job_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["jobId"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/v1/goals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = PaginatedGoalEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetLinkedGoalsForJobResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetLinkedGoalsForJobResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetLinkedGoalsForJobResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
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
    job_id: str,
) -> Response[
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
]:
    """Get linked goals for a job

     Retrieve goals for a Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetLinkedGoalsForJobResponse400 | GetLinkedGoalsForJobResponse404 | GetLinkedGoalsForJobResponse500 | PaginatedGoalEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> (
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
    | None
):
    """Get linked goals for a job

     Retrieve goals for a Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetLinkedGoalsForJobResponse400 | GetLinkedGoalsForJobResponse404 | GetLinkedGoalsForJobResponse500 | PaginatedGoalEnvelopeV1
    """

    return sync_detailed(
        client=client,
        job_id=job_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> Response[
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
]:
    """Get linked goals for a job

     Retrieve goals for a Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetLinkedGoalsForJobResponse400 | GetLinkedGoalsForJobResponse404 | GetLinkedGoalsForJobResponse500 | PaginatedGoalEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> (
    FailureEnvelopeV1
    | GetLinkedGoalsForJobResponse400
    | GetLinkedGoalsForJobResponse404
    | GetLinkedGoalsForJobResponse500
    | PaginatedGoalEnvelopeV1
    | None
):
    """Get linked goals for a job

     Retrieve goals for a Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetLinkedGoalsForJobResponse400 | GetLinkedGoalsForJobResponse404 | GetLinkedGoalsForJobResponse500 | PaginatedGoalEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            job_id=job_id,
        )
    ).parsed
