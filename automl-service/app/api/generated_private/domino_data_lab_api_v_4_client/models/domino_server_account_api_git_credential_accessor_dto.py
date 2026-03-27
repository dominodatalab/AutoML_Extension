from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_account_api_git_credential_accessor_dto_git_service_provider import (
    DominoServerAccountApiGitCredentialAccessorDtoGitServiceProvider,
)

T = TypeVar("T", bound="DominoServerAccountApiGitCredentialAccessorDto")


@_attrs_define
class DominoServerAccountApiGitCredentialAccessorDto:
    """
    Attributes:
        id (str):
        name (str):
        git_service_provider (DominoServerAccountApiGitCredentialAccessorDtoGitServiceProvider):
        domain (str):
        fingerprint (str):
        protocol (str):
    """

    id: str
    name: str
    git_service_provider: DominoServerAccountApiGitCredentialAccessorDtoGitServiceProvider
    domain: str
    fingerprint: str
    protocol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        git_service_provider = self.git_service_provider.value

        domain = self.domain

        fingerprint = self.fingerprint

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "gitServiceProvider": git_service_provider,
                "domain": domain,
                "fingerprint": fingerprint,
                "protocol": protocol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        git_service_provider = DominoServerAccountApiGitCredentialAccessorDtoGitServiceProvider(
            d.pop("gitServiceProvider")
        )

        domain = d.pop("domain")

        fingerprint = d.pop("fingerprint")

        protocol = d.pop("protocol")

        domino_server_account_api_git_credential_accessor_dto = cls(
            id=id,
            name=name,
            git_service_provider=git_service_provider,
            domain=domain,
            fingerprint=fingerprint,
            protocol=protocol,
        )

        domino_server_account_api_git_credential_accessor_dto.additional_properties = d
        return domino_server_account_api_git_credential_accessor_dto

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
