from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hardware_tier_capacity_v1 import HardwareTierCapacityV1
    from ..models.hardware_tier_compute_cluster_restrictions_v1 import HardwareTierComputeClusterRestrictionsV1
    from ..models.hardware_tier_flags_v1 import HardwareTierFlagsV1
    from ..models.hardware_tier_gpu_configuration_v1 import HardwareTierGpuConfigurationV1
    from ..models.hardware_tier_over_provisioning_v1 import HardwareTierOverProvisioningV1
    from ..models.hardware_tier_pod_customization_v1 import HardwareTierPodCustomizationV1
    from ..models.hardware_tier_resources_v1 import HardwareTierResourcesV1
    from ..models.hardware_tier_v1_metadata import HardwareTierV1Metadata


T = TypeVar("T", bound="HardwareTierV1")


@_attrs_define
class HardwareTierV1:
    """
    Attributes:
        cents_per_minute (float): Cost per minute of using this hardware tier as defined by an Admin.
        creation_time (datetime.datetime): When the hardware tier was created Example: 2022-03-12T02:13:44.467Z.
        flags (HardwareTierFlagsV1): Boolean flags for a hardware tier
        id (str):  Example: small-k8s.
        metadata (HardwareTierV1Metadata):
        name (str):  Example: My-HardwareTier.
        pod_customization (HardwareTierPodCustomizationV1): Custom fields for hardwareTier
        resources (HardwareTierResourcesV1): Compute resources for a hardware tier
        update_time (datetime.datetime): When the hardwareTier was last updated Example: 2022-03-12T02:13:44.467Z.
        availability_zones (list[str] | Unset):
        capacity (HardwareTierCapacityV1 | Unset): Current capacity information for a hardware tier. Note: Not necessary
            on requests to update a hardware tier.
        compute_cluster_restrictions (HardwareTierComputeClusterRestrictionsV1 | Unset): Details about specific compute
            clusters a hardware tier is restricted to
        data_plane_id (str | Unset):
        gpu_configuration (HardwareTierGpuConfigurationV1 | Unset): Gpu configuration for a hardware tier
        max_simultaneous_executions (int | Unset):
        node_pool (str | Unset):
        over_provisioning (HardwareTierOverProvisioningV1 | Unset): Over provisioning settings for a hardware tier
        tags (list[str] | Unset):
    """

    cents_per_minute: float
    creation_time: datetime.datetime
    flags: HardwareTierFlagsV1
    id: str
    metadata: HardwareTierV1Metadata
    name: str
    pod_customization: HardwareTierPodCustomizationV1
    resources: HardwareTierResourcesV1
    update_time: datetime.datetime
    availability_zones: list[str] | Unset = UNSET
    capacity: HardwareTierCapacityV1 | Unset = UNSET
    compute_cluster_restrictions: HardwareTierComputeClusterRestrictionsV1 | Unset = UNSET
    data_plane_id: str | Unset = UNSET
    gpu_configuration: HardwareTierGpuConfigurationV1 | Unset = UNSET
    max_simultaneous_executions: int | Unset = UNSET
    node_pool: str | Unset = UNSET
    over_provisioning: HardwareTierOverProvisioningV1 | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cents_per_minute = self.cents_per_minute

        creation_time = self.creation_time.isoformat()

        flags = self.flags.to_dict()

        id = self.id

        metadata = self.metadata.to_dict()

        name = self.name

        pod_customization = self.pod_customization.to_dict()

        resources = self.resources.to_dict()

        update_time = self.update_time.isoformat()

        availability_zones: list[str] | Unset = UNSET
        if not isinstance(self.availability_zones, Unset):
            availability_zones = self.availability_zones

        capacity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()

        compute_cluster_restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = self.compute_cluster_restrictions.to_dict()

        data_plane_id = self.data_plane_id

        gpu_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu_configuration, Unset):
            gpu_configuration = self.gpu_configuration.to_dict()

        max_simultaneous_executions = self.max_simultaneous_executions

        node_pool = self.node_pool

        over_provisioning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.over_provisioning, Unset):
            over_provisioning = self.over_provisioning.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "centsPerMinute": cents_per_minute,
                "creationTime": creation_time,
                "flags": flags,
                "id": id,
                "metadata": metadata,
                "name": name,
                "podCustomization": pod_customization,
                "resources": resources,
                "updateTime": update_time,
            }
        )
        if availability_zones is not UNSET:
            field_dict["availabilityZones"] = availability_zones
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if compute_cluster_restrictions is not UNSET:
            field_dict["computeClusterRestrictions"] = compute_cluster_restrictions
        if data_plane_id is not UNSET:
            field_dict["dataPlaneId"] = data_plane_id
        if gpu_configuration is not UNSET:
            field_dict["gpuConfiguration"] = gpu_configuration
        if max_simultaneous_executions is not UNSET:
            field_dict["maxSimultaneousExecutions"] = max_simultaneous_executions
        if node_pool is not UNSET:
            field_dict["nodePool"] = node_pool
        if over_provisioning is not UNSET:
            field_dict["overProvisioning"] = over_provisioning
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hardware_tier_capacity_v1 import HardwareTierCapacityV1
        from ..models.hardware_tier_compute_cluster_restrictions_v1 import HardwareTierComputeClusterRestrictionsV1
        from ..models.hardware_tier_flags_v1 import HardwareTierFlagsV1
        from ..models.hardware_tier_gpu_configuration_v1 import HardwareTierGpuConfigurationV1
        from ..models.hardware_tier_over_provisioning_v1 import HardwareTierOverProvisioningV1
        from ..models.hardware_tier_pod_customization_v1 import HardwareTierPodCustomizationV1
        from ..models.hardware_tier_resources_v1 import HardwareTierResourcesV1
        from ..models.hardware_tier_v1_metadata import HardwareTierV1Metadata

        d = dict(src_dict)
        cents_per_minute = d.pop("centsPerMinute")

        creation_time = isoparse(d.pop("creationTime"))

        flags = HardwareTierFlagsV1.from_dict(d.pop("flags"))

        id = d.pop("id")

        metadata = HardwareTierV1Metadata.from_dict(d.pop("metadata"))

        name = d.pop("name")

        pod_customization = HardwareTierPodCustomizationV1.from_dict(d.pop("podCustomization"))

        resources = HardwareTierResourcesV1.from_dict(d.pop("resources"))

        update_time = isoparse(d.pop("updateTime"))

        availability_zones = cast(list[str], d.pop("availabilityZones", UNSET))

        _capacity = d.pop("capacity", UNSET)
        capacity: HardwareTierCapacityV1 | Unset
        if isinstance(_capacity, Unset):
            capacity = UNSET
        else:
            capacity = HardwareTierCapacityV1.from_dict(_capacity)

        _compute_cluster_restrictions = d.pop("computeClusterRestrictions", UNSET)
        compute_cluster_restrictions: HardwareTierComputeClusterRestrictionsV1 | Unset
        if isinstance(_compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = UNSET
        else:
            compute_cluster_restrictions = HardwareTierComputeClusterRestrictionsV1.from_dict(
                _compute_cluster_restrictions
            )

        data_plane_id = d.pop("dataPlaneId", UNSET)

        _gpu_configuration = d.pop("gpuConfiguration", UNSET)
        gpu_configuration: HardwareTierGpuConfigurationV1 | Unset
        if isinstance(_gpu_configuration, Unset):
            gpu_configuration = UNSET
        else:
            gpu_configuration = HardwareTierGpuConfigurationV1.from_dict(_gpu_configuration)

        max_simultaneous_executions = d.pop("maxSimultaneousExecutions", UNSET)

        node_pool = d.pop("nodePool", UNSET)

        _over_provisioning = d.pop("overProvisioning", UNSET)
        over_provisioning: HardwareTierOverProvisioningV1 | Unset
        if isinstance(_over_provisioning, Unset):
            over_provisioning = UNSET
        else:
            over_provisioning = HardwareTierOverProvisioningV1.from_dict(_over_provisioning)

        tags = cast(list[str], d.pop("tags", UNSET))

        hardware_tier_v1 = cls(
            cents_per_minute=cents_per_minute,
            creation_time=creation_time,
            flags=flags,
            id=id,
            metadata=metadata,
            name=name,
            pod_customization=pod_customization,
            resources=resources,
            update_time=update_time,
            availability_zones=availability_zones,
            capacity=capacity,
            compute_cluster_restrictions=compute_cluster_restrictions,
            data_plane_id=data_plane_id,
            gpu_configuration=gpu_configuration,
            max_simultaneous_executions=max_simultaneous_executions,
            node_pool=node_pool,
            over_provisioning=over_provisioning,
            tags=tags,
        )

        hardware_tier_v1.additional_properties = d
        return hardware_tier_v1

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
