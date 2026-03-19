from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegisteredModelProjectSummaryV1")


@_attrs_define
class RegisteredModelProjectSummaryV1:
    """type that tracks properties of the project associated with a model

    Attributes:
        id (str): ID of the project housing the model Example: 62313ce67a0af0281c01a6a5.
        is_git_based_project (bool): Whether the project is a git-based project
        name (str): Name of the project overview housing the model Example: TO-DO.
        owner_username (str): Name of the project owner Example: TO-DO.
    """

    id: str
    is_git_based_project: bool
    name: str
    owner_username: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_git_based_project = self.is_git_based_project

        name = self.name

        owner_username = self.owner_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isGitBasedProject": is_git_based_project,
                "name": name,
                "ownerUsername": owner_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_git_based_project = d.pop("isGitBasedProject")

        name = d.pop("name")

        owner_username = d.pop("ownerUsername")

        registered_model_project_summary_v1 = cls(
            id=id,
            is_git_based_project=is_git_based_project,
            name=name,
            owner_username=owner_username,
        )

        registered_model_project_summary_v1.additional_properties = d
        return registered_model_project_summary_v1

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
