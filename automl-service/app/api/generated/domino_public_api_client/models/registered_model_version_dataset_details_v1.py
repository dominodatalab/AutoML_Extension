from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegisteredModelVersionDatasetDetailsV1")


@_attrs_define
class RegisteredModelVersionDatasetDetailsV1:
    """
    Attributes:
        id (str): The id of the dataset
        name (str): The name of the dataset
        snapshot_id (str): The snapshotId of the dataset
    """

    id: str
    name: str
    snapshot_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        snapshot_id = self.snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "snapshotId": snapshot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        snapshot_id = d.pop("snapshotId")

        registered_model_version_dataset_details_v1 = cls(
            id=id,
            name=name,
            snapshot_id=snapshot_id,
        )

        registered_model_version_dataset_details_v1.additional_properties = d
        return registered_model_version_dataset_details_v1

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
