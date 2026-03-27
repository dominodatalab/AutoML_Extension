from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoDatasetrwApiDatasetRwProjectDetailsDto")


@_attrs_define
class DominoDatasetrwApiDatasetRwProjectDetailsDto:
    """
    Attributes:
        source_project_name (str):
        source_project_id (str):
        source_project_owner_username (str):
        shared_project_names (list[str]):
        shared_project_ids (list[str]):
        shared_project_owner_usernames (list[str]):
    """

    source_project_name: str
    source_project_id: str
    source_project_owner_username: str
    shared_project_names: list[str]
    shared_project_ids: list[str]
    shared_project_owner_usernames: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_project_name = self.source_project_name

        source_project_id = self.source_project_id

        source_project_owner_username = self.source_project_owner_username

        shared_project_names = self.shared_project_names

        shared_project_ids = self.shared_project_ids

        shared_project_owner_usernames = self.shared_project_owner_usernames

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceProjectName": source_project_name,
                "sourceProjectId": source_project_id,
                "sourceProjectOwnerUsername": source_project_owner_username,
                "sharedProjectNames": shared_project_names,
                "sharedProjectIds": shared_project_ids,
                "sharedProjectOwnerUsernames": shared_project_owner_usernames,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_project_name = d.pop("sourceProjectName")

        source_project_id = d.pop("sourceProjectId")

        source_project_owner_username = d.pop("sourceProjectOwnerUsername")

        shared_project_names = cast(list[str], d.pop("sharedProjectNames"))

        shared_project_ids = cast(list[str], d.pop("sharedProjectIds"))

        shared_project_owner_usernames = cast(list[str], d.pop("sharedProjectOwnerUsernames"))

        domino_datasetrw_api_dataset_rw_project_details_dto = cls(
            source_project_name=source_project_name,
            source_project_id=source_project_id,
            source_project_owner_username=source_project_owner_username,
            shared_project_names=shared_project_names,
            shared_project_ids=shared_project_ids,
            shared_project_owner_usernames=shared_project_owner_usernames,
        )

        domino_datasetrw_api_dataset_rw_project_details_dto.additional_properties = d
        return domino_datasetrw_api_dataset_rw_project_details_dto

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
