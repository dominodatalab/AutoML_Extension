from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_endpoint_status_v1 import ModelEndpointStatusV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_endpoint_user_v1 import ModelEndpointUserV1


T = TypeVar("T", bound="ModelEndpointVersionSummaryV1")


@_attrs_define
class ModelEndpointVersionSummaryV1:
    """A summary of a model endpoint version

    Attributes:
        created_at (datetime.datetime): The date and time the model endpoint was created Example:
            2020-10-05T12:56:55.000Z.
        creator (ModelEndpointUserV1):
        number (int): The version number of the model endpoint Example: 1.
        status (ModelEndpointStatusV1):
        label (str | Unset): The label of the model endpoint Example: v1.
    """

    created_at: datetime.datetime
    creator: ModelEndpointUserV1
    number: int
    status: ModelEndpointStatusV1
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        creator = self.creator.to_dict()

        number = self.number

        status = self.status.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "creator": creator,
                "number": number,
                "status": status,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_endpoint_user_v1 import ModelEndpointUserV1

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        creator = ModelEndpointUserV1.from_dict(d.pop("creator"))

        number = d.pop("number")

        status = ModelEndpointStatusV1(d.pop("status"))

        label = d.pop("label", UNSET)

        model_endpoint_version_summary_v1 = cls(
            created_at=created_at,
            creator=creator,
            number=number,
            status=status,
            label=label,
        )

        model_endpoint_version_summary_v1.additional_properties = d
        return model_endpoint_version_summary_v1

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
