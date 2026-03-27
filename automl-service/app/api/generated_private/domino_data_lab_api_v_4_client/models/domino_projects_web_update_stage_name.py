from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoProjectsWebUpdateStageName")


@_attrs_define
class DominoProjectsWebUpdateStageName:
    """
    Attributes:
        stage_id (str):
        stage_name (str):
    """

    stage_id: str
    stage_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stageId": stage_id,
                "stageName": stage_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stageId")

        stage_name = d.pop("stageName")

        domino_projects_web_update_stage_name = cls(
            stage_id=stage_id,
            stage_name=stage_name,
        )

        domino_projects_web_update_stage_name.additional_properties = d
        return domino_projects_web_update_stage_name

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
