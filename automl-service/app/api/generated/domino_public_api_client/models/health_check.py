from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheck")


@_attrs_define
class HealthCheck:
    """
    Attributes:
        status (str):
        version (str):
        commit (str | Unset):
        kubecost_status (str | Unset):
    """

    status: str
    version: str
    commit: str | Unset = UNSET
    kubecost_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        version = self.version

        commit = self.commit

        kubecost_status = self.kubecost_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "version": version,
            }
        )
        if commit is not UNSET:
            field_dict["commit"] = commit
        if kubecost_status is not UNSET:
            field_dict["kubecostStatus"] = kubecost_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        version = d.pop("version")

        commit = d.pop("commit", UNSET)

        kubecost_status = d.pop("kubecostStatus", UNSET)

        health_check = cls(
            status=status,
            version=version,
            commit=commit,
            kubecost_status=kubecost_status,
        )

        health_check.additional_properties = d
        return health_check

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
