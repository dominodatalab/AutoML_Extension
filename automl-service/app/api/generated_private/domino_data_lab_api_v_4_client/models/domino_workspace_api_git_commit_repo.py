from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiGitCommitRepo")


@_attrs_define
class DominoWorkspaceApiGitCommitRepo:
    """
    Attributes:
        repo_id (str):
        commit_message (str):
        file_paths (list[str] | None | Unset):
    """

    repo_id: str
    commit_message: str
    file_paths: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_id = self.repo_id

        commit_message = self.commit_message

        file_paths: list[str] | None | Unset
        if isinstance(self.file_paths, Unset):
            file_paths = UNSET
        elif isinstance(self.file_paths, list):
            file_paths = self.file_paths

        else:
            file_paths = self.file_paths

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoId": repo_id,
                "commitMessage": commit_message,
            }
        )
        if file_paths is not UNSET:
            field_dict["filePaths"] = file_paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_id = d.pop("repoId")

        commit_message = d.pop("commitMessage")

        def _parse_file_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_paths_type_0 = cast(list[str], data)

                return file_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file_paths = _parse_file_paths(d.pop("filePaths", UNSET))

        domino_workspace_api_git_commit_repo = cls(
            repo_id=repo_id,
            commit_message=commit_message,
            file_paths=file_paths,
        )

        domino_workspace_api_git_commit_repo.additional_properties = d
        return domino_workspace_api_git_commit_repo

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
