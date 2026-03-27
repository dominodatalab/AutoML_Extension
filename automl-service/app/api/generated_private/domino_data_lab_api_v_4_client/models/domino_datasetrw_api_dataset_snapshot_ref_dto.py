from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetrwApiDatasetSnapshotRefDto")


@_attrs_define
class DominoDatasetrwApiDatasetSnapshotRefDto:
    """
    Attributes:
        dataset_id (str):
        snapshot_version (int):
        dataset_name (None | str | Unset):
    """

    dataset_id: str
    snapshot_version: int
    dataset_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        snapshot_version = self.snapshot_version

        dataset_name: None | str | Unset
        if isinstance(self.dataset_name, Unset):
            dataset_name = UNSET
        else:
            dataset_name = self.dataset_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "snapshotVersion": snapshot_version,
            }
        )
        if dataset_name is not UNSET:
            field_dict["datasetName"] = dataset_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        snapshot_version = d.pop("snapshotVersion")

        def _parse_dataset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_name = _parse_dataset_name(d.pop("datasetName", UNSET))

        domino_datasetrw_api_dataset_snapshot_ref_dto = cls(
            dataset_id=dataset_id,
            snapshot_version=snapshot_version,
            dataset_name=dataset_name,
        )

        domino_datasetrw_api_dataset_snapshot_ref_dto.additional_properties = d
        return domino_datasetrw_api_dataset_snapshot_ref_dto

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
