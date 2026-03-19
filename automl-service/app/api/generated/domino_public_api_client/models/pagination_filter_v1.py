from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationFilterV1")


@_attrs_define
class PaginationFilterV1:
    """
    Attributes:
        page_number (int):
        page_size (int):
        sort_order (str):
    """

    page_number: int
    page_size: int
    sort_order: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_number = self.page_number

        page_size = self.page_size

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageNumber": page_number,
                "pageSize": page_size,
                "sortOrder": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_number = d.pop("pageNumber")

        page_size = d.pop("pageSize")

        sort_order = d.pop("sortOrder")

        pagination_filter_v1 = cls(
            page_number=page_number,
            page_size=page_size,
            sort_order=sort_order,
        )

        pagination_filter_v1.additional_properties = d
        return pagination_filter_v1

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
