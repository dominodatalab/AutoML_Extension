from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_notifications_limited_audience import DominoNotificationsLimitedAudience
    from ..models.domino_notifications_notification import DominoNotificationsNotification
    from ..models.domino_notifications_timeframe import DominoNotificationsTimeframe


T = TypeVar("T", bound="DominoNotificationsAdminNotification")


@_attrs_define
class DominoNotificationsAdminNotification:
    """
    Attributes:
        notification (DominoNotificationsNotification):
        timeframe (DominoNotificationsTimeframe):
        expired (bool): has this notification expired?
        limited_audience (DominoNotificationsLimitedAudience | Unset): Definition of a limited audience for a
            notification. If present, a notification will be shown to users who are mentioned directly, or part of a
            mentioned org, or have one of the mentioned roles (at least one of these criteria must apply).
    """

    notification: DominoNotificationsNotification
    timeframe: DominoNotificationsTimeframe
    expired: bool
    limited_audience: DominoNotificationsLimitedAudience | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification = self.notification.to_dict()

        timeframe = self.timeframe.to_dict()

        expired = self.expired

        limited_audience: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limited_audience, Unset):
            limited_audience = self.limited_audience.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification": notification,
                "timeframe": timeframe,
                "expired": expired,
            }
        )
        if limited_audience is not UNSET:
            field_dict["limitedAudience"] = limited_audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_notifications_limited_audience import DominoNotificationsLimitedAudience
        from ..models.domino_notifications_notification import DominoNotificationsNotification
        from ..models.domino_notifications_timeframe import DominoNotificationsTimeframe

        d = dict(src_dict)
        notification = DominoNotificationsNotification.from_dict(d.pop("notification"))

        timeframe = DominoNotificationsTimeframe.from_dict(d.pop("timeframe"))

        expired = d.pop("expired")

        _limited_audience = d.pop("limitedAudience", UNSET)
        limited_audience: DominoNotificationsLimitedAudience | Unset
        if isinstance(_limited_audience, Unset):
            limited_audience = UNSET
        else:
            limited_audience = DominoNotificationsLimitedAudience.from_dict(_limited_audience)

        domino_notifications_admin_notification = cls(
            notification=notification,
            timeframe=timeframe,
            expired=expired,
            limited_audience=limited_audience,
        )

        domino_notifications_admin_notification.additional_properties = d
        return domino_notifications_admin_notification

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
