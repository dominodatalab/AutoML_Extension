from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_admin_interface_admin_projects_settings import DominoAdminInterfaceAdminProjectsSettings


T = TypeVar("T", bound="DominoAdminInterfaceAdminSettings")


@_attrs_define
class DominoAdminInterfaceAdminSettings:
    """
    Attributes:
        projects (DominoAdminInterfaceAdminProjectsSettings):
    """

    projects: DominoAdminInterfaceAdminProjectsSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = self.projects.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_admin_projects_settings import DominoAdminInterfaceAdminProjectsSettings

        d = dict(src_dict)
        projects = DominoAdminInterfaceAdminProjectsSettings.from_dict(d.pop("projects"))

        domino_admin_interface_admin_settings = cls(
            projects=projects,
        )

        domino_admin_interface_admin_settings.additional_properties = d
        return domino_admin_interface_admin_settings

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
