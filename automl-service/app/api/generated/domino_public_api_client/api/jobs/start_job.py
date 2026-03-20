from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.job_envelope_v1 import JobEnvelopeV1
from ...models.new_job_v1 import NewJobV1
from ...models.start_job_response_400 import StartJobResponse400
from ...models.start_job_response_404 import StartJobResponse404
from ...models.start_job_response_500 import StartJobResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: NewJobV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/jobs/v1/jobs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500 | None:
    if response.status_code == 200:
        response_200 = JobEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartJobResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartJobResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = StartJobResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewJobV1,
) -> Response[FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500]:
    """Start a Job

     Start a new Job. Required permissions: `StartJob, UseGlobalCompute`

    Args:
        body (NewJobV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewJobV1,
) -> FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500 | None:
    """Start a Job

     Start a new Job. Required permissions: `StartJob, UseGlobalCompute`

    Args:
        body (NewJobV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewJobV1,
) -> Response[FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500]:
    """Start a Job

     Start a new Job. Required permissions: `StartJob, UseGlobalCompute`

    Args:
        body (NewJobV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewJobV1,
) -> FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500 | None:
    """Start a Job

     Start a new Job. Required permissions: `StartJob, UseGlobalCompute`

    Args:
        body (NewJobV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | JobEnvelopeV1 | StartJobResponse400 | StartJobResponse404 | StartJobResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
