from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_version_log_line import ModelApiVersionLogLine


T = TypeVar("T", bound="ModelApiVersionBuildLogs")


@_attrs_define
class ModelApiVersionBuildLogs:
    """
    Attributes:
        logs (list[ModelApiVersionLogLine]): The build logs.
        model_id (str): The id of the Model API
        model_version_id (str): The id of the Model API Version
        status (str): The status of the build.
        build_id (str | Unset): The id of the build of the Model API Version
        since_time_nano (str | Unset): The start date of the logs.
    """

    logs: list[ModelApiVersionLogLine]
    model_id: str
    model_version_id: str
    status: str
    build_id: str | Unset = UNSET
    since_time_nano: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        model_id = self.model_id

        model_version_id = self.model_version_id

        status = self.status

        build_id = self.build_id

        since_time_nano = self.since_time_nano

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logs": logs,
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "status": status,
            }
        )
        if build_id is not UNSET:
            field_dict["buildId"] = build_id
        if since_time_nano is not UNSET:
            field_dict["sinceTimeNano"] = since_time_nano

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_version_log_line import ModelApiVersionLogLine

        d = dict(src_dict)
        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = ModelApiVersionLogLine.from_dict(logs_item_data)

            logs.append(logs_item)

        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        status = d.pop("status")

        build_id = d.pop("buildId", UNSET)

        since_time_nano = d.pop("sinceTimeNano", UNSET)

        model_api_version_build_logs = cls(
            logs=logs,
            model_id=model_id,
            model_version_id=model_version_id,
            status=status,
            build_id=build_id,
            since_time_nano=since_time_nano,
        )

        model_api_version_build_logs.additional_properties = d
        return model_api_version_build_logs

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
