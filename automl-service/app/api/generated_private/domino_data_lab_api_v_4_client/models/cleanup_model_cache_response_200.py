from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CleanupModelCacheResponse200")


@_attrs_define
class CleanupModelCacheResponse200:
    """
    Attributes:
        success_count (int | Unset):
        failure_count (int | Unset):
        skipped_count (int | Unset):
        deleted_paths (list[str] | Unset):
        dry_run (bool | Unset):
    """

    success_count: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    skipped_count: int | Unset = UNSET
    deleted_paths: list[str] | Unset = UNSET
    dry_run: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_count = self.success_count

        failure_count = self.failure_count

        skipped_count = self.skipped_count

        deleted_paths: list[str] | Unset = UNSET
        if not isinstance(self.deleted_paths, Unset):
            deleted_paths = self.deleted_paths

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_count is not UNSET:
            field_dict["successCount"] = success_count
        if failure_count is not UNSET:
            field_dict["failureCount"] = failure_count
        if skipped_count is not UNSET:
            field_dict["skippedCount"] = skipped_count
        if deleted_paths is not UNSET:
            field_dict["deletedPaths"] = deleted_paths
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success_count = d.pop("successCount", UNSET)

        failure_count = d.pop("failureCount", UNSET)

        skipped_count = d.pop("skippedCount", UNSET)

        deleted_paths = cast(list[str], d.pop("deletedPaths", UNSET))

        dry_run = d.pop("dryRun", UNSET)

        cleanup_model_cache_response_200 = cls(
            success_count=success_count,
            failure_count=failure_count,
            skipped_count=skipped_count,
            deleted_paths=deleted_paths,
            dry_run=dry_run,
        )

        cleanup_model_cache_response_200.additional_properties = d
        return cleanup_model_cache_response_200

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
