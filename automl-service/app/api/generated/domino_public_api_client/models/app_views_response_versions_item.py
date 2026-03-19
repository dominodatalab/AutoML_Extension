from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_views_response_versions_item_users import AppViewsResponseVersionsItemUsers
    from ..models.app_views_timeseries import AppViewsTimeseries


T = TypeVar("T", bound="AppViewsResponseVersionsItem")


@_attrs_define
class AppViewsResponseVersionsItem:
    """
    Attributes:
        count (int):
        id (str):
        timeseries (list[AppViewsTimeseries]):
        users (AppViewsResponseVersionsItemUsers):
    """

    count: int
    id: str
    timeseries: list[AppViewsTimeseries]
    users: AppViewsResponseVersionsItemUsers
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        id = self.id

        timeseries = []
        for timeseries_item_data in self.timeseries:
            timeseries_item = timeseries_item_data.to_dict()
            timeseries.append(timeseries_item)

        users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "id": id,
                "timeseries": timeseries,
                "users": users,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_views_response_versions_item_users import AppViewsResponseVersionsItemUsers
        from ..models.app_views_timeseries import AppViewsTimeseries

        d = dict(src_dict)
        count = d.pop("count")

        id = d.pop("id")

        timeseries = []
        _timeseries = d.pop("timeseries")
        for timeseries_item_data in _timeseries:
            timeseries_item = AppViewsTimeseries.from_dict(timeseries_item_data)

            timeseries.append(timeseries_item)

        users = AppViewsResponseVersionsItemUsers.from_dict(d.pop("users"))

        app_views_response_versions_item = cls(
            count=count,
            id=id,
            timeseries=timeseries,
            users=users,
        )

        app_views_response_versions_item.additional_properties = d
        return app_views_response_versions_item

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
