from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.goal_envelope_v1 import GoalEnvelopeV1
from ...models.goal_to_link_v1 import GoalToLinkV1
from ...models.link_job_to_goal_response_400 import LinkJobToGoalResponse400
from ...models.link_job_to_goal_response_404 import LinkJobToGoalResponse404
from ...models.link_job_to_goal_response_500 import LinkJobToGoalResponse500
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: GoalToLinkV1,
    job_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["jobId"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/jobs/v1/goals",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GoalEnvelopeV1
    | LinkJobToGoalResponse400
    | LinkJobToGoalResponse404
    | LinkJobToGoalResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GoalEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LinkJobToGoalResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = LinkJobToGoalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = LinkJobToGoalResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500
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
    body: GoalToLinkV1,
    job_id: str,
) -> Response[
    FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500
]:
    """Link a goal to a job

     Link the Goal with the specified Id to a Job. Required permissions: `ViewJobs, Edit`

    Args:
        job_id (str):
        body (GoalToLinkV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GoalToLinkV1,
    job_id: str,
) -> (
    FailureEnvelopeV1
    | GoalEnvelopeV1
    | LinkJobToGoalResponse400
    | LinkJobToGoalResponse404
    | LinkJobToGoalResponse500
    | None
):
    """Link a goal to a job

     Link the Goal with the specified Id to a Job. Required permissions: `ViewJobs, Edit`

    Args:
        job_id (str):
        body (GoalToLinkV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
        job_id=job_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GoalToLinkV1,
    job_id: str,
) -> Response[
    FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500
]:
    """Link a goal to a job

     Link the Goal with the specified Id to a Job. Required permissions: `ViewJobs, Edit`

    Args:
        job_id (str):
        body (GoalToLinkV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GoalToLinkV1,
    job_id: str,
) -> (
    FailureEnvelopeV1
    | GoalEnvelopeV1
    | LinkJobToGoalResponse400
    | LinkJobToGoalResponse404
    | LinkJobToGoalResponse500
    | None
):
    """Link a goal to a job

     Link the Goal with the specified Id to a Job. Required permissions: `ViewJobs, Edit`

    Args:
        job_id (str):
        body (GoalToLinkV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GoalEnvelopeV1 | LinkJobToGoalResponse400 | LinkJobToGoalResponse404 | LinkJobToGoalResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            job_id=job_id,
        )
    ).parsed
