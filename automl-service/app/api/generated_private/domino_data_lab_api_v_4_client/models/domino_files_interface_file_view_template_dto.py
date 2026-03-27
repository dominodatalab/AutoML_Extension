from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_files_interface_commit_summary_for_filepath import DominoFilesInterfaceCommitSummaryForFilepath


T = TypeVar("T", bound="DominoFilesInterfaceFileViewTemplateDto")


@_attrs_define
class DominoFilesInterfaceFileViewTemplateDto:
    """
    Attributes:
        commit_summary_for_filepath (DominoFilesInterfaceCommitSummaryForFilepath):
        external_data_volumes_enabled (bool):
        enable_read_write_datasets (bool):
        enable_spark_clusters (bool):
        enable_ray_clusters (bool):
        enable_dask_clusters (bool):
        can_start_run (bool):
        can_edit (bool):
    """

    commit_summary_for_filepath: DominoFilesInterfaceCommitSummaryForFilepath
    external_data_volumes_enabled: bool
    enable_read_write_datasets: bool
    enable_spark_clusters: bool
    enable_ray_clusters: bool
    enable_dask_clusters: bool
    can_start_run: bool
    can_edit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_summary_for_filepath = self.commit_summary_for_filepath.to_dict()

        external_data_volumes_enabled = self.external_data_volumes_enabled

        enable_read_write_datasets = self.enable_read_write_datasets

        enable_spark_clusters = self.enable_spark_clusters

        enable_ray_clusters = self.enable_ray_clusters

        enable_dask_clusters = self.enable_dask_clusters

        can_start_run = self.can_start_run

        can_edit = self.can_edit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitSummaryForFilepath": commit_summary_for_filepath,
                "externalDataVolumesEnabled": external_data_volumes_enabled,
                "enableReadWriteDatasets": enable_read_write_datasets,
                "enableSparkClusters": enable_spark_clusters,
                "enableRayClusters": enable_ray_clusters,
                "enableDaskClusters": enable_dask_clusters,
                "canStartRun": can_start_run,
                "canEdit": can_edit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_files_interface_commit_summary_for_filepath import (
            DominoFilesInterfaceCommitSummaryForFilepath,
        )

        d = dict(src_dict)
        commit_summary_for_filepath = DominoFilesInterfaceCommitSummaryForFilepath.from_dict(
            d.pop("commitSummaryForFilepath")
        )

        external_data_volumes_enabled = d.pop("externalDataVolumesEnabled")

        enable_read_write_datasets = d.pop("enableReadWriteDatasets")

        enable_spark_clusters = d.pop("enableSparkClusters")

        enable_ray_clusters = d.pop("enableRayClusters")

        enable_dask_clusters = d.pop("enableDaskClusters")

        can_start_run = d.pop("canStartRun")

        can_edit = d.pop("canEdit")

        domino_files_interface_file_view_template_dto = cls(
            commit_summary_for_filepath=commit_summary_for_filepath,
            external_data_volumes_enabled=external_data_volumes_enabled,
            enable_read_write_datasets=enable_read_write_datasets,
            enable_spark_clusters=enable_spark_clusters,
            enable_ray_clusters=enable_ray_clusters,
            enable_dask_clusters=enable_dask_clusters,
            can_start_run=can_start_run,
            can_edit=can_edit,
        )

        domino_files_interface_file_view_template_dto.additional_properties = d
        return domino_files_interface_file_view_template_dto

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
