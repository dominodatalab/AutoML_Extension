from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectManagementWebFilterProjectGoals")


@_attrs_define
class DominoProjectManagementWebFilterProjectGoals:
    """
    Attributes:
        stage_ids (list[str] | None | Unset):
        assignee_ids (list[str] | None | Unset):
    """

    stage_ids: list[str] | None | Unset = UNSET
    assignee_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_ids: list[str] | None | Unset
        if isinstance(self.stage_ids, Unset):
            stage_ids = UNSET
        elif isinstance(self.stage_ids, list):
            stage_ids = self.stage_ids

        else:
            stage_ids = self.stage_ids

        assignee_ids: list[str] | None | Unset
        if isinstance(self.assignee_ids, Unset):
            assignee_ids = UNSET
        elif isinstance(self.assignee_ids, list):
            assignee_ids = self.assignee_ids

        else:
            assignee_ids = self.assignee_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage_ids is not UNSET:
            field_dict["stageIds"] = stage_ids
        if assignee_ids is not UNSET:
            field_dict["assigneeIds"] = assignee_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_stage_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stage_ids_type_0 = cast(list[str], data)

                return stage_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        stage_ids = _parse_stage_ids(d.pop("stageIds", UNSET))

        def _parse_assignee_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignee_ids_type_0 = cast(list[str], data)

                return assignee_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assignee_ids = _parse_assignee_ids(d.pop("assigneeIds", UNSET))

        domino_project_management_web_filter_project_goals = cls(
            stage_ids=stage_ids,
            assignee_ids=assignee_ids,
        )

        domino_project_management_web_filter_project_goals.additional_properties = d
        return domino_project_management_web_filter_project_goals

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
