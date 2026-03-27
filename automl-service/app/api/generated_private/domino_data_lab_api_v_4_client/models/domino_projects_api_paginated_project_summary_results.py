from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_summary import DominoProjectsApiProjectSummary


T = TypeVar("T", bound="DominoProjectsApiPaginatedProjectSummaryResults")


@_attrs_define
class DominoProjectsApiPaginatedProjectSummaryResults:
    """
    Attributes:
        page (list[DominoProjectsApiProjectSummary]):
        total_matches (int):
    """

    page: list[DominoProjectsApiProjectSummary]
    total_matches: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = []
        for page_item_data in self.page:
            page_item = page_item_data.to_dict()
            page.append(page_item)

        total_matches = self.total_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "totalMatches": total_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_summary import DominoProjectsApiProjectSummary

        d = dict(src_dict)
        page = []
        _page = d.pop("page")
        for page_item_data in _page:
            page_item = DominoProjectsApiProjectSummary.from_dict(page_item_data)

            page.append(page_item)

        total_matches = d.pop("totalMatches")

        domino_projects_api_paginated_project_summary_results = cls(
            page=page,
            total_matches=total_matches,
        )

        domino_projects_api_paginated_project_summary_results.additional_properties = d
        return domino_projects_api_paginated_project_summary_results

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
