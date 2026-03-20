from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_envelope_v1 import DeleteEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.unlink_job_from_goal_response_400 import UnlinkJobFromGoalResponse400
from ...models.unlink_job_from_goal_response_404 import UnlinkJobFromGoalResponse404
from ...models.unlink_job_from_goal_response_500 import UnlinkJobFromGoalResponse500
from ...types import UNSET, Response


def _get_kwargs(
    goal_id: str,
    *,
    job_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["jobId"] = job_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/jobs/v1/goals/{goal_id}".format(
            goal_id=quote(str(goal_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UnlinkJobFromGoalResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UnlinkJobFromGoalResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UnlinkJobFromGoalResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
]:
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
    job_id: str,
) -> Response[
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
]:
    """Unlink goal from job

     Unlink the Goal with the specified Id from a Job. Required permissions: `ViewJobs, Edit`

    Args:
        goal_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | FailureEnvelopeV1 | UnlinkJobFromGoalResponse400 | UnlinkJobFromGoalResponse404 | UnlinkJobFromGoalResponse500]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
    | None
):
    """Unlink goal from job

     Unlink the Goal with the specified Id from a Job. Required permissions: `ViewJobs, Edit`

    Args:
        goal_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | FailureEnvelopeV1 | UnlinkJobFromGoalResponse400 | UnlinkJobFromGoalResponse404 | UnlinkJobFromGoalResponse500
    """

    return sync_detailed(
        goal_id=goal_id,
        client=client,
        job_id=job_id,
    ).parsed


async def asyncio_detailed(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> Response[
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
]:
    """Unlink goal from job

     Unlink the Goal with the specified Id from a Job. Required permissions: `ViewJobs, Edit`

    Args:
        goal_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | FailureEnvelopeV1 | UnlinkJobFromGoalResponse400 | UnlinkJobFromGoalResponse404 | UnlinkJobFromGoalResponse500]
    """

    kwargs = _get_kwargs(
        goal_id=goal_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    goal_id: str,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | UnlinkJobFromGoalResponse400
    | UnlinkJobFromGoalResponse404
    | UnlinkJobFromGoalResponse500
    | None
):
    """Unlink goal from job

     Unlink the Goal with the specified Id from a Job. Required permissions: `ViewJobs, Edit`

    Args:
        goal_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | FailureEnvelopeV1 | UnlinkJobFromGoalResponse400 | UnlinkJobFromGoalResponse404 | UnlinkJobFromGoalResponse500
    """

    return (
        await asyncio_detailed(
            goal_id=goal_id,
            client=client,
            job_id=job_id,
        )
    ).parsed
