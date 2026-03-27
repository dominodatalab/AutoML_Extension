from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_artifacts_object_dto import DominoJobsInterfaceArtifactsObjectDto
    from ..models.domino_jobs_interface_artifacts_start_state_dto import DominoJobsInterfaceArtifactsStartStateDto


T = TypeVar("T", bound="DominoJobsInterfaceArtifactsInfoDto")


@_attrs_define
class DominoJobsInterfaceArtifactsInfoDto:
    """
    Attributes:
        start_state (DominoJobsInterfaceArtifactsStartStateDto):
        end_state (DominoJobsInterfaceArtifactsObjectDto):
        changes (list[str]):
    """

    start_state: DominoJobsInterfaceArtifactsStartStateDto
    end_state: DominoJobsInterfaceArtifactsObjectDto
    changes: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_state = self.start_state.to_dict()

        end_state = self.end_state.to_dict()

        changes = self.changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startState": start_state,
                "endState": end_state,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_artifacts_object_dto import DominoJobsInterfaceArtifactsObjectDto
        from ..models.domino_jobs_interface_artifacts_start_state_dto import DominoJobsInterfaceArtifactsStartStateDto

        d = dict(src_dict)
        start_state = DominoJobsInterfaceArtifactsStartStateDto.from_dict(d.pop("startState"))

        end_state = DominoJobsInterfaceArtifactsObjectDto.from_dict(d.pop("endState"))

        changes = cast(list[str], d.pop("changes"))

        domino_jobs_interface_artifacts_info_dto = cls(
            start_state=start_state,
            end_state=end_state,
            changes=changes,
        )

        domino_jobs_interface_artifacts_info_dto.additional_properties = d
        return domino_jobs_interface_artifacts_info_dto

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
