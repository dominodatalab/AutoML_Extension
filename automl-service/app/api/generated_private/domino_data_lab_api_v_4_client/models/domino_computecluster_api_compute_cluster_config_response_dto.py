from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computecluster_api_compute_cluster_config_response_dto_extra_configs_type_0 import (
        DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0,
    )
    from ..models.domino_environments_api_environment_revision_summary import (
        DominoEnvironmentsApiEnvironmentRevisionSummary,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.information import Information


T = TypeVar("T", bound="DominoComputeclusterApiComputeClusterConfigResponseDto")


@_attrs_define
class DominoComputeclusterApiComputeClusterConfigResponseDto:
    """
    Attributes:
        cluster_type (ComputeClusterType): Type of compute cluster
        compute_environment (DominoEnvironmentsApiEnvironmentRevisionSummary):
        worker_count (int):
        worker_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        worker_hardware_tier_name (str):
        master_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier | Unset):
        master_hardware_tier_name (None | str | Unset):
        max_worker_count (int | None | Unset):
        worker_storage (Information | Unset):
        extra_configs (DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0 | None | Unset):
    """

    cluster_type: ComputeClusterType
    compute_environment: DominoEnvironmentsApiEnvironmentRevisionSummary
    worker_count: int
    worker_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    worker_hardware_tier_name: str
    master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset = UNSET
    master_hardware_tier_name: None | str | Unset = UNSET
    max_worker_count: int | None | Unset = UNSET
    worker_storage: Information | Unset = UNSET
    extra_configs: DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_computecluster_api_compute_cluster_config_response_dto_extra_configs_type_0 import (
            DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0,
        )

        cluster_type = self.cluster_type.value

        compute_environment = self.compute_environment.to_dict()

        worker_count = self.worker_count

        worker_hardware_tier_id = self.worker_hardware_tier_id.to_dict()

        worker_hardware_tier_name = self.worker_hardware_tier_name

        master_hardware_tier_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.master_hardware_tier_id, Unset):
            master_hardware_tier_id = self.master_hardware_tier_id.to_dict()

        master_hardware_tier_name: None | str | Unset
        if isinstance(self.master_hardware_tier_name, Unset):
            master_hardware_tier_name = UNSET
        else:
            master_hardware_tier_name = self.master_hardware_tier_name

        max_worker_count: int | None | Unset
        if isinstance(self.max_worker_count, Unset):
            max_worker_count = UNSET
        else:
            max_worker_count = self.max_worker_count

        worker_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worker_storage, Unset):
            worker_storage = self.worker_storage.to_dict()

        extra_configs: dict[str, Any] | None | Unset
        if isinstance(self.extra_configs, Unset):
            extra_configs = UNSET
        elif isinstance(self.extra_configs, DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0):
            extra_configs = self.extra_configs.to_dict()
        else:
            extra_configs = self.extra_configs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterType": cluster_type,
                "computeEnvironment": compute_environment,
                "workerCount": worker_count,
                "workerHardwareTierId": worker_hardware_tier_id,
                "workerHardwareTierName": worker_hardware_tier_name,
            }
        )
        if master_hardware_tier_id is not UNSET:
            field_dict["masterHardwareTierId"] = master_hardware_tier_id
        if master_hardware_tier_name is not UNSET:
            field_dict["masterHardwareTierName"] = master_hardware_tier_name
        if max_worker_count is not UNSET:
            field_dict["maxWorkerCount"] = max_worker_count
        if worker_storage is not UNSET:
            field_dict["workerStorage"] = worker_storage
        if extra_configs is not UNSET:
            field_dict["extraConfigs"] = extra_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computecluster_api_compute_cluster_config_response_dto_extra_configs_type_0 import (
            DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0,
        )
        from ..models.domino_environments_api_environment_revision_summary import (
            DominoEnvironmentsApiEnvironmentRevisionSummary,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.information import Information

        d = dict(src_dict)
        cluster_type = ComputeClusterType(d.pop("clusterType"))

        compute_environment = DominoEnvironmentsApiEnvironmentRevisionSummary.from_dict(d.pop("computeEnvironment"))

        worker_count = d.pop("workerCount")

        worker_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("workerHardwareTierId"))

        worker_hardware_tier_name = d.pop("workerHardwareTierName")

        _master_hardware_tier_id = d.pop("masterHardwareTierId", UNSET)
        master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset
        if isinstance(_master_hardware_tier_id, Unset):
            master_hardware_tier_id = UNSET
        else:
            master_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(_master_hardware_tier_id)

        def _parse_master_hardware_tier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        master_hardware_tier_name = _parse_master_hardware_tier_name(d.pop("masterHardwareTierName", UNSET))

        def _parse_max_worker_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_worker_count = _parse_max_worker_count(d.pop("maxWorkerCount", UNSET))

        _worker_storage = d.pop("workerStorage", UNSET)
        worker_storage: Information | Unset
        if isinstance(_worker_storage, Unset):
            worker_storage = UNSET
        else:
            worker_storage = Information.from_dict(_worker_storage)

        def _parse_extra_configs(
            data: object,
        ) -> DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_configs_type_0 = (
                    DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0.from_dict(data)
                )

                return extra_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoComputeclusterApiComputeClusterConfigResponseDtoExtraConfigsType0 | None | Unset, data)

        extra_configs = _parse_extra_configs(d.pop("extraConfigs", UNSET))

        domino_computecluster_api_compute_cluster_config_response_dto = cls(
            cluster_type=cluster_type,
            compute_environment=compute_environment,
            worker_count=worker_count,
            worker_hardware_tier_id=worker_hardware_tier_id,
            worker_hardware_tier_name=worker_hardware_tier_name,
            master_hardware_tier_id=master_hardware_tier_id,
            master_hardware_tier_name=master_hardware_tier_name,
            max_worker_count=max_worker_count,
            worker_storage=worker_storage,
            extra_configs=extra_configs,
        )

        domino_computecluster_api_compute_cluster_config_response_dto.additional_properties = d
        return domino_computecluster_api_compute_cluster_config_response_dto

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
