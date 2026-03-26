from __future__ import annotations
from enum import Enum


class GitServiceProviderV1(str, Enum):
    BITBUCKET = "bitbucket"
    BITBUCKETSERVER = "bitbucketServer"
    GITHUB = "github"
    GITHUBENTERPRISE = "githubEnterprise"
    GITLAB = "gitLab"
    GITLABENTERPRISE = "gitLabEnterprise"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
