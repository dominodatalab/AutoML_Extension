from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failure_envelope_v1 import FailureEnvelopeV1
from ...models.get_unregistered_models_for_experiment_response_400 import GetUnregisteredModelsForExperimentResponse400
from ...models.get_unregistered_models_for_experiment_response_404 import GetUnregisteredModelsForExperimentResponse404
from ...models.get_unregistered_models_for_experiment_response_500 import GetUnregisteredModelsForExperimentResponse500
from ...models.unregistered_models_for_experiment_response_v1 import UnregisteredModelsForExperimentResponseV1
from ...types import Response


def _get_kwargs(
    experiment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registeredmodels/v1/experiments/{experiment_id}/unregistered-models".format(
            experiment_id=quote(str(experiment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
    | None
):
    if response.status_code == 200:
        response_200 = UnregisteredModelsForExperimentResponseV1.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetUnregisteredModelsForExperimentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FailureEnvelopeV1.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = FailureEnvelopeV1.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetUnregisteredModelsForExperimentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetUnregisteredModelsForExperimentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
]:
    """Get unregistered models for an experiment

     Returns models logged from all runs in an experiment that are not yet registered in the model
    registry. This includes MLflow 2 artifact paths (directories) and MLflow 3 logged model IDs with
    their names. The response is organized by run ID.

    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetUnregisteredModelsForExperimentResponse400 | GetUnregisteredModelsForExperimentResponse404 | GetUnregisteredModelsForExperimentResponse500 | UnregisteredModelsForExperimentResponseV1]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
    | None
):
    """Get unregistered models for an experiment

     Returns models logged from all runs in an experiment that are not yet registered in the model
    registry. This includes MLflow 2 artifact paths (directories) and MLflow 3 logged model IDs with
    their names. The response is organized by run ID.

    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetUnregisteredModelsForExperimentResponse400 | GetUnregisteredModelsForExperimentResponse404 | GetUnregisteredModelsForExperimentResponse500 | UnregisteredModelsForExperimentResponseV1
    """

    return sync_detailed(
        experiment_id=experiment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
]:
    """Get unregistered models for an experiment

     Returns models logged from all runs in an experiment that are not yet registered in the model
    registry. This includes MLflow 2 artifact paths (directories) and MLflow 3 logged model IDs with
    their names. The response is organized by run ID.

    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailureEnvelopeV1 | GetUnregisteredModelsForExperimentResponse400 | GetUnregisteredModelsForExperimentResponse404 | GetUnregisteredModelsForExperimentResponse500 | UnregisteredModelsForExperimentResponseV1]
    """

    kwargs = _get_kwargs(
        experiment_id=experiment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    experiment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    FailureEnvelopeV1
    | GetUnregisteredModelsForExperimentResponse400
    | GetUnregisteredModelsForExperimentResponse404
    | GetUnregisteredModelsForExperimentResponse500
    | UnregisteredModelsForExperimentResponseV1
    | None
):
    """Get unregistered models for an experiment

     Returns models logged from all runs in an experiment that are not yet registered in the model
    registry. This includes MLflow 2 artifact paths (directories) and MLflow 3 logged model IDs with
    their names. The response is organized by run ID.

    Args:
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailureEnvelopeV1 | GetUnregisteredModelsForExperimentResponse400 | GetUnregisteredModelsForExperimentResponse404 | GetUnregisteredModelsForExperimentResponse500 | UnregisteredModelsForExperimentResponseV1
    """

    return (
        await asyncio_detailed(
            experiment_id=experiment_id,
            client=client,
        )
    ).parsed
