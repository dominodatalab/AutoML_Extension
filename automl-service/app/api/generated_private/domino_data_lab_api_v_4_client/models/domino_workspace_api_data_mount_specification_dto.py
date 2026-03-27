from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_workspace_api_volume_mount_dto import DominoWorkspaceApiVolumeMountDto


T = TypeVar("T", bound="DominoWorkspaceApiDataMountSpecificationDto")


@_attrs_define
class DominoWorkspaceApiDataMountSpecificationDto:
    """
    Attributes:
        name (str):
        mount (DominoWorkspaceApiVolumeMountDto):
        id (None | str | Unset):
    """

    name: str
    mount: DominoWorkspaceApiVolumeMountDto
    id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mount = self.mount.to_dict()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mount": mount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_workspace_api_volume_mount_dto import DominoWorkspaceApiVolumeMountDto

        d = dict(src_dict)
        name = d.pop("name")

        mount = DominoWorkspaceApiVolumeMountDto.from_dict(d.pop("mount"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        domino_workspace_api_data_mount_specification_dto = cls(
            name=name,
            mount=mount,
            id=id,
        )

        domino_workspace_api_data_mount_specification_dto.additional_properties = d
        return domino_workspace_api_data_mount_specification_dto

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
