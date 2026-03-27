from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoGruzApiStopRequest")


@_attrs_define
class DominoGruzApiStopRequest:
    """
    Attributes:
        save_changes (bool):
        commit_message (None | str | Unset):
        save_datasets (bool | None | Unset):
        stopping_user_id (None | str | Unset):
    """

    save_changes: bool
    commit_message: None | str | Unset = UNSET
    save_datasets: bool | None | Unset = UNSET
    stopping_user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        save_changes = self.save_changes

        commit_message: None | str | Unset
        if isinstance(self.commit_message, Unset):
            commit_message = UNSET
        else:
            commit_message = self.commit_message

        save_datasets: bool | None | Unset
        if isinstance(self.save_datasets, Unset):
            save_datasets = UNSET
        else:
            save_datasets = self.save_datasets

        stopping_user_id: None | str | Unset
        if isinstance(self.stopping_user_id, Unset):
            stopping_user_id = UNSET
        else:
            stopping_user_id = self.stopping_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "saveChanges": save_changes,
            }
        )
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message
        if save_datasets is not UNSET:
            field_dict["saveDatasets"] = save_datasets
        if stopping_user_id is not UNSET:
            field_dict["stoppingUserId"] = stopping_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        save_changes = d.pop("saveChanges")

        def _parse_commit_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit_message = _parse_commit_message(d.pop("commitMessage", UNSET))

        def _parse_save_datasets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        save_datasets = _parse_save_datasets(d.pop("saveDatasets", UNSET))

        def _parse_stopping_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stopping_user_id = _parse_stopping_user_id(d.pop("stoppingUserId", UNSET))

        domino_gruz_api_stop_request = cls(
            save_changes=save_changes,
            commit_message=commit_message,
            save_datasets=save_datasets,
            stopping_user_id=stopping_user_id,
        )

        domino_gruz_api_stop_request.additional_properties = d
        return domino_gruz_api_stop_request

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
