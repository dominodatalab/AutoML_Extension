from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_job_details_response_400 import GetJobDetailsResponse400
from ...models.get_job_details_response_404 import GetJobDetailsResponse404
from ...models.get_job_details_response_500 import GetJobDetailsResponse500
from ...models.job_envelope_v1 import JobEnvelopeV1
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/beta/jobs/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetJobDetailsResponse400
    | GetJobDetailsResponse404
    | GetJobDetailsResponse500
    | JobEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = JobEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobDetailsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJobDetailsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetJobDetailsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1
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
) -> Response[
    FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1
]:
    """Get Job details

     Retrieve a Job's details by its Id. Required permissions: `ViewJobs`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetJobDetailsResponse400
    | GetJobDetailsResponse404
    | GetJobDetailsResponse500
    | JobEnvelopeV1
    | None
):
    """Get Job details

     Retrieve a Job's details by its Id. Required permissions: `ViewJobs`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1
]:
    """Get Job details

     Retrieve a Job's details by its Id. Required permissions: `ViewJobs`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetJobDetailsResponse400
    | GetJobDetailsResponse404
    | GetJobDetailsResponse500
    | JobEnvelopeV1
    | None
):
    """Get Job details

     Retrieve a Job's details by its Id. Required permissions: `ViewJobs`. *Note:* This is a beta
    endpoint with known limitations.

    Args:
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobDetailsResponse400 | GetJobDetailsResponse404 | GetJobDetailsResponse500 | JobEnvelopeV1
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
