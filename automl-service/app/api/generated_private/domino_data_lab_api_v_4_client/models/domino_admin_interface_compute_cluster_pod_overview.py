from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_admin_interface_compute_cluster_pod_overview_deployable_object_type import (
    DominoAdminInterfaceComputeClusterPodOverviewDeployableObjectType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceComputeClusterPodOverview")


@_attrs_define
class DominoAdminInterfaceComputeClusterPodOverview:
    """
    Attributes:
        deployable_object_type (DominoAdminInterfaceComputeClusterPodOverviewDeployableObjectType):
        deployable_object_id (str):
        status (str):
        role (str):
        is_master (bool):
        compute_node_id (None | str | Unset):
    """

    deployable_object_type: DominoAdminInterfaceComputeClusterPodOverviewDeployableObjectType
    deployable_object_id: str
    status: str
    role: str
    is_master: bool
    compute_node_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deployable_object_type = self.deployable_object_type.value

        deployable_object_id = self.deployable_object_id

        status = self.status

        role = self.role

        is_master = self.is_master

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
                "role": role,
                "isMaster": is_master,
            }
        )
        if compute_node_id is not UNSET:
            field_dict["computeNodeId"] = compute_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deployable_object_type = DominoAdminInterfaceComputeClusterPodOverviewDeployableObjectType(
            d.pop("deployableObjectType")
        )

        deployable_object_id = d.pop("deployableObjectId")

        status = d.pop("status")

        role = d.pop("role")

        is_master = d.pop("isMaster")

        def _parse_compute_node_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compute_node_id = _parse_compute_node_id(d.pop("computeNodeId", UNSET))

        domino_admin_interface_compute_cluster_pod_overview = cls(
            deployable_object_type=deployable_object_type,
            deployable_object_id=deployable_object_id,
            status=status,
            role=role,
            is_master=is_master,
            compute_node_id=compute_node_id,
        )

        domino_admin_interface_compute_cluster_pod_overview.additional_properties = d
        return domino_admin_interface_compute_cluster_pod_overview

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
