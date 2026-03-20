from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1

T = TypeVar("T", bound="GitCredentialsAccessorV1")


@_attrs_define
class GitCredentialsAccessorV1:
    """
    Attributes:
        domain (str): The domain these credentials apply to Example: github.com.
        fingerprint (str):  Example: ba:78:09:d8:4b:3b:09:9b:43:bf:9b:5a:34:f7:3f:28.
        git_service_provider (GitServiceProviderV1): Git service provider
        id (str): Id for these git credentials
        name (str): Name for these git credentials Example: My creds.
        protocol (str):  Example: https.
    """

    domain: str
    fingerprint: str
    git_service_provider: GitServiceProviderV1
    id: str
    name: str
    protocol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        fingerprint = self.fingerprint

        git_service_provider = self.git_service_provider.value

        id = self.id

        name = self.name

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "fingerprint": fingerprint,
                "gitServiceProvider": git_service_provider,
                "id": id,
                "name": name,
                "protocol": protocol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        fingerprint = d.pop("fingerprint")

        git_service_provider = GitServiceProviderV1(d.pop("gitServiceProvider"))

        id = d.pop("id")

        name = d.pop("name")

        protocol = d.pop("protocol")

        git_credentials_accessor_v1 = cls(
            domain=domain,
            fingerprint=fingerprint,
            git_service_provider=git_service_provider,
            id=id,
            name=name,
            protocol=protocol,
        )

        git_credentials_accessor_v1.additional_properties = d
        return git_credentials_accessor_v1

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
