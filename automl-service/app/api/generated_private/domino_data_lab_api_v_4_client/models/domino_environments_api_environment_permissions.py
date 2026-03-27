from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentPermissions")


@_attrs_define
class DominoEnvironmentsApiEnvironmentPermissions:
    """
    Attributes:
        can_edit (bool):
        can_archive (bool):
    """

    can_edit: bool
    can_archive: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_edit = self.can_edit

        can_archive = self.can_archive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canEdit": can_edit,
                "canArchive": can_archive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_edit = d.pop("canEdit")

        can_archive = d.pop("canArchive")

        domino_environments_api_environment_permissions = cls(
            can_edit=can_edit,
            can_archive=can_archive,
        )

        domino_environments_api_environment_permissions.additional_properties = d
        return domino_environments_api_environment_permissions

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
