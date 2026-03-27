from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoModelmanagerWebModelPermissionsForMonitoringRequest")


@_attrs_define
class DominoModelmanagerWebModelPermissionsForMonitoringRequest:
    """
    Attributes:
        user_id_to_check_permissions_for (str):
        model_ids (list[str]):
    """

    user_id_to_check_permissions_for: str
    model_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id_to_check_permissions_for = self.user_id_to_check_permissions_for

        model_ids = self.model_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userIdToCheckPermissionsFor": user_id_to_check_permissions_for,
                "modelIds": model_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id_to_check_permissions_for = d.pop("userIdToCheckPermissionsFor")

        model_ids = cast(list[str], d.pop("modelIds"))

        domino_modelmanager_web_model_permissions_for_monitoring_request = cls(
            user_id_to_check_permissions_for=user_id_to_check_permissions_for,
            model_ids=model_ids,
        )

        domino_modelmanager_web_model_permissions_for_monitoring_request.additional_properties = d
        return domino_modelmanager_web_model_permissions_for_monitoring_request

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
