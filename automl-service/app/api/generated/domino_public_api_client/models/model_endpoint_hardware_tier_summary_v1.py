from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelEndpointHardwareTierSummaryV1")


@_attrs_define
class ModelEndpointHardwareTierSummaryV1:
    """
    Attributes:
        data_plane_id (str): Unique identifier for the data plane owning the hardware tier Example:
            62313ce67a0af0281c01a6a5.
        data_plane_name (str): Name of the data plane owning the hardware tier Example: My Data Plane.
        id (str): Unique identifier for the hardware tier Example: 62313ce67a0af0281c01a6a5.
    """

    data_plane_id: str
    data_plane_name: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_plane_id = self.data_plane_id

        data_plane_name = self.data_plane_name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataPlaneId": data_plane_id,
                "dataPlaneName": data_plane_name,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_plane_id = d.pop("dataPlaneId")

        data_plane_name = d.pop("dataPlaneName")

        id = d.pop("id")

        model_endpoint_hardware_tier_summary_v1 = cls(
            data_plane_id=data_plane_id,
            data_plane_name=data_plane_name,
            id=id,
        )

        model_endpoint_hardware_tier_summary_v1.additional_properties = d
        return model_endpoint_hardware_tier_summary_v1

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
