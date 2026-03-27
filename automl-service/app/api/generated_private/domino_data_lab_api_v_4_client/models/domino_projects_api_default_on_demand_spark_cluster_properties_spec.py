from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_default_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_0 import (
    DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_default_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
        DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpec")


@_attrs_define
class DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpec:
    """
    Attributes:
        maximum_execution_slots_per_user (int):
        compute_environment_id (None | str | Unset):
        compute_environment_revision_spec
            (DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0 |
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1 | None | Unset):
        executor_count (int | None | Unset):
        executor_hardware_tier_id (None | str | Unset):
        executor_storage (Information | Unset):
        master_hardware_tier_id (None | str | Unset):
    """

    maximum_execution_slots_per_user: int
    compute_environment_id: None | str | Unset = UNSET
    compute_environment_revision_spec: (
        DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
        | DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    executor_count: int | None | Unset = UNSET
    executor_hardware_tier_id: None | str | Unset = UNSET
    executor_storage: Information | Unset = UNSET
    master_hardware_tier_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_projects_api_default_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        )

        maximum_execution_slots_per_user = self.maximum_execution_slots_per_user

        compute_environment_id: None | str | Unset
        if isinstance(self.compute_environment_id, Unset):
            compute_environment_id = UNSET
        else:
            compute_environment_id = self.compute_environment_id

        compute_environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.compute_environment_revision_spec, Unset):
            compute_environment_revision_spec = UNSET
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.value
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.to_dict()
        else:
            compute_environment_revision_spec = self.compute_environment_revision_spec

        executor_count: int | None | Unset
        if isinstance(self.executor_count, Unset):
            executor_count = UNSET
        else:
            executor_count = self.executor_count

        executor_hardware_tier_id: None | str | Unset
        if isinstance(self.executor_hardware_tier_id, Unset):
            executor_hardware_tier_id = UNSET
        else:
            executor_hardware_tier_id = self.executor_hardware_tier_id

        executor_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor_storage, Unset):
            executor_storage = self.executor_storage.to_dict()

        master_hardware_tier_id: None | str | Unset
        if isinstance(self.master_hardware_tier_id, Unset):
            master_hardware_tier_id = UNSET
        else:
            master_hardware_tier_id = self.master_hardware_tier_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maximumExecutionSlotsPerUser": maximum_execution_slots_per_user,
            }
        )
        if compute_environment_id is not UNSET:
            field_dict["computeEnvironmentId"] = compute_environment_id
        if compute_environment_revision_spec is not UNSET:
            field_dict["computeEnvironmentRevisionSpec"] = compute_environment_revision_spec
        if executor_count is not UNSET:
            field_dict["executorCount"] = executor_count
        if executor_hardware_tier_id is not UNSET:
            field_dict["executorHardwareTierId"] = executor_hardware_tier_id
        if executor_storage is not UNSET:
            field_dict["executorStorage"] = executor_storage
        if master_hardware_tier_id is not UNSET:
            field_dict["masterHardwareTierId"] = master_hardware_tier_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_default_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        )
        from ..models.information import Information

        d = dict(src_dict)
        maximum_execution_slots_per_user = d.pop("maximumExecutionSlotsPerUser")

        def _parse_compute_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compute_environment_id = _parse_compute_environment_id(d.pop("computeEnvironmentId", UNSET))

        def _parse_compute_environment_revision_spec(
            data: object,
        ) -> (
            DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
            | DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compute_environment_revision_spec_type_0 = (
                    DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0(data)
                )

                return compute_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compute_environment_revision_spec_type_1 = DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1.from_dict(
                    data
                )

                return compute_environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
                | DominoProjectsApiDefaultOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        compute_environment_revision_spec = _parse_compute_environment_revision_spec(
            d.pop("computeEnvironmentRevisionSpec", UNSET)
        )

        def _parse_executor_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        executor_count = _parse_executor_count(d.pop("executorCount", UNSET))

        def _parse_executor_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        executor_hardware_tier_id = _parse_executor_hardware_tier_id(d.pop("executorHardwareTierId", UNSET))

        _executor_storage = d.pop("executorStorage", UNSET)
        executor_storage: Information | Unset
        if isinstance(_executor_storage, Unset):
            executor_storage = UNSET
        else:
            executor_storage = Information.from_dict(_executor_storage)

        def _parse_master_hardware_tier_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        master_hardware_tier_id = _parse_master_hardware_tier_id(d.pop("masterHardwareTierId", UNSET))

        domino_projects_api_default_on_demand_spark_cluster_properties_spec = cls(
            maximum_execution_slots_per_user=maximum_execution_slots_per_user,
            compute_environment_id=compute_environment_id,
            compute_environment_revision_spec=compute_environment_revision_spec,
            executor_count=executor_count,
            executor_hardware_tier_id=executor_hardware_tier_id,
            executor_storage=executor_storage,
            master_hardware_tier_id=master_hardware_tier_id,
        )

        domino_projects_api_default_on_demand_spark_cluster_properties_spec.additional_properties = d
        return domino_projects_api_default_on_demand_spark_cluster_properties_spec

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
