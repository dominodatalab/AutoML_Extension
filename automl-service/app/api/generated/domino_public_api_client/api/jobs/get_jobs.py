from __future__ import annotations
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_jobs_response_400 import GetJobsResponse400
from ...models.get_jobs_response_404 import GetJobsResponse404
from ...models.get_jobs_response_500 import GetJobsResponse500
from ...models.get_jobs_sort_by import GetJobsSortBy
from ...models.get_jobs_status_filter import GetJobsStatusFilter
from ...models.paginated_job_envelope_v1 import PaginatedJobEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: GetJobsSortBy | Unset = UNSET,
    domino_stats_sort_field_name: str | Unset = UNSET,
    ascending: bool | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    status_filter: GetJobsStatusFilter | Unset = UNSET,
    tag_filter: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["projectId"] = project_id

    params["offset"] = offset

    params["limit"] = limit

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    params["dominoStatsSortFieldName"] = domino_stats_sort_field_name

    params["ascending"] = ascending

    params["showArchived"] = show_archived

    json_status_filter: str | Unset = UNSET
    if not isinstance(status_filter, Unset):
        json_status_filter = status_filter.value

    params["statusFilter"] = json_status_filter

    params["tagFilter"] = tag_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/beta/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1 | None:
    if response.status_code == 200:
        response_200 = PaginatedJobEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetJobsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetJobsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1
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
    project_id: str,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: GetJobsSortBy | Unset = UNSET,
    domino_stats_sort_field_name: str | Unset = UNSET,
    ascending: bool | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    status_filter: GetJobsStatusFilter | Unset = UNSET,
    tag_filter: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1
]:
    """Get Jobs for a project

     Retrieve all Jobs that belong to a project. Required permissions: `ViewJobs.` *Note:* This is a beta
    endpoint with known limitations.

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):
        sort_by (GetJobsSortBy | Unset):
        domino_stats_sort_field_name (str | Unset):
        ascending (bool | Unset):
        show_archived (bool | Unset):
        status_filter (GetJobsStatusFilter | Unset):
        tag_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        ascending=ascending,
        show_archived=show_archived,
        status_filter=status_filter,
        tag_filter=tag_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: GetJobsSortBy | Unset = UNSET,
    domino_stats_sort_field_name: str | Unset = UNSET,
    ascending: bool | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    status_filter: GetJobsStatusFilter | Unset = UNSET,
    tag_filter: str | Unset = UNSET,
) -> FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1 | None:
    """Get Jobs for a project

     Retrieve all Jobs that belong to a project. Required permissions: `ViewJobs.` *Note:* This is a beta
    endpoint with known limitations.

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):
        sort_by (GetJobsSortBy | Unset):
        domino_stats_sort_field_name (str | Unset):
        ascending (bool | Unset):
        show_archived (bool | Unset):
        status_filter (GetJobsStatusFilter | Unset):
        tag_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        ascending=ascending,
        show_archived=show_archived,
        status_filter=status_filter,
        tag_filter=tag_filter,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: GetJobsSortBy | Unset = UNSET,
    domino_stats_sort_field_name: str | Unset = UNSET,
    ascending: bool | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    status_filter: GetJobsStatusFilter | Unset = UNSET,
    tag_filter: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1
]:
    """Get Jobs for a project

     Retrieve all Jobs that belong to a project. Required permissions: `ViewJobs.` *Note:* This is a beta
    endpoint with known limitations.

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):
        sort_by (GetJobsSortBy | Unset):
        domino_stats_sort_field_name (str | Unset):
        ascending (bool | Unset):
        show_archived (bool | Unset):
        status_filter (GetJobsStatusFilter | Unset):
        tag_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        domino_stats_sort_field_name=domino_stats_sort_field_name,
        ascending=ascending,
        show_archived=show_archived,
        status_filter=status_filter,
        tag_filter=tag_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_by: GetJobsSortBy | Unset = UNSET,
    domino_stats_sort_field_name: str | Unset = UNSET,
    ascending: bool | Unset = UNSET,
    show_archived: bool | Unset = UNSET,
    status_filter: GetJobsStatusFilter | Unset = UNSET,
    tag_filter: str | Unset = UNSET,
) -> FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1 | None:
    """Get Jobs for a project

     Retrieve all Jobs that belong to a project. Required permissions: `ViewJobs.` *Note:* This is a beta
    endpoint with known limitations.

    Args:
        project_id (str):
        offset (int | Unset):
        limit (int | Unset):
        sort_by (GetJobsSortBy | Unset):
        domino_stats_sort_field_name (str | Unset):
        ascending (bool | Unset):
        show_archived (bool | Unset):
        status_filter (GetJobsStatusFilter | Unset):
        tag_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetJobsResponse400 | GetJobsResponse404 | GetJobsResponse500 | PaginatedJobEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            domino_stats_sort_field_name=domino_stats_sort_field_name,
            ascending=ascending,
            show_archived=show_archived,
            status_filter=status_filter,
            tag_filter=tag_filter,
        )
    ).parsed
