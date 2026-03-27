from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_projects_api_project_gateway_run_count_for_type_run_type import (
    DominoServerProjectsApiProjectGatewayRunCountForTypeRunType,
)

T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewayRunCountForType")


@_attrs_define
class DominoServerProjectsApiProjectGatewayRunCountForType:
    """
    Attributes:
        run_type (DominoServerProjectsApiProjectGatewayRunCountForTypeRunType):
        executing_count (int):
        stopped_count (int):
    """

    run_type: DominoServerProjectsApiProjectGatewayRunCountForTypeRunType
    executing_count: int
    stopped_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_type = self.run_type.value

        executing_count = self.executing_count

        stopped_count = self.stopped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runType": run_type,
                "executingCount": executing_count,
                "stoppedCount": stopped_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_type = DominoServerProjectsApiProjectGatewayRunCountForTypeRunType(d.pop("runType"))

        executing_count = d.pop("executingCount")

        stopped_count = d.pop("stoppedCount")

        domino_server_projects_api_project_gateway_run_count_for_type = cls(
            run_type=run_type,
            executing_count=executing_count,
            stopped_count=stopped_count,
        )

        domino_server_projects_api_project_gateway_run_count_for_type.additional_properties = d
        return domino_server_projects_api_project_gateway_run_count_for_type

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
