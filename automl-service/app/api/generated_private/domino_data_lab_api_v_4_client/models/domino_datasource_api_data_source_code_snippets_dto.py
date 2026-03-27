from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_datasource_api_data_source_code_snippets_dto_snippets_by_languages import (
        DominoDatasourceApiDataSourceCodeSnippetsDtoSnippetsByLanguages,
    )


T = TypeVar("T", bound="DominoDatasourceApiDataSourceCodeSnippetsDto")


@_attrs_define
class DominoDatasourceApiDataSourceCodeSnippetsDto:
    """
    Attributes:
        snippets_by_languages (DominoDatasourceApiDataSourceCodeSnippetsDtoSnippetsByLanguages):
    """

    snippets_by_languages: DominoDatasourceApiDataSourceCodeSnippetsDtoSnippetsByLanguages
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snippets_by_languages = self.snippets_by_languages.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snippetsByLanguages": snippets_by_languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasource_api_data_source_code_snippets_dto_snippets_by_languages import (
            DominoDatasourceApiDataSourceCodeSnippetsDtoSnippetsByLanguages,
        )

        d = dict(src_dict)
        snippets_by_languages = DominoDatasourceApiDataSourceCodeSnippetsDtoSnippetsByLanguages.from_dict(
            d.pop("snippetsByLanguages")
        )

        domino_datasource_api_data_source_code_snippets_dto = cls(
            snippets_by_languages=snippets_by_languages,
        )

        domino_datasource_api_data_source_code_snippets_dto.additional_properties = d
        return domino_datasource_api_data_source_code_snippets_dto

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
