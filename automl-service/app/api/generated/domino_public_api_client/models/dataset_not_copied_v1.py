from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dataset_info_v1 import DatasetInfoV1


T = TypeVar("T", bound="DatasetNotCopiedV1")


@_attrs_define
class DatasetNotCopiedV1:
    """
    Attributes:
        dataset_info (DatasetInfoV1):
        error_message (str): error message explaining why dataset wasn't copied
    """

    dataset_info: DatasetInfoV1
    error_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_info = self.dataset_info.to_dict()

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetInfo": dataset_info,
                "errorMessage": error_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_info_v1 import DatasetInfoV1

        d = dict(src_dict)
        dataset_info = DatasetInfoV1.from_dict(d.pop("datasetInfo"))

        error_message = d.pop("errorMessage")

        dataset_not_copied_v1 = cls(
            dataset_info=dataset_info,
            error_message=error_message,
        )

        dataset_not_copied_v1.additional_properties = d
        return dataset_not_copied_v1

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
