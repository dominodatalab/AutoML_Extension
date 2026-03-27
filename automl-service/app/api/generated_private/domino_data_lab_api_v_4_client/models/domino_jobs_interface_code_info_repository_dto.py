from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceCodeInfoRepositoryDto")


@_attrs_define
class DominoJobsInterfaceCodeInfoRepositoryDto:
    """
    Attributes:
        id (str):
        link_text (str):
        full_url (str):
        commit (None | str | Unset):
        commit_resource_link (None | str | Unset):
        branch (None | str | Unset):
    """

    id: str
    link_text: str
    full_url: str
    commit: None | str | Unset = UNSET
    commit_resource_link: None | str | Unset = UNSET
    branch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        link_text = self.link_text

        full_url = self.full_url

        commit: None | str | Unset
        if isinstance(self.commit, Unset):
            commit = UNSET
        else:
            commit = self.commit

        commit_resource_link: None | str | Unset
        if isinstance(self.commit_resource_link, Unset):
            commit_resource_link = UNSET
        else:
            commit_resource_link = self.commit_resource_link

        branch: None | str | Unset
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "linkText": link_text,
                "fullUrl": full_url,
            }
        )
        if commit is not UNSET:
            field_dict["commit"] = commit
        if commit_resource_link is not UNSET:
            field_dict["commitResourceLink"] = commit_resource_link
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        link_text = d.pop("linkText")

        full_url = d.pop("fullUrl")

        def _parse_commit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit = _parse_commit(d.pop("commit", UNSET))

        def _parse_commit_resource_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_resource_link = _parse_commit_resource_link(d.pop("commitResourceLink", UNSET))

        def _parse_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch = _parse_branch(d.pop("branch", UNSET))

        domino_jobs_interface_code_info_repository_dto = cls(
            id=id,
            link_text=link_text,
            full_url=full_url,
            commit=commit,
            commit_resource_link=commit_resource_link,
            branch=branch,
        )

        domino_jobs_interface_code_info_repository_dto.additional_properties = d
        return domino_jobs_interface_code_info_repository_dto

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
