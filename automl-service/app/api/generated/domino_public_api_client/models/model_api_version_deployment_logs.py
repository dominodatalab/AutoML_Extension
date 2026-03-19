from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_version_log_line import ModelApiVersionLogLine


T = TypeVar("T", bound="ModelApiVersionDeploymentLogs")


@_attrs_define
class ModelApiVersionDeploymentLogs:
    """
    Attributes:
        logs (list[ModelApiVersionLogLine] | Unset): The deployment logs.
        status (str | Unset): The status of the deployment.
    """

    logs: list[ModelApiVersionLogLine] | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_api_version_log_line import ModelApiVersionLogLine

        d = dict(src_dict)
        _logs = d.pop("logs", UNSET)
        logs: list[ModelApiVersionLogLine] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = ModelApiVersionLogLine.from_dict(logs_item_data)

                logs.append(logs_item)

        status = d.pop("status", UNSET)

        model_api_version_deployment_logs = cls(
            logs=logs,
            status=status,
        )

        model_api_version_deployment_logs.additional_properties = d
        return model_api_version_deployment_logs

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
