from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine


T = TypeVar("T", bound="DominoModelmanagerApiModelInstanceLogs")


@_attrs_define
class DominoModelmanagerApiModelInstanceLogs:
    """
    Attributes:
        model_id (str):
        model_version_id (str):
        max_results (int):
        logs (list[DominoModelmanagerApiLogLine]):
        pod_name (None | str | Unset):
        container_name (None | str | Unset):
        since_time_nano (int | None | Unset):
        tail (bool | None | Unset):
    """

    model_id: str
    model_version_id: str
    max_results: int
    logs: list[DominoModelmanagerApiLogLine]
    pod_name: None | str | Unset = UNSET
    container_name: None | str | Unset = UNSET
    since_time_nano: int | None | Unset = UNSET
    tail: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        model_version_id = self.model_version_id

        max_results = self.max_results

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        pod_name: None | str | Unset
        if isinstance(self.pod_name, Unset):
            pod_name = UNSET
        else:
            pod_name = self.pod_name

        container_name: None | str | Unset
        if isinstance(self.container_name, Unset):
            container_name = UNSET
        else:
            container_name = self.container_name

        since_time_nano: int | None | Unset
        if isinstance(self.since_time_nano, Unset):
            since_time_nano = UNSET
        else:
            since_time_nano = self.since_time_nano

        tail: bool | None | Unset
        if isinstance(self.tail, Unset):
            tail = UNSET
        else:
            tail = self.tail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelId": model_id,
                "modelVersionId": model_version_id,
                "maxResults": max_results,
                "logs": logs,
            }
        )
        if pod_name is not UNSET:
            field_dict["podName"] = pod_name
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if since_time_nano is not UNSET:
            field_dict["sinceTimeNano"] = since_time_nano
        if tail is not UNSET:
            field_dict["tail"] = tail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_modelmanager_api_log_line import DominoModelmanagerApiLogLine

        d = dict(src_dict)
        model_id = d.pop("modelId")

        model_version_id = d.pop("modelVersionId")

        max_results = d.pop("maxResults")

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = DominoModelmanagerApiLogLine.from_dict(logs_item_data)

            logs.append(logs_item)

        def _parse_pod_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pod_name = _parse_pod_name(d.pop("podName", UNSET))

        def _parse_container_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_name = _parse_container_name(d.pop("containerName", UNSET))

        def _parse_since_time_nano(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        since_time_nano = _parse_since_time_nano(d.pop("sinceTimeNano", UNSET))

        def _parse_tail(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        tail = _parse_tail(d.pop("tail", UNSET))

        domino_modelmanager_api_model_instance_logs = cls(
            model_id=model_id,
            model_version_id=model_version_id,
            max_results=max_results,
            logs=logs,
            pod_name=pod_name,
            container_name=container_name,
            since_time_nano=since_time_nano,
            tail=tail,
        )

        domino_modelmanager_api_model_instance_logs.additional_properties = d
        return domino_modelmanager_api_model_instance_logs

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
