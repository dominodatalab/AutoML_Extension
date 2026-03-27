from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_supported_action_details_kind import DominoProjectsApiSupportedActionDetailsKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DominoProjectsApiSupportedActionDetails")


@_attrs_define
class DominoProjectsApiSupportedActionDetails:
    """
    Attributes:
        kind (DominoProjectsApiSupportedActionDetailsKind):
        authorized (bool):
        supported (bool | None | Unset):
        reason (None | str | Unset):
    """

    kind: DominoProjectsApiSupportedActionDetailsKind
    authorized: bool
    supported: bool | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        authorized = self.authorized

        supported: bool | None | Unset
        if isinstance(self.supported, Unset):
            supported = UNSET
        else:
            supported = self.supported

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "authorized": authorized,
            }
        )
        if supported is not UNSET:
            field_dict["supported"] = supported
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = DominoProjectsApiSupportedActionDetailsKind(d.pop("kind"))

        authorized = d.pop("authorized")

        def _parse_supported(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supported = _parse_supported(d.pop("supported", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        domino_projects_api_supported_action_details = cls(
            kind=kind,
            authorized=authorized,
            supported=supported,
            reason=reason,
        )

        domino_projects_api_supported_action_details.additional_properties = d
        return domino_projects_api_supported_action_details

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
