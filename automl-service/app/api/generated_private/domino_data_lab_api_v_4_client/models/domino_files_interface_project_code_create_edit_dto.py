from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_files_interface_project_code_create_edit_dto_status import (
    DominoFilesInterfaceProjectCodeCreateEditDtoStatus,
)

if TYPE_CHECKING:
    from ..models.domino_files_interface_default_values import DominoFilesInterfaceDefaultValues
    from ..models.domino_files_interface_project_code_create_edit_dto_relative_bread_crumbs_item import (
        DominoFilesInterfaceProjectCodeCreateEditDtoRelativeBreadCrumbsItem,
    )


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeCreateEditDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeCreateEditDto:
    """
    Attributes:
        at_head_commit (bool):
        content (str):
        current_commit_id (str):
        default_values (DominoFilesInterfaceDefaultValues):
        filename (str):
        is_default_app_sh (bool):
        old_path (str):
        relative_bread_crumbs (list[DominoFilesInterfaceProjectCodeCreateEditDtoRelativeBreadCrumbsItem]):
        show_save_and_run (bool):
        status (DominoFilesInterfaceProjectCodeCreateEditDtoStatus):
    """

    at_head_commit: bool
    content: str
    current_commit_id: str
    default_values: DominoFilesInterfaceDefaultValues
    filename: str
    is_default_app_sh: bool
    old_path: str
    relative_bread_crumbs: list[DominoFilesInterfaceProjectCodeCreateEditDtoRelativeBreadCrumbsItem]
    show_save_and_run: bool
    status: DominoFilesInterfaceProjectCodeCreateEditDtoStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at_head_commit = self.at_head_commit

        content = self.content

        current_commit_id = self.current_commit_id

        default_values = self.default_values.to_dict()

        filename = self.filename

        is_default_app_sh = self.is_default_app_sh

        old_path = self.old_path

        relative_bread_crumbs = []
        for relative_bread_crumbs_item_data in self.relative_bread_crumbs:
            relative_bread_crumbs_item = relative_bread_crumbs_item_data.to_dict()
            relative_bread_crumbs.append(relative_bread_crumbs_item)

        show_save_and_run = self.show_save_and_run

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "atHeadCommit": at_head_commit,
                "content": content,
                "currentCommitId": current_commit_id,
                "defaultValues": default_values,
                "filename": filename,
                "isDefaultAppSh": is_default_app_sh,
                "oldPath": old_path,
                "relativeBreadCrumbs": relative_bread_crumbs,
                "showSaveAndRun": show_save_and_run,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_default_values import DominoFilesInterfaceDefaultValues
        from ..models.domino_files_interface_project_code_create_edit_dto_relative_bread_crumbs_item import (
            DominoFilesInterfaceProjectCodeCreateEditDtoRelativeBreadCrumbsItem,
        )

        d = dict(src_dict)
        at_head_commit = d.pop("atHeadCommit")

        content = d.pop("content")

        current_commit_id = d.pop("currentCommitId")

        default_values = DominoFilesInterfaceDefaultValues.from_dict(d.pop("defaultValues"))

        filename = d.pop("filename")

        is_default_app_sh = d.pop("isDefaultAppSh")

        old_path = d.pop("oldPath")

        relative_bread_crumbs = []
        _relative_bread_crumbs = d.pop("relativeBreadCrumbs")
        for relative_bread_crumbs_item_data in _relative_bread_crumbs:
            relative_bread_crumbs_item = DominoFilesInterfaceProjectCodeCreateEditDtoRelativeBreadCrumbsItem.from_dict(
                relative_bread_crumbs_item_data
            )

            relative_bread_crumbs.append(relative_bread_crumbs_item)

        show_save_and_run = d.pop("showSaveAndRun")

        status = DominoFilesInterfaceProjectCodeCreateEditDtoStatus(d.pop("status"))

        domino_files_interface_project_code_create_edit_dto = cls(
            at_head_commit=at_head_commit,
            content=content,
            current_commit_id=current_commit_id,
            default_values=default_values,
            filename=filename,
            is_default_app_sh=is_default_app_sh,
            old_path=old_path,
            relative_bread_crumbs=relative_bread_crumbs,
            show_save_and_run=show_save_and_run,
            status=status,
        )

        domino_files_interface_project_code_create_edit_dto.additional_properties = d
        return domino_files_interface_project_code_create_edit_dto

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
