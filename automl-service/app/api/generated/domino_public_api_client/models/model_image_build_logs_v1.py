from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_image_build_logs_v1_build_status import ModelImageBuildLogsV1BuildStatus

if TYPE_CHECKING:
    from ..models.build_log_line_v1 import BuildLogLineV1


T = TypeVar("T", bound="ModelImageBuildLogsV1")


@_attrs_define
class ModelImageBuildLogsV1:
    """
    Attributes:
        build_id (str):
        build_status (ModelImageBuildLogsV1BuildStatus):
        logs (list[BuildLogLineV1]):
        model_name (str):
        model_version (str):
    """

    build_id: str
    build_status: ModelImageBuildLogsV1BuildStatus
    logs: list[BuildLogLineV1]
    model_name: str
    model_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_id = self.build_id

        build_status = self.build_status.value

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        model_name = self.model_name

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buildId": build_id,
                "buildStatus": build_status,
                "logs": logs,
                "modelName": model_name,
                "modelVersion": model_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_log_line_v1 import BuildLogLineV1

        d = dict(src_dict)
        build_id = d.pop("buildId")

        build_status = ModelImageBuildLogsV1BuildStatus(d.pop("buildStatus"))

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = BuildLogLineV1.from_dict(logs_item_data)

            logs.append(logs_item)

        model_name = d.pop("modelName")

        model_version = d.pop("modelVersion")

        model_image_build_logs_v1 = cls(
            build_id=build_id,
            build_status=build_status,
            logs=logs,
            model_name=model_name,
            model_version=model_version,
        )

        model_image_build_logs_v1.additional_properties = d
        return model_image_build_logs_v1

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
