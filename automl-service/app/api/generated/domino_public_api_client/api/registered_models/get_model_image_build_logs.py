from __future__ import annotations
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_model_image_build_logs_response_404 import GetModelImageBuildLogsResponse404
from ...models.get_model_image_build_logs_response_500 import GetModelImageBuildLogsResponse500
from ...models.model_image_build_logs_v1 import ModelImageBuildLogsV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    since_time_nano: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sinceTimeNano"] = since_time_nano

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/{model_name}/versions/{model_version}/builds/{build_id}/logs".format(
            model_name=quote(str(model_name), safe=""),
            model_version=quote(str(model_version), safe=""),
            build_id=quote(str(build_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetModelImageBuildLogsResponse404
    | GetModelImageBuildLogsResponse500
    | ModelImageBuildLogsV1
    | None
):
    if response.status_code == 200:
        response_200 = ModelImageBuildLogsV1.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetModelImageBuildLogsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetModelImageBuildLogsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1
]:
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
    since_time_nano: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1
]:
    """Get model image build logs

     Get model image build logs for streaming

    Args:
        model_name (str):
        model_version (str):
        build_id (str):
        since_time_nano (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
        since_time_nano=since_time_nano,
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
    since_time_nano: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelImageBuildLogsResponse404
    | GetModelImageBuildLogsResponse500
    | ModelImageBuildLogsV1
    | None
):
    """Get model image build logs

     Get model image build logs for streaming

    Args:
        model_name (str):
        model_version (str):
        build_id (str):
        since_time_nano (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1
    """

    return sync_detailed(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
        client=client,
        since_time_nano=since_time_nano,
    ).parsed


async def asyncio_detailed(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: int | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1
]:
    """Get model image build logs

     Get model image build logs for streaming

    Args:
        model_name (str):
        model_version (str):
        build_id (str):
        since_time_nano (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1]
    """

    kwargs = _get_kwargs(
        model_name=model_name,
        model_version=model_version,
        build_id=build_id,
        since_time_nano=since_time_nano,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_name: str,
    model_version: str,
    build_id: str,
    *,
    client: AuthenticatedClient | Client,
    since_time_nano: int | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | GetModelImageBuildLogsResponse404
    | GetModelImageBuildLogsResponse500
    | ModelImageBuildLogsV1
    | None
):
    """Get model image build logs

     Get model image build logs for streaming

    Args:
        model_name (str):
        model_version (str):
        build_id (str):
        since_time_nano (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetModelImageBuildLogsResponse404 | GetModelImageBuildLogsResponse500 | ModelImageBuildLogsV1
    """

    return (
        await asyncio_detailed(
            model_name=model_name,
            model_version=model_version,
            build_id=build_id,
            client=client,
            since_time_nano=since_time_nano,
        )
    ).parsed
