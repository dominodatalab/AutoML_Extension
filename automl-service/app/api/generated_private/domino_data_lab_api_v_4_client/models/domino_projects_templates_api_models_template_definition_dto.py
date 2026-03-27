from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domino_projects_templates_api_models_template_definition_dto_project_type import (
    DominoProjectsTemplatesApiModelsTemplateDefinitionDtoProjectType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domino_projects_templates_api_models_app_dto import DominoProjectsTemplatesApiModelsAppDto
    from ..models.domino_projects_templates_api_models_backing_project_dto import (
        DominoProjectsTemplatesApiModelsBackingProjectDto,
    )
    from ..models.domino_projects_templates_api_models_dataset_dto import DominoProjectsTemplatesApiModelsDatasetDto
    from ..models.domino_projects_templates_api_models_datasource_dto import (
        DominoProjectsTemplatesApiModelsDatasourceDto,
    )
    from ..models.domino_projects_templates_api_models_external_data_volume_dto import (
        DominoProjectsTemplatesApiModelsExternalDataVolumeDto,
    )
    from ..models.domino_projects_templates_api_models_git_repository_dto import (
        DominoProjectsTemplatesApiModelsGitRepositoryDto,
    )
    from ..models.domino_projects_templates_api_models_launcher_dto import DominoProjectsTemplatesApiModelsLauncherDto
    from ..models.domino_projects_templates_api_models_net_app_volume_dto import (
        DominoProjectsTemplatesApiModelsNetAppVolumeDto,
    )
    from ..models.domino_projects_templates_api_models_project_goal_dto import (
        DominoProjectsTemplatesApiModelsProjectGoalDto,
    )
    from ..models.domino_projects_templates_api_models_settings_dto import DominoProjectsTemplatesApiModelsSettingsDto


T = TypeVar("T", bound="DominoProjectsTemplatesApiModelsTemplateDefinitionDto")


@_attrs_define
class DominoProjectsTemplatesApiModelsTemplateDefinitionDto:
    """
    Attributes:
        backing_project (DominoProjectsTemplatesApiModelsBackingProjectDto):
        project_type (DominoProjectsTemplatesApiModelsTemplateDefinitionDtoProjectType):
        imported_repos (list[DominoProjectsTemplatesApiModelsGitRepositoryDto]):
        goals (list[DominoProjectsTemplatesApiModelsProjectGoalDto]):
        settings (DominoProjectsTemplatesApiModelsSettingsDto):
        net_app_volumes (list[DominoProjectsTemplatesApiModelsNetAppVolumeDto]):
        datasets (list[DominoProjectsTemplatesApiModelsDatasetDto]):
        datasources (list[DominoProjectsTemplatesApiModelsDatasourceDto]):
        external_data_volumes (list[DominoProjectsTemplatesApiModelsExternalDataVolumeDto]):
        apps (list[DominoProjectsTemplatesApiModelsAppDto]):
        launchers (list[DominoProjectsTemplatesApiModelsLauncherDto]):
        main_repository (DominoProjectsTemplatesApiModelsGitRepositoryDto | Unset):
    """

    backing_project: DominoProjectsTemplatesApiModelsBackingProjectDto
    project_type: DominoProjectsTemplatesApiModelsTemplateDefinitionDtoProjectType
    imported_repos: list[DominoProjectsTemplatesApiModelsGitRepositoryDto]
    goals: list[DominoProjectsTemplatesApiModelsProjectGoalDto]
    settings: DominoProjectsTemplatesApiModelsSettingsDto
    net_app_volumes: list[DominoProjectsTemplatesApiModelsNetAppVolumeDto]
    datasets: list[DominoProjectsTemplatesApiModelsDatasetDto]
    datasources: list[DominoProjectsTemplatesApiModelsDatasourceDto]
    external_data_volumes: list[DominoProjectsTemplatesApiModelsExternalDataVolumeDto]
    apps: list[DominoProjectsTemplatesApiModelsAppDto]
    launchers: list[DominoProjectsTemplatesApiModelsLauncherDto]
    main_repository: DominoProjectsTemplatesApiModelsGitRepositoryDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backing_project = self.backing_project.to_dict()

        project_type = self.project_type.value

        imported_repos = []
        for imported_repos_item_data in self.imported_repos:
            imported_repos_item = imported_repos_item_data.to_dict()
            imported_repos.append(imported_repos_item)

        goals = []
        for goals_item_data in self.goals:
            goals_item = goals_item_data.to_dict()
            goals.append(goals_item)

        settings = self.settings.to_dict()

        net_app_volumes = []
        for net_app_volumes_item_data in self.net_app_volumes:
            net_app_volumes_item = net_app_volumes_item_data.to_dict()
            net_app_volumes.append(net_app_volumes_item)

        datasets = []
        for datasets_item_data in self.datasets:
            datasets_item = datasets_item_data.to_dict()
            datasets.append(datasets_item)

        datasources = []
        for datasources_item_data in self.datasources:
            datasources_item = datasources_item_data.to_dict()
            datasources.append(datasources_item)

        external_data_volumes = []
        for external_data_volumes_item_data in self.external_data_volumes:
            external_data_volumes_item = external_data_volumes_item_data.to_dict()
            external_data_volumes.append(external_data_volumes_item)

        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()
            apps.append(apps_item)

        launchers = []
        for launchers_item_data in self.launchers:
            launchers_item = launchers_item_data.to_dict()
            launchers.append(launchers_item)

        main_repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_repository, Unset):
            main_repository = self.main_repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "backingProject": backing_project,
                "projectType": project_type,
                "importedRepos": imported_repos,
                "goals": goals,
                "settings": settings,
                "netAppVolumes": net_app_volumes,
                "datasets": datasets,
                "datasources": datasources,
                "externalDataVolumes": external_data_volumes,
                "apps": apps,
                "launchers": launchers,
            }
        )
        if main_repository is not UNSET:
            field_dict["mainRepository"] = main_repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domino_projects_templates_api_models_app_dto import DominoProjectsTemplatesApiModelsAppDto
        from ..models.domino_projects_templates_api_models_backing_project_dto import (
            DominoProjectsTemplatesApiModelsBackingProjectDto,
        )
        from ..models.domino_projects_templates_api_models_dataset_dto import DominoProjectsTemplatesApiModelsDatasetDto
        from ..models.domino_projects_templates_api_models_datasource_dto import (
            DominoProjectsTemplatesApiModelsDatasourceDto,
        )
        from ..models.domino_projects_templates_api_models_external_data_volume_dto import (
            DominoProjectsTemplatesApiModelsExternalDataVolumeDto,
        )
        from ..models.domino_projects_templates_api_models_git_repository_dto import (
            DominoProjectsTemplatesApiModelsGitRepositoryDto,
        )
        from ..models.domino_projects_templates_api_models_launcher_dto import (
            DominoProjectsTemplatesApiModelsLauncherDto,
        )
        from ..models.domino_projects_templates_api_models_net_app_volume_dto import (
            DominoProjectsTemplatesApiModelsNetAppVolumeDto,
        )
        from ..models.domino_projects_templates_api_models_project_goal_dto import (
            DominoProjectsTemplatesApiModelsProjectGoalDto,
        )
        from ..models.domino_projects_templates_api_models_settings_dto import (
            DominoProjectsTemplatesApiModelsSettingsDto,
        )

        d = dict(src_dict)
        backing_project = DominoProjectsTemplatesApiModelsBackingProjectDto.from_dict(d.pop("backingProject"))

        project_type = DominoProjectsTemplatesApiModelsTemplateDefinitionDtoProjectType(d.pop("projectType"))

        imported_repos = []
        _imported_repos = d.pop("importedRepos")
        for imported_repos_item_data in _imported_repos:
            imported_repos_item = DominoProjectsTemplatesApiModelsGitRepositoryDto.from_dict(imported_repos_item_data)

            imported_repos.append(imported_repos_item)

        goals = []
        _goals = d.pop("goals")
        for goals_item_data in _goals:
            goals_item = DominoProjectsTemplatesApiModelsProjectGoalDto.from_dict(goals_item_data)

            goals.append(goals_item)

        settings = DominoProjectsTemplatesApiModelsSettingsDto.from_dict(d.pop("settings"))

        net_app_volumes = []
        _net_app_volumes = d.pop("netAppVolumes")
        for net_app_volumes_item_data in _net_app_volumes:
            net_app_volumes_item = DominoProjectsTemplatesApiModelsNetAppVolumeDto.from_dict(net_app_volumes_item_data)

            net_app_volumes.append(net_app_volumes_item)

        datasets = []
        _datasets = d.pop("datasets")
        for datasets_item_data in _datasets:
            datasets_item = DominoProjectsTemplatesApiModelsDatasetDto.from_dict(datasets_item_data)

            datasets.append(datasets_item)

        datasources = []
        _datasources = d.pop("datasources")
        for datasources_item_data in _datasources:
            datasources_item = DominoProjectsTemplatesApiModelsDatasourceDto.from_dict(datasources_item_data)

            datasources.append(datasources_item)

        external_data_volumes = []
        _external_data_volumes = d.pop("externalDataVolumes")
        for external_data_volumes_item_data in _external_data_volumes:
            external_data_volumes_item = DominoProjectsTemplatesApiModelsExternalDataVolumeDto.from_dict(
                external_data_volumes_item_data
            )

            external_data_volumes.append(external_data_volumes_item)

        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = DominoProjectsTemplatesApiModelsAppDto.from_dict(apps_item_data)

            apps.append(apps_item)

        launchers = []
        _launchers = d.pop("launchers")
        for launchers_item_data in _launchers:
            launchers_item = DominoProjectsTemplatesApiModelsLauncherDto.from_dict(launchers_item_data)

            launchers.append(launchers_item)

        _main_repository = d.pop("mainRepository", UNSET)
        main_repository: DominoProjectsTemplatesApiModelsGitRepositoryDto | Unset
        if isinstance(_main_repository, Unset):
            main_repository = UNSET
        else:
            main_repository = DominoProjectsTemplatesApiModelsGitRepositoryDto.from_dict(_main_repository)

        domino_projects_templates_api_models_template_definition_dto = cls(
            backing_project=backing_project,
            project_type=project_type,
            imported_repos=imported_repos,
            goals=goals,
            settings=settings,
            net_app_volumes=net_app_volumes,
            datasets=datasets,
            datasources=datasources,
            external_data_volumes=external_data_volumes,
            apps=apps,
            launchers=launchers,
            main_repository=main_repository,
        )

        domino_projects_templates_api_models_template_definition_dto.additional_properties = d
        return domino_projects_templates_api_models_template_definition_dto

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
