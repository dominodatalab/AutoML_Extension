from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoAdminInterfaceUserProjectSizeInKB")


@_attrs_define
class DominoAdminInterfaceUserProjectSizeInKB:
    """
    Attributes:
        last_updated (datetime.datetime):
        unit (str):
        domino_file_system (float | None | Unset):
    """

    last_updated: datetime.datetime
    unit: str
    domino_file_system: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_updated = self.last_updated.isoformat()

        unit = self.unit

        domino_file_system: float | None | Unset
        if isinstance(self.domino_file_system, Unset):
            domino_file_system = UNSET
        else:
            domino_file_system = self.domino_file_system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastUpdated": last_updated,
                "unit": unit,
            }
        )
        if domino_file_system is not UNSET:
            field_dict["dominoFileSystem"] = domino_file_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_updated = isoparse(d.pop("lastUpdated"))

        unit = d.pop("unit")

        def _parse_domino_file_system(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        domino_file_system = _parse_domino_file_system(d.pop("dominoFileSystem", UNSET))

        domino_admin_interface_user_project_size_in_kb = cls(
            last_updated=last_updated,
            unit=unit,
            domino_file_system=domino_file_system,
        )

        domino_admin_interface_user_project_size_in_kb.additional_properties = d
        return domino_admin_interface_user_project_size_in_kb

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
