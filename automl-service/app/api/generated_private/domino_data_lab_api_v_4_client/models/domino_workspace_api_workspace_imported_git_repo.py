from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceImportedGitRepo")


@_attrs_define
class DominoWorkspaceApiWorkspaceImportedGitRepo:
    """
    Attributes:
        id (str):
        name (str):
        ref (str):
        starting_branch (None | str | Unset):
    """

    id: str
    name: str
    ref: str
    starting_branch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ref = self.ref

        starting_branch: None | str | Unset
        if isinstance(self.starting_branch, Unset):
            starting_branch = UNSET
        else:
            starting_branch = self.starting_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ref": ref,
            }
        )
        if starting_branch is not UNSET:
            field_dict["startingBranch"] = starting_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        ref = d.pop("ref")

        def _parse_starting_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_branch = _parse_starting_branch(d.pop("startingBranch", UNSET))

        domino_workspace_api_workspace_imported_git_repo = cls(
            id=id,
            name=name,
            ref=ref,
            starting_branch=starting_branch,
        )

        domino_workspace_api_workspace_imported_git_repo.additional_properties = d
        return domino_workspace_api_workspace_imported_git_repo

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
