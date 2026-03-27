from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner


T = TypeVar("T", bound="DominoEnvironmentsApiEnvironmentOverview")


@_attrs_define
class DominoEnvironmentsApiEnvironmentOverview:
    """
    Attributes:
        id (str):
        name (str):
        assign_latest_revision_as_active (bool):
        is_accessible (bool):
        children_following_active (int):
        owner (DominoEnvironmentsApiEnvironmentOwner | Unset):
    """

    id: str
    name: str
    assign_latest_revision_as_active: bool
    is_accessible: bool
    children_following_active: int
    owner: DominoEnvironmentsApiEnvironmentOwner | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        assign_latest_revision_as_active = self.assign_latest_revision_as_active

        is_accessible = self.is_accessible

        children_following_active = self.children_following_active

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "assignLatestRevisionAsActive": assign_latest_revision_as_active,
                "isAccessible": is_accessible,
                "childrenFollowingActive": children_following_active,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_environments_api_environment_owner import DominoEnvironmentsApiEnvironmentOwner

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        assign_latest_revision_as_active = d.pop("assignLatestRevisionAsActive")

        is_accessible = d.pop("isAccessible")

        children_following_active = d.pop("childrenFollowingActive")

        _owner = d.pop("owner", UNSET)
        owner: DominoEnvironmentsApiEnvironmentOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = DominoEnvironmentsApiEnvironmentOwner.from_dict(_owner)

        domino_environments_api_environment_overview = cls(
            id=id,
            name=name,
            assign_latest_revision_as_active=assign_latest_revision_as_active,
            is_accessible=is_accessible,
            children_following_active=children_following_active,
            owner=owner,
        )

        domino_environments_api_environment_overview.additional_properties = d
        return domino_environments_api_environment_overview

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
