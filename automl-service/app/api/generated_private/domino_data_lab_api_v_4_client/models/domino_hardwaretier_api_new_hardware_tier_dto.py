from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_hardwaretier_api_new_hardware_tier_dto_cluster_type import (
    DominoHardwaretierApiNewHardwareTierDtoClusterType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_capacity_type_restrictions_dto import (
        DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_compute_cluster_restrictions_dto import (
        DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_gpu_configuration_dto import (
        DominoHardwaretierApiHardwareTierGpuConfigurationDto,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_overprovisioning_dto import (
        DominoHardwaretierApiHardwareTierOverprovisioningDto,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto import (
        DominoHardwaretierApiHardwareTierPodCustomizationDto,
    )
    from ..models.domino_hardwaretier_api_hwt_resources import DominoHardwaretierApiHwtResources
    from ..models.domino_hardwaretier_api_new_hwt_flags import DominoHardwaretierApiNewHwtFlags


T = TypeVar("T", bound="DominoHardwaretierApiNewHardwareTierDto")


@_attrs_define
class DominoHardwaretierApiNewHardwareTierDto:
    """
    Attributes:
        id (str):
        name (str):
        hwt_resources (DominoHardwaretierApiHwtResources):
        node_pool (str):
        hwt_flags (DominoHardwaretierApiNewHwtFlags | Unset):
        cluster_type (DominoHardwaretierApiNewHardwareTierDtoClusterType | Unset):
        gpu_configuration (DominoHardwaretierApiHardwareTierGpuConfigurationDto | Unset):
        cents_per_minute (float | None | Unset):
        capacity_type_restrictions (DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto | Unset):
        compute_cluster_restrictions (DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto | Unset):
        max_simultaneous_executions (int | None | Unset):
        overprovisioning (DominoHardwaretierApiHardwareTierOverprovisioningDto | Unset):
        pod_customization (DominoHardwaretierApiHardwareTierPodCustomizationDto | Unset):
        data_plane_id (None | str | Unset):
        tags (list[str] | None | Unset):
        availability_zones (list[str] | None | Unset):
    """

    id: str
    name: str
    hwt_resources: DominoHardwaretierApiHwtResources
    node_pool: str
    hwt_flags: DominoHardwaretierApiNewHwtFlags | Unset = UNSET
    cluster_type: DominoHardwaretierApiNewHardwareTierDtoClusterType | Unset = UNSET
    gpu_configuration: DominoHardwaretierApiHardwareTierGpuConfigurationDto | Unset = UNSET
    cents_per_minute: float | None | Unset = UNSET
    capacity_type_restrictions: DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto | Unset = UNSET
    compute_cluster_restrictions: DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto | Unset = UNSET
    max_simultaneous_executions: int | None | Unset = UNSET
    overprovisioning: DominoHardwaretierApiHardwareTierOverprovisioningDto | Unset = UNSET
    pod_customization: DominoHardwaretierApiHardwareTierPodCustomizationDto | Unset = UNSET
    data_plane_id: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    availability_zones: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        hwt_resources = self.hwt_resources.to_dict()

        node_pool = self.node_pool

        hwt_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hwt_flags, Unset):
            hwt_flags = self.hwt_flags.to_dict()

        cluster_type: str | Unset = UNSET
        if not isinstance(self.cluster_type, Unset):
            cluster_type = self.cluster_type.value

        gpu_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu_configuration, Unset):
            gpu_configuration = self.gpu_configuration.to_dict()

        cents_per_minute: float | None | Unset
        if isinstance(self.cents_per_minute, Unset):
            cents_per_minute = UNSET
        else:
            cents_per_minute = self.cents_per_minute

        capacity_type_restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capacity_type_restrictions, Unset):
            capacity_type_restrictions = self.capacity_type_restrictions.to_dict()

        compute_cluster_restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = self.compute_cluster_restrictions.to_dict()

        max_simultaneous_executions: int | None | Unset
        if isinstance(self.max_simultaneous_executions, Unset):
            max_simultaneous_executions = UNSET
        else:
            max_simultaneous_executions = self.max_simultaneous_executions

        overprovisioning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overprovisioning, Unset):
            overprovisioning = self.overprovisioning.to_dict()

        pod_customization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pod_customization, Unset):
            pod_customization = self.pod_customization.to_dict()

        data_plane_id: None | str | Unset
        if isinstance(self.data_plane_id, Unset):
            data_plane_id = UNSET
        else:
            data_plane_id = self.data_plane_id

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        availability_zones: list[str] | None | Unset
        if isinstance(self.availability_zones, Unset):
            availability_zones = UNSET
        elif isinstance(self.availability_zones, list):
            availability_zones = self.availability_zones

        else:
            availability_zones = self.availability_zones

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "hwtResources": hwt_resources,
                "nodePool": node_pool,
            }
        )
        if hwt_flags is not UNSET:
            field_dict["hwtFlags"] = hwt_flags
        if cluster_type is not UNSET:
            field_dict["clusterType"] = cluster_type
        if gpu_configuration is not UNSET:
            field_dict["gpuConfiguration"] = gpu_configuration
        if cents_per_minute is not UNSET:
            field_dict["centsPerMinute"] = cents_per_minute
        if capacity_type_restrictions is not UNSET:
            field_dict["capacityTypeRestrictions"] = capacity_type_restrictions
        if compute_cluster_restrictions is not UNSET:
            field_dict["computeClusterRestrictions"] = compute_cluster_restrictions
        if max_simultaneous_executions is not UNSET:
            field_dict["maxSimultaneousExecutions"] = max_simultaneous_executions
        if overprovisioning is not UNSET:
            field_dict["overprovisioning"] = overprovisioning
        if pod_customization is not UNSET:
            field_dict["podCustomization"] = pod_customization
        if data_plane_id is not UNSET:
            field_dict["dataPlaneId"] = data_plane_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if availability_zones is not UNSET:
            field_dict["availabilityZones"] = availability_zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_capacity_type_restrictions_dto import (
            DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_compute_cluster_restrictions_dto import (
            DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_gpu_configuration_dto import (
            DominoHardwaretierApiHardwareTierGpuConfigurationDto,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_overprovisioning_dto import (
            DominoHardwaretierApiHardwareTierOverprovisioningDto,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_pod_customization_dto import (
            DominoHardwaretierApiHardwareTierPodCustomizationDto,
        )
        from ..models.domino_hardwaretier_api_hwt_resources import DominoHardwaretierApiHwtResources
        from ..models.domino_hardwaretier_api_new_hwt_flags import DominoHardwaretierApiNewHwtFlags

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        hwt_resources = DominoHardwaretierApiHwtResources.from_dict(d.pop("hwtResources"))

        node_pool = d.pop("nodePool")

        _hwt_flags = d.pop("hwtFlags", UNSET)
        hwt_flags: DominoHardwaretierApiNewHwtFlags | Unset
        if isinstance(_hwt_flags, Unset):
            hwt_flags = UNSET
        else:
            hwt_flags = DominoHardwaretierApiNewHwtFlags.from_dict(_hwt_flags)

        _cluster_type = d.pop("clusterType", UNSET)
        cluster_type: DominoHardwaretierApiNewHardwareTierDtoClusterType | Unset
        if isinstance(_cluster_type, Unset):
            cluster_type = UNSET
        else:
            cluster_type = DominoHardwaretierApiNewHardwareTierDtoClusterType(_cluster_type)

        _gpu_configuration = d.pop("gpuConfiguration", UNSET)
        gpu_configuration: DominoHardwaretierApiHardwareTierGpuConfigurationDto | Unset
        if isinstance(_gpu_configuration, Unset):
            gpu_configuration = UNSET
        else:
            gpu_configuration = DominoHardwaretierApiHardwareTierGpuConfigurationDto.from_dict(_gpu_configuration)

        def _parse_cents_per_minute(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cents_per_minute = _parse_cents_per_minute(d.pop("centsPerMinute", UNSET))

        _capacity_type_restrictions = d.pop("capacityTypeRestrictions", UNSET)
        capacity_type_restrictions: DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto | Unset
        if isinstance(_capacity_type_restrictions, Unset):
            capacity_type_restrictions = UNSET
        else:
            capacity_type_restrictions = DominoHardwaretierApiHardwareTierCapacityTypeRestrictionsDto.from_dict(
                _capacity_type_restrictions
            )

        _compute_cluster_restrictions = d.pop("computeClusterRestrictions", UNSET)
        compute_cluster_restrictions: DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto | Unset
        if isinstance(_compute_cluster_restrictions, Unset):
            compute_cluster_restrictions = UNSET
        else:
            compute_cluster_restrictions = DominoHardwaretierApiHardwareTierComputeClusterRestrictionsDto.from_dict(
                _compute_cluster_restrictions
            )

        def _parse_max_simultaneous_executions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_simultaneous_executions = _parse_max_simultaneous_executions(d.pop("maxSimultaneousExecutions", UNSET))

        _overprovisioning = d.pop("overprovisioning", UNSET)
        overprovisioning: DominoHardwaretierApiHardwareTierOverprovisioningDto | Unset
        if isinstance(_overprovisioning, Unset):
            overprovisioning = UNSET
        else:
            overprovisioning = DominoHardwaretierApiHardwareTierOverprovisioningDto.from_dict(_overprovisioning)

        _pod_customization = d.pop("podCustomization", UNSET)
        pod_customization: DominoHardwaretierApiHardwareTierPodCustomizationDto | Unset
        if isinstance(_pod_customization, Unset):
            pod_customization = UNSET
        else:
            pod_customization = DominoHardwaretierApiHardwareTierPodCustomizationDto.from_dict(_pod_customization)

        def _parse_data_plane_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_plane_id = _parse_data_plane_id(d.pop("dataPlaneId", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_availability_zones(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                availability_zones_type_0 = cast(list[str], data)

                return availability_zones_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        availability_zones = _parse_availability_zones(d.pop("availabilityZones", UNSET))

        domino_hardwaretier_api_new_hardware_tier_dto = cls(
            id=id,
            name=name,
            hwt_resources=hwt_resources,
            node_pool=node_pool,
            hwt_flags=hwt_flags,
            cluster_type=cluster_type,
            gpu_configuration=gpu_configuration,
            cents_per_minute=cents_per_minute,
            capacity_type_restrictions=capacity_type_restrictions,
            compute_cluster_restrictions=compute_cluster_restrictions,
            max_simultaneous_executions=max_simultaneous_executions,
            overprovisioning=overprovisioning,
            pod_customization=pod_customization,
            data_plane_id=data_plane_id,
            tags=tags,
            availability_zones=availability_zones,
        )

        domino_hardwaretier_api_new_hardware_tier_dto.additional_properties = d
        return domino_hardwaretier_api_new_hardware_tier_dto

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
