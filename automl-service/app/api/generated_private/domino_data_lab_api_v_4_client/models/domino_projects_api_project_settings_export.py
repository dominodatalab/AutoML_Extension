from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_settings_export_export_package_type import (
    DominoProjectsApiProjectSettingsExportExportPackageType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectSettingsExport")


@_attrs_define
class DominoProjectsApiProjectSettingsExport:
    """
    Attributes:
        export_environment_variables (bool):
        export_files (bool):
        export_package_type (DominoProjectsApiProjectSettingsExportExportPackageType | Unset):
    """

    export_environment_variables: bool
    export_files: bool
    export_package_type: DominoProjectsApiProjectSettingsExportExportPackageType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_environment_variables = self.export_environment_variables

        export_files = self.export_files

        export_package_type: str | Unset = UNSET
        if not isinstance(self.export_package_type, Unset):
            export_package_type = self.export_package_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exportEnvironmentVariables": export_environment_variables,
                "exportFiles": export_files,
            }
        )
        if export_package_type is not UNSET:
            field_dict["exportPackageType"] = export_package_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_environment_variables = d.pop("exportEnvironmentVariables")

        export_files = d.pop("exportFiles")

        _export_package_type = d.pop("exportPackageType", UNSET)
        export_package_type: DominoProjectsApiProjectSettingsExportExportPackageType | Unset
        if isinstance(_export_package_type, Unset):
            export_package_type = UNSET
        else:
            export_package_type = DominoProjectsApiProjectSettingsExportExportPackageType(_export_package_type)

        domino_projects_api_project_settings_export = cls(
            export_environment_variables=export_environment_variables,
            export_files=export_files,
            export_package_type=export_package_type,
        )

        domino_projects_api_project_settings_export.additional_properties = d
        return domino_projects_api_project_settings_export

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
