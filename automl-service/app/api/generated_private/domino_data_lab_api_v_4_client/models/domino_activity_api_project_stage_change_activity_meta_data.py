from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage


T = TypeVar("T", bound="DominoActivityApiProjectStageChangeActivityMetaData")


@_attrs_define
class DominoActivityApiProjectStageChangeActivityMetaData:
    """
    Attributes:
        project_name (str):
        from_stage (DominoActivityApiProjectStage):
        to_stage (DominoActivityApiProjectStage):
    """

    project_name: str
    from_stage: DominoActivityApiProjectStage
    to_stage: DominoActivityApiProjectStage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_name = self.project_name

        from_stage = self.from_stage.to_dict()

        to_stage = self.to_stage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectName": project_name,
                "fromStage": from_stage,
                "toStage": to_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage

        d = dict(src_dict)
        project_name = d.pop("projectName")

        from_stage = DominoActivityApiProjectStage.from_dict(d.pop("fromStage"))

        to_stage = DominoActivityApiProjectStage.from_dict(d.pop("toStage"))

        domino_activity_api_project_stage_change_activity_meta_data = cls(
            project_name=project_name,
            from_stage=from_stage,
            to_stage=to_stage,
        )

        domino_activity_api_project_stage_change_activity_meta_data.additional_properties = d
        return domino_activity_api_project_stage_change_activity_meta_data

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
