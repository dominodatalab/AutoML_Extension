from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_model_version_status_activity_meta_data_action import (
    DominoActivityApiModelVersionStatusActivityMetaDataAction,
)

T = TypeVar("T", bound="DominoActivityApiModelVersionStatusActivityMetaData")


@_attrs_define
class DominoActivityApiModelVersionStatusActivityMetaData:
    """
    Attributes:
        action (DominoActivityApiModelVersionStatusActivityMetaDataAction):
        current_status (str):
        model_name (str):
        model_id (str):
        model_version_number (int):
    """

    action: DominoActivityApiModelVersionStatusActivityMetaDataAction
    current_status: str
    model_name: str
    model_id: str
    model_version_number: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        current_status = self.current_status

        model_name = self.model_name

        model_id = self.model_id

        model_version_number = self.model_version_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "currentStatus": current_status,
                "modelName": model_name,
                "modelId": model_id,
                "modelVersionNumber": model_version_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = DominoActivityApiModelVersionStatusActivityMetaDataAction(d.pop("action"))

        current_status = d.pop("currentStatus")

        model_name = d.pop("modelName")

        model_id = d.pop("modelId")

        model_version_number = d.pop("modelVersionNumber")

        domino_activity_api_model_version_status_activity_meta_data = cls(
            action=action,
            current_status=current_status,
            model_name=model_name,
            model_id=model_id,
            model_version_number=model_version_number,
        )

        domino_activity_api_model_version_status_activity_meta_data.additional_properties = d
        return domino_activity_api_model_version_status_activity_meta_data

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
