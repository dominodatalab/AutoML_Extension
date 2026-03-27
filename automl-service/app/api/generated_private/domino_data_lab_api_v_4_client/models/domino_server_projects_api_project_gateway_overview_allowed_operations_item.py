from enum import Enum


class DominoServerProjectsApiProjectGatewayOverviewAllowedOperationsItem(str, Enum):
    BROWSEREADFILES = "BrowseReadFiles"
    CHANGEPROJECTSETTINGS = "ChangeProjectSettings"
    EDIT = "Edit"
    EDITTAGS = "EditTags"
    PROJECTSEARCHPREVIEW = "ProjectSearchPreview"
    RUN = "Run"
    RUNLAUNCHERS = "RunLaunchers"
    UPDATEPROJECTDESCRIPTION = "UpdateProjectDescription"
    VIEWRUNS = "ViewRuns"
    VIEWWORKSPACES = "ViewWorkspaces"

    def __str__(self) -> str:
        return str(self.value)
