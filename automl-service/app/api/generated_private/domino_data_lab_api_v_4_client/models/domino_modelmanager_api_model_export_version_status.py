from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_export_version_status_status import (
    DominoModelmanagerApiModelExportVersionStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoModelmanagerApiModelExportVersionStatus")


@_attrs_define
class DominoModelmanagerApiModelExportVersionStatus:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        export_id (str):
        export_version_id (str):
        status (DominoModelmanagerApiModelExportVersionStatusStatus):
        error_message (None | str | Unset):
    """

    model_id: str
    model_version_id: str
    export_id: str
    export_version_id: str
    status: DominoModelmanagerApiModelExportVersionStatusStatus
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        export_id = self.export_id

        export_version_id = self.export_version_id

        status = self.status.value

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
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
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        export_id = d.pop("exportId")

        export_version_id = d.pop("exportVersionId")

        status = DominoModelmanagerApiModelExportVersionStatusStatus(d.pop("status"))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        domino_modelmanager_api_model_export_version_status = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            export_id=export_id,
            export_version_id=export_version_id,
            status=status,
            error_message=error_message,
        )

        domino_modelmanager_api_model_export_version_status.additional_properties = d
        return domino_modelmanager_api_model_export_version_status

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
