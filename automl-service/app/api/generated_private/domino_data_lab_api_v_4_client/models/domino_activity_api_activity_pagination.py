from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiActivityPagination")


@_attrs_define
class DominoActivityApiActivityPagination:
    """
    Attributes:
        page_size (int):
        latest_time_stamp (int):
    """

    page_size: int
    latest_time_stamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        latest_time_stamp = self.latest_time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pageSize": page_size,
                "latestTimeStamp": latest_time_stamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize")

        latest_time_stamp = d.pop("latestTimeStamp")

        domino_activity_api_activity_pagination = cls(
            page_size=page_size,
            latest_time_stamp=latest_time_stamp,
        )

        domino_activity_api_activity_pagination.additional_properties = d
        return domino_activity_api_activity_pagination

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
