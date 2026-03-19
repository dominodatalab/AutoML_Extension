from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TagV1")


@_attrs_define
class TagV1:
    """
    Attributes:
        created_at (datetime.datetime): When the tag was created. Example: 2022-03-15T21:48:36.586Z.
        creator_id (str): Id of the user who created the tag. Example: 6231342b7a0af0281c01a69e.
        id (str): Id of the tag. Example: 623133e87a0af0281c01a69d.
        name (str): Name of the tag. Example: KMeansTest.
    """

    created_at: datetime.datetime
    creator_id: str
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator_id = self.creator_id

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "creatorId": creator_id,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        creator_id = d.pop("creatorId")

        id = d.pop("id")

        name = d.pop("name")

        tag_v1 = cls(
            created_at=created_at,
            creator_id=creator_id,
            id=id,
            name=name,
        )

        tag_v1.additional_properties = d
        return tag_v1

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
