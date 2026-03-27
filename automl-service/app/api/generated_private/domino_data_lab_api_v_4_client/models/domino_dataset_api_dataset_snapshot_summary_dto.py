from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_dataset_api_dataset_snapshot_dto import DominoDatasetApiDatasetSnapshotDto


T = TypeVar("T", bound="DominoDatasetApiDatasetSnapshotSummaryDto")


@_attrs_define
class DominoDatasetApiDatasetSnapshotSummaryDto:
    """
    Attributes:
        snapshot (DominoDatasetApiDatasetSnapshotDto):
        dataset_description (None | str | Unset):
        run_url (None | str | Unset):
        author_username (None | str | Unset):
        origin_name (None | str | Unset):
    """

    snapshot: DominoDatasetApiDatasetSnapshotDto
    dataset_description: None | str | Unset = UNSET
    run_url: None | str | Unset = UNSET
    author_username: None | str | Unset = UNSET
    origin_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot = self.snapshot.to_dict()

        dataset_description: None | str | Unset
        if isinstance(self.dataset_description, Unset):
            dataset_description = UNSET
        else:
            dataset_description = self.dataset_description

        run_url: None | str | Unset
        if isinstance(self.run_url, Unset):
            run_url = UNSET
        else:
            run_url = self.run_url

        author_username: None | str | Unset
        if isinstance(self.author_username, Unset):
            author_username = UNSET
        else:
            author_username = self.author_username

        origin_name: None | str | Unset
        if isinstance(self.origin_name, Unset):
            origin_name = UNSET
        else:
            origin_name = self.origin_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot": snapshot,
            }
        )
        if dataset_description is not UNSET:
            field_dict["datasetDescription"] = dataset_description
        if run_url is not UNSET:
            field_dict["runUrl"] = run_url
        if author_username is not UNSET:
            field_dict["authorUsername"] = author_username
        if origin_name is not UNSET:
            field_dict["originName"] = origin_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_dataset_api_dataset_snapshot_dto import DominoDatasetApiDatasetSnapshotDto

        d = dict(src_dict)
        snapshot = DominoDatasetApiDatasetSnapshotDto.from_dict(d.pop("snapshot"))

        def _parse_dataset_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_description = _parse_dataset_description(d.pop("datasetDescription", UNSET))

        def _parse_run_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        run_url = _parse_run_url(d.pop("runUrl", UNSET))

        def _parse_author_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_username = _parse_author_username(d.pop("authorUsername", UNSET))

        def _parse_origin_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin_name = _parse_origin_name(d.pop("originName", UNSET))

        domino_dataset_api_dataset_snapshot_summary_dto = cls(
            snapshot=snapshot,
            dataset_description=dataset_description,
            run_url=run_url,
            author_username=author_username,
            origin_name=origin_name,
        )

        domino_dataset_api_dataset_snapshot_summary_dto.additional_properties = d
        return domino_dataset_api_dataset_snapshot_summary_dto

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
