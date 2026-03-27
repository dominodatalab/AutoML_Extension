from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminUsermanagementApiUpdateUserRequest")


@_attrs_define
class DominoAdminUsermanagementApiUpdateUserRequest:
    """
    Attributes:
        roles (list[str] | None | Unset):
        enabled (bool | None | Unset):
        is_domino_employee (bool | None | Unset):
    """

    roles: list[str] | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    is_domino_employee: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roles: list[str] | None | Unset
        if isinstance(self.roles, Unset):
            roles = UNSET
        elif isinstance(self.roles, list):
            roles = self.roles

        else:
            roles = self.roles

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        is_domino_employee: bool | None | Unset
        if isinstance(self.is_domino_employee, Unset):
            is_domino_employee = UNSET
        else:
            is_domino_employee = self.is_domino_employee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if is_domino_employee is not UNSET:
            field_dict["isDominoEmployee"] = is_domino_employee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_roles(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = cast(list[str], data)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        roles = _parse_roles(d.pop("roles", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_is_domino_employee(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_domino_employee = _parse_is_domino_employee(d.pop("isDominoEmployee", UNSET))

        domino_admin_usermanagement_api_update_user_request = cls(
            roles=roles,
            enabled=enabled,
            is_domino_employee=is_domino_employee,
        )

        domino_admin_usermanagement_api_update_user_request.additional_properties = d
        return domino_admin_usermanagement_api_update_user_request

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
