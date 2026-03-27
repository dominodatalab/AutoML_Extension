from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceGitCredentials")


@_attrs_define
class DominoFilesInterfaceGitCredentials:
    """
    Attributes:
        id (str):
        name (str):
        domain (str):
        fingerprint (str):
        git_service_provider (str):
        protocol (str):
    """

    id: str
    name: str
    domain: str
    fingerprint: str
    git_service_provider: str
    protocol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        domain = self.domain

        fingerprint = self.fingerprint

        git_service_provider = self.git_service_provider

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "domain": domain,
                "fingerprint": fingerprint,
                "gitServiceProvider": git_service_provider,
                "protocol": protocol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        domain = d.pop("domain")

        fingerprint = d.pop("fingerprint")

        git_service_provider = d.pop("gitServiceProvider")

        protocol = d.pop("protocol")

        domino_files_interface_git_credentials = cls(
            id=id,
            name=name,
            domain=domain,
            fingerprint=fingerprint,
            git_service_provider=git_service_provider,
            protocol=protocol,
        )

        domino_files_interface_git_credentials.additional_properties = d
        return domino_files_interface_git_credentials

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
