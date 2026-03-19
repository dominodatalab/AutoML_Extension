from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..models.provider_repo_visibility_v1 import ProviderRepoVisibilityV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoToCreateV1")


@_attrs_define
class RepoToCreateV1:
    """An object representing a new git repo to create in a remote repository

    Attributes:
        credential_id (str):
        owner (str):
        repository_to_create_name (str):
        visibility (ProviderRepoVisibilityV1): The visibility of the code repo. Internal can only be used for Github
            Enterprise.
        repository_template_name (str | Unset):
        service_provider (GitServiceProviderV1 | Unset): Git service provider
    """

    credential_id: str
    owner: str
    repository_to_create_name: str
    visibility: ProviderRepoVisibilityV1
    repository_template_name: str | Unset = UNSET
    service_provider: GitServiceProviderV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        owner = self.owner

        repository_to_create_name = self.repository_to_create_name

        visibility = self.visibility.value

        repository_template_name = self.repository_template_name

        service_provider: str | Unset = UNSET
        if not isinstance(self.service_provider, Unset):
            service_provider = self.service_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialId": credential_id,
                "owner": owner,
                "repositoryToCreateName": repository_to_create_name,
                "visibility": visibility,
            }
        )
        if repository_template_name is not UNSET:
            field_dict["repositoryTemplateName"] = repository_template_name
        if service_provider is not UNSET:
            field_dict["serviceProvider"] = service_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = d.pop("credentialId")

        owner = d.pop("owner")

        repository_to_create_name = d.pop("repositoryToCreateName")

        visibility = ProviderRepoVisibilityV1(d.pop("visibility"))

        repository_template_name = d.pop("repositoryTemplateName", UNSET)

        _service_provider = d.pop("serviceProvider", UNSET)
        service_provider: GitServiceProviderV1 | Unset
        if isinstance(_service_provider, Unset):
            service_provider = UNSET
        else:
            service_provider = GitServiceProviderV1(_service_provider)

        repo_to_create_v1 = cls(
            credential_id=credential_id,
            owner=owner,
            repository_to_create_name=repository_to_create_name,
            visibility=visibility,
            repository_template_name=repository_template_name,
            service_provider=service_provider,
        )

        repo_to_create_v1.additional_properties = d
        return repo_to_create_v1

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
