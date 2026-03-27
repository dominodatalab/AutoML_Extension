from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfacePaginationFilter")


@_attrs_define
class DominoJobsInterfacePaginationFilter:
    """
    Attributes:
        limit (int):
        offset (int):
        latest_time_nano (None | str | Unset):
    """

    limit: int
    offset: int
    latest_time_nano: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        latest_time_nano: None | str | Unset
        if isinstance(self.latest_time_nano, Unset):
            latest_time_nano = UNSET
        else:
            latest_time_nano = self.latest_time_nano

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
            }
        )
        if latest_time_nano is not UNSET:
            field_dict["latestTimeNano"] = latest_time_nano

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        offset = d.pop("offset")

        def _parse_latest_time_nano(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_time_nano = _parse_latest_time_nano(d.pop("latestTimeNano", UNSET))

        domino_jobs_interface_pagination_filter = cls(
            limit=limit,
            offset=offset,
            latest_time_nano=latest_time_nano,
        )

        domino_jobs_interface_pagination_filter.additional_properties = d
        return domino_jobs_interface_pagination_filter

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
