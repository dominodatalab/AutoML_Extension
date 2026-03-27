from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoScheduledjobApiDataConfigDto")


@_attrs_define
class DominoScheduledjobApiDataConfigDto:
    """
    Attributes:
        snapshot_datasets_on_completion (bool):
        snapshot_net_app_volumes_on_completion (bool):
        dataset_config (None | str | Unset):
        external_volume_mounts (list[str] | None | Unset):
        net_app_volume_ids (list[str] | None | Unset):
    """

    snapshot_datasets_on_completion: bool
    snapshot_net_app_volumes_on_completion: bool
    dataset_config: None | str | Unset = UNSET
    external_volume_mounts: list[str] | None | Unset = UNSET
    net_app_volume_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_datasets_on_completion = self.snapshot_datasets_on_completion

        snapshot_net_app_volumes_on_completion = self.snapshot_net_app_volumes_on_completion

        dataset_config: None | str | Unset
        if isinstance(self.dataset_config, Unset):
            dataset_config = UNSET
        else:
            dataset_config = self.dataset_config

        external_volume_mounts: list[str] | None | Unset
        if isinstance(self.external_volume_mounts, Unset):
            external_volume_mounts = UNSET
        elif isinstance(self.external_volume_mounts, list):
            external_volume_mounts = self.external_volume_mounts

        else:
            external_volume_mounts = self.external_volume_mounts

        net_app_volume_ids: list[str] | None | Unset
        if isinstance(self.net_app_volume_ids, Unset):
            net_app_volume_ids = UNSET
        elif isinstance(self.net_app_volume_ids, list):
            net_app_volume_ids = self.net_app_volume_ids

        else:
            net_app_volume_ids = self.net_app_volume_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshotDatasetsOnCompletion": snapshot_datasets_on_completion,
                "snapshotNetAppVolumesOnCompletion": snapshot_net_app_volumes_on_completion,
            }
        )
        if dataset_config is not UNSET:
            field_dict["datasetConfig"] = dataset_config
        if external_volume_mounts is not UNSET:
            field_dict["externalVolumeMounts"] = external_volume_mounts
        if net_app_volume_ids is not UNSET:
            field_dict["netAppVolumeIds"] = net_app_volume_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_datasets_on_completion = d.pop("snapshotDatasetsOnCompletion")

        snapshot_net_app_volumes_on_completion = d.pop("snapshotNetAppVolumesOnCompletion")

        def _parse_dataset_config(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_config = _parse_dataset_config(d.pop("datasetConfig", UNSET))

        def _parse_external_volume_mounts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                external_volume_mounts_type_0 = cast(list[str], data)

                return external_volume_mounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        external_volume_mounts = _parse_external_volume_mounts(d.pop("externalVolumeMounts", UNSET))

        def _parse_net_app_volume_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                net_app_volume_ids_type_0 = cast(list[str], data)

                return net_app_volume_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        net_app_volume_ids = _parse_net_app_volume_ids(d.pop("netAppVolumeIds", UNSET))

        domino_scheduledjob_api_data_config_dto = cls(
            snapshot_datasets_on_completion=snapshot_datasets_on_completion,
            snapshot_net_app_volumes_on_completion=snapshot_net_app_volumes_on_completion,
            dataset_config=dataset_config,
            external_volume_mounts=external_volume_mounts,
            net_app_volume_ids=net_app_volume_ids,
        )

        domino_scheduledjob_api_data_config_dto.additional_properties = d
        return domino_scheduledjob_api_data_config_dto

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
