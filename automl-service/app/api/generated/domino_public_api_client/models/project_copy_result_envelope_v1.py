from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_not_copied_v1 import DatasetNotCopiedV1
    from ..models.metadata_v1 import MetadataV1
    from ..models.net_app_volume_not_copied_v1 import NetAppVolumeNotCopiedV1
    from ..models.project_v1 import ProjectV1


T = TypeVar("T", bound="ProjectCopyResultEnvelopeV1")


@_attrs_define
class ProjectCopyResultEnvelopeV1:
    """
    Attributes:
        metadata (MetadataV1):
        project (ProjectV1):
        datasets_not_copied (list[DatasetNotCopiedV1] | Unset):
        net_app_volumes_not_copied (list[NetAppVolumeNotCopiedV1] | Unset):
    """

    metadata: MetadataV1
    project: ProjectV1
    datasets_not_copied: list[DatasetNotCopiedV1] | Unset = UNSET
    net_app_volumes_not_copied: list[NetAppVolumeNotCopiedV1] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata.to_dict()

        project = self.project.to_dict()

        datasets_not_copied: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.datasets_not_copied, Unset):
            datasets_not_copied = []
            for datasets_not_copied_item_data in self.datasets_not_copied:
                datasets_not_copied_item = datasets_not_copied_item_data.to_dict()
                datasets_not_copied.append(datasets_not_copied_item)

        net_app_volumes_not_copied: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.net_app_volumes_not_copied, Unset):
            net_app_volumes_not_copied = []
            for net_app_volumes_not_copied_item_data in self.net_app_volumes_not_copied:
                net_app_volumes_not_copied_item = net_app_volumes_not_copied_item_data.to_dict()
                net_app_volumes_not_copied.append(net_app_volumes_not_copied_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadata": metadata,
                "project": project,
            }
        )
        if datasets_not_copied is not UNSET:
            field_dict["datasetsNotCopied"] = datasets_not_copied
        if net_app_volumes_not_copied is not UNSET:
            field_dict["netAppVolumesNotCopied"] = net_app_volumes_not_copied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_not_copied_v1 import DatasetNotCopiedV1
        from ..models.metadata_v1 import MetadataV1
        from ..models.net_app_volume_not_copied_v1 import NetAppVolumeNotCopiedV1
        from ..models.project_v1 import ProjectV1

        d = dict(src_dict)
        metadata = MetadataV1.from_dict(d.pop("metadata"))

        project = ProjectV1.from_dict(d.pop("project"))

        _datasets_not_copied = d.pop("datasetsNotCopied", UNSET)
        datasets_not_copied: list[DatasetNotCopiedV1] | Unset = UNSET
        if _datasets_not_copied is not UNSET:
            datasets_not_copied = []
            for datasets_not_copied_item_data in _datasets_not_copied:
                datasets_not_copied_item = DatasetNotCopiedV1.from_dict(datasets_not_copied_item_data)

                datasets_not_copied.append(datasets_not_copied_item)

        _net_app_volumes_not_copied = d.pop("netAppVolumesNotCopied", UNSET)
        net_app_volumes_not_copied: list[NetAppVolumeNotCopiedV1] | Unset = UNSET
        if _net_app_volumes_not_copied is not UNSET:
            net_app_volumes_not_copied = []
            for net_app_volumes_not_copied_item_data in _net_app_volumes_not_copied:
                net_app_volumes_not_copied_item = NetAppVolumeNotCopiedV1.from_dict(
                    net_app_volumes_not_copied_item_data
                )

                net_app_volumes_not_copied.append(net_app_volumes_not_copied_item)

        project_copy_result_envelope_v1 = cls(
            metadata=metadata,
            project=project,
            datasets_not_copied=datasets_not_copied,
            net_app_volumes_not_copied=net_app_volumes_not_copied,
        )

        project_copy_result_envelope_v1.additional_properties = d
        return project_copy_result_envelope_v1

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
