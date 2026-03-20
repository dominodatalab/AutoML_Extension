from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_file_context_mount_config import DatasetFileContextMountConfig
    from ..models.project_sidebar_mount_config import ProjectSidebarMountConfig
    from ..models.top_bar_mount_config import TopBarMountConfig


T = TypeVar("T", bound="UIMountPointTypeConfigs")


@_attrs_define
class UIMountPointTypeConfigs:
    """The configuration for the UI mount points of the Extension. Each property corresponds to a different mount point in
    the Domino UI where the Extension can be mounted.

        Attributes:
            dataset_file_context (DatasetFileContextMountConfig | Unset):
            project_sidebar (ProjectSidebarMountConfig | Unset):
            top_bar (TopBarMountConfig | Unset):
    """

    dataset_file_context: DatasetFileContextMountConfig | Unset = UNSET
    project_sidebar: ProjectSidebarMountConfig | Unset = UNSET
    top_bar: TopBarMountConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_file_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dataset_file_context, Unset):
            dataset_file_context = self.dataset_file_context.to_dict()

        project_sidebar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_sidebar, Unset):
            project_sidebar = self.project_sidebar.to_dict()

        top_bar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_bar, Unset):
            top_bar = self.top_bar.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_file_context is not UNSET:
            field_dict["datasetFileContext"] = dataset_file_context
        if project_sidebar is not UNSET:
            field_dict["projectSidebar"] = project_sidebar
        if top_bar is not UNSET:
            field_dict["topBar"] = top_bar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_file_context_mount_config import DatasetFileContextMountConfig
        from ..models.project_sidebar_mount_config import ProjectSidebarMountConfig
        from ..models.top_bar_mount_config import TopBarMountConfig

        d = dict(src_dict)
        _dataset_file_context = d.pop("datasetFileContext", UNSET)
        dataset_file_context: DatasetFileContextMountConfig | Unset
        if isinstance(_dataset_file_context, Unset):
            dataset_file_context = UNSET
        else:
            dataset_file_context = DatasetFileContextMountConfig.from_dict(_dataset_file_context)

        _project_sidebar = d.pop("projectSidebar", UNSET)
        project_sidebar: ProjectSidebarMountConfig | Unset
        if isinstance(_project_sidebar, Unset):
            project_sidebar = UNSET
        else:
            project_sidebar = ProjectSidebarMountConfig.from_dict(_project_sidebar)

        _top_bar = d.pop("topBar", UNSET)
        top_bar: TopBarMountConfig | Unset
        if isinstance(_top_bar, Unset):
            top_bar = UNSET
        else:
            top_bar = TopBarMountConfig.from_dict(_top_bar)

        ui_mount_point_type_configs = cls(
            dataset_file_context=dataset_file_context,
            project_sidebar=project_sidebar,
            top_bar=top_bar,
        )

        ui_mount_point_type_configs.additional_properties = d
        return ui_mount_point_type_configs

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
