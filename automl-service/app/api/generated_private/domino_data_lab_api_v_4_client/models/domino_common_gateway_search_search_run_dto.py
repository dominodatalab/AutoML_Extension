from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoCommonGatewaySearchSearchRunDTO")


@_attrs_define
class DominoCommonGatewaySearchSearchRunDTO:
    """
    Attributes:
        command (str):
        status (str):
        completed (str):
        duration (str):
        owner_name (str):
        project_name (str):
        job_link (str):
        result_link (str):
    """

    command: str
    status: str
    completed: str
    duration: str
    owner_name: str
    project_name: str
    job_link: str
    result_link: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        status = self.status

        completed = self.completed

        duration = self.duration

        owner_name = self.owner_name

        project_name = self.project_name

        job_link = self.job_link

        result_link = self.result_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "status": status,
                "completed": completed,
                "duration": duration,
                "ownerName": owner_name,
                "projectName": project_name,
                "jobLink": job_link,
                "resultLink": result_link,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        status = d.pop("status")

        completed = d.pop("completed")

        duration = d.pop("duration")

        owner_name = d.pop("ownerName")

        project_name = d.pop("projectName")

        job_link = d.pop("jobLink")

        result_link = d.pop("resultLink")

        domino_common_gateway_search_search_run_dto = cls(
            command=command,
            status=status,
            completed=completed,
            duration=duration,
            owner_name=owner_name,
            project_name=project_name,
            job_link=job_link,
            result_link=result_link,
        )

        domino_common_gateway_search_search_run_dto.additional_properties = d
        return domino_common_gateway_search_search_run_dto

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
