from __future__ import annotations
from enum import Enum


class GitServiceProviderV1(str, Enum):
    BITBUCKET = "Bitbucket"
    BITBUCKETSERVER = "BitbucketServer"
    GITHUB = "Github"
    GITHUBENTERPRISE = "GithubEnterprise"
    GITLAB = "GitLab"
    GITLABENTERPRISE = "GitLabEnterprise"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
