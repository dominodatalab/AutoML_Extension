from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_computegrid_execution_unit_overview_deployable_object_type import (
    DominoComputegridExecutionUnitOverviewDeployableObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoComputegridExecutionUnitOverview")


@_attrs_define
class DominoComputegridExecutionUnitOverview:
    """
    Attributes:
        deployable_object_type (DominoComputegridExecutionUnitOverviewDeployableObjectType):
        deployable_object_id (str):
        status (str):
        compute_node_id (None | str | Unset):
    """

    deployable_object_type: DominoComputegridExecutionUnitOverviewDeployableObjectType
    deployable_object_id: str
    status: str
    compute_node_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployable_object_type = self.deployable_object_type.value

        deployable_object_id = self.deployable_object_id

        status = self.status

        compute_node_id: None | str | Unset
        if isinstance(self.compute_node_id, Unset):
            compute_node_id = UNSET
        else:
            compute_node_id = self.compute_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deployableObjectType": deployable_object_type,
                "deployableObjectId": deployable_object_id,
                "status": status,
            }
        )
        if compute_node_id is not UNSET:
            field_dict["computeNodeId"] = compute_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployable_object_type = DominoComputegridExecutionUnitOverviewDeployableObjectType(
            d.pop("deployableObjectType")
        )

        deployable_object_id = d.pop("deployableObjectId")

        status = d.pop("status")

        def _parse_compute_node_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compute_node_id = _parse_compute_node_id(d.pop("computeNodeId", UNSET))

        domino_computegrid_execution_unit_overview = cls(
            deployable_object_type=deployable_object_type,
            deployable_object_id=deployable_object_id,
            status=status,
            compute_node_id=compute_node_id,
        )

        domino_computegrid_execution_unit_overview.additional_properties = d
        return domino_computegrid_execution_unit_overview

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
