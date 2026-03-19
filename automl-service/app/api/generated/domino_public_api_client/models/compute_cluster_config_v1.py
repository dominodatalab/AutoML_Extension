from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cluster_type_v1 import ClusterTypeV1
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeClusterConfigV1")


@_attrs_define
class ComputeClusterConfigV1:
    """
    Attributes:
        cluster_type (ClusterTypeV1): Type of compute cluster
        compute_environment_id (str): Id of compute environment to use. Example: 623139857a0af0281c01a6a4.
        worker_count (int): Number of workers to use in compute cluster. Used as min number of workers in maxWorkerCount
            is set. Example: 4.
        worker_hardware_tier (str): Hardware tier to use for workers in compute cluster. Example: large-k8s.
        compute_environment_revision_spec (str | Unset): Specification describing which environment revision to use.
            Defaults to "ActiveRevision" Example: ActiveRevision | LatestRevision | SomeRevision(623131577a0af0281c01a69a).
        master_hardware_tier_id (str | Unset): Hardware tier to use for master node in compute cluster. Example:
            medium-k8s.
        max_worker_count (int | Unset): Max number of workers to use in compute cluster. Enables auto-scaling for
            cluster when present. Example: 10.
        worker_storage_mb (float | Unset): Disk size in MB for each worker. Example: 5.
    """

    cluster_type: ClusterTypeV1
    compute_environment_id: str
    worker_count: int
    worker_hardware_tier: str
    compute_environment_revision_spec: str | Unset = UNSET
    master_hardware_tier_id: str | Unset = UNSET
    max_worker_count: int | Unset = UNSET
    worker_storage_mb: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster_type = self.cluster_type.value

        compute_environment_id = self.compute_environment_id

        worker_count = self.worker_count

        worker_hardware_tier = self.worker_hardware_tier

        compute_environment_revision_spec = self.compute_environment_revision_spec

        master_hardware_tier_id = self.master_hardware_tier_id

        max_worker_count = self.max_worker_count

        worker_storage_mb = self.worker_storage_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterType": cluster_type,
                "computeEnvironmentId": compute_environment_id,
                "workerCount": worker_count,
                "workerHardwareTier": worker_hardware_tier,
            }
        )
        if compute_environment_revision_spec is not UNSET:
            field_dict["computeEnvironmentRevisionSpec"] = compute_environment_revision_spec
        if master_hardware_tier_id is not UNSET:
            field_dict["masterHardwareTierId"] = master_hardware_tier_id
        if max_worker_count is not UNSET:
            field_dict["maxWorkerCount"] = max_worker_count
        if worker_storage_mb is not UNSET:
            field_dict["workerStorageMB"] = worker_storage_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cluster_type = ClusterTypeV1(d.pop("clusterType"))

        compute_environment_id = d.pop("computeEnvironmentId")

        worker_count = d.pop("workerCount")

        worker_hardware_tier = d.pop("workerHardwareTier")

        compute_environment_revision_spec = d.pop("computeEnvironmentRevisionSpec", UNSET)

        master_hardware_tier_id = d.pop("masterHardwareTierId", UNSET)

        max_worker_count = d.pop("maxWorkerCount", UNSET)

        worker_storage_mb = d.pop("workerStorageMB", UNSET)

        compute_cluster_config_v1 = cls(
            cluster_type=cluster_type,
            compute_environment_id=compute_environment_id,
            worker_count=worker_count,
            worker_hardware_tier=worker_hardware_tier,
            compute_environment_revision_spec=compute_environment_revision_spec,
            master_hardware_tier_id=master_hardware_tier_id,
            max_worker_count=max_worker_count,
            worker_storage_mb=worker_storage_mb,
        )

        compute_cluster_config_v1.additional_properties = d
        return compute_cluster_config_v1

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
