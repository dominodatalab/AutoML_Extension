from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_activity_api_activity_activity import DominoActivityApiActivityActivity
from ..models.domino_activity_api_activity_activity_source import DominoActivityApiActivityActivitySource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_activity_api_activity_by import DominoActivityApiActivityBy


T = TypeVar("T", bound="DominoActivityApiActivity")


@_attrs_define
class DominoActivityApiActivity:
    """
    Attributes:
        id (str):
        activity_source (DominoActivityApiActivityActivitySource):
        activity (DominoActivityApiActivityActivity):
        source_id (str):
        timestamp (int):
        project_id (str):
        metadata (Any):
        activity_by (DominoActivityApiActivityBy | Unset):
    """

    id: str
    activity_source: DominoActivityApiActivityActivitySource
    activity: DominoActivityApiActivityActivity
    source_id: str
    timestamp: int
    project_id: str
    metadata: Any
    activity_by: DominoActivityApiActivityBy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_source = self.activity_source.value

        activity = self.activity.value

        source_id = self.source_id

        timestamp = self.timestamp

        project_id = self.project_id

        metadata = self.metadata

        activity_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_by, Unset):
            activity_by = self.activity_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "activitySource": activity_source,
                "activity": activity,
                "sourceId": source_id,
                "timestamp": timestamp,
                "projectId": project_id,
                "metadata": metadata,
            }
        )
        if activity_by is not UNSET:
            field_dict["activityBy"] = activity_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_activity_api_activity_by import DominoActivityApiActivityBy

        d = dict(src_dict)
        id = d.pop("id")

        activity_source = DominoActivityApiActivityActivitySource(d.pop("activitySource"))

        activity = DominoActivityApiActivityActivity(d.pop("activity"))

        source_id = d.pop("sourceId")

        timestamp = d.pop("timestamp")

        project_id = d.pop("projectId")

        metadata = d.pop("metadata")

        _activity_by = d.pop("activityBy", UNSET)
        activity_by: DominoActivityApiActivityBy | Unset
        if isinstance(_activity_by, Unset):
            activity_by = UNSET
        else:
            activity_by = DominoActivityApiActivityBy.from_dict(_activity_by)

        domino_activity_api_activity = cls(
            id=id,
            activity_source=activity_source,
            activity=activity,
            source_id=source_id,
            timestamp=timestamp,
            project_id=project_id,
            metadata=metadata,
            activity_by=activity_by,
        )

        domino_activity_api_activity.additional_properties = d
        return domino_activity_api_activity

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
