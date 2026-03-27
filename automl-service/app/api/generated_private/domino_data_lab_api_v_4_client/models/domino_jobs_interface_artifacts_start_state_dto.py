from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_artifacts_object_dto import DominoJobsInterfaceArtifactsObjectDto


T = TypeVar("T", bound="DominoJobsInterfaceArtifactsStartStateDto")


@_attrs_define
class DominoJobsInterfaceArtifactsStartStateDto:
    """
    Attributes:
        project_artifacts (DominoJobsInterfaceArtifactsObjectDto):
        imported_project_artifacts (list[DominoJobsInterfaceArtifactsObjectDto]):
    """

    project_artifacts: DominoJobsInterfaceArtifactsObjectDto
    imported_project_artifacts: list[DominoJobsInterfaceArtifactsObjectDto]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_artifacts = self.project_artifacts.to_dict()

        imported_project_artifacts = []
        for imported_project_artifacts_item_data in self.imported_project_artifacts:
            imported_project_artifacts_item = imported_project_artifacts_item_data.to_dict()
            imported_project_artifacts.append(imported_project_artifacts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectArtifacts": project_artifacts,
                "importedProjectArtifacts": imported_project_artifacts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_artifacts_object_dto import DominoJobsInterfaceArtifactsObjectDto

        d = dict(src_dict)
        project_artifacts = DominoJobsInterfaceArtifactsObjectDto.from_dict(d.pop("projectArtifacts"))

        imported_project_artifacts = []
        _imported_project_artifacts = d.pop("importedProjectArtifacts")
        for imported_project_artifacts_item_data in _imported_project_artifacts:
            imported_project_artifacts_item = DominoJobsInterfaceArtifactsObjectDto.from_dict(
                imported_project_artifacts_item_data
            )

            imported_project_artifacts.append(imported_project_artifacts_item)

        domino_jobs_interface_artifacts_start_state_dto = cls(
            project_artifacts=project_artifacts,
            imported_project_artifacts=imported_project_artifacts,
        )

        domino_jobs_interface_artifacts_start_state_dto.additional_properties = d
        return domino_jobs_interface_artifacts_start_state_dto

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
