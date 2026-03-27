from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_computegrid_monitored_execution_resource_list_combined_resource_status import (
    DominoComputegridMonitoredExecutionResourceListCombinedResourceStatus,
)

if TYPE_CHECKING:
    from ..models.domino_computegrid_monitored_execution_resource import DominoComputegridMonitoredExecutionResource


T = TypeVar("T", bound="DominoComputegridMonitoredExecutionResourceList")


@_attrs_define
class DominoComputegridMonitoredExecutionResourceList:
    """
    Attributes:
        resource_plural_name (str):
        resource_singular_name (str):
        resources (list[DominoComputegridMonitoredExecutionResource]):
        combined_resource_status (DominoComputegridMonitoredExecutionResourceListCombinedResourceStatus):
    """

    resource_plural_name: str
    resource_singular_name: str
    resources: list[DominoComputegridMonitoredExecutionResource]
    combined_resource_status: DominoComputegridMonitoredExecutionResourceListCombinedResourceStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_plural_name = self.resource_plural_name

        resource_singular_name = self.resource_singular_name

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        combined_resource_status = self.combined_resource_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourcePluralName": resource_plural_name,
                "resourceSingularName": resource_singular_name,
                "resources": resources,
                "combinedResourceStatus": combined_resource_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computegrid_monitored_execution_resource import DominoComputegridMonitoredExecutionResource

        d = dict(src_dict)
        resource_plural_name = d.pop("resourcePluralName")

        resource_singular_name = d.pop("resourceSingularName")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = DominoComputegridMonitoredExecutionResource.from_dict(resources_item_data)

            resources.append(resources_item)

        combined_resource_status = DominoComputegridMonitoredExecutionResourceListCombinedResourceStatus(
            d.pop("combinedResourceStatus")
        )

        domino_computegrid_monitored_execution_resource_list = cls(
            resource_plural_name=resource_plural_name,
            resource_singular_name=resource_singular_name,
            resources=resources,
            combined_resource_status=combined_resource_status,
        )

        domino_computegrid_monitored_execution_resource_list.additional_properties = d
        return domino_computegrid_monitored_execution_resource_list

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
