from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_files_interface_file_view_template_dto import DominoFilesInterfaceFileViewTemplateDto
    from ..models.domino_files_interface_project_code_view_dto_relative_bread_crumbs_item import (
        DominoFilesInterfaceProjectCodeViewDtoRelativeBreadCrumbsItem,
    )
    from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeViewDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeViewDto:
    """
    Attributes:
        project_id (str):
        project_visibility (str):
        file_view_template (DominoFilesInterfaceFileViewTemplateDto):
        filename (str):
        relative_bread_crumbs (list[DominoFilesInterfaceProjectCodeViewDtoRelativeBreadCrumbsItem]):
        revert_file_endpoint (str):
        is_file_runnable_as_app (bool):
        is_file_runnable_from_view (bool):
        head_revision_directory_link (str):
        is_comment_preview_enabled (bool):
        action (str):
        run_number_for_commit (str):
        commits_run_link (str):
        selected_revision (DominoFilesInterfaceRevisionShape):
        available_revisions (list[DominoFilesInterfaceRevisionShape]):
        csrf_token (None | str | Unset):
    """

    project_id: str
    project_visibility: str
    file_view_template: DominoFilesInterfaceFileViewTemplateDto
    filename: str
    relative_bread_crumbs: list[DominoFilesInterfaceProjectCodeViewDtoRelativeBreadCrumbsItem]
    revert_file_endpoint: str
    is_file_runnable_as_app: bool
    is_file_runnable_from_view: bool
    head_revision_directory_link: str
    is_comment_preview_enabled: bool
    action: str
    run_number_for_commit: str
    commits_run_link: str
    selected_revision: DominoFilesInterfaceRevisionShape
    available_revisions: list[DominoFilesInterfaceRevisionShape]
    csrf_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_visibility = self.project_visibility

        file_view_template = self.file_view_template.to_dict()

        filename = self.filename

        relative_bread_crumbs = []
        for relative_bread_crumbs_item_data in self.relative_bread_crumbs:
            relative_bread_crumbs_item = relative_bread_crumbs_item_data.to_dict()
            relative_bread_crumbs.append(relative_bread_crumbs_item)

        revert_file_endpoint = self.revert_file_endpoint

        is_file_runnable_as_app = self.is_file_runnable_as_app

        is_file_runnable_from_view = self.is_file_runnable_from_view

        head_revision_directory_link = self.head_revision_directory_link

        is_comment_preview_enabled = self.is_comment_preview_enabled

        action = self.action

        run_number_for_commit = self.run_number_for_commit

        commits_run_link = self.commits_run_link

        selected_revision = self.selected_revision.to_dict()

        available_revisions = []
        for available_revisions_item_data in self.available_revisions:
            available_revisions_item = available_revisions_item_data.to_dict()
            available_revisions.append(available_revisions_item)

        csrf_token: None | str | Unset
        if isinstance(self.csrf_token, Unset):
            csrf_token = UNSET
        else:
            csrf_token = self.csrf_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectVisibility": project_visibility,
                "fileViewTemplate": file_view_template,
                "filename": filename,
                "relativeBreadCrumbs": relative_bread_crumbs,
                "revertFileEndpoint": revert_file_endpoint,
                "isFileRunnableAsApp": is_file_runnable_as_app,
                "isFileRunnableFromView": is_file_runnable_from_view,
                "headRevisionDirectoryLink": head_revision_directory_link,
                "isCommentPreviewEnabled": is_comment_preview_enabled,
                "action": action,
                "runNumberForCommit": run_number_for_commit,
                "commitsRunLink": commits_run_link,
                "selectedRevision": selected_revision,
                "availableRevisions": available_revisions,
            }
        )
        if csrf_token is not UNSET:
            field_dict["csrfToken"] = csrf_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_file_view_template_dto import DominoFilesInterfaceFileViewTemplateDto
        from ..models.domino_files_interface_project_code_view_dto_relative_bread_crumbs_item import (
            DominoFilesInterfaceProjectCodeViewDtoRelativeBreadCrumbsItem,
        )
        from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape

        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_visibility = d.pop("projectVisibility")

        file_view_template = DominoFilesInterfaceFileViewTemplateDto.from_dict(d.pop("fileViewTemplate"))

        filename = d.pop("filename")

        relative_bread_crumbs = []
        _relative_bread_crumbs = d.pop("relativeBreadCrumbs")
        for relative_bread_crumbs_item_data in _relative_bread_crumbs:
            relative_bread_crumbs_item = DominoFilesInterfaceProjectCodeViewDtoRelativeBreadCrumbsItem.from_dict(
                relative_bread_crumbs_item_data
            )

            relative_bread_crumbs.append(relative_bread_crumbs_item)

        revert_file_endpoint = d.pop("revertFileEndpoint")

        is_file_runnable_as_app = d.pop("isFileRunnableAsApp")

        is_file_runnable_from_view = d.pop("isFileRunnableFromView")

        head_revision_directory_link = d.pop("headRevisionDirectoryLink")

        is_comment_preview_enabled = d.pop("isCommentPreviewEnabled")

        action = d.pop("action")

        run_number_for_commit = d.pop("runNumberForCommit")

        commits_run_link = d.pop("commitsRunLink")

        selected_revision = DominoFilesInterfaceRevisionShape.from_dict(d.pop("selectedRevision"))

        available_revisions = []
        _available_revisions = d.pop("availableRevisions")
        for available_revisions_item_data in _available_revisions:
            available_revisions_item = DominoFilesInterfaceRevisionShape.from_dict(available_revisions_item_data)

            available_revisions.append(available_revisions_item)

        def _parse_csrf_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csrf_token = _parse_csrf_token(d.pop("csrfToken", UNSET))

        domino_files_interface_project_code_view_dto = cls(
            project_id=project_id,
            project_visibility=project_visibility,
            file_view_template=file_view_template,
            filename=filename,
            relative_bread_crumbs=relative_bread_crumbs,
            revert_file_endpoint=revert_file_endpoint,
            is_file_runnable_as_app=is_file_runnable_as_app,
            is_file_runnable_from_view=is_file_runnable_from_view,
            head_revision_directory_link=head_revision_directory_link,
            is_comment_preview_enabled=is_comment_preview_enabled,
            action=action,
            run_number_for_commit=run_number_for_commit,
            commits_run_link=commits_run_link,
            selected_revision=selected_revision,
            available_revisions=available_revisions,
            csrf_token=csrf_token,
        )

        domino_files_interface_project_code_view_dto.additional_properties = d
        return domino_files_interface_project_code_view_dto

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
