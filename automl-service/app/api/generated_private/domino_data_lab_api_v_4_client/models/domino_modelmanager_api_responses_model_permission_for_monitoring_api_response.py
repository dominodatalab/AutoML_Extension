from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerApiResponsesModelPermissionForMonitoringApiResponse")


@_attrs_define
class DominoModelmanagerApiResponsesModelPermissionForMonitoringApiResponse:
    """
    Attributes:
        model_id (str):
        can_list_model_api (bool):
    """

    model_id: str
    can_list_model_api: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        can_list_model_api = self.can_list_model_api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "canListModelApi": can_list_model_api,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        can_list_model_api = d.pop("canListModelApi")

        domino_modelmanager_api_responses_model_permission_for_monitoring_api_response = cls(
            model_id=model_id,
            can_list_model_api=can_list_model_api,
        )

        domino_modelmanager_api_responses_model_permission_for_monitoring_api_response.additional_properties = d
        return domino_modelmanager_api_responses_model_permission_for_monitoring_api_response

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
