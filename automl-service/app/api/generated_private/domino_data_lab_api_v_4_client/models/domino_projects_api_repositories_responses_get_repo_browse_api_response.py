from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_responses_browse_repo_browser_entry_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO,
    )
    from ..models.domino_projects_api_repositories_responses_browse_repo_browser_summary_dto import (
        DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiRepositoriesResponsesGetRepoBrowseApiResponse")


@_attrs_define
class DominoProjectsApiRepositoriesResponsesGetRepoBrowseApiResponse:
    """
    Attributes:
        items (list[DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO]):
        summary (DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO):
    """

    items: list[DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO]
    summary: DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_responses_browse_repo_browser_entry_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO,
        )
        from ..models.domino_projects_api_repositories_responses_browse_repo_browser_summary_dto import (
            DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserEntryDTO.from_dict(items_item_data)

            items.append(items_item)

        summary = DominoProjectsApiRepositoriesResponsesBrowseRepoBrowserSummaryDTO.from_dict(d.pop("summary"))

        domino_projects_api_repositories_responses_get_repo_browse_api_response = cls(
            items=items,
            summary=summary,
        )

        domino_projects_api_repositories_responses_get_repo_browse_api_response.additional_properties = d
        return domino_projects_api_repositories_responses_get_repo_browse_api_response

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
