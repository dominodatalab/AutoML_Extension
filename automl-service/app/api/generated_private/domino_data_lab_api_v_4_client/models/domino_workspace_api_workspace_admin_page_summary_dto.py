from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.information import Information


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceAdminPageSummaryDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceAdminPageSummaryDto:
    """
    Attributes:
        total_num_workspaces (int):
        max_allowed_num_workspaces (int):
        total_allocated_volume_size (Information):
        total_started_workspaces (int):
        max_allowed_allocated_volume_size (Information | Unset):
    """

    total_num_workspaces: int
    max_allowed_num_workspaces: int
    total_allocated_volume_size: Information
    total_started_workspaces: int
    max_allowed_allocated_volume_size: Information | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_num_workspaces = self.total_num_workspaces

        max_allowed_num_workspaces = self.max_allowed_num_workspaces

        total_allocated_volume_size = self.total_allocated_volume_size.to_dict()

        total_started_workspaces = self.total_started_workspaces

        max_allowed_allocated_volume_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_allowed_allocated_volume_size, Unset):
            max_allowed_allocated_volume_size = self.max_allowed_allocated_volume_size.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalNumWorkspaces": total_num_workspaces,
                "maxAllowedNumWorkspaces": max_allowed_num_workspaces,
                "totalAllocatedVolumeSize": total_allocated_volume_size,
                "totalStartedWorkspaces": total_started_workspaces,
            }
        )
        if max_allowed_allocated_volume_size is not UNSET:
            field_dict["maxAllowedAllocatedVolumeSize"] = max_allowed_allocated_volume_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.information import Information

        d = dict(src_dict)
        total_num_workspaces = d.pop("totalNumWorkspaces")

        max_allowed_num_workspaces = d.pop("maxAllowedNumWorkspaces")

        total_allocated_volume_size = Information.from_dict(d.pop("totalAllocatedVolumeSize"))

        total_started_workspaces = d.pop("totalStartedWorkspaces")

        _max_allowed_allocated_volume_size = d.pop("maxAllowedAllocatedVolumeSize", UNSET)
        max_allowed_allocated_volume_size: Information | Unset
        if isinstance(_max_allowed_allocated_volume_size, Unset):
            max_allowed_allocated_volume_size = UNSET
        else:
            max_allowed_allocated_volume_size = Information.from_dict(_max_allowed_allocated_volume_size)

        domino_workspace_api_workspace_admin_page_summary_dto = cls(
            total_num_workspaces=total_num_workspaces,
            max_allowed_num_workspaces=max_allowed_num_workspaces,
            total_allocated_volume_size=total_allocated_volume_size,
            total_started_workspaces=total_started_workspaces,
            max_allowed_allocated_volume_size=max_allowed_allocated_volume_size,
        )

        domino_workspace_api_workspace_admin_page_summary_dto.additional_properties = d
        return domino_workspace_api_workspace_admin_page_summary_dto

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
