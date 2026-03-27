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

    @classmethod
    def _missing_(cls, value: object) -> GitServiceProviderV1 | None:
        if isinstance(value, str):
            lookup = {v.value.lower(): v for v in cls}
            return lookup.get(value.lower(), cls.UNKNOWN)
        return None

    def __str__(self) -> str:
        return str(self.value)
