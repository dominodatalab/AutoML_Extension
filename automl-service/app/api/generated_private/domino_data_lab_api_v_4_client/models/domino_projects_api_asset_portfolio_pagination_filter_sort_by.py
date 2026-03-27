from enum import Enum


class DominoProjectsApiAssetPortfolioPaginationFilterSortBy(str, Enum):
    ASSETTYPE = "assetType"
    LAST24HOURS = "last24Hours"
    LASTUPDATED = "lastUpdated"
    NAME = "name"
    NUMBEROFVERSIONS = "numberOfVersions"
    OWNERNAME = "ownerName"
    PROJECTNAME = "projectName"

    def __str__(self) -> str:
        return str(self.value)
