from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerWebExportVersionStatusWithoutModelResponse")


@_attrs_define
class DominoModelmanagerWebExportVersionStatusWithoutModelResponse:
    """
    Attributes:
        export_id (str):
        export_version_id (str):
        status (str):
        error_message (None | str | Unset):
    """

    export_id: str
    export_version_id: str
    status: str
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_id = self.export_id

        export_version_id = self.export_version_id

        status = self.status

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exportId": export_id,
                "exportVersionId": export_version_id,
                "status": status,
            }
        )
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_id = d.pop("exportId")

        export_version_id = d.pop("exportVersionId")

        status = d.pop("status")

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        domino_modelmanager_web_export_version_status_without_model_response = cls(
            export_id=export_id,
            export_version_id=export_version_id,
            status=status,
            error_message=error_message,
        )

        domino_modelmanager_web_export_version_status_without_model_response.additional_properties = d
        return domino_modelmanager_web_export_version_status_without_model_response

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
