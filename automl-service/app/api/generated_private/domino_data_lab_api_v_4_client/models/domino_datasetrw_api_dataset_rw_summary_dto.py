from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_datasetrw_api_dataset_rw_summary_dto_lifecycle_status import (
    DominoDatasetrwApiDatasetRwSummaryDtoLifecycleStatus,
)
from ..models.domino_datasetrw_api_dataset_rw_summary_dto_size_status import (
    DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_datasetrw_api_dataset_rw_project_details_dto import (
        DominoDatasetrwApiDatasetRwProjectDetailsDto,
    )


T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwSummaryDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwSummaryDto:
    """
    Attributes:
        id (str):
        name (str):
        projects (DominoDatasetrwApiDatasetRwProjectDetailsDto):
        lifecycle_status (DominoDatasetrwApiDatasetRwSummaryDtoLifecycleStatus):
        unique_name (None | str | Unset):
        description (None | str | Unset):
        owner_username (None | str | Unset):
        size_in_bytes (int | None | Unset):
        owner_usernames (list[str] | None | Unset):
        size_status (DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus | Unset):
        storage_name (None | str | Unset):
    """

    id: str
    name: str
    projects: DominoDatasetrwApiDatasetRwProjectDetailsDto
    lifecycle_status: DominoDatasetrwApiDatasetRwSummaryDtoLifecycleStatus
    unique_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    owner_username: None | str | Unset = UNSET
    size_in_bytes: int | None | Unset = UNSET
    owner_usernames: list[str] | None | Unset = UNSET
    size_status: DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus | Unset = UNSET
    storage_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        projects = self.projects.to_dict()

        lifecycle_status = self.lifecycle_status.value

        unique_name: None | str | Unset
        if isinstance(self.unique_name, Unset):
            unique_name = UNSET
        else:
            unique_name = self.unique_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        owner_username: None | str | Unset
        if isinstance(self.owner_username, Unset):
            owner_username = UNSET
        else:
            owner_username = self.owner_username

        size_in_bytes: int | None | Unset
        if isinstance(self.size_in_bytes, Unset):
            size_in_bytes = UNSET
        else:
            size_in_bytes = self.size_in_bytes

        owner_usernames: list[str] | None | Unset
        if isinstance(self.owner_usernames, Unset):
            owner_usernames = UNSET
        elif isinstance(self.owner_usernames, list):
            owner_usernames = self.owner_usernames

        else:
            owner_usernames = self.owner_usernames

        size_status: str | Unset = UNSET
        if not isinstance(self.size_status, Unset):
            size_status = self.size_status.value

        storage_name: None | str | Unset
        if isinstance(self.storage_name, Unset):
            storage_name = UNSET
        else:
            storage_name = self.storage_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "projects": projects,
                "lifecycleStatus": lifecycle_status,
            }
        )
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name
        if description is not UNSET:
            field_dict["description"] = description
        if owner_username is not UNSET:
            field_dict["ownerUsername"] = owner_username
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes
        if owner_usernames is not UNSET:
            field_dict["ownerUsernames"] = owner_usernames
        if size_status is not UNSET:
            field_dict["sizeStatus"] = size_status
        if storage_name is not UNSET:
            field_dict["storageName"] = storage_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_datasetrw_api_dataset_rw_project_details_dto import (
            DominoDatasetrwApiDatasetRwProjectDetailsDto,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        projects = DominoDatasetrwApiDatasetRwProjectDetailsDto.from_dict(d.pop("projects"))

        lifecycle_status = DominoDatasetrwApiDatasetRwSummaryDtoLifecycleStatus(d.pop("lifecycleStatus"))

        def _parse_unique_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_name = _parse_unique_name(d.pop("uniqueName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_owner_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_username = _parse_owner_username(d.pop("ownerUsername", UNSET))

        def _parse_size_in_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_in_bytes = _parse_size_in_bytes(d.pop("sizeInBytes", UNSET))

        def _parse_owner_usernames(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_usernames_type_0 = cast(list[str], data)

                return owner_usernames_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        owner_usernames = _parse_owner_usernames(d.pop("ownerUsernames", UNSET))

        _size_status = d.pop("sizeStatus", UNSET)
        size_status: DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus | Unset
        if isinstance(_size_status, Unset):
            size_status = UNSET
        else:
            size_status = DominoDatasetrwApiDatasetRwSummaryDtoSizeStatus(_size_status)

        def _parse_storage_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_name = _parse_storage_name(d.pop("storageName", UNSET))

        domino_datasetrw_api_dataset_rw_summary_dto = cls(
            id=id,
            name=name,
            projects=projects,
            lifecycle_status=lifecycle_status,
            unique_name=unique_name,
            description=description,
            owner_username=owner_username,
            size_in_bytes=size_in_bytes,
            owner_usernames=owner_usernames,
            size_status=size_status,
            storage_name=storage_name,
        )

        domino_datasetrw_api_dataset_rw_summary_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_summary_dto

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
