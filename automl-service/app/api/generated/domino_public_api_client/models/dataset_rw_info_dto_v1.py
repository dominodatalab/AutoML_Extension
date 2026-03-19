from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_rw_details_v1 import DatasetRwDetailsV1
    from ..models.dataset_rw_project_info_dto_v1 import DatasetRwProjectInfoDtoV1


T = TypeVar("T", bound="DatasetRwInfoDtoV1")


@_attrs_define
class DatasetRwInfoDtoV1:
    """
    Attributes:
        dataset (DatasetRwDetailsV1):
        project_info (DatasetRwProjectInfoDtoV1 | Unset):
    """

    dataset: DatasetRwDetailsV1
    project_info: DatasetRwProjectInfoDtoV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset = self.dataset.to_dict()

        project_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_info, Unset):
            project_info = self.project_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataset": dataset,
            }
        )
        if project_info is not UNSET:
            field_dict["projectInfo"] = project_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_rw_details_v1 import DatasetRwDetailsV1
        from ..models.dataset_rw_project_info_dto_v1 import DatasetRwProjectInfoDtoV1

        d = dict(src_dict)
        dataset = DatasetRwDetailsV1.from_dict(d.pop("dataset"))

        _project_info = d.pop("projectInfo", UNSET)
        project_info: DatasetRwProjectInfoDtoV1 | Unset
        if isinstance(_project_info, Unset):
            project_info = UNSET
        else:
            project_info = DatasetRwProjectInfoDtoV1.from_dict(_project_info)

        dataset_rw_info_dto_v1 = cls(
            dataset=dataset,
            project_info=project_info,
        )

        dataset_rw_info_dto_v1.additional_properties = d
        return dataset_rw_info_dto_v1

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
