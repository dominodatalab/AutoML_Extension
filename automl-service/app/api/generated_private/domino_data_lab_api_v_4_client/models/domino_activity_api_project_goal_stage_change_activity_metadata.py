from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage


T = TypeVar("T", bound="DominoActivityApiProjectGoalStageChangeActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalStageChangeActivityMetadata:
    """
    Attributes:
        from_stage (DominoActivityApiProjectStage):
        to_stage (DominoActivityApiProjectStage):
        title (str):
    """

    from_stage: DominoActivityApiProjectStage
    to_stage: DominoActivityApiProjectStage
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_stage = self.from_stage.to_dict()

        to_stage = self.to_stage.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromStage": from_stage,
                "toStage": to_stage,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_project_stage import DominoActivityApiProjectStage

        d = dict(src_dict)
        from_stage = DominoActivityApiProjectStage.from_dict(d.pop("fromStage"))

        to_stage = DominoActivityApiProjectStage.from_dict(d.pop("toStage"))

        title = d.pop("title")

        domino_activity_api_project_goal_stage_change_activity_metadata = cls(
            from_stage=from_stage,
            to_stage=to_stage,
            title=title,
        )

        domino_activity_api_project_goal_stage_change_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_stage_change_activity_metadata

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
