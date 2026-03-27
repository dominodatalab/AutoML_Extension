from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGitprovidersApiRepoDTO")


@_attrs_define
class DominoGitprovidersApiRepoDTO:
    """
    Attributes:
        repo_name (str):
        external_url (str):
        default_branch (None | str | Unset):
    """

    repo_name: str
    external_url: str
    default_branch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repo_name = self.repo_name

        external_url = self.external_url

        default_branch: None | str | Unset
        if isinstance(self.default_branch, Unset):
            default_branch = UNSET
        else:
            default_branch = self.default_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repoName": repo_name,
                "externalUrl": external_url,
            }
        )
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_name = d.pop("repoName")

        external_url = d.pop("externalUrl")

        def _parse_default_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_branch = _parse_default_branch(d.pop("defaultBranch", UNSET))

        domino_gitproviders_api_repo_dto = cls(
            repo_name=repo_name,
            external_url=external_url,
            default_branch=default_branch,
        )

        domino_gitproviders_api_repo_dto.additional_properties = d
        return domino_gitproviders_api_repo_dto

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
