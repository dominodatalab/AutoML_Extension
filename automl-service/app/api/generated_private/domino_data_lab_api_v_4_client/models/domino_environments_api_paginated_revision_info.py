from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoEnvironmentsApiPaginatedRevisionInfo")


@_attrs_define
class DominoEnvironmentsApiPaginatedRevisionInfo:
    """
    Attributes:
        total_pages (int):
        current_page (int):
        page_size (int):
    """

    total_pages: int
    current_page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_pages = self.total_pages

        current_page = self.current_page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalPages": total_pages,
                "currentPage": current_page,
                "pageSize": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_pages = d.pop("totalPages")

        current_page = d.pop("currentPage")

        page_size = d.pop("pageSize")

        domino_environments_api_paginated_revision_info = cls(
            total_pages=total_pages,
            current_page=current_page,
            page_size=page_size,
        )

        domino_environments_api_paginated_revision_info.additional_properties = d
        return domino_environments_api_paginated_revision_info

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
