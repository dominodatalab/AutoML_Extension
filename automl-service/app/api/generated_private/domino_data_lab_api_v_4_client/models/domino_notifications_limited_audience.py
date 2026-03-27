from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_notifications_name_and_id import DominoNotificationsNameAndId


T = TypeVar("T", bound="DominoNotificationsLimitedAudience")


@_attrs_define
class DominoNotificationsLimitedAudience:
    """Definition of a limited audience for a notification. If present, a notification will be shown to users who are
    mentioned directly, or part of a mentioned org, or have one of the mentioned roles (at least one of these criteria
    must apply).

        Attributes:
            users (list[DominoNotificationsNameAndId] | Unset): Names and IDs of users who will receive this notification
            orgs (list[DominoNotificationsNameAndId] | Unset): Names and IDs of orgs whose users will receive this
                notification
            roles (list[DominoNotificationsNameAndId] | Unset): Names and Ids of Roles. Users that have any of these Roles
                will receive this notification.
    """

    users: list[DominoNotificationsNameAndId] | Unset = UNSET
    orgs: list[DominoNotificationsNameAndId] | Unset = UNSET
    roles: list[DominoNotificationsNameAndId] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        orgs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orgs, Unset):
            orgs = []
            for orgs_item_data in self.orgs:
                orgs_item = orgs_item_data.to_dict()
                orgs.append(orgs_item)

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if orgs is not UNSET:
            field_dict["orgs"] = orgs
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_notifications_name_and_id import DominoNotificationsNameAndId

        d = dict(src_dict)
        _users = d.pop("users", UNSET)
        users: list[DominoNotificationsNameAndId] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = DominoNotificationsNameAndId.from_dict(users_item_data)

                users.append(users_item)

        _orgs = d.pop("orgs", UNSET)
        orgs: list[DominoNotificationsNameAndId] | Unset = UNSET
        if _orgs is not UNSET:
            orgs = []
            for orgs_item_data in _orgs:
                orgs_item = DominoNotificationsNameAndId.from_dict(orgs_item_data)

                orgs.append(orgs_item)

        _roles = d.pop("roles", UNSET)
        roles: list[DominoNotificationsNameAndId] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = DominoNotificationsNameAndId.from_dict(roles_item_data)

                roles.append(roles_item)

        domino_notifications_limited_audience = cls(
            users=users,
            orgs=orgs,
            roles=roles,
        )

        domino_notifications_limited_audience.additional_properties = d
        return domino_notifications_limited_audience

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
