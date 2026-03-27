from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_project_goal_status_change_activity_metadata_from_status import (
    DominoActivityApiProjectGoalStatusChangeActivityMetadataFromStatus,
)
from ..models.domino_activity_api_project_goal_status_change_activity_metadata_to_status import (
    DominoActivityApiProjectGoalStatusChangeActivityMetadataToStatus,
)

T = TypeVar("T", bound="DominoActivityApiProjectGoalStatusChangeActivityMetadata")


@_attrs_define
class DominoActivityApiProjectGoalStatusChangeActivityMetadata:
    """
    Attributes:
        from_status (DominoActivityApiProjectGoalStatusChangeActivityMetadataFromStatus):
        to_status (DominoActivityApiProjectGoalStatusChangeActivityMetadataToStatus):
        project_goal_title (str):
    """

    from_status: DominoActivityApiProjectGoalStatusChangeActivityMetadataFromStatus
    to_status: DominoActivityApiProjectGoalStatusChangeActivityMetadataToStatus
    project_goal_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_status = self.from_status.value

        to_status = self.to_status.value

        project_goal_title = self.project_goal_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromStatus": from_status,
                "toStatus": to_status,
                "projectGoalTitle": project_goal_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_status = DominoActivityApiProjectGoalStatusChangeActivityMetadataFromStatus(d.pop("fromStatus"))

        to_status = DominoActivityApiProjectGoalStatusChangeActivityMetadataToStatus(d.pop("toStatus"))

        project_goal_title = d.pop("projectGoalTitle")

        domino_activity_api_project_goal_status_change_activity_metadata = cls(
            from_status=from_status,
            to_status=to_status,
            project_goal_title=project_goal_title,
        )

        domino_activity_api_project_goal_status_change_activity_metadata.additional_properties = d
        return domino_activity_api_project_goal_status_change_activity_metadata

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
