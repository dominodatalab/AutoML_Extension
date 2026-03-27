from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_admin_interface_user_project_size_in_kb import DominoAdminInterfaceUserProjectSizeInKB


T = TypeVar("T", bound="DominoAdminInterfaceUserProjectEntry")


@_attrs_define
class DominoAdminInterfaceUserProjectEntry:
    """
    Attributes:
        project_id (str):
        name (str):
        created (datetime.datetime):
        runs (int):
        total_run_time_in_hours (float):
        archived (bool):
        owner_username (None | str | Unset):
        owner_name (None | str | Unset):
        last_run_start (datetime.datetime | None | Unset):
        size (DominoAdminInterfaceUserProjectSizeInKB | Unset):
    """

    project_id: str
    name: str
    created: datetime.datetime
    runs: int
    total_run_time_in_hours: float
    archived: bool
    owner_username: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    last_run_start: datetime.datetime | None | Unset = UNSET
    size: DominoAdminInterfaceUserProjectSizeInKB | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        created = self.created.isoformat()

        runs = self.runs

        total_run_time_in_hours = self.total_run_time_in_hours

        archived = self.archived

        owner_username: None | str | Unset
        if isinstance(self.owner_username, Unset):
            owner_username = UNSET
        else:
            owner_username = self.owner_username

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        last_run_start: None | str | Unset
        if isinstance(self.last_run_start, Unset):
            last_run_start = UNSET
        elif isinstance(self.last_run_start, datetime.datetime):
            last_run_start = self.last_run_start.isoformat()
        else:
            last_run_start = self.last_run_start

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectId": project_id,
                "name": name,
                "created": created,
                "runs": runs,
                "totalRunTimeInHours": total_run_time_in_hours,
                "archived": archived,
            }
        )
        if owner_username is not UNSET:
            field_dict["ownerUsername"] = owner_username
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if last_run_start is not UNSET:
            field_dict["lastRunStart"] = last_run_start
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_admin_interface_user_project_size_in_kb import DominoAdminInterfaceUserProjectSizeInKB

        d = dict(src_dict)
        project_id = d.pop("projectId")

        name = d.pop("name")

        created = isoparse(d.pop("created"))

        runs = d.pop("runs")

        total_run_time_in_hours = d.pop("totalRunTimeInHours")

        archived = d.pop("archived")

        def _parse_owner_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_username = _parse_owner_username(d.pop("ownerUsername", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("ownerName", UNSET))

        def _parse_last_run_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_start_type_0 = isoparse(data)

                return last_run_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run_start = _parse_last_run_start(d.pop("lastRunStart", UNSET))

        _size = d.pop("size", UNSET)
        size: DominoAdminInterfaceUserProjectSizeInKB | Unset
        if isinstance(_size, Unset):
            size = UNSET
        else:
            size = DominoAdminInterfaceUserProjectSizeInKB.from_dict(_size)

        domino_admin_interface_user_project_entry = cls(
            project_id=project_id,
            name=name,
            created=created,
            runs=runs,
            total_run_time_in_hours=total_run_time_in_hours,
            archived=archived,
            owner_username=owner_username,
            owner_name=owner_name,
            last_run_start=last_run_start,
            size=size,
        )

        domino_admin_interface_user_project_entry.additional_properties = d
        return domino_admin_interface_user_project_entry

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
