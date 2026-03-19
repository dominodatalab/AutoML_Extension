from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hardware_tier_compute_cluster_restrictions_v1 import HardwareTierComputeClusterRestrictionsV1
    from ..models.hardware_tier_gpu_configuration_v1 import HardwareTierGpuConfigurationV1
    from ..models.hardware_tier_over_provisioning_v1 import HardwareTierOverProvisioningV1
    from ..models.hardware_tier_pod_customization_v1 import HardwareTierPodCustomizationV1
    from ..models.hardware_tier_resources_v1 import HardwareTierResourcesV1
    from ..models.new_hardware_tier_flags_v1 import NewHardwareTierFlagsV1


T = TypeVar("T", bound="NewHardwareTierV1")


@_attrs_define
class NewHardwareTierV1:
    """
    Attributes:
        id (str):  Example: small-k8s.
        name (str):  Example: My-HardwareTier.
        node_pool (str):
        resources (HardwareTierResourcesV1): Compute resources for a hardware tier
        availability_zones (list[str] | Unset):
        cents_per_minute (float | Unset): Cost per minute of using this hardware tier as defined by an Admin.
        compute_cluster_restrictions (HardwareTierComputeClusterRestrictionsV1 | Unset): Details about specific compute
            clusters a hardware tier is restricted to
        data_plane_id (str | Unset):
        flags (NewHardwareTierFlagsV1 | Unset): Boolean flags for creating a new hardware tier
        gpu_configuration (HardwareTierGpuConfigurationV1 | Unset): Gpu configuration for a hardware tier
        max_simultaneous_executions (int | Unset):
        over_provisioning (HardwareTierOverProvisioningV1 | Unset): Over provisioning settings for a hardware tier
        pod_customization (HardwareTierPodCustomizationV1 | Unset): Custom fields for hardwareTier
        tags (list[str] | Unset):
    """

    id: str
    name: str
    node_pool: str
    resources: HardwareTierResourcesV1
    availability_zones: list[str] | Unset = UNSET
    cents_per_minute: float | Unset = UNSET
    compute_cluster_restrictions: HardwareTierComputeClusterRestrictionsV1 | Unset = UNSET
    data_plane_id: str | Unset = UNSET
    flags: NewHardwareTierFlagsV1 | Unset = UNSET
    gpu_configuration: HardwareTierGpuConfigurationV1 | Unset = UNSET
    max_simultaneous_executions: int | Unset = UNSET
    over_provisioning: HardwareTierOverProvisioningV1 | Unset = UNSET
    pod_customization: HardwareTierPodCustomizationV1 | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        node_pool = self.node_pool

        resources = self.resources.to_dict()

        availability_zones: list[str] | Unset = UNSET
        if not isinstance(self.availability_zones, Unset):
            availability_zones = self.availability_zones

        cents_per_minute = self.cents_per_minute

        compute_cluster_restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = self.compute_cluster_restrictions.to_dict()

        data_plane_id = self.data_plane_id

        flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags.to_dict()

        gpu_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu_configuration, Unset):
            gpu_configuration = self.gpu_configuration.to_dict()

        max_simultaneous_executions = self.max_simultaneous_executions

        over_provisioning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.over_provisioning, Unset):
            over_provisioning = self.over_provisioning.to_dict()

        pod_customization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pod_customization, Unset):
            pod_customization = self.pod_customization.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "nodePool": node_pool,
                "resources": resources,
            }
        )
        if availability_zones is not UNSET:
            field_dict["availabilityZones"] = availability_zones
        if cents_per_minute is not UNSET:
            field_dict["centsPerMinute"] = cents_per_minute
        if compute_cluster_restrictions is not UNSET:
            field_dict["computeClusterRestrictions"] = compute_cluster_restrictions
        if data_plane_id is not UNSET:
            field_dict["dataPlaneId"] = data_plane_id
        if flags is not UNSET:
            field_dict["flags"] = flags
        if gpu_configuration is not UNSET:
            field_dict["gpuConfiguration"] = gpu_configuration
        if max_simultaneous_executions is not UNSET:
            field_dict["maxSimultaneousExecutions"] = max_simultaneous_executions
        if over_provisioning is not UNSET:
            field_dict["overProvisioning"] = over_provisioning
        if pod_customization is not UNSET:
            field_dict["podCustomization"] = pod_customization
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hardware_tier_compute_cluster_restrictions_v1 import HardwareTierComputeClusterRestrictionsV1
        from ..models.hardware_tier_gpu_configuration_v1 import HardwareTierGpuConfigurationV1
        from ..models.hardware_tier_over_provisioning_v1 import HardwareTierOverProvisioningV1
        from ..models.hardware_tier_pod_customization_v1 import HardwareTierPodCustomizationV1
        from ..models.hardware_tier_resources_v1 import HardwareTierResourcesV1
        from ..models.new_hardware_tier_flags_v1 import NewHardwareTierFlagsV1

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        node_pool = d.pop("nodePool")

        resources = HardwareTierResourcesV1.from_dict(d.pop("resources"))

        availability_zones = cast(list[str], d.pop("availabilityZones", UNSET))

        cents_per_minute = d.pop("centsPerMinute", UNSET)

        _compute_cluster_restrictions = d.pop("computeClusterRestrictions", UNSET)
        compute_cluster_restrictions: HardwareTierComputeClusterRestrictionsV1 | Unset
        if isinstance(_compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = UNSET
        else:
            compute_cluster_restrictions = HardwareTierComputeClusterRestrictionsV1.from_dict(
                _compute_cluster_restrictions
            )

        data_plane_id = d.pop("dataPlaneId", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: NewHardwareTierFlagsV1 | Unset
        if isinstance(_flags, Unset):
            flags = UNSET
        else:
            flags = NewHardwareTierFlagsV1.from_dict(_flags)

        _gpu_configuration = d.pop("gpuConfiguration", UNSET)
        gpu_configuration: HardwareTierGpuConfigurationV1 | Unset
        if isinstance(_gpu_configuration, Unset):
            gpu_configuration = UNSET
        else:
            gpu_configuration = HardwareTierGpuConfigurationV1.from_dict(_gpu_configuration)

        max_simultaneous_executions = d.pop("maxSimultaneousExecutions", UNSET)

        _over_provisioning = d.pop("overProvisioning", UNSET)
        over_provisioning: HardwareTierOverProvisioningV1 | Unset
        if isinstance(_over_provisioning, Unset):
            over_provisioning = UNSET
        else:
            over_provisioning = HardwareTierOverProvisioningV1.from_dict(_over_provisioning)

        _pod_customization = d.pop("podCustomization", UNSET)
        pod_customization: HardwareTierPodCustomizationV1 | Unset
        if isinstance(_pod_customization, Unset):
            pod_customization = UNSET
        else:
            pod_customization = HardwareTierPodCustomizationV1.from_dict(_pod_customization)

        tags = cast(list[str], d.pop("tags", UNSET))

        new_hardware_tier_v1 = cls(
            id=id,
            name=name,
            node_pool=node_pool,
            resources=resources,
            availability_zones=availability_zones,
            cents_per_minute=cents_per_minute,
            compute_cluster_restrictions=compute_cluster_restrictions,
            data_plane_id=data_plane_id,
            flags=flags,
            gpu_configuration=gpu_configuration,
            max_simultaneous_executions=max_simultaneous_executions,
            over_provisioning=over_provisioning,
            pod_customization=pod_customization,
            tags=tags,
        )

        new_hardware_tier_v1.additional_properties = d
        return new_hardware_tier_v1

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
