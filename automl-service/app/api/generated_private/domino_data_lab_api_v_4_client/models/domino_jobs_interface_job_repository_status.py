from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_jobs_interface_job_repository_status_status import DominoJobsInterfaceJobRepositoryStatusStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_repository_changes import DominoJobsInterfaceRepositoryChanges


T = TypeVar("T", bound="DominoJobsInterfaceJobRepositoryStatus")


@_attrs_define
class DominoJobsInterfaceJobRepositoryStatus:
    """
    Attributes:
        name (str):
        status (DominoJobsInterfaceJobRepositoryStatusStatus):
        changes (DominoJobsInterfaceRepositoryChanges | Unset):
    """

    name: str
    status: DominoJobsInterfaceJobRepositoryStatusStatus
    changes: DominoJobsInterfaceRepositoryChanges | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.value

        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_repository_changes import DominoJobsInterfaceRepositoryChanges

        d = dict(src_dict)
        name = d.pop("name")

        status = DominoJobsInterfaceJobRepositoryStatusStatus(d.pop("status"))

        _changes = d.pop("changes", UNSET)
        changes: DominoJobsInterfaceRepositoryChanges | Unset
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = DominoJobsInterfaceRepositoryChanges.from_dict(_changes)

        domino_jobs_interface_job_repository_status = cls(
            name=name,
            status=status,
            changes=changes,
        )

        domino_jobs_interface_job_repository_status.additional_properties = d
        return domino_jobs_interface_job_repository_status

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
