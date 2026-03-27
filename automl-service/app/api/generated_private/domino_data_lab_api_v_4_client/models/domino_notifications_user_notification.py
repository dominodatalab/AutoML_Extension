from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_notifications_notification import DominoNotificationsNotification
    from ..models.domino_notifications_timeframe import DominoNotificationsTimeframe


T = TypeVar("T", bound="DominoNotificationsUserNotification")


@_attrs_define
class DominoNotificationsUserNotification:
    """
    Attributes:
        notification (DominoNotificationsNotification):
        timeframe (DominoNotificationsTimeframe):
        read (bool): has this notification been read by the current user?
        expired (bool): has this notification expired?
    """

    notification: DominoNotificationsNotification
    timeframe: DominoNotificationsTimeframe
    read: bool
    expired: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification = self.notification.to_dict()

        timeframe = self.timeframe.to_dict()

        read = self.read

        expired = self.expired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification": notification,
                "timeframe": timeframe,
                "read": read,
                "expired": expired,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_notifications_notification import DominoNotificationsNotification
        from ..models.domino_notifications_timeframe import DominoNotificationsTimeframe

        d = dict(src_dict)
        notification = DominoNotificationsNotification.from_dict(d.pop("notification"))

        timeframe = DominoNotificationsTimeframe.from_dict(d.pop("timeframe"))

        read = d.pop("read")

        expired = d.pop("expired")

        domino_notifications_user_notification = cls(
            notification=notification,
            timeframe=timeframe,
            read=read,
            expired=expired,
        )

        domino_notifications_user_notification.additional_properties = d
        return domino_notifications_user_notification

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
