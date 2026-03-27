from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_dto import DominoDatasetrwApiDatasetRwDto
    from ..models.domino_datasetrw_api_dataset_rw_project_info_dto import DominoDatasetrwApiDatasetRwProjectInfoDto
    from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwInfoDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwInfoDto:
    """
    Attributes:
        dataset_rw_dto (DominoDatasetrwApiDatasetRwDto):
        project_info (DominoDatasetrwApiDatasetRwProjectInfoDto | Unset):
        storage_info (DominoDatasetrwApiDatasetRwStorageInfoDto | Unset):
    """

    dataset_rw_dto: DominoDatasetrwApiDatasetRwDto
    project_info: DominoDatasetrwApiDatasetRwProjectInfoDto | Unset = UNSET
    storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_rw_dto = self.dataset_rw_dto.to_dict()

        project_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_info, Unset):
            project_info = self.project_info.to_dict()

        storage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_info, Unset):
            storage_info = self.storage_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetRwDto": dataset_rw_dto,
            }
        )
        if project_info is not UNSET:
            field_dict["projectInfo"] = project_info
        if storage_info is not UNSET:
            field_dict["storageInfo"] = storage_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_dto import DominoDatasetrwApiDatasetRwDto
        from ..models.domino_datasetrw_api_dataset_rw_project_info_dto import DominoDatasetrwApiDatasetRwProjectInfoDto
        from ..models.domino_datasetrw_api_dataset_rw_storage_info_dto import DominoDatasetrwApiDatasetRwStorageInfoDto

        d = dict(src_dict)
        dataset_rw_dto = DominoDatasetrwApiDatasetRwDto.from_dict(d.pop("datasetRwDto"))

        _project_info = d.pop("projectInfo", UNSET)
        project_info: DominoDatasetrwApiDatasetRwProjectInfoDto | Unset
        if isinstance(_project_info, Unset):
            project_info = UNSET
        else:
            project_info = DominoDatasetrwApiDatasetRwProjectInfoDto.from_dict(_project_info)

        _storage_info = d.pop("storageInfo", UNSET)
        storage_info: DominoDatasetrwApiDatasetRwStorageInfoDto | Unset
        if isinstance(_storage_info, Unset):
            storage_info = UNSET
        else:
            storage_info = DominoDatasetrwApiDatasetRwStorageInfoDto.from_dict(_storage_info)

        domino_datasetrw_api_dataset_rw_info_dto = cls(
            dataset_rw_dto=dataset_rw_dto,
            project_info=project_info,
            storage_info=storage_info,
        )

        domino_datasetrw_api_dataset_rw_info_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_info_dto

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
