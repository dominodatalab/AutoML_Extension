from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportFilesRepoTargetV1")


@_attrs_define
class ImportFilesRepoTargetV1:
    """Specifies what git repository to import the source project files into

    Attributes:
        repo_name (str): The name of the git repository to import the project files into
        repo_owner_name (str): The name of the target git repository's owner
        force (bool | Unset): Whether or not to overwrite all files and git history in the repository
    """

    repo_name: str
    repo_owner_name: str
    force: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_name = self.repo_name

        repo_owner_name = self.repo_owner_name

        force = self.force

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoName": repo_name,
                "repoOwnerName": repo_owner_name,
            }
        )
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_name = d.pop("repoName")

        repo_owner_name = d.pop("repoOwnerName")

        force = d.pop("force", UNSET)

        import_files_repo_target_v1 = cls(
            repo_name=repo_name,
            repo_owner_name=repo_owner_name,
            force=force,
        )

        import_files_repo_target_v1.additional_properties = d
        return import_files_repo_target_v1

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
