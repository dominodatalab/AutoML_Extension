from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwUploadSessionDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwUploadSessionDto:
    """
    Attributes:
        upload_key (str):
        last_touched (int):
        dataset_id (str):
        id (str):
    """

    upload_key: str
    last_touched: int
    dataset_id: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_key = self.upload_key

        last_touched = self.last_touched

        dataset_id = self.dataset_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadKey": upload_key,
                "lastTouched": last_touched,
                "datasetId": dataset_id,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_key = d.pop("uploadKey")

        last_touched = d.pop("lastTouched")

        dataset_id = d.pop("datasetId")

        id = d.pop("id")

        domino_datasetrw_api_dataset_rw_upload_session_dto = cls(
            upload_key=upload_key,
            last_touched=last_touched,
            dataset_id=dataset_id,
            id=id,
        )

        domino_datasetrw_api_dataset_rw_upload_session_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_upload_session_dto

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
