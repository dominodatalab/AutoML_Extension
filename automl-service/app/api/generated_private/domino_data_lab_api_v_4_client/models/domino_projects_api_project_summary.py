from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domino_projects_api_project_summary_project_type import DominoProjectsApiProjectSummaryProjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
    from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
    from ..models.domino_projects_api_project_git_repository_temp import DominoProjectsApiProjectGitRepositoryTemp
    from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus
    from ..models.domino_projects_api_project_tag_dto import DominoProjectsApiProjectTagDTO
    from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
    from ..models.domino_projects_api_repositories_git_repository_dto import (
        DominoProjectsApiRepositoriesGitRepositoryDTO,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectSummary")


@_attrs_define
class DominoProjectsApiProjectSummary:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        created (datetime.datetime):
        visibility (str):
        owner_id (str):
        owner_username (str):
        imported_git_repositories (list[DominoProjectsApiRepositoriesGitRepositoryDTO]):
        collaborator_ids (list[str]):
        collaborators (list[DominoProjectsApiCollaboratorDTO]):
        tags (list[DominoProjectsApiProjectTagDTO]):
        stage_id (str):
        status (DominoProjectsApiProjectStatus):
        project_type (DominoProjectsApiProjectSummaryProjectType):
        main_repository (DominoProjectsApiProjectGitRepositoryTemp | Unset):
        template_details (DominoProjectsApiProjectTemplateDetails | Unset):
        internal_tags (list[str] | None | Unset):
        billing_tag (DominoProjectsApiBillingTag | Unset):
    """

    id: str
    name: str
    description: str
    created: datetime.datetime
    visibility: str
    owner_id: str
    owner_username: str
    imported_git_repositories: list[DominoProjectsApiRepositoriesGitRepositoryDTO]
    collaborator_ids: list[str]
    collaborators: list[DominoProjectsApiCollaboratorDTO]
    tags: list[DominoProjectsApiProjectTagDTO]
    stage_id: str
    status: DominoProjectsApiProjectStatus
    project_type: DominoProjectsApiProjectSummaryProjectType
    main_repository: DominoProjectsApiProjectGitRepositoryTemp | Unset = UNSET
    template_details: DominoProjectsApiProjectTemplateDetails | Unset = UNSET
    internal_tags: list[str] | None | Unset = UNSET
    billing_tag: DominoProjectsApiBillingTag | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        created = self.created.isoformat()

        visibility = self.visibility

        owner_id = self.owner_id

        owner_username = self.owner_username

        imported_git_repositories = []
        for imported_git_repositories_item_data in self.imported_git_repositories:
            imported_git_repositories_item = imported_git_repositories_item_data.to_dict()
            imported_git_repositories.append(imported_git_repositories_item)

        collaborator_ids = self.collaborator_ids

        collaborators = []
        for collaborators_item_data in self.collaborators:
            collaborators_item = collaborators_item_data.to_dict()
            collaborators.append(collaborators_item)

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        stage_id = self.stage_id

        status = self.status.to_dict()

        project_type = self.project_type.value

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        template_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_details, Unset):
            template_details = self.template_details.to_dict()

        internal_tags: list[str] | None | Unset
        if isinstance(self.internal_tags, Unset):
            internal_tags = UNSET
        elif isinstance(self.internal_tags, list):
            internal_tags = self.internal_tags

        else:
            internal_tags = self.internal_tags

        billing_tag: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_tag, Unset):
            billing_tag = self.billing_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "created": created,
                "visibility": visibility,
                "ownerId": owner_id,
                "ownerUsername": owner_username,
                "importedGitRepositories": imported_git_repositories,
                "collaboratorIds": collaborator_ids,
                "collaborators": collaborators,
                "tags": tags,
                "stageId": stage_id,
                "status": status,
                "projectType": project_type,
            }
        )
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository
        if template_details is not UNSET:
            field_dict["templateDetails"] = template_details
        if internal_tags is not UNSET:
            field_dict["internalTags"] = internal_tags
        if billing_tag is not UNSET:
            field_dict["billingTag"] = billing_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_billing_tag import DominoProjectsApiBillingTag
        from ..models.domino_projects_api_collaborator_dto import DominoProjectsApiCollaboratorDTO
        from ..models.domino_projects_api_project_git_repository_temp import DominoProjectsApiProjectGitRepositoryTemp
        from ..models.domino_projects_api_project_status import DominoProjectsApiProjectStatus
        from ..models.domino_projects_api_project_tag_dto import DominoProjectsApiProjectTagDTO
        from ..models.domino_projects_api_project_template_details import DominoProjectsApiProjectTemplateDetails
        from ..models.domino_projects_api_repositories_git_repository_dto import (
            DominoProjectsApiRepositoriesGitRepositoryDTO,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        created = isoparse(d.pop("created"))

        visibility = d.pop("visibility")

        owner_id = d.pop("ownerId")

        owner_username = d.pop("ownerUsername")

        imported_git_repositories = []
        _imported_git_repositories = d.pop("importedGitRepositories")
        for imported_git_repositories_item_data in _imported_git_repositories:
            imported_git_repositories_item = DominoProjectsApiRepositoriesGitRepositoryDTO.from_dict(
                imported_git_repositories_item_data
            )

            imported_git_repositories.append(imported_git_repositories_item)

        collaborator_ids = cast(list[str], d.pop("collaboratorIds"))

        collaborators = []
        _collaborators = d.pop("collaborators")
        for collaborators_item_data in _collaborators:
            collaborators_item = DominoProjectsApiCollaboratorDTO.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = DominoProjectsApiProjectTagDTO.from_dict(tags_item_data)

            tags.append(tags_item)

        stage_id = d.pop("stageId")

        status = DominoProjectsApiProjectStatus.from_dict(d.pop("status"))

        project_type = DominoProjectsApiProjectSummaryProjectType(d.pop("projectType"))

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

        def _parse_internal_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_tags_type_0 = cast(list[str], data)

                return internal_tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        internal_tags = _parse_internal_tags(d.pop("internalTags", UNSET))

        _billing_tag = d.pop("billingTag", UNSET)
        billing_tag: DominoProjectsApiBillingTag | Unset
        if isinstance(_billing_tag, Unset):
            billing_tag = UNSET
        else:
            billing_tag = DominoProjectsApiBillingTag.from_dict(_billing_tag)

        domino_projects_api_project_summary = cls(
            id=id,
            name=name,
            description=description,
            created=created,
            visibility=visibility,
            owner_id=owner_id,
            owner_username=owner_username,
            imported_git_repositories=imported_git_repositories,
            collaborator_ids=collaborator_ids,
            collaborators=collaborators,
            tags=tags,
            stage_id=stage_id,
            status=status,
            project_type=project_type,
            main_repository=main_repository,
            template_details=template_details,
            internal_tags=internal_tags,
            billing_tag=billing_tag,
        )

        domino_projects_api_project_summary.additional_properties = d
        return domino_projects_api_project_summary

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
