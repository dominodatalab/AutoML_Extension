from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape


T = TypeVar("T", bound="DominoFilesInterfaceProjectCodeBrowseCommitDto")


@_attrs_define
class DominoFilesInterfaceProjectCodeBrowseCommitDto:
    """
    Attributes:
        commits_non_empty (bool):
        this_commit_id (str):
        head_commit_id (str):
        head_commit_created_at (int):
        project_size_bytes (int):
        run_number_for_commit (str):
        commits_run_link (str):
        selected_revision (DominoFilesInterfaceRevisionShape):
    """

    commits_non_empty: bool
    this_commit_id: str
    head_commit_id: str
    head_commit_created_at: int
    project_size_bytes: int
    run_number_for_commit: str
    commits_run_link: str
    selected_revision: DominoFilesInterfaceRevisionShape
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commits_non_empty = self.commits_non_empty

        this_commit_id = self.this_commit_id

        head_commit_id = self.head_commit_id

        head_commit_created_at = self.head_commit_created_at

        project_size_bytes = self.project_size_bytes

        run_number_for_commit = self.run_number_for_commit

        commits_run_link = self.commits_run_link

        selected_revision = self.selected_revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitsNonEmpty": commits_non_empty,
                "thisCommitId": this_commit_id,
                "headCommitId": head_commit_id,
                "headCommitCreatedAt": head_commit_created_at,
                "projectSizeBytes": project_size_bytes,
                "runNumberForCommit": run_number_for_commit,
                "commitsRunLink": commits_run_link,
                "selectedRevision": selected_revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_revision_shape import DominoFilesInterfaceRevisionShape

        d = dict(src_dict)
        commits_non_empty = d.pop("commitsNonEmpty")

        this_commit_id = d.pop("thisCommitId")

        head_commit_id = d.pop("headCommitId")

        head_commit_created_at = d.pop("headCommitCreatedAt")

        project_size_bytes = d.pop("projectSizeBytes")

        run_number_for_commit = d.pop("runNumberForCommit")

        commits_run_link = d.pop("commitsRunLink")

        selected_revision = DominoFilesInterfaceRevisionShape.from_dict(d.pop("selectedRevision"))

        domino_files_interface_project_code_browse_commit_dto = cls(
            commits_non_empty=commits_non_empty,
            this_commit_id=this_commit_id,
            head_commit_id=head_commit_id,
            head_commit_created_at=head_commit_created_at,
            project_size_bytes=project_size_bytes,
            run_number_for_commit=run_number_for_commit,
            commits_run_link=commits_run_link,
            selected_revision=selected_revision,
        )

        domino_files_interface_project_code_browse_commit_dto.additional_properties = d
        return domino_files_interface_project_code_browse_commit_dto

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
