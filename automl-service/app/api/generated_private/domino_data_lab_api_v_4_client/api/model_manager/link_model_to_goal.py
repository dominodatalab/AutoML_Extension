from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_modelmanager_api_model_goal import DominoModelmanagerApiModelGoal
from ...models.domino_modelmanager_web_linkmodel_to_goal import DominoModelmanagerWebLinkmodelToGoal
from ...types import Response


def _get_kwargs(
    model_version_id: str,
    *,
    body: DominoModelmanagerWebLinkmodelToGoal,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/modelManager/{model_version_id}/linkModeltoGoal".format(
            model_version_id=quote(str(model_version_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DominoModelmanagerApiModelGoal.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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

    if response.status_code == 500:
        response_500 = DominoApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoModelmanagerWebLinkmodelToGoal,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]]:
    """Link model API to a goal

    Args:
        model_version_id (str):
        body (DominoModelmanagerWebLinkmodelToGoal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoModelmanagerWebLinkmodelToGoal,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal] | None:
    """Link model API to a goal

    Args:
        model_version_id (str):
        body (DominoModelmanagerWebLinkmodelToGoal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]
    """

    return sync_detailed(
        model_version_id=model_version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoModelmanagerWebLinkmodelToGoal,
) -> Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]]:
    """Link model API to a goal

    Args:
        model_version_id (str):
        body (DominoModelmanagerWebLinkmodelToGoal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]]
    """

    kwargs = _get_kwargs(
        model_version_id=model_version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    model_version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DominoModelmanagerWebLinkmodelToGoal,
) -> DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal] | None:
    """Link model API to a goal

    Args:
        model_version_id (str):
        body (DominoModelmanagerWebLinkmodelToGoal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | list[DominoModelmanagerApiModelGoal]
    """

    return (
        await asyncio_detailed(
            model_version_id=model_version_id,
            client=client,
            body=body,
        )
    ).parsed
