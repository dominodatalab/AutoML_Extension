from __future__ import annotations
from enum import Enum


class CredentialsType(str, Enum):
    AWS = "AWS"
    HMAC = "HMAC"

    def __str__(self) -> str:
        return str(self.value)
