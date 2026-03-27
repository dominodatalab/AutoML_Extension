from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_compute_cluster_pod_overview import (
        DominoAdminInterfaceComputeClusterPodOverview,
    )
    from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview
    from ..models.information import Information


T = TypeVar("T", bound="DominoAdminInterfaceComputeClusterOverview")


@_attrs_define
class DominoAdminInterfaceComputeClusterOverview:
    """
    Attributes:
        cluster_name (str):
        cluster_type (str):
        worker_hardware_tier (DominoAdminInterfaceHardwareTierOverview):
        web_ui_path (str):
        pod_overviews (list[DominoAdminInterfaceComputeClusterPodOverview]):
        master_hardware_tier (DominoAdminInterfaceHardwareTierOverview | Unset):
        worker_storage_size (Information | Unset):
    """

    cluster_name: str
    cluster_type: str
    worker_hardware_tier: DominoAdminInterfaceHardwareTierOverview
    web_ui_path: str
    pod_overviews: list[DominoAdminInterfaceComputeClusterPodOverview]
    master_hardware_tier: DominoAdminInterfaceHardwareTierOverview | Unset = UNSET
    worker_storage_size: Information | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_name = self.cluster_name

        cluster_type = self.cluster_type

        worker_hardware_tier = self.worker_hardware_tier.to_dict()

        web_ui_path = self.web_ui_path

        pod_overviews = []
        for pod_overviews_item_data in self.pod_overviews:
            pod_overviews_item = pod_overviews_item_data.to_dict()
            pod_overviews.append(pod_overviews_item)

        master_hardware_tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.master_hardware_tier, Unset):
            master_hardware_tier = self.master_hardware_tier.to_dict()

        worker_storage_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worker_storage_size, Unset):
            worker_storage_size = self.worker_storage_size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterName": cluster_name,
                "clusterType": cluster_type,
                "workerHardwareTier": worker_hardware_tier,
                "webUiPath": web_ui_path,
                "podOverviews": pod_overviews,
            }
        )
        if master_hardware_tier is not UNSET:
            field_dict["masterHardwareTier"] = master_hardware_tier
        if worker_storage_size is not UNSET:
            field_dict["workerStorageSize"] = worker_storage_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_compute_cluster_pod_overview import (
            DominoAdminInterfaceComputeClusterPodOverview,
        )
        from ..models.domino_admin_interface_hardware_tier_overview import DominoAdminInterfaceHardwareTierOverview
        from ..models.information import Information

        d = dict(src_dict)
        cluster_name = d.pop("clusterName")

        cluster_type = d.pop("clusterType")

        worker_hardware_tier = DominoAdminInterfaceHardwareTierOverview.from_dict(d.pop("workerHardwareTier"))

        web_ui_path = d.pop("webUiPath")

        pod_overviews = []
        _pod_overviews = d.pop("podOverviews")
        for pod_overviews_item_data in _pod_overviews:
            pod_overviews_item = DominoAdminInterfaceComputeClusterPodOverview.from_dict(pod_overviews_item_data)

            pod_overviews.append(pod_overviews_item)

        _master_hardware_tier = d.pop("masterHardwareTier", UNSET)
        master_hardware_tier: DominoAdminInterfaceHardwareTierOverview | Unset
        if isinstance(_master_hardware_tier, Unset):
            master_hardware_tier = UNSET
        else:
            master_hardware_tier = DominoAdminInterfaceHardwareTierOverview.from_dict(_master_hardware_tier)

        _worker_storage_size = d.pop("workerStorageSize", UNSET)
        worker_storage_size: Information | Unset
        if isinstance(_worker_storage_size, Unset):
            worker_storage_size = UNSET
        else:
            worker_storage_size = Information.from_dict(_worker_storage_size)

        domino_admin_interface_compute_cluster_overview = cls(
            cluster_name=cluster_name,
            cluster_type=cluster_type,
            worker_hardware_tier=worker_hardware_tier,
            web_ui_path=web_ui_path,
            pod_overviews=pod_overviews,
            master_hardware_tier=master_hardware_tier,
            worker_storage_size=worker_storage_size,
        )

        domino_admin_interface_compute_cluster_overview.additional_properties = d
        return domino_admin_interface_compute_cluster_overview

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
