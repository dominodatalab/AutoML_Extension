from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_project_by_id_response_400 import GetProjectByIdResponse400
from ...models.get_project_by_id_response_404 import GetProjectByIdResponse404
from ...models.get_project_by_id_response_500 import GetProjectByIdResponse500
from ...models.project_envelope_v1 import ProjectEnvelopeV1
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/projects/v1/projects/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
    | None
):
    if response.status_code == 200:
        response_200 = ProjectEnvelopeV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectByIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetProjectByIdResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetProjectByIdResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
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
) -> Response[
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
]:
    """Get Project by Id

     Get project by id. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectByIdResponse400 | GetProjectByIdResponse404 | GetProjectByIdResponse500 | ProjectEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
    | None
):
    """Get Project by Id

     Get project by id. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectByIdResponse400 | GetProjectByIdResponse404 | GetProjectByIdResponse500 | ProjectEnvelopeV1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
]:
    """Get Project by Id

     Get project by id. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetProjectByIdResponse400 | GetProjectByIdResponse404 | GetProjectByIdResponse500 | ProjectEnvelopeV1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetProjectByIdResponse400
    | GetProjectByIdResponse404
    | GetProjectByIdResponse500
    | ProjectEnvelopeV1
    | None
):
    """Get Project by Id

     Get project by id. Required permissions: `ListProject`

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetProjectByIdResponse400 | GetProjectByIdResponse404 | GetProjectByIdResponse500 | ProjectEnvelopeV1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
