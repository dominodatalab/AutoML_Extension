from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1
    from ..models.project_git_repository_v1 import ProjectGitRepositoryV1


T = TypeVar("T", bound="PaginatedGitRepositoriesEnvelopeV1")


@_attrs_define
class PaginatedGitRepositoriesEnvelopeV1:
    """
    Attributes:
        metadata (PaginatedMetadataV1):
        repositories (list[ProjectGitRepositoryV1]):
    """

    metadata: PaginatedMetadataV1
    repositories: list[ProjectGitRepositoryV1]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        repositories = []
        for repositories_item_data in self.repositories:
            repositories_item = repositories_item_data.to_dict()
            repositories.append(repositories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "repositories": repositories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1
        from ..models.project_git_repository_v1 import ProjectGitRepositoryV1

        d = dict(src_dict)
        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        repositories = []
        _repositories = d.pop("repositories")
        for repositories_item_data in _repositories:
            repositories_item = ProjectGitRepositoryV1.from_dict(repositories_item_data)

            repositories.append(repositories_item)

        paginated_git_repositories_envelope_v1 = cls(
            metadata=metadata,
            repositories=repositories,
        )

        paginated_git_repositories_envelope_v1.additional_properties = d
        return paginated_git_repositories_envelope_v1

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
