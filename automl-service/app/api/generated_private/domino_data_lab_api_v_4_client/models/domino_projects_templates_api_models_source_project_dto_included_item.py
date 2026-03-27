from enum import Enum


class DominoProjectsTemplatesApiModelsSourceProjectDtoIncludedItem(str, Enum):
    APPS = "apps"
    ARTIFACTS = "artifacts"
    CODE = "code"
    DATASETS = "datasets"
    DATA_SOURCES = "data_sources"
    EXTERNAL_DATA_VOLUMES = "external_data_volumes"
    GOALS = "goals"
    IMPORTED_PROJECTS = "imported_projects"
    IMPORTED_REPOSITORIES = "imported_repositories"
    INTEGRATIONS = "integrations"
    LAUNCHERS = "launchers"
    MOUNTED_DATASETS = "mounted_datasets"
    NET_APP_VOLUMES = "net_app_volumes"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)
