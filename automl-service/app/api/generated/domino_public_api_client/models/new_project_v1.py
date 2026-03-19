from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_visibility_v1 import ProjectVisibilityV1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_tag_v1 import BillingTagV1
    from ..models.new_project_git_repository_v1 import NewProjectGitRepositoryV1
    from ..models.project_template_details_v1 import ProjectTemplateDetailsV1
    from ..models.repo_to_create_v1 import RepoToCreateV1


T = TypeVar("T", bound="NewProjectV1")


@_attrs_define
class NewProjectV1:
    """
    Attributes:
        description (str): Project description.
        name (str): Name of this project. The name must be unique and cannot contain white space.
        visibility (ProjectVisibilityV1): Project visibility
        billing_tag (BillingTagV1 | Unset): Billing Tag to assign to projects for cost aggregation
        is_restricted (bool | Unset): Optional flag for setting a new project as restricted. ProjectClassifier
            permission required for use.
        main_repository (NewProjectGitRepositoryV1 | Unset):
        owner_id (str | Unset): Optional Id of a user to own this project. Defaults to the calling user if not provided.
            Does not currently support creating projects owned by Organizations.
        repo_to_create (RepoToCreateV1 | Unset): An object representing a new git repo to create in a remote repository
        template_details (ProjectTemplateDetailsV1 | Unset):
    """

    description: str
    name: str
    visibility: ProjectVisibilityV1
    billing_tag: BillingTagV1 | Unset = UNSET
    is_restricted: bool | Unset = UNSET
    main_repository: NewProjectGitRepositoryV1 | Unset = UNSET
    owner_id: str | Unset = UNSET
    repo_to_create: RepoToCreateV1 | Unset = UNSET
    template_details: ProjectTemplateDetailsV1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        visibility = self.visibility.value

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        is_restricted = self.is_restricted

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        owner_id = self.owner_id

        repo_to_create: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_to_create, Unset):
            repo_to_create = self.repo_to_create.to_dict()

        template_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_details, Unset):
            template_details = self.template_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "name": name,
                "visibility": visibility,
            }
        )
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if repo_to_create is not UNSET:
            field_dict["repoToCreate"] = repo_to_create
        if template_details is not UNSET:
            field_dict["templateDetails"] = template_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_tag_v1 import BillingTagV1
        from ..models.new_project_git_repository_v1 import NewProjectGitRepositoryV1
        from ..models.project_template_details_v1 import ProjectTemplateDetailsV1
        from ..models.repo_to_create_v1 import RepoToCreateV1

        d = dict(src_dict)
        description = d.pop("description")

        name = d.pop("name")

        visibility = ProjectVisibilityV1(d.pop("visibility"))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: BillingTagV1 | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = BillingTagV1.from_dict(_billing_tag)

        is_restricted = d.pop("isRestricted", UNSET)

        _main_repository = d.pop("mainRepository", UNSET)
        main_repository: NewProjectGitRepositoryV1 | Unset
        if isinstance(_main_repository, Unset):
            main_repository = UNSET
        else:
            main_repository = NewProjectGitRepositoryV1.from_dict(_main_repository)

        owner_id = d.pop("ownerId", UNSET)

        _repo_to_create = d.pop("repoToCreate", UNSET)
        repo_to_create: RepoToCreateV1 | Unset
        if isinstance(_repo_to_create, Unset):
            repo_to_create = UNSET
        else:
            repo_to_create = RepoToCreateV1.from_dict(_repo_to_create)

        _template_details = d.pop("templateDetails", UNSET)
        template_details: ProjectTemplateDetailsV1 | Unset
        if isinstance(_template_details, Unset):
            template_details = UNSET
        else:
            template_details = ProjectTemplateDetailsV1.from_dict(_template_details)

        new_project_v1 = cls(
            description=description,
            name=name,
            visibility=visibility,
            billing_tag=billing_tag,
            is_restricted=is_restricted,
            main_repository=main_repository,
            owner_id=owner_id,
            repo_to_create=repo_to_create,
            template_details=template_details,
        )

        new_project_v1.additional_properties = d
        return new_project_v1

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
