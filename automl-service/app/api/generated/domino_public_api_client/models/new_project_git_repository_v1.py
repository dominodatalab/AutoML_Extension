from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_repository_reference_v1 import ProjectRepositoryReferenceV1


T = TypeVar("T", bound="NewProjectGitRepositoryV1")


@_attrs_define
class NewProjectGitRepositoryV1:
    """
    Attributes:
        uri (str): URI of the repository origin Example: https://github.com/torvalds/linux.
        default_ref (ProjectRepositoryReferenceV1 | Unset):
        git_credential_id (str | Unset): Id of the git creds to use for the repo. Credentials only apply for the current
            user, and other users will need to add their own unique creds.
        name (str | Unset): Optional name of the repository in the project
        service_provider (GitServiceProviderV1 | Unset): Git service provider
    """

    uri: str
    default_ref: ProjectRepositoryReferenceV1 | Unset = UNSET
    git_credential_id: str | Unset = UNSET
    name: str | Unset = UNSET
    service_provider: GitServiceProviderV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        default_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_ref, Unset):
            default_ref = self.default_ref.to_dict()

        git_credential_id = self.git_credential_id

        name = self.name

        service_provider: str | Unset = UNSET
        if not isinstance(self.service_provider, Unset):
            service_provider = self.service_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if default_ref is not UNSET:
            field_dict["defaultRef"] = default_ref
        if git_credential_id is not UNSET:
            field_dict["gitCredentialId"] = git_credential_id
        if name is not UNSET:
            field_dict["name"] = name
        if service_provider is not UNSET:
            field_dict["serviceProvider"] = service_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_repository_reference_v1 import ProjectRepositoryReferenceV1

        d = dict(src_dict)
        uri = d.pop("uri")

        _default_ref = d.pop("defaultRef", UNSET)
        default_ref: ProjectRepositoryReferenceV1 | Unset
        if isinstance(_default_ref, Unset):
            default_ref = UNSET
        else:
            default_ref = ProjectRepositoryReferenceV1.from_dict(_default_ref)

        git_credential_id = d.pop("gitCredentialId", UNSET)

        name = d.pop("name", UNSET)

        _service_provider = d.pop("serviceProvider", UNSET)
        service_provider: GitServiceProviderV1 | Unset
        if isinstance(_service_provider, Unset):
            service_provider = UNSET
        else:
            service_provider = GitServiceProviderV1(_service_provider)

        new_project_git_repository_v1 = cls(
            uri=uri,
            default_ref=default_ref,
            git_credential_id=git_credential_id,
            name=name,
            service_provider=service_provider,
        )

        new_project_git_repository_v1.additional_properties = d
        return new_project_git_repository_v1

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
