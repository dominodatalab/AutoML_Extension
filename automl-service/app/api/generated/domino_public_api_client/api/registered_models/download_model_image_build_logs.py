from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_model_image_build_logs_response_404 import DownloadModelImageBuildLogsResponse404
from ...models.download_model_image_build_logs_response_500 import DownloadModelImageBuildLogsResponse500
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...types import Response


def _get_kwargs(
    model_name: str,
    model_version: str,
    build_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/{model_name}/versions/{model_version}/builds/{build_id}/logs/download".format(
            model_name=quote(str(model_name), safe=""),
            model_version=quote(str(model_version), safe=""),
            build_id=quote(str(build_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1 | None:
    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DownloadModelImageBuildLogsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = DownloadModelImageBuildLogsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1]:
    """Download model image build logs

     Download model image build logs as new-line-separated JSON

    Args:
        model_name (str):
        model_version (str):
        build_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1 | None:
    """Download model image build logs

     Download model image build logs as new-line-separated JSON

    Args:
        model_name (str):
        model_version (str):
        build_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1
    """

    return sync_detailed(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1]:
    """Download model image build logs

     Download model image build logs as new-line-separated JSON

    Args:
        model_name (str):
        model_version (str):
        build_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1 | None:
    """Download model image build logs

     Download model image build logs as new-line-separated JSON

    Args:
        model_name (str):
        model_version (str):
        build_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadModelImageBuildLogsResponse404 | DownloadModelImageBuildLogsResponse500 | FailureEnvelopeV1
    """

    return (
        await asyncio_detailed(
            model_name=model_name,
            model_version=model_version,
            build_id=build_id,
            client=client,
        )
    ).parsed
