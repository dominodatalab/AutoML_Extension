from __future__ import annotations
from enum import Enum


class BillingTagsSettingModeV1(str, Enum):
    DISABLED = "disabled"
    OPTIONAL = "optional"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
