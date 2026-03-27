from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataplane_data_plane import DominoDataplaneDataPlane


T = TypeVar("T", bound="DominoAdminInterfaceComputeNodeInfrastructureInfo")


@_attrs_define
class DominoAdminInterfaceComputeNodeInfrastructureInfo:
    """
    Attributes:
        name (str):
        is_build_node (bool):
        data_plane (DominoDataplaneDataPlane):
        node_pool (None | str | Unset):
        instance_type (None | str | Unset):
    """

    name: str
    is_build_node: bool
    data_plane: DominoDataplaneDataPlane
    node_pool: None | str | Unset = UNSET
    instance_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_build_node = self.is_build_node

        data_plane = self.data_plane.to_dict()

        node_pool: None | str | Unset
        if isinstance(self.node_pool, Unset):
            node_pool = UNSET
        else:
            node_pool = self.node_pool

        instance_type: None | str | Unset
        if isinstance(self.instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = self.instance_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "isBuildNode": is_build_node,
                "dataPlane": data_plane,
            }
        )
        if node_pool is not UNSET:
            field_dict["nodePool"] = node_pool
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataplane_data_plane import DominoDataplaneDataPlane

        d = dict(src_dict)
        name = d.pop("name")

        is_build_node = d.pop("isBuildNode")

        data_plane = DominoDataplaneDataPlane.from_dict(d.pop("dataPlane"))

        def _parse_node_pool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_pool = _parse_node_pool(d.pop("nodePool", UNSET))

        def _parse_instance_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_type = _parse_instance_type(d.pop("instanceType", UNSET))

        domino_admin_interface_compute_node_infrastructure_info = cls(
            name=name,
            is_build_node=is_build_node,
            data_plane=data_plane,
            node_pool=node_pool,
            instance_type=instance_type,
        )

        domino_admin_interface_compute_node_infrastructure_info.additional_properties = d
        return domino_admin_interface_compute_node_infrastructure_info

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
