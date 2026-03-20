from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_v1 import JobV1
    from ..models.paginated_metadata_v1 import PaginatedMetadataV1


T = TypeVar("T", bound="PaginatedJobEnvelopeV1")


@_attrs_define
class PaginatedJobEnvelopeV1:
    """
    Attributes:
        jobs (list[JobV1]):
        metadata (PaginatedMetadataV1):
    """

    jobs: list[JobV1]
    metadata: PaginatedMetadataV1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()
            jobs.append(jobs_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_v1 import JobV1
        from ..models.paginated_metadata_v1 import PaginatedMetadataV1

        d = dict(src_dict)
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = JobV1.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        metadata = PaginatedMetadataV1.from_dict(d.pop("metadata"))

        paginated_job_envelope_v1 = cls(
            jobs=jobs,
            metadata=metadata,
        )

        paginated_job_envelope_v1.additional_properties = d
        return paginated_job_envelope_v1

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
