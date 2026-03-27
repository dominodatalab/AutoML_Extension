from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO


T = TypeVar("T", bound="DominoProjectsApiRepositoriesGitRepositoryDTO")


@_attrs_define
class DominoProjectsApiRepositoriesGitRepositoryDTO:
    """
    Attributes:
        uri (str):
        ref (DominoProjectsApiRepositoriesReferenceDTO):
        service_provider (str):
        id (None | str | Unset):
        name (None | str | Unset):
        credential_id (None | str | Unset):
    """

    uri: str
    ref: DominoProjectsApiRepositoriesReferenceDTO
    service_provider: str
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    credential_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        ref = self.ref.to_dict()

        service_provider = self.service_provider

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        credential_id: None | str | Unset
        if isinstance(self.credential_id, Unset):
            credential_id = UNSET
        else:
            credential_id = self.credential_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "ref": ref,
                "serviceProvider": service_provider,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if credential_id is not UNSET:
            field_dict["credentialId"] = credential_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_repositories_reference_dto import DominoProjectsApiRepositoriesReferenceDTO

        d = dict(src_dict)
        uri = d.pop("uri")

        ref = DominoProjectsApiRepositoriesReferenceDTO.from_dict(d.pop("ref"))

        service_provider = d.pop("serviceProvider")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_credential_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        credential_id = _parse_credential_id(d.pop("credentialId", UNSET))

        domino_projects_api_repositories_git_repository_dto = cls(
            uri=uri,
            ref=ref,
            service_provider=service_provider,
            id=id,
            name=name,
            credential_id=credential_id,
        )

        domino_projects_api_repositories_git_repository_dto.additional_properties = d
        return domino_projects_api_repositories_git_repository_dto

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
