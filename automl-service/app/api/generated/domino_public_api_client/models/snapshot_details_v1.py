from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.snapshot_details_v1_status import SnapshotDetailsV1Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="SnapshotDetailsV1")


@_attrs_define
class SnapshotDetailsV1:
    """
    Attributes:
        created_at (datetime.datetime): When the snapshot was created Example: 2022-03-12T02:13:44.467Z.
        dataset_id (str): ID of the dataset this snapshot belongs to
        id (str): ID of this snapshot
        status (SnapshotDetailsV1Status):
        creator_id (str | Unset): ID of the user who created this snapshot
        description (str | Unset):
        last_mounted (datetime.datetime | Unset): When the snapshot was last mounted
    """

    created_at: datetime.datetime
    dataset_id: str
    id: str
    status: SnapshotDetailsV1Status
    creator_id: str | Unset = UNSET
    description: str | Unset = UNSET
    last_mounted: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        id = self.id

        status = self.status.value

        creator_id = self.creator_id

        description = self.description

        last_mounted: str | Unset = UNSET
        if not isinstance(self.last_mounted, Unset):
            last_mounted = self.last_mounted.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "datasetId": dataset_id,
                "id": id,
                "status": status,
            }
        )
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if description is not UNSET:
            field_dict["description"] = description
        if last_mounted is not UNSET:
            field_dict["lastMounted"] = last_mounted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        dataset_id = d.pop("datasetId")

        id = d.pop("id")

        status = SnapshotDetailsV1Status(d.pop("status"))

        creator_id = d.pop("creatorId", UNSET)

        description = d.pop("description", UNSET)

        _last_mounted = d.pop("lastMounted", UNSET)
        last_mounted: datetime.datetime | Unset
        if isinstance(_last_mounted, Unset):
            last_mounted = UNSET
        else:
            last_mounted = isoparse(_last_mounted)

        snapshot_details_v1 = cls(
            created_at=created_at,
            dataset_id=dataset_id,
            id=id,
            status=status,
            creator_id=creator_id,
            description=description,
            last_mounted=last_mounted,
        )

        snapshot_details_v1.additional_properties = d
        return snapshot_details_v1

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
