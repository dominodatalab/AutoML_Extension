from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_cost_metrics_v1 import CloudCostMetricsV1
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.free_form_json_object_v1 import FreeFormJsonObjectV1
from ...models.get_cloud_cost_response_400 import GetCloudCostResponse400
from ...models.get_cloud_cost_response_404 import GetCloudCostResponse404
from ...models.get_cloud_cost_response_500 import GetCloudCostResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window: str,
    cost_metric: CloudCostMetricsV1 | Unset = UNSET,
    aggregate: str | Unset = UNSET,
    filter_invoice_entity_i_ds: str | Unset = UNSET,
    filter_account_i_ds: str | Unset = UNSET,
    filter_providers: str | Unset = UNSET,
    filter_providers_id: str | Unset = UNSET,
    filter_services: str | Unset = UNSET,
    filter_categories: str | Unset = UNSET,
    filter_labels: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    json_cost_metric: str | Unset = UNSET
    if not isinstance(cost_metric, Unset):
        json_cost_metric = cost_metric.value

    params["costMetric"] = json_cost_metric

    params["aggregate"] = aggregate

    params["filterInvoiceEntityIDs"] = filter_invoice_entity_i_ds

    params["filterAccountIDs"] = filter_account_i_ds

    params["filterProviders"] = filter_providers

    params["filterProvidersID"] = filter_providers_id

    params["filterServices"] = filter_services

    params["filterCategories"] = filter_categories

    params["filterLabels"] = filter_labels

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cost/v1/cloudCost",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
    | None
):
    if response.status_code == 200:
        response_200 = FreeFormJsonObjectV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCloudCostResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetCloudCostResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetCloudCostResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
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
    window: str,
    cost_metric: CloudCostMetricsV1 | Unset = UNSET,
    aggregate: str | Unset = UNSET,
    filter_invoice_entity_i_ds: str | Unset = UNSET,
    filter_account_i_ds: str | Unset = UNSET,
    filter_providers: str | Unset = UNSET,
    filter_providers_id: str | Unset = UNSET,
    filter_services: str | Unset = UNSET,
    filter_categories: str | Unset = UNSET,
    filter_labels: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
]:
    """Get the cloud cost data

     Retrieve cloud cost

    Args:
        window (str):
        cost_metric (CloudCostMetricsV1 | Unset): Determines which cloud cost metric type will be
            returned
        aggregate (str | Unset):
        filter_invoice_entity_i_ds (str | Unset):
        filter_account_i_ds (str | Unset):
        filter_providers (str | Unset):
        filter_providers_id (str | Unset):
        filter_services (str | Unset):
        filter_categories (str | Unset):
        filter_labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | FreeFormJsonObjectV1 | GetCloudCostResponse400 | GetCloudCostResponse404 | GetCloudCostResponse500]
    """

    kwargs = _get_kwargs(
        window=window,
        cost_metric=cost_metric,
        aggregate=aggregate,
        filter_invoice_entity_i_ds=filter_invoice_entity_i_ds,
        filter_account_i_ds=filter_account_i_ds,
        filter_providers=filter_providers,
        filter_providers_id=filter_providers_id,
        filter_services=filter_services,
        filter_categories=filter_categories,
        filter_labels=filter_labels,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    cost_metric: CloudCostMetricsV1 | Unset = UNSET,
    aggregate: str | Unset = UNSET,
    filter_invoice_entity_i_ds: str | Unset = UNSET,
    filter_account_i_ds: str | Unset = UNSET,
    filter_providers: str | Unset = UNSET,
    filter_providers_id: str | Unset = UNSET,
    filter_services: str | Unset = UNSET,
    filter_categories: str | Unset = UNSET,
    filter_labels: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
    | None
):
    """Get the cloud cost data

     Retrieve cloud cost

    Args:
        window (str):
        cost_metric (CloudCostMetricsV1 | Unset): Determines which cloud cost metric type will be
            returned
        aggregate (str | Unset):
        filter_invoice_entity_i_ds (str | Unset):
        filter_account_i_ds (str | Unset):
        filter_providers (str | Unset):
        filter_providers_id (str | Unset):
        filter_services (str | Unset):
        filter_categories (str | Unset):
        filter_labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | FreeFormJsonObjectV1 | GetCloudCostResponse400 | GetCloudCostResponse404 | GetCloudCostResponse500
    """

    return sync_detailed(
        client=client,
        window=window,
        cost_metric=cost_metric,
        aggregate=aggregate,
        filter_invoice_entity_i_ds=filter_invoice_entity_i_ds,
        filter_account_i_ds=filter_account_i_ds,
        filter_providers=filter_providers,
        filter_providers_id=filter_providers_id,
        filter_services=filter_services,
        filter_categories=filter_categories,
        filter_labels=filter_labels,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    cost_metric: CloudCostMetricsV1 | Unset = UNSET,
    aggregate: str | Unset = UNSET,
    filter_invoice_entity_i_ds: str | Unset = UNSET,
    filter_account_i_ds: str | Unset = UNSET,
    filter_providers: str | Unset = UNSET,
    filter_providers_id: str | Unset = UNSET,
    filter_services: str | Unset = UNSET,
    filter_categories: str | Unset = UNSET,
    filter_labels: str | Unset = UNSET,
) -> Response[
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
]:
    """Get the cloud cost data

     Retrieve cloud cost

    Args:
        window (str):
        cost_metric (CloudCostMetricsV1 | Unset): Determines which cloud cost metric type will be
            returned
        aggregate (str | Unset):
        filter_invoice_entity_i_ds (str | Unset):
        filter_account_i_ds (str | Unset):
        filter_providers (str | Unset):
        filter_providers_id (str | Unset):
        filter_services (str | Unset):
        filter_categories (str | Unset):
        filter_labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | FreeFormJsonObjectV1 | GetCloudCostResponse400 | GetCloudCostResponse404 | GetCloudCostResponse500]
    """

    kwargs = _get_kwargs(
        window=window,
        cost_metric=cost_metric,
        aggregate=aggregate,
        filter_invoice_entity_i_ds=filter_invoice_entity_i_ds,
        filter_account_i_ds=filter_account_i_ds,
        filter_providers=filter_providers,
        filter_providers_id=filter_providers_id,
        filter_services=filter_services,
        filter_categories=filter_categories,
        filter_labels=filter_labels,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window: str,
    cost_metric: CloudCostMetricsV1 | Unset = UNSET,
    aggregate: str | Unset = UNSET,
    filter_invoice_entity_i_ds: str | Unset = UNSET,
    filter_account_i_ds: str | Unset = UNSET,
    filter_providers: str | Unset = UNSET,
    filter_providers_id: str | Unset = UNSET,
    filter_services: str | Unset = UNSET,
    filter_categories: str | Unset = UNSET,
    filter_labels: str | Unset = UNSET,
) -> (
    FailureEnvelopeV1
    | FreeFormJsonObjectV1
    | GetCloudCostResponse400
    | GetCloudCostResponse404
    | GetCloudCostResponse500
    | None
):
    """Get the cloud cost data

     Retrieve cloud cost

    Args:
        window (str):
        cost_metric (CloudCostMetricsV1 | Unset): Determines which cloud cost metric type will be
            returned
        aggregate (str | Unset):
        filter_invoice_entity_i_ds (str | Unset):
        filter_account_i_ds (str | Unset):
        filter_providers (str | Unset):
        filter_providers_id (str | Unset):
        filter_services (str | Unset):
        filter_categories (str | Unset):
        filter_labels (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | FreeFormJsonObjectV1 | GetCloudCostResponse400 | GetCloudCostResponse404 | GetCloudCostResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            window=window,
            cost_metric=cost_metric,
            aggregate=aggregate,
            filter_invoice_entity_i_ds=filter_invoice_entity_i_ds,
            filter_account_i_ds=filter_account_i_ds,
            filter_providers=filter_providers,
            filter_providers_id=filter_providers_id,
            filter_services=filter_services,
            filter_categories=filter_categories,
            filter_labels=filter_labels,
        )
    ).parsed
