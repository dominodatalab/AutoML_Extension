from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment import DominoEnvironmentsApiEnvironment
    from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
    from ..models.domino_environments_api_visible_environments import DominoEnvironmentsApiVisibleEnvironments


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentRevisionDetails")


@_attrs_define
class DominoEnvironmentsApiEnvironmentRevisionDetails:
    """
    Attributes:
        environment (DominoEnvironmentsApiEnvironment):
        environment_revision (DominoEnvironmentsApiEnvironmentRevision):
        is_latest_revision (bool):
        visible_environments (DominoEnvironmentsApiVisibleEnvironments):
        can_revert_to (bool):
        has_running_build (bool):
        base (DominoEnvironmentsApiEnvironmentRevision | Unset):
    """

    environment: DominoEnvironmentsApiEnvironment
    environment_revision: DominoEnvironmentsApiEnvironmentRevision
    is_latest_revision: bool
    visible_environments: DominoEnvironmentsApiVisibleEnvironments
    can_revert_to: bool
    has_running_build: bool
    base: DominoEnvironmentsApiEnvironmentRevision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment = self.environment.to_dict()

        environment_revision = self.environment_revision.to_dict()

        is_latest_revision = self.is_latest_revision

        visible_environments = self.visible_environments.to_dict()

        can_revert_to = self.can_revert_to

        has_running_build = self.has_running_build

        base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base, Unset):
            base = self.base.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environment": environment,
                "environmentRevision": environment_revision,
                "isLatestRevision": is_latest_revision,
                "visibleEnvironments": visible_environments,
                "canRevertTo": can_revert_to,
                "hasRunningBuild": has_running_build,
            }
        )
        if base is not UNSET:
            field_dict["base"] = base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment import DominoEnvironmentsApiEnvironment
        from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
        from ..models.domino_environments_api_visible_environments import DominoEnvironmentsApiVisibleEnvironments

        d = dict(src_dict)
        environment = DominoEnvironmentsApiEnvironment.from_dict(d.pop("environment"))

        environment_revision = DominoEnvironmentsApiEnvironmentRevision.from_dict(d.pop("environmentRevision"))

        is_latest_revision = d.pop("isLatestRevision")

        visible_environments = DominoEnvironmentsApiVisibleEnvironments.from_dict(d.pop("visibleEnvironments"))

        can_revert_to = d.pop("canRevertTo")

        has_running_build = d.pop("hasRunningBuild")

        _base = d.pop("base", UNSET)
        base: DominoEnvironmentsApiEnvironmentRevision | Unset
        if isinstance(_base, Unset):
            base = UNSET
        else:
            base = DominoEnvironmentsApiEnvironmentRevision.from_dict(_base)

        domino_environments_api_environment_revision_details = cls(
            environment=environment,
            environment_revision=environment_revision,
            is_latest_revision=is_latest_revision,
            visible_environments=visible_environments,
            can_revert_to=can_revert_to,
            has_running_build=has_running_build,
            base=base,
        )

        domino_environments_api_environment_revision_details.additional_properties = d
        return domino_environments_api_environment_revision_details

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
