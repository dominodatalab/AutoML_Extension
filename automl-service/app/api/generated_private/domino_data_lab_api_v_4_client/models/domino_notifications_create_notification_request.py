from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_notifications_priority import DominoNotificationsPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoNotificationsCreateNotificationRequest")


@_attrs_define
class DominoNotificationsCreateNotificationRequest:
    """Request to create a new notification. If any of (targetUsers, targetRoles, targetOrgs) contain a valid entry, then
    the notification will be visible to users for which at least one of these conditions apply. Otherwise, it will be
    visible to all users.

        Attributes:
            title (str): the notification title
            priority (DominoNotificationsPriority):
            message (str | Unset): the notification body
            start (datetime.datetime | Unset): optional start date/time (defaults to now) Example: 2022-12-03T10:15:30Z.
            end (datetime.datetime | Unset): optional end date/time Example: 2022-12-03T10:15:30Z.
            target_users (list[str] | Unset): DominoIds of users who will receive this notification.
            target_orgs (list[str] | Unset): DominoIds of orgs whose users will receive this notification.
            target_roles (list[str] | Unset): Ids of Roles. Users that have any of these Roles will receive this
                notification.
    """

    title: str
    priority: DominoNotificationsPriority
    message: str | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    target_users: list[str] | Unset = UNSET
    target_orgs: list[str] | Unset = UNSET
    target_roles: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        priority = self.priority.value

        message = self.message

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        target_users: list[str] | Unset = UNSET
        if not isinstance(self.target_users, Unset):
            target_users = self.target_users

        target_orgs: list[str] | Unset = UNSET
        if not isinstance(self.target_orgs, Unset):
            target_orgs = self.target_orgs

        target_roles: list[str] | Unset = UNSET
        if not isinstance(self.target_roles, Unset):
            target_roles = self.target_roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "priority": priority,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if target_users is not UNSET:
            field_dict["targetUsers"] = target_users
        if target_orgs is not UNSET:
            field_dict["targetOrgs"] = target_orgs
        if target_roles is not UNSET:
            field_dict["targetRoles"] = target_roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        priority = DominoNotificationsPriority(d.pop("priority"))

        message = d.pop("message", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        target_users = cast(list[str], d.pop("targetUsers", UNSET))

        target_orgs = cast(list[str], d.pop("targetOrgs", UNSET))

        target_roles = cast(list[str], d.pop("targetRoles", UNSET))

        domino_notifications_create_notification_request = cls(
            title=title,
            priority=priority,
            message=message,
            start=start,
            end=end,
            target_users=target_users,
            target_orgs=target_orgs,
            target_roles=target_roles,
        )

        domino_notifications_create_notification_request.additional_properties = d
        return domino_notifications_create_notification_request

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
