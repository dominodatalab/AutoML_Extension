from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="SshGitCredential")


@_attrs_define
class SshGitCredential:
    """
    Attributes:
        git_service_provider (GitServiceProviderV1): Git service provider
        name (str):
        key (str):
        domain (str | Unset):
        passphrase (str | Unset):
    """

    git_service_provider: GitServiceProviderV1
    name: str
    key: str
    domain: str | Unset = UNSET
    passphrase: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_service_provider = self.git_service_provider.value

        name = self.name

        key = self.key

        domain = self.domain

        passphrase = self.passphrase

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitServiceProvider": git_service_provider,
                "name": name,
                "key": key,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_service_provider = GitServiceProviderV1(d.pop("gitServiceProvider"))

        name = d.pop("name")

        key = d.pop("key")

        domain = d.pop("domain", UNSET)

        passphrase = d.pop("passphrase", UNSET)

        ssh_git_credential = cls(
            git_service_provider=git_service_provider,
            name=name,
            key=key,
            domain=domain,
            passphrase=passphrase,
        )

        ssh_git_credential.additional_properties = d
        return ssh_git_credential

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
