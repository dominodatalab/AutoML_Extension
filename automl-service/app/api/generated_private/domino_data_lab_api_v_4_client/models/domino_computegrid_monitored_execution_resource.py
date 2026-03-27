from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_computegrid_monitored_execution_resource_startup_status import (
    DominoComputegridMonitoredExecutionResourceStartupStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_computegrid_monitored_execution_resource_extra_info_type_0 import (
        DominoComputegridMonitoredExecutionResourceExtraInfoType0,
    )


T = TypeVar("T", bound="DominoComputegridMonitoredExecutionResource")


@_attrs_define
class DominoComputegridMonitoredExecutionResource:
    """
    Attributes:
        short_name (str):
        full_name (str):
        startup_status (DominoComputegridMonitoredExecutionResourceStartupStatus):
        startup_status_message (str):
        help_text (None | str | Unset):
        debug_text (None | str | Unset):
        last_event_timestamp (datetime.datetime | None | Unset):
        extra_info (DominoComputegridMonitoredExecutionResourceExtraInfoType0 | None | Unset):
    """

    short_name: str
    full_name: str
    startup_status: DominoComputegridMonitoredExecutionResourceStartupStatus
    startup_status_message: str
    help_text: None | str | Unset = UNSET
    debug_text: None | str | Unset = UNSET
    last_event_timestamp: datetime.datetime | None | Unset = UNSET
    extra_info: DominoComputegridMonitoredExecutionResourceExtraInfoType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domino_computegrid_monitored_execution_resource_extra_info_type_0 import (
            DominoComputegridMonitoredExecutionResourceExtraInfoType0,
        )

        short_name = self.short_name

        full_name = self.full_name

        startup_status = self.startup_status.value

        startup_status_message = self.startup_status_message

        help_text: None | str | Unset
        if isinstance(self.help_text, Unset):
            help_text = UNSET
        else:
            help_text = self.help_text

        debug_text: None | str | Unset
        if isinstance(self.debug_text, Unset):
            debug_text = UNSET
        else:
            debug_text = self.debug_text

        last_event_timestamp: None | str | Unset
        if isinstance(self.last_event_timestamp, Unset):
            last_event_timestamp = UNSET
        elif isinstance(self.last_event_timestamp, datetime.datetime):
            last_event_timestamp = self.last_event_timestamp.isoformat()
        else:
            last_event_timestamp = self.last_event_timestamp

        extra_info: dict[str, Any] | None | Unset
        if isinstance(self.extra_info, Unset):
            extra_info = UNSET
        elif isinstance(self.extra_info, DominoComputegridMonitoredExecutionResourceExtraInfoType0):
            extra_info = self.extra_info.to_dict()
        else:
            extra_info = self.extra_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shortName": short_name,
                "fullName": full_name,
                "startupStatus": startup_status,
                "startupStatusMessage": startup_status_message,
            }
        )
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if debug_text is not UNSET:
            field_dict["debugText"] = debug_text
        if last_event_timestamp is not UNSET:
            field_dict["lastEventTimestamp"] = last_event_timestamp
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_computegrid_monitored_execution_resource_extra_info_type_0 import (
            DominoComputegridMonitoredExecutionResourceExtraInfoType0,
        )

        d = dict(src_dict)
        short_name = d.pop("shortName")

        full_name = d.pop("fullName")

        startup_status = DominoComputegridMonitoredExecutionResourceStartupStatus(d.pop("startupStatus"))

        startup_status_message = d.pop("startupStatusMessage")

        def _parse_help_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        help_text = _parse_help_text(d.pop("helpText", UNSET))

        def _parse_debug_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        debug_text = _parse_debug_text(d.pop("debugText", UNSET))

        def _parse_last_event_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_event_timestamp_type_0 = isoparse(data)

                return last_event_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_event_timestamp = _parse_last_event_timestamp(d.pop("lastEventTimestamp", UNSET))

        def _parse_extra_info(data: object) -> DominoComputegridMonitoredExecutionResourceExtraInfoType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_info_type_0 = DominoComputegridMonitoredExecutionResourceExtraInfoType0.from_dict(data)

                return extra_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DominoComputegridMonitoredExecutionResourceExtraInfoType0 | None | Unset, data)

        extra_info = _parse_extra_info(d.pop("extraInfo", UNSET))

        domino_computegrid_monitored_execution_resource = cls(
            short_name=short_name,
            full_name=full_name,
            startup_status=startup_status,
            startup_status_message=startup_status_message,
            help_text=help_text,
            debug_text=debug_text,
            last_event_timestamp=last_event_timestamp,
            extra_info=extra_info,
        )

        domino_computegrid_monitored_execution_resource.additional_properties = d
        return domino_computegrid_monitored_execution_resource

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
