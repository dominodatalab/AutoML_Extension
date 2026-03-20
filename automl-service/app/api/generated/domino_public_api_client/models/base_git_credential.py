from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseGitCredential")


@_attrs_define
class BaseGitCredential:
    """
    Attributes:
        git_service_provider (GitServiceProviderV1): Git service provider
        name (str):
        domain (str | Unset):
    """

    git_service_provider: GitServiceProviderV1
    name: str
    domain: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        git_service_provider = self.git_service_provider.value

        name = self.name

        domain = self.domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitServiceProvider": git_service_provider,
                "name": name,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        git_service_provider = GitServiceProviderV1(d.pop("gitServiceProvider"))

        name = d.pop("name")

        domain = d.pop("domain", UNSET)

        base_git_credential = cls(
            git_service_provider=git_service_provider,
            name=name,
            domain=domain,
        )

        base_git_credential.additional_properties = d
        return base_git_credential

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
