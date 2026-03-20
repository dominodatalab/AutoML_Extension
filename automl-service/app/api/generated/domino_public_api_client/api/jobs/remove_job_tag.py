from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_envelope_v1 import DeleteEnvelopeV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.remove_job_tag_response_400 import RemoveJobTagResponse400
from ...models.remove_job_tag_response_404 import RemoveJobTagResponse404
from ...models.remove_job_tag_response_500 import RemoveJobTagResponse500
from ...types import UNSET, Response


def _get_kwargs(
    job_id: str,
    tag_id: str,
    *,
    project_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/jobs/v1/jobs/{job_id}/tags/{tag_id}".format(
            job_id=quote(str(job_id), safe=""),
            tag_id=quote(str(tag_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | RemoveJobTagResponse400
    | RemoveJobTagResponse404
    | RemoveJobTagResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RemoveJobTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveJobTagResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveJobTagResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
) -> Response[
    DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500
]:
    """Remove a tag from a Job

     Remove a Tag from the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        tag_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        tag_id=tag_id,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | RemoveJobTagResponse400
    | RemoveJobTagResponse404
    | RemoveJobTagResponse500
    | None
):
    """Remove a tag from a Job

     Remove a Tag from the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        tag_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500
    """

    return sync_detailed(
        job_id=job_id,
        tag_id=tag_id,
        client=client,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
) -> Response[
    DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500
]:
    """Remove a tag from a Job

     Remove a Tag from the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        tag_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        tag_id=tag_id,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    tag_id: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
) -> (
    DeleteEnvelopeV1
    | FailureEnvelopeV1
    | RemoveJobTagResponse400
    | RemoveJobTagResponse404
    | RemoveJobTagResponse500
    | None
):
    """Remove a tag from a Job

     Remove a Tag from the Job with the specified Id. Required permissions: `ViewJobs`

    Args:
        job_id (str):
        tag_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteEnvelopeV1 | FailureEnvelopeV1 | RemoveJobTagResponse400 | RemoveJobTagResponse404 | RemoveJobTagResponse500
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            tag_id=tag_id,
            client=client,
            project_id=project_id,
        )
    ).parsed
