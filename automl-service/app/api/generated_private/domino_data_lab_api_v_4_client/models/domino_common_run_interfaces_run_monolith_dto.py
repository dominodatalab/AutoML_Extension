from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_common_run_interfaces_run_monolith_dto_status import DominoCommonRunInterfacesRunMonolithDTOStatus

T = TypeVar("T", bound="DominoCommonRunInterfacesRunMonolithDTO")


@_attrs_define
class DominoCommonRunInterfacesRunMonolithDTO:
    """
    Attributes:
        id (str):
        title (str):
        command (str):
        start_time (str):
        next_fire_time (str):
        project_id (str):
        project_identity (str):
        run_type (str):
        hardware_tier_name (str):
        run_duration_in_seconds (float):
        estimated_cost (float):
        status (DominoCommonRunInterfacesRunMonolithDTOStatus):
    """

    id: str
    title: str
    command: str
    start_time: str
    next_fire_time: str
    project_id: str
    project_identity: str
    run_type: str
    hardware_tier_name: str
    run_duration_in_seconds: float
    estimated_cost: float
    status: DominoCommonRunInterfacesRunMonolithDTOStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        command = self.command

        start_time = self.start_time

        next_fire_time = self.next_fire_time

        project_id = self.project_id

        project_identity = self.project_identity

        run_type = self.run_type

        hardware_tier_name = self.hardware_tier_name

        run_duration_in_seconds = self.run_duration_in_seconds

        estimated_cost = self.estimated_cost

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "command": command,
                "startTime": start_time,
                "nextFireTime": next_fire_time,
                "projectId": project_id,
                "projectIdentity": project_identity,
                "runType": run_type,
                "hardwareTierName": hardware_tier_name,
                "runDurationInSeconds": run_duration_in_seconds,
                "estimatedCost": estimated_cost,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        command = d.pop("command")

        start_time = d.pop("startTime")

        next_fire_time = d.pop("nextFireTime")

        project_id = d.pop("projectId")

        project_identity = d.pop("projectIdentity")

        run_type = d.pop("runType")

        hardware_tier_name = d.pop("hardwareTierName")

        run_duration_in_seconds = d.pop("runDurationInSeconds")

        estimated_cost = d.pop("estimatedCost")

        status = DominoCommonRunInterfacesRunMonolithDTOStatus(d.pop("status"))

        domino_common_run_interfaces_run_monolith_dto = cls(
            id=id,
            title=title,
            command=command,
            start_time=start_time,
            next_fire_time=next_fire_time,
            project_id=project_id,
            project_identity=project_identity,
            run_type=run_type,
            hardware_tier_name=hardware_tier_name,
            run_duration_in_seconds=run_duration_in_seconds,
            estimated_cost=estimated_cost,
            status=status,
        )

        domino_common_run_interfaces_run_monolith_dto.additional_properties = d
        return domino_common_run_interfaces_run_monolith_dto

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
