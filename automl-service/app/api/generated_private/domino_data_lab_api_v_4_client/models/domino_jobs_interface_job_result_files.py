from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_result_file_metadata import DominoJobsInterfaceResultFileMetadata


T = TypeVar("T", bound="DominoJobsInterfaceJobResultFiles")


@_attrs_define
class DominoJobsInterfaceJobResultFiles:
    """
    Attributes:
        commit_id (str):
        file_metadata (list[DominoJobsInterfaceResultFileMetadata]):
    """

    commit_id: str
    file_metadata: list[DominoJobsInterfaceResultFileMetadata]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_id = self.commit_id

        file_metadata = []
        for file_metadata_item_data in self.file_metadata:
            file_metadata_item = file_metadata_item_data.to_dict()
            file_metadata.append(file_metadata_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitId": commit_id,
                "fileMetadata": file_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_result_file_metadata import DominoJobsInterfaceResultFileMetadata

        d = dict(src_dict)
        commit_id = d.pop("commitId")

        file_metadata = []
        _file_metadata = d.pop("fileMetadata")
        for file_metadata_item_data in _file_metadata:
            file_metadata_item = DominoJobsInterfaceResultFileMetadata.from_dict(file_metadata_item_data)

            file_metadata.append(file_metadata_item)

        domino_jobs_interface_job_result_files = cls(
            commit_id=commit_id,
            file_metadata=file_metadata,
        )

        domino_jobs_interface_job_result_files.additional_properties = d
        return domino_jobs_interface_job_result_files

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
