from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_job_tag_response_400 import AddJobTagResponse400
from ...models.add_job_tag_response_404 import AddJobTagResponse404
from ...models.add_job_tag_response_500 import AddJobTagResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.tag_envelope_v1 import TagEnvelopeV1
from ...models.tag_to_add_v1 import TagToAddV1
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    body: TagToAddV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/jobs/v1/jobs/{job_id}/tags".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1 | None:
    if response.status_code == 200:
        response_200 = TagEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddJobTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddJobTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = AddJobTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1]:
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
    body: TagToAddV1,
) -> Response[AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1]:
    """Add a tag to a Job

     Add a Tag to the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        body (TagToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TagToAddV1,
) -> AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1 | None:
    """Add a tag to a Job

     Add a Tag to the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        body (TagToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TagToAddV1,
) -> Response[AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1]:
    """Add a tag to a Job

     Add a Tag to the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        body (TagToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TagToAddV1,
) -> AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1 | None:
    """Add a tag to a Job

     Add a Tag to the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        body (TagToAddV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddJobTagResponse400 | AddJobTagResponse404 | AddJobTagResponse500 | FailureEnvelopeV1 | TagEnvelopeV1
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed
