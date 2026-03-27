from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage
    from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus


T = TypeVar("T", bound="DominoProjectsApiProjectStageAndStatus")


@_attrs_define
class DominoProjectsApiProjectStageAndStatus:
    """
    Attributes:
        id (str):
        name (str):
        stage (DominoProjectsApiProjectStage):
        status (DominoProjectsApiProjectStatus):
        last_stage_change_in_millis (int | None | Unset):
        last_status_change_in_millis (int | None | Unset):
    """

    id: str
    name: str
    stage: DominoProjectsApiProjectStage
    status: DominoProjectsApiProjectStatus
    last_stage_change_in_millis: int | None | Unset = UNSET
    last_status_change_in_millis: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage = self.stage.to_dict()

        status = self.status.to_dict()

        last_stage_change_in_millis: int | None | Unset
        if isinstance(self.last_stage_change_in_millis, Unset):
            last_stage_change_in_millis = UNSET
        else:
            last_stage_change_in_millis = self.last_stage_change_in_millis

        last_status_change_in_millis: int | None | Unset
        if isinstance(self.last_status_change_in_millis, Unset):
            last_status_change_in_millis = UNSET
        else:
            last_status_change_in_millis = self.last_status_change_in_millis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage": stage,
                "status": status,
            }
        )
        if last_stage_change_in_millis is not UNSET:
            field_dict["lastStageChangeInMillis"] = last_stage_change_in_millis
        if last_status_change_in_millis is not UNSET:
            field_dict["lastStatusChangeInMillis"] = last_status_change_in_millis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_stage import DominoProjectsApiProjectStage
        from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage = DominoProjectsApiProjectStage.from_dict(d.pop("stage"))

        status = DominoProjectsApiProjectStatus.from_dict(d.pop("status"))

        def _parse_last_stage_change_in_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_stage_change_in_millis = _parse_last_stage_change_in_millis(d.pop("lastStageChangeInMillis", UNSET))

        def _parse_last_status_change_in_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_status_change_in_millis = _parse_last_status_change_in_millis(d.pop("lastStatusChangeInMillis", UNSET))

        domino_projects_api_project_stage_and_status = cls(
            id=id,
            name=name,
            stage=stage,
            status=status,
            last_stage_change_in_millis=last_stage_change_in_millis,
            last_status_change_in_millis=last_status_change_in_millis,
        )

        domino_projects_api_project_stage_and_status.additional_properties = d
        return domino_projects_api_project_stage_and_status

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
