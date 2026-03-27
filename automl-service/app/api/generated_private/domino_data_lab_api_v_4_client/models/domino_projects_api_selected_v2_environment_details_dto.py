from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiSelectedV2EnvironmentDetailsDTO")


@_attrs_define
class DominoProjectsApiSelectedV2EnvironmentDetailsDTO:
    """
    Attributes:
        latest_revision_url (str):
        latest_revision (int | None | Unset):
        latest_revision_status (None | str | Unset):
        selected_revision (int | None | Unset):
        selected_revision_id (None | str | Unset):
        selected_revision_url (None | str | Unset):
        restricted_revision_number (int | None | Unset):
        restricted_revision_id (None | str | Unset):
    """

    latest_revision_url: str
    latest_revision: int | None | Unset = UNSET
    latest_revision_status: None | str | Unset = UNSET
    selected_revision: int | None | Unset = UNSET
    selected_revision_id: None | str | Unset = UNSET
    selected_revision_url: None | str | Unset = UNSET
    restricted_revision_number: int | None | Unset = UNSET
    restricted_revision_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_revision_url = self.latest_revision_url

        latest_revision: int | None | Unset
        if isinstance(self.latest_revision, Unset):
            latest_revision = UNSET
        else:
            latest_revision = self.latest_revision

        latest_revision_status: None | str | Unset
        if isinstance(self.latest_revision_status, Unset):
            latest_revision_status = UNSET
        else:
            latest_revision_status = self.latest_revision_status

        selected_revision: int | None | Unset
        if isinstance(self.selected_revision, Unset):
            selected_revision = UNSET
        else:
            selected_revision = self.selected_revision

        selected_revision_id: None | str | Unset
        if isinstance(self.selected_revision_id, Unset):
            selected_revision_id = UNSET
        else:
            selected_revision_id = self.selected_revision_id

        selected_revision_url: None | str | Unset
        if isinstance(self.selected_revision_url, Unset):
            selected_revision_url = UNSET
        else:
            selected_revision_url = self.selected_revision_url

        restricted_revision_number: int | None | Unset
        if isinstance(self.restricted_revision_number, Unset):
            restricted_revision_number = UNSET
        else:
            restricted_revision_number = self.restricted_revision_number

        restricted_revision_id: None | str | Unset
        if isinstance(self.restricted_revision_id, Unset):
            restricted_revision_id = UNSET
        else:
            restricted_revision_id = self.restricted_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latestRevisionUrl": latest_revision_url,
            }
        )
        if latest_revision is not UNSET:
            field_dict["latestRevision"] = latest_revision
        if latest_revision_status is not UNSET:
            field_dict["latestRevisionStatus"] = latest_revision_status
        if selected_revision is not UNSET:
            field_dict["selectedRevision"] = selected_revision
        if selected_revision_id is not UNSET:
            field_dict["selectedRevisionId"] = selected_revision_id
        if selected_revision_url is not UNSET:
            field_dict["selectedRevisionUrl"] = selected_revision_url
        if restricted_revision_number is not UNSET:
            field_dict["restrictedRevisionNumber"] = restricted_revision_number
        if restricted_revision_id is not UNSET:
            field_dict["restrictedRevisionId"] = restricted_revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latest_revision_url = d.pop("latestRevisionUrl")

        def _parse_latest_revision(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_revision = _parse_latest_revision(d.pop("latestRevision", UNSET))

        def _parse_latest_revision_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_revision_status = _parse_latest_revision_status(d.pop("latestRevisionStatus", UNSET))

        def _parse_selected_revision(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        selected_revision = _parse_selected_revision(d.pop("selectedRevision", UNSET))

        def _parse_selected_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_revision_id = _parse_selected_revision_id(d.pop("selectedRevisionId", UNSET))

        def _parse_selected_revision_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_revision_url = _parse_selected_revision_url(d.pop("selectedRevisionUrl", UNSET))

        def _parse_restricted_revision_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        restricted_revision_number = _parse_restricted_revision_number(d.pop("restrictedRevisionNumber", UNSET))

        def _parse_restricted_revision_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        restricted_revision_id = _parse_restricted_revision_id(d.pop("restrictedRevisionId", UNSET))

        domino_projects_api_selected_v2_environment_details_dto = cls(
            latest_revision_url=latest_revision_url,
            latest_revision=latest_revision,
            latest_revision_status=latest_revision_status,
            selected_revision=selected_revision,
            selected_revision_id=selected_revision_id,
            selected_revision_url=selected_revision_url,
            restricted_revision_number=restricted_revision_number,
            restricted_revision_id=restricted_revision_id,
        )

        domino_projects_api_selected_v2_environment_details_dto.additional_properties = d
        return domino_projects_api_selected_v2_environment_details_dto

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
