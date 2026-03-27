from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_workspace_api_workspace_quota_status_dto_status import (
    DominoWorkspaceApiWorkspaceQuotaStatusDtoStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoWorkspaceApiWorkspaceQuotaStatusDto")


@_attrs_define
class DominoWorkspaceApiWorkspaceQuotaStatusDto:
    """
    Attributes:
        status (DominoWorkspaceApiWorkspaceQuotaStatusDtoStatus):
        current_value (int | None | Unset):
        limit (int | None | Unset):
    """

    status: DominoWorkspaceApiWorkspaceQuotaStatusDtoStatus
    current_value: int | None | Unset = UNSET
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        current_value: int | None | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = DominoWorkspaceApiWorkspaceQuotaStatusDtoStatus(d.pop("status"))

        def _parse_current_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_value = _parse_current_value(d.pop("currentValue", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        domino_workspace_api_workspace_quota_status_dto = cls(
            status=status,
            current_value=current_value,
            limit=limit,
        )

        domino_workspace_api_workspace_quota_status_dto.additional_properties = d
        return domino_workspace_api_workspace_quota_status_dto

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
