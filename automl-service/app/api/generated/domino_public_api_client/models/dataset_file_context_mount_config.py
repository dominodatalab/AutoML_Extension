from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_file_context_mount_point import DatasetFileContextMountPoint


T = TypeVar("T", bound="DatasetFileContextMountConfig")


@_attrs_define
class DatasetFileContextMountConfig:
    """
    Attributes:
        enabled (bool): If true, the Extension is mounted in the Dataset file context of the Domino UI.
        all_projects (bool | Unset): If true, the Extension will be mounted for all projects. If false, the extension
            will only be mounted for the projects specified in the projectIds field.
        file_types (list[str] | Unset): The file types that the Extension should be mounted for in the dataset file
            context.
        mount_points (list[DatasetFileContextMountPoint] | Unset):
    """

    enabled: bool
    all_projects: bool | Unset = UNSET
    file_types: list[str] | Unset = UNSET
    mount_points: list[DatasetFileContextMountPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        all_projects = self.all_projects

        file_types: list[str] | Unset = UNSET
        if not isinstance(self.file_types, Unset):
            file_types = self.file_types

        mount_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mount_points, Unset):
            mount_points = []
            for mount_points_item_data in self.mount_points:
                mount_points_item = mount_points_item_data.to_dict()
                mount_points.append(mount_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if all_projects is not UNSET:
            field_dict["allProjects"] = all_projects
        if file_types is not UNSET:
            field_dict["fileTypes"] = file_types
        if mount_points is not UNSET:
            field_dict["mountPoints"] = mount_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_file_context_mount_point import DatasetFileContextMountPoint

        d = dict(src_dict)
        enabled = d.pop("enabled")

        all_projects = d.pop("allProjects", UNSET)

        file_types = cast(list[str], d.pop("fileTypes", UNSET))

        _mount_points = d.pop("mountPoints", UNSET)
        mount_points: list[DatasetFileContextMountPoint] | Unset = UNSET
        if _mount_points is not UNSET:
            mount_points = []
            for mount_points_item_data in _mount_points:
                mount_points_item = DatasetFileContextMountPoint.from_dict(mount_points_item_data)

                mount_points.append(mount_points_item)

        dataset_file_context_mount_config = cls(
            enabled=enabled,
            all_projects=all_projects,
            file_types=file_types,
            mount_points=mount_points,
        )

        dataset_file_context_mount_config.additional_properties = d
        return dataset_file_context_mount_config

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
