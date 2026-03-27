from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProvenanceApiProvenanceGitRepoDto")


@_attrs_define
class DominoProvenanceApiProvenanceGitRepoDto:
    """
    Attributes:
        id (str):
        name (str):
        commit_id (str):
        branch_name (str):
        is_main_repo (bool):
    """

    id: str
    name: str
    commit_id: str
    branch_name: str
    is_main_repo: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        commit_id = self.commit_id

        branch_name = self.branch_name

        is_main_repo = self.is_main_repo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "commitId": commit_id,
                "branchName": branch_name,
                "isMainRepo": is_main_repo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        commit_id = d.pop("commitId")

        branch_name = d.pop("branchName")

        is_main_repo = d.pop("isMainRepo")

        domino_provenance_api_provenance_git_repo_dto = cls(
            id=id,
            name=name,
            commit_id=commit_id,
            branch_name=branch_name,
            is_main_repo=is_main_repo,
        )

        domino_provenance_api_provenance_git_repo_dto.additional_properties = d
        return domino_provenance_api_provenance_git_repo_dto

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
