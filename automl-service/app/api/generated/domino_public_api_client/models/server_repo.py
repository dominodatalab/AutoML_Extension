from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerRepo")


@_attrs_define
class ServerRepo:
    """
    Attributes:
        base_url (str): PPM server base URL
        full_url (str): Complete repository URL
        repo_name (str): Repository name
    """

    base_url: str
    full_url: str
    repo_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        full_url = self.full_url

        repo_name = self.repo_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseUrl": base_url,
                "fullUrl": full_url,
                "repoName": repo_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_url = d.pop("baseUrl")

        full_url = d.pop("fullUrl")

        repo_name = d.pop("repoName")

        server_repo = cls(
            base_url=base_url,
            full_url=full_url,
            repo_name=repo_name,
        )

        server_repo.additional_properties = d
        return server_repo

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
