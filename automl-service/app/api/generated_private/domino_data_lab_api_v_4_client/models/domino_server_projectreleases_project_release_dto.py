from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoServerProjectreleasesProjectReleaseDto")


@_attrs_define
class DominoServerProjectreleasesProjectReleaseDto:
    """
    Attributes:
        project_id (str):
        run_id (str):
        created_at (int):
        created_by (str):
    """

    project_id: str
    run_id: str
    created_at: int
    created_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        run_id = self.run_id

        created_at = self.created_at

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "runId": run_id,
                "createdAt": created_at,
                "createdBy": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId")

        run_id = d.pop("runId")

        created_at = d.pop("createdAt")

        created_by = d.pop("createdBy")

        domino_server_projectreleases_project_release_dto = cls(
            project_id=project_id,
            run_id=run_id,
            created_at=created_at,
            created_by=created_by,
        )

        domino_server_projectreleases_project_release_dto.additional_properties = d
        return domino_server_projectreleases_project_release_dto

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
