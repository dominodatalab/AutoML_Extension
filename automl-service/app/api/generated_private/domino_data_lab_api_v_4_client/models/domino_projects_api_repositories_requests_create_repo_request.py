from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_repositories_requests_create_repo_request_service_provider import (
    DominoProjectsApiRepositoriesRequestsCreateRepoRequestServiceProvider,
)
from ..models.domino_projects_api_repositories_requests_create_repo_request_visibility import (
    DominoProjectsApiRepositoriesRequestsCreateRepoRequestVisibility,
)

T = TypeVar("T", bound="DominoProjectsApiRepositoriesRequestsCreateRepoRequest")


@_attrs_define
class DominoProjectsApiRepositoriesRequestsCreateRepoRequest:
    """
    Attributes:
        service_provider (DominoProjectsApiRepositoriesRequestsCreateRepoRequestServiceProvider):
        credential_id (str):
        repository_to_create_name (str):
        owner (str):
        visibility (DominoProjectsApiRepositoriesRequestsCreateRepoRequestVisibility):
    """

    service_provider: DominoProjectsApiRepositoriesRequestsCreateRepoRequestServiceProvider
    credential_id: str
    repository_to_create_name: str
    owner: str
    visibility: DominoProjectsApiRepositoriesRequestsCreateRepoRequestVisibility
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_provider = self.service_provider.value

        credential_id = self.credential_id

        repository_to_create_name = self.repository_to_create_name

        owner = self.owner

        visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceProvider": service_provider,
                "credentialId": credential_id,
                "repositoryToCreateName": repository_to_create_name,
                "owner": owner,
                "visibility": visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_provider = DominoProjectsApiRepositoriesRequestsCreateRepoRequestServiceProvider(
            d.pop("serviceProvider")
        )

        credential_id = d.pop("credentialId")

        repository_to_create_name = d.pop("repositoryToCreateName")

        owner = d.pop("owner")

        visibility = DominoProjectsApiRepositoriesRequestsCreateRepoRequestVisibility(d.pop("visibility"))

        domino_projects_api_repositories_requests_create_repo_request = cls(
            service_provider=service_provider,
            credential_id=credential_id,
            repository_to_create_name=repository_to_create_name,
            owner=owner,
            visibility=visibility,
        )

        domino_projects_api_repositories_requests_create_repo_request.additional_properties = d
        return domino_projects_api_repositories_requests_create_repo_request

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
