from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.domino_jobs_interface_environment_revision_ref import DominoJobsInterfaceEnvironmentRevisionRef


T = TypeVar("T", bound="DominoJobsInterfaceEnvironmentWithRevisions")


@_attrs_define
class DominoJobsInterfaceEnvironmentWithRevisions:
    """
    Attributes:
        id (str):
        name (str):
        revisions (list[DominoJobsInterfaceEnvironmentRevisionRef]):
        is_default (bool):
        is_restricted (bool):
    """

    id: str
    name: str
    revisions: list[DominoJobsInterfaceEnvironmentRevisionRef]
    is_default: bool
    is_restricted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)

        is_default = self.is_default

        is_restricted = self.is_restricted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "revisions": revisions,
                "isDefault": is_default,
                "isRestricted": is_restricted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_jobs_interface_environment_revision_ref import DominoJobsInterfaceEnvironmentRevisionRef

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in _revisions:
            revisions_item = DominoJobsInterfaceEnvironmentRevisionRef.from_dict(revisions_item_data)

            revisions.append(revisions_item)

        is_default = d.pop("isDefault")

        is_restricted = d.pop("isRestricted")

        domino_jobs_interface_environment_with_revisions = cls(
            id=id,
            name=name,
            revisions=revisions,
            is_default=is_default,
            is_restricted=is_restricted,
        )

        domino_jobs_interface_environment_with_revisions.additional_properties = d
        return domino_jobs_interface_environment_with_revisions

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
