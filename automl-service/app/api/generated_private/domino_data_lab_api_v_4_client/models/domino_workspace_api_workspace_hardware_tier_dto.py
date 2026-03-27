from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_hardwaretier_api_hardware_tier_identifier import DominoHardwaretierApiHardwareTierIdentifier
    from ..models.domino_workspace_api_data_plane_ref_dto import DominoWorkspaceApiDataPlaneRefDto


T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceHardwareTierDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceHardwareTierDto:
    """
    Attributes:
        id (DominoHardwaretierApiHardwareTierIdentifier):
        name (str):
        data_plane (DominoWorkspaceApiDataPlaneRefDto | Unset):
    """

    id: DominoHardwaretierApiHardwareTierIdentifier
    name: str
    data_plane: DominoWorkspaceApiDataPlaneRefDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        name = self.name

        data_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_plane, Unset):
            data_plane = self.data_plane.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if data_plane is not UNSET:
            field_dict["dataPlane"] = data_plane

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_hardwaretier_api_hardware_tier_identifier import (
            DominoHardwaretierApiHardwareTierIdentifier,
        )
        from ..models.domino_workspace_api_data_plane_ref_dto import DominoWorkspaceApiDataPlaneRefDto

        d = dict(src_dict)
        id = DominoHardwaretierApiHardwareTierIdentifier.from_dict(d.pop("id"))

        name = d.pop("name")

        _data_plane = d.pop("dataPlane", UNSET)
        data_plane: DominoWorkspaceApiDataPlaneRefDto | Unset
        if isinstance(_data_plane, Unset):
            data_plane = UNSET
        else:
            data_plane = DominoWorkspaceApiDataPlaneRefDto.from_dict(_data_plane)

        domino_workspace_api_workspace_hardware_tier_dto = cls(
            id=id,
            name=name,
            data_plane=data_plane,
        )

        domino_workspace_api_workspace_hardware_tier_dto.additional_properties = d
        return domino_workspace_api_workspace_hardware_tier_dto

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
