from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_admin_usermanagement_api_admin_user_management_user_with_usage import (
        DominoAdminUsermanagementApiAdminUserManagementUserWithUsage,
    )
    from ..models.domino_admin_usermanagement_api_users_with_usage_metadata import (
        DominoAdminUsermanagementApiUsersWithUsageMetadata,
    )


T = TypeVar("T", bound="DominoAdminUsermanagementApiUsersWithUsageResponse")


@_attrs_define
class DominoAdminUsermanagementApiUsersWithUsageResponse:
    """
    Attributes:
        users (list[DominoAdminUsermanagementApiAdminUserManagementUserWithUsage]):
        metadata (DominoAdminUsermanagementApiUsersWithUsageMetadata):
    """

    users: list[DominoAdminUsermanagementApiAdminUserManagementUserWithUsage]
    metadata: DominoAdminUsermanagementApiUsersWithUsageMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_usermanagement_api_admin_user_management_user_with_usage import (
            DominoAdminUsermanagementApiAdminUserManagementUserWithUsage,
        )
        from ..models.domino_admin_usermanagement_api_users_with_usage_metadata import (
            DominoAdminUsermanagementApiUsersWithUsageMetadata,
        )

        d = dict(src_dict)
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = DominoAdminUsermanagementApiAdminUserManagementUserWithUsage.from_dict(users_item_data)

            users.append(users_item)

        metadata = DominoAdminUsermanagementApiUsersWithUsageMetadata.from_dict(d.pop("metadata"))

        domino_admin_usermanagement_api_users_with_usage_response = cls(
            users=users,
            metadata=metadata,
        )

        domino_admin_usermanagement_api_users_with_usage_response.additional_properties = d
        return domino_admin_usermanagement_api_users_with_usage_response

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
