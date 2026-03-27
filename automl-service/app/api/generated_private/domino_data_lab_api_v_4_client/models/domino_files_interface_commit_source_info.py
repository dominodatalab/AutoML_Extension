from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_files_interface_commit_source_info_source_type import (
    DominoFilesInterfaceCommitSourceInfoSourceType,
)

T = TypeVar("T", bound="DominoFilesInterfaceCommitSourceInfo")


@_attrs_define
class DominoFilesInterfaceCommitSourceInfo:
    """
    Attributes:
        source_project_id (str):
        source_id (str):
        source_number (int):
        source_type (DominoFilesInterfaceCommitSourceInfoSourceType):
    """

    source_project_id: str
    source_id: str
    source_number: int
    source_type: DominoFilesInterfaceCommitSourceInfoSourceType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_project_id = self.source_project_id

        source_id = self.source_id

        source_number = self.source_number

        source_type = self.source_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceProjectId": source_project_id,
                "sourceId": source_id,
                "sourceNumber": source_number,
                "sourceType": source_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_project_id = d.pop("sourceProjectId")

        source_id = d.pop("sourceId")

        source_number = d.pop("sourceNumber")

        source_type = DominoFilesInterfaceCommitSourceInfoSourceType(d.pop("sourceType"))

        domino_files_interface_commit_source_info = cls(
            source_project_id=source_project_id,
            source_id=source_id,
            source_number=source_number,
            source_type=source_type,
        )

        domino_files_interface_commit_source_info.additional_properties = d
        return domino_files_interface_commit_source_info

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
