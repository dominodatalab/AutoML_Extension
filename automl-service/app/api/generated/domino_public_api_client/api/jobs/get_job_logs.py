from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_job_logs_log_type import GetJobLogsLogType
from ...models.get_job_logs_response_400 import GetJobLogsResponse400
from ...models.get_job_logs_response_404 import GetJobLogsResponse404
from ...models.get_job_logs_response_500 import GetJobLogsResponse500
from ...models.logs_envelope_v1 import LogsEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    log_type: GetJobLogsLogType | Unset = UNSET,
    limit: int | Unset = UNSET,
    latest_time_nano: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_log_type: str | Unset = UNSET
    if not isinstance(log_type, Unset):
        json_log_type = log_type.value

    params["logType"] = json_log_type

    params["limit"] = limit

    params["latestTimeNano"] = latest_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/beta/jobs/{job_id}/logs".format(
            job_id=quote(str(job_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1 | None:
    if response.status_code == 200:
        response_200 = LogsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobLogsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJobLogsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetJobLogsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetJobLogsLogType | Unset = UNSET,
    limit: int | Unset = UNSET,
    latest_time_nano: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1
]:
    """Get logs for a Job

     Retrieve the logs for the Job with the specified Id. Required permissions: `ViewJobs`. *Note:* This
    is a beta endpoint with known limitations.

    Args:
        job_id (str):
        log_type (GetJobLogsLogType | Unset):
        limit (int | Unset):
        latest_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        log_type=log_type,
        limit=limit,
        latest_time_nano=latest_time_nano,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetJobLogsLogType | Unset = UNSET,
    limit: int | Unset = UNSET,
    latest_time_nano: str | Unset = UNSET,
) -> FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1 | None:
    """Get logs for a Job

     Retrieve the logs for the Job with the specified Id. Required permissions: `ViewJobs`. *Note:* This
    is a beta endpoint with known limitations.

    Args:
        job_id (str):
        log_type (GetJobLogsLogType | Unset):
        limit (int | Unset):
        latest_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        log_type=log_type,
        limit=limit,
        latest_time_nano=latest_time_nano,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetJobLogsLogType | Unset = UNSET,
    limit: int | Unset = UNSET,
    latest_time_nano: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1
]:
    """Get logs for a Job

     Retrieve the logs for the Job with the specified Id. Required permissions: `ViewJobs`. *Note:* This
    is a beta endpoint with known limitations.

    Args:
        job_id (str):
        log_type (GetJobLogsLogType | Unset):
        limit (int | Unset):
        latest_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        log_type=log_type,
        limit=limit,
        latest_time_nano=latest_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: GetJobLogsLogType | Unset = UNSET,
    limit: int | Unset = UNSET,
    latest_time_nano: str | Unset = UNSET,
) -> FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1 | None:
    """Get logs for a Job

     Retrieve the logs for the Job with the specified Id. Required permissions: `ViewJobs`. *Note:* This
    is a beta endpoint with known limitations.

    Args:
        job_id (str):
        log_type (GetJobLogsLogType | Unset):
        limit (int | Unset):
        latest_time_nano (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobLogsResponse400 | GetJobLogsResponse404 | GetJobLogsResponse500 | LogsEnvelopeV1
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            log_type=log_type,
            limit=limit,
            latest_time_nano=latest_time_nano,
        )
    ).parsed
