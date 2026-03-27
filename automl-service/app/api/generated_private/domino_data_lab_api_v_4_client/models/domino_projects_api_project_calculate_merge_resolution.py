from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_calculate_merge_resolution_decisions import (
        DominoProjectsApiProjectCalculateMergeResolutionDecisions,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectCalculateMergeResolution")


@_attrs_define
class DominoProjectsApiProjectCalculateMergeResolution:
    """
    Attributes:
        into_project_id (str):
        from_project_id (str):
        decisions (DominoProjectsApiProjectCalculateMergeResolutionDecisions):  Example: {'nested/file.text': 'Keep',
            'root.file': 'Accept'}.
    """

    into_project_id: str
    from_project_id: str
    decisions: DominoProjectsApiProjectCalculateMergeResolutionDecisions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        into_project_id = self.into_project_id

        from_project_id = self.from_project_id

        decisions = self.decisions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intoProjectId": into_project_id,
                "fromProjectId": from_project_id,
                "decisions": decisions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_calculate_merge_resolution_decisions import (
            DominoProjectsApiProjectCalculateMergeResolutionDecisions,
        )

        d = dict(src_dict)
        into_project_id = d.pop("intoProjectId")

        from_project_id = d.pop("fromProjectId")

        decisions = DominoProjectsApiProjectCalculateMergeResolutionDecisions.from_dict(d.pop("decisions"))

        domino_projects_api_project_calculate_merge_resolution = cls(
            into_project_id=into_project_id,
            from_project_id=from_project_id,
            decisions=decisions,
        )

        domino_projects_api_project_calculate_merge_resolution.additional_properties = d
        return domino_projects_api_project_calculate_merge_resolution

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
