from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesWebFullDeleteSpecification")


@_attrs_define
class DominoFilesWebFullDeleteSpecification:
    """
    Attributes:
        file_path (str):
        project_id (str):
        commit_id (str):
        delete_reason (str):
    """

    file_path: str
    project_id: str
    commit_id: str
    delete_reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_path = self.file_path

        project_id = self.project_id

        commit_id = self.commit_id

        delete_reason = self.delete_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filePath": file_path,
                "projectId": project_id,
                "commitId": commit_id,
                "deleteReason": delete_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_path = d.pop("filePath")

        project_id = d.pop("projectId")

        commit_id = d.pop("commitId")

        delete_reason = d.pop("deleteReason")

        domino_files_web_full_delete_specification = cls(
            file_path=file_path,
            project_id=project_id,
            commit_id=commit_id,
            delete_reason=delete_reason,
        )

        domino_files_web_full_delete_specification.additional_properties = d
        return domino_files_web_full_delete_specification

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
