from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceFilesPermissionsDto")


@_attrs_define
class DominoFilesInterfaceFilesPermissionsDto:
    """
    Attributes:
        global_use_file_storage (bool):
        can_run (bool):
        can_edit (bool):
        can_browse_read_files (bool):
        can_list_project (bool):
        can_full_delete (bool):
        can_change_project_settings (bool):
    """

    global_use_file_storage: bool
    can_run: bool
    can_edit: bool
    can_browse_read_files: bool
    can_list_project: bool
    can_full_delete: bool
    can_change_project_settings: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_use_file_storage = self.global_use_file_storage

        can_run = self.can_run

        can_edit = self.can_edit

        can_browse_read_files = self.can_browse_read_files

        can_list_project = self.can_list_project

        can_full_delete = self.can_full_delete

        can_change_project_settings = self.can_change_project_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "globalUseFileStorage": global_use_file_storage,
                "canRun": can_run,
                "canEdit": can_edit,
                "canBrowseReadFiles": can_browse_read_files,
                "canListProject": can_list_project,
                "canFullDelete": can_full_delete,
                "canChangeProjectSettings": can_change_project_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_use_file_storage = d.pop("globalUseFileStorage")

        can_run = d.pop("canRun")

        can_edit = d.pop("canEdit")

        can_browse_read_files = d.pop("canBrowseReadFiles")

        can_list_project = d.pop("canListProject")

        can_full_delete = d.pop("canFullDelete")

        can_change_project_settings = d.pop("canChangeProjectSettings")

        domino_files_interface_files_permissions_dto = cls(
            global_use_file_storage=global_use_file_storage,
            can_run=can_run,
            can_edit=can_edit,
            can_browse_read_files=can_browse_read_files,
            can_list_project=can_list_project,
            can_full_delete=can_full_delete,
            can_change_project_settings=can_change_project_settings,
        )

        domino_files_interface_files_permissions_dto.additional_properties = d
        return domino_files_interface_files_permissions_dto

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
