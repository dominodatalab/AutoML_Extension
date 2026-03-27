from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_projects_api_main_repository_details_service_provider import (
    DominoServerProjectsApiMainRepositoryDetailsServiceProvider,
)

T = TypeVar("T", bound="DominoServerProjectsApiMainRepositoryDetails")


@_attrs_define
class DominoServerProjectsApiMainRepositoryDetails:
    """
    Attributes:
        uri (str):
        id (str):
        service_provider (DominoServerProjectsApiMainRepositoryDetailsServiceProvider):
    """

    uri: str
    id: str
    service_provider: DominoServerProjectsApiMainRepositoryDetailsServiceProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        id = self.id

        service_provider = self.service_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "id": id,
                "serviceProvider": service_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        id = d.pop("id")

        service_provider = DominoServerProjectsApiMainRepositoryDetailsServiceProvider(d.pop("serviceProvider"))

        domino_server_projects_api_main_repository_details = cls(
            uri=uri,
            id=id,
            service_provider=service_provider,
        )

        domino_server_projects_api_main_repository_details.additional_properties = d
        return domino_server_projects_api_main_repository_details

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
