from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_visibility_v1 import ProjectVisibilityV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_tag_v1 import BillingTagV1
    from ..models.project_collaborator_v1 import ProjectCollaboratorV1
    from ..models.project_git_repository_v1 import ProjectGitRepositoryV1


T = TypeVar("T", bound="ProjectV1")


@_attrs_define
class ProjectV1:
    """
    Attributes:
        collaborators (list[ProjectCollaboratorV1]): List of collaborators, if any
        description (str): A description of the project
        id (str): Project ID Example: 626046fcb7e5d347dbe7a904.
        is_restricted (bool): Whether a project is restricted
        name (str): Name of the project Example: My Project.
        owner_id (str): userId of the project owner Example: 662604702b7e5d347dbe7a908.
        owner_username (str): username of the project owner Example: steve_holt.
        visibility (ProjectVisibilityV1): Project visibility
        billing_tag (BillingTagV1 | Unset): Billing Tag to assign to projects for cost aggregation
        internal_tags (list[str] | Unset): Optional list of strings containing internal tags of project Example:
            ['restricted'].
        main_repository (ProjectGitRepositoryV1 | Unset):
    """

    collaborators: list[ProjectCollaboratorV1]
    description: str
    id: str
    is_restricted: bool
    name: str
    owner_id: str
    owner_username: str
    visibility: ProjectVisibilityV1
    billing_tag: BillingTagV1 | Unset = UNSET
    internal_tags: list[str] | Unset = UNSET
    main_repository: ProjectGitRepositoryV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        description = self.description

        id = self.id

        is_restricted = self.is_restricted

        name = self.name

        owner_id = self.owner_id

        owner_username = self.owner_username

        visibility = self.visibility.value

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        internal_tags: list[str] | Unset = UNSET
        if not isinstance(self.internal_tags, Unset):
            internal_tags = self.internal_tags

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collaborators": collaborators,
                "description": description,
                "id": id,
                "isRestricted": is_restricted,
                "name": name,
                "ownerId": owner_id,
                "ownerUsername": owner_username,
                "visibility": visibility,
            }
        )
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag
        if internal_tags is not UNSET:
            field_dict["internalTags"] = internal_tags
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_tag_v1 import BillingTagV1
        from ..models.project_collaborator_v1 import ProjectCollaboratorV1
        from ..models.project_git_repository_v1 import ProjectGitRepositoryV1

        d = dict(src_dict)
        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = ProjectCollaboratorV1.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        description = d.pop("description")

        id = d.pop("id")

        is_restricted = d.pop("isRestricted")

        name = d.pop("name")

        owner_id = d.pop("ownerId")

        owner_username = d.pop("ownerUsername")

        visibility = ProjectVisibilityV1(d.pop("visibility"))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: BillingTagV1 | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = BillingTagV1.from_dict(_billing_tag)

        internal_tags = cast(list[str], d.pop("internalTags", UNSET))

        _main_repository = d.pop("mainRepository", UNSET)
        main_repository: ProjectGitRepositoryV1 | Unset
        if isinstance(_main_repository, Unset):
            main_repository = UNSET
        else:
            main_repository = ProjectGitRepositoryV1.from_dict(_main_repository)

        project_v1 = cls(
            collaborators=collaborators,
            description=description,
            id=id,
            is_restricted=is_restricted,
            name=name,
            owner_id=owner_id,
            owner_username=owner_username,
            visibility=visibility,
            billing_tag=billing_tag,
            internal_tags=internal_tags,
            main_repository=main_repository,
        )

        project_v1.additional_properties = d
        return project_v1

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
