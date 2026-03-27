from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_api_project_template_prerequisites import (
        DominoProjectsApiProjectTemplatePrerequisites,
    )
    from ..models.domino_projects_api_repositories_responses_project_template_repository_dto import (
        DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO,
    )
    from ..models.domino_projects_templates_api_models_dependency_template_dto import (
        DominoProjectsTemplatesApiModelsDependencyTemplateDto,
    )
    from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink
    from ..models.domino_projects_templates_api_models_named_optional_link import (
        DominoProjectsTemplatesApiModelsNamedOptionalLink,
    )
    from ..models.domino_projects_templates_api_models_project_hub_model_dto import (
        DominoProjectsTemplatesApiModelsProjectHubModelDto,
    )
    from ..models.domino_projects_templates_api_models_project_template_environment_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto,
    )
    from ..models.domino_projects_templates_api_models_project_template_goals_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto,
    )
    from ..models.domino_projects_templates_api_models_project_template_imported_repository_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateImportedRepositoryDto,
    )
    from ..models.domino_projects_templates_api_models_project_template_project_settings_dto import (
        DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto,
    )
    from ..models.domino_projects_templates_api_models_value_optional_link import (
        DominoProjectsTemplatesApiModelsValueOptionalLink,
    )


T = TypeVar("T", bound="DominoProjectsApiProjectHubTemplateResult")


@_attrs_define
class DominoProjectsApiProjectHubTemplateResult:
    """
    Attributes:
        template_id (str):
        title (str):
        categories (list[str]):
        main_repository (DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO):
        created (datetime.datetime):
        updated (datetime.datetime):
        owner (DominoProjectsTemplatesApiModelsNamedLink):
        models (list[DominoProjectsTemplatesApiModelsProjectHubModelDto]):
        revision_id (str):
        imported_repositories (list[DominoProjectsTemplatesApiModelsProjectTemplateImportedRepositoryDto]):
        description (None | str | Unset):
        base_64_logo (None | str | Unset):
        license_ (DominoProjectsTemplatesApiModelsNamedLink | Unset):
        data (DominoProjectsTemplatesApiModelsNamedOptionalLink | Unset):
        data_format (None | str | Unset):
        recommended (bool | None | Unset):
        prerequisites (list[DominoProjectsApiProjectTemplatePrerequisites] | None | Unset):
        goals (list[DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto] | None | Unset):
        hardware_tier (DominoProjectsTemplatesApiModelsValueOptionalLink | Unset):
        environment_reqs (DominoProjectsTemplatesApiModelsValueOptionalLink | Unset):
        environment (DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto | Unset):
        project_settings (DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto | Unset):
        dependencies (list[DominoProjectsTemplatesApiModelsDependencyTemplateDto] | None | Unset):
        supported_domino_versions (list[str] | None | Unset):
    """

    template_id: str
    title: str
    categories: list[str]
    main_repository: DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO
    created: datetime.datetime
    updated: datetime.datetime
    owner: DominoProjectsTemplatesApiModelsNamedLink
    models: list[DominoProjectsTemplatesApiModelsProjectHubModelDto]
    revision_id: str
    imported_repositories: list[DominoProjectsTemplatesApiModelsProjectTemplateImportedRepositoryDto]
    description: None | str | Unset = UNSET
    base_64_logo: None | str | Unset = UNSET
    license_: DominoProjectsTemplatesApiModelsNamedLink | Unset = UNSET
    data: DominoProjectsTemplatesApiModelsNamedOptionalLink | Unset = UNSET
    data_format: None | str | Unset = UNSET
    recommended: bool | None | Unset = UNSET
    prerequisites: list[DominoProjectsApiProjectTemplatePrerequisites] | None | Unset = UNSET
    goals: list[DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto] | None | Unset = UNSET
    hardware_tier: DominoProjectsTemplatesApiModelsValueOptionalLink | Unset = UNSET
    environment_reqs: DominoProjectsTemplatesApiModelsValueOptionalLink | Unset = UNSET
    environment: DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto | Unset = UNSET
    project_settings: DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto | Unset = UNSET
    dependencies: list[DominoProjectsTemplatesApiModelsDependencyTemplateDto] | None | Unset = UNSET
    supported_domino_versions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        title = self.title

        categories = self.categories

        main_repository = self.main_repository.to_dict()

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        owner = self.owner.to_dict()

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        revision_id = self.revision_id

        imported_repositories = []
        for imported_repositories_item_data in self.imported_repositories:
            imported_repositories_item = imported_repositories_item_data.to_dict()
            imported_repositories.append(imported_repositories_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        base_64_logo: None | str | Unset
        if isinstance(self.base_64_logo, Unset):
            base_64_logo = UNSET
        else:
            base_64_logo = self.base_64_logo

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        data_format: None | str | Unset
        if isinstance(self.data_format, Unset):
            data_format = UNSET
        else:
            data_format = self.data_format

        recommended: bool | None | Unset
        if isinstance(self.recommended, Unset):
            recommended = UNSET
        else:
            recommended = self.recommended

        prerequisites: list[dict[str, Any]] | None | Unset
        if isinstance(self.prerequisites, Unset):
            prerequisites = UNSET
        elif isinstance(self.prerequisites, list):
            prerequisites = []
            for prerequisites_type_0_item_data in self.prerequisites:
                prerequisites_type_0_item = prerequisites_type_0_item_data.to_dict()
                prerequisites.append(prerequisites_type_0_item)

        else:
            prerequisites = self.prerequisites

        goals: list[dict[str, Any]] | None | Unset
        if isinstance(self.goals, Unset):
            goals = UNSET
        elif isinstance(self.goals, list):
            goals = []
            for goals_type_0_item_data in self.goals:
                goals_type_0_item = goals_type_0_item_data.to_dict()
                goals.append(goals_type_0_item)

        else:
            goals = self.goals

        hardware_tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hardware_tier, Unset):
            hardware_tier = self.hardware_tier.to_dict()

        environment_reqs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment_reqs, Unset):
            environment_reqs = self.environment_reqs.to_dict()

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        project_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_settings, Unset):
            project_settings = self.project_settings.to_dict()

        dependencies: list[dict[str, Any]] | None | Unset
        if isinstance(self.dependencies, Unset):
            dependencies = UNSET
        elif isinstance(self.dependencies, list):
            dependencies = []
            for dependencies_type_0_item_data in self.dependencies:
                dependencies_type_0_item = dependencies_type_0_item_data.to_dict()
                dependencies.append(dependencies_type_0_item)

        else:
            dependencies = self.dependencies

        supported_domino_versions: list[str] | None | Unset
        if isinstance(self.supported_domino_versions, Unset):
            supported_domino_versions = UNSET
        elif isinstance(self.supported_domino_versions, list):
            supported_domino_versions = self.supported_domino_versions

        else:
            supported_domino_versions = self.supported_domino_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateId": template_id,
                "title": title,
                "categories": categories,
                "mainRepository": main_repository,
                "created": created,
                "updated": updated,
                "owner": owner,
                "models": models,
                "revisionId": revision_id,
                "importedRepositories": imported_repositories,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if base_64_logo is not UNSET:
            field_dict["base64Logo"] = base_64_logo
        if license_ is not UNSET:
            field_dict["license"] = license_
        if data is not UNSET:
            field_dict["data"] = data
        if data_format is not UNSET:
            field_dict["dataFormat"] = data_format
        if recommended is not UNSET:
            field_dict["recommended"] = recommended
        if prerequisites is not UNSET:
            field_dict["prerequisites"] = prerequisites
        if goals is not UNSET:
            field_dict["goals"] = goals
        if hardware_tier is not UNSET:
            field_dict["hardwareTier"] = hardware_tier
        if environment_reqs is not UNSET:
            field_dict["environmentReqs"] = environment_reqs
        if environment is not UNSET:
            field_dict["environment"] = environment
        if project_settings is not UNSET:
            field_dict["projectSettings"] = project_settings
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if supported_domino_versions is not UNSET:
            field_dict["supportedDominoVersions"] = supported_domino_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_api_project_template_prerequisites import (
            DominoProjectsApiProjectTemplatePrerequisites,
        )
        from ..models.domino_projects_api_repositories_responses_project_template_repository_dto import (
            DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO,
        )
        from ..models.domino_projects_templates_api_models_dependency_template_dto import (
            DominoProjectsTemplatesApiModelsDependencyTemplateDto,
        )
        from ..models.domino_projects_templates_api_models_named_link import DominoProjectsTemplatesApiModelsNamedLink
        from ..models.domino_projects_templates_api_models_named_optional_link import (
            DominoProjectsTemplatesApiModelsNamedOptionalLink,
        )
        from ..models.domino_projects_templates_api_models_project_hub_model_dto import (
            DominoProjectsTemplatesApiModelsProjectHubModelDto,
        )
        from ..models.domino_projects_templates_api_models_project_template_environment_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto,
        )
        from ..models.domino_projects_templates_api_models_project_template_goals_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto,
        )
        from ..models.domino_projects_templates_api_models_project_template_imported_repository_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateImportedRepositoryDto,
        )
        from ..models.domino_projects_templates_api_models_project_template_project_settings_dto import (
            DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto,
        )
        from ..models.domino_projects_templates_api_models_value_optional_link import (
            DominoProjectsTemplatesApiModelsValueOptionalLink,
        )

        d = dict(src_dict)
        template_id = d.pop("templateId")

        title = d.pop("title")

        categories = cast(list[str], d.pop("categories"))

        main_repository = DominoProjectsApiRepositoriesResponsesProjectTemplateRepositoryDTO.from_dict(
            d.pop("mainRepository")
        )

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        owner = DominoProjectsTemplatesApiModelsNamedLink.from_dict(d.pop("owner"))

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = DominoProjectsTemplatesApiModelsProjectHubModelDto.from_dict(models_item_data)

            models.append(models_item)

        revision_id = d.pop("revisionId")

        imported_repositories = []
        _imported_repositories = d.pop("importedRepositories")
        for imported_repositories_item_data in _imported_repositories:
            imported_repositories_item = DominoProjectsTemplatesApiModelsProjectTemplateImportedRepositoryDto.from_dict(
                imported_repositories_item_data
            )

            imported_repositories.append(imported_repositories_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_base_64_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base_64_logo = _parse_base_64_logo(d.pop("base64Logo", UNSET))

        _license_ = d.pop("license", UNSET)
        license_: DominoProjectsTemplatesApiModelsNamedLink | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = DominoProjectsTemplatesApiModelsNamedLink.from_dict(_license_)

        _data = d.pop("data", UNSET)
        data: DominoProjectsTemplatesApiModelsNamedOptionalLink | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DominoProjectsTemplatesApiModelsNamedOptionalLink.from_dict(_data)

        def _parse_data_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_format = _parse_data_format(d.pop("dataFormat", UNSET))

        def _parse_recommended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        recommended = _parse_recommended(d.pop("recommended", UNSET))

        def _parse_prerequisites(data: object) -> list[DominoProjectsApiProjectTemplatePrerequisites] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                prerequisites_type_0 = []
                _prerequisites_type_0 = data
                for prerequisites_type_0_item_data in _prerequisites_type_0:
                    prerequisites_type_0_item = DominoProjectsApiProjectTemplatePrerequisites.from_dict(
                        prerequisites_type_0_item_data
                    )

                    prerequisites_type_0.append(prerequisites_type_0_item)

                return prerequisites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsApiProjectTemplatePrerequisites] | None | Unset, data)

        prerequisites = _parse_prerequisites(d.pop("prerequisites", UNSET))

        def _parse_goals(data: object) -> list[DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                goals_type_0 = []
                _goals_type_0 = data
                for goals_type_0_item_data in _goals_type_0:
                    goals_type_0_item = DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto.from_dict(
                        goals_type_0_item_data
                    )

                    goals_type_0.append(goals_type_0_item)

                return goals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsTemplatesApiModelsProjectTemplateGoalsDto] | None | Unset, data)

        goals = _parse_goals(d.pop("goals", UNSET))

        _hardware_tier = d.pop("hardwareTier", UNSET)
        hardware_tier: DominoProjectsTemplatesApiModelsValueOptionalLink | Unset
        if isinstance(_hardware_tier, Unset):
            hardware_tier = UNSET
        else:
            hardware_tier = DominoProjectsTemplatesApiModelsValueOptionalLink.from_dict(_hardware_tier)

        _environment_reqs = d.pop("environmentReqs", UNSET)
        environment_reqs: DominoProjectsTemplatesApiModelsValueOptionalLink | Unset
        if isinstance(_environment_reqs, Unset):
            environment_reqs = UNSET
        else:
            environment_reqs = DominoProjectsTemplatesApiModelsValueOptionalLink.from_dict(_environment_reqs)

        _environment = d.pop("environment", UNSET)
        environment: DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = DominoProjectsTemplatesApiModelsProjectTemplateEnvironmentDto.from_dict(_environment)

        _project_settings = d.pop("projectSettings", UNSET)
        project_settings: DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto | Unset
        if isinstance(_project_settings, Unset):
            project_settings = UNSET
        else:
            project_settings = DominoProjectsTemplatesApiModelsProjectTemplateProjectSettingsDto.from_dict(
                _project_settings
            )

        def _parse_dependencies(
            data: object,
        ) -> list[DominoProjectsTemplatesApiModelsDependencyTemplateDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dependencies_type_0 = []
                _dependencies_type_0 = data
                for dependencies_type_0_item_data in _dependencies_type_0:
                    dependencies_type_0_item = DominoProjectsTemplatesApiModelsDependencyTemplateDto.from_dict(
                        dependencies_type_0_item_data
                    )

                    dependencies_type_0.append(dependencies_type_0_item)

                return dependencies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DominoProjectsTemplatesApiModelsDependencyTemplateDto] | None | Unset, data)

        dependencies = _parse_dependencies(d.pop("dependencies", UNSET))

        def _parse_supported_domino_versions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                supported_domino_versions_type_0 = cast(list[str], data)

                return supported_domino_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        supported_domino_versions = _parse_supported_domino_versions(d.pop("supportedDominoVersions", UNSET))

        domino_projects_api_project_hub_template_result = cls(
            template_id=template_id,
            title=title,
            categories=categories,
            main_repository=main_repository,
            created=created,
            updated=updated,
            owner=owner,
            models=models,
            revision_id=revision_id,
            imported_repositories=imported_repositories,
            description=description,
            base_64_logo=base_64_logo,
            license_=license_,
            data=data,
            data_format=data_format,
            recommended=recommended,
            prerequisites=prerequisites,
            goals=goals,
            hardware_tier=hardware_tier,
            environment_reqs=environment_reqs,
            environment=environment,
            project_settings=project_settings,
            dependencies=dependencies,
            supported_domino_versions=supported_domino_versions,
        )

        domino_projects_api_project_hub_template_result.additional_properties = d
        return domino_projects_api_project_hub_template_result

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
