from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_jobs_interface_resolved_job_properties import DominoJobsInterfaceResolvedJobProperties
from ...models.domino_jobs_web_resolve_default_job_properties_request import (
    DominoJobsWebResolveDefaultJobPropertiesRequest,
)
from ...models.resolve_job_defaults_response_409 import ResolveJobDefaultsResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: DominoJobsWebResolveDefaultJobPropertiesRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jobs/{project_id}/resolveJobDefaults".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409 | None:
    if response.status_code == 200:
        response_200 = DominoJobsInterfaceResolvedJobProperties.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ResolveJobDefaultsResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409]:
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
    body: DominoJobsWebResolveDefaultJobPropertiesRequest | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409]:
    """Resolves default values used to create a Job. Allows all properties to be known externally before
    Job creation

    Args:
        project_id (str):
        body (DominoJobsWebResolveDefaultJobPropertiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409]
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
    body: DominoJobsWebResolveDefaultJobPropertiesRequest | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409 | None:
    """Resolves default values used to create a Job. Allows all properties to be known externally before
    Job creation

    Args:
        project_id (str):
        body (DominoJobsWebResolveDefaultJobPropertiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409
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
    body: DominoJobsWebResolveDefaultJobPropertiesRequest | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409]:
    """Resolves default values used to create a Job. Allows all properties to be known externally before
    Job creation

    Args:
        project_id (str):
        body (DominoJobsWebResolveDefaultJobPropertiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409]
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
    body: DominoJobsWebResolveDefaultJobPropertiesRequest | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409 | None:
    """Resolves default values used to create a Job. Allows all properties to be known externally before
    Job creation

    Args:
        project_id (str):
        body (DominoJobsWebResolveDefaultJobPropertiesRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceResolvedJobProperties | ResolveJobDefaultsResponse409
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
