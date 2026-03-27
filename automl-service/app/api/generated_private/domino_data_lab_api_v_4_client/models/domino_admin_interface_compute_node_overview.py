from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_admin_interface_compute_node_status import DominoAdminInterfaceComputeNodeStatus
    from ..models.domino_admin_interface_compute_node_utilization import DominoAdminInterfaceComputeNodeUtilization


T = TypeVar("T", bound="DominoAdminInterfaceComputeNodeOverview")


@_attrs_define
class DominoAdminInterfaceComputeNodeOverview:
    """
    Attributes:
        name (str):
        status (DominoAdminInterfaceComputeNodeStatus):
        utilization (DominoAdminInterfaceComputeNodeUtilization):
    """

    name: str
    status: DominoAdminInterfaceComputeNodeStatus
    utilization: DominoAdminInterfaceComputeNodeUtilization
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.to_dict()

        utilization = self.utilization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "utilization": utilization,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_compute_node_status import DominoAdminInterfaceComputeNodeStatus
        from ..models.domino_admin_interface_compute_node_utilization import DominoAdminInterfaceComputeNodeUtilization

        d = dict(src_dict)
        name = d.pop("name")

        status = DominoAdminInterfaceComputeNodeStatus.from_dict(d.pop("status"))

        utilization = DominoAdminInterfaceComputeNodeUtilization.from_dict(d.pop("utilization"))

        domino_admin_interface_compute_node_overview = cls(
            name=name,
            status=status,
            utilization=utilization,
        )

        domino_admin_interface_compute_node_overview.additional_properties = d
        return domino_admin_interface_compute_node_overview

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
