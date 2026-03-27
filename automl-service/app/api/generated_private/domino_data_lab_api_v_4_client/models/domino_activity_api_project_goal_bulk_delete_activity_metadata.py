from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_goal_bulk_delete_activity_metadata_to_status import (
    DominoActivityApiProjectGoalBulkDeleteActivityMetadataToStatus,
)

T = TypeVar("T", bound="DominoActivityApiProjectGoalBulkDeleteActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalBulkDeleteActivityMetadata:
    """
    Attributes:
        goal_ids (list[str]):
        goal_names (list[str]):
        to_status (DominoActivityApiProjectGoalBulkDeleteActivityMetadataToStatus):
    """

    goal_ids: list[str]
    goal_names: list[str]
    to_status: DominoActivityApiProjectGoalBulkDeleteActivityMetadataToStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goal_ids = self.goal_ids

        goal_names = self.goal_names

        to_status = self.to_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goalIds": goal_ids,
                "goalNames": goal_names,
                "toStatus": to_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goal_ids = cast(list[str], d.pop("goalIds"))

        goal_names = cast(list[str], d.pop("goalNames"))

        to_status = DominoActivityApiProjectGoalBulkDeleteActivityMetadataToStatus(d.pop("toStatus"))

        domino_activity_api_project_goal_bulk_delete_activity_metadata = cls(
            goal_ids=goal_ids,
            goal_names=goal_names,
            to_status=to_status,
        )

        domino_activity_api_project_goal_bulk_delete_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_bulk_delete_activity_metadata

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
