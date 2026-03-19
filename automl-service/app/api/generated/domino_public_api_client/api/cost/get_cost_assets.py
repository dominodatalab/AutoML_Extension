from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_assets_envelope_v1 import CostAssetsEnvelopeV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str,
    aggregate: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    accumulate: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params["aggregate"] = aggregate

    params["start"] = start

    params["end"] = end

    params["accumulate"] = accumulate

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cost/v1/asset",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CostAssetsEnvelopeV1 | None:
    if response.status_code == 200:
        response_200 = CostAssetsEnvelopeV1.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CostAssetsEnvelopeV1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    accumulate: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[CostAssetsEnvelopeV1]:
    """Get the asset cost over a time window

     Retrieve asset cost

    Args:
        window (str):
        aggregate (str | Unset):
        start (str | Unset):
        end (str | Unset):
        accumulate (bool | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAssetsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        window=window,
        aggregate=aggregate,
        start=start,
        end=end,
        accumulate=accumulate,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    accumulate: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> CostAssetsEnvelopeV1 | None:
    """Get the asset cost over a time window

     Retrieve asset cost

    Args:
        window (str):
        aggregate (str | Unset):
        start (str | Unset):
        end (str | Unset):
        accumulate (bool | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAssetsEnvelopeV1
    """

    return sync_detailed(
        client=client,
        window=window,
        aggregate=aggregate,
        start=start,
        end=end,
        accumulate=accumulate,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    accumulate: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[CostAssetsEnvelopeV1]:
    """Get the asset cost over a time window

     Retrieve asset cost

    Args:
        window (str):
        aggregate (str | Unset):
        start (str | Unset):
        end (str | Unset):
        accumulate (bool | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostAssetsEnvelopeV1]
    """

    kwargs = _get_kwargs(
        window=window,
        aggregate=aggregate,
        start=start,
        end=end,
        accumulate=accumulate,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    aggregate: str | Unset = UNSET,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    accumulate: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> CostAssetsEnvelopeV1 | None:
    """Get the asset cost over a time window

     Retrieve asset cost

    Args:
        window (str):
        aggregate (str | Unset):
        start (str | Unset):
        end (str | Unset):
        accumulate (bool | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostAssetsEnvelopeV1
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            aggregate=aggregate,
            start=start,
            end=end,
            accumulate=accumulate,
            filter_=filter_,
        )
    ).parsed
