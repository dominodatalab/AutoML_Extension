from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_project_models_fork_or_copy_project_visibility import (
    DominoNucleusProjectModelsForkOrCopyProjectVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
    from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
    from ..models.domino_projects_api_copy_git_request import DominoProjectsApiCopyGitRequest
    from ..models.domino_projects_api_new_tags_dto import DominoProjectsApiNewTagsDTO


T = TypeVar("T", bound="DominoNucleusProjectModelsForkOrCopyProject")


@_attrs_define
class DominoNucleusProjectModelsForkOrCopyProject:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        visibility (DominoNucleusProjectModelsForkOrCopyProjectVisibility | Unset):
        owner_id (None | str | Unset):
        collaborators (list[DominoProjectsApiCollaboratorDTO] | None | Unset):
        tags (DominoProjectsApiNewTagsDTO | Unset):
        copy_git_request (DominoProjectsApiCopyGitRequest | Unset):
        billing_tag (DominoProjectsApiBillingTag | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    visibility: DominoNucleusProjectModelsForkOrCopyProjectVisibility | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    collaborators: list[DominoProjectsApiCollaboratorDTO] | None | Unset = UNSET
    tags: DominoProjectsApiNewTagsDTO | Unset = UNSET
    copy_git_request: DominoProjectsApiCopyGitRequest | Unset = UNSET
    billing_tag: DominoProjectsApiBillingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        collaborators: list[dict[str, Any]] | None | Unset
        if isinstance(self.collaborators, Unset):
            collaborators = UNSET
        elif isinstance(self.collaborators, list):
            collaborators = []
            for collaborators_type_0_item_data in self.collaborators:
                collaborators_type_0_item = collaborators_type_0_item_data.to_dict()
                collaborators.append(collaborators_type_0_item)

        else:
            collaborators = self.collaborators

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        copy_git_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_git_request, Unset):
            copy_git_request = self.copy_git_request.to_dict()

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators
        if tags is not UNSET:
            field_dict["tags"] = tags
        if copy_git_request is not UNSET:
            field_dict["copyGitRequest"] = copy_git_request
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
        from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
        from ..models.domino_projects_api_copy_git_request import DominoProjectsApiCopyGitRequest
        from ..models.domino_projects_api_new_tags_dto import DominoProjectsApiNewTagsDTO

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _visibility = d.pop("visibility", UNSET)
        visibility: DominoNucleusProjectModelsForkOrCopyProjectVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = DominoNucleusProjectModelsForkOrCopyProjectVisibility(_visibility)

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("ownerId", UNSET))

        def _parse_collaborators(data: object) -> list[DominoProjectsApiCollaboratorDTO] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collaborators_type_0 = []
                _collaborators_type_0 = data
                for collaborators_type_0_item_data in _collaborators_type_0:
                    collaborators_type_0_item = DominoProjectsApiCollaboratorDTO.from_dict(
                        collaborators_type_0_item_data
                    )

                    collaborators_type_0.append(collaborators_type_0_item)

                return collaborators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsApiCollaboratorDTO] | None | Unset, data)

        collaborators = _parse_collaborators(d.pop("collaborators", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: DominoProjectsApiNewTagsDTO | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = DominoProjectsApiNewTagsDTO.from_dict(_tags)

        _copy_git_request = d.pop("copyGitRequest", UNSET)
        copy_git_request: DominoProjectsApiCopyGitRequest | Unset
        if isinstance(_copy_git_request, Unset):
            copy_git_request = UNSET
        else:
            copy_git_request = DominoProjectsApiCopyGitRequest.from_dict(_copy_git_request)

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: DominoProjectsApiBillingTag | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = DominoProjectsApiBillingTag.from_dict(_billing_tag)

        domino_nucleus_project_models_fork_or_copy_project = cls(
            name=name,
            description=description,
            visibility=visibility,
            owner_id=owner_id,
            collaborators=collaborators,
            tags=tags,
            copy_git_request=copy_git_request,
            billing_tag=billing_tag,
        )

        domino_nucleus_project_models_fork_or_copy_project.additional_properties = d
        return domino_nucleus_project_models_fork_or_copy_project

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
