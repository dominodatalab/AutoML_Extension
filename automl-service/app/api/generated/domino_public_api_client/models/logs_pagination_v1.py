from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogsPaginationV1")


@_attrs_define
class LogsPaginationV1:
    """
    Attributes:
        limit (int): Max number of log messages to retrieve. Example: 10.
        latest_time_nano (str | Unset): Time of last log. Can be used to specify only logs after a certain time.
            Example: 1647051415275957459.
    """

    limit: int
    latest_time_nano: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        latest_time_nano = self.latest_time_nano

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
            }
        )
        if latest_time_nano is not UNSET:
            field_dict["latestTimeNano"] = latest_time_nano

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        latest_time_nano = d.pop("latestTimeNano", UNSET)

        logs_pagination_v1 = cls(
            limit=limit,
            latest_time_nano=latest_time_nano,
        )

        logs_pagination_v1.additional_properties = d
        return logs_pagination_v1

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
