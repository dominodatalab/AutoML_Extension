from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoFilesInterfaceProjectReleaseDto")


@_attrs_define
class DominoFilesInterfaceProjectReleaseDto:
    """
    Attributes:
        release_id (str):
        run_number (int):
        run_heading (str):
        created_at (str):
        is_selected (bool):
    """

    release_id: str
    run_number: int
    run_heading: str
    created_at: str
    is_selected: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_id = self.release_id

        run_number = self.run_number

        run_heading = self.run_heading

        created_at = self.created_at

        is_selected = self.is_selected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "releaseId": release_id,
                "runNumber": run_number,
                "runHeading": run_heading,
                "createdAt": created_at,
                "isSelected": is_selected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        release_id = d.pop("releaseId")

        run_number = d.pop("runNumber")

        run_heading = d.pop("runHeading")

        created_at = d.pop("createdAt")

        is_selected = d.pop("isSelected")

        domino_files_interface_project_release_dto = cls(
            release_id=release_id,
            run_number=run_number,
            run_heading=run_heading,
            created_at=created_at,
            is_selected=is_selected,
        )

        domino_files_interface_project_release_dto.additional_properties = d
        return domino_files_interface_project_release_dto

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
