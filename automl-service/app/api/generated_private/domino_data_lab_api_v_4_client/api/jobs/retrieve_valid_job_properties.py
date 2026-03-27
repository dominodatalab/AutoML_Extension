from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_jobs_interface_valid_job_properties import DominoJobsInterfaceValidJobProperties
from ...models.retrieve_valid_job_properties_response_409 import RetrieveValidJobPropertiesResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    page_size: float | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_page_size: float | None | Unset
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["pageSize"] = json_page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs/{project_id}/retrieveValidProperties".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409 | None:
    if response.status_code == 200:
        response_200 = DominoJobsInterfaceValidJobProperties.from_dict(response.json())

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
        response_409 = RetrieveValidJobPropertiesResponse409.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409]:
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
    page_size: float | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409]:
    """Retrieves valid properties that can be used for starting a job, like available hardware tiers,
    environments, etc.

    Args:
        project_id (str):
        page_size (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409 | None:
    """Retrieves valid properties that can be used for starting a job, like available hardware tiers,
    environments, etc.

    Args:
        project_id (str):
        page_size (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
) -> Response[DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409]:
    """Retrieves valid properties that can be used for starting a job, like available hardware tiers,
    environments, etc.

    Args:
        project_id (str):
        page_size (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: float | None | Unset = UNSET,
) -> DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409 | None:
    """Retrieves valid properties that can be used for starting a job, like available hardware tiers,
    environments, etc.

    Args:
        project_id (str):
        page_size (float | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoJobsInterfaceValidJobProperties | RetrieveValidJobPropertiesResponse409
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            page_size=page_size,
        )
    ).parsed
