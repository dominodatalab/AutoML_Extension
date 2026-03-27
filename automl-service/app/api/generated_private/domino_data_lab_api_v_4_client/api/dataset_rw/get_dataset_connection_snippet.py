from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domino_api_error_response import DominoApiErrorResponse
from ...models.domino_datasetrw_api_dataset_rw_connection_snippet import DominoDatasetrwApiDatasetRwConnectionSnippet
from ...models.get_dataset_connection_snippet_language import GetDatasetConnectionSnippetLanguage
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    language: GetDatasetConnectionSnippetLanguage,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasetrw/dataset/{dataset_id}/connection-snippets/{language}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            language=quote(str(language), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet | None:
    if response.status_code == 200:
        response_200 = DominoDatasetrwApiDatasetRwConnectionSnippet.from_dict(response.json())

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
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    language: GetDatasetConnectionSnippetLanguage,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet]:
    """Gets dataset's current dataset's grants details

    Args:
        dataset_id (str):
        language (GetDatasetConnectionSnippetLanguage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    language: GetDatasetConnectionSnippetLanguage,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet | None:
    """Gets dataset's current dataset's grants details

    Args:
        dataset_id (str):
        language (GetDatasetConnectionSnippetLanguage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet
    """

    return sync_detailed(
        dataset_id=dataset_id,
        language=language,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    language: GetDatasetConnectionSnippetLanguage,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet]:
    """Gets dataset's current dataset's grants details

    Args:
        dataset_id (str):
        language (GetDatasetConnectionSnippetLanguage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    language: GetDatasetConnectionSnippetLanguage,
    *,
    client: AuthenticatedClient | Client,
) -> DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet | None:
    """Gets dataset's current dataset's grants details

    Args:
        dataset_id (str):
        language (GetDatasetConnectionSnippetLanguage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DominoApiErrorResponse | DominoDatasetrwApiDatasetRwConnectionSnippet
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            language=language,
            client=client,
        )
    ).parsed
