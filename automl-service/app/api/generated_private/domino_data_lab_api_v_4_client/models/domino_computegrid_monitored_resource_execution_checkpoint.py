from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_computegrid_monitored_resource_execution_checkpoint_checkpoint_name import (
    DominoComputegridMonitoredResourceExecutionCheckpointCheckpointName,
)
from ..models.domino_computegrid_monitored_resource_execution_checkpoint_combined_resource_status import (
    DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus,
)
from ..models.domino_computegrid_monitored_resource_execution_checkpoint_status import (
    DominoComputegridMonitoredResourceExecutionCheckpointStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computegrid_monitored_execution_resource_list import (
        DominoComputegridMonitoredExecutionResourceList,
    )


T = TypeVar("T", bound="DominoComputegridMonitoredResourceExecutionCheckpoint")


@_attrs_define
class DominoComputegridMonitoredResourceExecutionCheckpoint:
    """
    Attributes:
        checkpoint_name (DominoComputegridMonitoredResourceExecutionCheckpointCheckpointName):
        status (DominoComputegridMonitoredResourceExecutionCheckpointStatus):
        message (None | str | Unset):
        completed_timestamp (datetime.datetime | None | Unset):
        time_spent_millis (int | None | Unset):
        combined_resource_status (DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus | Unset):
        startup_tip (None | str | Unset):
        resources (list[DominoComputegridMonitoredExecutionResourceList] | None | Unset):
    """

    checkpoint_name: DominoComputegridMonitoredResourceExecutionCheckpointCheckpointName
    status: DominoComputegridMonitoredResourceExecutionCheckpointStatus
    message: None | str | Unset = UNSET
    completed_timestamp: datetime.datetime | None | Unset = UNSET
    time_spent_millis: int | None | Unset = UNSET
    combined_resource_status: DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus | Unset = (
        UNSET
    )
    startup_tip: None | str | Unset = UNSET
    resources: list[DominoComputegridMonitoredExecutionResourceList] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoint_name = self.checkpoint_name.value

        status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        completed_timestamp: None | str | Unset
        if isinstance(self.completed_timestamp, Unset):
            completed_timestamp = UNSET
        elif isinstance(self.completed_timestamp, datetime.datetime):
            completed_timestamp = self.completed_timestamp.isoformat()
        else:
            completed_timestamp = self.completed_timestamp

        time_spent_millis: int | None | Unset
        if isinstance(self.time_spent_millis, Unset):
            time_spent_millis = UNSET
        else:
            time_spent_millis = self.time_spent_millis

        combined_resource_status: str | Unset = UNSET
        if not isinstance(self.combined_resource_status, Unset):
            combined_resource_status = self.combined_resource_status.value

        startup_tip: None | str | Unset
        if isinstance(self.startup_tip, Unset):
            startup_tip = UNSET
        else:
            startup_tip = self.startup_tip

        resources: list[dict[str, Any]] | None | Unset
        if isinstance(self.resources, Unset):
            resources = UNSET
        elif isinstance(self.resources, list):
            resources = []
            for resources_type_0_item_data in self.resources:
                resources_type_0_item = resources_type_0_item_data.to_dict()
                resources.append(resources_type_0_item)

        else:
            resources = self.resources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpointName": checkpoint_name,
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if completed_timestamp is not UNSET:
            field_dict["completedTimestamp"] = completed_timestamp
        if time_spent_millis is not UNSET:
            field_dict["timeSpentMillis"] = time_spent_millis
        if combined_resource_status is not UNSET:
            field_dict["combinedResourceStatus"] = combined_resource_status
        if startup_tip is not UNSET:
            field_dict["startupTip"] = startup_tip
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computegrid_monitored_execution_resource_list import (
            DominoComputegridMonitoredExecutionResourceList,
        )

        d = dict(src_dict)
        checkpoint_name = DominoComputegridMonitoredResourceExecutionCheckpointCheckpointName(d.pop("checkpointName"))

        status = DominoComputegridMonitoredResourceExecutionCheckpointStatus(d.pop("status"))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_completed_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_timestamp_type_0 = isoparse(data)

                return completed_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_timestamp = _parse_completed_timestamp(d.pop("completedTimestamp", UNSET))

        def _parse_time_spent_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_spent_millis = _parse_time_spent_millis(d.pop("timeSpentMillis", UNSET))

        _combined_resource_status = d.pop("combinedResourceStatus", UNSET)
        combined_resource_status: DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus | Unset
        if isinstance(_combined_resource_status, Unset):
            combined_resource_status = UNSET
        else:
            combined_resource_status = DominoComputegridMonitoredResourceExecutionCheckpointCombinedResourceStatus(
                _combined_resource_status
            )

        def _parse_startup_tip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        startup_tip = _parse_startup_tip(d.pop("startupTip", UNSET))

        def _parse_resources(data: object) -> list[DominoComputegridMonitoredExecutionResourceList] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resources_type_0 = []
                _resources_type_0 = data
                for resources_type_0_item_data in _resources_type_0:
                    resources_type_0_item = DominoComputegridMonitoredExecutionResourceList.from_dict(
                        resources_type_0_item_data
                    )

                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoComputegridMonitoredExecutionResourceList] | None | Unset, data)

        resources = _parse_resources(d.pop("resources", UNSET))

        domino_computegrid_monitored_resource_execution_checkpoint = cls(
            checkpoint_name=checkpoint_name,
            status=status,
            message=message,
            completed_timestamp=completed_timestamp,
            time_spent_millis=time_spent_millis,
            combined_resource_status=combined_resource_status,
            startup_tip=startup_tip,
            resources=resources,
        )

        domino_computegrid_monitored_resource_execution_checkpoint.additional_properties = d
        return domino_computegrid_monitored_resource_execution_checkpoint

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
