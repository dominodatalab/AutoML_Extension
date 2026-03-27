from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceGitRepo")


@_attrs_define
class DominoFilesInterfaceGitRepo:
    """
    Attributes:
        id (str):
        location (str):
        repo_name (str):
        uri (str):
        ref_label (str):
        ref_type (str):
        service_provider (str):
    """

    id: str
    location: str
    repo_name: str
    uri: str
    ref_label: str
    ref_type: str
    service_provider: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        location = self.location

        repo_name = self.repo_name

        uri = self.uri

        ref_label = self.ref_label

        ref_type = self.ref_type

        service_provider = self.service_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "location": location,
                "repoName": repo_name,
                "uri": uri,
                "refLabel": ref_label,
                "refType": ref_type,
                "serviceProvider": service_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        location = d.pop("location")

        repo_name = d.pop("repoName")

        uri = d.pop("uri")

        ref_label = d.pop("refLabel")

        ref_type = d.pop("refType")

        service_provider = d.pop("serviceProvider")

        domino_files_interface_git_repo = cls(
            id=id,
            location=location,
            repo_name=repo_name,
            uri=uri,
            ref_label=ref_label,
            ref_type=ref_type,
            service_provider=service_provider,
        )

        domino_files_interface_git_repo.additional_properties = d
        return domino_files_interface_git_repo

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
