from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_api_version_log_line import ModelApiVersionLogLine


T = TypeVar("T", bound="ModelApiVersionInstanceLogs")


@_attrs_define
class ModelApiVersionInstanceLogs:
    """
    Attributes:
        logs (list[ModelApiVersionLogLine]): The instance logs.
        max_results (int): The maximum number of logs to retrieve
        model_id (str): The id of the Model API
        model_version_id (str): The id of the Model API Version
        container_name (str | Unset): The name of the container the Model API Version is deployed to.
        pod_name (str | Unset): The name of the pod the Model API Version is deployed to.
        since_time_nano (str | Unset): The start date of the logs.
        tail (bool | Unset): Whether to fetch from tail or not
    """

    logs: list[ModelApiVersionLogLine]
    max_results: int
    model_id: str
    model_version_id: str
    container_name: str | Unset = UNSET
    pod_name: str | Unset = UNSET
    since_time_nano: str | Unset = UNSET
    tail: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        max_results = self.max_results

        model_id = self.model_id

        model_version_id = self.model_version_id

        container_name = self.container_name

        pod_name = self.pod_name

        since_time_nano = self.since_time_nano

        tail = self.tail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logs": logs,
                "maxResults": max_results,
                "modelId": model_id,
                "modelVersionId": model_version_id,
            }
        )
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if pod_name is not UNSET:
            field_dict["podName"] = pod_name
        if since_time_nano is not UNSET:
            field_dict["sinceTimeNano"] = since_time_nano
        if tail is not UNSET:
            field_dict["tail"] = tail

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

        max_results = d.pop("maxResults")

        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        container_name = d.pop("containerName", UNSET)

        pod_name = d.pop("podName", UNSET)

        since_time_nano = d.pop("sinceTimeNano", UNSET)

        tail = d.pop("tail", UNSET)

        model_api_version_instance_logs = cls(
            logs=logs,
            max_results=max_results,
            model_id=model_id,
            model_version_id=model_version_id,
            container_name=container_name,
            pod_name=pod_name,
            since_time_nano=since_time_nano,
            tail=tail,
        )

        model_api_version_instance_logs.additional_properties = d
        return model_api_version_instance_logs

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
