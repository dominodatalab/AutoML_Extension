from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_nucleus_project_models_new_project_visibility import DominoNucleusProjectModelsNewProjectVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
    from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
    from ..models.domino_projects_api_new_tags_dto import DominoProjectsApiNewTagsDTO
    from ..models.domino_projects_api_project_git_repository_temp import DominoProjectsApiProjectGitRepositoryTemp
    from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
    from ..models.domino_projects_api_repositories_requests_create_repo_request import (
        DominoProjectsApiRepositoriesRequestsCreateRepoRequest,
    )


T = TypeVar("T", bound="DominoNucleusProjectModelsNewProject")


@_attrs_define
class DominoNucleusProjectModelsNewProject:
    """
    Attributes:
        name (str):
        description (str):
        visibility (DominoNucleusProjectModelsNewProjectVisibility):
        owner_id (str):
        collaborators (list[DominoProjectsApiCollaboratorDTO]):
        tags (DominoProjectsApiNewTagsDTO):
        repo_to_create (DominoProjectsApiRepositoriesRequestsCreateRepoRequest | Unset):
        main_repository (DominoProjectsApiProjectGitRepositoryTemp | Unset):
        template_details (DominoProjectsApiProjectTemplateDetails | Unset):
        is_restricted (bool | None | Unset):
        billing_tag (DominoProjectsApiBillingTag | Unset):
    """

    name: str
    description: str
    visibility: DominoNucleusProjectModelsNewProjectVisibility
    owner_id: str
    collaborators: list[DominoProjectsApiCollaboratorDTO]
    tags: DominoProjectsApiNewTagsDTO
    repo_to_create: DominoProjectsApiRepositoriesRequestsCreateRepoRequest | Unset = UNSET
    main_repository: DominoProjectsApiProjectGitRepositoryTemp | Unset = UNSET
    template_details: DominoProjectsApiProjectTemplateDetails | Unset = UNSET
    is_restricted: bool | None | Unset = UNSET
    billing_tag: DominoProjectsApiBillingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        visibility = self.visibility.value

        owner_id = self.owner_id

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        tags = self.tags.to_dict()

        repo_to_create: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repo_to_create, Unset):
            repo_to_create = self.repo_to_create.to_dict()

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        template_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_details, Unset):
            template_details = self.template_details.to_dict()

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "visibility": visibility,
                "ownerId": owner_id,
                "collaborators": collaborators,
                "tags": tags,
            }
        )
        if repo_to_create is not UNSET:
            field_dict["repoToCreate"] = repo_to_create
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository
        if template_details is not UNSET:
            field_dict["templateDetails"] = template_details
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
        from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
        from ..models.domino_projects_api_new_tags_dto import DominoProjectsApiNewTagsDTO
        from ..models.domino_projects_api_project_git_repository_temp import DominoProjectsApiProjectGitRepositoryTemp
        from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
        from ..models.domino_projects_api_repositories_requests_create_repo_request import (
            DominoProjectsApiRepositoriesRequestsCreateRepoRequest,
        )

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        visibility = DominoNucleusProjectModelsNewProjectVisibility(d.pop("visibility"))

        owner_id = d.pop("ownerId")

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoProjectsApiCollaboratorDTO.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        tags = DominoProjectsApiNewTagsDTO.from_dict(d.pop("tags"))

        _repo_to_create = d.pop("repoToCreate", UNSET)
        repo_to_create: DominoProjectsApiRepositoriesRequestsCreateRepoRequest | Unset
        if isinstance(_repo_to_create, Unset):
            repo_to_create = UNSET
        else:
            repo_to_create = DominoProjectsApiRepositoriesRequestsCreateRepoRequest.from_dict(_repo_to_create)

        _main_repository = d.pop("mainRepository", UNSET)
        main_repository: DominoProjectsApiProjectGitRepositoryTemp | Unset
        if isinstance(_main_repository, Unset):
            main_repository = UNSET
        else:
            main_repository = DominoProjectsApiProjectGitRepositoryTemp.from_dict(_main_repository)

        _template_details = d.pop("templateDetails", UNSET)
        template_details: DominoProjectsApiProjectTemplateDetails | Unset
        if isinstance(_template_details, Unset):
            template_details = UNSET
        else:
            template_details = DominoProjectsApiProjectTemplateDetails.from_dict(_template_details)

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("isRestricted", UNSET))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: DominoProjectsApiBillingTag | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = DominoProjectsApiBillingTag.from_dict(_billing_tag)

        domino_nucleus_project_models_new_project = cls(
            name=name,
            description=description,
            visibility=visibility,
            owner_id=owner_id,
            collaborators=collaborators,
            tags=tags,
            repo_to_create=repo_to_create,
            main_repository=main_repository,
            template_details=template_details,
            is_restricted=is_restricted,
            billing_tag=billing_tag,
        )

        domino_nucleus_project_models_new_project.additional_properties = d
        return domino_nucleus_project_models_new_project

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
