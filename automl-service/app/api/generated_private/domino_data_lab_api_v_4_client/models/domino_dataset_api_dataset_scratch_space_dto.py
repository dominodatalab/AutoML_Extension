from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_dataset_api_dataset_scratch_space_dto_promotion_warning_status import (
    DominoDatasetApiDatasetScratchSpaceDtoPromotionWarningStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoDatasetApiDatasetScratchSpaceDto")


@_attrs_define
class DominoDatasetApiDatasetScratchSpaceDto:
    """
    Attributes:
        user_id (str):
        project_id (str):
        last_updated_date_millis (int):
        scratch_space_size (int):
        is_partial_size (bool):
        id (str):
        promotion_warning_status (DominoDatasetApiDatasetScratchSpaceDtoPromotionWarningStatus):
        last_snapshot_date_millis (int | None | Unset):
        days_since_last_snapshot (int | None | Unset):
    """

    user_id: str
    project_id: str
    last_updated_date_millis: int
    scratch_space_size: int
    is_partial_size: bool
    id: str
    promotion_warning_status: DominoDatasetApiDatasetScratchSpaceDtoPromotionWarningStatus
    last_snapshot_date_millis: int | None | Unset = UNSET
    days_since_last_snapshot: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        project_id = self.project_id

        last_updated_date_millis = self.last_updated_date_millis

        scratch_space_size = self.scratch_space_size

        is_partial_size = self.is_partial_size

        id = self.id

        promotion_warning_status = self.promotion_warning_status.value

        last_snapshot_date_millis: int | None | Unset
        if isinstance(self.last_snapshot_date_millis, Unset):
            last_snapshot_date_millis = UNSET
        else:
            last_snapshot_date_millis = self.last_snapshot_date_millis

        days_since_last_snapshot: int | None | Unset
        if isinstance(self.days_since_last_snapshot, Unset):
            days_since_last_snapshot = UNSET
        else:
            days_since_last_snapshot = self.days_since_last_snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "projectId": project_id,
                "lastUpdatedDateMillis": last_updated_date_millis,
                "scratchSpaceSize": scratch_space_size,
                "isPartialSize": is_partial_size,
                "id": id,
                "promotionWarningStatus": promotion_warning_status,
            }
        )
        if last_snapshot_date_millis is not UNSET:
            field_dict["lastSnapshotDateMillis"] = last_snapshot_date_millis
        if days_since_last_snapshot is not UNSET:
            field_dict["daysSinceLastSnapshot"] = days_since_last_snapshot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        project_id = d.pop("projectId")

        last_updated_date_millis = d.pop("lastUpdatedDateMillis")

        scratch_space_size = d.pop("scratchSpaceSize")

        is_partial_size = d.pop("isPartialSize")

        id = d.pop("id")

        promotion_warning_status = DominoDatasetApiDatasetScratchSpaceDtoPromotionWarningStatus(
            d.pop("promotionWarningStatus")
        )

        def _parse_last_snapshot_date_millis(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_snapshot_date_millis = _parse_last_snapshot_date_millis(d.pop("lastSnapshotDateMillis", UNSET))

        def _parse_days_since_last_snapshot(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_since_last_snapshot = _parse_days_since_last_snapshot(d.pop("daysSinceLastSnapshot", UNSET))

        domino_dataset_api_dataset_scratch_space_dto = cls(
            user_id=user_id,
            project_id=project_id,
            last_updated_date_millis=last_updated_date_millis,
            scratch_space_size=scratch_space_size,
            is_partial_size=is_partial_size,
            id=id,
            promotion_warning_status=promotion_warning_status,
            last_snapshot_date_millis=last_snapshot_date_millis,
            days_since_last_snapshot=days_since_last_snapshot,
        )

        domino_dataset_api_dataset_scratch_space_dto.additional_properties = d
        return domino_dataset_api_dataset_scratch_space_dto

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
