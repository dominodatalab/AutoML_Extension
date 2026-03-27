from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_admin_interface_compute_node_cpu_utilization import (
        DominoAdminInterfaceComputeNodeCpuUtilization,
    )
    from ..models.domino_admin_interface_compute_node_disk_utilization import (
        DominoAdminInterfaceComputeNodeDiskUtilization,
    )
    from ..models.domino_admin_interface_compute_node_mem_utilization import (
        DominoAdminInterfaceComputeNodeMemUtilization,
    )


T = TypeVar("T", bound="DominoAdminInterfaceComputeNodeUtilization")


@_attrs_define
class DominoAdminInterfaceComputeNodeUtilization:
    """
    Attributes:
        cpu_utilization (DominoAdminInterfaceComputeNodeCpuUtilization):
        mem_utilization (DominoAdminInterfaceComputeNodeMemUtilization):
        disk_utilization (DominoAdminInterfaceComputeNodeDiskUtilization):
    """

    cpu_utilization: DominoAdminInterfaceComputeNodeCpuUtilization
    mem_utilization: DominoAdminInterfaceComputeNodeMemUtilization
    disk_utilization: DominoAdminInterfaceComputeNodeDiskUtilization
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_utilization = self.cpu_utilization.to_dict()

        mem_utilization = self.mem_utilization.to_dict()

        disk_utilization = self.disk_utilization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpuUtilization": cpu_utilization,
                "memUtilization": mem_utilization,
                "diskUtilization": disk_utilization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_compute_node_cpu_utilization import (
            DominoAdminInterfaceComputeNodeCpuUtilization,
        )
        from ..models.domino_admin_interface_compute_node_disk_utilization import (
            DominoAdminInterfaceComputeNodeDiskUtilization,
        )
        from ..models.domino_admin_interface_compute_node_mem_utilization import (
            DominoAdminInterfaceComputeNodeMemUtilization,
        )

        d = dict(src_dict)
        cpu_utilization = DominoAdminInterfaceComputeNodeCpuUtilization.from_dict(d.pop("cpuUtilization"))

        mem_utilization = DominoAdminInterfaceComputeNodeMemUtilization.from_dict(d.pop("memUtilization"))

        disk_utilization = DominoAdminInterfaceComputeNodeDiskUtilization.from_dict(d.pop("diskUtilization"))

        domino_admin_interface_compute_node_utilization = cls(
            cpu_utilization=cpu_utilization,
            mem_utilization=mem_utilization,
            disk_utilization=disk_utilization,
        )

        domino_admin_interface_compute_node_utilization.additional_properties = d
        return domino_admin_interface_compute_node_utilization

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
