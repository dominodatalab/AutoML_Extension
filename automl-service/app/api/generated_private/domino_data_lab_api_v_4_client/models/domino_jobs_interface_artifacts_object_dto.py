from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoJobsInterfaceArtifactsObjectDto")


@_attrs_define
class DominoJobsInterfaceArtifactsObjectDto:
    """
    Attributes:
        commit_id (str):
        project_name (str):
        owner_name (str):
    """

    commit_id: str
    project_name: str
    owner_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        project_name = self.project_name

        owner_name = self.owner_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "projectName": project_name,
                "ownerName": owner_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_id = d.pop("commitId")

        project_name = d.pop("projectName")

        owner_name = d.pop("ownerName")

        domino_jobs_interface_artifacts_object_dto = cls(
            commit_id=commit_id,
            project_name=project_name,
            owner_name=owner_name,
        )

        domino_jobs_interface_artifacts_object_dto.additional_properties = d
        return domino_jobs_interface_artifacts_object_dto

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
