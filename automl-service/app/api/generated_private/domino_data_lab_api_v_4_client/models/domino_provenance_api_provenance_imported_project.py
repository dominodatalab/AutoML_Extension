from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProvenanceApiProvenanceImportedProject")


@_attrs_define
class DominoProvenanceApiProvenanceImportedProject:
    """
    Attributes:
        project_id (str):
        project_name (str):
        owner_id (str):
        commit_id (str):
        directory_name (None | str | Unset):
        release (None | str | Unset):
    """

    project_id: str
    project_name: str
    owner_id: str
    commit_id: str
    directory_name: None | str | Unset = UNSET
    release: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        owner_id = self.owner_id

        commit_id = self.commit_id

        directory_name: None | str | Unset
        if isinstance(self.directory_name, Unset):
            directory_name = UNSET
        else:
            directory_name = self.directory_name

        release: None | str | Unset
        if isinstance(self.release, Unset):
            release = UNSET
        else:
            release = self.release

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "projectName": project_name,
                "ownerId": owner_id,
                "commitId": commit_id,
            }
        )
        if directory_name is not UNSET:
            field_dict["directoryName"] = directory_name
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        project_name = d.pop("projectName")

        owner_id = d.pop("ownerId")

        commit_id = d.pop("commitId")

        def _parse_directory_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_name = _parse_directory_name(d.pop("directoryName", UNSET))

        def _parse_release(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        release = _parse_release(d.pop("release", UNSET))

        domino_provenance_api_provenance_imported_project = cls(
            project_id=project_id,
            project_name=project_name,
            owner_id=owner_id,
            commit_id=commit_id,
            directory_name=directory_name,
            release=release,
        )

        domino_provenance_api_provenance_imported_project.additional_properties = d
        return domino_provenance_api_provenance_imported_project

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
