from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_connection_snippet_language import (
    DominoDatasetrwApiDatasetRwConnectionSnippetLanguage,
)

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwConnectionSnippet")


@_attrs_define
class DominoDatasetrwApiDatasetRwConnectionSnippet:
    """
    Attributes:
        language (DominoDatasetrwApiDatasetRwConnectionSnippetLanguage):
        snippet (str):
    """

    language: DominoDatasetrwApiDatasetRwConnectionSnippetLanguage
    snippet: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language.value

        snippet = self.snippet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "snippet": snippet,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = DominoDatasetrwApiDatasetRwConnectionSnippetLanguage(d.pop("language"))

        snippet = d.pop("snippet")

        domino_datasetrw_api_dataset_rw_connection_snippet = cls(
            language=language,
            snippet=snippet,
        )

        domino_datasetrw_api_dataset_rw_connection_snippet.additional_properties = d
        return domino_datasetrw_api_dataset_rw_connection_snippet

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
