from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_apiserverutils_pagination_pagination_filter_sort_order import (
    DominoApiserverutilsPaginationPaginationFilterSortOrder,
)

T = TypeVar("T", bound="DominoApiserverutilsPaginationPaginationFilter")


@_attrs_define
class DominoApiserverutilsPaginationPaginationFilter:
    """
    Attributes:
        page_size (int):
        page_number (int):
        sort_order (DominoApiserverutilsPaginationPaginationFilterSortOrder):
    """

    page_size: int
    page_number: int
    sort_order: DominoApiserverutilsPaginationPaginationFilterSortOrder
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        page_number = self.page_number

        sort_order = self.sort_order.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageSize": page_size,
                "pageNumber": page_number,
                "sortOrder": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize")

        page_number = d.pop("pageNumber")

        sort_order = DominoApiserverutilsPaginationPaginationFilterSortOrder(d.pop("sortOrder"))

        domino_apiserverutils_pagination_pagination_filter = cls(
            page_size=page_size,
            page_number=page_number,
            sort_order=sort_order,
        )

        domino_apiserverutils_pagination_pagination_filter.additional_properties = d
        return domino_apiserverutils_pagination_pagination_filter

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
