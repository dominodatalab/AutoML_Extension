from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_cluster_type import ComputeClusterType
from ..models.domino_computecluster_api_default_compute_cluster_settings_compute_environment_revision_spec_type_0 import (
    DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computecluster_api_default_compute_cluster_settings_compute_environment_revision_spec_type_1 import (
        DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1,
    )
    from ..models.domino_computecluster_api_default_compute_cluster_settings_extra_configs_type_0 import (
        DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0,
    )
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.information import Information


T = TypeVar("T", bound="DominoComputeclusterApiDefaultComputeClusterSettings")


@_attrs_define
class DominoComputeclusterApiDefaultComputeClusterSettings:
    """
    Attributes:
        cluster_type (ComputeClusterType): Type of compute cluster
        worker_count (int):
        max_user_execution_slots (int):
        compute_environment_id (None | str | Unset):
        compute_environment_revision_spec
            (DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0 |
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1 | None | Unset):
        master_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier | Unset):
        max_worker_count (int | None | Unset):
        worker_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier | Unset):
        worker_storage (Information | Unset):
        extra_configs (DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0 | None | Unset):
    """

    cluster_type: ComputeClusterType
    worker_count: int
    max_user_execution_slots: int
    compute_environment_id: None | str | Unset = UNSET
    compute_environment_revision_spec: (
        DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0
        | DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset = UNSET
    max_worker_count: int | None | Unset = UNSET
    worker_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset = UNSET
    worker_storage: Information | Unset = UNSET
    extra_configs: DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_computecluster_api_default_compute_cluster_settings_compute_environment_revision_spec_type_1 import (
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1,
        )
        from ..models.domino_computecluster_api_default_compute_cluster_settings_extra_configs_type_0 import (
            DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0,
        )

        cluster_type = self.cluster_type.value

        worker_count = self.worker_count

        max_user_execution_slots = self.max_user_execution_slots

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
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.value
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.to_dict()
        else:
            compute_environment_revision_spec = self.compute_environment_revision_spec

        master_hardware_tier_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.master_hardware_tier_id, Unset):
            master_hardware_tier_id = self.master_hardware_tier_id.to_dict()

        max_worker_count: int | None | Unset
        if isinstance(self.max_worker_count, Unset):
            max_worker_count = UNSET
        else:
            max_worker_count = self.max_worker_count

        worker_hardware_tier_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worker_hardware_tier_id, Unset):
            worker_hardware_tier_id = self.worker_hardware_tier_id.to_dict()

        worker_storage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worker_storage, Unset):
            worker_storage = self.worker_storage.to_dict()

        extra_configs: dict[str, Any] | None | Unset
        if isinstance(self.extra_configs, Unset):
            extra_configs = UNSET
        elif isinstance(self.extra_configs, DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0):
            extra_configs = self.extra_configs.to_dict()
        else:
            extra_configs = self.extra_configs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clusterType": cluster_type,
                "workerCount": worker_count,
                "maxUserExecutionSlots": max_user_execution_slots,
            }
        )
        if compute_environment_id is not UNSET:
            field_dict["computeEnvironmentId"] = compute_environment_id
        if compute_environment_revision_spec is not UNSET:
            field_dict["computeEnvironmentRevisionSpec"] = compute_environment_revision_spec
        if master_hardware_tier_id is not UNSET:
            field_dict["masterHardwareTierId"] = master_hardware_tier_id
        if max_worker_count is not UNSET:
            field_dict["maxWorkerCount"] = max_worker_count
        if worker_hardware_tier_id is not UNSET:
            field_dict["workerHardwareTierId"] = worker_hardware_tier_id
        if worker_storage is not UNSET:
            field_dict["workerStorage"] = worker_storage
        if extra_configs is not UNSET:
            field_dict["extraConfigs"] = extra_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computecluster_api_default_compute_cluster_settings_compute_environment_revision_spec_type_1 import (
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1,
        )
        from ..models.domino_computecluster_api_default_compute_cluster_settings_extra_configs_type_0 import (
            DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0,
        )
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.information import Information

        d = dict(src_dict)
        cluster_type = ComputeClusterType(d.pop("clusterType"))

        worker_count = d.pop("workerCount")

        max_user_execution_slots = d.pop("maxUserExecutionSlots")

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
            DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0
            | DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1
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
                    DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0(data)
                )

                return compute_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compute_environment_revision_spec_type_1 = (
                    DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1.from_dict(
                        data
                    )
                )

                return compute_environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType0
                | DominoComputeclusterApiDefaultComputeClusterSettingsComputeEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        compute_environment_revision_spec = _parse_compute_environment_revision_spec(
            d.pop("computeEnvironmentRevisionSpec", UNSET)
        )

        _master_hardware_tier_id = d.pop("masterHardwareTierId", UNSET)
        master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset
        if isinstance(_master_hardware_tier_id, Unset):
            master_hardware_tier_id = UNSET
        else:
            master_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(_master_hardware_tier_id)

        def _parse_max_worker_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_worker_count = _parse_max_worker_count(d.pop("maxWorkerCount", UNSET))

        _worker_hardware_tier_id = d.pop("workerHardwareTierId", UNSET)
        worker_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier | Unset
        if isinstance(_worker_hardware_tier_id, Unset):
            worker_hardware_tier_id = UNSET
        else:
            worker_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(_worker_hardware_tier_id)

        _worker_storage = d.pop("workerStorage", UNSET)
        worker_storage: Information | Unset
        if isinstance(_worker_storage, Unset):
            worker_storage = UNSET
        else:
            worker_storage = Information.from_dict(_worker_storage)

        def _parse_extra_configs(
            data: object,
        ) -> DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_configs_type_0 = DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0.from_dict(
                    data
                )

                return extra_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoComputeclusterApiDefaultComputeClusterSettingsExtraConfigsType0 | None | Unset, data)

        extra_configs = _parse_extra_configs(d.pop("extraConfigs", UNSET))

        domino_computecluster_api_default_compute_cluster_settings = cls(
            cluster_type=cluster_type,
            worker_count=worker_count,
            max_user_execution_slots=max_user_execution_slots,
            compute_environment_id=compute_environment_id,
            compute_environment_revision_spec=compute_environment_revision_spec,
            master_hardware_tier_id=master_hardware_tier_id,
            max_worker_count=max_worker_count,
            worker_hardware_tier_id=worker_hardware_tier_id,
            worker_storage=worker_storage,
            extra_configs=extra_configs,
        )

        domino_computecluster_api_default_compute_cluster_settings.additional_properties = d
        return domino_computecluster_api_default_compute_cluster_settings

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
