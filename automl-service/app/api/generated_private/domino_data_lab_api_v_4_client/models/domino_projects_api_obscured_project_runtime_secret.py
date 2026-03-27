from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_api_environment_runtime_secret import DominoProjectsApiApiEnvironmentRuntimeSecret


T = TypeVar("T", bound="DominoProjectsApiObscuredProjectRuntimeSecret")


@_attrs_define
class DominoProjectsApiObscuredProjectRuntimeSecret:
    """
    Attributes:
        runtime_secret (DominoProjectsApiApiEnvironmentRuntimeSecret):
        mount_path (None | str | Unset):
    """

    runtime_secret: DominoProjectsApiApiEnvironmentRuntimeSecret
    mount_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime_secret = self.runtime_secret.to_dict()

        mount_path: None | str | Unset
        if isinstance(self.mount_path, Unset):
            mount_path = UNSET
        else:
            mount_path = self.mount_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runtimeSecret": runtime_secret,
            }
        )
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_api_environment_runtime_secret import (
            DominoProjectsApiApiEnvironmentRuntimeSecret,
        )

        d = dict(src_dict)
        runtime_secret = DominoProjectsApiApiEnvironmentRuntimeSecret.from_dict(d.pop("runtimeSecret"))

        def _parse_mount_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mount_path = _parse_mount_path(d.pop("mountPath", UNSET))

        domino_projects_api_obscured_project_runtime_secret = cls(
            runtime_secret=runtime_secret,
            mount_path=mount_path,
        )

        domino_projects_api_obscured_project_runtime_secret.additional_properties = d
        return domino_projects_api_obscured_project_runtime_secret

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
