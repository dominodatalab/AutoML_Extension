from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_storage_dto_load_balance_type import (
    DominoDatasetrwApiDatasetRwStorageDtoLoadBalanceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_mount_info_dto import DominoDatasetrwApiDatasetRwMountInfoDto
    from ..models.domino_datasetrw_api_dataset_rw_storage_readiness_dto import (
        DominoDatasetrwApiDatasetRwStorageReadinessDto,
    )


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwStorageDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwStorageDto:
    """
    Attributes:
        id (str):
        name (str):
        data_plane_id (str):
        is_data_plane_default (bool):
        load_balance_type (DominoDatasetrwApiDatasetRwStorageDtoLoadBalanceType):
        storage_added_at (int):
        unregistered_at (int | None | Unset):
        number_of_active_datasets (int | None | Unset):
        data_plane_name (None | str | Unset):
        hardware_tiers (list[str] | None | Unset):
        hostname (None | str | Unset):
        mount_info (DominoDatasetrwApiDatasetRwMountInfoDto | Unset):
        readiness_info (DominoDatasetrwApiDatasetRwStorageReadinessDto | Unset):
    """

    id: str
    name: str
    data_plane_id: str
    is_data_plane_default: bool
    load_balance_type: DominoDatasetrwApiDatasetRwStorageDtoLoadBalanceType
    storage_added_at: int
    unregistered_at: int | None | Unset = UNSET
    number_of_active_datasets: int | None | Unset = UNSET
    data_plane_name: None | str | Unset = UNSET
    hardware_tiers: list[str] | None | Unset = UNSET
    hostname: None | str | Unset = UNSET
    mount_info: DominoDatasetrwApiDatasetRwMountInfoDto | Unset = UNSET
    readiness_info: DominoDatasetrwApiDatasetRwStorageReadinessDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        data_plane_id = self.data_plane_id

        is_data_plane_default = self.is_data_plane_default

        load_balance_type = self.load_balance_type.value

        storage_added_at = self.storage_added_at

        unregistered_at: int | None | Unset
        if isinstance(self.unregistered_at, Unset):
            unregistered_at = UNSET
        else:
            unregistered_at = self.unregistered_at

        number_of_active_datasets: int | None | Unset
        if isinstance(self.number_of_active_datasets, Unset):
            number_of_active_datasets = UNSET
        else:
            number_of_active_datasets = self.number_of_active_datasets

        data_plane_name: None | str | Unset
        if isinstance(self.data_plane_name, Unset):
            data_plane_name = UNSET
        else:
            data_plane_name = self.data_plane_name

        hardware_tiers: list[str] | None | Unset
        if isinstance(self.hardware_tiers, Unset):
            hardware_tiers = UNSET
        elif isinstance(self.hardware_tiers, list):
            hardware_tiers = self.hardware_tiers

        else:
            hardware_tiers = self.hardware_tiers

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        mount_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mount_info, Unset):
            mount_info = self.mount_info.to_dict()

        readiness_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.readiness_info, Unset):
            readiness_info = self.readiness_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "dataPlaneId": data_plane_id,
                "isDataPlaneDefault": is_data_plane_default,
                "loadBalanceType": load_balance_type,
                "storageAddedAt": storage_added_at,
            }
        )
        if unregistered_at is not UNSET:
            field_dict["unregisteredAt"] = unregistered_at
        if number_of_active_datasets is not UNSET:
            field_dict["numberOfActiveDatasets"] = number_of_active_datasets
        if data_plane_name is not UNSET:
            field_dict["dataPlaneName"] = data_plane_name
        if hardware_tiers is not UNSET:
            field_dict["hardwareTiers"] = hardware_tiers
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if mount_info is not UNSET:
            field_dict["mountInfo"] = mount_info
        if readiness_info is not UNSET:
            field_dict["readinessInfo"] = readiness_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_mount_info_dto import DominoDatasetrwApiDatasetRwMountInfoDto
        from ..models.domino_datasetrw_api_dataset_rw_storage_readiness_dto import (
            DominoDatasetrwApiDatasetRwStorageReadinessDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        data_plane_id = d.pop("dataPlaneId")

        is_data_plane_default = d.pop("isDataPlaneDefault")

        load_balance_type = DominoDatasetrwApiDatasetRwStorageDtoLoadBalanceType(d.pop("loadBalanceType"))

        storage_added_at = d.pop("storageAddedAt")

        def _parse_unregistered_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unregistered_at = _parse_unregistered_at(d.pop("unregisteredAt", UNSET))

        def _parse_number_of_active_datasets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_active_datasets = _parse_number_of_active_datasets(d.pop("numberOfActiveDatasets", UNSET))

        def _parse_data_plane_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_plane_name = _parse_data_plane_name(d.pop("dataPlaneName", UNSET))

        def _parse_hardware_tiers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hardware_tiers_type_0 = cast(list[str], data)

                return hardware_tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hardware_tiers = _parse_hardware_tiers(d.pop("hardwareTiers", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        _mount_info = d.pop("mountInfo", UNSET)
        mount_info: DominoDatasetrwApiDatasetRwMountInfoDto | Unset
        if isinstance(_mount_info, Unset):
            mount_info = UNSET
        else:
            mount_info = DominoDatasetrwApiDatasetRwMountInfoDto.from_dict(_mount_info)

        _readiness_info = d.pop("readinessInfo", UNSET)
        readiness_info: DominoDatasetrwApiDatasetRwStorageReadinessDto | Unset
        if isinstance(_readiness_info, Unset):
            readiness_info = UNSET
        else:
            readiness_info = DominoDatasetrwApiDatasetRwStorageReadinessDto.from_dict(_readiness_info)

        domino_datasetrw_api_dataset_rw_storage_dto = cls(
            id=id,
            name=name,
            data_plane_id=data_plane_id,
            is_data_plane_default=is_data_plane_default,
            load_balance_type=load_balance_type,
            storage_added_at=storage_added_at,
            unregistered_at=unregistered_at,
            number_of_active_datasets=number_of_active_datasets,
            data_plane_name=data_plane_name,
            hardware_tiers=hardware_tiers,
            hostname=hostname,
            mount_info=mount_info,
            readiness_info=readiness_info,
        )

        domino_datasetrw_api_dataset_rw_storage_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_storage_dto

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
