from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_notifications_priority import DominoNotificationsPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNotificationsHasNotifications")


@_attrs_define
class DominoNotificationsHasNotifications:
    """
    Attributes:
        unread (bool):
        priority (DominoNotificationsPriority | Unset):
    """

    unread: bool
    priority: DominoNotificationsPriority | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unread = self.unread

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unread": unread,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unread = d.pop("unread")

        _priority = d.pop("priority", UNSET)
        priority: DominoNotificationsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = DominoNotificationsPriority(_priority)

        domino_notifications_has_notifications = cls(
            unread=unread,
            priority=priority,
        )

        domino_notifications_has_notifications.additional_properties = d
        return domino_notifications_has_notifications

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
