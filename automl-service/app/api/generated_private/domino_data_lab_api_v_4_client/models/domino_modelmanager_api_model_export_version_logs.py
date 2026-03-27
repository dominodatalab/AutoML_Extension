from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_export_version_logs_status import (
    DominoModelmanagerApiModelExportVersionLogsStatus,
)

T = TypeVar("T", bound="DominoModelmanagerApiModelExportVersionLogs")


@_attrs_define
class DominoModelmanagerApiModelExportVersionLogs:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        export_version_id (str):
        status (DominoModelmanagerApiModelExportVersionLogsStatus):
        logs (str):
    """

    model_id: str
    model_version_id: str
    export_version_id: str
    status: DominoModelmanagerApiModelExportVersionLogsStatus
    logs: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        export_version_id = self.export_version_id

        status = self.status.value

        logs = self.logs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "exportVersionId": export_version_id,
                "status": status,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        export_version_id = d.pop("exportVersionId")

        status = DominoModelmanagerApiModelExportVersionLogsStatus(d.pop("status"))

        logs = d.pop("logs")

        domino_modelmanager_api_model_export_version_logs = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            export_version_id=export_version_id,
            status=status,
            logs=logs,
        )

        domino_modelmanager_api_model_export_version_logs.additional_properties = d
        return domino_modelmanager_api_model_export_version_logs

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
