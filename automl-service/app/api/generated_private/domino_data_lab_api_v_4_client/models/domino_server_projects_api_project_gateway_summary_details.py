from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoServerProjectsApiProjectGatewaySummaryDetails")


@_attrs_define
class DominoServerProjectsApiProjectGatewaySummaryDetails:
    """
    Attributes:
        updated_at (datetime.datetime):
        is_restricted (bool | None | Unset):
    """

    updated_at: datetime.datetime
    is_restricted: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updatedAt": updated_at,
            }
        )
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("isRestricted", UNSET))

        domino_server_projects_api_project_gateway_summary_details = cls(
            updated_at=updated_at,
            is_restricted=is_restricted,
        )

        domino_server_projects_api_project_gateway_summary_details.additional_properties = d
        return domino_server_projects_api_project_gateway_summary_details

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
