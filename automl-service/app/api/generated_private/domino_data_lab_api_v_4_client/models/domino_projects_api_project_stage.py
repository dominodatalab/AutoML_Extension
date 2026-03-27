from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_project_stage_stage_creation_source import (
    DominoProjectsApiProjectStageStageCreationSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiProjectStage")


@_attrs_define
class DominoProjectsApiProjectStage:
    """
    Attributes:
        id (str):
        stage (str):
        created_at (int):
        is_archived (bool):
        stage_creation_source (DominoProjectsApiProjectStageStageCreationSource):
        created_by (None | str | Unset):
    """

    id: str
    stage: str
    created_at: int
    is_archived: bool
    stage_creation_source: DominoProjectsApiProjectStageStageCreationSource
    created_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        stage = self.stage

        created_at = self.created_at

        is_archived = self.is_archived

        stage_creation_source = self.stage_creation_source.value

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "stage": stage,
                "createdAt": created_at,
                "isArchived": is_archived,
                "stageCreationSource": stage_creation_source,
            }
        )
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        stage = d.pop("stage")

        created_at = d.pop("createdAt")

        is_archived = d.pop("isArchived")

        stage_creation_source = DominoProjectsApiProjectStageStageCreationSource(d.pop("stageCreationSource"))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        domino_projects_api_project_stage = cls(
            id=id,
            stage=stage,
            created_at=created_at,
            is_archived=is_archived,
            stage_creation_source=stage_creation_source,
            created_by=created_by,
        )

        domino_projects_api_project_stage.additional_properties = d
        return domino_projects_api_project_stage

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
