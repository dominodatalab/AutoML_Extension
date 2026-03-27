from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_usermanagement_api_admin_user_management_user import (
        DominoAdminUsermanagementApiAdminUserManagementUser,
    )
    from ..models.domino_admin_usermanagement_api_brief_user_usage_report import (
        DominoAdminUsermanagementApiBriefUserUsageReport,
    )


T = TypeVar("T", bound="DominoAdminUsermanagementApiAdminUserManagementUserWithUsage")


@_attrs_define
class DominoAdminUsermanagementApiAdminUserManagementUserWithUsage:
    """
    Attributes:
        user (DominoAdminUsermanagementApiAdminUserManagementUser):
        usage (DominoAdminUsermanagementApiBriefUserUsageReport | Unset):
    """

    user: DominoAdminUsermanagementApiAdminUserManagementUser
    usage: DominoAdminUsermanagementApiBriefUserUsageReport | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_usermanagement_api_admin_user_management_user import (
            DominoAdminUsermanagementApiAdminUserManagementUser,
        )
        from ..models.domino_admin_usermanagement_api_brief_user_usage_report import (
            DominoAdminUsermanagementApiBriefUserUsageReport,
        )

        d = dict(src_dict)
        user = DominoAdminUsermanagementApiAdminUserManagementUser.from_dict(d.pop("user"))

        _usage = d.pop("usage", UNSET)
        usage: DominoAdminUsermanagementApiBriefUserUsageReport | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = DominoAdminUsermanagementApiBriefUserUsageReport.from_dict(_usage)

        domino_admin_usermanagement_api_admin_user_management_user_with_usage = cls(
            user=user,
            usage=usage,
        )

        domino_admin_usermanagement_api_admin_user_management_user_with_usage.additional_properties = d
        return domino_admin_usermanagement_api_admin_user_management_user_with_usage

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
