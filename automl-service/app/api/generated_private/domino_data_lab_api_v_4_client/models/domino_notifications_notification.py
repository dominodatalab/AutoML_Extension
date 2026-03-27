from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_notifications_priority import DominoNotificationsPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_notifications_origin import DominoNotificationsOrigin


T = TypeVar("T", bound="DominoNotificationsNotification")


@_attrs_define
class DominoNotificationsNotification:
    """
    Attributes:
        id (str): Message ID, not displayed anywhere Example: abc123.
        title (str):  Example: Important notification.
        created (datetime.datetime):
        origin (DominoNotificationsOrigin): Message source or author. Modeled as object for future extensibility
        priority (DominoNotificationsPriority):
        message (str | Unset):  Example: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt..
    """

    id: str
    title: str
    created: datetime.datetime
    origin: DominoNotificationsOrigin
    priority: DominoNotificationsPriority
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        created = self.created.isoformat()

        origin = self.origin.to_dict()

        priority = self.priority.value

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "created": created,
                "origin": origin,
                "priority": priority,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_notifications_origin import DominoNotificationsOrigin

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        created = isoparse(d.pop("created"))

        origin = DominoNotificationsOrigin.from_dict(d.pop("origin"))

        priority = DominoNotificationsPriority(d.pop("priority"))

        message = d.pop("message", UNSET)

        domino_notifications_notification = cls(
            id=id,
            title=title,
            created=created,
            origin=origin,
            priority=priority,
            message=message,
        )

        domino_notifications_notification.additional_properties = d
        return domino_notifications_notification

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
