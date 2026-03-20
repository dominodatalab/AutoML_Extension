from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.git_service_provider_v1 import GitServiceProviderV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_repository_reference_v1 import ProjectRepositoryReferenceV1


T = TypeVar("T", bound="ProjectGitRepositoryV1")


@_attrs_define
class ProjectGitRepositoryV1:
    """
    Attributes:
        default_ref (ProjectRepositoryReferenceV1):
        id (str): Id of the repository Example: 62604702b7e5d347dbe7a908.
        service_provider (GitServiceProviderV1): Git service provider
        uri (str): URI of the repository origin Example: https://github.com/torvalds/linux.
        name (str | Unset): Optional name of the repository in the project. If not provided, a name will be inferred
            from the URL
    """

    default_ref: ProjectRepositoryReferenceV1
    id: str
    service_provider: GitServiceProviderV1
    uri: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_ref = self.default_ref.to_dict()

        id = self.id

        service_provider = self.service_provider.value

        uri = self.uri

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaultRef": default_ref,
                "id": id,
                "serviceProvider": service_provider,
                "uri": uri,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_repository_reference_v1 import ProjectRepositoryReferenceV1

        d = dict(src_dict)
        default_ref = ProjectRepositoryReferenceV1.from_dict(d.pop("defaultRef"))

        id = d.pop("id")

        service_provider = GitServiceProviderV1(d.pop("serviceProvider"))

        uri = d.pop("uri")

        name = d.pop("name", UNSET)

        project_git_repository_v1 = cls(
            default_ref=default_ref,
            id=id,
            service_provider=service_provider,
            uri=uri,
            name=name,
        )

        project_git_repository_v1.additional_properties = d
        return project_git_repository_v1

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
