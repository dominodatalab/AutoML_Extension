from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview


T = TypeVar("T", bound="DominoAdminInterfaceOnDemandSparkClusterOverview")


@_attrs_define
class DominoAdminInterfaceOnDemandSparkClusterOverview:
    """
    Attributes:
        name (str):
        master_hardware_tier (DominoAdminInterfaceHardwareTierOverview):
        worker_hardware_tier (DominoAdminInterfaceHardwareTierOverview):
        web_ui_path (str):
        worker_storage_mb (float | None | Unset):
    """

    name: str
    master_hardware_tier: DominoAdminInterfaceHardwareTierOverview
    worker_hardware_tier: DominoAdminInterfaceHardwareTierOverview
    web_ui_path: str
    worker_storage_mb: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        master_hardware_tier = self.master_hardware_tier.to_dict()

        worker_hardware_tier = self.worker_hardware_tier.to_dict()

        web_ui_path = self.web_ui_path

        worker_storage_mb: float | None | Unset
        if isinstance(self.worker_storage_mb, Unset):
            worker_storage_mb = UNSET
        else:
            worker_storage_mb = self.worker_storage_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "masterHardwareTier": master_hardware_tier,
                "workerHardwareTier": worker_hardware_tier,
                "webUiPath": web_ui_path,
            }
        )
        if worker_storage_mb is not UNSET:
            field_dict["workerStorageMB"] = worker_storage_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview

        d = dict(src_dict)
        name = d.pop("name")

        master_hardware_tier = DominoAdminInterfaceHardwareTierOverview.from_dict(d.pop("masterHardwareTier"))

        worker_hardware_tier = DominoAdminInterfaceHardwareTierOverview.from_dict(d.pop("workerHardwareTier"))

        web_ui_path = d.pop("webUiPath")

        def _parse_worker_storage_mb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        worker_storage_mb = _parse_worker_storage_mb(d.pop("workerStorageMB", UNSET))

        domino_admin_interface_on_demand_spark_cluster_overview = cls(
            name=name,
            master_hardware_tier=master_hardware_tier,
            worker_hardware_tier=worker_hardware_tier,
            web_ui_path=web_ui_path,
            worker_storage_mb=worker_storage_mb,
        )

        domino_admin_interface_on_demand_spark_cluster_overview.additional_properties = d
        return domino_admin_interface_on_demand_spark_cluster_overview

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
