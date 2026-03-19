from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationMetaPagination")


@_attrs_define
class PaginationMetaPagination:
    """The pagination information for the list of Extensions.

    Attributes:
        limit (int): The number of Extensions returned per page.
        offset (int): The number of Extensions skipped before starting to collect the result set.
        total_count (int): The total number of Extensions returned that match the filters.
    """

    limit: int
    offset: int
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
                "totalCount": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        total_count = d.pop("totalCount")

        pagination_meta_pagination = cls(
            limit=limit,
            offset=offset,
            total_count=total_count,
        )

        pagination_meta_pagination.additional_properties = d
        return pagination_meta_pagination

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
