from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGruzApiPreparedRepository")


@_attrs_define
class DominoGruzApiPreparedRepository:
    """
    Attributes:
        id (str):
        name (str):
        uri_host (str):
        uri_path (str):
        service_provider (str):
        ref (str):
        uri_port (None | str | Unset):
        starting_ref (None | str | Unset):
        finished_ref (None | str | Unset):
        starting_branch (None | str | Unset):
        finished_branch (None | str | Unset):
    """

    id: str
    name: str
    uri_host: str
    uri_path: str
    service_provider: str
    ref: str
    uri_port: None | str | Unset = UNSET
    starting_ref: None | str | Unset = UNSET
    finished_ref: None | str | Unset = UNSET
    starting_branch: None | str | Unset = UNSET
    finished_branch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        uri_host = self.uri_host

        uri_path = self.uri_path

        service_provider = self.service_provider

        ref = self.ref

        uri_port: None | str | Unset
        if isinstance(self.uri_port, Unset):
            uri_port = UNSET
        else:
            uri_port = self.uri_port

        starting_ref: None | str | Unset
        if isinstance(self.starting_ref, Unset):
            starting_ref = UNSET
        else:
            starting_ref = self.starting_ref

        finished_ref: None | str | Unset
        if isinstance(self.finished_ref, Unset):
            finished_ref = UNSET
        else:
            finished_ref = self.finished_ref

        starting_branch: None | str | Unset
        if isinstance(self.starting_branch, Unset):
            starting_branch = UNSET
        else:
            starting_branch = self.starting_branch

        finished_branch: None | str | Unset
        if isinstance(self.finished_branch, Unset):
            finished_branch = UNSET
        else:
            finished_branch = self.finished_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "uriHost": uri_host,
                "uriPath": uri_path,
                "serviceProvider": service_provider,
                "ref": ref,
            }
        )
        if uri_port is not UNSET:
            field_dict["uriPort"] = uri_port
        if starting_ref is not UNSET:
            field_dict["startingRef"] = starting_ref
        if finished_ref is not UNSET:
            field_dict["finishedRef"] = finished_ref
        if starting_branch is not UNSET:
            field_dict["startingBranch"] = starting_branch
        if finished_branch is not UNSET:
            field_dict["finishedBranch"] = finished_branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        uri_host = d.pop("uriHost")

        uri_path = d.pop("uriPath")

        service_provider = d.pop("serviceProvider")

        ref = d.pop("ref")

        def _parse_uri_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uri_port = _parse_uri_port(d.pop("uriPort", UNSET))

        def _parse_starting_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_ref = _parse_starting_ref(d.pop("startingRef", UNSET))

        def _parse_finished_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_ref = _parse_finished_ref(d.pop("finishedRef", UNSET))

        def _parse_starting_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_branch = _parse_starting_branch(d.pop("startingBranch", UNSET))

        def _parse_finished_branch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_branch = _parse_finished_branch(d.pop("finishedBranch", UNSET))

        domino_gruz_api_prepared_repository = cls(
            id=id,
            name=name,
            uri_host=uri_host,
            uri_path=uri_path,
            service_provider=service_provider,
            ref=ref,
            uri_port=uri_port,
            starting_ref=starting_ref,
            finished_ref=finished_ref,
            starting_branch=starting_branch,
            finished_branch=finished_branch,
        )

        domino_gruz_api_prepared_repository.additional_properties = d
        return domino_gruz_api_prepared_repository

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
