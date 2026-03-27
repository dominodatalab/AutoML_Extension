from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_gruz_api_run_post_processing_control import DominoGruzApiRunPostProcessingControl


T = TypeVar("T", bound="DominoGruzApiRunPostProcessing")


@_attrs_define
class DominoGruzApiRunPostProcessing:
    """
    Attributes:
        post_processing_control (DominoGruzApiRunPostProcessingControl | Unset):
        post_processed_timestamp (datetime.datetime | None | Unset):
    """

    post_processing_control: DominoGruzApiRunPostProcessingControl | Unset = UNSET
    post_processed_timestamp: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_processing_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_processing_control, Unset):
            post_processing_control = self.post_processing_control.to_dict()

        post_processed_timestamp: None | str | Unset
        if isinstance(self.post_processed_timestamp, Unset):
            post_processed_timestamp = UNSET
        elif isinstance(self.post_processed_timestamp, datetime.datetime):
            post_processed_timestamp = self.post_processed_timestamp.isoformat()
        else:
            post_processed_timestamp = self.post_processed_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_processing_control is not UNSET:
            field_dict["postProcessingControl"] = post_processing_control
        if post_processed_timestamp is not UNSET:
            field_dict["postProcessedTimestamp"] = post_processed_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_gruz_api_run_post_processing_control import DominoGruzApiRunPostProcessingControl

        d = dict(src_dict)
        _post_processing_control = d.pop("postProcessingControl", UNSET)
        post_processing_control: DominoGruzApiRunPostProcessingControl | Unset
        if isinstance(_post_processing_control, Unset):
            post_processing_control = UNSET
        else:
            post_processing_control = DominoGruzApiRunPostProcessingControl.from_dict(_post_processing_control)

        def _parse_post_processed_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_processed_timestamp_type_0 = isoparse(data)

                return post_processed_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        post_processed_timestamp = _parse_post_processed_timestamp(d.pop("postProcessedTimestamp", UNSET))

        domino_gruz_api_run_post_processing = cls(
            post_processing_control=post_processing_control,
            post_processed_timestamp=post_processed_timestamp,
        )

        domino_gruz_api_run_post_processing.additional_properties = d
        return domino_gruz_api_run_post_processing

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
