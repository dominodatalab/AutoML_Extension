from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_build_logs_v2_status import DominoModelmanagerApiModelBuildLogsV2Status

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine


T = TypeVar("T", bound="DominoModelmanagerApiModelBuildLogsV2")


@_attrs_define
class DominoModelmanagerApiModelBuildLogsV2:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        status (DominoModelmanagerApiModelBuildLogsV2Status):
        logs (list[DominoModelmanagerApiLogLine]):
    """

    model_id: str
    model_version_id: str
    status: DominoModelmanagerApiModelBuildLogsV2Status
    logs: list[DominoModelmanagerApiLogLine]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        status = self.status.value

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "status": status,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine

        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        status = DominoModelmanagerApiModelBuildLogsV2Status(d.pop("status"))

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = DominoModelmanagerApiLogLine.from_dict(logs_item_data)

            logs.append(logs_item)

        domino_modelmanager_api_model_build_logs_v2 = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            status=status,
            logs=logs,
        )

        domino_modelmanager_api_model_build_logs_v2.additional_properties = d
        return domino_modelmanager_api_model_build_logs_v2

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
