from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_projects_domain_entities_project_git_repository_service_provider import (
    DominoServerProjectsDomainEntitiesProjectGitRepositoryServiceProvider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoServerProjectsDomainEntitiesProjectGitRepository")


@_attrs_define
class DominoServerProjectsDomainEntitiesProjectGitRepository:
    """
    Attributes:
        id (str):
        uri_host (str):
        uri_path (str):
        default_ref (DominoProjectsApiRepositoriesReferenceDTO):
        service_provider (DominoServerProjectsDomainEntitiesProjectGitRepositoryServiceProvider):
        uri_port (None | str | Unset):
        name (None | str | Unset):
    """

    id: str
    uri_host: str
    uri_path: str
    default_ref: DominoProjectsApiRepositoriesReferenceDTO
    service_provider: DominoServerProjectsDomainEntitiesProjectGitRepositoryServiceProvider
    uri_port: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uri_host = self.uri_host

        uri_path = self.uri_path

        default_ref = self.default_ref.to_dict()

        service_provider = self.service_provider.value

        uri_port: None | str | Unset
        if isinstance(self.uri_port, Unset):
            uri_port = UNSET
        else:
            uri_port = self.uri_port

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uriHost": uri_host,
                "uriPath": uri_path,
                "defaultRef": default_ref,
                "serviceProvider": service_provider,
            }
        )
        if uri_port is not UNSET:
            field_dict["uriPort"] = uri_port
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        id = d.pop("id")

        uri_host = d.pop("uriHost")

        uri_path = d.pop("uriPath")

        default_ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(d.pop("defaultRef"))

        service_provider = DominoServerProjectsDomainEntitiesProjectGitRepositoryServiceProvider(
            d.pop("serviceProvider")
        )

        def _parse_uri_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri_port = _parse_uri_port(d.pop("uriPort", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        domino_server_projects_domain_entities_project_git_repository = cls(
            id=id,
            uri_host=uri_host,
            uri_path=uri_path,
            default_ref=default_ref,
            service_provider=service_provider,
            uri_port=uri_port,
            name=name,
        )

        domino_server_projects_domain_entities_project_git_repository.additional_properties = d
        return domino_server_projects_domain_entities_project_git_repository

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
