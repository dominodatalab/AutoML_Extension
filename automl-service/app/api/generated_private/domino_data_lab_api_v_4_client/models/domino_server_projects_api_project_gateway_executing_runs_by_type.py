from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_server_projects_api_project_gateway_executing_runs_by_type_run_type import (
    DominoServerProjectsApiProjectGatewayExecutingRunsByTypeRunType,
)

T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewayExecutingRunsByType")


@_attrs_define
class DominoServerProjectsApiProjectGatewayExecutingRunsByType:
    """
    Attributes:
        run_type (DominoServerProjectsApiProjectGatewayExecutingRunsByTypeRunType):
        count (int):
    """

    run_type: DominoServerProjectsApiProjectGatewayExecutingRunsByTypeRunType
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_type = self.run_type.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runType": run_type,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_type = DominoServerProjectsApiProjectGatewayExecutingRunsByTypeRunType(d.pop("runType"))

        count = d.pop("count")

        domino_server_projects_api_project_gateway_executing_runs_by_type = cls(
            run_type=run_type,
            count=count,
        )

        domino_server_projects_api_project_gateway_executing_runs_by_type.additional_properties = d
        return domino_server_projects_api_project_gateway_executing_runs_by_type

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
