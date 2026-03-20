from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_results_settings_v1_branch import ProjectResultsSettingsV1Branch

T = TypeVar("T", bound="ProjectResultsSettingsV1")


@_attrs_define
class ProjectResultsSettingsV1:
    """
    Attributes:
        branch (ProjectResultsSettingsV1Branch):
    """

    branch: ProjectResultsSettingsV1Branch
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = ProjectResultsSettingsV1Branch(d.pop("branch"))

        project_results_settings_v1 = cls(
            branch=branch,
        )

        project_results_settings_v1.additional_properties = d
        return project_results_settings_v1

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
