from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_api_workspace_cluster_config_dto_compute_environment_revision_spec_type_0 import (
    DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_workspace_api_workspace_cluster_config_dto_compute_environment_revision_spec_type_1 import (
        DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1,
    )
    from ..models.information import Information


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceClusterConfigDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceClusterConfigDto:
    """
    Attributes:
        compute_environment_id (str):
        executor_count (int):
        executor_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        master_hardware_tier_id (DominoHardwaretierApiHardwareTierIdentifier):
        compute_environment_revision_spec
            (DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0 |
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1 | None | Unset):
        volume_size (Information | Unset):
    """

    compute_environment_id: str
    executor_count: int
    executor_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    master_hardware_tier_id: DominoHardwaretierApiHardwareTierIdentifier
    compute_environment_revision_spec: (
        DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0
        | DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1
        | None
        | Unset
    ) = UNSET
    volume_size: Information | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_workspace_api_workspace_cluster_config_dto_compute_environment_revision_spec_type_1 import (
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1,
        )

        compute_environment_id = self.compute_environment_id

        executor_count = self.executor_count

        executor_hardware_tier_id = self.executor_hardware_tier_id.to_dict()

        master_hardware_tier_id = self.master_hardware_tier_id.to_dict()

        compute_environment_revision_spec: dict[str, Any] | None | str | Unset
        if isinstance(self.compute_environment_revision_spec, Unset):
            compute_environment_revision_spec = UNSET
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.value
        elif isinstance(
            self.compute_environment_revision_spec,
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1,
        ):
            compute_environment_revision_spec = self.compute_environment_revision_spec.to_dict()
        else:
            compute_environment_revision_spec = self.compute_environment_revision_spec

        volume_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.volume_size, Unset):
            volume_size = self.volume_size.to_dict()

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
        if volume_size is not UNSET:
            field_dict["volumeSize"] = volume_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_workspace_api_workspace_cluster_config_dto_compute_environment_revision_spec_type_1 import (
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1,
        )
        from ..models.information import Information

        d = dict(src_dict)
        compute_environment_id = d.pop("computeEnvironmentId")

        executor_count = d.pop("executorCount")

        executor_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(
            d.pop("executorHardwareTierId")
        )

        master_hardware_tier_id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("masterHardwareTierId"))

        def _parse_compute_environment_revision_spec(
            data: object,
        ) -> (
            DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0
            | DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1
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
                    DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0(data)
                )

                return compute_environment_revision_spec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                compute_environment_revision_spec_type_1 = (
                    DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1.from_dict(data)
                )

                return compute_environment_revision_spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType0
                | DominoWorkspaceApiWorkspaceClusterConfigDtoComputeEnvironmentRevisionSpecType1
                | None
                | Unset,
                data,
            )

        compute_environment_revision_spec = _parse_compute_environment_revision_spec(
            d.pop("computeEnvironmentRevisionSpec", UNSET)
        )

        _volume_size = d.pop("volumeSize", UNSET)
        volume_size: Information | Unset
        if isinstance(_volume_size, Unset):
            volume_size = UNSET
        else:
            volume_size = Information.from_dict(_volume_size)

        domino_workspace_api_workspace_cluster_config_dto = cls(
            compute_environment_id=compute_environment_id,
            executor_count=executor_count,
            executor_hardware_tier_id=executor_hardware_tier_id,
            master_hardware_tier_id=master_hardware_tier_id,
            compute_environment_revision_spec=compute_environment_revision_spec,
            volume_size=volume_size,
        )

        domino_workspace_api_workspace_cluster_config_dto.additional_properties = d
        return domino_workspace_api_workspace_cluster_config_dto

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
