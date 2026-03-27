from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_activity_api_activity import DominoActivityApiActivity
    from ..models.domino_activity_api_activity_pagination import DominoActivityApiActivityPagination


T = TypeVar("T", bound="DominoActivityApiActivityStream")


@_attrs_define
class DominoActivityApiActivityStream:
    """
    Attributes:
        activity (list[DominoActivityApiActivity]):
        pagination (DominoActivityApiActivityPagination):
    """

    activity: list[DominoActivityApiActivity]
    pagination: DominoActivityApiActivityPagination
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = []
        for activity_item_data in self.activity:
            activity_item = activity_item_data.to_dict()
            activity.append(activity_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity": activity,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_activity import DominoActivityApiActivity
        from ..models.domino_activity_api_activity_pagination import DominoActivityApiActivityPagination

        d = dict(src_dict)
        activity = []
        _activity = d.pop("activity")
        for activity_item_data in _activity:
            activity_item = DominoActivityApiActivity.from_dict(activity_item_data)

            activity.append(activity_item)

        pagination = DominoActivityApiActivityPagination.from_dict(d.pop("pagination"))

        domino_activity_api_activity_stream = cls(
            activity=activity,
            pagination=pagination,
        )

        domino_activity_api_activity_stream.additional_properties = d
        return domino_activity_api_activity_stream

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
