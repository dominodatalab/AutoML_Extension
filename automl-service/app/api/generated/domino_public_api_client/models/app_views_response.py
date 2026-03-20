from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_views_response_users import AppViewsResponseUsers
    from ..models.app_views_response_versions_item import AppViewsResponseVersionsItem
    from ..models.app_views_timeseries import AppViewsTimeseries


T = TypeVar("T", bound="AppViewsResponse")


@_attrs_define
class AppViewsResponse:
    """
    Attributes:
        count (int):
        timeseries (list[AppViewsTimeseries]):
        users (AppViewsResponseUsers):
        versions (list[AppViewsResponseVersionsItem]):
    """

    count: int
    timeseries: list[AppViewsTimeseries]
    users: AppViewsResponseUsers
    versions: list[AppViewsResponseVersionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        timeseries = []
        for timeseries_item_data in self.timeseries:
            timeseries_item = timeseries_item_data.to_dict()
            timeseries.append(timeseries_item)

        users = self.users.to_dict()

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "timeseries": timeseries,
                "users": users,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_views_response_users import AppViewsResponseUsers
        from ..models.app_views_response_versions_item import AppViewsResponseVersionsItem
        from ..models.app_views_timeseries import AppViewsTimeseries

        d = dict(src_dict)
        count = d.pop("count")

        timeseries = []
        _timeseries = d.pop("timeseries")
        for timeseries_item_data in _timeseries:
            timeseries_item = AppViewsTimeseries.from_dict(timeseries_item_data)

            timeseries.append(timeseries_item)

        users = AppViewsResponseUsers.from_dict(d.pop("users"))

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = AppViewsResponseVersionsItem.from_dict(versions_item_data)

            versions.append(versions_item)

        app_views_response = cls(
            count=count,
            timeseries=timeseries,
            users=users,
            versions=versions,
        )

        app_views_response.additional_properties = d
        return app_views_response

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
