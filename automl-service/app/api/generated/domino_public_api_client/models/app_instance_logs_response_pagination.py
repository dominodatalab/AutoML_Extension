from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AppInstanceLogsResponsePagination")


@_attrs_define
class AppInstanceLogsResponsePagination:
    """
    Attributes:
        latest_time (str):
        limit (int):
        offset (int):
    """

    latest_time: str
    limit: int
    offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_time = self.latest_time

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latestTime": latest_time,
                "limit": limit,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_time = d.pop("latestTime")

        limit = d.pop("limit")

        offset = d.pop("offset")

        app_instance_logs_response_pagination = cls(
            latest_time=latest_time,
            limit=limit,
            offset=offset,
        )

        app_instance_logs_response_pagination.additional_properties = d
        return app_instance_logs_response_pagination

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
