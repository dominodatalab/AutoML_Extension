from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_environments_api_base_revision import DominoEnvironmentsApiBaseRevision


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentBaseDrift")


@_attrs_define
class DominoEnvironmentsApiEnvironmentBaseDrift:
    """
    Attributes:
        is_outdated (bool):
        base_of_active_revision (DominoEnvironmentsApiBaseRevision):
        active_revision_of_base_environment (DominoEnvironmentsApiBaseRevision):
    """

    is_outdated: bool
    base_of_active_revision: DominoEnvironmentsApiBaseRevision
    active_revision_of_base_environment: DominoEnvironmentsApiBaseRevision
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_outdated = self.is_outdated

        base_of_active_revision = self.base_of_active_revision.to_dict()

        active_revision_of_base_environment = self.active_revision_of_base_environment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isOutdated": is_outdated,
                "baseOfActiveRevision": base_of_active_revision,
                "activeRevisionOfBaseEnvironment": active_revision_of_base_environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_base_revision import DominoEnvironmentsApiBaseRevision

        d = dict(src_dict)
        is_outdated = d.pop("isOutdated")

        base_of_active_revision = DominoEnvironmentsApiBaseRevision.from_dict(d.pop("baseOfActiveRevision"))

        active_revision_of_base_environment = DominoEnvironmentsApiBaseRevision.from_dict(
            d.pop("activeRevisionOfBaseEnvironment")
        )

        domino_environments_api_environment_base_drift = cls(
            is_outdated=is_outdated,
            base_of_active_revision=base_of_active_revision,
            active_revision_of_base_environment=active_revision_of_base_environment,
        )

        domino_environments_api_environment_base_drift.additional_properties = d
        return domino_environments_api_environment_base_drift

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
