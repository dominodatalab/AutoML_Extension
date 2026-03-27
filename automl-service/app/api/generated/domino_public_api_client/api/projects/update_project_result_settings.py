from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.project_results_settings_envelope_v1 import ProjectResultsSettingsEnvelopeV1
from ...models.project_results_settings_v1 import ProjectResultsSettingsV1
from ...models.update_project_result_settings_response_400 import UpdateProjectResultSettingsResponse400
from ...models.update_project_result_settings_response_404 import UpdateProjectResultSettingsResponse404
from ...models.update_project_result_settings_response_500 import UpdateProjectResultSettingsResponse500
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ProjectResultsSettingsV1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/projects/beta/projects/{project_id}/results-settings".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = ProjectResultsSettingsEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateProjectResultSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateProjectResultSettingsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UpdateProjectResultSettingsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
]:
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
    body: ProjectResultsSettingsV1,
) -> Response[
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
]:
    """Update project result settings

    Args:
        project_id (str):
        body (ProjectResultsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ProjectResultsSettingsEnvelopeV1 | UpdateProjectResultSettingsResponse400 | UpdateProjectResultSettingsResponse404 | UpdateProjectResultSettingsResponse500]
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
    body: ProjectResultsSettingsV1,
) -> (
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
    | None
):
    """Update project result settings

    Args:
        project_id (str):
        body (ProjectResultsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ProjectResultsSettingsEnvelopeV1 | UpdateProjectResultSettingsResponse400 | UpdateProjectResultSettingsResponse404 | UpdateProjectResultSettingsResponse500
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
    body: ProjectResultsSettingsV1,
) -> Response[
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
]:
    """Update project result settings

    Args:
        project_id (str):
        body (ProjectResultsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | ProjectResultsSettingsEnvelopeV1 | UpdateProjectResultSettingsResponse400 | UpdateProjectResultSettingsResponse404 | UpdateProjectResultSettingsResponse500]
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
    body: ProjectResultsSettingsV1,
) -> (
    FailureEnvelopeV1
    | ProjectResultsSettingsEnvelopeV1
    | UpdateProjectResultSettingsResponse400
    | UpdateProjectResultSettingsResponse404
    | UpdateProjectResultSettingsResponse500
    | None
):
    """Update project result settings

    Args:
        project_id (str):
        body (ProjectResultsSettingsV1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | ProjectResultsSettingsEnvelopeV1 | UpdateProjectResultSettingsResponse400 | UpdateProjectResultSettingsResponse404 | UpdateProjectResultSettingsResponse500
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
