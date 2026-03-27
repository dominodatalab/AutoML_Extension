from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoAdminUsermanagementApiAllowedActions")


@_attrs_define
class DominoAdminUsermanagementApiAllowedActions:
    """
    Attributes:
        create_users (bool):
        enable_disable_users (bool):
        manage_feature_flags (bool):
        mark_unmark_user_as_domino_employee (bool):
        reset_passwords (bool):
        save_roles (bool):
        view_external_orgs (bool):
        view_data_analyst_column (bool):
    """

    create_users: bool
    enable_disable_users: bool
    manage_feature_flags: bool
    mark_unmark_user_as_domino_employee: bool
    reset_passwords: bool
    save_roles: bool
    view_external_orgs: bool
    view_data_analyst_column: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_users = self.create_users

        enable_disable_users = self.enable_disable_users

        manage_feature_flags = self.manage_feature_flags

        mark_unmark_user_as_domino_employee = self.mark_unmark_user_as_domino_employee

        reset_passwords = self.reset_passwords

        save_roles = self.save_roles

        view_external_orgs = self.view_external_orgs

        view_data_analyst_column = self.view_data_analyst_column

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createUsers": create_users,
                "enableDisableUsers": enable_disable_users,
                "manageFeatureFlags": manage_feature_flags,
                "markUnmarkUserAsDominoEmployee": mark_unmark_user_as_domino_employee,
                "resetPasswords": reset_passwords,
                "saveRoles": save_roles,
                "viewExternalOrgs": view_external_orgs,
                "viewDataAnalystColumn": view_data_analyst_column,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_users = d.pop("createUsers")

        enable_disable_users = d.pop("enableDisableUsers")

        manage_feature_flags = d.pop("manageFeatureFlags")

        mark_unmark_user_as_domino_employee = d.pop("markUnmarkUserAsDominoEmployee")

        reset_passwords = d.pop("resetPasswords")

        save_roles = d.pop("saveRoles")

        view_external_orgs = d.pop("viewExternalOrgs")

        view_data_analyst_column = d.pop("viewDataAnalystColumn")

        domino_admin_usermanagement_api_allowed_actions = cls(
            create_users=create_users,
            enable_disable_users=enable_disable_users,
            manage_feature_flags=manage_feature_flags,
            mark_unmark_user_as_domino_employee=mark_unmark_user_as_domino_employee,
            reset_passwords=reset_passwords,
            save_roles=save_roles,
            view_external_orgs=view_external_orgs,
            view_data_analyst_column=view_data_analyst_column,
        )

        domino_admin_usermanagement_api_allowed_actions.additional_properties = d
        return domino_admin_usermanagement_api_allowed_actions

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
