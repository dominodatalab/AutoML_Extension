from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_api_collaborator_for_governance_approvers_role import (
    DominoProjectsApiCollaboratorForGovernanceApproversRole,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_common_user_person_dto import DominoCommonUserPersonDTO


T = TypeVar("T", bound="DominoProjectsApiCollaboratorForGovernanceApprovers")


@_attrs_define
class DominoProjectsApiCollaboratorForGovernanceApprovers:
    """
    Attributes:
        collaborator (DominoCommonUserPersonDTO):
        role (DominoProjectsApiCollaboratorForGovernanceApproversRole):
        is_organization (bool):
        associated_organization_id (None | str | Unset):
    """

    collaborator: DominoCommonUserPersonDTO
    role: DominoProjectsApiCollaboratorForGovernanceApproversRole
    is_organization: bool
    associated_organization_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborator = self.collaborator.to_dict()

        role = self.role.value

        is_organization = self.is_organization

        associated_organization_id: None | str | Unset
        if isinstance(self.associated_organization_id, Unset):
            associated_organization_id = UNSET
        else:
            associated_organization_id = self.associated_organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborator": collaborator,
                "role": role,
                "isOrganization": is_organization,
            }
        )
        if associated_organization_id is not UNSET:
            field_dict["associatedOrganizationId"] = associated_organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_common_user_person_dto import DominoCommonUserPersonDTO

        d = dict(src_dict)
        collaborator = DominoCommonUserPersonDTO.from_dict(d.pop("collaborator"))

        role = DominoProjectsApiCollaboratorForGovernanceApproversRole(d.pop("role"))

        is_organization = d.pop("isOrganization")

        def _parse_associated_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        associated_organization_id = _parse_associated_organization_id(d.pop("associatedOrganizationId", UNSET))

        domino_projects_api_collaborator_for_governance_approvers = cls(
            collaborator=collaborator,
            role=role,
            is_organization=is_organization,
            associated_organization_id=associated_organization_id,
        )

        domino_projects_api_collaborator_for_governance_approvers.additional_properties = d
        return domino_projects_api_collaborator_for_governance_approvers

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
