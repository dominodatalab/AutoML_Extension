from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoNucleusFileProjectCommitDeprecated")


@_attrs_define
class DominoNucleusFileProjectCommitDeprecated:
    """
    Attributes:
        id (str):
        name (str):
        commit_time (int):
    """

    id: str
    name: str
    commit_time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        commit_time = self.commit_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "commitTime": commit_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        commit_time = d.pop("commitTime")

        domino_nucleus_file_project_commit_deprecated = cls(
            id=id,
            name=name,
            commit_time=commit_time,
        )

        domino_nucleus_file_project_commit_deprecated.additional_properties = d
        return domino_nucleus_file_project_commit_deprecated

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
