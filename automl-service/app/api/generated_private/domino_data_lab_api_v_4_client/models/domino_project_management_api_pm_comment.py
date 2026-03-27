from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_project_management_api_domino_entity import DominoProjectManagementApiDominoEntity
    from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId
    from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser


T = TypeVar("T", bound="DominoProjectManagementApiPmComment")


@_attrs_define
class DominoProjectManagementApiPmComment:
    """
    Attributes:
        id (DominoProjectManagementApiPmId):
        comment_body (str):
        created (int):
        updated_at (int):
        commenter (DominoProjectManagementApiPmUser | Unset):
        domino_entity (DominoProjectManagementApiDominoEntity | Unset):
    """

    id: DominoProjectManagementApiPmId
    comment_body: str
    created: int
    updated_at: int
    commenter: DominoProjectManagementApiPmUser | Unset = UNSET
    domino_entity: DominoProjectManagementApiDominoEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.to_dict()

        comment_body = self.comment_body

        created = self.created

        updated_at = self.updated_at

        commenter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commenter, Unset):
            commenter = self.commenter.to_dict()

        domino_entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domino_entity, Unset):
            domino_entity = self.domino_entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "commentBody": comment_body,
                "created": created,
                "updatedAt": updated_at,
            }
        )
        if commenter is not UNSET:
            field_dict["commenter"] = commenter
        if domino_entity is not UNSET:
            field_dict["dominoEntity"] = domino_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_project_management_api_domino_entity import DominoProjectManagementApiDominoEntity
        from ..models.domino_project_management_api_pm_id import DominoProjectManagementApiPmId
        from ..models.domino_project_management_api_pm_user import DominoProjectManagementApiPmUser

        d = dict(src_dict)
        id = DominoProjectManagementApiPmId.from_dict(d.pop("id"))

        comment_body = d.pop("commentBody")

        created = d.pop("created")

        updated_at = d.pop("updatedAt")

        _commenter = d.pop("commenter", UNSET)
        commenter: DominoProjectManagementApiPmUser | Unset
        if isinstance(_commenter, Unset):
            commenter = UNSET
        else:
            commenter = DominoProjectManagementApiPmUser.from_dict(_commenter)

        _domino_entity = d.pop("dominoEntity", UNSET)
        domino_entity: DominoProjectManagementApiDominoEntity | Unset
        if isinstance(_domino_entity, Unset):
            domino_entity = UNSET
        else:
            domino_entity = DominoProjectManagementApiDominoEntity.from_dict(_domino_entity)

        domino_project_management_api_pm_comment = cls(
            id=id,
            comment_body=comment_body,
            created=created,
            updated_at=updated_at,
            commenter=commenter,
            domino_entity=domino_entity,
        )

        domino_project_management_api_pm_comment.additional_properties = d
        return domino_project_management_api_pm_comment

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
