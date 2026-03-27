from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DominoQuotaWebCreateQuotaOverridesRequest")


@_attrs_define
class DominoQuotaWebCreateQuotaOverridesRequest:
    """
    Attributes:
        target_ids (list[str]):
        quota_limit (int): quota limit
    """

    target_ids: list[str]
    quota_limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_ids = self.target_ids

        quota_limit = self.quota_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetIds": target_ids,
                "quotaLimit": quota_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_ids = cast(list[str], d.pop("targetIds"))

        quota_limit = d.pop("quotaLimit")

        domino_quota_web_create_quota_overrides_request = cls(
            target_ids=target_ids,
            quota_limit=quota_limit,
        )

        domino_quota_web_create_quota_overrides_request.additional_properties = d
        return domino_quota_web_create_quota_overrides_request

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
