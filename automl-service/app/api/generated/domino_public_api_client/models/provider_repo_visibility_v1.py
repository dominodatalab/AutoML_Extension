from enum import Enum


class ProviderRepoVisibilityV1(str, Enum):
    INTERNAL = "internal"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
