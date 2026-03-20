from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_views_timeseries_users import AppViewsTimeseriesUsers


T = TypeVar("T", bound="AppViewsTimeseries")


@_attrs_define
class AppViewsTimeseries:
    """
    Attributes:
        count (int):
        timestamp (float):
        users (AppViewsTimeseriesUsers):
    """

    count: int
    timestamp: float
    users: AppViewsTimeseriesUsers
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        timestamp = self.timestamp

        users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "timestamp": timestamp,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_views_timeseries_users import AppViewsTimeseriesUsers

        d = dict(src_dict)
        count = d.pop("count")

        timestamp = d.pop("timestamp")

        users = AppViewsTimeseriesUsers.from_dict(d.pop("users"))

        app_views_timeseries = cls(
            count=count,
            timestamp=timestamp,
            users=users,
        )

        app_views_timeseries.additional_properties = d
        return app_views_timeseries

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
