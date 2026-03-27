from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment import DominoEnvironmentsApiEnvironment
    from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
    from ..models.domino_environments_api_environment_revision_summary import (
        DominoEnvironmentsApiEnvironmentRevisionSummary,
    )


T = TypeVar("T", bound="DominoEnvironmentsApiVisibleEnvironments")


@_attrs_define
class DominoEnvironmentsApiVisibleEnvironments:
    """
    Attributes:
        active_environment_revisions (list[DominoEnvironmentsApiEnvironmentRevisionSummary]):
        default_env (DominoEnvironmentsApiEnvironment):
        default_env_rev (DominoEnvironmentsApiEnvironmentRevision | Unset):
    """

    active_environment_revisions: list[DominoEnvironmentsApiEnvironmentRevisionSummary]
    default_env: DominoEnvironmentsApiEnvironment
    default_env_rev: DominoEnvironmentsApiEnvironmentRevision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_environment_revisions = []
        for active_environment_revisions_item_data in self.active_environment_revisions:
            active_environment_revisions_item = active_environment_revisions_item_data.to_dict()
            active_environment_revisions.append(active_environment_revisions_item)

        default_env = self.default_env.to_dict()

        default_env_rev: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_env_rev, Unset):
            default_env_rev = self.default_env_rev.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activeEnvironmentRevisions": active_environment_revisions,
                "defaultEnv": default_env,
            }
        )
        if default_env_rev is not UNSET:
            field_dict["defaultEnvRev"] = default_env_rev

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment import DominoEnvironmentsApiEnvironment
        from ..models.domino_environments_api_environment_revision import DominoEnvironmentsApiEnvironmentRevision
        from ..models.domino_environments_api_environment_revision_summary import (
            DominoEnvironmentsApiEnvironmentRevisionSummary,
        )

        d = dict(src_dict)
        active_environment_revisions = []
        _active_environment_revisions = d.pop("activeEnvironmentRevisions")
        for active_environment_revisions_item_data in _active_environment_revisions:
            active_environment_revisions_item = DominoEnvironmentsApiEnvironmentRevisionSummary.from_dict(
                active_environment_revisions_item_data
            )

            active_environment_revisions.append(active_environment_revisions_item)

        default_env = DominoEnvironmentsApiEnvironment.from_dict(d.pop("defaultEnv"))

        _default_env_rev = d.pop("defaultEnvRev", UNSET)
        default_env_rev: DominoEnvironmentsApiEnvironmentRevision | Unset
        if isinstance(_default_env_rev, Unset):
            default_env_rev = UNSET
        else:
            default_env_rev = DominoEnvironmentsApiEnvironmentRevision.from_dict(_default_env_rev)

        domino_environments_api_visible_environments = cls(
            active_environment_revisions=active_environment_revisions,
            default_env=default_env,
            default_env_rev=default_env_rev,
        )

        domino_environments_api_visible_environments.additional_properties = d
        return domino_environments_api_visible_environments

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
