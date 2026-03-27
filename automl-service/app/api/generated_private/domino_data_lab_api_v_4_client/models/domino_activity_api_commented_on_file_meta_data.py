from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoActivityApiCommentedOnFileMetaData")


@_attrs_define
class DominoActivityApiCommentedOnFileMetaData:
    """
    Attributes:
        commit_id (str):
        file_name (str):
        separator (str):
    """

    commit_id: str
    file_name: str
    separator: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        file_name = self.file_name

        separator = self.separator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "fileName": file_name,
                "separator": separator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_id = d.pop("commitId")

        file_name = d.pop("fileName")

        separator = d.pop("separator")

        domino_activity_api_commented_on_file_meta_data = cls(
            commit_id=commit_id,
            file_name=file_name,
            separator=separator,
        )

        domino_activity_api_commented_on_file_meta_data.additional_properties = d
        return domino_activity_api_commented_on_file_meta_data

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
