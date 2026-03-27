from enum import Enum


class DominoProjectsApiRepositoriesRequestsCreateRepoRequestServiceProvider(str, Enum):
    BITBUCKET = "bitbucket"
    BITBUCKETSERVER = "bitbucketServer"
    GITHUB = "github"
    GITHUBENTERPRISE = "githubEnterprise"
    GITLAB = "gitlab"
    GITLABENTERPRISE = "gitlabEnterprise"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
