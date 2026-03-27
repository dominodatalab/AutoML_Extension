from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesWebArchiveFileComment")


@_attrs_define
class DominoFilesWebArchiveFileComment:
    """
    Attributes:
        project_id (str):
        comment_thread_id (str):
        comment_id (str):
    """

    project_id: str
    comment_thread_id: str
    comment_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        comment_thread_id = self.comment_thread_id

        comment_id = self.comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "commentThreadId": comment_thread_id,
                "commentId": comment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        comment_thread_id = d.pop("commentThreadId")

        comment_id = d.pop("commentId")

        domino_files_web_archive_file_comment = cls(
            project_id=project_id,
            comment_thread_id=comment_thread_id,
            comment_id=comment_id,
        )

        domino_files_web_archive_file_comment.additional_properties = d
        return domino_files_web_archive_file_comment

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
