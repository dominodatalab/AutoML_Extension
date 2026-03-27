from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_modelmanager_api_model_export_logs_status import DominoModelmanagerApiModelExportLogsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine


T = TypeVar("T", bound="DominoModelmanagerApiModelExportLogs")


@_attrs_define
class DominoModelmanagerApiModelExportLogs:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        status (DominoModelmanagerApiModelExportLogsStatus):
        logs (list[DominoModelmanagerApiLogLine]):
        since_time_nano (int | None | Unset):
    """

    model_id: str
    model_version_id: str
    status: DominoModelmanagerApiModelExportLogsStatus
    logs: list[DominoModelmanagerApiLogLine]
    since_time_nano: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        status = self.status.value

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        since_time_nano: int | None | Unset
        if isinstance(self.since_time_nano, Unset):
            since_time_nano = UNSET
        else:
            since_time_nano = self.since_time_nano

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
        if since_time_nano is not UNSET:
            field_dict["sinceTimeNano"] = since_time_nano

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine

        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        status = DominoModelmanagerApiModelExportLogsStatus(d.pop("status"))

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = DominoModelmanagerApiLogLine.from_dict(logs_item_data)

            logs.append(logs_item)

        def _parse_since_time_nano(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        since_time_nano = _parse_since_time_nano(d.pop("sinceTimeNano", UNSET))

        domino_modelmanager_api_model_export_logs = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            status=status,
            logs=logs,
            since_time_nano=since_time_nano,
        )

        domino_modelmanager_api_model_export_logs.additional_properties = d
        return domino_modelmanager_api_model_export_logs

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
