from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoJobsInterfaceDependentRepository")


@_attrs_define
class DominoJobsInterfaceDependentRepository:
    """
    Attributes:
        id (str):
        name (str):
        uri (str):
        ref (str):
        service_provider (str):
        starting_commit_id (None | str | Unset):
        starting_commit_uri (None | str | Unset):
        finished_commit_id (None | str | Unset):
        finished_commit_uri (None | str | Unset):
        starting_branch (None | str | Unset):
        finished_branch (None | str | Unset):
    """

    id: str
    name: str
    uri: str
    ref: str
    service_provider: str
    starting_commit_id: None | str | Unset = UNSET
    starting_commit_uri: None | str | Unset = UNSET
    finished_commit_id: None | str | Unset = UNSET
    finished_commit_uri: None | str | Unset = UNSET
    starting_branch: None | str | Unset = UNSET
    finished_branch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        uri = self.uri

        ref = self.ref

        service_provider = self.service_provider

        starting_commit_id: None | str | Unset
        if isinstance(self.starting_commit_id, Unset):
            starting_commit_id = UNSET
        else:
            starting_commit_id = self.starting_commit_id

        starting_commit_uri: None | str | Unset
        if isinstance(self.starting_commit_uri, Unset):
            starting_commit_uri = UNSET
        else:
            starting_commit_uri = self.starting_commit_uri

        finished_commit_id: None | str | Unset
        if isinstance(self.finished_commit_id, Unset):
            finished_commit_id = UNSET
        else:
            finished_commit_id = self.finished_commit_id

        finished_commit_uri: None | str | Unset
        if isinstance(self.finished_commit_uri, Unset):
            finished_commit_uri = UNSET
        else:
            finished_commit_uri = self.finished_commit_uri

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
                "uri": uri,
                "ref": ref,
                "serviceProvider": service_provider,
            }
        )
        if starting_commit_id is not UNSET:
            field_dict["startingCommitId"] = starting_commit_id
        if starting_commit_uri is not UNSET:
            field_dict["startingCommitUri"] = starting_commit_uri
        if finished_commit_id is not UNSET:
            field_dict["finishedCommitId"] = finished_commit_id
        if finished_commit_uri is not UNSET:
            field_dict["finishedCommitUri"] = finished_commit_uri
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

        uri = d.pop("uri")

        ref = d.pop("ref")

        service_provider = d.pop("serviceProvider")

        def _parse_starting_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_commit_id = _parse_starting_commit_id(d.pop("startingCommitId", UNSET))

        def _parse_starting_commit_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starting_commit_uri = _parse_starting_commit_uri(d.pop("startingCommitUri", UNSET))

        def _parse_finished_commit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_commit_id = _parse_finished_commit_id(d.pop("finishedCommitId", UNSET))

        def _parse_finished_commit_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finished_commit_uri = _parse_finished_commit_uri(d.pop("finishedCommitUri", UNSET))

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

        domino_jobs_interface_dependent_repository = cls(
            id=id,
            name=name,
            uri=uri,
            ref=ref,
            service_provider=service_provider,
            starting_commit_id=starting_commit_id,
            starting_commit_uri=starting_commit_uri,
            finished_commit_id=finished_commit_id,
            finished_commit_uri=finished_commit_uri,
            starting_branch=starting_branch,
            finished_branch=finished_branch,
        )

        domino_jobs_interface_dependent_repository.additional_properties = d
        return domino_jobs_interface_dependent_repository

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
