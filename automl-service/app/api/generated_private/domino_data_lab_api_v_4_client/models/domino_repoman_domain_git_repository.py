from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_repoman_domain_git_repository_service_provider import (
    DominoRepomanDomainGitRepositoryServiceProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoRepomanDomainGitRepository")


@_attrs_define
class DominoRepomanDomainGitRepository:
    """
    Attributes:
        id (str):
        name (str):
        uri_host (str):
        uri_path (str):
        service_provider (DominoRepomanDomainGitRepositoryServiceProvider):
        uri_port (None | str | Unset):
        is_feature_store (bool | None | Unset):
    """

    id: str
    name: str
    uri_host: str
    uri_path: str
    service_provider: DominoRepomanDomainGitRepositoryServiceProvider
    uri_port: None | str | Unset = UNSET
    is_feature_store: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        uri_host = self.uri_host

        uri_path = self.uri_path

        service_provider = self.service_provider.value

        uri_port: None | str | Unset
        if isinstance(self.uri_port, Unset):
            uri_port = UNSET
        else:
            uri_port = self.uri_port

        is_feature_store: bool | None | Unset
        if isinstance(self.is_feature_store, Unset):
            is_feature_store = UNSET
        else:
            is_feature_store = self.is_feature_store

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "uriHost": uri_host,
                "uriPath": uri_path,
                "serviceProvider": service_provider,
            }
        )
        if uri_port is not UNSET:
            field_dict["uriPort"] = uri_port
        if is_feature_store is not UNSET:
            field_dict["isFeatureStore"] = is_feature_store

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        uri_host = d.pop("uriHost")

        uri_path = d.pop("uriPath")

        service_provider = DominoRepomanDomainGitRepositoryServiceProvider(d.pop("serviceProvider"))

        def _parse_uri_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri_port = _parse_uri_port(d.pop("uriPort", UNSET))

        def _parse_is_feature_store(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_feature_store = _parse_is_feature_store(d.pop("isFeatureStore", UNSET))

        domino_repoman_domain_git_repository = cls(
            id=id,
            name=name,
            uri_host=uri_host,
            uri_path=uri_path,
            service_provider=service_provider,
            uri_port=uri_port,
            is_feature_store=is_feature_store,
        )

        domino_repoman_domain_git_repository.additional_properties = d
        return domino_repoman_domain_git_repository

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
