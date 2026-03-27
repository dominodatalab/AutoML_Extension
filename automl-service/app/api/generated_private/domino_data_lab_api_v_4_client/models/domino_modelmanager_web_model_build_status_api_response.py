from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerWebModelBuildStatusApiResponse")


@_attrs_define
class DominoModelmanagerWebModelBuildStatusApiResponse:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        status (str):
    """

    model_id: str
    model_version_id: str
    status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        status = d.pop("status")

        domino_modelmanager_web_model_build_status_api_response = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            status=status,
        )

        domino_modelmanager_web_model_build_status_api_response.additional_properties = d
        return domino_modelmanager_web_model_build_status_api_response

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
