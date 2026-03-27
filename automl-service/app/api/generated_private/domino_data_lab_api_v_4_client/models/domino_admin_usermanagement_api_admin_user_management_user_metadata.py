from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoAdminUsermanagementApiAdminUserManagementUserMetadata")


@_attrs_define
class DominoAdminUsermanagementApiAdminUserManagementUserMetadata:
    """
    Attributes:
        is_managable_by_viewer (bool):
    """

    is_managable_by_viewer: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_managable_by_viewer = self.is_managable_by_viewer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isManagableByViewer": is_managable_by_viewer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_managable_by_viewer = d.pop("isManagableByViewer")

        domino_admin_usermanagement_api_admin_user_management_user_metadata = cls(
            is_managable_by_viewer=is_managable_by_viewer,
        )

        domino_admin_usermanagement_api_admin_user_management_user_metadata.additional_properties = d
        return domino_admin_usermanagement_api_admin_user_management_user_metadata

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
