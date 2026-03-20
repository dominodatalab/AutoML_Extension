from enum import Enum


class ProjectTemplateSourceProjectComponent(str, Enum):
    APPS = "Apps"
    ARTIFACTS = "Artifacts"
    CODE = "Code"
    DATASETS = "Datasets"
    DATASOURCES = "DataSources"
    EXTERNALDATAVOLUMES = "ExternalDataVolumes"
    GOALS = "Goals"
    IMPORTEDPROJECTS = "ImportedProjects"
    IMPORTEDREPOSITORIES = "ImportedRepositories"
    INTEGRATIONS = "Integrations"
    LAUNCHERS = "Launchers"
    MOUNTEDDATASETS = "MountedDatasets"
    NETAPPVOLUMES = "NetAppVolumes"
    TAGS = "Tags"

    def __str__(self) -> str:
        return str(self.value)
