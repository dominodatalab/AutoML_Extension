from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_0 import (
    DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
        DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoProjectsApiOnDemandSparkClusterPropertiesSpec")


@_attrs_define
class DominoProjectsApiOnDemandSparkClusterPropertiesSpec:
    """
    Attributes:
        compute_environment_id (str):
        executor_count (int):
        executor_hardware_tier_id (str):
        master_hardware_tier_id (str):
        compute_environment_revision_spec
            (DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0 |
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1 | None | Unset):
        executor_storage (Information | Unset):
    """

    compute_environment_id: str
    executor_count: int
    executor_hardware_tier_id: str
    master_hardware_tier_id: str
    compute_environment_revision_spec: (
        DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
        | DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    executor_storage: Information | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        )

        compute_environment_id = self.compute_environment_id

        executor_count = self.executor_count

        executor_hardware_tier_id = self.executor_hardware_tier_id

        master_hardware_tier_id = self.master_hardware_tier_id

        compute_environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.compute_environment_revision_spec, Unset):
            compute_environment_revision_spec = UNSET
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.value
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.to_dict()
        else:
            compute_environment_revision_spec = self.compute_environment_revision_spec

        executor_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor_storage, Unset):
            executor_storage = self.executor_storage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "computeEnvironmentId": compute_environment_id,
                "executorCount": executor_count,
                "executorHardwareTierId": executor_hardware_tier_id,
                "masterHardwareTierId": master_hardware_tier_id,
            }
        )
        if compute_environment_revision_spec is not UNSET:
            field_dict["computeEnvironmentRevisionSpec"] = compute_environment_revision_spec
        if executor_storage is not UNSET:
            field_dict["executorStorage"] = executor_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_on_demand_spark_cluster_properties_spec_compute_environment_revision_spec_type_1 import (
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1,
        )
        from ..models.information import Information

        d = dict(src_dict)
        compute_environment_id = d.pop("computeEnvironmentId")

        executor_count = d.pop("executorCount")

        executor_hardware_tier_id = d.pop("executorHardwareTierId")

        master_hardware_tier_id = d.pop("masterHardwareTierId")

        def _parse_compute_environment_revision_spec(
            data: object,
        ) -> (
            DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
            | DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
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
                    DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0(data)
                )

                return compute_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compute_environment_revision_spec_type_1 = (
                    DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1.from_dict(
                        data
                    )
                )

                return compute_environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType0
                | DominoProjectsApiOnDemandSparkClusterPropertiesSpecComputeEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        compute_environment_revision_spec = _parse_compute_environment_revision_spec(
            d.pop("computeEnvironmentRevisionSpec", UNSET)
        )

        _executor_storage = d.pop("executorStorage", UNSET)
        executor_storage: Information | Unset
        if isinstance(_executor_storage, Unset):
            executor_storage = UNSET
        else:
            executor_storage = Information.from_dict(_executor_storage)

        domino_projects_api_on_demand_spark_cluster_properties_spec = cls(
            compute_environment_id=compute_environment_id,
            executor_count=executor_count,
            executor_hardware_tier_id=executor_hardware_tier_id,
            master_hardware_tier_id=master_hardware_tier_id,
            compute_environment_revision_spec=compute_environment_revision_spec,
            executor_storage=executor_storage,
        )

        domino_projects_api_on_demand_spark_cluster_properties_spec.additional_properties = d
        return domino_projects_api_on_demand_spark_cluster_properties_spec

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
