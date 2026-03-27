from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_project_code_shared_view_dto_relative_bread_crumbs_item import (
        DominoFilesInterfaceProjectCodeSharedViewDtoRelativeBreadCrumbsItem,
    )
    from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeSharedViewDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeSharedViewDto:
    """
    Attributes:
        available_revisions (list[DominoFilesInterfaceRevisionShape]):
        commit_id (str):
        commits_run_link (str):
        filename (str):
        is_comment_preview_enabled (bool):
        project_id (str):
        relative_bread_crumbs (list[DominoFilesInterfaceProjectCodeSharedViewDtoRelativeBreadCrumbsItem]):
        run_number_for_commit (str):
        selected_revision (DominoFilesInterfaceRevisionShape):
    """

    available_revisions: list[DominoFilesInterfaceRevisionShape]
    commit_id: str
    commits_run_link: str
    filename: str
    is_comment_preview_enabled: bool
    project_id: str
    relative_bread_crumbs: list[DominoFilesInterfaceProjectCodeSharedViewDtoRelativeBreadCrumbsItem]
    run_number_for_commit: str
    selected_revision: DominoFilesInterfaceRevisionShape
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_revisions = []
        for available_revisions_item_data in self.available_revisions:
            available_revisions_item = available_revisions_item_data.to_dict()
            available_revisions.append(available_revisions_item)

        commit_id = self.commit_id

        commits_run_link = self.commits_run_link

        filename = self.filename

        is_comment_preview_enabled = self.is_comment_preview_enabled

        project_id = self.project_id

        relative_bread_crumbs = []
        for relative_bread_crumbs_item_data in self.relative_bread_crumbs:
            relative_bread_crumbs_item = relative_bread_crumbs_item_data.to_dict()
            relative_bread_crumbs.append(relative_bread_crumbs_item)

        run_number_for_commit = self.run_number_for_commit

        selected_revision = self.selected_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableRevisions": available_revisions,
                "commitId": commit_id,
                "commitsRunLink": commits_run_link,
                "filename": filename,
                "isCommentPreviewEnabled": is_comment_preview_enabled,
                "projectId": project_id,
                "relativeBreadCrumbs": relative_bread_crumbs,
                "runNumberForCommit": run_number_for_commit,
                "selectedRevision": selected_revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_project_code_shared_view_dto_relative_bread_crumbs_item import (
            DominoFilesInterfaceProjectCodeSharedViewDtoRelativeBreadCrumbsItem,
        )
        from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape

        d = dict(src_dict)
        available_revisions = []
        _available_revisions = d.pop("availableRevisions")
        for available_revisions_item_data in _available_revisions:
            available_revisions_item = DominoFilesInterfaceRevisionShape.from_dict(available_revisions_item_data)

            available_revisions.append(available_revisions_item)

        commit_id = d.pop("commitId")

        commits_run_link = d.pop("commitsRunLink")

        filename = d.pop("filename")

        is_comment_preview_enabled = d.pop("isCommentPreviewEnabled")

        project_id = d.pop("projectId")

        relative_bread_crumbs = []
        _relative_bread_crumbs = d.pop("relativeBreadCrumbs")
        for relative_bread_crumbs_item_data in _relative_bread_crumbs:
            relative_bread_crumbs_item = DominoFilesInterfaceProjectCodeSharedViewDtoRelativeBreadCrumbsItem.from_dict(
                relative_bread_crumbs_item_data
            )

            relative_bread_crumbs.append(relative_bread_crumbs_item)

        run_number_for_commit = d.pop("runNumberForCommit")

        selected_revision = DominoFilesInterfaceRevisionShape.from_dict(d.pop("selectedRevision"))

        domino_files_interface_project_code_shared_view_dto = cls(
            available_revisions=available_revisions,
            commit_id=commit_id,
            commits_run_link=commits_run_link,
            filename=filename,
            is_comment_preview_enabled=is_comment_preview_enabled,
            project_id=project_id,
            relative_bread_crumbs=relative_bread_crumbs,
            run_number_for_commit=run_number_for_commit,
            selected_revision=selected_revision,
        )

        domino_files_interface_project_code_shared_view_dto.additional_properties = d
        return domino_files_interface_project_code_shared_view_dto

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
